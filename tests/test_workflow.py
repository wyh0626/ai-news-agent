"""LangGraph 工作流测试"""

from src.graph.conditions import should_write
from src.graph.workflow import build_workflow
from src.models import ExtractedItem, SourceType


def test_should_write_enough_items():
    state = {
        "extracted_items": [
            ExtractedItem(
                id=f"item_{i}",
                source_type=SourceType.REDDIT,
                title=f"Title {i}",
                content=f"Content {i}",
            )
            for i in range(10)
        ]
    }
    assert should_write(state) == "write"


def test_should_write_not_enough():
    state = {"extracted_items": []}
    assert should_write(state) == "skip"


def test_workflow_builds():
    """验证工作流图可以正确构建"""
    workflow = build_workflow()
    assert workflow is not None
    graph = workflow.compile()
    assert graph is not None
