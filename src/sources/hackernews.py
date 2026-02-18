"""Hacker News 数据源适配器 - 通过 hnrss 采集 AI 相关热门内容"""

import logging
from datetime import datetime, timezone
from time import mktime
from urllib.parse import quote

import feedparser
import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource
from src.tools.ai_filter import batch_filter_ai

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (RSS Reader)"

# hnrss 的核心 AI 搜索词（用 OR 连接，API 侧粗筛）
HN_SEARCH_TERMS = [
    "AI", "LLM", "GPT", "machine learning", "deep learning",
    "neural network", "transformer", "diffusion", "NLP",
    "OpenAI", "Anthropic", "Claude", "Gemini", "Llama",
]


class HackerNewsSource(BaseSource):
    """通过 hnrss 采集 AI 相关的 Hacker News 热门内容

    两级过滤：
    1. hnrss `q=` 参数：API 侧粗筛（核心固定词，极少变动）
    2. LLM 批量标题分类：精准判断是否 AI 相关（自动适应新术语）
    """

    def __init__(self, min_score: int = 50):
        self.min_score = min_score
        query = " OR ".join(HN_SEARCH_TERMS)
        self.url = (
            f"https://hnrss.org/newest"
            f"?points={min_score}"
            f"&count=50"
            f"&q={quote(query)}"
        )

    @property
    def source_id(self) -> str:
        return "hackernews"

    @property
    def default_interval(self) -> int:
        return 1800  # 30 min

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info("采集 Hacker News (AI 过滤) ...")
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
            logger.error(f"采集 HN 失败: {e}")
            return []

        # 先收集所有候选条目
        candidates: list[tuple[dict, datetime | None]] = []
        for entry in feed.entries:
            published = self._parse_time(entry)
            if since and published and published <= since:
                continue
            candidates.append((entry, published))

        if not candidates:
            logger.info("HN: 无新内容")
            return []

        # LLM 批量判断标题是否 AI 相关
        titles = [e.get("title", "") for e, _ in candidates]
        descs = [e.get("summary", "")[:80] for e, _ in candidates]
        ai_indices = set(await batch_filter_ai(titles, descs))

        items: list[RawItem] = []
        for idx, (entry, published) in enumerate(candidates):
            if idx not in ai_indices:
                continue

            hn_url = entry.get("comments", "")
            original_url = entry.get("link", "")

            item = RawItem(
                source_type=SourceType.HACKERNEWS,
                source_id=hn_url.split("=")[-1] if "id=" in hn_url else entry.get("id", ""),
                title=entry.get("title", ""),
                content=entry.get("summary", ""),
                url=original_url,
                author=entry.get("author", ""),
                published_at=published,
                metadata={
                    "hn_url": hn_url,
                    "original_url": original_url,
                },
            )
            items.append(item)

        logger.info(
            f"HN: {len(items)} 条 AI 资讯 "
            f"(>={self.min_score} points, "
            f"LLM 过滤 {len(candidates)} → {len(items)})"
        )
        return items

    @staticmethod
    def _parse_time(entry) -> datetime | None:
        for field in ("published_parsed", "updated_parsed"):
            parsed = entry.get(field)
            if parsed:
                return datetime.fromtimestamp(mktime(parsed), tz=timezone.utc)
        return None
