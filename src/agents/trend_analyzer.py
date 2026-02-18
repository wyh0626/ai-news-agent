"""Trend Analyzer - 基于长期记忆的趋势分析和专题深度报告（v0.4）"""

import json
import logging
from datetime import datetime, timezone

from langchain_openai import ChatOpenAI

from src.config import settings

logger = logging.getLogger(__name__)

TREND_REPORT_PROMPT = """你是一位专业的 AI 行业分析师。请根据以下过去 {days} 天的话题热度数据和近期新闻，
撰写一份中文 AI 行业趋势分析报告。

## 话题热度数据 (按热度排序)
{topics_json}

## 近期高分新闻
{articles_json}

要求：
1. 用 Markdown 格式
2. 分析 3-5 个核心趋势
3. 每个趋势给出数据支撑和简要分析
4. 最后给出未来一周的关注建议
5. 语言专业、数据驱动，面向 AI 从业者

请直接输出 Markdown 内容。"""

DEEPDIVE_PROMPT = """你是一位专业的 AI 行业分析师。请围绕话题「{topic}」撰写一份深度分析报告。

## 相关新闻
{articles_json}

要求：
1. 用 Markdown 格式
2. 概述话题背景和重要性
3. 梳理关键事件时间线
4. 分析各方（公司/研究者）的动向
5. 展望未来发展方向
6. 语言专业，引用具体来源

请直接输出 Markdown 内容。"""


def _build_llm() -> ChatOpenAI:
    kwargs = {"model": settings.openai_model, "max_tokens": 16384}
    if settings.openai_api_key:
        kwargs["api_key"] = settings.openai_api_key
    if settings.openai_base_url:
        kwargs["base_url"] = settings.openai_base_url
    return ChatOpenAI(**kwargs)


async def generate_trend_report(days: int = 7) -> str | None:
    """生成周趋势分析报告"""
    try:
        from src.storage.postgres import get_postgres

        pg = await get_postgres()
        if not pg.available:
            logger.warning("PostgreSQL 不可用，无法生成趋势报告")
            return None

        # 获取话题热度数据
        trending = await pg.get_trending_topics(days=days, limit=20)
        if not trending:
            logger.info("没有足够的话题数据生成趋势报告")
            return None

        topics_json = json.dumps(trending, ensure_ascii=False, indent=2, default=str)

        # 获取近期高分文章
        articles = []
        async with pg._pool.connection() as conn:
            rows = await conn.execute(
                """SELECT title, summary, topics, source_type, url, importance_score
                   FROM article_index
                   WHERE created_at >= NOW() - INTERVAL '%s days'
                   ORDER BY importance_score DESC
                   LIMIT 30""",
                (days,),
            )
            async for row in rows:
                articles.append({
                    "title": row[0], "summary": row[1], "topics": row[2],
                    "source": row[3], "url": row[4], "score": row[5],
                })

        articles_json = json.dumps(articles, ensure_ascii=False, indent=2, default=str)

        if not settings.openai_api_key:
            return _fallback_trend_report(trending, articles, days)

        llm = _build_llm()
        prompt = TREND_REPORT_PROMPT.format(
            days=days, topics_json=topics_json, articles_json=articles_json
        )
        resp = await llm.ainvoke(prompt)
        return resp.content

    except Exception as e:
        logger.error(f"趋势报告生成失败: {e}")
        return None


async def generate_deepdive_report(topic: str) -> str | None:
    """生成专题深度报告"""
    try:
        from src.storage.postgres import get_postgres

        pg = await get_postgres()
        if not pg.available:
            return None

        # 获取该话题相关文章
        async with pg._pool.connection() as conn:
            rows = await conn.execute(
                """SELECT title, summary, url, source_type, importance_score, published_at
                   FROM article_index
                   WHERE %s = ANY(topics)
                   ORDER BY published_at DESC
                   LIMIT 20""",
                (topic,),
            )
            articles = []
            async for row in rows:
                articles.append({
                    "title": row[0], "summary": row[1], "url": row[2],
                    "source": row[3], "score": row[4], "date": str(row[5]),
                })

        if not articles:
            return None

        articles_json = json.dumps(articles, ensure_ascii=False, indent=2, default=str)

        if not settings.openai_api_key:
            return f"# 专题: {topic}\n\n共 {len(articles)} 篇相关文章。需要 LLM 生成深度分析。"

        llm = _build_llm()
        prompt = DEEPDIVE_PROMPT.format(topic=topic, articles_json=articles_json)
        resp = await llm.ainvoke(prompt)
        return resp.content

    except Exception as e:
        logger.error(f"专题报告生成失败: {e}")
        return None


def _fallback_trend_report(trending: list, articles: list, days: int) -> str:
    """LLM 不可用时的降级趋势报告"""
    lines = [
        f"# 📊 AI 行业趋势周报",
        f"",
        f"> 过去 {days} 天的话题热度分析",
        "",
        "## 热门话题 Top 10",
        "",
    ]
    for i, t in enumerate(trending[:10], 1):
        lines.append(f"{i}. **{t['topic']}** — 出现 {t['count']} 次，活跃 {t['active_days']} 天")
    lines.append("")
    lines.append("## 重要新闻")
    lines.append("")
    for a in articles[:10]:
        lines.append(f"- [{a['title']}]({a.get('url', '')})")
    lines.append("")
    lines.append("---")
    lines.append(f"*需要配置 LLM 以获取深度分析*")
    return "\n".join(lines)
