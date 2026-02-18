"""MongoDB 存储层 - 原始数据和清洗后数据的持久化"""

import logging
from datetime import datetime, timezone
from typing import Optional

from src.config import settings
from src.models import CleanedItem, ExtractedItem, RawItem

logger = logging.getLogger(__name__)


class MongoStorage:
    """MongoDB 存储管理器"""

    def __init__(self, mongo_url: str | None = None):
        self.mongo_url = mongo_url or settings.mongo_url
        self._client = None
        self._db = None

    async def connect(self):
        """建立 MongoDB 连接"""
        try:
            from motor.motor_asyncio import AsyncIOMotorClient

            self._client = AsyncIOMotorClient(self.mongo_url)
            self._db = self._client.ainews
            # 创建索引
            await self._db.raw_items.create_index("source_id", unique=True)
            await self._db.raw_items.create_index("fetched_at")
            await self._db.cleaned_items.create_index("id", unique=True)
            await self._db.extracted_items.create_index("id", unique=True)
            await self._db.extracted_items.create_index("published_at")
            logger.info("MongoDB 连接成功")
        except ImportError:
            logger.warning("motor 未安装，MongoDB 存储不可用。pip install motor")
            self._db = None
        except Exception as e:
            logger.error(f"MongoDB 连接失败: {e}")
            self._db = None

    async def close(self):
        if self._client:
            self._client.close()

    @property
    def available(self) -> bool:
        return self._db is not None

    # ── Raw Items ────────────────────────────────────────

    async def save_raw_items(self, items: list[RawItem]) -> int:
        """保存原始采集数据，返回新增数量"""
        if not self.available or not items:
            return 0
        saved = 0
        for item in items:
            doc = item.model_dump(mode="json")
            try:
                await self._db.raw_items.update_one(
                    {"source_id": item.source_id},
                    {"$set": doc},
                    upsert=True,
                )
                saved += 1
            except Exception as e:
                logger.debug(f"保存 raw_item 失败: {e}")
        logger.info(f"MongoDB: 保存 {saved}/{len(items)} 条原始数据")
        return saved

    async def get_recent_source_ids(self, source_type: str, limit: int = 200) -> set[str]:
        """获取最近的 source_id 集合，用于增量采集"""
        if not self.available:
            return set()
        cursor = self._db.raw_items.find(
            {"source_type": source_type},
            {"source_id": 1},
        ).sort("fetched_at", -1).limit(limit)
        return {doc["source_id"] async for doc in cursor}

    # ── Cleaned Items ────────────────────────────────────

    async def save_cleaned_items(self, items: list[CleanedItem]) -> int:
        if not self.available or not items:
            return 0
        saved = 0
        for item in items:
            doc = item.model_dump(mode="json")
            try:
                await self._db.cleaned_items.update_one(
                    {"id": item.id}, {"$set": doc}, upsert=True
                )
                saved += 1
            except Exception as e:
                logger.debug(f"保存 cleaned_item 失败: {e}")
        return saved

    # ── Extracted Items ──────────────────────────────────

    async def save_extracted_items(self, items: list[ExtractedItem]) -> int:
        if not self.available or not items:
            return 0
        saved = 0
        for item in items:
            doc = item.model_dump(mode="json")
            try:
                await self._db.extracted_items.update_one(
                    {"id": item.id}, {"$set": doc}, upsert=True
                )
                saved += 1
            except Exception as e:
                logger.debug(f"保存 extracted_item 失败: {e}")
        return saved

    async def get_extracted_items_by_date(
        self, start: datetime, end: datetime
    ) -> list[dict]:
        """获取日期范围内的提取数据"""
        if not self.available:
            return []
        cursor = self._db.extracted_items.find(
            {"published_at": {"$gte": start.isoformat(), "$lte": end.isoformat()}}
        )
        return [doc async for doc in cursor]

    # ── Articles ─────────────────────────────────────────

    async def save_article(self, article_data: dict) -> bool:
        if not self.available:
            return False
        try:
            await self._db.articles.update_one(
                {"date": article_data["date"]},
                {"$set": article_data},
                upsert=True,
            )
            return True
        except Exception as e:
            logger.error(f"保存文章失败: {e}")
            return False


# 全局单例
_mongo: Optional[MongoStorage] = None


async def get_mongo() -> MongoStorage:
    global _mongo
    if _mongo is None:
        _mongo = MongoStorage()
        await _mongo.connect()
    return _mongo
