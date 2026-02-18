"""数据库初始化脚本 - 创建表、扩展和索引"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import settings


async def init_postgres():
    """初始化 PostgreSQL: pgvector 扩展 + 表结构"""
    from src.storage.postgres import PostgresStorage

    pg = PostgresStorage()
    await pg.connect()
    if not pg.available:
        print("❌ PostgreSQL 连接失败，请确认数据库是否启动")
        return False
    await pg.init_tables()
    await pg.close()
    print("✅ PostgreSQL 初始化完成")
    return True


async def init_mongo():
    """初始化 MongoDB: 创建集合和索引"""
    from src.storage.mongo import MongoStorage

    mongo = MongoStorage()
    await mongo.connect()
    if not mongo.available:
        print("❌ MongoDB 连接失败，请确认数据库是否启动")
        return False
    await mongo.close()
    print("✅ MongoDB 初始化完成")
    return True


async def main():
    print("=" * 50)
    print("AI News Agent - 数据库初始化")
    print("=" * 50)
    print(f"PostgreSQL: {settings.postgres_url}")
    print(f"MongoDB:    {settings.mongo_url}")
    print()

    pg_ok = await init_postgres()
    mongo_ok = await init_mongo()

    print()
    if pg_ok and mongo_ok:
        print("🎉 所有数据库初始化完成")
    else:
        print("⚠️  部分数据库初始化失败，请检查连接配置")


if __name__ == "__main__":
    asyncio.run(main())
