"""Cleaner Agent 测试"""

import pytest

from src.agents.cleaner import (
    _clean_one,
    _compute_quality_score,
    _normalize_whitespace,
    _simple_dedup,
    _strip_html,
)
from src.models import CleanedItem, RawItem, SourceType


def test_strip_html():
    assert _strip_html("<p>Hello <b>world</b></p>") == "Hello world"
    assert _strip_html("&amp; test &lt;") == "& test <"
    assert _strip_html("no html here") == "no html here"


def test_normalize_whitespace():
    assert _normalize_whitespace("  hello   world  ") == "hello world"
    assert _normalize_whitespace("line\n\nnew") == "line new"


def test_compute_quality_score():
    # 低质量条目
    low = RawItem(source_type=SourceType.REDDIT, source_id="1", title="Hi")
    assert _compute_quality_score(low) < 0.5

    # 高质量条目
    from datetime import datetime, timezone

    high = RawItem(
        source_type=SourceType.REDDIT,
        source_id="2",
        title="A comprehensive guide to fine-tuning LLMs",
        content="x" * 300,
        score=600,
        published_at=datetime.now(tz=timezone.utc),
    )
    assert _compute_quality_score(high) >= 0.8


def test_clean_one():
    raw = RawItem(
        source_type=SourceType.REDDIT,
        source_id="test_123",
        title="<b>Test</b>  Title",
        content="<p>Some   content</p>",
    )
    cleaned = _clean_one(raw)
    assert cleaned.title == "Test Title"
    assert cleaned.content == "Some content"
    assert cleaned.id  # 应该生成了 ID


def test_simple_dedup():
    items = [
        CleanedItem(id="a", source_type=SourceType.REDDIT, title="Same Title", content="c1"),
        CleanedItem(id="b", source_type=SourceType.REDDIT, title="Same Title", content="c2"),
        CleanedItem(id="c", source_type=SourceType.REDDIT, title="Different Title", content="c3"),
    ]
    result = _simple_dedup(items)
    dupes = [i for i in result if i.is_duplicate]
    assert len(dupes) == 1
    assert dupes[0].id == "b"
