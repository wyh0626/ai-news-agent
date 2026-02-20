"""PostgreSQL 存储层 - 长期记忆、语义检索、文章索引"""

import json
import logging
from datetime import datetime, timezone
from typing import Optional

from src.config import settings

logger = logging.getLogger(__name__)

# SQL DDL
INIT_SQL = """
-- 启用 pgvector 扩展
CREATE EXTENSION IF NOT EXISTS vector;

-- 文章索引表 (长期记忆)
CREATE TABLE IF NOT EXISTS article_index (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    summary TEXT DEFAULT '',
    url TEXT DEFAULT '',
    source_type TEXT DEFAULT '',
    topics TEXT[] DEFAULT '{}',
    entities TEXT[] DEFAULT '{}',
    importance_score FLOAT DEFAULT 5.0,
    published_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    embedding vector(1536)
);

-- 话题热度追踪表
CREATE TABLE IF NOT EXISTS topic_trends (
    id SERIAL PRIMARY KEY,
    topic TEXT NOT NULL,
    count INT DEFAULT 1,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    UNIQUE(topic, date)
);

-- 去重指纹表
CREATE TABLE IF NOT EXISTS dedup_fingerprints (
    id TEXT PRIMARY KEY,
    title_hash TEXT NOT NULL,
    embedding vector(1536),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 数据源元数据表
CREATE TABLE IF NOT EXISTS source_metadata (
    source_id TEXT PRIMARY KEY,
    last_fetch_at TIMESTAMPTZ,
    total_fetched INT DEFAULT 0,
    error_count INT DEFAULT 0,
    reliability_score FLOAT DEFAULT 1.0,
    config JSONB DEFAULT '{}'
);

-- 写作偏好表
CREATE TABLE IF NOT EXISTS writing_preferences (
    key TEXT PRIMARY KEY,
    value JSONB NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 索引
CREATE INDEX IF NOT EXISTS idx_article_index_published ON article_index(published_at DESC);
CREATE INDEX IF NOT EXISTS idx_article_index_topics ON article_index USING GIN(topics);
CREATE INDEX IF NOT EXISTS idx_article_embedding ON article_index USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
CREATE INDEX IF NOT EXISTS idx_dedup_embedding ON dedup_fingerprints USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
CREATE INDEX IF NOT EXISTS idx_topic_trends_date ON topic_trends(date DESC);
"""


class PostgresStorage:
    """PostgreSQL 存储管理器 - 长期记忆核心"""

    def __init__(self, postgres_url: str | None = None):
        self.postgres_url = postgres_url or settings.postgres_url
        self._pool = None

    async def connect(self):
        try:
            import psycopg_pool

            # keepalives 防止 Neon 等云数据库长时间运行后 SSL 连接断开
            connect_kwargs = {
                "keepalives": 1,
                "keepalives_idle": 30,
                "keepalives_interval": 10,
                "keepalives_count": 5,
            }
            self._pool = psycopg_pool.AsyncConnectionPool(
                self.postgres_url,
                min_size=1,
                max_size=5,
                open=False,
                kwargs=connect_kwargs,
                reconnect_timeout=30,
            )
            await self._pool.open()
            logger.info("PostgreSQL 连接成功")
        except ImportError:
            logger.warning("psycopg 未安装，PostgreSQL 存储不可用。pip install 'psycopg[binary]' psycopg-pool")
            self._pool = None
        except Exception as e:
            logger.error(f"PostgreSQL 连接失败: {e}")
            self._pool = None

    async def close(self):
        if self._pool:
            await self._pool.close()

    @property
    def available(self) -> bool:
        return self._pool is not None

    async def init_tables(self):
        """初始化数据库表"""
        if not self.available:
            return
        async with self._pool.connection() as conn:
            # 先创建 extension，再创建表（分开执行避免事务问题）
            await conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
            await conn.commit()
            # 创建表（跳过 ivfflat 索引如果数据量不够）
            for statement in INIT_SQL.split(";"):
                stmt = statement.strip()
                if not stmt:
                    continue
                try:
                    await conn.execute(stmt)
                except Exception as e:
                    if "ivfflat" in stmt.lower() and "does not exist" in str(e):
                        logger.debug(f"跳过 ivfflat 索引 (数据量不足): {e}")
                    else:
                        logger.warning(f"SQL 执行警告: {e}")
            await conn.commit()
        logger.info("PostgreSQL 表初始化完成")

    # ── 文章索引 (长期记忆) ────────────────────────────────

    async def save_article_index(
        self,
        article_id: str,
        title: str,
        summary: str,
        url: str,
        source_type: str,
        topics: list[str],
        entities: list[str],
        importance_score: float,
        published_at: datetime | None,
        embedding: list[float] | None = None,
    ):
        """保存文章到长期记忆索引"""
        if not self.available:
            return
        async with self._pool.connection() as conn:
            await conn.execute(
                """INSERT INTO article_index
                   (id, title, summary, url, source_type, topics, entities,
                    importance_score, published_at, embedding)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                   ON CONFLICT (id) DO UPDATE SET
                       title = EXCLUDED.title,
                       summary = EXCLUDED.summary,
                       embedding = EXCLUDED.embedding""",
                (
                    article_id, title, summary, url, source_type,
                    topics, entities, importance_score, published_at,
                    str(embedding) if embedding else None,
                ),
            )
            await conn.commit()

    async def search_similar(
        self, embedding: list[float], top_k: int = 5, threshold: float = 0.85
    ) -> list[dict]:
        """语义搜索：找到与给定 embedding 最相似的文章"""
        if not self.available or not embedding:
            return []
        async with self._pool.connection() as conn:
            rows = await conn.execute(
                """SELECT id, title, summary, url, source_type, topics,
                          1 - (embedding <=> %s::vector) AS similarity
                   FROM article_index
                   WHERE embedding IS NOT NULL
                   ORDER BY embedding <=> %s::vector
                   LIMIT %s""",
                (str(embedding), str(embedding), top_k),
            )
            results = []
            async for row in rows:
                sim = row[6]
                if sim >= threshold:
                    results.append({
                        "id": row[0], "title": row[1], "summary": row[2],
                        "url": row[3], "source_type": row[4], "topics": row[5],
                        "similarity": sim,
                    })
            return results

    # ── 去重指纹 ──────────────────────────────────────────

    async def save_dedup_fingerprint(
        self, item_id: str, title_hash: str, embedding: list[float] | None = None
    ):
        if not self.available:
            return
        async with self._pool.connection() as conn:
            await conn.execute(
                """INSERT INTO dedup_fingerprints (id, title_hash, embedding)
                   VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING""",
                (item_id, title_hash, str(embedding) if embedding else None),
            )
            await conn.commit()

    async def find_similar_fingerprints(
        self, embedding: list[float], top_k: int = 5, threshold: float = 0.85
    ) -> list[dict]:
        """语义去重：找相似指纹"""
        if not self.available or not embedding:
            return []
        async with self._pool.connection() as conn:
            rows = await conn.execute(
                """SELECT id, title_hash,
                          1 - (embedding <=> %s::vector) AS similarity
                   FROM dedup_fingerprints
                   WHERE embedding IS NOT NULL
                   ORDER BY embedding <=> %s::vector
                   LIMIT %s""",
                (str(embedding), str(embedding), top_k),
            )
            results = []
            async for row in rows:
                if row[2] >= threshold:
                    results.append({"id": row[0], "title_hash": row[1], "similarity": row[2]})
            return results

    # ── 话题热度 ──────────────────────────────────────────

    async def update_topic_trend(self, topic: str, count: int = 1):
        if not self.available:
            return
        async with self._pool.connection() as conn:
            await conn.execute(
                """INSERT INTO topic_trends (topic, count, date)
                   VALUES (%s, %s, CURRENT_DATE)
                   ON CONFLICT (topic, date)
                   DO UPDATE SET count = topic_trends.count + EXCLUDED.count""",
                (topic, count),
            )
            await conn.commit()

    async def get_trending_topics(self, days: int = 7, limit: int = 20) -> list[dict]:
        """获取最近 N 天的热门话题"""
        if not self.available:
            return []
        async with self._pool.connection() as conn:
            rows = await conn.execute(
                """SELECT topic, SUM(count) AS total_count,
                          COUNT(DISTINCT date) AS active_days
                   FROM topic_trends
                   WHERE date >= CURRENT_DATE - %s
                   GROUP BY topic
                   ORDER BY total_count DESC
                   LIMIT %s""",
                (days, limit),
            )
            return [
                {"topic": row[0], "count": row[1], "active_days": row[2]}
                async for row in rows
            ]

    # ── 数据源元数据 ──────────────────────────────────────

    async def update_source_metadata(
        self, source_id: str, fetched_count: int, had_error: bool = False
    ):
        if not self.available:
            return
        async with self._pool.connection() as conn:
            await conn.execute(
                """INSERT INTO source_metadata (source_id, last_fetch_at, total_fetched, error_count)
                   VALUES (%s, NOW(), %s, %s)
                   ON CONFLICT (source_id) DO UPDATE SET
                       last_fetch_at = NOW(),
                       total_fetched = source_metadata.total_fetched + EXCLUDED.total_fetched,
                       error_count = source_metadata.error_count + EXCLUDED.error_count""",
                (source_id, fetched_count, 1 if had_error else 0),
            )
            await conn.commit()


# 全局单例
_pg: Optional[PostgresStorage] = None


async def get_postgres() -> PostgresStorage:
    global _pg
    if _pg is None:
        _pg = PostgresStorage()
        await _pg.connect()
        await _pg.init_tables()
    return _pg
