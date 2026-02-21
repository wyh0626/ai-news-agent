"""Cleaner Agent - 将原始数据标准化为统一格式"""

import hashlib
import logging
import re
from html import unescape

from src.graph.state import PipelineState
from src.models import CleanedItem, RawItem

logger = logging.getLogger(__name__)


def _strip_html(text: str) -> str:
    """移除 HTML 标签"""
    text = unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def _normalize_whitespace(text: str) -> str:
    """规范化空白字符"""
    return re.sub(r"\s+", " ", text).strip()


def _compute_quality_score(item: RawItem) -> float:
    """基于规则的质量评分 (0-1)"""
    score = 0.3  # 基础分

    # 标题长度加分
    if 10 < len(item.title) < 200:
        score += 0.1

    # 内容长度加分
    content_len = len(item.content)
    if content_len > 50:
        score += 0.1
    if content_len > 200:
        score += 0.1

    # 平台互动分数加分
    if item.score > 10:
        score += 0.1
    if item.score > 100:
        score += 0.1
    if item.score > 500:
        score += 0.1

    # 有发布时间加分
    if item.published_at:
        score += 0.1

    return min(score, 1.0)


def _make_id(item: RawItem) -> str:
    """生成全局唯一 ID"""
    raw = f"{item.source_type.value}:{item.source_id}"
    return hashlib.md5(raw.encode()).hexdigest()[:16]


def _clean_one(item: RawItem) -> CleanedItem:
    """清洗单条原始数据"""
    title = _normalize_whitespace(_strip_html(item.title))
    content = _normalize_whitespace(_strip_html(item.content))

    return CleanedItem(
        id=_make_id(item),
        source_type=item.source_type,
        title=title,
        content=content,
        url=item.url,
        author=item.author,
        published_at=item.published_at,
        language="en",  # v0.1 暂不做语言检测
        quality_score=_compute_quality_score(item),
        metadata=item.metadata,
    )


def _simple_dedup(items: list[CleanedItem]) -> list[CleanedItem]:
    """基于标题相似度的简单去重"""
    seen_titles: dict[str, str] = {}  # normalized_title -> id
    result: list[CleanedItem] = []

    for item in items:
        # 标题标准化用于比较
        norm_title = item.title.lower().strip()
        if norm_title in seen_titles:
            item.is_duplicate = True
            item.duplicate_of = seen_titles[norm_title]
            logger.debug(f"Duplicate title: {item.title[:50]}...")
        else:
            seen_titles[norm_title] = item.id
        result.append(item)

    return result


async def cleaner_node(state: PipelineState) -> dict:
    """Cleaner 节点：批量清洗原始数据"""
    raw_items = state.get("raw_items", [])
    if not raw_items:
        logger.warning("No raw items to clean")
        return {"cleaned_items": []}

    logger.info(f"Cleaning {len(raw_items)} raw items ...")

    # 清洗
    cleaned = [_clean_one(item) for item in raw_items]

    # 按质量分排序
    cleaned.sort(key=lambda x: x.quality_score, reverse=True)

    # 简单去重
    cleaned = _simple_dedup(cleaned)

    valid_count = sum(1 for c in cleaned if not c.is_duplicate)
    logger.info(f"Cleaning done: {len(cleaned)} items, {valid_count} valid, {len(cleaned) - valid_count} duplicates")

    return {"cleaned_items": cleaned}
