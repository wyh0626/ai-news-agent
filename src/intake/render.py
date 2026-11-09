import html
import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from src.models import GeneratedArticle


def md(text):
    return re.sub(r"([\\`*_{}\[\]#!|])", r"\\\1", html.escape(text, quote=False))


def news_markdown(item):
    news = item["news"]
    parts = [f"## {md(news['title_zh'])}", md(news["body_zh"])]
    if item["image"]:
        label = {
            "native_zh": "X 中文页面截图",
            "grok_x_original": "X 原帖截图 · Grok 提供",
            "grok_article_original": "外部新闻原文截图 · Grok 提供",
        }.get(item["screenshot_status"], "X 原文截图（未翻译）")
        parts.append(f"![{label}](/news-shots/{item['image']})")
    if news["tweet_text_zh"]:
        parts += ["**推文中文译文（Grok 提供）**", md(news["tweet_text_zh"])]
    if news["uncertainties"]:
        parts += ["**待核实**", "\n".join(f"- {md(t)}" for t in news["uncertainties"])]
    parts.append("**信源**")
    parts += [f"- [{md(s['label'])}](<{s['url']}>)" for s in news["sources"]]
    if news["tweet_url"]:
        parts.append(f"- [原推文](<{news['tweet_url']}>)")
    parts.append(
        f"原帖发布时间：{news.get('published_at') or news.get('published_date') or '未确认'}"
    )
    return "\n\n".join(parts)


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def export_daily(store, day: str, data_dir: Path, output: Path, site: Path | None = None):
    # Bucket by local receipt date, so delayed imports do not disappear into old reports.
    datetime.strptime(day, "%Y-%m-%d")
    items = [
        r
        for r in reversed(store.list_news(100000))
        if datetime.fromtimestamp(r["created"], ZoneInfo("Asia/Shanghai")).date().isoformat() == day
    ]
    if not items:
        raise ValueError("当天没有已接收新闻（按北京时间接收日归档）")
    article = GeneratedArticle(
        title=f"AI 资讯 — {day}",
        date=day,
        description=" · ".join(i["news"]["title_zh"] for i in items[:3])[:200],
        markdown_content_zh="\n\n---\n\n".join(news_markdown(i) for i in items),
        item_count=len(items),
    )
    frontmatter = (
        "---\n"
        + "\n".join(
            f"{k}: {json.dumps(v, ensure_ascii=False)}"
            for k, v in {
                "title": article.title,
                "description": article.description,
                "pubDate": day,
                "category": "daily",
                "lang": "zh",
            }.items()
        )
        + "\n---\n\n"
    )
    filename = f"grok-daily-{day}-zh.md"
    targets = [(output / filename, output / "news-shots")]
    if site:
        targets.append((site / "src/content/blog" / filename, site / "public/news-shots"))
    for doc, assets in targets:
        for item in items:
            if item["image"]:
                assets.mkdir(parents=True, exist_ok=True)
                shutil.copy2(data_dir / "images" / item["image"], assets / item["image"])
        atomic_write(doc, frontmatter + article.markdown_content_zh + "\n")
    return {
        "path": str(output / filename),
        "count": len(items),
        "images": sum(bool(i["image"]) for i in items),
    }
