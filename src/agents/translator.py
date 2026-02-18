"""Translator Agent - 将中文日报翻译为英文版

放在 publisher 之前或之后，用 LLM 将中文 markdown 翻译为英文，
输出英文版日报文件 (ai-daily-YYYY-MM-DD-en.md)。
"""

import logging

from langchain_openai import ChatOpenAI

from src.config import settings
from src.graph.state import PipelineState

logger = logging.getLogger(__name__)

TRANSLATE_PROMPT = """You are a professional AI news translator. Translate the following Chinese AI daily newsletter into English.

Rules:
1. Keep the exact same Markdown structure (headings, lists, links, horizontal rules)
2. Translate ALL Chinese text to natural, fluent English — no Chinese characters should remain in the output
3. This includes: section headers, sub-group titles (### 话题名), item titles (bold text), summaries, and all descriptions
4. Keep technical terms, model names, company names, and proper nouns in their original form (e.g. Qwen3.5, OpenAI, LangChain)
5. Keep all URLs unchanged
6. Translate link labels: [原始链接-xxx] → [Source-xxx]
7. Translate fixed section headers: 今日焦点 → Top Stories, 重点报道 → Featured, 快讯速览 → Quick Bites
8. The title format: "AI Daily — YYYY-MM-DD"
9. Output the translated Markdown directly, no code blocks

--- Chinese Newsletter ---
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


async def translate_to_english(markdown_zh: str) -> str | None:
    """将中文日报 markdown 翻译为英文"""
    if not settings.openai_api_key:
        logger.info("未配置 LLM，跳过英文翻译")
        return None

    try:
        llm = _build_llm()
        prompt = TRANSLATE_PROMPT.format(markdown=markdown_zh)
        resp = await llm.ainvoke(prompt)
        content = resp.content

        # 基本校验
        if "##" not in content or len(content) < 200:
            logger.warning("英文翻译输出不完整，跳过")
            return None

        logger.info("英文日报翻译完成")
        return content
    except Exception as e:
        logger.warning(f"英文翻译失败: {e}")
        return None


async def translator_node(state: PipelineState) -> dict:
    """Translator 节点：将中文日报翻译为英文版，存入 article 的 metadata"""
    article = state.get("article")
    if not article or not article.markdown_content:
        return {}

    logger.info("开始翻译英文版日报 ...")
    en_markdown = await translate_to_english(article.markdown_content)

    if en_markdown:
        article.markdown_content_en = en_markdown
        return {"article": article}

    return {}
