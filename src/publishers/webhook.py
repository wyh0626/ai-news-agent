"""Webhook 发布器（v0.5）- 推送到 Slack / Discord / 飞书 / 自定义 Webhook"""

import json
import logging
from typing import Optional

import httpx

from src.config import settings

logger = logging.getLogger(__name__)


class WebhookPublisher:
    """通用 Webhook 发布器"""

    def __init__(self, webhook_url: str, platform: str = "generic"):
        self.webhook_url = webhook_url
        self.platform = platform

    @property
    def available(self) -> bool:
        return bool(self.webhook_url)

    async def send(self, title: str, content: str, url: str = "") -> bool:
        """发送 Webhook 通知"""
        if not self.available:
            return False

        payload = self._build_payload(title, content, url)
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.post(
                    self.webhook_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                )
                resp.raise_for_status()
            logger.info(f"Webhook [{self.platform}] 推送成功: {title}")
            return True
        except Exception as e:
            logger.error(f"Webhook [{self.platform}] 推送失败: {e}")
            return False

    def _build_payload(self, title: str, content: str, url: str) -> dict:
        """根据平台构建 payload"""
        if self.platform == "slack":
            return self._slack_payload(title, content, url)
        elif self.platform == "discord":
            return self._discord_payload(title, content, url)
        elif self.platform == "feishu":
            return self._feishu_payload(title, content, url)
        else:
            return self._generic_payload(title, content, url)

    @staticmethod
    def _slack_payload(title: str, content: str, url: str) -> dict:
        # Slack 消息长度限制，截断
        truncated = content[:3000] if len(content) > 3000 else content
        blocks = [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": title[:150]},
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": truncated},
            },
        ]
        if url:
            blocks.append({
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "查看完整报告"},
                        "url": url,
                    }
                ],
            })
        return {"blocks": blocks}

    @staticmethod
    def _discord_payload(title: str, content: str, url: str) -> dict:
        truncated = content[:4000] if len(content) > 4000 else content
        embed = {
            "title": title[:256],
            "description": truncated,
            "color": 15258703,  # #E94560
        }
        if url:
            embed["url"] = url
        return {"embeds": [embed]}

    @staticmethod
    def _feishu_payload(title: str, content: str, url: str) -> dict:
        return {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {"tag": "plain_text", "content": title},
                    "template": "red",
                },
                "elements": [
                    {
                        "tag": "markdown",
                        "content": content[:30000],
                    },
                ],
            },
        }

    @staticmethod
    def _generic_payload(title: str, content: str, url: str) -> dict:
        return {"title": title, "content": content, "url": url}


class SlackPublisher(WebhookPublisher):
    def __init__(self, webhook_url: str):
        super().__init__(webhook_url, platform="slack")


class DiscordPublisher(WebhookPublisher):
    def __init__(self, webhook_url: str):
        super().__init__(webhook_url, platform="discord")


class FeishuPublisher(WebhookPublisher):
    def __init__(self, webhook_url: str):
        super().__init__(webhook_url, platform="feishu")
