"""Pipeline 入口脚本 - 运行一次完整的新闻采集→清洗→提取→撰稿流程"""

import asyncio
import logging
import sys
from pathlib import Path

# 确保 src 可被 import
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import settings
from src.graph.workflow import compile_graph


def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    # 降低第三方库日志
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)


async def main(sources: list[str] | None = None):
    setup_logging()
    logger = logging.getLogger("pipeline")

    logger.info("=" * 60)
    logger.info("AI News Agent Pipeline - v0.1")
    logger.info("=" * 60)

    graph = compile_graph()

    # 初始状态
    initial_state = {
        "raw_items": [],
        "cleaned_items": [],
        "deduped_items": [],
        "extracted_items": [],
        "article": None,
        "run_id": "",
        "run_started_at": "",
        "sources_config": sources or ["reddit", "hackernews", "arxiv", "github", "twitter"],
        "errors": [],
        "messages": [],
    }

    # 运行 pipeline
    result = await graph.ainvoke(initial_state)

    # 输出结果
    article = result.get("article")
    if article:
        logger.info(f"✅ 文章生成成功: {article.title}")
        logger.info(f"   包含 {article.item_count} 条新闻")
        logger.info(f"   输出目录: {settings.output_path}")
    else:
        extracted = result.get("extracted_items", [])
        logger.info(f"⏸️  本次未生成文章 (仅 {len(extracted)} 条新闻)")

    errors = result.get("errors", [])
    if errors:
        logger.warning(f"⚠️  运行过程中有 {len(errors)} 个错误:")
        for err in errors:
            logger.warning(f"   - {err}")

    return result


if __name__ == "__main__":
    # 支持命令行参数指定数据源
    sources = sys.argv[1:] if len(sys.argv) > 1 else None
    asyncio.run(main(sources))
