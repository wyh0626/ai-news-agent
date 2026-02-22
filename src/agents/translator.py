"""Translator Agent - 将英文日报翻译为中文版

放在 writer 之后、publisher 之前，用 LLM 将英文 markdown 翻译为中文，
输出中文版日报文件 (ai-daily-YYYY-MM-DD-zh.md)。
"""

import logging

from langchain_openai import ChatOpenAI

from src.config import settings
from src.graph.state import PipelineState

logger = logging.getLogger(__name__)

TRANSLATE_PROMPT = """你是一位专业的 AI 新闻翻译。请将以下英文 AI 日报翻译为中文。

规则：
1. 保持完全相同的 Markdown 结构（标题、列表、链接、分割线）
2. 将所有英文文本翻译为自然流畅的中文——输出中不应保留英文描述性文字
3. 包括：章节标题、子分组标题（### Topic Name）、新闻标题（加粗文本）、摘要和所有描述
4. ⚠️ 特别注意：Top Stories 下的每条 ### 编号标题（如 ### 1. Some Title）中的标题文字必须翻译为中文，编号保留
5. 技术术语、模型名、公司名、专有名词保留原文（如 Qwen3.5, OpenAI, LangChain）
6. 所有 URL 保持不变
7. 翻译链接标签：[Source-xxx] → [来源-xxx]
8. 翻译固定章节标题：Top Stories → 今日焦点, Featured → 重点报道, Quick Bites → 快讯速览
9. 标题格式："AI 日报 — YYYY-MM-DD"
10. 直接输出翻译后的 Markdown，不要包裹在代码块中

--- English Newsletter ---
{markdown}"""


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


async def translate_to_chinese(markdown_en: str) -> str | None:
    """将英文日报 markdown 翻译为中文"""
    if not settings.openai_api_key:
        logger.info("LLM not configured, skipping Chinese translation")
        return None

    try:
        llm = _build_llm()
        prompt = TRANSLATE_PROMPT.format(markdown=markdown_en)
        resp = await llm.ainvoke(prompt)
        content = resp.content

        # 基本校验
        if "##" not in content or len(content) < 200:
            logger.warning("Chinese translation output incomplete, skipping")
            return None

        logger.info("Chinese newsletter translation complete")
        return content
    except Exception as e:
        logger.warning(f"Chinese translation failed: {e}")
        return None


async def translator_node(state: PipelineState) -> dict:
    """Translator 节点：将英文日报翻译为中文版"""
    article = state.get("article")
    if not article or not article.markdown_content:
        return {}

    logger.info("Translating newsletter to Chinese ...")
    zh_markdown = await translate_to_chinese(article.markdown_content)

    if zh_markdown:
        article.markdown_content_zh = zh_markdown
        return {"article": article}

    return {}
