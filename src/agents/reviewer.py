"""Reviewer Agent - 写前审稿：合并同一事件的重复新闻

放在 extractor 与 writer 之间，用 LLM 识别报道同一事件的多条新闻，
保留最高分的一条并将其他信息合入，避免日报中出现重复内容。
"""

import json
import logging

from langchain_openai import ChatOpenAI

from src.config import settings
from src.graph.state import PipelineState
from src.models import ExtractedItem

logger = logging.getLogger(__name__)

MERGE_PROMPT = """You are an AI news editor. Review the following news list and identify **duplicate or highly similar items** that cover the same event or topic.

Merge criteria:
- Same product launch, same paper, same project, same news event
- Different discussion threads about the same GitHub repository
- Different angles on the same model release (e.g. "Qwen3.5 released" and "Qwen3.5 weights now available")

NOT duplicates:
- Similar topic but different specific content (e.g. two different AI safety papers)

Return a JSON object in this format:

{{"groups": [
  {{"group": [0, 3, 7], "keep": 0, "reason": "All about Qwen3.5 release"}},
  {{"group": [2, 5], "keep": 2, "reason": "Same GitHub project"}}
]}}

If no merges needed, return {{"groups": []}}. Return JSON only, no other text.

--- News List ---
{items_text}"""


def _build_llm() -> ChatOpenAI:
    kwargs = {
        "model": settings.openai_model,
        "max_tokens": 16384,
        "model_kwargs": {"response_format": {"type": "json_object"}},
    }
    if settings.openai_api_key:
        kwargs["api_key"] = settings.openai_api_key
    if settings.openai_base_url:
        kwargs["base_url"] = settings.openai_base_url
    return ChatOpenAI(**kwargs)


def _parse_merge_groups(raw: str) -> list[dict]:
    """解析 LLM 返回的合并分组 JSON，支持 {"groups":[...]} 和 [...] 两种格式"""
    text = raw.strip()

    def _extract_groups(obj) -> list[dict] | None:
        """从解析结果中提取 groups 列表"""
        if isinstance(obj, list):
            return obj
        if isinstance(obj, dict) and "groups" in obj:
            return obj["groups"]
        return None

    # 直接解析
    try:
        result = _extract_groups(json.loads(text))
        if result is not None:
            return result
    except json.JSONDecodeError:
        pass

    # 提取 ```json ... ```
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            try:
                result = _extract_groups(json.loads(part))
                if result is not None:
                    return result
            except json.JSONDecodeError:
                continue

    # 提取 { ... } 或 [ ... ]
    for open_c, close_c in [("{", "}"), ("[", "]")]:
        start = text.find(open_c)
        end = text.rfind(close_c)
        if start != -1 and end != -1 and end > start:
            try:
                result = _extract_groups(json.loads(text[start:end + 1]))
                if result is not None:
                    return result
            except json.JSONDecodeError:
                pass

    logger.warning(f"合并分组 JSON 解析失败，LLM 原始响应:\n{text}")
    return []


def _items_to_text(items: list[ExtractedItem]) -> str:
    """将条目列表转为带序号的文本，供 LLM 判断"""
    lines = []
    for i, item in enumerate(items):
        lines.append(
            f"[{i}] Title: {item.title}\n"
            f"    Source: {item.source_type.value} | URL: {item.url}\n"
            f"    Summary: {item.summary[:100]}"
        )
    return "\n".join(lines)


def _merge_items(items: list[ExtractedItem], groups: list[dict]) -> list[ExtractedItem]:
    """根据合并分组，保留 keep 条目，丢弃其余重复条目"""
    to_remove: set[int] = set()

    for g in groups:
        indices = g.get("group", [])
        keep_idx = g.get("keep", indices[0] if indices else 0)
        reason = g.get("reason", "")

        if not indices or len(indices) < 2:
            continue

        # 验证索引合法性
        valid = all(0 <= idx < len(items) for idx in indices)
        if not valid:
            logger.warning(f"合并分组索引越界: {indices}, 跳过")
            continue

        # keep 条目吸收其他条目的信息
        keep_item = items[keep_idx]
        merged_urls = []
        for idx in indices:
            if idx != keep_idx:
                to_remove.add(idx)
                other = items[idx]
                if other.url and other.url != keep_item.url:
                    merged_urls.append(other.url)
                # 取更高的 importance_score
                if other.importance_score > keep_item.importance_score:
                    keep_item.importance_score = other.importance_score

        logger.info(
            f"合并 {len(indices)} 条 → 保留 [{keep_idx}] '{keep_item.title}' "
            f"(原因: {reason})"
        )

    result = [item for i, item in enumerate(items) if i not in to_remove]
    return result


async def reviewer_node(state: PipelineState) -> dict:
    """Reviewer 节点：写前审稿，合并同一事件的重复新闻"""
    extracted = state.get("extracted_items", [])
    if len(extracted) <= 5:
        logger.info(f"新闻条目较少 ({len(extracted)} 条)，跳过审稿合并")
        return {}

    logger.info(f"审稿开始: {len(extracted)} 条新闻，检查重复事件 ...")

    # URL 精确去重（同一 URL 直接去掉）
    seen_urls: dict[str, int] = {}
    url_dupes: set[int] = set()
    for i, item in enumerate(extracted):
        if item.url in seen_urls:
            url_dupes.add(i)
            logger.info(f"URL 重复: [{i}] '{item.title}' 与 [{seen_urls[item.url]}] 相同 URL")
        else:
            seen_urls[item.url] = i

    if url_dupes:
        extracted = [item for i, item in enumerate(extracted) if i not in url_dupes]
        logger.info(f"URL 去重: 移除 {len(url_dupes)} 条，剩余 {len(extracted)} 条")

    # LLM 事件级合并
    if not settings.openai_api_key:
        logger.info("未配置 LLM，跳过事件级合并")
        return {"extracted_items": extracted}

    try:
        llm = _build_llm()
        items_text = _items_to_text(extracted)
        prompt = MERGE_PROMPT.format(items_text=items_text)
        resp = await llm.ainvoke(prompt)
        groups = _parse_merge_groups(resp.content)

        if groups:
            before = len(extracted)
            extracted = _merge_items(extracted, groups)
            logger.info(f"事件合并: {before} → {len(extracted)} 条 (合并 {len(groups)} 组)")
        else:
            logger.info("未发现需要合并的重复事件")

    except Exception as e:
        logger.warning(f"LLM 审稿失败，跳过合并: {e}")

    logger.info(f"审稿完成: 最终 {len(extracted)} 条新闻")
    return {"extracted_items": extracted}
