"""LangGraph 主工作流图定义"""

import logging
from datetime import datetime, timezone
from uuid import uuid4

from langgraph.graph import END, StateGraph

from src.agents.cleaner import cleaner_node
from src.agents.collector import collector_node
from src.agents.dedup import dedup_node
from src.agents.extractor import extractor_node
from src.agents.memory_updater import update_memory_node
from src.agents.reviewer import reviewer_node
from src.agents.translator import translator_node
from src.agents.writer import writer_node
from src.graph.conditions import should_write
from src.graph.state import PipelineState
from src.publishers.markdown import publish_node

logger = logging.getLogger(__name__)


async def load_schedule_node(state: PipelineState) -> dict:
    """加载调度配置，决定本次运行采集哪些数据源"""
    sources = state.get("sources_config")
    if not sources:
        sources = ["reddit", "hackernews"]

    run_id = state.get("run_id") or str(uuid4())[:8]
    started = datetime.now(tz=timezone.utc).isoformat()

    logger.info(f"Pipeline start [run_id={run_id}], sources: {sources}")
    return {
        "run_id": run_id,
        "run_started_at": started,
        "sources_config": sources,
        "errors": [],
    }


async def save_and_wait_node(state: PipelineState) -> dict:
    """新闻不足时保存状态等待下次运行"""
    extracted = state.get("extracted_items", [])
    logger.info(f"Not enough items ({len(extracted)}), saving state and waiting for next run")
    return {}


def build_workflow() -> StateGraph:
    """构建完整的 Pipeline 工作流图"""
    workflow = StateGraph(PipelineState)

    # 注册节点
    workflow.add_node("load_schedule", load_schedule_node)
    workflow.add_node("collector", collector_node)
    workflow.add_node("cleaner", cleaner_node)
    workflow.add_node("dedup", dedup_node)
    workflow.add_node("extractor", extractor_node)
    workflow.add_node("reviewer", reviewer_node)
    workflow.add_node("writer", writer_node)
    workflow.add_node("translator", translator_node)
    workflow.add_node("publisher", publish_node)
    workflow.add_node("update_memory", update_memory_node)
    workflow.add_node("save_and_wait", save_and_wait_node)

    # 定义边
    workflow.set_entry_point("load_schedule")
    workflow.add_edge("load_schedule", "collector")
    workflow.add_edge("collector", "cleaner")
    workflow.add_edge("cleaner", "dedup")
    workflow.add_edge("dedup", "extractor")

    # 条件边：是否生成文章
    workflow.add_conditional_edges(
        "extractor",
        should_write,
        {
            "write": "reviewer",
            "skip": "save_and_wait",
        },
    )

    workflow.add_edge("reviewer", "writer")
    workflow.add_edge("writer", "translator")
    workflow.add_edge("translator", "publisher")
    workflow.add_edge("publisher", "update_memory")
    workflow.add_edge("update_memory", END)
    workflow.add_edge("save_and_wait", END)

    return workflow


def compile_graph():
    """编译工作流图为可执行的 Runnable"""
    workflow = build_workflow()
    return workflow.compile()
