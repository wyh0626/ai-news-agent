import asyncio
import copy
import html
import io
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs

import httpx
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from src.intake import outbox
from src.intake.app import create_app
from src.intake.digest import build_digest, day_window, previous_day, publication_day
from src.intake.models import BilingualBatch
from src.intake.store import Store
from src.intake.telegram import Telegram, caption, deliver_one


@pytest.fixture
def payload():
    return json.loads((Path(__file__).parents[1] / "examples/grok-bilingual.json").read_text())


@pytest.fixture
def client(tmp_path):
    with TestClient(create_app(tmp_path, local_demo=True)) as client:
        yield client


def upload(client, url, size=(1280, 600)):
    image = io.BytesIO()
    Image.new("RGB", size, "white").save(image, format="PNG")
    response = client.post(
        "/api/assets",
        params={"source_url": url, "kind": "x_original"},
        content=image.getvalue(),
        headers={"Content-Type": "image/png"},
    )
    assert response.status_code == 201
    return response.json()["asset_id"]


def test_bilingual_flow_with_optional_screenshot(client, payload):
    payload["items"][0]["screenshot_asset_id"] = upload(client, payload["items"][0]["tweet_url"])
    response = client.post("/api/v2/news", json=payload)
    assert response.status_code == 202, response.text
    ids = response.json()["accepted"]
    assert len(ids) == 2
    assert client.get("/healthz").json() == {
        "status": "ok",
        "mode": "local-demo",
        "screenshots": "provided-only",
        "telegram_enabled": False,
        "worker": False,
    }
    assert client.app.state.store.claim() is None
    rows = client.get("/api/items").json()["items"]
    assert all(r["state"] == "ready" and r["attempts"] == 0 for r in rows)
    assert {r["screenshot_status"] for r in rows} == {"skipped", "grok_x_original"}
    zh = client.get("/api/feed/zh").json()["items"]
    en = client.get("/api/feed/en").json()["items"]
    assert [n["id"] for n in zh] == [n["id"] for n in en]
    assert all(n["summary"] and n["event_key"] for n in en)
    assert en[0]["title"] != zh[0]["title"]
    jobs = client.get("/api/telegram/outbox").json()
    assert jobs["enabled"] is False and len(jobs["items"]) == 2
    assert all(j["attempts"] == 0 and j["status"] == "pending" for j in jobs["items"])
    preview = client.get(f"/api/items/{ids[0]}/telegram-preview").json()
    assert preview["sent"] is False and preview["has_image"]
    assert payload["items"][0]["summary_zh"] in preview["caption_html"]
    assert payload["items"][0]["body_zh"] not in preview["caption_html"]


def test_retry_dedup_and_changed_translation_no_double_queue(client, payload):
    assert len(client.post("/api/v2/news", json=payload).json()["accepted"]) == 2
    assert client.post("/api/v2/news", json=payload).json()["replayed"]
    payload["run_id"] = "another-run"
    payload["items"][0]["body_en"] += " Changed draft."
    result = client.post("/api/v2/news", json=payload).json()
    assert not result["accepted"] and len(result["duplicates"]) == 2
    assert result["duplicates"][0]["needs_review"]
    assert len(outbox.list_jobs(client.app.state.store)) == 2
    payload["items"][0]["summary_en"] += " New summary."
    assert client.post("/api/v2/news", json=payload).status_code == 409


def test_parallel_batch_retry_enqueues_exactly_once(tmp_path, payload):
    store = Store(tmp_path / "db.sqlite3")
    batch = BilingualBatch.model_validate(payload)
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(lambda _: store.ingest(batch, bilingual=True), range(12)))
    assert sum(not r["replayed"] for r in results) == 1
    assert len(outbox.list_jobs(store)) == 2


@pytest.mark.parametrize(
    "mutate",
    [
        lambda n: n.pop("body_en"),
        lambda n: n.update(story_type="external", screenshot_asset_id="0" * 64),
        lambda n: n.update(tweet_url=None),
        lambda n: n.update(published_at="2026-11-09T11:00:00"),
        lambda n: n.update(uncertainties=["尚待核实"], uncertainties_en=[]),
        lambda n: n.update(summary_zh="字" * 241),
        lambda n: n.update(image_url="https://example.org/not-an-upload.png"),
    ],
)
def test_v2_rejects_invalid_input_before_queueing(client, payload, mutate):
    mutate(payload["items"][0])
    assert client.post("/api/v2/news", json=payload).status_code == 422
    assert not outbox.list_jobs(client.app.state.store)


def test_invalid_second_asset_rolls_back_news_and_outbox(client, payload):
    n = payload["items"][1]
    n.update(
        story_type="x", tweet_url="https://x.com/demo/status/102", screenshot_asset_id="0" * 64
    )
    assert client.post("/api/v2/news", json=payload).status_code == 422
    assert client.app.state.store.list_news() == []
    assert outbox.list_jobs(client.app.state.store) == []
    assert client.app.state.store.get_batch(payload["run_id"]) is None


def test_screenshot_cannot_be_of_another_cited_tweet(client, payload):
    n = payload["items"][0]
    other = "https://x.com/other/status/300"
    n["sources"].append({"label": "Other post", "url": other})
    n["screenshot_asset_id"] = upload(client, other)
    assert client.post("/api/v2/news", json=payload).status_code == 422


def test_date_only_unknown_time_and_openapi(client, payload):
    payload["items"][0]["published_at"] = None
    payload["items"][0]["published_date"] = "2026-11-08"
    response = client.post("/api/v2/news", json=payload)
    news_id = response.json()["accepted"][0]
    n = client.get(f"/api/items/{news_id}").json()["news"]
    assert n["published_at"] is None and n["published_date"] == "2026-11-08"
    assert "2026-11-08" in client.get(f"/api/items/{news_id}/markdown").text
    schema = client.get("/openapi.json").json()
    assert schema["paths"]["/api/v2/news"]["post"]["security"]
    required = schema["components"]["schemas"]["BilingualNews"]["required"]
    assert "summary_zh" in required and "body_en" in required
    assert "published_at" not in required


def test_v2_endpoints_require_token(tmp_path, payload):
    with TestClient(create_app(tmp_path, token="t" * 32)) as client:
        assert client.post("/api/v2/news", json=payload).status_code == 401
        assert client.get("/api/feed/en").status_code == 401
        assert client.get("/api/telegram/outbox").status_code == 401


def test_caption_safe_and_bounded(payload):
    news = payload["items"][0]
    news.update(
        title_zh="<script>" + "😀" * 200, summary_zh="😀" * 240, uncertainties=["未核实" * 150]
    )
    news["sources"] = [{"label": "<来源>" * 40, "url": 'https://example.org/?a=1&b="test"'}] * 12
    text = caption(news)
    assert "<script>" not in text and "&lt;script&gt;" in text
    assert "&quot;test&quot;" in text
    plain = html.unescape(re.sub("<[^>]*>", "", text))
    assert len(plain.encode("utf-16-le")) // 2 <= 1024
    assert "待核实" not in plain


def run_sender(store, directory, handler):
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            return await deliver_one(store, directory, Telegram("TEST_ONLY", "@demo", client))

    return asyncio.run(run())


@pytest.mark.parametrize(
    "image_size,method,field",
    [
        (None, "sendMessage", None),
        ((1280, 600), "sendPhoto", "photo"),
        ((200, 5000), "sendDocument", "document"),
    ],
)
def test_telegram_payload_and_persisted_sent_state(
    client, payload, tmp_path, image_size, method, field
):
    payload["items"] = payload["items"][:1]
    if image_size:
        payload["items"][0]["screenshot_asset_id"] = upload(
            client, payload["items"][0]["tweet_url"], image_size
        )
    client.post("/api/v2/news", json=payload)
    calls = []

    def handler(request):
        calls.append(request)
        assert request.url.path.endswith("/" + method)
        if field:
            assert f'name="{field}"'.encode() in request.content
            assert payload["items"][0]["summary_zh"].encode() in request.content
        else:
            fields = parse_qs(request.content.decode())
            assert payload["items"][0]["summary_zh"] in fields["text"][0]
            assert fields["chat_id"] == ["@demo"]
        return httpx.Response(200, json={"ok": True, "result": {"message_id": 42}})

    store = client.app.state.store
    assert run_sender(store, tmp_path, handler)
    assert not run_sender(Store(store.path), tmp_path, handler)
    assert len(calls) == 1
    job = outbox.list_jobs(store)[0]
    assert job["status"] == "sent" and job["message_id"] == 42


def test_telegram_timeout_is_uncertain_and_never_blindly_retried(client, payload, tmp_path):
    payload["items"] = payload["items"][:1]
    client.post("/api/v2/news", json=payload)

    def handler(request):
        raise httpx.ReadTimeout("test only", request=request)

    store = client.app.state.store
    assert run_sender(store, tmp_path, handler)
    assert not run_sender(store, tmp_path, handler)
    assert outbox.list_jobs(store)[0]["status"] == "uncertain"


def test_telegram_known_rate_limit_retries_only_after_delay(client, payload, tmp_path):
    payload["items"] = payload["items"][:1]
    client.post("/api/v2/news", json=payload)
    store = client.app.state.store

    def handler(request):
        return httpx.Response(429, json={"ok": False, "parameters": {"retry_after": 120}})

    assert run_sender(store, tmp_path, handler)
    assert outbox.list_jobs(store)[0]["status"] == "pending"
    assert not run_sender(store, tmp_path, handler)
    for _ in range(4):
        with store.connect() as db:
            db.execute("UPDATE telegram_outbox SET next_try=0")
        assert run_sender(store, tmp_path, handler)
    assert outbox.list_jobs(store)[0]["status"] == "failed"
    assert not run_sender(store, tmp_path, handler)


def test_crashed_delivery_goes_to_review_on_restart(client, payload):
    payload["items"] = payload["items"][:1]
    client.post("/api/v2/news", json=payload)
    store = client.app.state.store
    assert outbox.claim(store)
    with store.connect() as db:
        db.execute("UPDATE telegram_outbox SET lease_until=0")
    assert outbox.claim(Store(store.path)) is None
    assert outbox.list_jobs(store)[0]["status"] == "uncertain"


def frontmatter(path):
    lines = Path(path).read_text().splitlines()[1:-1]
    return {key: json.loads(value) for key, value in (line.split(": ", 1) for line in lines)}


def test_daily_eight_oclock_boundaries_and_shared_image(client, payload, tmp_path):
    payload["items"][0]["screenshot_asset_id"] = upload(client, payload["items"][0]["tweet_url"])
    ids = client.post("/api/v2/news", json=payload).json()["accepted"]
    store = client.app.state.store
    start, end = day_window("2026-11-08")
    # Include both edges correctly; receipt date is independent of source publication date.
    with store.connect() as db:
        db.execute("UPDATE news SET created=? WHERE id=?", (start, ids[0]))
        db.execute("UPDATE news SET created=? WHERE id=?", (end - 0.001, ids[1]))
    old = copy.deepcopy(payload)
    old["run_id"] = "outside-window"
    for i, n in enumerate(old["items"]):
        n.update(
            event_key=f"outside-{i}",
            tweet_url=None,
            story_type="external",
            title_zh=f"另一则测试新闻{i}",
            screenshot_asset_id=None,
            sources=[{"label": "Test", "url": f"https://example.org/outside/{i}"}],
        )
    outside = client.post("/api/v2/news", json=old).json()["accepted"]
    with store.connect() as db:
        db.execute("UPDATE news SET created=? WHERE id=?", (start - 0.001, outside[0]))
        db.execute("UPDATE news SET created=? WHERE id=?", (end, outside[1]))
    result = build_digest(store, tmp_path, tmp_path / "site", "2026-11-08")
    assert result["count"] == 2 and result["images"] == 1
    assert len(result["asset_files"]) == 1
    zh, en = [frontmatter(p) for p in result["files"]]
    assert zh["pairSlug"] == "grok-daily-2026-11-08-en"
    assert en["pairSlug"] == "grok-daily-2026-11-08-zh"
    assert zh["digestItems"][0]["image"] == en["digestItems"][0]["image"]
    assert zh["digestItems"][1]["image"] is None
    assert en["digestItems"][0]["body"] == payload["items"][0]["body_en"]
    assert zh["receiptWindowStart"] == "2026-11-07T08:00:00+08:00"
    assert zh["receiptWindowEnd"] == "2026-11-08T08:00:00+08:00"
    with Image.open(result["asset_files"][0]) as image:
        assert image.format == "WEBP" and image.width <= 1280
    before = [Path(p).read_bytes() for p in result["files"] + result["asset_files"]]
    assert build_digest(store, tmp_path, tmp_path / "site", "2026-11-08") == result
    assert before == [Path(p).read_bytes() for p in result["files"] + result["asset_files"]]


def test_previous_day_handles_utc_and_month_boundary():
    assert previous_day(datetime.fromisoformat("2026-11-30T17:00:00+00:00")) == "2026-11-30"
    assert (
        day_window("2026-11-08")[0]
        == datetime.fromisoformat("2026-11-07T00:00:00+00:00").timestamp()
    )


def test_publication_day_uses_last_closed_window_across_months():
    assert publication_day(datetime.fromisoformat("2026-12-01T07:59:59+08:00")) == "2026-11-30"
    assert publication_day(datetime.fromisoformat("2026-12-01T08:00:00+08:00")) == "2026-12-01"
    assert publication_day(datetime.fromisoformat("2026-12-01T00:00:00+00:00")) == "2026-12-01"


def test_supplement_keeps_receipt_time_and_is_not_republished_tomorrow(client, payload, tmp_path):
    ids = client.post("/api/v2/news", json=payload).json()["accepted"]
    store = client.app.state.store
    _, cutoff = day_window("2026-11-10")
    with store.connect() as db:
        db.execute("UPDATE news SET created=? WHERE id=?", (cutoff - 60, ids[0]))
        db.execute("UPDATE news SET created=? WHERE id=?", (cutoff + 3600, ids[1]))
    assert build_digest(store, tmp_path, tmp_path / "site", "2026-11-10")["count"] == 1
    preview = build_digest(
        store, tmp_path, tmp_path / "site", "2026-11-10", supplement_ids=[ids[1]]
    )
    assert preview["count"] == 2
    assert frontmatter(preview["files"][0])["supplementCount"] == 1
    # Preview alone must not suppress a story from its normal receipt window.
    assert build_digest(store, tmp_path, tmp_path / "site", "2026-11-11")["count"] == 1
    (tmp_path / "publication-overrides.json").write_text(json.dumps({ids[1]: "2026-11-10"}))
    assert build_digest(store, tmp_path, tmp_path / "site", "2026-11-10")["count"] == 2
    assert build_digest(store, tmp_path, tmp_path / "site", "2026-11-11")["count"] == 0
    with store.connect() as db:
        assert (
            db.execute("SELECT created FROM news WHERE id=?", (ids[1],)).fetchone()[0]
            == cutoff + 3600
        )
    with pytest.raises(ValueError, match="different issue"):
        build_digest(store, tmp_path, tmp_path / "site", "2026-11-11", supplement_ids=[ids[1]])
    with pytest.raises(ValueError, match="not an accepted"):
        build_digest(store, tmp_path, tmp_path / "site", "2026-11-10", supplement_ids=["unknown"])


def test_legacy_route_not_in_v2_digest(client, payload, tmp_path):
    payload.pop("schema_version")
    assert client.post("/webhooks/grok", json=payload).status_code == 202
    day = datetime.now().astimezone().date().isoformat()
    result = build_digest(client.app.state.store, tmp_path, tmp_path / "site", day)
    assert result["count"] == 0 and result["files"] == []
    assert client.get("/api/feed/zh").json()["items"] == []
    assert client.get("/api/feed/en").json()["items"] == []
