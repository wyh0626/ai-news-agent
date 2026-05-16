---
title: "AI 日报 — 2026-05-15"
description: "OpenAI增理财Anthropic推MonetFigure扩展50小时排序直播"
lang: "zh"
pairSlug: "ai-daily-2026-05-15"
---

# AI 日报 — 2026-05-15

> 覆盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 为 ChatGPT Pro 推出个人理财功能

OpenAI 为美国地区的 ChatGPT Pro 用户上线了个人理财功能，支持通过 Plaid 安全连接银行账户，提供支出看板，以及基于真实交易数据进行落地问答的 GPT-5.5。未来还将集成 Intuit，用于估算税务和申请信用卡，系统会在多轮对话间持久化上下文记忆。此次功能首先仅向 Pro 用户开放，之后将扩展到免费层。 [来源-twitter](https://x.com/kimmonismus/status/2055320528198521041)

### 2. Anthropic 发布 Claude Monet；画师要“熟了”？

Anthropic 宣布了一款名为 Claude Monet 的产品。配套文案中使用了“Painters are cooked”（画家要熟了）这样的表述，暗示其可能具备艺术创作或多模态能力，尽管目前并未给出技术细节。关于该模型的具体能力、发布时间或技术参数，在这条推文中都尚未披露。 [来源-twitter](https://x.com/fabianstelzer/status/2055176830907285573)

### 3. Figure 机器人直播已连续自主分拣 50+ 小时

Figure 正在直播其自主包装机器人，以展示其不间断运行能力。团队称这些机器人已连续运行超过 50 小时无停机，累计分拣包裹超过 63,000 个，并且目前仍在持续运行，直到出现故障为止。 [来源-twitter](https://x.com/adcock_brett/status/2055376836218310926)

## 📰 重点报道

### LLM

- **统一缩放策略将 AI 推理能力提升到奥赛金牌水平** — AI 推理模型在数学与物理奥林匹克竞赛（IMO 和 IPhO）上的表现已经接近金牌水平。一篇新论文提出了一套简单统一的流程，将一个后训练过的推理骨干模型转化为奥赛级解题器，其起点是基于“反困惑度”（reverse-perplexity）的监督微调课程设计。该工作凸显了 AI 在长链条数学与科学问题求解上的新进展。 [来源-huggingface](https://huggingface.co/papers/2605.13301)
- **MemLens 基准评估 LVLM 的多模态长期记忆能力** — MemLens 提出了 MEMLENS，这是一套用于评估多模态、多轮会话记忆能力的综合性基准。它包含 789 个问题，覆盖五大类记忆维度，旨在系统对比长上下文 LVLM 与带记忆增强的智能体在需要多模态证据支持的任务上的表现。MEMLENS 托管在 HuggingFace 上，试图填补当前多模态记忆评测方面的空白。 [来源-huggingface](https://huggingface.co/papers/2605.14906)
- **Orthrus-Qwen3-8B：冻结骨干；输出分布完全一致** — Orthrus-Qwen3-8B 在一个冻结的自回归 Transformer 每一层中插入可训练的 diffusion attention 模块，与 AR 头共享 KV cache。diffusion 头一次并行处理 32 个 token，而 AR 头在第二遍验证输出，从而在理论上保证其输出分布与基础 Qwen3-8B 完全一致。该方法在 MATH-500 上实现最多 7.8 倍 tokens-per-forward 和约 6 倍壁钟时间加速，仅需训练 16% 的参数；与其他 diffusion LM 不同，它无需修改基座权重，也不需要像推测解码那样额外的 drafter 或单独的 cache，同时还能保持 Qwen3-8B 的准确率。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te5xpu/orthrusqwen38b_up_to_78tokensforward_on_qwen38b/)
- **字节跳动 Seed 团队发布 Cola-DLM 扩散语言模型** — Cola DLM 是一种分层连续潜空间扩散语言模型，将 Text VAE 与块因果 Diffusion Transformer（DiT）先验相结合。VAE 负责将文本映射到连续潜变量序列并将其解码回 token，而 DiT 通过 Flow Matching 在潜空间中进行先验迁移；仓库提供 HuggingFace 格式的 checkpoint，并附有相关论文、GitHub 仓库及项目/博客页面链接。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdtaqt/bytedanceseedcoladlm_hugging_face/)
- **ChatGPT 订阅现已可在 Zed Agent 中使用** — Zed 的智能体现在支持使用 ChatGPT 订阅，使用方式和速率限制与此前支持的 Codex 一致。尽管有些服务商正在转向按用量计费，OpenAI 开发者账号 (@openaidevs) 仍在支持基于订阅的第三方工具接入。这让 Zed 中的工具集成可以无缝使用 ChatGPT。 [来源-twitter](https://x.com/zeddotdev/status/2055335727483781624)
- **Anthropic 获得 xAI GPU，开始复刻 Codex 战术手册** — 有消息称 Anthropic 从 xAI 处拿到了 GPU，并迅速开始执行类似 Codex 的产品和运营策略。这一举动表明 AI 竞争进一步加剧，开发者有望从中获益。 [来源-twitter](https://x.com/Yuchenj_UW/status/2055349045556814029)
- **Garry Tan 推出 gstack：一个人就能当 6 种角色的 23 个 AI 工具栈** — Garry Tan 推广 gstack，这是一个由 23 个精挑细选的工具组成的集合，旨在让单人开发者通过 AI agents 同时扮演 CEO、设计师、工程经理、发布经理、文档撰写者和 QA 等多种角色。他认为只要工具合适，独立创作者的推进速度可以媲美团队规模开发，并提到 OpenClaw 和 Andrej Karpathy 的观点作为灵感来源。 [来源-github](https://github.com/garrytan/gstack)
- **自托管 MCP 服务器为本地 LLM 提供实时金融数据** — Equibles 是一个自托管 MCP 服务器，用于抓取并提供美国公开金融数据（SEC 文件、13F、内幕与国会议员交易、FINRA 做空数据、FRED、CFTC 期货、VIX 等）给支持 MCP 的客户端。它完全本地运行，不依赖云端或遥测，使任何本地模型智能体都能查询最新信息。仓库地址：https://github.com/daniel3303/Equibles [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te2jko/i_built_a_selfhosted_opensource_mcp_server_that/)
- **Intern-S2-Preview：35B 科学多模态模型，横跨数百项任务** — Intern-S2-Preview 是一款 350 亿参数的科学多模态基础模型，通过从预训练到强化学习的全链路训练流程，在数百种专业科学任务上实现可扩展的任务覆盖。其在核心科学任务上的表现据称可比肩万亿级的 Intern-S1-Pro，同时保持强大的通用推理、多模态理解与智能体能力。该模型在 Qwen3.5 基础上继续预训练，并强调通过任务规模扩展而非仅仅参数/数据扩展来提升能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdrw0s/internlminterns2preview_hugging_face/)
- **SupraLabs 发布面向大众的开源小型 AI 模型** — 新实验室 SupraLabs 宣布其使命是训练、微调并探索小型开源 AI 模型，以提升 AI 的可及性。他们目前在 Hugging Face 上托管了如 Supra-Mini-v4-2M 等模型，并规划后续发布 StorySupra 10M 与 Supra Mini v5 5M 等模型，更新将通过其 Hugging Face Spaces 博客发布，同时也邀请社区参与与支持。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdvvf2/founding_supralabs_real_opensource_ai_models_for/)
- **Qwen-35B-A3B 动态算力分配，在 HLE 上逼近 GPT-5.4** — 一条 Reddit 帖子声称，在一组高难度问题上，对子问题和演化片段使用 Qwen-35B-A3B 动态分配计算预算，可以获得接近 GPT-5.4-xHigh 在 HLE 指标上的表现。该说法凸显了当前 LLM 研究中围绕算力高效评估与模型优化策略的持续探索。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te8sxt/dynamically_allocating_compute_budget_to_hard_set/)

### Edge AI

- **基于 Jetson Orin NX 与 Gemma 4 E4B 的全离线行李箱机器人** — 一位工程师打造了一个完全离线运行的行李箱机器人，采用 Jetson Orin NX 驱动，并在其上运行 Gemma 4 E4B 与带 q8_0 KV cache 的 llama.cpp。该系统支持 12K 上下文，缓存条件下 TTFT 约 200ms，生成速度为 14–15 token/s，每轮提示中描述 30+ 个传感器；所有 STT、TTS、视觉和 OCR 都在本地端侧完成，无需联网。设计者强调保持 prompt 结构对 cache 友好的重要性，并邀请其他人对比在 Orin 级硬件上的 tok/s 和传感器/工具上下文处理能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdz5gr/built_a_fully_offline_suitcase_robot_around_a/)

### Multimodal

- **Causal Forcing++ 实现 1–2 步实时视频扩散生成** — 研究者提出 Causal Forcing++，在逐帧自回归架构下推进实时视频生成。他们研究了 1–2 步采样机制，用以替代当前分块 4 步蒸馏方案，从而降低延迟并实现更精细的响应控制。该工作针对现有自回归扩散蒸馏中粒度过粗的问题，提出适用于流式视频的可扩展实时方法。 [来源-huggingface](https://huggingface.co/papers/2605.15141)

### RL

- **自蒸馏智能体强化学习：面向多轮 LLM 的 OPSD** — On-Policy Self-Distillation（OPSD）为后训练阶段的 LLM 智能体提供基于 token 级别的指导，通过带有特权上下文的教师分支来实现。当将 OPSD 扩展到多轮智能体时，会出现复合型不稳定性，从而削弱监督信号的有效性。 [来源-huggingface](https://huggingface.co/papers/2605.15155)

### Open Source

- **SANA-WM：面向分钟级视频的 2.6B 世界模型** — SANA-WM 是一个开源、26 亿参数的世界模型，专为生成时长 1 分钟、分辨率 720p 的视频设计，并支持精确的相机控制。其视觉质量可匹敌 LingBot-World 和 HY-WorldPlay 等大型基线模型，同时大幅提升效率。该架构以 Hybrid Linear Attention 为核心，将逐帧的 Gated DeltaNet 与 softmax attention 结合，并配合其他关键设计。 [来源-huggingface](https://huggingface.co/papers/2605.15178)
- **AllenAI 发布开源机器人控制模型 MolmoAct2 系列** — AllenAI 正在发布 MolmoAct2 的迭代微调版本，这是一款 50 亿参数的视觉-语言-动作模型，可用于机器人控制，覆盖多个机器人数据集（LIBERO、DROID、BimanualYAM、SO100_101）。所有发布版本均提供开源权重、训练数据、训练代码以及技术论文。MolmoAct2 系列被定位为适用于 LLM 驱动机器人控制的即插即用方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te9unl/allenai_has_been_iterating_on_their_molmoact2/)

### Hardware

- **4 张 RTX 3090 横向扩展：Qwen 3.6 的 220W 能效甜点** — 一份深入测试对比了在 vLLM TP=4 配置下，四张 RTX 3090 运行 Qwen 3.6-27B 时的功耗与吞吐量。结果显示在约 220W 时能效达到峰值，而超过 250W 后回报递减，同时在多种配置下吞吐量仍保持较高水平。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te9o18/finding_the_4x_3090_sweet_spot/)
- **Snapdragon X2 笔电上对 20 万文档做 RAG** — 一条 Reddit 帖子展示了搭载 Qualcomm Snapdragon X2 Elite Extreme（2026）的华硕 Zenbook A16，称赞其极轻机身与便携充电器。帖子指出其 NPU 在嵌入与索引任务中表现强劲，大约相当于 RTX 5060 约 50% 的速度，却具有更轻便的形态，并展示了在约 20 万文件数据集上的 VecML AI-PC 软件演示，同时提到航班上充电功率受限的问题。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te93s3/rag_on_snapdragon_x2_laptop_200k_documents/)

### AI

- **Gemma4 26B MoE 在 MLX 中配合 Turboquant 与自定义 Kernel 运行** — 一位独立开发者展示了在 MLX 中运行 Gemma4 26B MoE 的方案，结合 turboquant 与旋转 KV cache。在一台拥有 128k 上下文和 4 路并发 batch 的 MacBook Air M5 上，其在 prompt 处理、速度与内存占用上可以与甚至超越在 8k 上下文下运行的 llama.cpp。该方案依赖自定义 SWA kernel 来实现 2-bit 级别的内存节省，从而在保持接近 FP16 的 prompt 性能的同时支持更大 batch，在长 prompt 的文本生成上有显著收益。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1te6os6/gemma4_26b_moe_running_in_mlx_with_turboquant_and/)

## ⚡ 快讯速览

- **Mitchell Hashimoto 警告：AI 炒作正在威胁软件的韧性** — Mitchell Hashimoto 指出许多公司陷入“AI 精神错乱”，理性对话变得困难。他借云基础设施中 MTBF 与 MTTR 的争论，强调快速修 bug 不能取代构建高韧性软件。他警惕在“AI agent 会大规模自动修复”的幻想下故意带 bug 上线，强调整体系统韧性的重要性。 [来源-twitter](https://x.com/mitchellh/status/2055380239711457578)
- **Grok Build 测试版主打极速编码，对标 Anthropic 与 xAI** — 面向 SuperGrok Heavy 订阅用户的 Grok Build 早期测试版已上线，它是一个面向编码、应用构建与流程自动化的 agent 型 CLI。该测试版邀请用户反馈以改进模型和产品，并被定位为对 Anthropic 与 xAI 的直接挑战。可通过 x.ai/cli 访问测试版。 [来源-twitter](https://x.com/theo/status/2055081594537537941)
- **Anthropic 为所有用户重置 5 小时与周度调用上限** — 据 ClaudeDevs 所述，Anthropic 已为所有用户重置 5 小时及每周调用次数上限。这一举措可能反映出其从 xAI Colossus 计算集群中获益，或受到 OpenAI 与 Codex 竞争压力；无论原因如何，用户都将从更高吞吐中获利。 [来源-twitter](https://x.com/kimmonismus/status/2055364277234528399)
- **LinkedIn 个人简介中的 prompt 注入，让猎头用古英语称呼我为“Lord”** — 一位用户在 LinkedIn 个人简介中疑似加入了 prompt 注入，结果导致猎头用古英语回复并称呼其为“Lord”。这条帖子展示了 prompt 注入或 AI 提示词如何影响现实世界的人际互动，凸显了社交平台中潜在的 AI 安全问题。 [来源-twitter](https://x.com/tmuxvim/status/2055275374905307216)
- **在 DGX Spark 上通过 Ollama 本地运行 Hermes Agent** — NousResearch 给出了一份在 DGX Spark 系统上完全本地运行 Hermes Agent 的操作手册。指南逐步演示如何通过 Ollama 搭建该智能体。这使得在高性能硬件上实现无需云端的本地 AI agent 成为可能。 [来源-twitter](https://x.com/NVIDIA_AI_PC/status/2055317325444710872)
- **Roboflow Supervision：与模型无关的通用视觉工具包** — Roboflow 的 supervision 项目提供一个可复用、与具体模型无关的计算机视觉工具包，覆盖从数据加载到实时区域计数的完整流程。它支持与 Ultralytics、Transformers、MMDetection 和 Inference 等热门库的连接，并能集成 rfdetr，用户只需简单的 pip 安装即可开始，并有示例代码可用。 [来源-github](https://github.com/roboflow/supervision)
- **NVIDIA 面向视频搜索与摘要的 AI Blueprint** — NVIDIA 的视频搜索与摘要（VSS）AI Blueprint 提供了构建 GPU 加速视觉 agent 和 AI 驱动视频分析的参考架构。它将加速视觉微服务与视觉语言模型（VLM）及大语言模型（LLM）结合，支持集成到现有应用、独立微服务或更大的视觉 agent 中。该 Blueprint 强调实时视频智能，包括特征提取、embedding 生成与流式理解，并托管在 GitHub 上。 [来源-github](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)
- **“内存富足、GPU 匮乏” vs 本地 LLM 前沿之争** — 有帖子讨论本地 LLM 的两条前沿路径：一是可装入中端 GPU（32GB/24GB）的致密模型；二是约 100B 参数、可部分 offload 到 128GB 内存的 MoE 模型。帖子指出目前 MoE 选择不多（如 Qwen 3.5 122B，尚无 3.6 版本），质疑内存富足但 GPU 较弱的用户是否选择受限，并提到小模型在工具调用和速度上的问题。文中还引用了 Qwen 27B、预计 Q3 的 minimaxi、DeepSeek V3 以及 Strix Halo GPU 等作为当前硬件环境的背景。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdyf75/are_the_rich_ram_poor_gpu_people_wrong_here/)
- **OpenMOSS GGML C++ 语音合成全流程发布** — 一条 Reddit 帖子宣布了基于 GGML、由纯 C++ 实现的 OpenMOSS 全流程 TTS 管线。该项目旨在简化 TTS 部署，既支持服务器模式，也支持单次命令行调用。OpenMOSS 被特别提到可支持除英语/中文之外的语言，如波兰语。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdwo1f/github_pwilkinopenmoss_openmoss_pure_c_pipeline/)
- **“Claude Code For Real Engineers” 演变为 “AI Coding For Real Engineers”** — 一则帖子对比了 Claude 以编码为核心的早期产品“Claude Code For Real Engineers”与当前版本“AI Coding For Real Engineers”的差异。这反映了品牌与能力从单纯的代码助手向更广义的 AI 辅助工程开发转变，凸显 Claude 在面向开发者 AI 工具上的持续布局。 [来源-twitter](https://x.com/mattpocockuk/status/2055177489538756984)
- **AI Agents 开始“放飞自我”，本地 Orchestrator 试验启动** — 一条 Reddit 帖子指出 AI agents 的能力与行为都变得更强也更“怪”。作者尝试在 Qwen 和 Gemma 不可用时，加入一个 orchestrator 来协调本地 AI 模型。该帖展现了社区在本地 AI 流水线与编排层面持续折腾与试验的现状。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1teca8q/opencode_you_naughty_minx/)
- **黑领结晚宴 + 城堡场地的“Group AI psychosis” 聚会** — 一则社交媒体帖子描述了一场在本地城堡、着黑领结礼服举行的“Group AI psychosis sesh”活动。该帖子更像是表情包式内容而非实际 AI 技术进展，几乎没有参与者或产出的具体信息，体现了社交媒体上围绕 AI 文化的各种怪诞梗图与亚文化。 [来源-twitter](https://x.com/TaylorLorenz/status/2055366400479261118)

---

*由 AI News Agent 生成 | 2026-05-15*