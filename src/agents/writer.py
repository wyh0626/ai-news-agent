"""Writer Agent - 将提取后的结构化信息编排为可读的每日简报"""

import logging
from collections import defaultdict
from datetime import datetime, timezone

from langchain_openai import ChatOpenAI

from src.config import settings
from src.graph.state import PipelineState
from src.models import ArticleSection, ExtractedItem, GeneratedArticle

logger = logging.getLogger(__name__)

WRITER_PROMPT = """你是一位专业的 AI 领域新闻编辑。请根据以下新闻条目，撰写一份中文每日 AI 新闻简报。

⚠️ 你必须严格按照下方模板格式输出，不得增减章节、不得改变标题层级、不得改变列表格式。

━━━━━━ 输出模板（严格遵守） ━━━━━━

# AI 日报 — {date}

> 共收录 {total_count} 条 AI 领域资讯

## 🔥 今日焦点

从重点新闻中选出最重要的 2-3 条作为焦点，用 ### 编号标题展开：

### 1. 新闻标题

2-3 句话的摘要分析，包含背景与影响。[原始链接-来源](url)

### 2. 新闻标题

2-3 句话的摘要分析。[原始链接-来源](url)

## 📰 重点报道

将剩余重点新闻按话题分组，每组一个 ### 标题，组内用列表：

### 话题分类名

- **新闻标题** — 一句话摘要 + 简要分析。[原始链接-来源](url)
- **新闻标题** — 一句话摘要。[原始链接-来源](url)

## ⚡ 快讯速览

所有快讯用统一的单行列表，不分组：

- **新闻标题** — 一句话概括。[原始链接-来源](url)
- **新闻标题** — 一句话概括。[原始链接-来源](url)

---

*本报告由 AI News Agent 自动生成 | {date}*

━━━━━━ 模板结束 ━━━━━━

写作规则：
1. 「今日焦点」只放 2-3 条，用 ### 编号标题，每条 2-3 句分析
2. 「重点报道」按话题分组（如"开源模型""AI 安全""工具与框架"等），组内用 - **标题** — 摘要 格式
3. 「快讯速览」每条一行，- **标题** — 一句话 格式
4. 每条新闻都必须附 [原始链接-来源](url)，其中“来源”取自素材中的 source 字段（如 x、reddit、hackernews、arxiv、github、rss）
5. 来自不同数据源的同类新闻可合并叙述
6. 语言简洁专业，面向 AI 从业者
7. 请直接输出 Markdown 内容，不要包裹在代码块中

## 重点新闻素材 (importance ≥ {threshold}，共 {featured_count} 条)
{featured_json}

## 快讯素材 (共 {brief_count} 条)
{brief_json}"""


def _build_llm() -> ChatOpenAI:
    kwargs = {
        "model": settings.openai_model,
        "max_tokens": 32768,
    }
    if settings.openai_api_key:
        kwargs["api_key"] = settings.openai_api_key
    if settings.openai_base_url:
        kwargs["base_url"] = settings.openai_base_url
    return ChatOpenAI(**kwargs)


def _group_by_topic(items: list[ExtractedItem]) -> dict[str, list[ExtractedItem]]:
    """按主题聚类新闻"""
    groups: dict[str, list[ExtractedItem]] = defaultdict(list)
    for item in items:
        primary_topic = item.topics[0] if item.topics else "其他"
        groups[primary_topic].append(item)
    return dict(groups)


def _build_fallback_markdown(items: list[ExtractedItem], today: str) -> str:
    """LLM 不可用时的降级模板渲染，与 LLM 输出格式保持一致"""
    lines = [
        f"# AI 日报 — {today}",
        "",
        f"> 共收录 {len(items)} 条 AI 领域资讯",
        "",
    ]

    # 今日焦点：importance >= 8 的前 3 条
    top_items = [i for i in items if i.importance_score >= 8][:3]
    if top_items:
        lines.append("## 🔥 今日焦点")
        lines.append("")
        for idx, item in enumerate(top_items, 1):
            summary = item.summary or item.title
            lines.append(f"### {idx}. {item.title}")
            lines.append("")
            src = item.source_type.value
            lines.append(f"{summary} [原始链接-{src}]({item.url})")
            lines.append("")

    # 重点报道：按话题分组，排除已在焦点中展示的
    top_ids = {id(i) for i in top_items}
    featured = [i for i in items if i.importance_score >= 7 and id(i) not in top_ids]
    if featured:
        groups = _group_by_topic(featured)
        lines.append("## 📰 重点报道")
        lines.append("")
        for topic, topic_items in groups.items():
            lines.append(f"### {topic}")
            lines.append("")
            for item in topic_items:
                summary = item.summary or item.title
                src = item.source_type.value
                lines.append(f"- **{item.title}** — {summary} [原始链接-{src}]({item.url})")
            lines.append("")

    # 快讯速览
    brief = [i for i in items if i.importance_score < 7]
    if brief:
        lines.append("## ⚡ 快讯速览")
        lines.append("")
        for item in brief:
            summary = item.summary or item.title
            src = item.source_type.value
            lines.append(f"- **{item.title}** — {summary} [原始链接-{src}]({item.url})")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*本报告由 AI News Agent 自动生成 | {today}*")

    return "\n".join(lines)


def _normalize_source_links(markdown: str) -> str:
    """后处理：统一所有链接标签为 [原始链接-来源](url) 格式"""
    import re

    # 域名 → 来源标签映射
    domain_map = {
        "x.com": "x", "twitter.com": "x",
        "reddit.com": "reddit",
        "news.ycombinator.com": "hackernews", "hn.algolia.com": "hackernews",
        "arxiv.org": "arxiv",
        "github.com": "github",
        "huggingface.co": "huggingface",
    }

    def _get_source(url: str) -> str:
        for domain, label in domain_map.items():
            if domain in url:
                return label
        return "rss"

    # 匹配所有 markdown 链接 [任意文本](url)
    def replacer(m):
        text = m.group(1)
        url = m.group(2)
        source = _get_source(url)
        return f"[原始链接-{source}]({url})"

    return re.sub(r'\[([^\]]*)\]\((https?://[^\)]+)\)', replacer, markdown)


def _items_to_json(items: list[ExtractedItem], brief: bool = False) -> str:
    """将新闻条目转为 JSON 字符串；brief=True 时只保留必要字段以节省 token"""
    import json

    data = []
    for item in items:
        if brief:
            data.append({
                "title": item.title,
                "source": item.source_type.value,
                "url": item.url,
            })
        else:
            data.append({
                "title": item.title,
                "summary": item.summary,
                "topics": item.topics,
                "importance_score": item.importance_score,
                "source": item.source_type.value,
                "url": item.url,
            })
    return json.dumps(data, ensure_ascii=False, indent=2)


def _split_featured_brief(
    items: list[ExtractedItem],
) -> tuple[list[ExtractedItem], list[ExtractedItem]]:
    """按 importance_score 将新闻分为重点和简要两层

    items 已按 importance_score 降序排列（由 Extractor 保证）
    """
    top_k = settings.top_k_featured
    featured = items[:top_k]
    brief = items[top_k:]
    return featured, brief


async def writer_node(state: PipelineState) -> dict:
    """Writer 节点：生成每日新闻简报（重点展开 + 快讯速览）"""
    extracted = state.get("extracted_items", [])
    if not extracted:
        logger.warning("没有提取数据，跳过撰稿")
        return {"article": None}

    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    featured, brief = _split_featured_brief(extracted)
    threshold = featured[-1].importance_score if featured else 0

    logger.info(
        f"开始撰写 {today} 日报: "
        f"重点 {len(featured)} 条 + 快讯 {len(brief)} 条 "
        f"(分界线 importance ≥ {threshold:.1f})"
    )

    groups = _group_by_topic(extracted)
    sections = [ArticleSection(topic=t, items=items) for t, items in groups.items()]

    # 尝试用 LLM 生成
    markdown = ""
    if settings.openai_api_key:
        try:
            llm = _build_llm()
            prompt = WRITER_PROMPT.format(
                date=today,
                total_count=len(extracted),
                featured_count=len(featured),
                brief_count=len(brief),
                threshold=threshold,
                featured_json=_items_to_json(featured),
                brief_json=_items_to_json(brief, brief=True),
            )
            resp = await llm.ainvoke(prompt)
            markdown = resp.content
            # 完整性检查：LLM 可能截断，缺少章节则降级
            required_sections = ["今日焦点", "快讯速览"]
            missing = [s for s in required_sections if s not in markdown]
            if missing:
                logger.warning(f"LLM 输出不完整，缺少章节: {missing}，降级为模板生成")
                markdown = _build_fallback_markdown(extracted, today)
            else:
                # LLM 输出的链接标签可能不统一，用后处理修正
                markdown = _normalize_source_links(markdown)
                logger.info("LLM 撰稿完成")
        except Exception as e:
            logger.error(f"LLM 撰稿失败，降级为模板生成: {e}")
            markdown = _build_fallback_markdown(extracted, today)
    else:
        logger.info("未配置 LLM，使用模板生成")
        markdown = _build_fallback_markdown(extracted, today)

    article = GeneratedArticle(
        title=f"AI 日报 — {today}",
        date=today,
        sections=sections,
        markdown_content=markdown,
        item_count=len(extracted),
    )

    logger.info(f"撰稿完成: {article.title}, {article.item_count} 条新闻")
    return {"article": article}
