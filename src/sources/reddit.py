"""Reddit 数据源适配器 - 通过 RSS feed 采集热门 AI 内容"""

import logging
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import feedparser
import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource
from src.tools.ai_filter import batch_filter_ai

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (Reddit RSS)"


def _strip_html(text: str) -> str:
    """移除 HTML 标签，保留纯文本"""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#\d+;", "", text)
    text = re.sub(r"&\w+;", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _extract_comments_count(summary: str) -> int:
    """从 RSS summary 中提取评论数"""
    m = re.search(r"(\d+)\s+comments?", summary)
    return int(m.group(1)) if m else 0


class RedditRSSSource(BaseSource):
    """通过 Reddit RSS feed 采集子版块热门内容

    两级过滤：
    1. 时间过滤：只保留 since 之后的帖子
    2. LLM 批量标题分类：精准判断是否 AI 相关
    """

    def __init__(self, subreddit: str, min_score: int = 50, limit: int = 50):
        self.subreddit = subreddit
        self.min_score = min_score
        self.url = f"https://www.reddit.com/r/{subreddit}/hot.rss?limit={limit}"

    @property
    def source_id(self) -> str:
        return f"reddit:{self.subreddit}"

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching Reddit r/{self.subreddit} (RSS hot) ...")
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
            logger.error(f"Fetch r/{self.subreddit} RSS failed: {e}")
            return []

        entries = feed.get("entries", [])
        if not entries:
            logger.info(f"r/{self.subreddit}: no entries in RSS")
            return []

        # 第一级过滤：时间
        candidates = []
        for entry in entries:
            # 解析发布时间
            published = None
            if entry.get("published"):
                try:
                    published = parsedate_to_datetime(entry["published"])
                    if published.tzinfo is None:
                        published = published.replace(tzinfo=timezone.utc)
                except Exception:
                    pass
            if since and published and published <= since:
                continue

            title = entry.get("title", "")
            link = entry.get("link", "")
            summary_html = entry.get("summary", "")
            content_text = _strip_html(summary_html)
            comments = _extract_comments_count(summary_html)
            author = entry.get("author", entry.get("author_detail", {}).get("name", ""))
            # 清理 author 前缀 /u/
            if author.startswith("/u/"):
                author = author[3:]

            # 从 link 中提取 post id
            post_id = ""
            id_match = re.search(r"/comments/(\w+)/", link)
            if id_match:
                post_id = id_match.group(1)

            candidates.append({
                "title": title,
                "content": content_text,
                "link": link,
                "author": author,
                "published": published,
                "comments": comments,
                "post_id": post_id,
            })

        if not candidates:
            logger.info(f"r/{self.subreddit}: no items after time filter")
            return []

        # 第二级过滤：LLM 判断是否 AI 相关
        titles = [c["title"] for c in candidates]
        descs = [c["content"][:80] for c in candidates]
        ai_indices = set(await batch_filter_ai(titles, descs))

        items: list[RawItem] = []
        for idx, c in enumerate(candidates):
            if idx not in ai_indices:
                continue
            # RSS 没有 upvote 数据，用评论数 * 10 作为粗略 score
            score = c["comments"] * 10 if c["comments"] > 0 else 1
            item = RawItem(
                source_type=SourceType.REDDIT,
                source_id=c["post_id"] or c["link"],
                title=c["title"],
                content=c["content"] or c["title"],
                url=c["link"],
                author=c["author"],
                published_at=c["published"],
                score=score,
                metadata={
                    "subreddit": self.subreddit,
                    "reddit_url": c["link"],
                    "num_comments": c["comments"],
                },
            )
            items.append(item)

        logger.info(
            f"r/{self.subreddit}: {len(items)} AI items "
            f"(RSS, LLM filtered {len(candidates)} → {len(items)})"
        )
        return items
