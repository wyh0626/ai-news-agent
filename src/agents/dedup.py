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
            logger.info("启用语义去重 (pgvector) ...")
            checked = []
            for item in candidates:
                result = await semantic_dedup(item, pg_storage=pg)
                if result.is_duplicate:
                    semantic_dupes += 1
                else:
                    checked.append(result)
            candidates = checked
    except Exception as e:
        logger.debug(f"语义去重不可用，跳过: {e}")

    logger.info(
        f"去重完成: {len(cleaned)} → {len(candidates)} 条 "
        f"(标题重复 {title_dupes}, 语义重复 {semantic_dupes})"
    )
    return {"deduped_items": candidates}
