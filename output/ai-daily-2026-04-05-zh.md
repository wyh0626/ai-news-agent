---
title: "AI 日报 — 2026-04-05"
description: "OpenAI推GPT-5.5Spud，Sora取消；Anthropic计费惹争议"
lang: "zh"
pairSlug: "ai-daily-2026-04-05"
---

# AI 日报 — 2026-04-05

> 涵盖 29 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 预训练 GPT-5.5「Spud」；Sora 项目被取消

OpenAI 已完成一款代号为 Spud（GPT-5.5）的新大型模型的预训练。公司声称，这一模型将在数周内展现出强大能力，有望加速整个经济进程，同时他们正在砍掉 Sora 项目，并放弃来自 Disney 的投资，将精力集中在 Spud 及其相关产品上。这一举措意味着要在全新的架构、数据和规模基础上重建模型体系，由 Greg Brockman 负责主导，而 Altman 将从安全监督中退居二线，转而专注于数据中心和供应链。 [来源-twitter](https://x.com/kimmonismus/status/2040754077781590060)

### 2. Anthropic 计费与 system prompt 绑定引发强烈反弹

一条爆火的帖子称，Anthropic 的计费会根据 system prompt 文本内容而变化，批评者认为这是一个「非常糟糕的信号」。帖子指出，Anthropic 正在阻止一方 harness 的使用，而第三方应用会被从额外用量中计费，而不是从套餐额度中扣减，本质上让价格随着用户的 prompt 文本而波动。 [来源-twitter](https://x.com/simonw/status/2040846932239851936)

### 3. Codex 应用服务器让构建智能体应用变得快捷

Codex 应用服务器允许用户在 Codex 之上构建自己的 agentic 应用，并在多设备间实现无缝会话同步，同时与 ChatGPT 账号集成。像 SIGKITTEN 的猫砂应用等演示表明，技能、智能体、会话、文件夹和提示词都可以通过应用服务器暴露出来，为移动端和桌面端提供统一的体验。 [来源-twitter](https://x.com/gdb/status/2040630239823339992)

## 📰 重点报道

### Open Source

- **Microsoft Agent Framework 支持多智能体 AI 工作流** — Microsoft 发布了 Agent Framework，这是一套支持跨语言的 AI 智能体构建、编排和部署平台，目前支持 Python 和 .NET。它可覆盖从简单对话型智能体到基于图的复杂多智能体工作流编排。仓库提供安装命令、文档（快速上手、教程、用户指南）以及从 Semantic Kernel 迁移的注意事项。 [来源-github](https://github.com/microsoft/agent-framework)
- **为 Claude Code 打造的开源 AI 求职工具开始走红** — 一个为 Claude Code 构建的开源 AI 求职系统 reportedly 发送了 700+ 份申请并成功拿到一份工作。它会自动爬取公司招聘页面、按岗位重写简历并自动填表，功能包括 14 种技能模式、Go 终端仪表盘、针对 ATS 优化的 PDF，以及预配置的 45+ 家公司。该项目由 GitHub 用户 santifer 维护。 [来源-twitter](https://x.com/garrytan/status/2040891664617848993)
- **Nanocode 让 Claude Code 以约 200 美元成本在 JAX TPU 上运行** — 一则 Hacker News 讨论聚焦于 Nanocode 声称可在 TPU 上以纯 JAX 方式运行 Claude Code，总成本约为 200 美元。讨论围绕 Salman Mohammadi 的开源方案展开，展示了通过在 TPU 上使用 JAX 以相对低成本获取 Claude Code 能力的路径。 [来源-hackernews](https://github.com/salmanmohammadi/nanocode/discussions/1)
- **Blaizzy 的 MLX-VLM 将 VLM 推理与微调带到 Mac 上** — MLX-VLM 是一个开源包，可在 macOS 上通过 MLX 实现视觉语言模型（VLM）以及 Omni 模型的推理和微调。该项目托管在 GitHub 的 Blaizzy/mlx-vlm 仓库中，提供命令行工具、聊天界面、多图对话功能，以及详尽的模型相关文档，方便用户进行部署和使用。 [来源-github](https://github.com/Blaizzy/mlx-vlm)
- **Travel Hacking Toolkit 实现 AI 驱动的积分旅行规划** — 一个在 Show HN 上发布的开源项目 Travel Hacking Toolkit，提供一套 AI 辅助工具，用于搜索里程票、比较现金票价，并在多个常旅客计划之间规划行程。该工具围绕 Claude Code 和 OpenCode 构建，内置 7 个技能和 6 个 MCP 服务器，可从 Seats.aero、Google Flights、AwardWallet、Trivago、Airbnb、Atlas Obscura 等数十个来源获取数据，同时结合 The Points Guy (TPG) 和 Upgra 的积分兑换比例与积分估值。项目目标是自动化处理「何时用积分、何时用现金」这类跨计划复杂计算。 [来源-hackernews](https://github.com/borski/travel-hacking-toolkit)

### AI Safety

- **Claude Code 揭示潜藏 23 年的 Linux 漏洞** — 据报道，一个名为 Claude Code 的 AI 驱动代码分析系统发现了一个在 Linux 内核中潜伏了 23 年的安全漏洞。该发现由 mtlynch.io 强调并在 Hacker News 上引发讨论，展示了 AI 辅助安全研究的潜力，以及其对开源软件安全性的重大影响。 [来源-hackernews](https://mtlynch.io/claude-code-found-linux-vulnerability/)

### LLM

- **Gemma 4（31B）以 0.20 美元/次成本称霸基准榜** — Gemma 4 是一款 310 亿参数模型，据报道在 FoodTruck Bench 排行榜中实现 100% 存活率和 +1,144% 的中位 ROI，每次运行成本仅为 0.20 美元。它在表现上击败了 GPT-5.2、Gemini 3 Pro、Sonnet 4.6 以及多款中国开源模型，唯一在价格上更具优势的是每次运行 36 美元的 Opus 4.6。结论是：Gemma 4 在性价比上极为突出，有望显著提升各类智能体工作流的效率。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sdcotc/gemma_4_just_casually_destroyed_every_model_on/)
- **Dante-2B：从零训练的 21 亿参数意大利语/英语双语 LLM** — Dante-2B 是一款 21 亿参数、仅解码架构的 LLM，从头训练以实现流利的意大利语和英语能力。它使用自定义的 64K BPE 分词器，采用 LLaMA 风格架构（28 层、d_model 2560），针对 2× H200 GPU 进行了优化。第一阶段训练已完成，模型在仅使用随机初始化、未对 Llama 或适配器进行微调的前提下，只用 16 天就达到了连贯的意大利语输出。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sdfwmu/dante2b_im_training_a_21b_bilingual_fully_open/)
- **中国多家实验室暂停开源最新模型，引发协同疑云** — 多家中国 AI 实验室（包括 Minimax-m2.7、GLM-5.1/5-turbo/5v-turbo、Qwen3.6 和 Mimo-v2-pro）都暂停开源其最新模型，并承诺在未来以改进版本发布。批评者指出，这一转变几乎是同步发生的，质疑这些举动是否意味着正向闭源模式进行某种协调转型，而非各家独立做出的自然选择。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sd22qy/anyone_else_find_it_weird_how_all_chinese_labs/)
- **基于 1900 年前文本训练的 LLM 挑战相对论与量子概念** — 一位研究者从零开始，用 1900 年前的文本训练 LLM，测试其是否能产出与量子力学和相对论相关的思想。该模型规模过小，难以形成有意义的推理，但在给定历史观测的情况下，仍展现出一些直观火花，例如关于能量量子以及重力与加速度局部等效的表述。数据集和模型已公开发布，同时提供演示网站、博客以及 GitHub 仓库。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sdampa/pre1900_llm_relativity_test/)

### AI Tools

- **Turboquant-gpu 实现任意 GPU 上 5 倍 KV cache 压缩** — Turboquant-gpu 提供一种 3-bit Lloyd-Max 融合 KV cache 压缩方案，用于 LLM 推理，并可通过简单的 compress+generate API 与 Hugging Face transformers 集成。据称在压缩效果上优于 MXFP4 和 NVFP4，并在 Mistral-7B 上实现了 5.02 倍 KV cache 减少（1,408 KB → 275 KB）。该项目基于 CUDA/cuTile，支持 CUDA 12/13，提供 PyTorch 回退机制，可运行在 RTX、H100、A100、B200 等常见 GPU 上。 [来源-twitter](https://x.com/anirudhbv_ce/status/2040874853881004163)

### Industry

- **「次级贷款式 AI 危机」正在到来** — 这篇文章认为，AI 行业正进入一个类似次级抵押贷款危机的高风险阶段，存在严重估值泡沫与脆弱的融资结构。作者呼吁在 AI 创业和部署中加强尽职调查，更注重可持续的商业模式与落地路径。 [来源-hackernews](https://www.wheresyoured.at/the-subprime-ai-crisis-is-here/)

## ⚡ 快讯速览

- **Grok Imagine 升级：可生成逼真电影级镜头** — Grok Imagine 进行了重大升级，现在可以生成更逼真的电影感镜头。帖子附带提示词模板和使用示例，帮助用户复现类似效果；更新通过设计师 doganuraldesign 在推文中分享。 [来源-twitter](https://x.com/doganuraldesign/status/2040808798030340596)
- **匿名化 ChatGPT 数据揭示健康咨询模式** — 一则引用美国匿名 ChatGPT 数据的帖子称，每周约有 200 万条与健康保险相关的信息，以及来自「医院荒漠」地区用户的 60 万条信息，其中 70% 发生在诊所工作时间之外。作者还分享自己在家庭健康事件中使用 ChatGPT（和 Claude）整理健康信息的经验，指出实时文档同步和数据摄取功能明显改善了决策过程。 [来源-twitter](https://x.com/CPMou2022/status/2040606209800290404)
- **Siri 通过 Telegram URL 连接 Hermes 智能体** — 使用 Siri 与 Hermes 智能体交互的方法是：创建一个新联系人，在其中添加 URL 字段并填入机器人链接，然后将 URL 类型设为 Telegram。只要有一个开启的对话，这就能让所有 Apple 设备通过 Siri 向 Hermes 智能体发送消息。 [来源-twitter](https://x.com/Teknium/status/2040616502643323205)
- **通过 Hermes 使用 Claude，只需一个 /claude-code 命令** — 在 Hermes Agent 中，只要输入 /claude-code，就能在一个新的 Hermes 会话中启动 Claude code 会话，从而无需任何「小技巧」即可访问 Anthropic 的 Claude。帖子称，这种方法保留了 Hermes 的自我改进循环和功能特性，相比之下 OpenClaw 的方法则做不到。相关信息来自 Teknium 在 X（Twitter）上的发帖。 [来源-twitter](https://x.com/Teknium/status/2040603975343542503)
- **重度用户正在侵蚀 AI 订阅制的利润空间** — 对 AI 订阅服务来说，盈利看起来似乎很容易，直到出现一个资源消耗极大的「重度用户」，迅速吞噬掉利润空间。结论是，在设计 AI SaaS 的价格和套餐结构时，必须充分考虑用户行为和用量分布带来的风险，尤其是高频用户对成本的冲击。 [来源-twitter](https://x.com/Yuchenj_UW/status/2040837406207959473)
- **音乐人指控 AI 公司克隆其音乐并提起诉讼** — 一位音乐人声称某家 AI 公司在克隆她的音乐，并已对该公司提起相关权利主张。该纠纷凸显了 AI 生成音乐领域的版权担忧。报道引用了 Hacker News 讨论中链接的一条 Twitter 帖子。 [来源-hackernews](https://twitter.com/unlimited_ls/status/2040577536136974444)
- **Block/goose：开源 AI 智能体自动化工程任务** — Block/goose 是一款本地、可扩展的 AI 智能体，可从头到尾自动化完成工程任务。它能从零构建项目、编写并执行代码、调试错误、编排工作流，并通过任意 LLM 调用外部 API；同时支持多模型配置、MCP 服务器集成，并提供桌面应用与命令行两种使用方式。 [来源-github](https://github.com/block/goose)
- **八年构思、三月落地：Syntaqlite AI 的构建历程** — 一篇文章记录了 Syntaqlite AI 的诞生：作者构思该项目长达八年，却在 AI 工具的帮助下用三个月完成。文中讨论了从想法到实现的过程、AI 在加速开发中的关键作用，以及在这一过程中的经验教训。 [来源-hackernews](https://lalitm.com/post/building-syntaqlite-ai/)
- **AI 复制音乐人文件，反而触发对艺术家的版权投诉** — 一起事件中，AI 复制了一位音乐人的文件，结果平台对这位艺术家发起了版权投诉。该故事在 Hacker News 上持续更新和讨论，引用了 XCancel 上 VladTheInflator 的帖子及一条相关推文。 [来源-hackernews](https://twitter.com/VladTheInflator/status/2039577001531768906)
- **一次提交加入 1.2 万篇 AI 生成博客文章** — 据报道，OneUptime/blog 仓库的一次 GitHub 提交中，约有 12,000 篇 AI 生成的博客文章被一次性推送进库。这一举动在 Hacker News 上引发了关于内容质量、许可风险、垃圾内容以及开源项目在批量自动化内容时代的维护问题等方面的讨论。 [来源-hackernews](https://github.com/OneUptime/blog/commit/30cd2384794c897d95aca77d173db44af51ca849)
- **《I Used AI. It Worked. I Hated It.》** — 一篇在 Hacker News 上流传的个人文章讲述了作者使用 AI 完成某项任务的经历：工具在结果上是成功的，但整体体验却让人十分沮丧。文章凸显了 AI 宣传的光鲜前景与现实使用体验之间的落差，包括效率、控制感以及满意度等方面的权衡。 [来源-hackernews](https://taggart-tech.com/reckoning/)
- **LLM Wiki 展示 Karpathy 的「想法文件」理念** — Karpathy 在一篇 LLM Wiki 中强调了「idea file（想法文件）」的做法，用以展示如何系统地整理和分享有关语言模型的构思。该帖子在 X 和 Hacker News 上广泛传播，并附有一个 GitHub Gist 以供进一步阅读。 [来源-hackernews](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- **取消 Claude Code 订阅，将四月环境迁移到本地 Gemma 4** — 有用户表示自己取消了四月份的 Claude Code 订阅，并将开发环境迁移到搭载 Gemma 4 的 MacBook Pro 上。TA 强调，这样的配置无需联网、没有 API 成本，也不存在调用限制，整体更加简化且偏向离线。 [来源-twitter](https://x.com/pcshipp/status/2040815682494042485)
- **Anthropic Claude 文档更新被称「离谱」** — 一条推文提到 Claude 文档最近一次更新，称这次更新「很猛」，但并未给出具体细节。它反映出 Anthropic 不断在面向开发者的文档和工具上推进改进。 [来源-twitter](https://x.com/theo/status/2040895674288570499)

---

*由 AI News Agent 生成 | 2026-04-05*