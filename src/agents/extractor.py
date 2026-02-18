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

EXTRACTION_PROMPT = """你是一个 AI 新闻分析师。请从以下新闻条目中提取结构化信息。

新闻标题: {title}
新闻内容: {content}
来源: {source_type}
URL: {url}

请以 JSON 格式返回以下字段:
{{
    "title_zh": "精准的中文标题（15字以内，概括核心内容，如：'RTX 5090 上 0.6B 模型推理速度测试'）",
    "summary": "2-3句话的核心摘要（中文）",
    "topics": ["主题分类标签列表，如: LLM, 开源模型, 多模态, RL, 具身智能, 行业应用, 数据集, 芯片硬件, AI安全, 工具框架"],
    "entities": ["关键实体列表: 公司名、人物、模型名、产品名"],
    "sentiment": "positive/neutral/negative",
    "importance_score": 1到10的重要性评分（10最重要）
}}

注意事项:
- title_zh 和 summary 必须准确区分"人物"和"产品/项目"：如某人加入某公司，主语是人不是产品（如"OpenClaw 作者加入 OpenAI"而非"ClawdBot 入职 OpenAI"）
- 不要臆测未提及的细节，忠实于原文内容

评分标准:
- 8-10: 重大发布、突破性研究、行业重大事件
- 5-7: 值得关注的更新、有趣的项目
- 1-4: 常规讨论、小更新

只返回 JSON，不要返回其他内容。"""


def _build_llm() -> ChatOpenAI:
    """构建 LLM 实例"""
    kwargs = {
        "model": settings.openai_model,
        "max_tokens": 4096,
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
        try:
            return json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            pass

    logger.warning(f"JSON 解析失败: {raw[:200]}...")
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

        # 优先使用 LLM 生成的中文标题
        title_zh = parsed.get("title_zh", "").strip()
        return ExtractedItem(
            id=item.id,
            source_type=item.source_type,
            title=title_zh if title_zh else item.title,
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
        logger.error(f"LLM 提取失败 [{item.id}]: {e}")
        return _fallback_extract(item)


async def extractor_node(state: PipelineState) -> dict:
    """Extractor 节点：批量提取结构化信息"""
    deduped = state.get("deduped_items", [])
    if not deduped:
        logger.warning("没有去重后的数据需要提取")
        return {"extracted_items": []}

    logger.info(f"开始提取 {len(deduped)} 条新闻的结构化信息 ...")

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
