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

    MAX_PAGES = 5

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        if not self.api_key:
            logger.warning("Firecrawl API Key not configured, skipping Twitter fetch")
            return []

        try:
            from firecrawl import Firecrawl
        except ImportError:
            logger.error("firecrawl-py not installed, run: pip install firecrawl-py")
            return []

        firecrawl = Firecrawl(api_key=self.api_key)
        # tweet_id -> RawItem，跨页去重并取最大互动数据
        best_items: dict[str, RawItem] = {}
        url = self.list_url

        for page in range(1, self.MAX_PAGES + 1):
            logger.info(f"Fetching via Firecrawl + Nitter (page {page}): {url}")
            try:
                doc = firecrawl.scrape(url, formats=["markdown"])
            except Exception as e:
                logger.error(f"Firecrawl fetch failed: {e}")
                break

            if not doc or not doc.markdown:
                logger.warning("Firecrawl returned no valid content")
                break

            logger.info(f"Firecrawl page {page}: {len(doc.markdown)} chars")

            page_items, oldest_time = self._parse_nitter_markdown(
                doc.markdown, since
            )

            # 同一推文取最大 score（互动数据最准确的那次）
            for item in page_items:
                tid = item.source_id
                if tid not in best_items or item.score > best_items[tid].score:
                    best_items[tid] = item

            # Stop if oldest tweet on this page is older than since
            if since and oldest_time and oldest_time <= since:
                logger.info(f"Reached tweets older than {since}, stopping pagination")
                break

            # Extract cursor for next page
            cursor = self._extract_cursor(doc.markdown)
            if not cursor:
                logger.info("No more pages (no cursor found)")
                break

            url = f"{self.list_url}?cursor={cursor}"

        all_items = list(best_items.values())
        logger.info(f"Total tweets fetched across {page} page(s): {len(all_items)}")

        if not all_items:
            return []

        pre_high = sorted(all_items, key=lambda x: x.score, reverse=True)[:5]
        logger.info("Twitter top-5 scores:")
        for it in pre_high:
            logger.info(f"  score={it.score:6d} @{it.author}: {it.title[:60]}")

        # 所有推文统一走 LLM AI 过滤（包括高分推文，避免非 AI 内容混入）
        try:
            from src.tools.ai_filter import batch_filter_ai
            titles = [it.title for it in all_items]
            descs = [it.content[:80] for it in all_items]
            ai_indices = set(await batch_filter_ai(titles, descs))
            filtered = [it for idx, it in enumerate(all_items) if idx in ai_indices]
            logger.info(
                f"Twitter (Firecrawl): {len(all_items)} tweets, "
                f"LLM filtered → {len(filtered)} AI-related"
            )
        except Exception as e:
            logger.warning(f"Twitter AI filter failed, returning all: {e}")
            filtered = all_items

        # 按 score 降序取 top 10
        filtered.sort(key=lambda x: x.score, reverse=True)
        result = filtered[:10]
        logger.info(f"Twitter final selection: top {len(result)} AI tweets by score")
        return result

    def _parse_nitter_markdown(
        self, markdown: str, since: datetime | None
    ) -> tuple[list[RawItem], datetime | None]:
        """解析 Nitter 返回的 markdown，提取推文

        Returns (items, oldest_published_time)
        """
        items: list[RawItem] = []
        seen_ids: set[str] = set()
        oldest_time: datetime | None = None

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

            # 同一页内去重（跨页去重在 fetch() 层用 best_items 处理）
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

            # 提取第一张媒体图片（排除头像）
            image_url = None
            img_match = re.search(
                r'!\[\]\((https://nitter\.net/pic/media[^)]+)\)', raw_content
            )
            if img_match:
                # 转为原图 URL（去掉 small/webp 参数）
                nitter_img = img_match.group(1)
                orig = re.sub(r'%3Fname%3D\w+%26format%3D\w+', '', nitter_img)
                image_url = orig.replace('/pic/media', '/pic/orig/media')

            title = text[:100].replace('\n', ' ').strip()
            if len(text) > 100:
                title += "..."

            meta: dict = {"via": "firecrawl+nitter", **engagement}
            if image_url:
                meta["image"] = image_url

            item = RawItem(
                source_type=SourceType.TWITTER,
                source_id=f"tw:{tweet_id}",
                title=title,
                content=text,
                url=f"https://x.com/{username}/status/{tweet_id}",
                author=username,
                published_at=published,
                score=(
                    engagement.get("likes", 0)
                    + engagement.get("retweets", 0) * 3
                    + engagement.get("replies", 0)
                ),
                metadata=meta,
            )
            items.append(item)

            # Track oldest tweet time for pagination
            if published and (oldest_time is None or published < oldest_time):
                oldest_time = published

        return items, oldest_time

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
    def _extract_cursor(markdown: str) -> str | None:
        """Extract pagination cursor from Nitter 'Load more' link"""
        m = re.search(r'\[Load more\]\([^)]*[?&]cursor=([^&)\s]+)', markdown)
        return m.group(1) if m else None

    @staticmethod
    def _extract_engagement(raw: str) -> dict:
        """从推文末尾提取互动数字（Nitter 格式：空行分隔的纯数字）"""
        lines = raw.strip().split('\n')
        # Collect trailing number lines, skipping empty lines and 'xxx retweeted' lines
        nums = []
        for line in reversed(lines):
            stripped = line.strip().replace(',', '')
            if not stripped:
                continue
            if re.match(r'^\d+$', stripped):
                nums.insert(0, int(stripped))
            elif nums:
                break
            elif re.match(r'.+retweeted$', stripped, re.IGNORECASE):
                continue
            else:
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
        # 去掉末尾的纯数字行和 retweeted 行（互动数据）
        lines = text.split('\n')
        while lines:
            tail = lines[-1].strip()
            if not tail or re.match(r'^\d[\d,]*$', tail) or re.match(r'.+retweeted$', tail, re.IGNORECASE):
                lines.pop()
            else:
                break
        # 去掉空行过多
        text = '\n'.join(lines)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()
