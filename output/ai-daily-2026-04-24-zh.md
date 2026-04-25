---
title: "AI 日报 — 2026-04-24"
description: "GPT-5.5覆盖Copilot，Codex增浏览测试，DeepSeekV4开源。"
lang: "zh"
pairSlug: "ai-daily-2026-04-24"
---

# AI 日报 — 2026-04-24

> 覆盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. GPT-5.5 推向 Copilot、M365 Copilot、Studio 与 Foundry

GPT-5.5 正在陆续上线 GitHub Copilot、M365 Copilot、Copilot Studio 和 Foundry，带来更强的推理能力、更可靠的多步执行，以及在长时、复杂任务上的更好表现。此次更新强调在完整工作流中为每个任务选择合适的模型，以更少迭代加速从想法到落地的过程。它进一步凸显了微软在生产力和开发者工具中持续深化 AI 集成的趋势。[来源-twitter](https://x.com/satyanadella/status/2047743651053556126)

### 2. Codex 支持浏览器内测试，闭合构建-验证闭环

OpenAI 的 Codex 现已支持基于浏览器的测试，使其能够像真实用户一样点击操作应用来构建前端并进行测试。它利用视觉能力“看到”用户所见，并检查网络/控制台日志来调试和修复问题，从而加速自主编程流程。更新中特别提到支持 HLS 播放，并演示了一个测试与功能交付的迭代闭环。[来源-twitter](https://x.com/JamesZmSun/status/2047522852854026378)

### 3. DeepSeek-V4 Preview 开源，支持 100 万上下文长度

DeepSeek 发布了开源的 DeepSeek-V4 Preview，包含两种配置：DeepSeek-V4-Pro（总参数 1.6T，激活参数 49B）和 DeepSeek-V4-Flash（总参数 284B，激活参数 13B）。它主打高性价比的 100 万上下文长度，同时带来 API 更新，并可通过 chat.deepseek.com 访问，伴随技术报告以及在 Hugging Face 上公开的 Open Weights。[来源-twitter](https://x.com/deepseek_ai/status/2047516922263285776)

## 📰 重点报道

### LLM

- **Google 将向 Anthropic 投资 100 亿美元，后续计划再投 300 亿美元** — Google 已同意按当前估值向 Anthropic 投资 100 亿美元，并计划未来最多追加 300 亿美元。这一动作发生在 Google 自身已有 Gemini AI 模型的背景下，凸显其在 AI 能力投入和战略合作上的大力度推进。[来源-twitter](https://x.com/FT/status/2047715653553942997)
- **本地 Qwen3.6 27B 通过 Llama.cpp 在 MacBook Pro 上运行** — 一位 AI 爱好者展示了使用 Llama.cpp，在 Pi 编码代理中本地运行 Qwen3.6 27B 于 MacBook Pro 上，即使在飞行模式下也能工作。帖子认为，本地模型的能力正在接近 Claude Code 的 Opus，并将强大的端侧 AI 描述为提升效率、安全性和主权控制的一条路径。[来源-twitter](https://x.com/julien_c/status/2047647522173104145)
- **LLaTiSA：从视觉感知到语义的难度分层时间序列推理** — 研究者正式提出了时间序列推理（TSR）的一个四层分类体系，以解决基于 LLM 的时间序列理解中任务定义支离破碎的问题。他们引入了 HiTSR，一个分层时间序列推理数据集，用于实现更严格的评测，并推动统一的 TSRM（时间序列推理模型）发展。[来源-huggingface](https://huggingface.co/papers/2604.17295)
- **Cline：带有人类参与环节的 IDE 自主编码代理** — Cline 是一个开源 AI 助手，可在你的 IDE 内运行，具备创建/编辑文件、执行命令以及在用户授权下借助浏览器完成任务的能力。它利用 Claude Sonnet 的代理式编程能力和 Model Context Protocol 来扩展功能，同时通过有人类参与的图形界面，确保每一次文件修改和终端命令都需用户确认。[来源-github](https://github.com/cline/cline)
- **Context-Mode 精简 AI 上下文，同时保留会话连续性** — Context Mode 是一个开源 MCP 服务器，通过对工具输出进行沙箱化，优化 AI 编码代理的上下文窗口使用。它宣称能将原始数据注入上下文的规模减少 98%，并通过在 SQLite 中记录编辑、任务和决策来维持会话连续性，再利用基于 BM25 的检索仅拉取相关数据。该项目托管于 GitHub 的 mksglu/context-mode 仓库，旨在防止在对话压缩和长时间会话中出现上下文丢失。[来源-github](https://github.com/mksglu/context-mode)
- **Anthropic 降级托管模型后又回滚变更** — Anthropic 承认曾短暂降低 Claude Code 的推理投入来减小延迟，结果导致托管模型看起来变得不那么强大。在收到用户反馈后，公司恢复了更高智能的默认设置，并修复了引起重复回答的清空会话 Bug；受影响的包括 Sonnet 4.6 和 Opus 4.6。这个事件被一些人视为证明开放权重和本地模型在可靠性方面价值的例证。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1suef7t/anthropic_admits_to_have_made_hosted_models_more/)
- **VLLM PR：Cohere 即将发布新 MoE 模型** — 一则 Reddit 帖子通过 VLLM PR 仓库的变更，预告 Cohere 即将发布一种新的混合专家（MoE）模型。帖子没有提供技术细节，也尚无官方确认。如果成真，将意味着 Cohere 在 LLM 产品上可能借助 MoE 模型获得更好的可扩展性收益。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sujzpf/vllm_pr_new_moe_model_from_cohere_soon/)

### Multimodal

- **WorldMark：交互式视频世界模型的统一基准** — WorldMark 提出了一套标准化基准，用于在同一场景和动作序列下评估交互式视频世界模型，试图解决 Genie、YUME、HY-World、Matrix-Game 等模型之间评测割裂的问题。通过提供统一的测试条件和控制接口，WorldMark 旨在让跨模型比较更公平，并采用标准化指标进行评估。[来源-huggingface](https://huggingface.co/papers/2604.21686)

### AI Agents

- **VoltAgent 发布 1000+ Agent 技能仓库** — VoltAgent 推出一个精心整理的代理技能集合，包含超过 1000 个真实世界的 agent 技能，由官方开发团队和社区共同贡献。该仓库列出来自 Anthropic、Google Labs、Vercel、Stripe、Cloudflare、Netlify、Trail of Bits、Sentry、Expo、Hugging Face、Figma 等厂商的官方技能，可与 Claude Code、Codex、Gemini CLI、Cursor 等工具配合使用。项目自称是贡献最积极的 agent 技能仓库之一，由活跃的社区共同打造。[来源-github](https://github.com/VoltAgent/awesome-agent-skills)

### AI Safety

- **AI 在电脑上“笨拙操作”的短暂时代之后将迎来极速发展** — 一条推文描绘了这样一个短暂阶段：AI 在电脑上操作时还会像人类那样笨拙地点击、失败、花很久写代码。它认为转瞬之间，这些系统就会以远超人类监控速度的效率操控电脑。该观点强调，AI 使用形态将从试错式交互转向快速、甚至难以被监控的自动化。[来源-twitter](https://x.com/tszzl/status/2047766300756488675)

### Open Source

- **Hugging Face 发布 ml-intern：开源 ML 工程师 CLI** — ml-intern 是一个开源命令行工具，像一名自主的 ML 工程师，能够在 Hugging Face 生态中阅读论文、训练模型并完成模型上线。它支持交互式与无头模式，提供简单的安装与快速开始配置，可接入包括 anthropic/claude-opus-4-6 在内的多种模型。该项目旨在通过单一工具界面整合 ML 研究、数据与云计算资源，简化从研究到部署的工作流。[来源-github](https://github.com/huggingface/ml-intern)
- **Open-Generative-AI：含 200+ 模型的无审查开源 Studio** — Open-Generative-AI 提供一个完全开源、自托管的替代方案，用于取代 Higgsfield AI、Freepik 等商业 AI Studio。它集成 200 多个模型，不设内容过滤，并采用 MIT 许可证，支持无审查的图像与视频生成；项目托管在 GitHub 上，并鼓励借助 AI 编码代理进行自动化。[来源-github](https://github.com/Anil-matcha/Open-Generative-AI)
- **免费 Claude Code 代理，实现跨服务零成本访问** — 一个 GitHub 项目提供轻量级代理，将 Claude Code 的 Anthropic API 调用路由到多个后端（NVIDIA NIM、OpenRouter、DeepSeek、LM Studio、llama.cpp）。它声称通过 NVIDIA NIM 可获得每分钟 40 次请求额度的免费使用，并且无需 Anthropic API key。该工具可通过终端、VSCode 扩展或 Discord 机器人使用，支持按模型映射配置，并与 Claude Code CLI/VSCode 实现即插即用兼容。[来源-github](https://github.com/Alishahryar1/free-claude-code)
- **ONNX Runtime：跨平台 AI 推理与训练加速器** — ONNX Runtime 提供一个跨平台推理与训练加速引擎，支持来自 PyTorch、TensorFlow/Keras 以及 scikit-learn、LightGBM、XGBoost 等经典 ML 库的模型。它通过利用硬件加速器和计算图优化来实现更快推理和更低成本；在训练方面，通过在多节点 NVIDIA GPU 上对 Transformer 模型进行支持，只需在 PyTorch 脚本中添加少量改动即可启用。[来源-github](https://github.com/microsoft/onnxruntime)

## ⚡ 快讯速览

- **LeCun：LLM 很有用，但仍需要世界模型与规划能力** — Yann LeCun 认为，尽管 LLM 很有用，但如果缺乏世界模型和零样本规划，它们就无法在现实世界中高效运行。他主张，一个机器人密集的未来需要系统真正理解物理世界并预判后果，同时在讨论中也提到反乌托邦式视觉表现与个人着装等话题。[来源-twitter](https://x.com/ylecun/status/2047636569767419951)
- **面向 AI Agents 与 Claude Code 的营销技能库** — coreyhaines31/marketingskills 提供了一套专注于营销任务的 AI agent 技能，面向使用 AI 编码代理进行转化率优化、文案、SEO、分析与增长工程的技术型市场人员和创业者。它支持 Claude Code、OpenAI Codex、Cursor、Windsurf 以及其他实现 Agent Skills 规范的代理，并鼓励社区贡献；项目同时引用 Magister、Conversion Factory、Swipe Files、Coding for Marketers 等相关资源与工具。[来源-github](https://github.com/coreyhaines31/marketingskills)
- **r/LocalLLaMa 更新版规以遏制垃圾机器人** — r/LocalLLaMa 子版块的版主宣布首次更新社区规则，以应对流量增长带来的劣质内容与垃圾信息。更新在规则 3 和规则 4 中加入了明确的最低业力值要求，并通过幻灯片详细说明变更，FAQ 中解释了为何新创建的机器人账号会被重点拦截，而业力高的老账号可能绕过 Reddit 的通用防御。管理团队将持续监测影响并计划未来进一步调整。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1su3ao4/rlocalllama_rule_updates/)
- **LocalLLaMA 当前进展一览** — 用户 /u/jacek2023 在 Reddit 上发布帖子，概述 LocalLLaMA 项目的当前状态。帖子附带相关讨论与评论链接，对项目现状进行集中梳理。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1suqfba/this_is_where_we_are_right_now_localllama/)
- **Chip Huyen《AI Engineering》图书资源中心** — 一个 GitHub 仓库聚合了 AI 工程师的学习资源及 Chip Huyen《AI Engineering》一书的配套材料。内容包括章节摘要、学习笔记、案例研究、提示词示例、错配分析，以及 ChatGPT 与 Claude 热力图生成器等工具，书中重点讲解如何将基础模型端到端适配到真实世界问题；该书已在 Amazon、O'Reilly、Kindle 等渠道上架，并非以大量代码示例为主的教程类读物。[来源-github](https://github.com/chiphuyen/aie-book)
- **AMA：Nous Research——开源 Hermes Agent 实验室** — 将举办一场与 Nous Research 团队的 AMA 活动，他们是开源 Hermes Agent 的开发者。活动时间为 4 月 29 日（周三）上午 8:00–11:00（PST），在单独的帖子中进行，本贴仅为预告。讨论将面向 r/LocalLLaMA 社区展开。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1suw9on/ama_announcement_nous_research_the_opensource_lab/)

---

*由 AI News Agent 生成 | 2026-04-24*