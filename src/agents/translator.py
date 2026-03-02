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

⚠️ 最重要的规则（违反即失败）：
1. **保持与原文完全相同的 Markdown 结构**——标题层级、列表缩进、链接、分割线、空行全部照搬
2. **不得删除、合并或缩短任何内容**——每条新闻的描述/摘要必须完整翻译，字数应与原文相当
3. Top Stories 下的每条 ### 必须保留标题 + 完整的描述段落（2-3 句），**绝对不能只留标题**
4. Quick Bites 列表项格式必须是 `- **标题** — 描述`，列表前缀只用一个 `-`，不要写成 `- -`

其他规则：
5. 将所有英文文本翻译为自然流畅的中文——输出中不应保留英文描述性文字
6. 技术术语、模型名、公司名、专有名词保留原文（如 Qwen3.5, OpenAI, LangChain）
7. 所有 URL 保持不变
8. 翻译链接标签：[Source-xxx] → [来源-xxx]
9. 翻译固定章节标题：Top Stories → 今日焦点, Featured → 重点报道, Quick Bites → 快讯速览
10. 标题格式："AI 日报 — YYYY-MM-DD"
11. 直接输出翻译后的 Markdown，不要包裹在代码块中

--- English Newsletter ---
{markdown}"""


def _build_llm() -> ChatOpenAI:
    # 翻译优先使用独立配置的模型，否则复用全局模型
    model = settings.translate_model or settings.openai_model
    api_key = settings.translate_api_key or settings.openai_api_key
    base_url = settings.translate_base_url or settings.openai_base_url
    kwargs = {
        "model": model,
        "max_tokens": 32768,
    }
    if api_key:
        kwargs["api_key"] = api_key
    if base_url:
        kwargs["base_url"] = base_url
    return ChatOpenAI(**kwargs)


def _postprocess_zh_markdown(content: str) -> str:
    """后处理：修复翻译模型常见的 markdown 格式问题"""
    import re

    lines = content.split("\n")
    fixed_lines = []
    for line in lines:
        # 修复双点列表项："- - **xxx**" → "- **xxx**"
        line = re.sub(r"^(\s*)- - \*\*", r"\1- **", line)
        # 修复多余空格列表项："-  **xxx**" → "- **xxx**"
        line = re.sub(r"^(\s*)-\s{2,}\*\*", r"\1- **", line)
        fixed_lines.append(line)

    return "\n".join(fixed_lines)


def _validate_translation(original: str, translated: str) -> list[str]:
    """校验翻译质量，返回警告列表"""
    warnings = []
    # 检查 Top Stories 描述是否被丢失（原文有描述段落，翻译后没有）
    orig_top_count = original.count("### 1.") + original.count("### 2.") + original.count("### 3.")
    zh_top_count = translated.count("### 1.") + translated.count("### 2.") + translated.count("### 3.")
    if orig_top_count > 0 and zh_top_count < orig_top_count:
        warnings.append(f"Top Stories heading count mismatch: original={orig_top_count}, translated={zh_top_count}")

    # 检查翻译后的行数是否严重偏少（低于原文 60% 说明可能丢内容）
    orig_lines = len([l for l in original.split("\n") if l.strip()])
    zh_lines = len([l for l in translated.split("\n") if l.strip()])
    if orig_lines > 0 and zh_lines / orig_lines < 0.6:
        warnings.append(f"Translated content too short: {zh_lines} lines vs original {orig_lines} lines")

    return warnings


async def translate_to_chinese(markdown_en: str) -> str | None:
    """将英文日报 markdown 翻译为中文"""
    api_key = settings.translate_api_key or settings.openai_api_key
    if not api_key:
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

        # 后处理修复常见格式问题
        content = _postprocess_zh_markdown(content)

        # 质量校验
        warnings = _validate_translation(markdown_en, content)
        for w in warnings:
            logger.warning(f"Translation quality issue: {w}")

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
