"""多渠道发布器 - Markdown 文件 + Newsletter 邮件 + Webhook 推送"""

import logging
from pathlib import Path

from src.config import settings
from src.graph.state import PipelineState
from src.models import GeneratedArticle

logger = logging.getLogger(__name__)


def _save_markdown(article: GeneratedArticle, output_dir: Path) -> Path:
    """将文章保存为 Markdown 文件（带 frontmatter）"""
    filename = f"ai-daily-{article.date}.md"
    filepath = output_dir / filename

    content = article.markdown_content
    if article.description:
        desc_escaped = article.description.replace('"', '\\"')
        frontmatter = f'---\ndescription: "{desc_escaped}"\n---\n\n'
        content = frontmatter + content

    filepath.write_text(content, encoding="utf-8")
    logger.info(f"Article saved: {filepath}")
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
        logger.debug(f"Newsletter publish skipped: {e}")


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
            logger.debug(f"Webhook [{platform}] push skipped: {e}")


async def publish_node(state: PipelineState) -> dict:
    """Publish 节点：多渠道发布文章"""
    article = state.get("article")
    if not article or not article.markdown_content:
        logger.warning("No article to publish")
        return {}

    # 1. 始终保存 Markdown 文件
    output_dir = settings.output_path
    filepath = _save_markdown(article, output_dir)

    # 1.5 保存中文翻译版（如果有）
    if article.markdown_content_zh:
        zh_filename = f"ai-daily-{article.date}-zh.md"
        zh_filepath = output_dir / zh_filename
        en_slug = f"ai-daily-{article.date}"
        zh_slug = f"ai-daily-{article.date}-zh"
        zh_desc = article.description_zh or article.description
        zh_desc_escaped = zh_desc.replace('"', '\\"')
        en_desc_escaped = article.description.replace('"', '\\"')
        zh_frontmatter = (
            f'---\n'
            f'title: "AI 日报 — {article.date}"\n'
            f'description: "{zh_desc_escaped}"\n'
            f'lang: "zh"\n'
            f'pairSlug: "{en_slug}"\n'
            f'---\n\n'
        )
        zh_filepath.write_text(zh_frontmatter + article.markdown_content_zh, encoding="utf-8")
        logger.info(f"Chinese version saved: {zh_filepath}")

        # 同步给英文版 frontmatter 补上 pairSlug（回写）
        en_content = filepath.read_text(encoding="utf-8")
        if "pairSlug" not in en_content:
            if en_content.startswith("---\n"):
                en_content = en_content.replace("---\n", f'---\nlang: "en"\npairSlug: "{zh_slug}"\n', 1)
            else:
                en_fm = f'---\nlang: "en"\npairSlug: "{zh_slug}"\ndescription: "{en_desc_escaped}"\n---\n\n'
                en_content = en_fm + en_content
            filepath.write_text(en_content, encoding="utf-8")

    # 2. 尝试发送邮件
    await _publish_newsletter(article)

    # 3. 尝试推送 Webhook
    await _publish_webhooks(article)

    logger.info(f"Publish complete: {filepath}")
    return {}
