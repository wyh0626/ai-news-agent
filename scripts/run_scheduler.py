"""定时调度服务 (v1.0) - 基于 APScheduler 定时触发 Pipeline"""

import asyncio
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import settings


def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("apscheduler").setLevel(logging.INFO)


logger = logging.getLogger("scheduler")


async def run_daily_pipeline():
    """每日 Pipeline: 全量采集 + 生成日报"""
    from scripts.run_pipeline import main as pipeline_main

    logger.info("⏰ 触发每日 Pipeline ...")
    try:
        await pipeline_main(sources=["reddit", "hackernews", "arxiv", "github", "rss"])
    except Exception as e:
        logger.error(f"每日 Pipeline 失败: {e}")


async def run_frequent_pipeline():
    """高频 Pipeline: 仅采集 Reddit + HN（不一定生成文章）"""
    from scripts.run_pipeline import main as pipeline_main

    logger.info("⏰ 触发高频采集 ...")
    try:
        await pipeline_main(sources=["reddit", "hackernews"])
    except Exception as e:
        logger.error(f"高频采集失败: {e}")


async def run_trend_report():
    """周报: 生成趋势分析"""
    logger.info("⏰ 触发周趋势报告 ...")
    try:
        from src.agents.trend_analyzer import generate_trend_report

        report = await generate_trend_report(days=7)
        if report:
            output_dir = settings.output_path
            from datetime import datetime, timezone

            date_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
            filepath = output_dir / f"ai-weekly-trend-{date_str}.md"
            filepath.write_text(report, encoding="utf-8")
            logger.info(f"趋势报告已保存: {filepath}")
        else:
            logger.info("趋势报告数据不足，跳过")
    except Exception as e:
        logger.error(f"趋势报告失败: {e}")


async def run_memory_maintenance():
    """定时维护: 清理过期记忆"""
    logger.info("⏰ 触发记忆维护 ...")
    try:
        from src.memory.maintenance import cleanup_expired_memories, compress_topic_trends

        await cleanup_expired_memories(days=30)
        await compress_topic_trends()
    except Exception as e:
        logger.error(f"记忆维护失败: {e}")


def main():
    setup_logging()

    try:
        from apscheduler.schedulers.asyncio import AsyncIOScheduler
        from apscheduler.triggers.cron import CronTrigger
        from apscheduler.triggers.interval import IntervalTrigger
    except ImportError:
        logger.error("APScheduler 未安装。请运行: pip install apscheduler")
        sys.exit(1)

    scheduler = AsyncIOScheduler()

    # 每日全量 Pipeline: 每天早上 8:00 UTC
    scheduler.add_job(
        run_daily_pipeline,
        CronTrigger(hour=8, minute=0),
        id="daily_pipeline",
        name="每日全量 Pipeline",
        misfire_grace_time=3600,
    )

    # 高频采集: 每 30 分钟
    scheduler.add_job(
        run_frequent_pipeline,
        IntervalTrigger(minutes=30),
        id="frequent_pipeline",
        name="高频采集 (Reddit + HN)",
        misfire_grace_time=600,
    )

    # 周趋势报告: 每周日 20:00 UTC
    scheduler.add_job(
        run_trend_report,
        CronTrigger(day_of_week="sun", hour=20, minute=0),
        id="weekly_trend",
        name="周趋势报告",
        misfire_grace_time=3600,
    )

    # 记忆维护: 每天凌晨 3:00 UTC
    scheduler.add_job(
        run_memory_maintenance,
        CronTrigger(hour=3, minute=0),
        id="memory_maintenance",
        name="记忆维护",
        misfire_grace_time=3600,
    )

    logger.info("=" * 60)
    logger.info("AI News Agent Scheduler - v1.0")
    logger.info("=" * 60)
    logger.info("已注册调度任务:")
    for job in scheduler.get_jobs():
        logger.info(f"  - [{job.id}] {job.name} | {job.trigger}")
    logger.info("=" * 60)

    scheduler.start()

    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.info("调度器关闭")
        scheduler.shutdown()


if __name__ == "__main__":
    main()
