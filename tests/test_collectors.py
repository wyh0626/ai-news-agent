"""数据源采集器测试"""

import pytest

from src.sources.reddit import RedditRSSSource
from src.sources.hackernews import HackerNewsSource
from src.sources.arxiv import ArxivSource


def test_reddit_source_init():
    source = RedditRSSSource("LocalLLaMA")
    assert source.source_id == "reddit:LocalLLaMA"
    assert "LocalLLaMA" in source.url


def test_hn_source_init():
    source = HackerNewsSource(min_score=100)
    assert source.source_id == "hackernews"
    assert "100" in source.url


def test_arxiv_source_init():
    source = ArxivSource(categories=["cs.AI"])
    assert source.source_id == "arxiv"
    assert len(source.urls) == 1


@pytest.mark.asyncio
async def test_reddit_fetch_live():
    """集成测试：实际从 Reddit 拉取数据（需要网络）"""
    source = RedditRSSSource("LocalLLaMA")
    items = await source.fetch()
    # RSS 应该返回一些条目（除非网络不通）
    # 这里只验证不会崩溃
    assert isinstance(items, list)
    if items:
        assert items[0].source_type.value == "reddit"
        assert items[0].title
