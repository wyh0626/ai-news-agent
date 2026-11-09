import asyncio
import hmac
import os
from contextlib import asynccontextmanager, suppress
from pathlib import Path
from urllib.parse import urlsplit
from typing import Literal

from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse
from pydantic import ValidationError

from .models import Batch, BilingualBatch, canonical_tweet, public_url
from . import outbox
from .telegram import Telegram, run_delivery, caption
from .assets import MAX_BYTES, save_png
from .render import news_markdown
from .store import Conflict, InvalidAsset, Store
from .worker import work_forever


def create_app(
    data_dir=None,
    *,
    local_demo=False,
    token=None,
    run_worker=False,
    mode="original",
    telegram=False,
):
    data_dir = Path(data_dir or os.getenv("NEWS_DATA_DIR", "data/grok-intake")).resolve()
    token = token if token is not None else os.getenv("NEWS_WEBHOOK_TOKEN", "")
    if not local_demo and len(token) < 32:
        raise ValueError("正式模式必须设置至少 32 字符的 NEWS_WEBHOOK_TOKEN")
    if mode not in {"native-zh", "original"}:
        raise ValueError("invalid screenshot mode")
    store = Store(data_dir / "news.sqlite3")

    sender = (
        Telegram(os.getenv("TELEGRAM_BOT_TOKEN", ""), os.getenv("TELEGRAM_CHANNEL_ID", ""))
        if telegram
        else None
    )

    @asynccontextmanager
    async def lifespan(app):
        task = asyncio.create_task(work_forever(store, data_dir, mode)) if run_worker else None
        delivery = asyncio.create_task(run_delivery(store, data_dir, sender)) if sender else None
        try:
            yield
        finally:
            if delivery:
                delivery.cancel()
                with suppress(asyncio.CancelledError):
                    await delivery
            if task:
                task.cancel()
                with suppress(asyncio.CancelledError):
                    await task

    app = FastAPI(title="AI Daily · Grok 新闻接收", version="2.0.0", lifespan=lifespan)
    app.state.store = store

    @app.middleware("http")
    async def boundary(request: Request, call_next):
        if local_demo:
            host = request.url.hostname
            peer = request.client.host if request.client else ""
            if host not in {"localhost", "127.0.0.1", "testserver"} or peer not in {
                "127.0.0.1",
                "::1",
                "testclient",
            }:
                return JSONResponse({"detail": "local demo accepts loopback only"}, status_code=403)
        if request.url.path.startswith("/api/") or request.url.path.startswith("/webhooks/"):
            if not local_demo:
                expected = ("Bearer " + token).encode()
                if not hmac.compare_digest(
                    request.headers.get("authorization", "").encode(), expected
                ):
                    return JSONResponse({"detail": "Unauthorized"}, status_code=401)
            origin = request.headers.get("origin")
            if origin and urlsplit(origin).netloc != request.headers.get("host"):
                return JSONResponse(
                    {"detail": "Cross-origin requests are disabled"}, status_code=403
                )
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        return response

    @app.get("/healthz")
    def health():
        return {
            "status": "ok",
            "mode": "local-demo" if local_demo else "authenticated",
            "screenshots": mode if run_worker else "provided-only",
            "telegram_enabled": telegram,
            "worker": run_worker,
        }

    @app.get("/")
    def index():
        return FileResponse(Path(__file__).with_name("index.html"))

    @app.post(
        "/webhooks/grok",
        status_code=202,
        openapi_extra={
            "requestBody": {
                "required": True,
                "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Batch"}}},
            }
        },
    )
    async def ingest(request: Request):
        return await receive(request, Batch)

    @app.post(
        "/api/v2/news",
        status_code=202,
        openapi_extra={
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {"schema": {"$ref": "#/components/schemas/BilingualBatch"}}
                },
            }
        },
    )
    async def bilingual_ingest(request: Request):
        return await receive(request, BilingualBatch)

    async def receive(request, model):
        if (
            request.headers.get("content-type", "").split(";")[0].strip().lower()
            != "application/json"
        ):
            raise HTTPException(415, "请使用 application/json")
        # Enforce limit while streaming, also for chunked requests lacking Content-Length.
        body = bytearray()
        async for chunk in request.stream():
            body.extend(chunk)
            if len(body) > 1_000_000:
                raise HTTPException(413, "每批最多 1 MB")
        try:
            batch = model.model_validate_json(bytes(body))
        except ValidationError as exc:
            return JSONResponse(
                {"detail": [{"field": list(e["loc"]), "message": e["msg"]} for e in exc.errors()]},
                status_code=422,
            )
        try:
            return store.ingest(batch, bilingual=model is BilingualBatch)
        except InvalidAsset as exc:
            raise HTTPException(422, str(exc)) from None
        except Conflict as exc:
            raise HTTPException(409, str(exc)) from None

    @app.post(
        "/api/assets",
        status_code=201,
        openapi_extra={
            "requestBody": {
                "required": True,
                "content": {"image/png": {"schema": {"type": "string", "format": "binary"}}},
            }
        },
    )
    async def upload_asset(
        request: Request,
        source_url: str = Query(max_length=2000),
        kind: Literal["x_original", "article_original"] = Query(),
    ):
        if request.headers.get("content-type", "").split(";")[0].strip().lower() != "image/png":
            raise HTTPException(415, "请直接发送 image/png 二进制文件，不是 JSON 或图片链接")
        try:
            source_url = (
                canonical_tweet(source_url) if kind == "x_original" else public_url(source_url)
            )
        except ValueError:
            raise HTTPException(422, "source_url 必须是实际截图页面的有效链接") from None
        body = bytearray()
        async for chunk in request.stream():
            body.extend(chunk)
            if len(body) > MAX_BYTES:
                raise HTTPException(413, "图片不能超过 8 MiB")
        try:
            asset = await asyncio.to_thread(save_png, bytes(body), source_url, kind, data_dir)
        except ValueError as exc:
            raise HTTPException(422, str(exc)) from None
        store.register_asset(asset)
        return {k: v for k, v in asset.items() if k != "filename"}

    @app.get("/api/items")
    def items():
        return {"items": store.list_news()}

    @app.get("/api/feed/{lang}")
    def feed(lang: Literal["zh", "en"]):
        result = []
        for row in store.list_bilingual():
            n = row["news"]
            if not n.get("title_" + lang):
                continue
            result.append(
                {
                    "id": row["id"],
                    "event_key": n.get("event_key"),
                    "title": n["title_" + lang],
                    "summary": n.get("summary_" + lang, ""),
                    "body": n["body_" + lang],
                    "sources": n["sources"],
                    "tweet_url": n["tweet_url"],
                    "published_at": n.get("published_at"),
                    "published_date": n.get("published_date"),
                    "uncertainties": n.get(
                        "uncertainties" if lang == "zh" else "uncertainties_en", []
                    ),
                    "image_url": f"/api/items/{row['id']}/image" if row["image"] else None,
                }
            )
        return {"lang": lang, "items": result}

    @app.get("/api/telegram/outbox")
    def telegram_outbox():
        return {"enabled": telegram, "items": outbox.list_jobs(store)}

    @app.get("/api/items/{news_id}/telegram-preview")
    def telegram_preview(news_id: str):
        item = get_item(news_id)
        return {
            "caption_html": caption(item["news"]),
            "has_image": bool(item["image"]),
            "sent": False,
        }

    @app.get("/api/runs/{run_id}")
    def batch(run_id: str):
        data = store.get_batch(run_id)
        if not data:
            raise HTTPException(404)
        return data

    def get_item(news_id):
        data = store.get(news_id)
        if not data:
            raise HTTPException(404)
        return data

    @app.get("/api/items/{news_id}")
    def item(news_id: str):
        return get_item(news_id)

    @app.get("/api/items/{news_id}/image")
    def image(news_id: str):
        item = get_item(news_id)
        if not item["image"]:
            raise HTTPException(404, "暂无截图")
        return FileResponse(data_dir / "images" / item["image"], media_type="image/png")

    @app.get("/api/items/{news_id}/markdown", response_class=PlainTextResponse)
    def markdown(news_id: str):
        return news_markdown(get_item(news_id))

    @app.post("/api/items/{news_id}/retry")
    def retry(news_id: str):
        get_item(news_id)
        if not store.retry(news_id):
            raise HTTPException(409, "仅待处理且未运行的截图可以重新排队")
        return {"state": "queued"}

    def schema():
        import json

        if not app.openapi_schema:
            result = get_openapi(title=app.title, version=app.version, routes=app.routes)
            components = result.setdefault("components", {})
            schemas = components.setdefault("schemas", {})
            for model_class in (Batch, BilingualBatch):
                model = json.loads(
                    json.dumps(model_class.model_json_schema()).replace(
                        "#/$defs/", "#/components/schemas/"
                    )
                )
                schemas.update(model.pop("$defs", {}))
                schemas[model_class.__name__] = model
            components["securitySchemes"] = {"WebhookBearer": {"type": "http", "scheme": "bearer"}}
            for route, methods in result["paths"].items():
                if route.startswith(("/api/", "/webhooks/")):
                    for operation in methods.values():
                        operation["security"] = [{"WebhookBearer": []}]
            app.openapi_schema = result
        return app.openapi_schema

    app.openapi = schema
    return app
