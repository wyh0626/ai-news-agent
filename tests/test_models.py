"""数据模型测试"""

from datetime import datetime, timezone

from src.models import (
    CleanedItem,
    ExtractedItem,
    GeneratedArticle,
    RawItem,
    Sentiment,
    SourceType,
)


def test_raw_item_creation():
    item = RawItem(
        source_type=SourceType.REDDIT,
        source_id="abc123",
        title="Test Title",
        content="Test content",
        url="https://reddit.com/r/test/123",
    )
    assert item.source_type == SourceType.REDDIT
    assert item.source_id == "abc123"
    assert item.score == 0
    assert item.fetched_at is not None


def test_raw_item_with_metadata():
    item = RawItem(
        source_type=SourceType.HACKERNEWS,
        source_id="hn_456",
        title="HN Post",
        score=150,
        metadata={"hn_url": "https://news.ycombinator.com/item?id=456"},
    )
    assert item.score == 150
    assert "hn_url" in item.metadata


def test_cleaned_item():
    item = CleanedItem(
        id="reddit_abc123",
        source_type=SourceType.REDDIT,
        title="Clean Title",
        content="Clean content",
        quality_score=0.75,
    )
    assert item.quality_score == 0.75
    assert item.is_duplicate is False
    assert item.language == "en"


def test_extracted_item():
    item = ExtractedItem(
        id="test_001",
        source_type=SourceType.ARXIV,
        title="A New LLM Architecture",
        content="We propose...",
        summary="提出了一种新的 LLM 架构",
        topics=["LLM", "架构"],
        entities=["OpenAI", "GPT-5"],
        sentiment=Sentiment.POSITIVE,
        importance_score=8.5,
    )
    assert item.importance_score == 8.5
    assert "LLM" in item.topics
    assert item.sentiment == Sentiment.POSITIVE


def test_generated_article():
    article = GeneratedArticle(
        title="AI 日报 - 2025-02-13",
        date="2025-02-13",
        markdown_content="# Test",
        item_count=10,
    )
    assert article.item_count == 10
    assert article.date == "2025-02-13"
