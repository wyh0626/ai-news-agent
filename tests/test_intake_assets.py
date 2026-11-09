import hashlib
import io
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest
from fastapi.testclient import TestClient
from PIL import Image

from src.intake.app import create_app
from src.intake.models import Batch
from src.intake.render import export_daily


@pytest.fixture
def client(tmp_path):
    with TestClient(create_app(tmp_path, local_demo=True, run_worker=False)) as client:
        yield client


@pytest.fixture
def payload():
    return json.loads((Path(__file__).parents[1] / "examples/grok-webhook.json").read_text())


def png():
    out = io.BytesIO()
    Image.new("RGB", (1280, 720), "white").save(out, format="PNG")
    return out.getvalue()


def upload(client, url, kind="x_original", content=None):
    return client.post(
        "/api/assets",
        params={"source_url": url, "kind": kind},
        content=png() if content is None else content,
        headers={"Content-Type": "image/png"},
    )


def test_original_x_upload_reuse_and_no_browser_job(client, payload):
    response = upload(client, payload["items"][0]["tweet_url"])
    assert response.status_code == 201, response.text
    asset = response.json()
    assert (asset["width"], asset["height"]) == (1280, 720)
    assert upload(client, payload["items"][0]["tweet_url"]).json()["asset_id"] == asset["asset_id"]
    payload["items"] = payload["items"][:1]
    payload["items"][0]["screenshot_asset_id"] = asset["asset_id"]
    result = client.post("/webhooks/grok", json=payload)
    assert result.status_code == 202, result.text
    news_id = result.json()["accepted"][0]
    item = client.get("/api/items/" + news_id).json()
    assert item["state"] == "ready" and item["attempts"] == 0
    assert item["screenshot_status"] == "grok_x_original"
    assert client.app.state.store.claim() is None
    assert client.get("/api/items/" + news_id + "/image").content == png()
    assert client.post("/webhooks/grok", json=payload).json()["replayed"]


def test_article_source_binding_and_export(client, payload, tmp_path):
    url = "https://example.org/news/new-model?utm_source=x"
    asset = upload(client, url, "article_original").json()
    payload["items"] = payload["items"][:1]
    payload["items"][0]["sources"].append(
        {"label": "官方公告", "url": "https://example.org/news/new-model"}
    )
    payload["items"][0]["screenshot_asset_id"] = asset["asset_id"]
    response = client.post("/webhooks/grok", json=payload)
    assert response.status_code == 202, response.text
    news_id = response.json()["accepted"][0]
    assert "外部新闻原文截图" in client.get("/api/items/" + news_id + "/markdown").text
    day = datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()
    result = export_daily(
        client.app.state.store, day, tmp_path, tmp_path / "out", tmp_path / "site"
    )
    assert result["images"] == 1
    assert list((tmp_path / "site/public/news-shots").glob("*.png"))


def test_bad_assets_rejected_and_batch_rolled_back(client, payload):
    bad = upload(client, "https://x.com/another/status/99").json()
    payload["items"][1]["screenshot_asset_id"] = bad["asset_id"]
    assert client.post("/webhooks/grok", json=payload).status_code == 422
    assert client.get("/api/items").json()["items"] == []
    payload["items"][1]["screenshot_asset_id"] = "0" * 64
    assert client.post("/webhooks/grok", json=payload).status_code == 422


@pytest.mark.parametrize("data", [b"<svg><script/></svg>", b"\x89PNG\r\n\x1a\n", b""])
def test_reject_fake_png(client, data):
    assert upload(client, "https://x.com/jack/status/20", content=data).status_code == 422


def test_upload_limits_and_auth(client, tmp_path):
    assert (
        upload(
            client, "https://x.com/jack/status/20", content=b"x" * (8 * 1024 * 1024 + 1)
        ).status_code
        == 413
    )
    assert upload(client, "file:///etc/passwd", "article_original").status_code == 422
    assert upload(client, "https://example.org/news", "x_original").status_code == 422
    assert (
        client.post(
            "/api/assets",
            params={"source_url": "https://x.com/jack/status/20", "kind": "x_original"},
            json={"image_url": "https://example.org/image.png"},
        ).status_code
        == 415
    )
    with TestClient(create_app(tmp_path / "secure", token="z" * 32, run_worker=False)) as secured:
        assert upload(secured, "https://x.com/jack/status/20").status_code == 401


def test_legacy_payload_digest_unchanged(payload):
    model = Batch.model_validate(payload)
    legacy = model.model_dump(mode="json")
    for item in legacy["items"]:
        for key in (
            "screenshot_asset_id",
            "summary_zh",
            "title_en",
            "summary_en",
            "body_en",
            "uncertainties_en",
            "story_type",
            "published_date",
        ):
            del item[key]
    digest = hashlib.sha256(
        json.dumps(legacy, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()
    assert model.digest() == digest
