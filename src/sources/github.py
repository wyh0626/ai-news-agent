"""GitHub Trending 数据源适配器 - RSS 采集 + LLM AI 过滤 + 跨天去重"""

import json
import logging
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

import feedparser
import httpx

from src.config import settings
from src.models import RawItem, SourceType
from src.sources.base import BaseSource
from src.tools.ai_filter import batch_filter_ai

logger = logging.getLogger(__name__)

USER_AGENT = "AI-News-Agent/1.0 (RSS Reader)"

# 去重缓存文件路径
TRENDING_CACHE_FILE = ".github_trending_cache.json"

# GitHub Trending RSS (社区维护，按语言/周期分类)
TRENDING_RSS_BASE = "https://mshibanami.github.io/GitHubTrendingRSS"


class GitHubTrendingSource(BaseSource):
    """通过 RSS 采集 GitHub Trending AI 项目

    功能：
    1. 从社区维护的 GitHub Trending RSS 源获取热门仓库
    2. LLM 批量标题+描述分类：自动判断项目是否 AI 相关
    3. 跨天去重：本地 JSON 缓存近 N 天已上榜项目
    """

    def __init__(self, language: str = "", since_period: str = "daily"):
        self.language = language
        self.since_period = since_period
        # RSS URL: /daily/all.xml 或 /daily/python.xml
        lang_path = language.lower() if language else "all"
        self.rss_url = f"{TRENDING_RSS_BASE}/{since_period}/{lang_path}.xml"

    @property
    def source_id(self) -> str:
        return "github_trending"

    @property
    def default_interval(self) -> int:
        return 14400  # 4 hours

    @staticmethod
    def _load_cache() -> dict:
        """加载去重缓存 {date_str: [repo_full_name, ...]}"""
        cache_path = Path(settings.output_dir) / TRENDING_CACHE_FILE
        if cache_path.exists():
            try:
                return json.loads(cache_path.read_text())
            except Exception:
                return {}
        return {}

    @staticmethod
    def _save_cache(cache: dict):
        """保存去重缓存，清理过期条目"""
        cache_path = Path(settings.output_dir) / TRENDING_CACHE_FILE
        cache_path.parent.mkdir(parents=True, exist_ok=True)

        # 清理超过 N 天的旧缓存
        cutoff = (
            datetime.now(tz=timezone.utc)
            - timedelta(days=settings.github_trending_dedup_days)
        ).strftime("%Y-%m-%d")
        cleaned = {k: v for k, v in cache.items() if k >= cutoff}

        cache_path.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2))

    @staticmethod
    def _extract_full_name(link: str) -> str:
        """从 GitHub URL 提取 owner/repo"""
        match = re.search(r"github\.com/([^/]+/[^/]+)", link)
        return match.group(1) if match else ""

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        logger.info(f"Fetching GitHub Trending (RSS: {self.rss_url}) ...")

        try:
            async with httpx.AsyncClient(
                timeout=30,
                headers={"User-Agent": USER_AGENT},
                follow_redirects=True,
            ) as client:
                resp = await client.get(self.rss_url)
                resp.raise_for_status()
            feed = feedparser.parse(resp.text)
        except Exception as e:
            logger.error(f"Fetch GitHub Trending RSS failed: {e}")
            return []

        entries = feed.entries[:50]
        if not entries:
            logger.info("GitHub Trending: no RSS entries")
            return []

        # 构建候选列表
        candidates: list[dict] = []
        for entry in entries:
            link = entry.get("link", "")
            full_name = self._extract_full_name(link)
            if not full_name:
                continue
            title = entry.get("title", full_name)
            desc = entry.get("summary", "") or ""
            candidates.append({
                "full_name": full_name,
                "title": title,
                "description": desc,
                "link": link,
            })

        if not candidates:
            logger.info("GitHub Trending: no valid repo entries")
            return []

        # LLM 批量判断项目是否 AI 相关
        titles = [c["full_name"] for c in candidates]
        descs = [c["description"][:80] for c in candidates]
        ai_indices = set(await batch_filter_ai(titles, descs))

        # 加载跨天去重缓存
        cache = self._load_cache()
        today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
        today_ai_repos: list[str] = []

        historical_repos: set[str] = set()
        for date_str, repo_list in cache.items():
            if date_str != today:
                historical_repos.update(repo_list)

        items: list[RawItem] = []
        deduped_count = 0

        for idx, c in enumerate(candidates):
            if idx not in ai_indices:
                continue

            full_name = c["full_name"]
            today_ai_repos.append(full_name)

            # 跨天去重
            if full_name in historical_repos:
                deduped_count += 1
                continue

            item = RawItem(
                source_type=SourceType.GITHUB,
                source_id=f"github:{full_name}",
                title=full_name,
                content=c["description"],
                url=c["link"],
                author=full_name.split("/")[0],
                published_at=datetime.now(tz=timezone.utc),
                metadata={},
            )
            items.append(item)

        # 更新缓存（只缓存 AI 项目）
        cache[today] = today_ai_repos
        self._save_cache(cache)

        logger.info(
            f"GitHub Trending: {len(items)} AI projects "
            f"(LLM filtered {len(candidates)} → {len(ai_indices)} AI, "
            f"cross-day dedup: {deduped_count} repeated)"
        )
        return items
