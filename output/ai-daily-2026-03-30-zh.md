---
title: "AI 日报 — 2026-03-30"
description: "Qwen3.5-Omni本地原生全模态AGI问世，ARC-AGI-3近零泛化。"
lang: "zh"
pairSlug: "ai-daily-2026-03-30"
---

# AI 日报 — 2026-03-30

> 共收录 39 条 AI 新闻

## 🔥 今日焦点

### 1. Qwen3.5-Omni 发布原生 Omni-Modal AGI

阿里巴巴的 Qwen3.5-Omni 推出了一款原生 omni-modal（全模态）AI，能够进行文本、图像、音频和视频理解，并支持实时交互。其引入 Audio-Visual Vibe Coding，可从视觉信息生成网站或游戏，自称在音频-视觉性能上达到 SOTA，并支持长时媒体、多语种以及细粒度语音控制。这标志着向完全集成的多模态技术栈转型，可能改变企业级 AI 采纳的竞争格局。 [来源-x](https://x.com/Alibaba_Qwen/status/2038636335272194241)

### 2. ARC-AGI-3 基准：AI 在全新环境中得分接近零

François Chollet 的 ARC-AGI-3 引入了 135 个全新的游戏环境，没有任何说明或任务目标，需要实时探索与适应。未经训练的人类可以解出所有环境，而顶尖 AI 模型得分不到 1%，凸显出严重的泛化能力差距，以及在稳健的、无指令通用智能方面的持续挑战。回到 ARC-AGI-3 这一版本强调了当前系统距离灵活的真实世界适应性还有多遥远。 [来源-x](https://x.com/Kasparov63/status/2038624223158030799)

### 3. 在 MacBook 上跑 397B Qwen3.5：无云端，纯 C/Metal

一位 AI 工程师展示了在一台配备 48GB 内存的 MacBook Pro 上运行 3970 亿参数模型（Qwen3.5-397B），使用纯 C/Metal 推理引擎（flash-moe），完全不依赖云端、GPU 或 Python。系统从 SSD 流式读取 209GB 的模型，每个 token 只加载 512 个专家中的 4 个，活动内存使用约 5.5GB，在支持完整工具调用的同时实现 4.4 token/秒的速度。这一成果突显了消费级硬件在本地部署 AI 负载方面惊人的潜力。 [来源-x](https://x.com/heynavtoor/status/2038614549973401699)

## 📰 重点报道

### Open Source & Embeddings
- **Microsoft Harrier OSS 多语言 Embedding 模型（27B/0.6B/270M）** — Harrier OSS v1 提供多语言 decoder-only 文本嵌入模型，使用最后一个 token 池化和 L2 归一化，可用于检索、聚类、语义相似度、分类等任务；发布时号称在 Multilingual MTEB v2 上达到 SOTA 水平。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7qh70/microsoftharrieross_27b06b270m/)

- **基于 Claude 蒸馏微调的 Qwen3.5-27B，本地推理可用** — 基于 Claude-4.6-Opus 蒸馏数据微调的 Qwen3.5-27B 提升了推理能力；在 16GB（4-bit）或 32GB（8-bit）硬件上可本地运行，并已在 HuggingFace 发布。 [来源-x](https://x.com/UnslothAI/status/2038625148354679270)

### Tools & Interfaces
- **Claude Code 新增计算机使用能力以实现 UI 自动化** — Claude Code 现在支持“使用电脑”能力，可以打开应用、点击操作 UI，并从命令行测试构建；目前在 Pro 和 Max 方案中以研究预览形式开放。 [来源-x](https://x.com/claudeai/status/2038663014098899416)

- **通过新插件在 Claude Code 中使用 Codex** — Anthropic 的 Claude Code 通过插件市场新条目（openai/codex-plugin-cc）接入 OpenAI Codex，支持 /codex:review、/codex:adversarial-review 等命令。 [来源-x](https://x.com/reach_vb/status/2038671858862583967)

### AI Safety & Research
- **斯坦福与哈佛发布令人不安的 AI 论文** — 一条 Reddit 帖子关注了斯坦福与哈佛在 arXiv 上的预印本（2602.20021），被描述为“今年最令人不安的 AI 论文”，并讨论了其更广泛的影响。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7w9mq/stanford_and_harvard_just_dropped_the_most/)

### Benchmarks & Frontier Models
- **Opus 在 Cursor 基准中比 Claude Code 高 20%** — 在一项前沿模型基准中，Cursor 的表现优于 Claude Code 和其他工具；Opus 从 77% 提升到 93%，GPT-5.4 从 82% 提升到 88%，Gemini 从 52% 提升到 57%，评测维度是 100 个功能点的 PRD 指标。 [来源-x](https://x.com/theo/status/2038690786821505378)

### Multimodal & Vision
- **Hybrid Memory 让视频世界模型能在遮挡下追踪目标** — 提出 Hybrid Memory，一种用于视频世界模型的记忆架构，在保留静态背景的同时跟踪动态目标，以避免主体在画面中“消失”，旨在提升长时视频理解能力。 [来源-huggingface](https://huggingface.co/papers/2603.25716)

---

*（注：39 条统计包含本期的重点报道与快讯速览。）*

## ⚡ 快讯速览

- **ShotStream 支持实时交互式多镜头视频生成** — 通过 ShotStream 实现实时交互式视频生成。 [来源-huggingface](https://huggingface.co/papers/2603.25746)
- **Claude Code 最佳实践开源指南发布** — 一份 Claude Code 最佳实践指南现已公开发布。 [来源-github](https://github.com/shanraisshan/claude-code-best-practice)
- **HJB 方程串联起强化学习与 Diffusion 模型** — 讨论如何通过 HJB 将强化学习与扩散模型联系起来。 [来源-rss](https://dani2442.github.io/posts/continuous-rl/)
- **AI 将工作拆分为低薪碎片，而非直接消灭岗位** — 分析指出，AI 更倾向于重组工作任务，而不是完全消除职位。 [来源-rss](https://www.theregister.com/2026/03/24/ai_job_unbundling/)
- **警方使用 AI 人脸识别错误逮捕北达州一名田纳西女性** — 该案例凸显了带偏见或出错的人脸识别系统的风险。 [来源-rss](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)
- **AI 数据中心热潮或演变为 9 万亿美元大泡沫** — 从行业层面评估 AI 基础设施扩张的系统性风险。 [来源-rss](https://www.ft.com/content/805f78f3-8da3-4fc0-b860-207a859ac723)
- **本地 Qwen3-VL 支持无需转录的语义视频搜索** — 本地运行的 Qwen3-VL 能在无需转录的情况下实现语义视频搜索。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7u4fr/semantic_video_search_using_local_qwen3vl/)
- **通过 Text-to-SQL 基准测试小型本地与 OpenRouter 模型** — 使用 Text-to-SQL 任务对本地模型进行基准评估。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7r9wu/i_tested_as_many_of_the_small_local_and/)
- **llama.cpp 在 Apple Silicon 上接入 Apple ANE 后端** — Apple Neural Engine 后端为 Apple Silicon 上的 llama.cpp 带来更高性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s835d5/new_apple_neural_engine_ane_backend_for_llamacpp/)
- **llama.cpp 斩获 10 万 Star** — llama.cpp 在社区采用度上达成重要里程碑。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7z7hj/llamacpp_at_100k_stars/)
- **OpenRouter 上出现 Qwen 3.6 Plus 预览版** — 预览发布预示着即将到来的性能改进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7zy3u/qwen_36_spotted/)
- **Sakana AI 就新 LLM 系列 Namazu 命名争议致歉** — 围绕 LLM 产品线命名所产生的一场争议。 [来源-x](https://x.com/iwiwi/status/2038535561921839133)
- **分享一些隐藏但实用的 Claude Code 功能** — 揭示 Claude Code 中一些鲜为人知的功能点。 [来源-x](https://x.com/bcherny/status/2038454336355999749)
- **Hermes Agent v0.6 新增 HLS 播放支持** — Hermes Agent 新增对 HTTP Live Streaming 播放的支持。 [来源-x](https://x.com/NousResearch/status/2038688578201346513)
- **Boaz Barak 博文：用四张虚构图表审视 AI 安全现状** — 以批判视角审视主流 AI 安全叙事。 [来源-x](https://x.com/sama/status/2038640963036626971)
- **通过实践而非阅读来学习 Claude Code** — 一种以实作驱动的 Claude Code 学习方法。 [来源-rss](https://claude.nagdy.me/)
- **AI 重写工程师职级晋升阶梯** — 探讨 AI 如何重塑工程师的职业发展路径。 [来源-rss](https://negroniventurestudios.com/2026/03/19/the-ladder-is-missing-rungs/)
- **AI 泡沫将如何破裂** — 分析 AI 市场动态与过度乐观可能带来的后果。 [来源-rss](https://martinvol.pe/blog/2026/03/30/how-the-ai-bubble-bursts/)
- **GitHub 上的 Claude Code 可视化指南** — 一份讲解 Claude Code 用法的图文可视化指南。 [来源-github](https://github.com/luongnv89/claude-howto)
- **AI 时代的数学方法与人类思维** — 一篇 arXiv 预印本，探讨数学方法与认知在 AI 时代的关系。 [来源-arxiv](https://arxiv.org/abs/2603.26524)
- **Claude Code 每 10 分钟自动执行 git reset --hard origin/main 重置仓库** — 仓库会定期重置到远程 origin 状态。 [来源-github](https://github.com/anthropics/claude-code/issues/40710)
- **Miasma 让 AI 网络爬虫困在无尽“毒坑”中** — 该项目演示了数据抓取可能遭遇的种种陷阱。 [来源-github](https://github.com/austin-weeks/miasma)
- **如果 AI 不需要更多内存，而是需要更好的数学？** — 围绕效率与以数学为中心的 AI 改进展开讨论。 [来源-rss](https://adlrocha.substack.com/p/adlrocha-what-if-ai-doesnt-need-more)
- **AI 时代的前 40 个月：一份回顾** — 对迄今为止 AI 时代的回顾性梳理。 [来源-rss](https://lzon.ca/posts/other/thoughts-ai-era/)
- **关于 TurboQuant 与 RaBitQ 讨论的技术澄清** — 针对模型量化工具的若干技术澄清。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7nq6b/technical_clarification_on_turboquant_rabitq_for/)
- **提醒：Claude Code 会破坏本地 KV 缓存；可通过设置修复** — 提供一个修复 Claude Code 缓存问题的实用设置方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7tn5s/psa_using_claude_code_without_anthropic_how_to/)
- **llamafile v0.10.0 采用新构建系统以兼容 llama.cpp** — 为兼容 llama.cpp 而更新构建系统。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7xnd2/llamafile_v0100/)
- **首个语言模型可追溯至 1913 年的 Markov** — 一则关于语言建模起源的历史小注。 [来源-x](https://x.com/jxmnop/status/2038640532700946851)
- **Claude 的“秘制配方”是什么，为何难以复制？** — 关于 Claude 设计特性的讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s7pxie/what_is_the_secret_sauce_claude_has_and_why_hasnt/)

---
*由 AI News Agent 生成 | 2026-03-30*