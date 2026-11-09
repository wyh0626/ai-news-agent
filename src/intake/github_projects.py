"""Retain the existing Trending RSS source without LLM or embedding calls."""

import json
import re
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

import httpx

from .digest import BJT, atomic_write

RSS_URL = "https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml"
AI_TERMS = re.compile(
    r"\b(ai|llms?|gpt\w*|chatgpt|claude|codex|gemini|deepseek|ollama|"
    r"langchain|langgraph|transformers|pytorch|tensorflow|diffusion|rag|mcp)\b"
    r"|artificial intelligence|machine learning|deep learning|language model"
    r"|人工智能|大模型|机器学习|深度学习|智能体",
    re.I,
)


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def parse_projects(content):
    if len(content) > 8 * 1024 * 1024:
        raise ValueError("Trending feed exceeds size limit")
    root = ET.fromstring(content)
    result, seen = [], set()
    for entry in root.findall("./channel/item")[:50]:
        link = (entry.findtext("link") or "").strip()
        url = urlsplit(link)
        name = url.path.strip("/")
        if url.scheme != "https" or url.netloc != "github.com":
            continue
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", name) or name.casefold() in seen:
            continue
        # RSS embeds the entire README after <hr>. Keep only the short description.
        raw = re.split(r"<hr\b", entry.findtext("description") or "", maxsplit=1, flags=re.I)[0]
        first = re.search(r"<p\b[^>]*>(.*?)</p>", raw, re.I | re.S)
        parser = PlainText()
        parser.feed(first[1] if first else raw)
        description = " ".join(" ".join(parser.parts).split())[:600]
        if not description or not AI_TERMS.search(name + " " + description):
            continue
        seen.add(name.casefold())
        result.append(
            {"name": name, "url": "https://github.com/" + name, "description": description}
        )
    return result


def daily_projects(data_dir: Path, day: str, *, client=None, now=None, exclude_urls=()):
    """Freeze one snapshot per issue; retries do not consume requests or change the issue."""
    directory = data_dir / "github-trending"
    snapshot = directory / f"{day}.json"
    if snapshot.exists():
        return json.loads(snapshot.read_text())
    today = (now or datetime.now(BJT)).astimezone(BJT).date()
    if date.fromisoformat(day) != today:
        return {"items": [], "status": "historical_snapshot_unavailable", "source": RSS_URL}
    previous = set()
    for offset in range(1, 4):
        path = directory / f"{today - timedelta(days=offset)}.json"
        if path.exists():
            previous.update(p["name"].casefold() for p in json.loads(path.read_text())["items"])
    excluded = {u.lower().rstrip("/").split("?")[0] for u in exclude_urls}
    own_client = client is None
    client = client or httpx.Client(timeout=30, follow_redirects=True)
    try:
        response = client.get(RSS_URL, headers={"User-Agent": "AI-Daily/2.0 (RSS Reader)"})
        response.raise_for_status()
        items = [
            p
            for p in parse_projects(response.content)
            if p["name"].casefold() not in previous and p["url"].lower() not in excluded
        ][:8]
        result = {"items": items, "status": "ok", "source": RSS_URL}
        atomic_write(snapshot, json.dumps(result, ensure_ascii=False))
        return result
    except (httpx.HTTPError, ET.ParseError, ValueError):
        # News still publishes. Never substitute a fabricated or stale Trending list.
        return {"items": [], "status": "fetch_failed", "source": RSS_URL}
    finally:
        if own_client:
            client.close()
