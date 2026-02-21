"""Product Hunt 数据源适配器 - 采集 AI 相关热门产品"""

import logging
from datetime import datetime, timezone

import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource
from src.tools.ai_filter import batch_filter_ai

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0"
GRAPHQL_URL = "https://api.producthunt.com/v2/api/graphql"

# 查询今日热门产品（无需 API key，使用公开端点）
QUERY = """
{
  posts(order: VOTES, first: 30) {
    edges {
      node {
        id
        name
        tagline
        description
        url
        votesCount
        commentsCount
        createdAt
        topics {
          edges {
            node { name }
          }
        }
        thumbnail { url }
      }
    }
  }
}
"""


class ProductHuntSource(BaseSource):
    """采集 Product Hunt 今日热门 AI 产品

    两级过滤：
    1. min_votes：只保留 votes >= min_votes 的产品
    2. LLM 批量标题分类：精准判断是否 AI 相关
    """

    def __init__(self, min_votes: int = 50, api_token: str | None = None):
        self.min_votes = min_votes
        self.api_token = api_token

    @property
    def source_id(self) -> str:
        return "producthunt"

    @property
    def default_interval(self) -> int:
        return 3600  # 1 hour

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching Product Hunt (min_votes={self.min_votes}) ...")

        headers = {
            "User-Agent": USER_AGENT,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self.api_token:
            headers["Authorization"] = f"Bearer {self.api_token}"

        try:
            async with httpx.AsyncClient(timeout=30, headers=headers) as client:
                resp = await client.post(
                    GRAPHQL_URL,
                    json={"query": QUERY},
                )
                resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error(f"Fetch Product Hunt failed: {e}")
            return []

        edges = data.get("data", {}).get("posts", {}).get("edges", [])
        if not edges:
            logger.warning("Product Hunt: no posts returned (may need API token)")
            return []

        # 第一级过滤：votes + 时间
        candidates = []
        for edge in edges:
            node = edge.get("node", {})
            votes = node.get("votesCount", 0)
            if votes < self.min_votes:
                continue
            created_str = node.get("createdAt", "")
            published: datetime | None = None
            if created_str:
                try:
                    published = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
                except ValueError:
                    pass
            if since and published and published <= since:
                continue
            candidates.append((node, published))

        if not candidates:
            logger.info("Product Hunt: no items after votes/time filter")
            return []

        # 第二级过滤：LLM 判断是否 AI 相关
        titles = [n.get("name", "") for n, _ in candidates]
        descs = [n.get("tagline", "")[:80] for n, _ in candidates]
        ai_indices = set(await batch_filter_ai(titles, descs))

        items: list[RawItem] = []
        for idx, (node, published) in enumerate(candidates):
            if idx not in ai_indices:
                continue
            thumbnail = (node.get("thumbnail") or {}).get("url", "")
            meta = {
                "votes": node.get("votesCount", 0),
                "num_comments": node.get("commentsCount", 0),
                "topics": [
                    e["node"]["name"]
                    for e in node.get("topics", {}).get("edges", [])
                ],
            }
            if thumbnail:
                meta["image"] = thumbnail

            item = RawItem(
                source_type=SourceType.PRODUCTHUNT,
                source_id=node.get("id", ""),
                title=node.get("name", ""),
                content=node.get("tagline", "") + "\n" + (node.get("description") or ""),
                url=node.get("url", ""),
                published_at=published,
                score=node.get("votesCount", 0),
                metadata=meta,
            )
            items.append(item)

        logger.info(
            f"Product Hunt: {len(items)} AI products "
            f"(>={self.min_votes} votes, LLM filtered {len(candidates)} → {len(items)})"
        )
        return items
