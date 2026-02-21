"""HuggingFace Daily Papers 数据源适配器"""

import logging
from datetime import datetime, timezone

import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0"
API_URL = "https://huggingface.co/api/daily_papers"


class HuggingFacePapersSource(BaseSource):
    """采集 HuggingFace 每日精选论文

    社区投票 upvotes 代表真实热度，全部为 AI 相关，无需 LLM 过滤。
    """

    def __init__(self, min_upvotes: int = 5):
        self.min_upvotes = min_upvotes

    @property
    def source_id(self) -> str:
        return "huggingface"

    @property
    def default_interval(self) -> int:
        return 3600  # 1 hour

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching HuggingFace Daily Papers (min_upvotes={self.min_upvotes}) ...")
        try:
            async with httpx.AsyncClient(
                timeout=30,
                headers={"User-Agent": USER_AGENT},
                follow_redirects=True,
            ) as client:
                resp = await client.get(API_URL)
                resp.raise_for_status()
            papers = resp.json()
        except Exception as e:
            logger.error(f"Fetch HuggingFace Papers failed: {e}")
            return []

        items: list[RawItem] = []
        for entry in papers:
            paper_info = entry.get("paper", {})

            # upvotes 在 paper 子对象里
            upvotes = paper_info.get("upvotes", 0)
            if upvotes < self.min_upvotes:
                continue

            # 时间：用论文被提交到 daily 的时间
            published_str = (
                paper_info.get("submittedOnDailyAt")
                or entry.get("publishedAt")
                or ""
            )
            published: datetime | None = None
            if published_str:
                try:
                    published = datetime.fromisoformat(published_str.replace("Z", "+00:00"))
                except ValueError:
                    pass
            # HF Papers 是每日批次数据，不做 since 过滤（避免因时区/延迟漏掉当日论文）

            paper_id = paper_info.get("id", "")
            # title/summary 在顶层（更完整），fallback 到 paper 子对象
            title = entry.get("title") or paper_info.get("title", "")
            abstract = entry.get("summary") or paper_info.get("summary", "")
            arxiv_url = f"https://arxiv.org/abs/{paper_id}" if paper_id else ""
            hf_url = f"https://huggingface.co/papers/{paper_id}" if paper_id else ""

            if not title:
                continue

            item = RawItem(
                source_type=SourceType.HUGGINGFACE,
                source_id=paper_id,
                title=title,
                content=abstract[:500] if abstract else title,
                url=hf_url or arxiv_url,
                author=", ".join(
                    a.get("name", "") for a in paper_info.get("authors", [])[:3]
                ),
                published_at=published,
                score=upvotes,
                metadata={
                    "upvotes": upvotes,
                    "arxiv_url": arxiv_url,
                    "hf_url": hf_url,
                },
            )
            items.append(item)

        logger.info(f"HuggingFace Papers: {len(items)} papers (>={self.min_upvotes} upvotes)")
        return items
