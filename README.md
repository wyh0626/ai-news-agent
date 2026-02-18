# 🤖 AI News Agent

[中文文档](./README.zh-CN.md)

A multi-agent AI news aggregation system built on LangGraph. Automatically collects, cleans, deduplicates, extracts structured information via LLM, and generates bilingual (Chinese & English) AI news briefings (daily / weekly) with multi-channel publishing.

**Features:**
- **5 data sources**: Reddit, Hacker News, ArXiv, GitHub Trending, Twitter/X
- **LLM-powered**: AI relevance filtering, structured extraction, Chinese title generation, English translation
- **Smart dedup**: Title matching + pgvector semantic dedup + event-level merging
- **Zero-cost deploy**: GitHub Actions cron + Neon free PostgreSQL + GitHub Pages
- **Multi-model**: OpenAI / Kimi (Moonshot) / DeepSeek / any OpenAI-compatible API

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/wyh0626/ai-news-agent.git
cd ai-news-agent

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[prod]"
```

### 2. Configure

```bash
cp .env.example .env
```

**Minimal config** (only need one LLM API Key):

```bash
OPENAI_API_KEY=sk-your-api-key
OPENAI_MODEL=gpt-4o-mini
```

**Using Kimi (Moonshot)**:

```bash
OPENAI_API_KEY=sk-your-moonshot-key
OPENAI_BASE_URL=https://api.moonshot.cn/v1
OPENAI_MODEL=moonshot-v1-auto
# Kimi doesn't provide Embedding API, configure separately for semantic dedup
EMBEDDING_API_KEY=sk-your-openai-key
EMBEDDING_BASE_URL=https://api.openai.com/v1
```

**Enable semantic dedup** (recommended):

```bash
# Option 1: Local Docker
docker compose up -d postgres

# Option 2: Neon free cloud database (recommended, pgvector built-in)
POSTGRES_URL=postgresql://user:pass@xxx.neon.tech/neondb?sslmode=require
```

### 3. Run

```bash
# Collect from all sources, generate daily report
python scripts/run_pipeline.py

# Specify sources
python scripts/run_pipeline.py reddit hackernews

# Twitter only
python scripts/run_pipeline.py twitter
```

### 4. Output

```
output/
├── ai-daily-2026-02-18.md       # Chinese report
├── ai-daily-2026-02-18-en.md    # English report
```

## Architecture

```
Collector → Cleaner → Dedup → Extractor → Reviewer → Writer → Translator → Publisher → Memory
  Fetch      Clean   Rule+Semantic  LLM      Event     LLM      ZH→EN      Multi-ch   Long-term
                                   Extract   Merge    Compose   Translate   Publish    Memory
```

| Agent | Role | Implementation |
|-------|------|----------------|
| **Collector** | Parallel multi-source fetching | feedparser + httpx + Firecrawl |
| **Cleaner** | Normalize format, remove noise | Rule engine |
| **Dedup** | Title dedup + semantic dedup | Title matching + pgvector |
| **Extractor** | Topic classification, summary, Chinese titles | LLM concurrent batch |
| **Reviewer** | Event-level dedup & merge | LLM identifies same events |
| **Writer** | Compose briefing (Top Stories + Featured + Quick Bites) | LLM + template fallback |
| **Translator** | Chinese report → English version | LLM translation |
| **Publisher** | Save Markdown + Email + Webhook | Multi-channel |

## Deployment

### Option 1: GitHub Actions (Recommended, zero server cost)

Pre-configured in `.github/workflows/daily-pipeline.yml`:

1. Fork this repo
2. Go to **Settings → Secrets → Actions**, add:

| Secret | Required | Description |
|--------|----------|-------------|
| `OPENAI_API_KEY` | ✅ | LLM API Key |
| `OPENAI_BASE_URL` | | API endpoint (default: OpenAI) |
| `OPENAI_MODEL` | | Model name (default: gpt-4o-mini) |
| `POSTGRES_URL` | | Neon database URL (enables semantic dedup) |
| `FIRECRAWL_API_KEY` | | Firecrawl Key (enables Twitter) |
| `TWITTER_LIST_URL` | | Twitter List URL |
| `NITTER_MIRROR_URL` | | Nitter mirror URL |

3. Go to **Settings → Pages**, set Source to **GitHub Actions**
4. Pipeline runs daily at UTC 00:00. Manual trigger also supported (daily/weekly mode).

### Option 2: Docker (Local / VPS)

```bash
docker compose up -d    # Start PostgreSQL + run pipeline
```

## Multi-channel Publishing

Configure in `.env` to auto-enable:

```bash
# Slack / Discord / Feishu (Lark)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...

# Email newsletter
SMTP_HOST=smtp.gmail.com
SMTP_USER=your@email.com
NEWSLETTER_RECIPIENTS=reader1@email.com,reader2@email.com
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent Framework | LangGraph (StateGraph) |
| LLM | OpenAI / Kimi / DeepSeek (compatible API) |
| Embedding | text-embedding-3-small + pgvector |
| Database | PostgreSQL + pgvector (Neon free tier) |
| Static Site | Astro + TailwindCSS |
| CI/CD | GitHub Actions + GitHub Pages |

## License

MIT
