"""Twitter/X 数据源适配器 - 通过 Firecrawl + Nitter 镜像采集 Twitter List"""

import logging
import re
from datetime import datetime, timezone

from src.config import settings
from src.models import RawItem, SourceType
from src.sources.base import BaseSource

logger = logging.getLogger(__name__)


class TwitterFirecrawlSource(BaseSource):
    """通过 Firecrawl + Nitter 镜像采集 Twitter/X List 的推文"""

    def __init__(self, api_key: str, list_url: str, nitter_mirror: str = ""):
        self.api_key = api_key
        self.nitter_mirror = (nitter_mirror or settings.nitter_mirror_url).rstrip("/")
        # 将 x.com URL 转为 nitter URL
        self.list_url = self._to_nitter_url(list_url)

    def _to_nitter_url(self, url: str) -> str:
        """将 x.com / twitter.com URL 转为 nitter 镜像 URL"""
        url = re.sub(r'https?://(x\.com|twitter\.com)', self.nitter_mirror, url)
        return url

    @property
    def source_id(self) -> str:
        return "twitter"

    @property
    def default_interval(self) -> int:
        return 900

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        if not self.api_key:
            logger.warning("Firecrawl API Key not configured, skipping Twitter fetch")
            return []

        logger.info(f"Fetching via Firecrawl + Nitter: {self.list_url}")

        try:
            from firecrawl import Firecrawl
        except ImportError:
            logger.error("firecrawl-py not installed, run: pip install firecrawl-py")
            return []

        try:
            firecrawl = Firecrawl(api_key=self.api_key)
            doc = firecrawl.scrape(self.list_url, formats=["markdown"])
        except Exception as e:
            logger.error(f"Firecrawl fetch failed: {e}")
            return []

        if not doc or not doc.markdown:
            logger.warning("Firecrawl returned no valid content")
            return []

        logger.info(f"Firecrawl returned {len(doc.markdown)} chars")

        items = self._parse_nitter_markdown(doc.markdown, since)
        if not items:
            return []

        # LLM 批量过滤非 AI 相关推文
        try:
            from src.tools.ai_filter import batch_filter_ai
            titles = [it.title for it in items]
            descs = [it.content[:80] for it in items]
            ai_indices = set(await batch_filter_ai(titles, descs))
            filtered = [it for idx, it in enumerate(items) if idx in ai_indices]
            logger.info(
                f"Twitter (Firecrawl): {len(items)} tweets, "
                f"LLM filtered → {len(filtered)} AI-related"
            )
            return filtered
        except Exception as e:
            logger.warning(f"Twitter AI filter failed, returning all: {e}")
            return items

    def _parse_nitter_markdown(self, markdown: str, since: datetime | None) -> list[RawItem]:
        """解析 Nitter 返回的 markdown，提取推文

        Nitter markdown 中每条推文的结构：
          [@username](...)     ← 用户名
          [时间](nitter.net/user/status/ID#m "日期")  ← 时间戳+链接
          推文正文...          ← 正文（可能多行）
          数字 数字 数字       ← 互动数据（回复/转发/点赞）
        """
        items: list[RawItem] = []
        seen_ids: set[str] = set()

        # 用正则找到所有推文时间戳行，它们是推文的锚点
        # 格式: [3m](https://nitter.net/user/status/ID#m "Feb 14, 2026 · 4:23 PM UTC")
        nitter_host = re.escape(self.nitter_mirror.split("://", 1)[-1])
        tweet_anchors = list(re.finditer(
            r'\[(?:\d+[smhd]|[A-Z][a-z]{2}\s+\d+)\]'
            rf'\(https?://{nitter_host}/(\w+)/status/(\d+)#m\s+"([^"]+)"\)',
            markdown
        ))

        if not tweet_anchors:
            logger.warning("No tweet anchors found")
            return []

        for idx, match in enumerate(tweet_anchors):
            username = match.group(1)
            tweet_id = match.group(2)
            date_str = match.group(3)

            if tweet_id in seen_ids:
                continue
            seen_ids.add(tweet_id)

            # 解析发布时间
            published = self._parse_nitter_date(date_str)
            if since and published and published <= since:
                continue

            # 提取推文正文：从时间戳行之后到下一条推文的用户头像之前
            content_start = match.end()
            if idx + 1 < len(tweet_anchors):
                # 下一个锚点前约 200 字符开始就是下一条推文的头像/用户名区域
                next_anchor_start = tweet_anchors[idx + 1].start()
                # 往回找到用户头像区域（以 [![ 开头的行）
                search_region = markdown[content_start:next_anchor_start]
                # 找最后一个头像 markdown 标记作为分界
                avatar_pos = search_region.rfind('[![')
                if avatar_pos > 0:
                    content_end = content_start + avatar_pos
                else:
                    content_end = next_anchor_start
            else:
                content_end = min(content_start + 2000, len(markdown))

            raw_content = markdown[content_start:content_end].strip()
            text = self._clean_nitter_text(raw_content)

            if not text or len(text) < 5:
                continue

            # 提取互动数据（推文末尾的数字行）
            engagement = self._extract_engagement(raw_content)

            title = text[:100].replace('\n', ' ').strip()
            if len(text) > 100:
                title += "..."

            item = RawItem(
                source_type=SourceType.TWITTER,
                source_id=f"tw:{tweet_id}",
                title=title,
                content=text,
                url=f"https://x.com/{username}/status/{tweet_id}",
                author=username,
                published_at=published,
                score=engagement.get("likes", 0) + engagement.get("retweets", 0) * 2,
                metadata={
                    "via": "firecrawl+nitter",
                    **engagement,
                },
            )
            items.append(item)

        return items

    @staticmethod
    def _parse_nitter_date(date_str: str) -> datetime | None:
        """解析 Nitter 日期格式: 'Feb 14, 2026 · 4:23 PM UTC'"""
        if not date_str:
            return None
        try:
            clean = date_str.replace('\u00b7', '·').strip()
            # "Feb 14, 2026 · 4:23 PM UTC"
            clean = re.sub(r'\s*·\s*', ' ', clean).replace(' UTC', '').strip()
            return datetime.strptime(clean, "%b %d, %Y %I:%M %p").replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            try:
                # 只有日期 "Feb 14, 2026"
                clean = date_str.split('·')[0].strip()
                return datetime.strptime(clean, "%b %d, %Y").replace(tzinfo=timezone.utc)
            except (ValueError, TypeError):
                return None

    @staticmethod
    def _extract_engagement(raw: str) -> dict:
        """从推文末尾提取互动数字（Nitter 格式：换行分隔的纯数字）"""
        lines = raw.strip().split('\n')
        # 末尾连续的纯数字行就是互动数据
        nums = []
        for line in reversed(lines):
            line = line.strip().replace(',', '')
            if re.match(r'^\d+$', line):
                nums.insert(0, int(line))
            elif nums:
                break

        result = {}
        if len(nums) >= 3:
            result = {"replies": nums[0], "retweets": nums[1], "likes": nums[2]}
        elif len(nums) == 2:
            result = {"retweets": nums[0], "likes": nums[1]}
        elif len(nums) == 1:
            result = {"likes": nums[0]}
        return result

    @staticmethod
    def _clean_nitter_text(text: str) -> str:
        """清理 Nitter markdown 推文文本"""
        # 去 markdown 图片链接 [![...](...)](...)
        text = re.sub(r'\[!\[.*?\]\(.*?\)\]\(.*?\)', '', text)
        # 去 markdown 图片
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
        # 将 markdown 链接转为纯文本，但保留 @ 和显示名
        text = re.sub(r'\[([^\]]*)\]\([^\)]+\)', r'\1', text)
        # 去掉引用推文中重复的 "显示名\n@username" 块
        text = re.sub(r'\n[^\n]+\n@\w{1,15}\n', '\n', text)
        # 去掉独立的 @username 引用行（通常是 Nitter 的 "@user" 格式）
        text = re.sub(r'^\s*@\w{1,15}"?\s*$', '', text, flags=re.MULTILINE)
        # 去掉末尾的纯数字行（互动数据）
        lines = text.split('\n')
        while lines and re.match(r'^\s*\d[\d,]*\s*$', lines[-1]):
            lines.pop()
        # 去掉空行过多
        text = '\n'.join(lines)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()
