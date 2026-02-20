"""Dedup Agent - 深度去重节点（规则 + 语义双重去重）"""

import logging

from src.graph.state import PipelineState
from src.models import CleanedItem

logger = logging.getLogger(__name__)


async def dedup_node(state: PipelineState) -> dict:
    """Dedup 节点：规则去重 + 语义去重（当 PostgreSQL 可用时）

    1. 先过滤 Cleaner 阶段标记的标题级重复
    2. 再通过 embedding 相似度做语义去重（需要 PG + API Key）
    """
    cleaned = state.get("cleaned_items", [])
    if not cleaned:
        return {"deduped_items": []}

    # Step 1: 过滤标题级重复
    candidates: list[CleanedItem] = [item for item in cleaned if not item.is_duplicate]
    title_dupes = len(cleaned) - len(candidates)

    # Step 2: 语义去重（尝试连接 PostgreSQL）
    semantic_dupes = 0
    try:
        from src.storage.postgres import get_postgres
        from src.memory.semantic import semantic_dedup

        pg = await get_postgres()
        if pg.available:
            logger.info("Semantic dedup enabled (pgvector) ...")
            checked = []
            for item in candidates:
                result = await semantic_dedup(item, pg_storage=pg)
                if result.is_duplicate:
                    semantic_dupes += 1
                else:
                    checked.append(result)
            candidates = checked
    except Exception as e:
        logger.debug(f"Semantic dedup unavailable, skipping: {e}")

    logger.info(
        f"Dedup done: {len(cleaned)} → {len(candidates)} items "
        f"(title dupes: {title_dupes}, semantic dupes: {semantic_dupes})"
    )
    return {"deduped_items": candidates}
