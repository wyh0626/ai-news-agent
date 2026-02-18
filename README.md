# 🤖 AI News Agent

基于 LangGraph 的多 Agent AI 新闻聚合系统。自动从多个数据源采集、清洗、语义去重、LLM 提取结构化信息，生成中英文双语 AI 新闻简报（日报 / 周报），支持多渠道发布。

**特点：**
- 5 大数据源：Reddit、Hacker News、ArXiv、GitHub Trending、Twitter/X
- LLM 驱动：AI 相关性过滤、结构化提取、中文标题生成、英文翻译
- 智能去重：标题去重 + pgvector 语义去重 + 事件级合并
- 零成本部署：GitHub Actions 定时运行 + Neon 免费 PostgreSQL + GitHub Pages
- 多模型支持：OpenAI / Kimi (Moonshot) / DeepSeek / 任何 OpenAI 兼容 API

## 快速开始

### 1. 克隆 & 安装

```bash
git clone https://github.com/wyh0626/ai-news-agent.git
cd ai-news-agent

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[prod]"
```

### 2. 配置

```bash
cp .env.example .env
```

**最小配置**（只需一个 LLM API Key 即可运行）：

```bash
OPENAI_API_KEY=sk-your-api-key
OPENAI_MODEL=gpt-4o-mini
```

**使用 Kimi (Moonshot)**：

```bash
OPENAI_API_KEY=sk-your-moonshot-key
OPENAI_BASE_URL=https://api.moonshot.cn/v1
OPENAI_MODEL=moonshot-v1-auto
# Kimi 不提供 Embedding，需要单独配置（用于语义去重）
EMBEDDING_API_KEY=sk-your-openai-key
EMBEDDING_BASE_URL=https://api.openai.com/v1
```

**启用语义去重**（推荐，避免重复报道）：

```bash
# 方式一：本地 Docker
docker compose up -d postgres

# 方式二：Neon 免费云数据库（推荐，自带 pgvector）
POSTGRES_URL=postgresql://user:pass@xxx.neon.tech/neondb?sslmode=require
```

### 3. 运行

```bash
# 采集全部数据源，生成日报
python scripts/run_pipeline.py

# 指定数据源
python scripts/run_pipeline.py reddit hackernews

# 只采集 Twitter
python scripts/run_pipeline.py twitter
```

### 4. 查看输出

```
output/
├── ai-daily-2026-02-18.md       # 中文日报
├── ai-daily-2026-02-18-en.md    # 英文日报
```

## 架构

```
Collector → Cleaner → Dedup → Extractor → Reviewer → Writer → Translator → Publisher → Memory
   采集       清洗    规则+语义   LLM提取   事件合并    LLM撰稿   中→英翻译    多渠道      长期记忆
```

| Agent | 职责 | 实现 |
|-------|------|------|
| **Collector** | 并行采集 5 大数据源 | feedparser + httpx + Firecrawl |
| **Cleaner** | 格式标准化、去噪 | 规则引擎 |
| **Dedup** | 标题去重 + 语义去重 | 标题匹配 + pgvector |
| **Extractor** | 主题分类、摘要、中文标题 | LLM 并发批处理 |
| **Reviewer** | 事件级去重合并 | LLM 识别同一事件 |
| **Writer** | 编排简报（今日焦点 + 重点 + 快讯） | LLM + 模板降级 |
| **Translator** | 中文日报 → 英文版 | LLM 翻译 |
| **Publisher** | 保存 Markdown + 邮件 + Webhook | 多渠道 |

## 部署

### 方案一：GitHub Actions（推荐，零服务器成本）

项目已配置好 `.github/workflows/daily-pipeline.yml`：

1. Fork 本仓库
2. 在 **Settings → Secrets → Actions** 中添加：

| Secret | 必填 | 说明 |
|--------|------|------|
| `OPENAI_API_KEY` | ✅ | LLM API Key |
| `OPENAI_BASE_URL` | | API 地址（默认 OpenAI） |
| `OPENAI_MODEL` | | 模型名（默认 gpt-4o-mini） |
| `POSTGRES_URL` | | Neon 数据库 URL（启用语义去重） |
| `FIRECRAWL_API_KEY` | | Firecrawl Key（启用 Twitter） |
| `TWITTER_LIST_URL` | | Twitter List URL |
| `NITTER_MIRROR_URL` | | Nitter 镜像地址 |

3. 在 **Settings → Pages** 中启用 GitHub Pages（Source: GitHub Actions）
4. Pipeline 每天 UTC 00:00 自动运行，也可手动触发（支持选择日报/周报模式）

### 方案二：Docker 本地/VPS

```bash
docker compose up -d    # 启动 PostgreSQL + 运行 Pipeline
```

## 多渠道发布

在 `.env` 中配置即自动启用：

```bash
# Slack / Discord / 飞书
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...

# 邮件
SMTP_HOST=smtp.gmail.com
SMTP_USER=your@email.com
NEWSLETTER_RECIPIENTS=reader1@email.com,reader2@email.com
```

## 技术栈

| 层次 | 技术 |
|------|------|
| Agent 框架 | LangGraph (StateGraph) |
| LLM | OpenAI / Kimi / DeepSeek（兼容 API） |
| Embedding | text-embedding-3-small + pgvector |
| 数据库 | PostgreSQL + pgvector（Neon 免费层） |
| 静态站 | Astro + TailwindCSS |
| CI/CD | GitHub Actions + GitHub Pages |

## License

MIT
