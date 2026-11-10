"""Chinese news reports with source previews or an uploaded original screenshot."""

import asyncio
import html
import json
import logging
from pathlib import Path
from urllib.parse import urlsplit

import httpx
from PIL import Image

from . import outbox


def text_units(text):
    return len(text.encode("utf-16-le")) // 2


def clip(text, units):
    if text_units(text) <= units:
        return text
    result = []
    used = 0
    for char in text:
        cost = text_units(char)
        if used + cost > units - 1:
            break
        result.append(char)
        used += cost
    return "".join(result).rstrip() + ("…" if units > 0 else "")


def display_sources(news):
    sources = list(news["sources"])[:3]
    if news.get("tweet_url") and news["tweet_url"] not in [s["url"] for s in sources]:
        sources.append({"label": "原推文", "url": news["tweet_url"]})
    return sources


def caption(news, limit=4096):
    title = clip(news["title_zh"], 200)
    sources = display_sources(news)
    labels = [clip(s["label"], 48) for s in sources]
    links = "信源：" + " · ".join(
        f'<a href="{html.escape(s["url"], quote=True)}">{html.escape(label)}</a>'
        for s, label in zip(sources, labels)
    )
    reserved = text_units(title + "\n\n\n\n信源：" + " · ".join(labels))
    # Preserve the supplied report and paragraphs; only trim at Telegram's actual limit.
    body = clip(
        news.get("body_zh") or news.get("summary_zh", ""), max(0, limit - reserved)
    )
    return "\n\n".join(["<b>" + html.escape(title) + "</b>", html.escape(body), links])


def link_preview_options(news):
    sources = display_sources(news)
    url = news.get("tweet_url") if news.get("story_type") == "x" else None
    if not url:
        url = next(
            (
                s["url"]
                for s in sources
                if s.get("dedup", True)
                and urlsplit(s["url"]).hostname
                not in {"x.com", "twitter.com", "www.x.com", "www.twitter.com"}
            ),
            sources[0]["url"],
        )
    return {
        "is_disabled": False,
        "url": url,
        "prefer_large_media": True,
        "show_above_text": True,
    }


class Telegram:
    def __init__(self, token, chat_id, client=None):
        if not token or not chat_id:
            raise ValueError("Telegram requires bot token and channel ID in process configuration")
        self.token = token
        self.chat_id = chat_id
        self.client = client

    async def send(self, item, data_dir):
        data = {"chat_id": self.chat_id, "parse_mode": "HTML"}
        text = caption(item["news"], limit=1024 if item["image"] else 4096)
        method = "sendMessage"
        files = None
        if item["image"]:
            image = Path(data_dir) / "images" / item["image"]
            with Image.open(image) as im:
                width, height = im.size
            photo_ok = width + height <= 10000 and max(width, height) / min(width, height) <= 20
            method = "sendPhoto" if photo_ok else "sendDocument"
            field = "photo" if photo_ok else "document"
            files = {field: (image.name, image.read_bytes(), "image/png")}
            data["caption"] = text
        else:
            data["text"] = text
            data["link_preview_options"] = json.dumps(link_preview_options(item["news"]))
        # Bot tokens are part of Telegram URLs; never log HTTP request URLs or exceptions.
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)

        async def request(client):
            return await client.post(
                f"https://api.telegram.org/bot{self.token}/{method}", data=data, files=files
            )

        try:
            if self.client:
                response = await request(self.client)
            else:
                async with httpx.AsyncClient(timeout=45, follow_redirects=False) as client:
                    response = await request(client)
        except httpx.HTTPError:
            return {"status": "uncertain", "error": "network_outcome_unknown"}
        try:
            result = response.json()
        except ValueError:
            return {"status": "uncertain", "error": "invalid_telegram_response"}
        if response.status_code == 200 and result.get("ok") is True:
            message_id = result.get("result", {}).get("message_id")
            if isinstance(message_id, int):
                return {"status": "sent", "message_id": message_id}
            return {"status": "uncertain", "error": "missing_message_id"}
        if response.status_code == 429 or result.get("error_code") == 429:
            wait = result.get("parameters", {}).get("retry_after", 60)
            wait = min(max(wait, 1), 86400) if isinstance(wait, int) else 60
            return {"status": "pending", "error": "rate_limited", "retry_after": wait}
        if 400 <= response.status_code < 500 and result.get("ok") is False:
            return {"status": "failed", "error": "telegram_rejected_request"}
        return {"status": "uncertain", "error": "telegram_outcome_unknown"}


async def deliver_one(store, data_dir, sender):
    job = outbox.claim(store)
    if not job:
        return False
    try:
        result = await sender.send(store.get(job["news_id"]), data_dir)
    except asyncio.CancelledError:
        raise
    except Exception:
        result = {"status": "uncertain", "error": "delivery_exception"}
    if result["status"] == "pending" and job["attempts"] >= 5:
        result = {"status": "failed", "error": "retry_limit_reached"}
    outbox.finish(store, job, **result)
    return True


async def run_delivery(store, data_dir, sender):
    while True:
        try:
            await deliver_one(store, data_dir, sender)
        except asyncio.CancelledError:
            raise
        except Exception:
            logging.getLogger(__name__).error("Telegram queue iteration failed")
        await asyncio.sleep(2)
