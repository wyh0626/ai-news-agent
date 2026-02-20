"""清空 PostgreSQL 中的历史数据（保留表结构）

用法: python scripts/clear_pg_data.py [--drop]
  默认: 清空所有表数据（TRUNCATE）
  --drop: 彻底删除所有表（DROP）
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import settings


TABLES = [
    "article_index",
    "topic_trends",
    "dedup_fingerprints",
    "source_metadata",
    "writing_preferences",
]


async def main():
    drop_mode = "--drop" in sys.argv

    if not settings.postgres_url:
        print("❌ 未配置 POSTGRES_URL，请检查 .env")
        return

    try:
        import psycopg

        conn = await psycopg.AsyncConnection.connect(settings.postgres_url)
    except Exception as e:
        print(f"❌ 连接失败: {e}")
        return

    async with conn:
        if drop_mode:
            print("🗑️  DROP 模式：删除所有表...")
            for table in TABLES:
                await conn.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
                print(f"  ✓ DROP {table}")
            await conn.commit()
            print("✅ 所有表已删除，下次运行 pipeline 会自动重建")
        else:
            print("🧹 TRUNCATE 模式：清空所有表数据...")
            for table in TABLES:
                try:
                    await conn.execute(f"TRUNCATE TABLE {table} CASCADE")
                    print(f"  ✓ TRUNCATE {table}")
                except Exception as e:
                    print(f"  ⚠ {table}: {e}")
            await conn.commit()
            print("✅ 所有表数据已清空，表结构保留")


if __name__ == "__main__":
    asyncio.run(main())
