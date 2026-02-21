"""AI 相关性过滤器 — 用 LLM 批量判断标题是否与 AI 相关

设计思路：
- 把 30-50 个标题一次性发给 LLM，让它返回 AI 相关条目的序号
- 输入 ~500 tokens，输出 ~50 tokens，每次调用约 $0.001
- 自动适应新术语（无需手动维护关键词表）
- LLM 不可用时降级为核心关键词匹配
"""

import asyncio
import json
import logging
import re
from typing import Sequence

from langchain_openai import ChatOpenAI

from src.config import settings

logger = logging.getLogger(__name__)

# 极小核心关键词集（仅用于 LLM 不可用时的降级方案，不需要维护）
_FALLBACK_CORE_KEYWORDS = [
    "ai", "llm", "gpt", "machine learning", "deep learning",
    "neural network", "transformer", "nlp", "diffusion",
    "reinforcement learning", "computer vision",
]

FILTER_PROMPT = """你是一个 AI 领域资讯分类专家。
请判断以下编号标题中，哪些与 AI / 人工智能 / 机器学习 / 深度学习 / 大语言模型 / 生成式 AI 等领域**直接相关**。

✅ 相关（必须直接涉及 AI 技术本身）：
- AI 模型发布、评测、部署、推理
- 机器学习 / 深度学习研究与应用
- AI 产品、工具、框架、平台
- AI 芯片、硬件、基础设施
- AI 安全、对齐、可解释性研究
- AI 相关公司技术动态（OpenAI、Google DeepMind、Anthropic、Meta AI 等）
- 数据集、标注、训练方法
- 任何直接使用或构建 AI 技术的项目

❌ 不相关（即使提到 AI 公司或 AI 一词也要排除）：
- 纯政治新闻（选举、战争、外交、制裁、贸易战）
- 军事行动、武器、国家安全（非 AI 安全）
- 体育、娱乐、名人八卦
- 经济/金融新闻（非 AI 投融资）
- 人权、社会议题（非 AI 伦理研究）
- 仅因为某人在 AI 公司工作就发的无关内容

标题列表：
{titles}

请**只返回** AI 相关条目的编号，用 JSON 数组格式，如: [0, 2, 5, 7]
如果全部相关返回所有编号，全部无关返回空数组 []。
只返回 JSON 数组，不要返回任何其他内容。"""


def _build_llm() -> ChatOpenAI:
    kwargs = {
        "model": settings.openai_model,
        "max_tokens": 16384,
    }
    if settings.openai_api_key:
        kwargs["api_key"] = settings.openai_api_key
    if settings.openai_base_url:
        kwargs["base_url"] = settings.openai_base_url
    return ChatOpenAI(**kwargs)


def _strip_html(text: str) -> str:
    """移除 HTML 标签，保留纯文本"""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&\w+;", " ", text)  # &amp; &lt; etc.
    return re.sub(r"\s+", " ", text).strip()


def _parse_indices(raw: str, max_idx: int) -> list[int]:
    """解析 LLM 返回的序号数组"""
    text = raw.strip()
    # 处理 markdown code block
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    try:
        indices = json.loads(text)
        if isinstance(indices, list):
            return [i for i in indices if isinstance(i, int) and 0 <= i < max_idx]
    except json.JSONDecodeError:
        pass

    # 备选：尝试提取所有数字
    import re
    numbers = re.findall(r"\d+", text)
    return [int(n) for n in numbers if 0 <= int(n) < max_idx]


def _fallback_filter(titles: Sequence[str]) -> list[int]:
    """LLM 不可用时的降级方案：核心关键词匹配"""
    result = []
    for i, title in enumerate(titles):
        text = title.lower()
        if any(kw in text for kw in _FALLBACK_CORE_KEYWORDS):
            result.append(i)
    return result


BATCH_SIZE = 25  # 每批最多 25 条，避免 prompt 过长导致 LLM 空响应
MAX_CONCURRENT = 8  # 最大并发批次数，避免触发限流


async def _filter_one_batch(
    llm: ChatOpenAI,
    titles: list[str],
    descriptions: list[str] | None,
    offset: int,
) -> list[int]:
    """单批次 LLM 过滤，返回全局索引列表"""
    lines = []
    for i, title in enumerate(titles):
        clean_title = _strip_html(title)
        line = f"{i}. {clean_title}"
        if descriptions and i < len(descriptions) and descriptions[i]:
            desc = _strip_html(descriptions[i])[:60]
            line += f" — {desc}"
        lines.append(line)

    titles_text = "\n".join(lines)
    prompt = FILTER_PROMPT.format(titles=titles_text)
    resp = await llm.ainvoke(prompt)
    raw_resp = (resp.content or "").strip()
    logger.debug(f"LLM AI filter batch response (offset={offset}): {raw_resp[:300]}")

    if not raw_resp:
        logger.warning(f"LLM returned empty response (offset={offset}), falling back to keyword filter")
        local = _fallback_filter(titles)
        return [idx + offset for idx in local]

    local_indices = _parse_indices(raw_resp, len(titles))
    return [idx + offset for idx in local_indices]


async def batch_filter_ai(
    titles: Sequence[str],
    descriptions: Sequence[str] | None = None,
) -> list[int]:
    """批量判断标题是否与 AI 相关，返回 AI 相关条目的索引列表

    自动分批（每批 25 条），合并结果。
    LLM 不可用时降级为核心关键词匹配。

    Args:
        titles: 标题列表
        descriptions: 可选的描述/摘要列表（拼接到标题后增加判断准确度）

    Returns:
        AI 相关条目的索引列表（0-based）
    """
    if not titles:
        return []

    titles_list = list(titles)
    descs_list = list(descriptions) if descriptions else None

    # LLM 不可用时降级
    if not settings.openai_api_key:
        logger.info("LLM not configured, using fallback keyword filter")
        return _fallback_filter(titles_list)

    try:
        llm = _build_llm()
        semaphore = asyncio.Semaphore(MAX_CONCURRENT)

        async def _limited_batch(start: int) -> list[int]:
            end = min(start + BATCH_SIZE, len(titles_list))
            batch_titles = titles_list[start:end]
            batch_descs = descs_list[start:end] if descs_list else None
            async with semaphore:
                return await _filter_one_batch(llm, batch_titles, batch_descs, offset=start)

        # 并行执行所有批次
        starts = list(range(0, len(titles_list), BATCH_SIZE))
        results = await asyncio.gather(*[_limited_batch(s) for s in starts])
        all_indices: list[int] = []
        for batch_result in results:
            all_indices.extend(batch_result)
        all_indices.sort()

        logger.info(
            f"LLM AI filter: {len(titles_list)} titles → {len(all_indices)} AI-related"
            + (f" ({len(starts)} batches)" if len(starts) > 1 else "")
        )
        return all_indices
    except Exception as e:
        logger.warning(f"LLM AI filter failed, falling back to keyword filter: {e}")
        return _fallback_filter(titles_list)
