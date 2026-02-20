"""Extractor Agent - 从清洗后的内容中提取结构化信息（LLM 驱动）"""

import asyncio
import json
import logging
from typing import Optional

from langchain_openai import ChatOpenAI

from src.config import settings
from src.graph.state import PipelineState
from src.models import CleanedItem, ExtractedItem, Sentiment

logger = logging.getLogger(__name__)

EXTRACTION_PROMPT = """You are an AI news analyst. Extract structured information from the following news item.

Title: {title}
Content: {content}
Source: {source_type}
URL: {url}
Platform Score: {platform_score}

Return a JSON object with these fields:
{{
    "title_en": "Concise English headline (max 12 words, capture the core news, e.g. 'RTX 5090 Achieves 16 FPS Real-Time Video Generation')",
    "summary": "2-3 sentence summary in English",
    "topics": ["topic tags, e.g.: LLM, Open Source, Multimodal, RL, Embodied AI, Industry, Dataset, Hardware, AI Safety, Tools"],
    "entities": ["key entities: company names, people, model names, product names"],
    "sentiment": "positive/neutral/negative",
    "importance_score": 1-10 importance rating (10 = most important)
}}

Importance scoring rules (be consistent):
- 9-10: Major product launch by top lab (OpenAI/Google/Anthropic/Meta), breakthrough SOTA result, critical industry event
- 7-8: Notable open-source model release, significant funding/acquisition, important benchmark result, viral demo
- 5-6: Interesting project/tool, meaningful update to existing product, good tutorial/analysis
- 3-4: Routine discussion, minor update, niche topic
- 1-2: Low-signal content, spam, off-topic

Also consider platform score as a signal: high upvotes/stars = likely more important.

Return JSON only, no other text."""


def _build_llm() -> ChatOpenAI:
    """构建 LLM 实例，强制 JSON 输出，temperature=0 保证评分稳定"""
    kwargs = {
        "model": settings.openai_model,
        "max_tokens": 16384,
        "temperature": 0,
        "model_kwargs": {"response_format": {"type": "json_object"}},
    }
    if settings.openai_api_key:
        kwargs["api_key"] = settings.openai_api_key
    if settings.openai_base_url:
        kwargs["base_url"] = settings.openai_base_url
    return ChatOpenAI(**kwargs)


def _parse_extraction(raw: str) -> Optional[dict]:
    """解析 LLM 返回的 JSON，支持多种格式"""
    text = raw.strip()

    # 1. 尝试直接解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 2. 提取 ```json ... ``` 代码块
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            try:
                return json.loads(part)
            except json.JSONDecodeError:
                continue

    # 3. 提取第一个 { ... } 块
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        chunk = text[start:end + 1]
        try:
            return json.loads(chunk)
        except json.JSONDecodeError:
            pass
        # 4. 容错：去掉行内注释、尾部逗号后再试
        try:
            cleaned = re.sub(r'//[^\n]*', '', chunk)          # 去 // 注释
            cleaned = re.sub(r',\s*([}\]])', r'\1', cleaned)  # 去尾部逗号
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

    logger.warning(f"JSON 解析失败，LLM 原始响应:\n{raw}")
    return None


def _fallback_extract(item: CleanedItem) -> ExtractedItem:
    """LLM 不可用时的降级提取方案"""
    return ExtractedItem(
        id=item.id,
        source_type=item.source_type,
        title=item.title,
        content=item.content,
        url=item.url,
        author=item.author,
        published_at=item.published_at,
        summary=item.content[:200] if item.content else item.title,
        topics=["AI"],
        entities=[],
        sentiment=Sentiment.NEUTRAL,
        importance_score=5.0,
    )


async def _extract_one(llm: ChatOpenAI, item: CleanedItem) -> ExtractedItem:
    """用 LLM 提取单条新闻的结构化信息"""
    prompt = EXTRACTION_PROMPT.format(
        title=item.title,
        content=item.content[:1000],  # 截断避免上下文过长
        source_type=item.source_type.value,
        url=item.url,
        platform_score=item.quality_score if hasattr(item, 'quality_score') else 0,
    )

    try:
        resp = await llm.ainvoke(prompt)
        parsed = _parse_extraction(resp.content)
        if not parsed:
            return _fallback_extract(item)

        sentiment_map = {
            "positive": Sentiment.POSITIVE,
            "neutral": Sentiment.NEUTRAL,
            "negative": Sentiment.NEGATIVE,
        }

        # 优先使用 LLM 生成的英文标题
        title_en = parsed.get("title_en", "").strip()
        return ExtractedItem(
            id=item.id,
            source_type=item.source_type,
            title=title_en if title_en else item.title,
            content=item.content,
            url=item.url,
            author=item.author,
            published_at=item.published_at,
            summary=parsed.get("summary", ""),
            topics=parsed.get("topics", []),
            entities=parsed.get("entities", []),
            sentiment=sentiment_map.get(parsed.get("sentiment", "neutral"), Sentiment.NEUTRAL),
            importance_score=float(parsed.get("importance_score", 5)),
        )
    except Exception as e:
        logger.error(f"LLM 提取失败 [{item.id}]: {type(e).__name__}: {e}")
        return _fallback_extract(item)


async def extractor_node(state: PipelineState) -> dict:
    """Extractor 节点：批量提取结构化信息"""
    deduped = state.get("deduped_items", [])
    if not deduped:
        logger.warning("没有去重后的数据需要提取")
        return {"extracted_items": []}

    logger.info(
        f"开始提取 {len(deduped)} 条新闻的结构化信息 ... "
        f"API_KEY={'SET' if settings.openai_api_key else 'EMPTY'} "
        f"MODEL={settings.openai_model} "
        f"BASE_URL={settings.openai_base_url or 'default'}"
    )

    # 检查 API key 是否配置
    if not settings.openai_api_key:
        logger.warning("未配置 OPENAI_API_KEY，使用降级方案提取")
        extracted = [_fallback_extract(item) for item in deduped]
    else:
        llm = _build_llm()
        # 并发批处理：每批 BATCH_SIZE 条，避免 rate limit
        BATCH_SIZE = 5
        extracted = []
        for i in range(0, len(deduped), BATCH_SIZE):
            batch = deduped[i : i + BATCH_SIZE]
            logger.info(f"  提取进度: {i+1}-{min(i+len(batch), len(deduped))}/{len(deduped)}")
            results = await asyncio.gather(*[_extract_one(llm, item) for item in batch])
            extracted.extend(results)

    # 按重要性排序
    extracted.sort(key=lambda x: x.importance_score, reverse=True)

    top_k = settings.top_k_featured
    featured = extracted[:top_k]
    brief = extracted[top_k:]

    logger.info(
        f"提取完成: {len(extracted)} 条 "
        f"(重点 {len(featured)} 条, 简要 {len(brief)} 条, "
        f"分界线 importance ≥ {featured[-1].importance_score if featured else 0:.1f})"
    )
    return {"extracted_items": extracted}
