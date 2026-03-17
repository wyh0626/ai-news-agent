---
title: "AI 日报 — 2026-03-16"
description: "英伟达推代理AI硬件，Lambda接入超智能云，视言模型或解壳游戏。"
lang: "zh"
pairSlug: "ai-daily-2026-03-16"
---

# AI 日报 — 2026-03-16

> 覆盖 47 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA 发布面向 Agentic AI 的 Vera CPU

NVIDIA 宣布推出 Vera CPU，这是一款专门为 agentic AI 工作负载打造的处理器。该硬件主打优化自主 AI 智能体及相关工作负载，表明 NVIDIA 正在将其 AI 基础设施布局从 GPU 拓展到更广泛的领域。该发布在 Hacker News 上引发了广泛讨论。[来源-hackernews](https://nvidianews.nvidia.com/news/nvidia-launches-vera-cpu-purpose-built-for-agentic-ai)

### 2. 视觉-语言模型能玩懂“猜壳游戏”吗？

VET-Bench 被提出为一个合成诊断测试平台，使用外观完全相同的物体，并要求模型通过时空连续性来进行跟踪。研究表明，当前最先进的视觉-语言模型在该基准上的表现接近随机水平，暴露出视觉实体追踪上的隐藏缺陷。结果表明，视觉-语言追踪研究需要更强大的模型以及更严谨稳健的基准。[来源-huggingface](https://huggingface.co/papers/2603.08436)

### 3. Lambda 在 GTC 2026 将 NVIDIA 硬件接入 Superintelligence Cloud

Lambda 在 NVIDIA GTC 2026 上宣布对 Superintelligence Cloud 的四项基础设施升级：引入 NVIDIA Vera CPU、新的 Lambda Bare Metal Instances、NVIDIA Photonics 以及 NVIDIA STX。通过集成 NVIDIA 硬件和先进互联，这些更新旨在为顶尖团队提供可扩展、可靠的 AI 工作负载支持。此举将 Lambda 的云服务与 NVIDIA 最新技术进一步深度绑定，用以支撑大规模 AI 开发。[来源-twitter](https://x.com/LambdaAPI/status/2033642834624983191)

## 📰 重点报道

### LLM

- **Leanstral：Mistral 发布的开源 Lean 4 代码 Agent** — Leanstral 是首个面向 Lean 4 的开源代码 Agent，Lean 4 是用于表达复杂数学对象与软件规格的证明助理。该模型属于 Mistral Small 4 家族的一员，采用 128 个专家（每个 token 激活 4 个）的 Mixture-of-Experts 架构，总参数量 119B、每个 token 激活 6.5B，并支持 256k token 上下文。它可接收文本和图像输入并输出文本，面向证明工程场景，支持 Proof Agentic、Tool Calling 和 Mistral Vibe Vision 等特性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvjvm9/mistralaileanstral2603_hugging_face/)
- **Attention Residuals 在 Kimi 模型中替代传统残差连接** — Attention Residuals 用 softmax 注意力机制替换了等权重的残差流，使每一层可以通过学习到的查询对之前的输出进行注意力聚合。Block AttnRes 在使用 1.25 倍更少计算量的前提下即可匹配基线损失，其基础是一个在 1.4T tokens 上训练的 48B 参数的 Kimi Linear 模型，并在 GPQA-Diamond、数学任务和 HumanEval 基准上取得了提升，同时带来的额外开销很小。讨论中还特别提到了 Karpathy 和 Elie Bakouch 的相关贡献。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rv7ige/residual_connections_havent_changed_for_10_years/)
- **LMEB 推出长时程记忆嵌入评测基准** — Long-horizon Memory Embedding Benchmark（LMEB）旨在填补对长时程、碎片化且依赖上下文的检索任务中记忆嵌入评估的空白。它为评估像 OpenClaw 这类记忆增强系统中的嵌入效果提供了一个全面框架，超出了传统篇章检索基准的范围。该框架已在 HuggingFace 发布，作为推进 AI 记忆研究的资源。[来源-huggingface](https://huggingface.co/papers/2603.12572)
- **XSkill 让多模态智能体具备持续学习能力** — XSkill 提出了一种面向多模态智能体的持续学习方法，通过从过去轨迹中学习而无需更新模型参数。它识别出两类可复用知识形态——经验与技能——用于指导工具选择和决策过程，从而提升工具使用与编排的效率和灵活性。这项工作旨在增强在多样化工具环境中的开放式推理任务能力。[来源-huggingface](https://huggingface.co/papers/2603.12056)
- **Anthropic 推出 Claude Partner Network 合作伙伴计划** — Anthropic 宣布启动 Claude Partner Network，以通过不断壮大的合作伙伴生态拓展 Claude 的使用渠道。该计划为合作伙伴提供资源、集成支持与激励措施，加速安全且面向企业级的 AI 部署。[来源-hackernews](https://www.anthropic.com/news/claude-partner-network)
- **Learn Claude Code：Nano 级 Claude Code 式 Agent 教程** — 这篇文章介绍了一个基于 Bash、从零构建的 Claude Code 风格 Agent，详细讲解了最小 Agent 循环（User → messages[] → LLM → response）以及按步推进的 12 个 Session，每次只增加一种机制。教程强调实际的 Agent 模式——工具调用、结果循环和规划——同时指出在线上环境中还需要策略、权限和生命周期等附加层。该项目托管在 GitHub 上的 shareAI-lab/learn-claude-code 仓库。[来源-github](https://github.com/shareAI-lab/learn-claude-code)
- **LocalLlama 宣布新的 Discord 服务器和 Bot** — LocalLlama 宣布推出新的 Discord 服务器以及一个用于测试开源模型的 Bot，并附上邀请链接。帖子提到旧服务器已被前任管理员删除，并指出社区正在朝着更技术向、少梗图的方向成长。新服务器旨在为 LocalLlama 爱好者提供快速问答、硬件展示，以及更高效的比赛与活动组织平台。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1mpk2va/announcing_localllama_discord_server_bot/)
- **NVIDIA 组建 Nemotron Coalition 推进开放 Frontier AI** — NVIDIA 宣布成立 Nemotron Coalition，将 Black Forest Labs、Cursor、LangChain、Mistral AI、Perplexity、Reflection AI、Sarvam AI 和 Thinking Machines Lab 等 AI 实验室联合起来，共同研发开放的 frontier 模型。成员在多模态能力、评测数据集、工具使用与长时程推理、高效可定制模型、可及性 AI 系统、可靠的开放系统、主权语言 AI 和数据协作等方面贡献各自的专长。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvlmzu/nvidia_launches_nemotron_coalition_of_leading/)
- **NVIDIA 推出 Nemotron-3 Nano 4B GGUF 模型** — 一篇 Reddit 帖子提到 NVIDIA 的 Nemotron-3 Nano 4B GGUF 模型，并链接到 LocalLLaMA 的相关讨论。帖子显示该模型为 4B 参数、GGUF 格式，暗示其可能已经对社区开放分享与使用。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvfcxq/nvidianemotron3nano4bgguf/)
- **Mistral Small 4:119B-2603** — 在 LocalLLaMA 子论坛中，用户 /u/seamonn 发布了一篇题为 “Mistral Small 4:119B-2603” 的 Reddit 帖子，并链接到关于 Mistral Small 模型变体的讨论。该帖子本身未给出更多细节，仅能通过链接与评论了解内容，平台评分显示为 0.4。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvlfbh/mistral_small_4119b2603/)
- **Reddit 上出现 Mistral 4 LLM 家族踪迹** — 一条 Reddit 动态报告称发现了 Mistral 4 家族的相关信息，表明 Mistral AI 开源阵营中出现新的成员。该帖由 r/LocalLLaMA 用户 /u/TKGaming_11 发布，指向关于这一发现及其对本地 LLaMA 部署潜在影响的讨论。这也显示出社区围绕开源 LLM 的活动愈发活跃。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvfypu/mistral_4_family_spotted/)
- **Mistral AI 与 NVIDIA 合作加速开放 Frontier 模型** — 一篇 Reddit 帖子指出，Mistral AI 已与 NVIDIA 建立合作关系，以加速开放 frontier 模型的发展。帖子未给出合作范围或具体实施细节，但这次联手表明业界围绕开放与 frontier AI 模型的动能持续增强。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvlfvg/mistral_ai_partners_with_nvidia_to_accelerate/)
- **Mistral 发布官方 NVFP4 模型：Mistral-Small-4-119B-2603-NVFP4** — Mistral 正式发布其 Mistral-Small-4-119B-2603 模型的 NVFP4 变体。相关公告出现在 Reddit 上，确认了该 NVFP4 版本的发布，但在该条目中并未给出技术细节或基准数据。这为研究者和开发者提供了 Mistral 模型阵列中又一个 NVFP4 选项。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvmt4y/mistral_releases_an_official_nvfp4_model/)

### LLMs

- **Qwen3.5-9B 在文档基准中表现亮眼，在 VQA 上也有惊喜** — 一项开放文档 AI 基准在 9000+ 份真实文档上评估了 20 个模型。Qwen3.5-9B 和 Qwen3.5-4B 在原始文本抽取（OlmOCR）中领先，其中 9B 和 4B 版本优于多款 frontier 模型，而 2B 版本则与 GPT-5.4 持平。在 VQA 任务中，Qwen3.5-9B 得分 79.5，仅次于 Gemini 3.1 Pro、略高于 GPT-5.4。各任务的详细拆分可在 idp-leaderboard.org 查看，展示了 Qwen 的优势和短板所在。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rv98wo/qwen359b_on_document_benchmarks_where_it_beats/)

### 生成式 AI

- **Suno AI 的 Neon Oni：虚构乐队演变为真实音乐人** — Suno AI 生成了 Neon Oni，一个拥有虚构简介和 AI 生成视频的日本金属乐队，在 Spotify 上收获了 8 万+ 月听众，甚至还卖出了周边。社区“侦探”将创作者追踪到欧洲，并在视频中发现 AI 生成的“怪手”，随后该创作者招募了 7 位东京本地乐手来现场演奏这些 AI 歌曲，已经举办了数场演出。在近期采访中，创作者表示 AI 实际上创造了工作机会而非取而代之，这种从 AI 到真实乐队的转变尤为引人注目。[来源-twitter](https://x.com/TheRundownAI/status/2033568236227244451)

### 多模态

- **Cheers 通过解耦 Patch 细节实现统一多模态建模** — Cheers 是一个统一多模态模型，它将 patch 级细节与语义表征解耦，从而解决联合任务中解码方式与视觉表征不匹配的问题。该方法在多模态理解方面稳定了语义表示，并在单一模型内提升图像生成的保真度。[来源-huggingface](https://huggingface.co/papers/2603.12793)

### 开源

- **OpenSWE 支持开放、可扩展的软件工程环境合成** — 训练有能力的软件工程（SWE）智能体需要大规模、可执行、可验证的环境，并具备动态反馈回路以支持迭代代码编辑、测试执行和方案改进。文章指出，现有开源数据集在规模和多样性上都不足，而工业界方案又不透明、学界难以访问。OpenSWE 被宣布为目前最大、完全透明的开放 SWE 环境合成框架，以 daVinci-Env 工作为代表，并托管在 HuggingFace 上。[来源-huggingface](https://huggingface.co/papers/2603.13023)
- **GitNexus：基于浏览器的代码知识图与 Graph RAG** — GitNexus 是一个完全在浏览器端运行的客户端知识图构建工具。只需拖入 GitHub 仓库或 ZIP 文件，即可生成交互式知识图，并配套内置的 Graph RAG Agent 用于代码探索。它将代码库索引为知识图——包括依赖关系、调用链与执行流程——并提供智能工具，以确保 AI agent 在理解代码时不遗漏关键信息。[来源-github](https://github.com/abhigyanpatwari/GitNexus)
- **Cognee：面向 AI Agent 记忆的开源知识引擎** — Cognee 是一款开源知识引擎，使 AI agents 能够以任意格式摄入数据并持续学习，从而提供合适的上下文。它将向量检索、图数据库与认知科学结合起来，使文档可按语义搜索，并通过演化关系连接在一起，从而实现个性化与动态的 AI 记忆。项目支持本地部署、本体对齐、多模态数据和多语言访问，并提供社区插件和文档。[来源-github](https://github.com/topoteretes/cognee)

### AI 工具

- **Weights & Biases 在 iOS 上发布 wandb 移动应用** — Weights & Biases 宣布其 wandb 移动应用在 iOS 正式上线，用户可随时随地监控训练任务。应用提供实时指标、崩溃告警以及 HLS 回放，回应了社区对 AI 实验监控移动化的强烈需求。[来源-twitter](https://x.com/cryptothaler/status/2033691115438657888)

### AI

- **基于 Claude 的工具 Godogen 可从文本生成完整 Godot 游戏** — Godogen 是一条使用 Claude Code 的游戏生成流水线，可从文本提示自动设计游戏架构、生成素材、编写 GDScript，并最终渲染为一个完整可玩的 Godot 4 项目。该项目通过自定义语言规格、API 文档、“怪癖”数据库以及 API 按需加载机制，来应对训练数据稀缺和运行时状态复杂等挑战。项目开源于 htdt/godogen，展示了端到端 AI 辅助游戏开发的可能性。[来源-hackernews](https://github.com/htdt/godogen)

### 具身智能（Embodied AI）

- **从不完美动作数据中学习类人网球运动能力** — 研究者探索使用不完美的人体动作数据来训练会打网球的类人智能体。该方法处理了动作捕捉中的噪声与不一致性，以训练具有运动能力的机器人控制策略，可能借助潜在表征的方法实现。工作展示了将人类动作迁移到具身 AI 表现上的最新进展。[来源-hackernews](https://zzk273.github.io/LATENT/)

### 硬件

- **DGX Station 已可通过 OEM 分销商采购** — 一则 Reddit 帖子称 DGX Station 现已可通过 OEM 分销商获得。帖子链接了 NVIDIA 的官方市场页面以及 DGX Station 规格，指出似乎没有创始人版（founder edition）。作者称其为许多人心目中的“梦想机器”，尽管帖子并未给出价格信息。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvnppg/dgx_station_is_available_via_oem_distributors/)
- **NVIDIA 2026 大会直播：疑似将发布新 Base Model** — 一条 Reddit 投递声称 NVIDIA 2026 大会正在直播，并暗示将发布一款新的基础模型。该帖由用户 /u/last_llm_standing 发布，缺乏技术细节，看起来更像是传闻而非官方公告。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvkxic/nvidia_2026_conference_live_new_base_model_coming/)

## ⚡ 快讯速览

- **Copilot 帮助患者要求正确医疗检查项目** — 一条推文/故事讲述了 Microsoft Copilot 如何帮助一名患者识别出应该进行、但医生二十年来一直未开具的医疗检查。该案例被用来论证 AI 在医疗决策中可以为患者和临床医生提供支持，用现实影响回应外界的质疑。[来源-twitter](https://x.com/mustafasuleyman/status/2033655842919395723)
- **开源项目中使用 Cursor AI：研究发现速度提升但质量受损** — 一篇 arXiv 论文分析了 Cursor AI 在开源项目中的使用情况，指出快速迭代与软件质量之间存在权衡。研究结果表明，以速度为核心的工作流可能会损害可维护性和可靠性，这在 AI 开发工具社区引发了争论。相关 Hacker News 讨论也获得了不少关注。[来源-hackernews](https://arxiv.org/abs/2511.04427)
- **Voygr 推出面向 AI 的地图 API，服务智能体与应用** — Voygr 正在构建一套“AI 就绪”的地图 API，将精准地理位置信息与新闻、事件等最新网络上下文相结合，以解决当前 Maps API 在数据新鲜度上的不足。团队同时推出 Business Validation API，用于验证实体地点在现实世界确实存在，使 AI 应用与智能体能够更可靠地推理真实世界中的地点。项目把地点数据的新鲜度定位为 AI 驱动应用的底层基础设施。[来源-hackernews](https://news.ycombinator.com/item?id=47401042)
- **OpenViking：面向 AI Agents 的开源上下文数据库** — OpenViking 是一款为 AI agents 设计的开源上下文数据库，在类文件系统范式下统一管理记忆、资源和技能，以支持分层、自演化的上下文交付。它旨在解决 agent 开发中上下文碎片化、上下文需求日益增长以及检索困难等问题。项目托管在 GitHub（volcengine/OpenViking），并提供社区渠道以便协作。[来源-github](https://github.com/volcengine/OpenViking)
- **Hermes 表现优于 mimimax2.5highspeed，可将 Telegram 消息写入 SQL 实现搜索** — 一条推文称赞 Hermes 近期表现强劲，即便是与能力较弱的 mimimax2.5highspeed 模型对比也很突出。帖子提到使用 Hermes 将 Telegram 消息写入 SQL 数据库，以支持更深入或可调优的检索能力。[来源-twitter](https://x.com/fbwalker4/status/2033683481415598450)
- **Apideck CLI：比 MCP 所需上下文更少的 AI-Agent 接口** — Apideck 推出了一款基于 CLI 的 AI-agent 接口，据称其上下文窗口消耗显著低于 MCP 服务器。文章将这一方法与 MCP 进行对比，讨论了在构建持久 AI agents 时的潜在取舍、使用场景和性能影响，并将该 CLI 方案定位为希望降低内存与延迟开销的开发者的一种轻量替代方案。[来源-hackernews](https://www.apideck.com/blog/mcp-server-eating-context-window-cli-alternative)
- **“为什么我可能会雇 AI 而不是研究生”** — 一篇观点文章探讨在科研中用 AI 取代部分研究生劳动力的想法。作者讨论了在生产力与成本上的潜在优势，以及依赖 AI 完成复杂学术任务在伦理和实践方面的挑战。[来源-hackernews](https://www.science.org/content/article/why-i-may-hire-ai-instead-graduate-student)
- **AI 工具削弱了学习计算机科学基础的动力** — 一条 Hacker News 帖子指出，强大的 AI 编程助手能快速给出解决方案，这可能会降低人们学习分布式系统、算法等深层 CS 主题的动力。该讨论向资深工程师提问：在这样的背景下，CS 基础为何仍然重要，从而凸显开发效率与基础知识之间的长期张力。[来源-hackernews](https://news.ycombinator.com/item?id=47394291)
- **Sebastian Raschka 发布 LLM Architecture Gallery** — 一篇在 Hacker News 上被大量分享的页面由 Sebastian Raschka 创建，名为 LLM Architecture Gallery，汇总整理了各类大语言模型架构。该页面作为一种资源，对不同的架构思路进行了概览式总结，在 Hacker News 上收获了 547 点赞和 41 条评论。[来源-hackernews](https://sebastianraschka.com/llm-architecture-gallery/)
- **Ask HN：AI 辅助编码在专业实践中的真实体验** — 一则 Ask HN 主题邀请开发者分享在专业环境中使用 AI 工具进行编码的亲身经历。提问包括：使用了哪些工具、哪些有效以及原因、遇到哪些挑战及其解决方式，并要求给出技术栈、项目类型与团队规模等背景信息。目标是在 2026 年 3 月这一时间点，构建一幅关于 AI 辅助开发的现实图景。[来源-hackernews](https://news.ycombinator.com/item?id=47388646)
- **“Spotify 的 AI DJ 愚蠢得惊人”** — Charles Petzold 批评 Spotify 的 AI DJ 在音乐编排上完全缺乏常识，指出其尴尬的曲目衔接和重复且不合口味的推荐。文章认为当前 AI 系统在现实媒体任务中仍难以正确理解上下文与用户意图，并以此例子提醒人们警惕在消费级产品中过度炒作 AI 功能。[来源-hackernews](https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html)
- **Claude 2026 年 3 月使用促销活动** — Claude 官方支持文章宣布了 2026 年 3 月的使用促销活动。内容介绍了用户如何参与以及该促销的相关条款。[来源-hackernews](https://support.claude.com/en/articles/14063676-claude-march-2026-usage-promotion)
- **Claude Code 最佳实践与编排指南** — 这个 GitHub 仓库总结了基于 Claude 的代码与工作流构建的最佳实践模式。内容涵盖命令、子 agent、技能与工作流的结构设计，以及 hooks 与 server 的组织方式，并通过徽章标注最佳实践、实现案例与编排流程。页面还引用了相关材料以及 Boris Cherny 在 X 上的相关讨论串。[来源-github](https://github.com/shanraisshan/claude-code-best-practice)
- **NVIDIA Rubin GPU 峰值仅带来约 2 倍吞吐提升** — 一则在线讨论称，NVIDIA 的 Rubin GPU 在最大吞吐下仅能带来约 2 倍的吞吐提升，尽管 Rubin 拥有更高的显存带宽和 FP4 性能。帖子还提到 Rubin 的更高功耗（B200 约 1000W，对比 R200 约 2300W），并认为其效率仍然存疑，强调应在相同 VRAM 配置下进行“苹果对苹果”的比较。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvmfdd/nvidia_admits_to_only_2x_performance_boost_at_max/)
- **OpenCode UI 默认代理到 app.opencode.ai，称不上真正本地** — 一篇 Reddit 帖子指出，OpenCode 的 serve 命令默认会将所有 Web UI 请求代理到 https://app.opencode.ai，且目前没有选项能让 Web UI 完全在本地提供服务。也就是说浏览器端 UI 并非真正意义上的本地部署。GitHub 上已有多条 PR 和 Issue 记录并讨论了这一行为。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rv690j/opencode_concerns_not_truely_local/)
- **独立开发者发布在 7GB VRAM 内运行的 SOTA Text-To-Sample Generator** — 一位 Reddit 用户宣布发布一款新的 SOTA Text-To-Sample Generator，并声称其可在 7GB VRAM 内运行（8GB 则更宽裕），主打内存效率。帖子将该项目归功于 /u/RoyalCities，并附上了发行链接。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rvnflv/so_i_was_the_guy_from_last_week_working_on_that/)
- **DLSS 5 呈现极其清晰的画面，“奥巴马梗图”在社交媒体疯传** — DLSS 5 作为一项 AI 驱动的超分辨率技术，被描述为能够呈现非常清晰的视觉效果。一条推文还提到了一张带有奥巴马形象的梗图，暗示高画质在社交媒体中格外显眼。该现象也凸显了 AI 图形技术如何驱动关注度与分享传播。[来源-twitter](https://x.com/scaling01/status/2033629340655567212)
- **Claude Code 让一位 60 岁开发者对编码的热情减弱** — 一名接近 60 岁的 Hacker News 用户分享说，Claude Code 等 AI 工具让他对编程的热情不如从前，在 AI 出现之前他更享受“亲手写代码”的过程。他认为 AI 虽然带来了新的“目的地”，却缩短了有意义的“旅程”，从而改变了开发者的动机。这篇帖子折射出更广泛的担忧：AI 对编程这门“手艺”以及个人成就感的影响。[来源-hackernews](https://news.ycombinator.com/item?id=47386813)
- **机器学习可视化入门（2015）** — 这是一篇 2015 年发布在 R2D3 上的交互式可视化机器学习入门教程，通过图形化方式讲解基础概念和算法。内容涵盖监督学习、决策边界、梯度下降和神经网络等主题，以通俗易懂的形式呈现。该资源在 Hacker News 上获得了热烈反响。[来源-hackernews](https://r2d3.us/visual-intro-to-machine-learning-part-1/)
- **VC 融资推介押注“硬件对齐模型架构”这一流行词** — Andrew N. Carr 在推文中调侃道，创业公司在向 VC 做 AI 项目路演时，最好在材料中加入“hardware aligned model architecture”这一表述，以搭上当前的 AI 热点。他借此强调“硬件感知的模型设计”正成为募资对话中的热门话题，也反映出流行语对投资人兴趣的影响力。[来源-twitter](https://x.com/andrew_n_carr/status/2033683891836309626)

---

*由 AI News Agent 生成 | 2026-03-16*