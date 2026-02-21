"""Pydantic 数据模型 - Pipeline 各阶段的数据结构定义"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class SourceType(str, Enum):
    REDDIT = "reddit"
    HACKERNEWS = "hackernews"
    ARXIV = "arxiv"
    GITHUB = "github"
    TWITTER = "twitter"
    RSS = "rss"
    HUGGINGFACE = "huggingface"
    PRODUCTHUNT = "producthunt"


class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


# ── Stage 1: Collector 输出 ──────────────────────────────────────────


class RawItem(BaseModel):
    """采集 Agent 输出的原始数据条目"""

    source_type: SourceType
    source_id: str = Field(description="数据源内唯一 ID，如 Reddit post id")
    title: str
    content: str = ""
    url: str = ""
    author: str = ""
    published_at: Optional[datetime] = None
    fetched_at: datetime = Field(default_factory=datetime.utcnow)
    score: int = Field(default=0, description="原始平台互动分数 (upvotes 等)")
    metadata: dict = Field(default_factory=dict, description="平台特有的额外字段")


# ── Stage 2: Cleaner 输出 ────────────────────────────────────────────


class CleanedItem(BaseModel):
    """清洗 Agent 输出的标准化数据"""

    id: str = Field(description="全局唯一 ID: {source_type}:{source_id}")
    source_type: SourceType
    title: str
    content: str
    url: str = ""
    author: str = ""
    published_at: Optional[datetime] = None
    language: str = "en"
    quality_score: float = Field(default=0.0, ge=0, le=1, description="质量评分 0-1")
    is_duplicate: bool = False
    duplicate_of: Optional[str] = None
    metadata: dict = Field(default_factory=dict, description="平台特有的额外字段（图片等）")


# ── Stage 3: Extractor 输出 ──────────────────────────────────────────


class ExtractedItem(BaseModel):
    """提取 Agent 输出的结构化数据"""

    id: str
    source_type: SourceType
    title: str
    content: str
    url: str = ""
    author: str = ""
    published_at: Optional[datetime] = None

    # 提取字段
    summary: str = Field(default="", description="2-3 句话的核心摘要")
    topics: list[str] = Field(default_factory=list, description="主题分类标签")
    entities: list[str] = Field(default_factory=list, description="关键实体: 公司、人物、模型名")
    sentiment: Sentiment = Sentiment.NEUTRAL
    importance_score: float = Field(default=5.0, ge=1, le=10, description="重要性评分 1-10")
    related_ids: list[str] = Field(default_factory=list, description="关联的历史新闻 ID")
    metadata: dict = Field(default_factory=dict, description="平台特有的额外字段（图片等）")


# ── Stage 4: Writer 输出 ─────────────────────────────────────────────


class ArticleSection(BaseModel):
    """文章的一个章节"""

    topic: str
    items: list[ExtractedItem]


class GeneratedArticle(BaseModel):
    """撰稿 Agent 生成的文章"""

    title: str
    date: str
    description: str = Field(default="", description="文章摘要，用于网站列表展示")
    sections: list[ArticleSection] = Field(default_factory=list)
    markdown_content: str = ""
    markdown_content_zh: str = ""
    item_count: int = 0
