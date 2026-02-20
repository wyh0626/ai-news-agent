"""Reddit RSS 数据源适配器"""

import logging
from datetime import datetime, timezone
from time import mktime

import feedparser
import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (RSS Reader)"


class RedditRSSSource(BaseSource):
    """通过 RSS 采集 Reddit 子版块内容"""

    def __init__(self, subreddit: str):
        self.subreddit = subreddit
        self.url = f"https://www.reddit.com/r/{subreddit}.rss"

    @property
    def source_id(self) -> str:
        return f"reddit:{self.subreddit}"

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching Reddit r/{self.subreddit} ...")
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
            logger.error(f"Fetch r/{self.subreddit} failed: {e}")
            return []

        if feed.bozo and not feed.entries:
            logger.warning(f"RSS parse error: {feed.bozo_exception}")
            return []

        items: list[RawItem] = []
        for entry in feed.entries:
            published = self._parse_time(entry)
            if since and published and published <= since:
                continue

            content = entry.get("summary", "") or entry.get("content", [{}])[0].get("value", "")

            item = RawItem(
                source_type=SourceType.REDDIT,
                source_id=entry.get("id", entry.get("link", "")),
                title=entry.get("title", ""),
                content=content,
                url=entry.get("link", ""),
                author=entry.get("author", ""),
                published_at=published,
                metadata={
                    "subreddit": self.subreddit,
                    "categories": [t.get("term", "") for t in entry.get("tags", [])],
                },
            )
            items.append(item)

        logger.info(f"r/{self.subreddit}: fetched {len(items)} items")
        return items

    @staticmethod
    def _parse_time(entry) -> datetime | None:
        for field in ("published_parsed", "updated_parsed"):
            parsed = entry.get(field)
            if parsed:
                return datetime.fromtimestamp(mktime(parsed), tz=timezone.utc)
        return None
