"""语义检索模块 - Embedding 生成 + 向量相似度搜索 + pgvector 集成"""

import asyncio
import hashlib
import logging
from typing import Optional

from src.config import settings

logger = logging.getLogger(__name__)


async def generate_embedding(text: str) -> list[float] | None:
    """通过 OpenAI Embedding API 生成文本向量"""
    api_key = settings.embedding_api_key or settings.openai_api_key
    base_url = settings.embedding_base_url or settings.openai_base_url or None
    if not api_key or not text.strip():
        return None
    try:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        resp = await client.embeddings.create(
            model=settings.embedding_model,
            input=text[:8000],
        )
        return resp.data[0].embedding
    except Exception as e:
        logger.warning(f"Embedding generation failed: {e}")
        return None


async def batch_generate_embeddings(texts: list[str]) -> list[list[float] | None]:
    """批量生成 embedding，每批最多 20 条"""
    api_key = settings.embedding_api_key or settings.openai_api_key
    base_url = settings.embedding_base_url or settings.openai_base_url or None
    if not api_key:
        return [None] * len(texts)
    try:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        results: list[list[float] | None] = []
        BATCH = 20
        for i in range(0, len(texts), BATCH):
            batch = [t[:8000] for t in texts[i : i + BATCH]]
            resp = await client.embeddings.create(
                model=settings.embedding_model, input=batch
            )
            for item in resp.data:
                results.append(item.embedding)
        return results
    except Exception as e:
        logger.warning(f"Batch embedding generation failed: {e}")
        return [None] * len(texts)


async def semantic_dedup(new_item, pg_storage=None):
    """语义去重：通过 embedding 相似度判断是否重复

    Args:
        new_item: 待检查的 CleanedItem
        pg_storage: PostgresStorage 实例

    Returns:
        更新后的 item（可能被标记为重复）
    """
    if pg_storage is None or not pg_storage.available:
        return new_item

    text = f"{new_item.title} {new_item.content[:500]}"
    embedding = await generate_embedding(text)
    if not embedding:
        return new_item

    # 在去重指纹库中搜索相似内容
    similar = await pg_storage.find_similar_fingerprints(
        embedding=embedding, top_k=3, threshold=0.85
    )

    if similar:
        best = similar[0]
        logger.info(
            f"Semantic dedup: '{new_item.title[:50]}...' matches {best['id']} "
            f"similarity {best['similarity']:.3f}"
        )
        new_item.is_duplicate = True
        new_item.duplicate_of = best["id"]
    else:
        # 新内容，保存指纹
        title_hash = hashlib.md5(new_item.title.lower().encode()).hexdigest()
        await pg_storage.save_dedup_fingerprint(
            item_id=new_item.id, title_hash=title_hash, embedding=embedding
        )

    return new_item


async def find_related(
    item, pg_storage=None, top_k: int = 5, threshold: float = 0.6
) -> list[dict]:
    """查找关联的历史新闻

    Args:
        item: ExtractedItem
        pg_storage: PostgresStorage 实例
        top_k: 返回最相关的 K 条
        threshold: 相似度阈值（低于去重阈值，找相关而非重复）

    Returns:
        关联的历史新闻列表
    """
    if pg_storage is None or not pg_storage.available:
        return []

    text = f"{item.title} {item.summary or item.content[:500]}"
    embedding = await generate_embedding(text)
    if not embedding:
        return []

    results = await pg_storage.search_similar(
        embedding=embedding, top_k=top_k, threshold=threshold
    )
    # 排除自身
    return [r for r in results if r["id"] != item.id]
