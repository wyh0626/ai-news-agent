"""条件边逻辑 - 控制 LangGraph 工作流的分支"""

from src.config import settings
from src.graph.state import PipelineState


def should_write(state: PipelineState) -> str:
    """判断是否积累了足够的新闻来生成文章"""
    extracted = state.get("extracted_items", [])
    min_items = settings.min_items_to_write

    if len(extracted) >= min_items:
        return "write"
    return "skip"
