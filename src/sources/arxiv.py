"""ArXiv RSS 数据源适配器 - 采集 AI 相关论文（LLM 过滤）"""

import logging
import re
from datetime import datetime, timezone
from time import mktime

import feedparser
import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource
from src.tools.ai_filter import batch_filter_ai

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (RSS Reader)"


class ArxivSource(BaseSource):
    """通过 RSS 采集 ArXiv AI 相关论文

    已限定 cs.AI/cs.LG/cs.CL 分类，额外通过 LLM 批量标题分类：
    - 过滤掉纯理论/纯数学论文
    - 自动适应新术语，无需维护关键词表
    """

    def __init__(self, categories: list[str] | None = None):
        self.categories = categories or ["cs.AI", "cs.LG", "cs.CL"]
        self.urls = [f"https://rss.arxiv.org/rss/{cat}" for cat in self.categories]

    @property
    def source_id(self) -> str:
        return "arxiv"

    @property
    def default_interval(self) -> int:
        return 21600  # 6 hours

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching ArXiv {self.categories} ...")
        # 第一步：从各分类 RSS 收集候选论文
        candidates: list[dict] = []  # {entry, arxiv_id, title, abstract, published}
        seen_ids: set[str] = set()

        for url in self.urls:
            try:
                async with httpx.AsyncClient(
                    timeout=30,
                    headers={"User-Agent": USER_AGENT},
                    follow_redirects=True,
                ) as client:
                    resp = await client.get(url)
                    resp.raise_for_status()
                feed = feedparser.parse(resp.text)
            except Exception as e:
                logger.error(f"Fetch {url} failed: {e}")
                continue

            for entry in feed.entries:
                published = self._parse_time(entry)
                if since and published and published <= since:
                    continue

                arxiv_id = self._extract_arxiv_id(entry.get("link", ""))
                if arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)

                candidates.append({
                    "entry": entry,
                    "arxiv_id": arxiv_id,
                    "title": self._clean_title(entry.get("title", "")),
                    "abstract": entry.get("summary", ""),
                    "published": published,
                })

        if not candidates:
            logger.info("ArXiv: no new papers")
            return []

        # 第二步：LLM 批量判断是否实用 AI 论文
        titles = [c["title"] for c in candidates]
        descs = [c["abstract"][:100] for c in candidates]
        ai_indices = set(await batch_filter_ai(titles, descs))

        # 第三步：构建结果
        all_items: list[RawItem] = []
        for idx, c in enumerate(candidates):
            if idx not in ai_indices:
                continue

            entry = c["entry"]
            item = RawItem(
                source_type=SourceType.ARXIV,
                source_id=c["arxiv_id"] or entry.get("id", ""),
                title=c["title"],
                content=c["abstract"],
                url=entry.get("link", ""),
                author=entry.get("author", ""),
                published_at=c["published"],
                metadata={
                    "categories": [t.get("term", "") for t in entry.get("tags", [])],
                },
            )
            all_items.append(item)

        logger.info(
            f"ArXiv: {len(all_items)} AI-related papers "
            f"(LLM filtered {len(candidates)} → {len(all_items)})"
        )
        return all_items

    @staticmethod
    def _extract_arxiv_id(url: str) -> str:
        match = re.search(r"(\d{4}\.\d{4,5})", url)
        return match.group(1) if match else url

    @staticmethod
    def _clean_title(title: str) -> str:
        return re.sub(r"\s+", " ", title).strip()

    @staticmethod
    def _parse_time(entry) -> datetime | None:
        for field in ("published_parsed", "updated_parsed"):
            parsed = entry.get(field)
            if parsed:
                return datetime.fromtimestamp(mktime(parsed), tz=timezone.utc)
        return None
