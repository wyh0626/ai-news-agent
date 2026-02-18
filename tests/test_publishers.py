"""发布器测试"""

import pytest

from src.publishers.webhook import (
    WebhookPublisher,
    SlackPublisher,
    DiscordPublisher,
    FeishuPublisher,
)
from src.publishers.newsletter import NewsletterPublisher


class TestWebhookPublisher:
    def test_not_available_empty_url(self):
        pub = WebhookPublisher("", platform="slack")
        assert pub.available is False

    def test_available_with_url(self):
        pub = WebhookPublisher("https://hooks.slack.com/test")
        assert pub.available is True

    def test_slack_payload(self):
        payload = WebhookPublisher._slack_payload("Title", "Content", "https://url")
        assert "blocks" in payload
        assert len(payload["blocks"]) == 3  # header + section + actions

    def test_discord_payload(self):
        payload = WebhookPublisher._discord_payload("Title", "Content", "https://url")
        assert "embeds" in payload
        assert payload["embeds"][0]["title"] == "Title"

    def test_feishu_payload(self):
        payload = WebhookPublisher._feishu_payload("Title", "Content", "")
        assert payload["msg_type"] == "interactive"

    def test_generic_payload(self):
        payload = WebhookPublisher._generic_payload("T", "C", "U")
        assert payload == {"title": "T", "content": "C", "url": "U"}

    def test_subclasses(self):
        assert SlackPublisher("url").platform == "slack"
        assert DiscordPublisher("url").platform == "discord"
        assert FeishuPublisher("url").platform == "feishu"


class TestNewsletterPublisher:
    def test_not_available_no_config(self):
        pub = NewsletterPublisher()
        assert pub.available is False

    def test_available_with_config(self):
        pub = NewsletterPublisher(
            smtp_host="smtp.test.com",
            smtp_user="user",
            smtp_password="pass",
        )
        assert pub.available is True

    def test_markdown_to_html(self):
        pub = NewsletterPublisher()
        html = pub._markdown_to_html("# Hello\n\nWorld")
        assert "<h1>" in html or "<pre>" in html
        assert "AI News Agent" in html
