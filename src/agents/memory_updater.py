"""Memory Updater Agent - 在 Pipeline 末尾统一更新长期记忆"""

import logging
from datetime import datetime, timezone

from src.graph.state import PipelineState

logger = logging.getLogger(__name__)


async def update_memory_node(state: PipelineState) -> dict:
    """更新长期记忆：文章索引、话题热度、数据源元数据

    在图的最后一个节点统一更新，确保只有完整处理过的数据才进入长期记忆。
    """
    extracted = state.get("extracted_items", [])
    if not extracted:
        return {}

    # 尝试连接数据库
    pg = None
    mongo = None
    try:
        from src.storage.postgres import get_postgres
        pg = await get_postgres()
    except Exception:
        pass
    try:
        from src.storage.mongo import get_mongo
        mongo = await get_mongo()
    except Exception:
        pass

    # ── 保存到 MongoDB ──────────────────────────────────
    if mongo and mongo.available:
        await mongo.save_extracted_items(extracted)
        article = state.get("article")
        if article:
            await mongo.save_article({
                "title": article.title,
                "date": article.date,
                "item_count": article.item_count,
                "markdown_content": article.markdown_content,
                "created_at": datetime.now(tz=timezone.utc).isoformat(),
            })
        logger.info(f"MongoDB: 保存 {len(extracted)} 条提取数据")

    # ── 更新 PostgreSQL 长期记忆 ─────────────────────────
    if pg and pg.available:
        # 1. 更新文章索引 + embedding
        try:
            from src.memory.semantic import generate_embedding

            saved_count = 0
            for item in extracted:
                text = f"{item.title} {item.summary or item.content[:500]}"
                embedding = await generate_embedding(text)
                await pg.save_article_index(
                    article_id=item.id,
                    title=item.title,
                    summary=item.summary,
                    url=item.url,
                    source_type=item.source_type.value,
                    topics=item.topics,
                    entities=item.entities,
                    importance_score=item.importance_score,
                    published_at=item.published_at,
                    embedding=embedding,
                )
                saved_count += 1

            logger.info(f"PostgreSQL: 索引 {saved_count} 篇文章")
        except Exception as e:
            logger.warning(f"文章索引更新失败: {e}")

        # 2. 更新话题热度
        try:
            topic_counts: dict[str, int] = {}
            for item in extracted:
                for topic in item.topics:
                    topic_counts[topic] = topic_counts.get(topic, 0) + 1
            for topic, count in topic_counts.items():
                await pg.update_topic_trend(topic, count)
            logger.info(f"PostgreSQL: 更新 {len(topic_counts)} 个话题热度")
        except Exception as e:
            logger.warning(f"话题热度更新失败: {e}")

        # 3. 更新数据源元数据
        try:
            source_counts: dict[str, int] = {}
            for item in extracted:
                key = item.source_type.value
                source_counts[key] = source_counts.get(key, 0) + 1
            for source_id, count in source_counts.items():
                await pg.update_source_metadata(source_id, count)
        except Exception as e:
            logger.warning(f"数据源元数据更新失败: {e}")

    return {}
