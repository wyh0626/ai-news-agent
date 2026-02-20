"""通用 RSS 数据源适配器 - 支持任意 RSS/Atom Feed（AI 博客等）"""

import logging
from datetime import datetime, timezone
from time import mktime

import feedparser
import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (RSS Reader)"

# 预置的 AI 博客 RSS 源
AI_BLOG_FEEDS = {
    "openai_blog": "https://openai.com/blog/rss.xml",
    "deepmind_blog": "https://deepmind.google/blog/rss.xml",
    "huggingface_blog": "https://huggingface.co/blog/feed.xml",
    "pytorch_blog": "https://pytorch.org/blog/feed.xml",
    "ollama_blog": "https://ollama.com/blog/rss",
}


class GenericRSSSource(BaseSource):
    """通用 RSS 数据源，可对接任意 RSS/Atom Feed"""

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    @property
    def source_id(self) -> str:
        return f"rss:{self.name}"

    @property
    def default_interval(self) -> int:
        return 3600  # 1 hour

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching RSS [{self.name}] ...")
        try:
            async with httpx.AsyncClient(
                timeout=30,
                headers={"User-Agent": USER_AGENT},
                follow_redirects=True,
            ) as client:
                resp = await client.get(self.url)
                resp.raise_for_status()
            feed = feedparser.parse(resp.text)
        except Exception as e:
            logger.error(f"Fetch [{self.name}] failed: {e}")
            return []

        if feed.bozo and not feed.entries:
            logger.warning(f"RSS [{self.name}] parse error: {feed.bozo_exception}")
            return []

        items: list[RawItem] = []
        for entry in feed.entries:
            published = self._parse_time(entry)
            if since and published and published <= since:
                continue

            content = ""
            if entry.get("content"):
                content = entry["content"][0].get("value", "")
            elif entry.get("summary"):
                content = entry["summary"]
            elif entry.get("description"):
                content = entry["description"]

            item = RawItem(
                source_type=SourceType.RSS,
                source_id=entry.get("id", entry.get("link", "")),
                title=entry.get("title", ""),
                content=content,
                url=entry.get("link", ""),
                author=entry.get("author", ""),
                published_at=published,
                metadata={
                    "feed_name": self.name,
                    "feed_url": self.url,
                    "tags": [t.get("term", "") for t in entry.get("tags", [])],
                },
            )
            items.append(item)

        logger.info(f"RSS [{self.name}]: fetched {len(items)} items")
        return items

    @staticmethod
    def _parse_time(entry) -> datetime | None:
        for field in ("published_parsed", "updated_parsed"):
            parsed = entry.get(field)
            if parsed:
                return datetime.fromtimestamp(mktime(parsed), tz=timezone.utc)
        return None


def get_ai_blog_sources() -> list[GenericRSSSource]:
    """获取预置的 AI 博客 RSS 源列表"""
    return [GenericRSSSource(name, url) for name, url in AI_BLOG_FEEDS.items()]
