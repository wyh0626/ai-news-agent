"""数据源适配器测试 - 覆盖所有数据源"""

import pytest

from src.sources.base import BaseSource
from src.sources.reddit import RedditRSSSource
from src.sources.hackernews import HackerNewsSource
from src.sources.arxiv import ArxivSource
from src.sources.github import GitHubTrendingSource
from src.sources.rss_generic import GenericRSSSource, get_ai_blog_sources
from src.sources.twitter import TwitterSource


class TestRedditSource:
    def test_init(self):
        source = RedditRSSSource("LocalLLaMA")
        assert source.source_id == "reddit:LocalLLaMA"
        assert "LocalLLaMA" in source.url
        assert isinstance(source, BaseSource)

    def test_default_interval(self):
        source = RedditRSSSource("test")
        assert source.default_interval == 900


class TestHackerNewsSource:
    def test_init(self):
        source = HackerNewsSource(min_score=100)
        assert source.source_id == "hackernews"
        assert "100" in source.url

    def test_url_has_query(self):
        source = HackerNewsSource()
        assert "q=" in source.url

    def test_default_interval(self):
        source = HackerNewsSource()
        assert source.default_interval == 1800



class TestArxivSource:
    def test_init(self):
        source = ArxivSource(categories=["cs.AI", "cs.CL"])
        assert source.source_id == "arxiv"
        assert len(source.urls) == 2

    def test_default_categories(self):
        source = ArxivSource()
        assert "cs.AI" in source.categories

    def test_extract_arxiv_id(self):
        assert ArxivSource._extract_arxiv_id("http://arxiv.org/abs/2401.12345") == "2401.12345"

    def test_clean_title(self):
        assert ArxivSource._clean_title("  Hello   World  ") == "Hello World"



class TestGitHubSource:
    def test_init(self):
        source = GitHubTrendingSource()
        assert source.source_id == "github_trending"
        assert source.default_interval == 14400



class TestGenericRSSSource:
    def test_init(self):
        source = GenericRSSSource("test_blog", "https://example.com/feed.xml")
        assert source.source_id == "rss:test_blog"
        assert source.default_interval == 3600

    def test_ai_blog_sources(self):
        sources = get_ai_blog_sources()
        assert len(sources) > 0
        assert all(isinstance(s, GenericRSSSource) for s in sources)


class TestTwitterSource:
    def test_init(self):
        source = TwitterSource(api_key="test_key")
        assert source.source_id == "twitter"
        assert len(source.kol_usernames) > 0

    def test_no_api_key(self):
        source = TwitterSource(api_key="")
        assert source.default_interval == 900

    @pytest.mark.asyncio
    async def test_fetch_no_key(self):
        source = TwitterSource(api_key="")
        items = await source.fetch()
        assert items == []

    def test_parse_twitter_time(self):
        result = TwitterSource._parse_twitter_time("Wed Feb 12 10:30:00 +0000 2025")
        assert result is not None
        assert result.year == 2025

    def test_parse_twitter_time_empty(self):
        assert TwitterSource._parse_twitter_time("") is None
