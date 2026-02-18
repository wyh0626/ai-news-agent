"""全局配置 - 基于 pydantic-settings，从环境变量 / .env 文件加载"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # LLM
    openai_api_key: str = ""
    openai_base_url: str = ""
    openai_model: str = "gpt-4o-mini"

    # Embedding（默认复用 LLM 的 API Key，也可单独配置）
    embedding_api_key: str = ""
    embedding_base_url: str = ""
    embedding_model: str = "text-embedding-3-small"

    # 数据源
    reddit_subreddits: str = "LocalLLaMA,MachineLearning,artificial"
    hn_min_score: int = 50
    twitter_api_key: str = ""
    twitter_kol_list: str = ""
    firecrawl_api_key: str = ""
    twitter_list_url: str = "https://x.com/i/lists/1585430245762441216"
    nitter_mirror_url: str = "https://nitter.net"

    # GitHub 趋势去重缓存天数
    github_trending_dedup_days: int = 3

    # 数据库
    postgres_url: str = "postgresql://postgres:postgres@localhost:5432/ainews"

    # 输出
    output_dir: str = "./output"
    output_format: str = "markdown"

    # Webhook 推送 (v0.5)
    slack_webhook_url: str = ""
    discord_webhook_url: str = ""
    feishu_webhook_url: str = ""

    # 邮件推送 (v0.5)
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    smtp_from: str = ""
    newsletter_recipients: str = ""

    # 审核模式 (v0.5): "auto" 或 "human"
    review_mode: str = "auto"

    # 监控 (v1.0)
    langsmith_api_key: str = ""
    langsmith_project: str = "ai-news-agent"

    # Pipeline
    report_mode: str = "daily"  # daily / weekly
    max_items_per_run: int = 50
    max_items_per_source: int = 15
    min_items_per_source: int = 3
    top_k_featured: int = 10
    min_items_to_write: int = 5
    log_level: str = "INFO"

    @property
    def output_path(self) -> Path:
        p = Path(self.output_dir)
        p.mkdir(parents=True, exist_ok=True)
        return p

    @property
    def subreddit_list(self) -> list[str]:
        return [s.strip() for s in self.reddit_subreddits.split(",") if s.strip()]



settings = Settings()
