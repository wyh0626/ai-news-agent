"""Reddit 数据源适配器 - 通过 JSON API 采集热门 AI 内容"""

import logging
from datetime import datetime, timezone

import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource
from src.tools.ai_filter import batch_filter_ai

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (Reddit JSON)"


class RedditRSSSource(BaseSource):
    """通过 Reddit JSON API 采集子版块热门内容

    两级过滤：
    1. min_score：只保留 upvotes >= min_score 的帖子
    2. LLM 批量标题分类：精准判断是否 AI 相关
    """

    def __init__(self, subreddit: str, min_score: int = 50, limit: int = 50):
        self.subreddit = subreddit
        self.min_score = min_score
        self.url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"

    @property
    def source_id(self) -> str:
        return f"reddit:{self.subreddit}"

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching Reddit r/{self.subreddit} (hot, min_score={self.min_score}) ...")
        try:
            async with httpx.AsyncClient(
                timeout=30,
                headers={"User-Agent": USER_AGENT},
                follow_redirects=True,
            ) as client:
                resp = await client.get(self.url)
                resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error(f"Fetch r/{self.subreddit} failed: {e}")
            return []

        posts = data.get("data", {}).get("children", [])
        if not posts:
            logger.info(f"r/{self.subreddit}: no posts returned")
            return []

        # 第一级过滤：时间 + upvotes 分数
        candidates = []
        for post in posts:
            d = post.get("data", {})
            if d.get("stickied"):
                continue
            score = d.get("score", 0)
            if score < self.min_score:
                continue
            created = d.get("created_utc")
            published = datetime.fromtimestamp(created, tz=timezone.utc) if created else None
            if since and published and published <= since:
                continue
            candidates.append((d, published))

        if not candidates:
            logger.info(f"r/{self.subreddit}: no items after score/time filter")
            return []

        # 第二级过滤：LLM 判断是否 AI 相关
        titles = [d.get("title", "") for d, _ in candidates]
        descs = [d.get("selftext", "")[:80] for d, _ in candidates]
        ai_indices = set(await batch_filter_ai(titles, descs))

        items: list[RawItem] = []
        for idx, (d, published) in enumerate(candidates):
            if idx not in ai_indices:
                continue
            permalink = "https://www.reddit.com" + d.get("permalink", "")
            url = d.get("url", permalink)
            item = RawItem(
                source_type=SourceType.REDDIT,
                source_id=d.get("id", ""),
                title=d.get("title", ""),
                content=d.get("selftext", "") or d.get("title", ""),
                url=url,
                author=d.get("author", ""),
                published_at=published,
                score=d.get("score", 0),
                metadata={
                    "subreddit": self.subreddit,
                    "reddit_url": permalink,
                    "upvotes": d.get("score", 0),
                    "num_comments": d.get("num_comments", 0),
                },
            )
            items.append(item)

        logger.info(
            f"r/{self.subreddit}: {len(items)} AI items "
            f"(>={self.min_score} upvotes, LLM filtered {len(candidates)} → {len(items)})"
        )
        return items
