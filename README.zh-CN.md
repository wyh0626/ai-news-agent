# 🤖 AI News Agent

[English](./README.md)

基于 LangGraph 的多 Agent AI 新闻聚合系统。自动从多个数据源采集、清洗、语义去重、LLM 提取结构化信息，生成中英文双语 AI 新闻简报（日报 / 周报），支持多渠道发布。

**特点：**
- **8 大数据源**：Reddit、Hacker News、ArXiv、GitHub Trending、RSS、Twitter/X、HuggingFace Papers、Product Hunt
- **LLM 驱动**：AI 相关性过滤、结构化提取、中文标题生成、英文翻译
- **智能去重**：标题去重 + pgvector 语义去重 + 事件级合并
- **零成本部署**：GitHub Actions 定时运行 + Neon 免费 PostgreSQL + GitHub Pages
- **多模型支持**：OpenAI / Kimi (Moonshot) / DeepSeek / 任何 OpenAI 兼容 API

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
# 编辑 .env，填入你的 API Key
```

**最小配置**（只需一个 LLM API Key，即可运行 Reddit / HN / ArXiv / GitHub / RSS / HuggingFace 六个免费源）：

```bash
OPENAI_API_KEY=sk-your-api-key
OPENAI_MODEL=gpt-4o-mini
```

> 💡 **无需任何第三方 Key**：上述 6 个数据源全部通过公开 RSS / API 采集，零额外成本。

**使用 Kimi (Moonshot) / DeepSeek**：

```bash
# Kimi
OPENAI_API_KEY=sk-your-moonshot-key
OPENAI_BASE_URL=https://api.moonshot.cn/v1
OPENAI_MODEL=moonshot-v1-auto
# Kimi 不提供 Embedding API，需要单独配置（用于语义去重）
EMBEDDING_API_KEY=sk-your-openai-key
EMBEDDING_BASE_URL=https://api.openai.com/v1

# DeepSeek
OPENAI_API_KEY=sk-your-deepseek-key
OPENAI_BASE_URL=https://api.deepseek.com/v1
OPENAI_MODEL=deepseek-chat
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
# 采集全部默认数据源，生成日报
python scripts/run_pipeline.py

# 指定数据源
python scripts/run_pipeline.py reddit hackernews arxiv

# 只采集 Twitter
python scripts/run_pipeline.py twitter
```

可用数据源标识：`reddit` `hackernews` `arxiv` `github` `rss` `huggingface` `producthunt` `twitter`

### 4. 查看输出

```
output/
├── ai-daily-2026-02-18.md       # 中文日报
├── ai-daily-2026-02-18-en.md    # 英文日报
```

---

## 数据源详解

每个数据源都有独立的采集策略、过滤机制和配置项。下表总览：

| 数据源 | 采集方式 | 需要 API Key | 默认开启 |
|--------|----------|:------------:|:--------:|
| Reddit | RSS | ❌ | ✅ |
| Hacker News | RSS (hnrss) | ❌ | ✅ |
| ArXiv | RSS | ❌ | ✅ |
| GitHub Trending | RSS (社区维护) | ❌ | ✅ |
| RSS (AI 博客) | RSS / Atom | ❌ | ✅ |
| HuggingFace Papers | HTTP API | ❌ | ✅ |
| Product Hunt | GraphQL API | ⚠️ 推荐 | ❌ |
| Twitter/X | Firecrawl + Nitter | ✅ | ❌ |

---

### 🟢 Reddit

**采集思路**：通过 Reddit 官方 RSS feed 获取指定子版块的热门帖子（`/r/{subreddit}/hot.rss`），无需任何 API Key。

**过滤机制（两级）**：
1. **时间过滤**：只保留 24h 内的帖子
2. **LLM AI 过滤**：将所有帖子标题+摘要送入 LLM 批量分类，精准筛选 AI 相关内容

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `REDDIT_SUBREDDITS` | `LocalLLaMA,MachineLearning,artificial,OpenAI,ClaudeAI,singularity,...` | 逗号分隔的子版块列表 |

```bash
# 示例：自定义要监控的子版块
REDDIT_SUBREDDITS=LocalLLaMA,MachineLearning,artificial,OpenAI,DeepSeek
```

> 💡 **开箱即用**：无需配置，默认监控 13 个 AI 相关子版块。

---

### 🟢 Hacker News

**采集思路**：通过 [hnrss.org](https://hnrss.org) 服务获取 HN 内容。请求时附带 AI 关键词（`AI OR LLM OR GPT OR machine learning ...`）进行 API 侧粗筛，同时设置最低分数门槛。

**过滤机制（两级）**：
1. **hnrss `q=` 参数**：API 侧关键词粗筛 + 分数门槛
2. **LLM AI 过滤**：批量标题分类，自动适应新术语

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `HN_MIN_SCORE` | `50` | 最低分数门槛（upvotes） |

```bash
# 降低门槛以获取更多内容
HN_MIN_SCORE=30
```

> 💡 **开箱即用**：无需配置，默认采集 50 分以上的 AI 相关帖子。

---

### 🟢 ArXiv

**采集思路**：通过 ArXiv 官方 RSS feed 采集 `cs.AI`（人工智能）、`cs.LG`（机器学习）、`cs.CL`（计算语言学）三个分类的最新论文。

**过滤机制（两级）**：
1. **分类限定**：只拉取 AI 相关分类
2. **LLM AI 过滤**：过滤纯理论/纯数学论文，保留实用 AI 论文

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `ARXIV_MAX_ITEMS` | `5` | 最终入选日报的论文上限（避免论文占比过高） |

> 💡 **开箱即用**：无需配置。分类固定为 cs.AI/cs.LG/cs.CL，最终精选 5 篇入选日报。

---

### 🟢 GitHub Trending

**采集思路**：通过社区维护的 [GitHub Trending RSS](https://github.com/mshibanami/GitHubTrendingRSS) 源获取每日热门仓库，再通过 LLM 判断是否 AI 相关。

**特色功能**：
- **跨天去重**：本地 JSON 缓存近 N 天已上榜项目，避免同一项目连续多天重复推送

**过滤机制（两级）**：
1. **LLM AI 过滤**：根据仓库名+描述判断是否 AI 相关
2. **跨天去重**：已在近几天上榜的项目自动跳过

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `GITHUB_TRENDING_DEDUP_DAYS` | `3` | 跨天去重缓存天数 |

> 💡 **开箱即用**：无需配置，默认采集全语言每日 Trending。

---

### 🟢 RSS (AI 博客)

**采集思路**：通过标准 RSS/Atom feed 直接订阅各大 AI 公司/项目的官方博客。内容天然为 AI 相关，无需 LLM 过滤。

**内置 5 个源**：
- OpenAI Blog
- DeepMind Blog
- HuggingFace Blog
- PyTorch Blog
- Ollama Blog

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `RSS_FEEDS` | 空（使用内置源） | 自定义 RSS 源，格式 `name1=url1,name2=url2` |

```bash
# 添加自定义 RSS 源（会叠加在内置源之上）
RSS_FEEDS=anthropic=https://www.anthropic.com/rss.xml,mistral=https://mistral.ai/feed
```

> 💡 **开箱即用**：无需配置，默认订阅 5 个 AI 官方博客。可通过 `RSS_FEEDS` 追加任意 RSS/Atom 源。

---

### 🟢 HuggingFace Papers

**采集思路**：通过 HuggingFace 公开 API（`/api/daily_papers`）获取每日社区精选论文。这些论文由社区投票筛选，upvotes 代表真实热度，**全部为 AI 相关，无需 LLM 过滤**。

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `HF_PAPERS_MIN_UPVOTES` | `5` | 最低投票数门槛 |

> 💡 **开箱即用**：无需配置，无需 Token。默认采集 5 票以上的热门论文。

---

### 🟡 Product Hunt

**采集思路**：通过 Product Hunt GraphQL API 查询当日发布的热门产品，按投票数排序。

**过滤机制（两级）**：
1. **投票门槛**：只保留 votes ≥ 阈值的产品
2. **LLM AI 过滤**：根据产品名+tagline 判断是否 AI 相关

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `PRODUCTHUNT_API_TOKEN` | 空 | Product Hunt API Token（[申请地址](https://www.producthunt.com/v2/oauth/applications)） |
| `PRODUCTHUNT_MIN_VOTES` | `50` | 最低投票数门槛 |

```bash
PRODUCTHUNT_API_TOKEN=your-token-here
PRODUCTHUNT_MIN_VOTES=50
```

> ⚠️ **需要 API Token**：前往 [Product Hunt Developer](https://www.producthunt.com/v2/oauth/applications) 免费申请。不配置 Token 时可能无法获取数据。

---

### 🟡 Twitter/X

**采集思路**：由于 Twitter API 价格昂贵，本项目采用 **Firecrawl + Nitter 镜像**的方案。流程如下：

1. 创建一个 [Twitter List](https://help.x.com/en/using-x/x-lists)，将你关注的 AI KOL 添加进去
2. 配置 Nitter 镜像地址，系统将 Twitter List URL 转换为 Nitter 镜像 URL
3. 通过 [Firecrawl](https://www.firecrawl.dev/) 爬取 Nitter 页面的 Markdown 内容
4. 正则解析推文（作者、正文、时间、互动数据）
5. 自动翻页采集 24h 内推文，跨页去重
6. LLM 批量过滤 AI 相关推文，按互动分数排序取 Top 20

**配置项**：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `FIRECRAWL_API_KEY` | 空 | Firecrawl API Key（[申请地址](https://www.firecrawl.dev/)，有免费额度） |
| `TWITTER_LIST_URL` | 预设 AI KOL 列表 | 你的 Twitter List 地址（如 `https://x.com/i/lists/xxx`） |
| `NITTER_MIRROR_URL` | `https://nitter.net` | Nitter 镜像地址 |

```bash
FIRECRAWL_API_KEY=fc-your-api-key
TWITTER_LIST_URL=https://x.com/i/lists/1585430245762441216
NITTER_MIRROR_URL=https://nitter.net
```

**如何创建 Twitter List**：
1. 打开 [x.com](https://x.com) → 右侧菜单 → Lists → Create a new List
2. 添加你关注的 AI KOL（如 @kaboroevoda, @AndrewYNg, @ylecun 等）
3. 复制 List URL 填入 `TWITTER_LIST_URL`

> ⚠️ **需要 Firecrawl API Key**：前往 [firecrawl.dev](https://www.firecrawl.dev/) 注册，免费额度即可使用。Nitter 镜像可能不稳定，如遇问题可更换镜像地址。

---

## 架构

```
Collector → Cleaner → Dedup → Extractor → Reviewer → Writer → Translator → Publisher → Memory
   采集       清洗    规则+语义   LLM提取   事件合并    LLM撰稿   中→英翻译    多渠道      长期记忆
```

| Agent | 职责 | 实现 |
|-------|------|------|
| **Collector** | 并行采集 8 大数据源 | feedparser + httpx + Firecrawl |
| **Cleaner** | 格式标准化、去噪 | 规则引擎 |
| **Dedup** | 标题去重 + 语义去重 | 标题匹配 + pgvector |
| **Extractor** | 主题分类、摘要、中文标题 | LLM 并发批处理 |
| **Reviewer** | 事件级去重合并 | LLM 识别同一事件 |
| **Writer** | 编排简报（今日焦点 + 重点 + 快讯） | LLM + 模板降级 |
| **Translator** | 中文日报 → 英文版 | LLM 翻译 |
| **Publisher** | 保存 Markdown + 邮件 + Webhook | 多渠道 |

## 部署

> ⚠️ 由于 Reddit RSS 屏蔽了 GitHub Actions 的 IP 段，Pipeline 无法在 GitHub Actions 中运行。推荐在本地或 VPS 上部署。

### 方案一：本地 / VPS 直接运行（推荐）

最简单的方式，直接用 cron 定时运行：

```bash
# 1. 克隆 & 安装（见「快速开始」）

# 2. 手动运行一次，确认正常
python scripts/run_pipeline.py

# 3. 设置 cron 定时任务（每天 UTC 00:00 = 北京时间 08:00）
crontab -e
# 添加以下行（根据实际路径修改）：
0 0 * * * cd /path/to/ai-news-agent && bash scripts/run_and_push.sh >> output/pipeline.log 2>&1
```

`run_and_push.sh` 会自动完成：运行 Pipeline → 同步内容到 site → git push → 触发 GitHub Pages 部署。

**自动 git push 配置**（二选一）：

```bash
# 方式一：GitHub Token（HTTPS，推荐）
GIT_TOKEN=ghp_your-github-token
GIT_REPO=your-username/ai-news-agent

# 方式二：SSH Key
# 确保 ~/.ssh/id_ed25519 已配置好 GitHub 访问权限
```

### 方案二：Docker（需自行构建镜像）

项目提供了 Dockerfile，但尚未发布预构建镜像，需要自行构建：

```bash
# 1. 构建镜像
docker build -t ai-news-agent .

# 2. 单次运行
docker run --rm --env-file .env -v ./output:/app/output ai-news-agent

# 3. 定时运行（通过 docker-compose）
# 编辑 docker-compose.yml 中的 image 为你构建的镜像名
docker compose up -d
```

### GitHub Pages 静态站部署

项目内置了 Astro 静态站（`site/` 目录），Pipeline 运行后自动 push 内容，GitHub Actions 会自动部署：

1. Fork 本仓库
2. 在 **Settings → Pages** 中启用 GitHub Pages（Source: **GitHub Actions**）
3. Pipeline push 新内容后，`.github/workflows/deploy-site.yml` 会自动构建并部署站点

## 多渠道发布

在 `.env` 中配置即自动启用：

```bash
# Slack / Discord / 飞书
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
DISCORD_WEBHOOK_URL=https://hooks.discord.com/api/webhooks/...
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...

# 邮件
SMTP_HOST=smtp.gmail.com
SMTP_USER=your@email.com
SMTP_PASSWORD=your-app-password
NEWSLETTER_RECIPIENTS=reader1@email.com,reader2@email.com
```

## Pipeline 调参

在 `.env` 中可微调 Pipeline 行为：

```bash
MAX_ITEMS_PER_RUN=50       # 每次运行最多处理条数
MAX_ITEMS_PER_SOURCE=15    # 每个数据源最多入选条数
ARXIV_MAX_ITEMS=5          # ArXiv 单独上限（避免论文占比过高）
TOP_K_FEATURED=10          # 精选条目数量
REPORT_MODE=daily          # daily / weekly
LOG_LEVEL=INFO             # DEBUG 可看到详细采集日志
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
