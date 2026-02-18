"""Twitter/X 数据源适配器 - 通过 twitterapi.io REST API 采集"""

import logging
from datetime import datetime, timezone

import httpx

from src.models import RawItem, SourceType
from src.sources.base import BaseSource

logger = logging.getLogger(__name__)

TWITTER_API_BASE = "https://api.twitterapi.io/twitter"


class TwitterSource(BaseSource):
    """通过 twitterapi.io 采集 Twitter/X KOL 内容"""

    def __init__(self, api_key: str, kol_usernames: list[str] | None = None):
        self.api_key = api_key
        self.kol_usernames = kol_usernames or [
            "ylecun",
            "kaborogevern",
            "AndrewYNg",
            "jimfan",
            "DrJimFan",
            "_jasonwei",
            "OpenAI",
            "GoogleDeepMind",
            "AnthropicAI",
            "huaborface",
        ]
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
        }

    @property
    def source_id(self) -> str:
        return "twitter"

    @property
    def default_interval(self) -> int:
        return 900  # 15 min

    async def fetch(self, since: datetime | None = None) -> list[RawItem]:
        if not self.api_key:
            logger.warning("未配置 Twitter API Key，跳过采集")
            return []

        logger.info(f"采集 Twitter, KOL 数: {len(self.kol_usernames)}")
        all_items: list[RawItem] = []

        async with httpx.AsyncClient(timeout=30, headers=self.headers) as client:
            for username in self.kol_usernames:
                items = await self._fetch_user_tweets(client, username, since)
                all_items.extend(items)

        logger.info(f"Twitter: 获取 {len(all_items)} 条推文")
        return all_items

    async def _fetch_user_tweets(
        self, client: httpx.AsyncClient, username: str, since: datetime | None
    ) -> list[RawItem]:
        """采集单个用户的最新推文"""
        try:
            resp = await client.get(
                f"{TWITTER_API_BASE}/user/last_tweets",
                params={"userName": username, "count": 10},
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.error(f"采集 @{username} 失败: {e}")
            return []

        tweets = data.get("tweets", [])
        items: list[RawItem] = []

        for tweet in tweets:
            created_str = tweet.get("createdAt", "")
            published = self._parse_twitter_time(created_str)
            if since and published and published <= since:
                continue

            # 过滤转推和回复，只保留原创推文
            if tweet.get("isRetweet"):
                continue

            text = tweet.get("text", "")
            tweet_id = tweet.get("id", "")

            item = RawItem(
                source_type=SourceType.TWITTER,
                source_id=f"tw:{tweet_id}",
                title=text[:100] + ("..." if len(text) > 100 else ""),
                content=text,
                url=f"https://x.com/{username}/status/{tweet_id}",
                author=username,
                published_at=published,
                score=tweet.get("likeCount", 0) + tweet.get("retweetCount", 0) * 2,
                metadata={
                    "likes": tweet.get("likeCount", 0),
                    "retweets": tweet.get("retweetCount", 0),
                    "replies": tweet.get("replyCount", 0),
                    "views": tweet.get("viewCount", 0),
                    "is_reply": tweet.get("isReply", False),
                    "media": tweet.get("media", []),
                },
            )
            items.append(item)

        return items

    @staticmethod
    def _parse_twitter_time(time_str: str) -> datetime | None:
        """解析 Twitter 时间格式"""
        if not time_str:
            return None
        try:
            # Twitter API 返回格式: "Wed Feb 12 10:30:00 +0000 2025"
            return datetime.strptime(time_str, "%a %b %d %H:%M:%S %z %Y")
        except (ValueError, TypeError):
            try:
                # ISO 格式备选
                return datetime.fromisoformat(time_str.replace("Z", "+00:00"))
            except (ValueError, TypeError):
                return None
