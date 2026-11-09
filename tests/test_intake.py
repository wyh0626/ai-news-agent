import asyncio
import copy
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest
from fastapi.testclient import TestClient

from src.intake.app import create_app
from src.intake.models import Batch, canonical_tweet
from src.intake.render import export_daily
from src.intake.store import Store
from src.intake.worker import process_one


@pytest.fixture
def payload():
    return json.loads((Path(__file__).parents[1] / "examples/grok-webhook.json").read_text())


@pytest.fixture
def client(tmp_path):
    with TestClient(create_app(tmp_path, local_demo=True, run_worker=False)) as client:
        yield client


def test_idempotent_retry_and_conflict(client, payload):
    first = client.post("/webhooks/grok", json=payload)
    assert first.status_code == 202
    retry = client.post("/webhooks/grok", json=payload).json()
    assert retry["replayed"] and retry["accepted"] == first.json()["accepted"]
    payload["items"][0]["body_zh"] += "更新"
    assert client.post("/webhooks/grok", json=payload).status_code == 409
    assert len(client.get("/api/items").json()["items"]) == 2


def test_alias_dedup_and_changed_content_retained(client, payload):
    client.post("/webhooks/grok", json=payload)
    payload["run_id"] = "second-run"
    payload["items"] = payload["items"][:1]
    payload["items"][0]["tweet_url"] = "https://twitter.com/renamed/status/20?s=20"
    payload["items"][0]["body_zh"] += "新增事实待审核"
    reply = client.post("/webhooks/grok", json=payload).json()
    assert not reply["accepted"]
    assert reply["duplicates"][0]["needs_review"]
    assert (
        client.get("/api/runs/second-run")
        .json()["request"]["items"][0]["body_zh"]
        .endswith("待审核")
    )


def test_source_tracking_and_event_dedup(client, payload):
    payload["items"] = payload["items"][1:]
    n = payload["items"][0]
    n["sources"] = [{"label": "文章", "url": "https://example.org/article?utm_source=x&a=1"}]
    client.post("/webhooks/grok", json=payload)
    payload["run_id"] = "source-repeat"
    n["title_zh"] = "另一个中文标题"
    n["event_key"] = "other-event-key"
    n["sources"][0]["url"] = "https://example.org/article?a=1&utm_medium=y#intro"
    r = client.post("/webhooks/grok", json=payload).json()
    assert r["duplicates"][0]["reason"] == "source"
    payload["run_id"] = "event-repeat"
    n["event_key"] = "demo-web-source-20261107"
    n["sources"][0]["url"] = "https://different.example/story"
    assert client.post("/webhooks/grok", json=payload).json()["duplicates"][0]["reason"] == "event"


def test_concurrent_ingestion_is_atomic(tmp_path, payload):
    store = Store(tmp_path / "db.sqlite3")

    def ingest(i):
        p = copy.deepcopy(payload)
        p["run_id"] = f"run-{i}"
        return store.ingest(Batch.model_validate(p))

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(ingest, range(12)))
    assert sum(len(r["accepted"]) for r in results) == 2
    assert len(store.list_news()) == 2


@pytest.mark.parametrize(
    "url",
    [
        "https://x.com.evil.org/u/status/1",
        "http://127.0.0.1/admin",
        "https://x.com/u/status/1/../../admin",
        "https://user:pass@x.com/u/status/1",
        "https://x.com:9000/u/status/1",
        "file:///etc/passwd",
    ],
)
def test_reject_non_tweet_urls(url):
    with pytest.raises(ValueError):
        canonical_tweet(url)


def test_input_boundaries(client, payload):
    p = copy.deepcopy(payload)
    p["items"][0]["published_at"] = "2026-11-07T10:00:00"
    assert client.post("/webhooks/grok", json=p).status_code == 422
    p = copy.deepcopy(payload)
    p["items"][0]["sources"][0]["url"] = "javascript:alert(1)"
    assert client.post("/webhooks/grok", json=p).status_code == 422
    assert (
        client.post(
            "/webhooks/grok", content="x" * 1_000_001, headers={"Content-Type": "application/json"}
        ).status_code
        == 413
    )
    assert client.post("/webhooks/grok", content=json.dumps(payload)).status_code == 415
    assert (
        client.post(
            "/webhooks/grok", json=payload, headers={"Origin": "https://evil.example"}
        ).status_code
        == 403
    )


def test_auth_fail_closed_and_openapi(tmp_path, payload):
    with pytest.raises(ValueError):
        create_app(tmp_path, token="")
    with TestClient(create_app(tmp_path, token="t" * 32, run_worker=False)) as client:
        assert client.post("/webhooks/grok", json=payload).status_code == 401
        assert client.get("/api/items").status_code == 401
        assert (
            client.post(
                "/webhooks/grok", json=payload, headers={"Authorization": "Bearer " + "t" * 32}
            ).status_code
            == 202
        )
        schema = client.get("/openapi.json").json()
        assert "News" in schema["components"]["schemas"]
        assert schema["paths"]["/webhooks/grok"]["post"]["requestBody"]["required"]


def test_worker_retries_survive_restart_and_recover_lease(tmp_path, payload):
    store = Store(tmp_path / "news.sqlite3")
    payload["items"] = payload["items"][:1]
    news_id = store.ingest(Batch.model_validate(payload))["accepted"][0]

    async def failed(*args):
        raise RuntimeError("native_translation_unavailable")

    for attempt in range(3):
        asyncio.run(process_one(store, tmp_path, capture_fn=failed))
        store = Store(store.path)
        with store.connect() as db:
            db.execute("UPDATE news SET next_try=0")
    row = store.get(news_id)
    assert row["state"] == "needs_review" and row["attempts"] == 3 and not row["image"]
    assert store.retry(news_id)
    abandoned = store.claim()
    with store.connect() as db:
        db.execute("UPDATE news SET lease_until=0")
    fresh = store.claim()
    assert fresh["id"] == news_id and fresh["owner"] != abandoned["owner"]
    store.finish(abandoned, status="original")
    assert store.get(news_id)["state"] == "processing"
    store.finish(fresh, status="not_applicable")
    assert store.get(news_id)["state"] == "ready"


def test_last_attempt_crash_goes_to_review(tmp_path, payload):
    store = Store(tmp_path / "news.sqlite3")
    store.ingest(Batch.model_validate(payload))
    with store.connect() as db:
        db.execute("UPDATE news SET state='processing',attempts=3,lease_until=0")
    assert store.claim() is None
    assert all(r["state"] == "needs_review" for r in store.list_news())


def test_worker_export_images_and_escape_markup(tmp_path, payload):
    store = Store(tmp_path / "news.sqlite3")
    payload["items"][0]["body_zh"] += "<script>alert(1)</script> ![x](https://evil.example/x)"
    store.ingest(Batch.model_validate(payload))

    async def captured(url, out, mode):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(b"fixture-image")
        return "native_zh"

    while asyncio.run(process_one(store, tmp_path, capture_fn=captured)):
        pass
    rows = store.list_news()
    assert all(r["state"] == "ready" for r in rows)
    day = datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()
    result = export_daily(store, day, tmp_path, tmp_path / "out", tmp_path / "site")
    assert result["count"] == 2 and result["images"] == 1
    article = Path(result["path"]).read_text()
    assert 'lang: "zh"' in article and "pubDate:" in article
    assert "<script>" not in article and "![x]" not in article
    assert len(list((tmp_path / "site/public/news-shots").glob("*.png"))) == 1
    assert len(list((tmp_path / "site/src/content/blog").glob("*.md"))) == 1
