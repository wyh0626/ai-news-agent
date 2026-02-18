"""LangGraph Pipeline State 定义"""

from datetime import datetime
from typing import Annotated, Optional

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from src.models import CleanedItem, ExtractedItem, GeneratedArticle, RawItem


def _replace_list(old: list, new: list) -> list:
    """替换策略：用新列表完全替换旧列表"""
    return new


class PipelineState(TypedDict):
    """Pipeline 运行时状态，贯穿整个 LangGraph 工作流"""

    # Stage 1: Collector 输出
    raw_items: Annotated[list[RawItem], _replace_list]

    # Stage 2: Cleaner 输出
    cleaned_items: Annotated[list[CleanedItem], _replace_list]

    # Stage 3: Dedup 输出
    deduped_items: Annotated[list[CleanedItem], _replace_list]

    # Stage 4: Extractor 输出
    extracted_items: Annotated[list[ExtractedItem], _replace_list]

    # Stage 5: Writer 输出
    article: Optional[GeneratedArticle]

    # Pipeline 元数据
    run_id: str
    run_started_at: str
    sources_config: list[str]  # 本次运行采集的数据源 ID
    errors: Annotated[list[str], _replace_list]

    # Agent 间通信
    messages: Annotated[list, add_messages]
