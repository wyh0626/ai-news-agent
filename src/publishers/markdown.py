"""多渠道发布器 - Markdown 文件 + Newsletter 邮件 + Webhook 推送"""

import logging
from pathlib import Path

from src.config import settings
from src.graph.state import PipelineState
from src.models import GeneratedArticle

logger = logging.getLogger(__name__)


def _save_markdown(article: GeneratedArticle, output_dir: Path) -> Path:
    """将文章保存为 Markdown 文件"""
    filename = f"ai-daily-{article.date}.md"
    filepath = output_dir / filename

    filepath.write_text(article.markdown_content, encoding="utf-8")
    logger.info(f"文章已保存: {filepath}")
    return filepath


async def _publish_newsletter(article: GeneratedArticle):
    """发送邮件通知"""
    try:
        from src.publishers.newsletter import NewsletterPublisher

        publisher = NewsletterPublisher()
        if publisher.available:
            publisher.send(
                subject=f"🤖 {article.title}",
                markdown_content=article.markdown_content,
            )
    except Exception as e:
        logger.debug(f"Newsletter 发布跳过: {e}")


async def _publish_webhooks(article: GeneratedArticle):
    """推送到配置的 Webhook 渠道"""
    webhook_configs = [
        ("slack", getattr(settings, "slack_webhook_url", "")),
        ("discord", getattr(settings, "discord_webhook_url", "")),
        ("feishu", getattr(settings, "feishu_webhook_url", "")),
    ]
    for platform, url in webhook_configs:
        if not url:
            continue
        try:
            from src.publishers.webhook import WebhookPublisher

            publisher = WebhookPublisher(url, platform=platform)
            await publisher.send(
                title=article.title,
                content=article.markdown_content[:3000],
            )
        except Exception as e:
            logger.debug(f"Webhook [{platform}] 推送跳过: {e}")


async def publish_node(state: PipelineState) -> dict:
    """Publish 节点：多渠道发布文章"""
    article = state.get("article")
    if not article or not article.markdown_content:
        logger.warning("没有文章需要发布")
        return {}

    # 1. 始终保存 Markdown 文件
    output_dir = settings.output_path
    filepath = _save_markdown(article, output_dir)

    # 1.5 保存英文版（如果有）
    if article.markdown_content_en:
        en_filename = f"ai-daily-{article.date}-en.md"
        en_filepath = output_dir / en_filename
        en_filepath.write_text(article.markdown_content_en, encoding="utf-8")
        logger.info(f"英文版已保存: {en_filepath}")

    # 2. 尝试发送邮件
    await _publish_newsletter(article)

    # 3. 尝试推送 Webhook
    await _publish_webhooks(article)

    logger.info(f"发布完成: {filepath}")
    return {}
