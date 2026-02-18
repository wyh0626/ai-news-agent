"""Collector Agent - 从各数据源并行采集原始数据"""

import asyncio
import logging
from datetime import datetime, timezone

from src.config import settings
from src.graph.state import PipelineState
from src.models import RawItem
from src.sources.arxiv import ArxivSource
from src.sources.github import GitHubTrendingSource
from src.sources.hackernews import HackerNewsSource
from src.sources.reddit import RedditRSSSource
from src.sources.twitter import TwitterSource
from src.sources.twitter_firecrawl import TwitterFirecrawlSource

logger = logging.getLogger(__name__)

# 数据源注册表
SOURCE_REGISTRY = {
    "reddit": lambda: [RedditRSSSource(sub) for sub in settings.subreddit_list],
    "hackernews": lambda: [HackerNewsSource(min_score=settings.hn_min_score)],
    "arxiv": lambda: [ArxivSource()],
    "github": lambda: [GitHubTrendingSource()],
    "twitter": lambda: (
        # 优先使用 Firecrawl 爬取 Twitter List
        [TwitterFirecrawlSource(
            api_key=settings.firecrawl_api_key,
            list_url=settings.twitter_list_url,
        )]
        if settings.firecrawl_api_key
        else (
            [TwitterSource(
                api_key=settings.twitter_api_key,
                kol_usernames=settings.twitter_kol_list.split(",") if settings.twitter_kol_list else None,
            )]
            if settings.twitter_api_key
            else []
        )
    ),
}


def _build_sources(source_ids: list[str]):
    """根据配置构建数据源实例列表"""
    sources = []
    for sid in source_ids:
        factory = SOURCE_REGISTRY.get(sid)
        if factory:
            sources.extend(factory())
        else:
            logger.warning(f"未知数据源: {sid}")
    return sources


async def _fetch_one(source, since: datetime | None) -> list[RawItem]:
    """单个数据源采集，带异常捕获"""
    try:
        return await source.fetch(since=since)
    except Exception as e:
        logger.error(f"{source.source_id} 采集失败: {e}")
        return []


def _smart_select(items_by_source: dict[str, list[RawItem]]) -> list[RawItem]:
    """智能选择策略：每源保底配额 + 按质量竞争剩余名额

    1. 每个源内按 score 降序排列
    2. 每个源先取 min_items_per_source 条（保底，不超过 max_items_per_source）
    3. 剩余名额从所有源的剩余条目中按 score 竞争
    4. 总数不超过 max_items_per_run
    """
    max_total = settings.max_items_per_run
    min_per_src = settings.min_items_per_source
    max_per_src = settings.max_items_per_source

    selected: list[RawItem] = []
    remaining_pool: list[RawItem] = []
    source_counts: dict[str, int] = {}

    for src_id, items in items_by_source.items():
        # 源内按 score 降序
        items.sort(key=lambda x: x.score, reverse=True)
        # 保底配额
        guaranteed = items[:min(min_per_src, max_per_src, len(items))]
        selected.extend(guaranteed)
        source_counts[src_id] = len(guaranteed)
        # 剩余进入竞争池
        remaining_pool.extend(items[len(guaranteed):])

    # 竞争剩余名额
    remaining_pool.sort(key=lambda x: x.score, reverse=True)
    for item in remaining_pool:
        if len(selected) >= max_total:
            break
        # 检查该源是否已达上限
        src_key = item.source_type.value
        if source_counts.get(src_key, 0) >= max_per_src:
            continue
        selected.append(item)
        source_counts[src_key] = source_counts.get(src_key, 0) + 1

    # 日志：各源入选数量
    for src_id, count in sorted(source_counts.items()):
        logger.info(f"  {src_id}: {count} 条入选")

    return selected


async def collector_node(state: PipelineState) -> dict:
    """Collector 节点：并行采集多个数据源，智能配额分配"""
    source_ids = state.get("sources_config", ["reddit"])
    sources = _build_sources(source_ids)

    if not sources:
        logger.warning("没有配置任何数据源")
        return {"raw_items": [], "errors": ["没有配置任何数据源"]}

    logger.info(f"开始采集, 数据源: {[s.source_id for s in sources]}")

    # 并行采集
    tasks = [_fetch_one(s, since=None) for s in sources]
    results = await asyncio.gather(*tasks)

    # 按源分组
    items_by_source: dict[str, list[RawItem]] = {}
    total_fetched = 0
    for source, items in zip(sources, results):
        src_key = source.source_id.split(":")[0]  # "reddit:LocalLLaMA" → "reddit"
        items_by_source.setdefault(src_key, []).extend(items)
        total_fetched += len(items)

    logger.info(f"采集原始数据 {total_fetched} 条, 来自 {len(items_by_source)} 类数据源")

    # 智能选择
    selected = _smart_select(items_by_source)

    logger.info(f"智能筛选完成: {total_fetched} → {len(selected)} 条")
    return {"raw_items": selected}
