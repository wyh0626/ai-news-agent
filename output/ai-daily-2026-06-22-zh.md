---
title: "AI 日报 — 2026-06-22"
description: "扩展修补，新增模型与工具；Gemini以GA为主接口，GLM5.2开放权重促开源"
lang: "zh"
pairSlug: "ai-daily-2026-06-22"
---

# AI 日报 — 2026-06-22

> 共收录 26 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI Daybreak 通过新模型与工具扩展补丁能力

OpenAI 宣布通过 Daybreak 加速安全漏洞修复，推出 Codex Security 插件和 GPT-5.5-Cyber，用于在主流软件中发现、验证并修补关键漏洞。该项目重点覆盖浏览器、内核和操作系统，对 cURL、Go、Python、Sigstore 和 pyca/cryptography 等进行修补，并发起 Patch the Planet 与 Cyber Partner Program 等计划，以使开源软件的漏洞修补更加大众化、可及化。 [来源-twitter](https://x.com/gdb/status/2069112120206332130)

### 2. Interactions API 正式 GA，成为 Gemini 模型与 Agent 的主要接口

Google 宣布 Interactions API 正式进入 GA 阶段，并成为 Gemini 模型与智能体的主要调用接口。本次发布提供稳定的 schema，并加入开发者强烈要求的特性，包括 Managed Agents、后台执行、扩展工具支持、多模态生成，以及即将到来的 Gemini Omni 支持。 [来源-twitter](https://x.com/Google/status/2069108942102310957)

### 3. GLM 5.2 开放权重用于 Autoresearch，强化开源生态

GLM 5.2 被称为首个在 autoresearch 流水线中测试的开放权重模型，并被证明能够胜任真实科研任务。本次发布在 Fable 5 受限的大环境下，为开源研究提供选择，并展示了在两台 8×H100 节点上，借助 SkyRL 在 Harbor 代码竞赛中进行异步 RL 训练的流程，包括运行追踪以及吞吐量/奖励对比等。 [来源-twitter](https://x.com/askalphaxiv/status/2069074178829901974)

## 📰 重点报道

### LLM

- **Ling and Ring 2.6 技术报告：万亿规模下高效的 Agentic AI** — Ling and Ring 2.6 的技术报告宣称在万亿参数级别实现高效且即时的 agentic intelligence。发布重点介绍了基础模型 Ling-2.6-1T 和 Ling-2.6-flash（100B），并讨论如何在中等配置 GPU 以及纯 CPU 环境下实现更快速推理，同时推出 Ling-mini-2.0 系列变体。Reddit 讨论串提到其在 8GB 显存和 CPU 上的惊人 tokens/s 表现，显示开源 AI 正在快速进步。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ucih9e/ling_and_ring_26_technical_report_efficient_and/)
- **封闭模型之上的闭源 orchestrator 引发主权担忧** — 一篇批评指出，将闭源 orchestrator 堆叠在闭源模型之上，会剥夺用户对模型选择与使用方式的控制权。文中将 Fugu 视作按轮次路由模型的系统，指出其基准测试提升有限且可能带来成本影响，并质疑围绕前沿模型（Model A/B/C）对比透明度以及对新增 LLM 的兼容性。 [来源-twitter](https://x.com/eliebakouch/status/2068939729811468503)
- **F 轮融资估值 130 亿美元；推理业务同比增长 20 倍** — 某初创公司完成 F 轮融资，估值达到 130 亿美元，并称过去一年推理业务增长了 20 倍。公司认为，客户需求的驱动力在于向“自有智能层”永久转变——通过后训练（post-training）的开源模型实现；其正在与客户合作，提供权重、训练配方以及持续学习所需工具。Abridge、Cursor、Decagon、Harvey、HubSpot、Lovable、Notion、OpenEvidence 和 Parallel 等客户，体现了企业自持 AI 的趋势。 [来源-twitter](https://x.com/amiruci/status/2069095112186196175)
- **Anthropic 禁止非公民使用 Fable 5；Mythos 6 可能不受限** — 有说法称，Anthropic 因禁令而禁止非本国公民研究者使用 Mythos/Fable 5，同时却允许开发更新的模型如 Mythos 6 或 Fable 6。若消息属实，这一政策在新模型持续具备强大能力的情况下，合理性可能会受到质疑。 [来源-twitter](https://x.com/Yuchenj_UW/status/2069101916387459390)
- **PerceptionDLM 让多模态 Diffusion LLM 实现并行区域感知** — PerceptionDLM 提出一种基于扩散的多模态语言模型，专门针对多图像区域的高效并行感知，旨在解决自回归式图像描述的瓶颈。该模型构建在 PerceptionDLM-Base 之上，据称达成多个任务的 SOTA 表现，标志着多模态 AI 在区域级感知能力上的提升。该工作发布在 HuggingFace，体现了多模态 LLM 研究中的开放科学贡献。 [来源-huggingface](https://huggingface.co/papers/2606.19534)
- **Apertus 推出面向 Sovereign AI 的开放基础模型** — Apertus 宣布推出一款为 Sovereign AI 场景设计的开放基础模型。该项目旨在为组织提供对 AI 部署的自治与治理能力，提供不依赖单一厂商的基础层。此消息在 Hacker News 上引发了广泛关注。 [来源-hackernews](https://apertvs.ai/)
- **同一模型、同一提示，测试四种 AI Agent** — 使用同一个自托管 Qwen3.6-27B 模型、llama.cpp 和完全相同的提示，对四种 agent 框架（pi、opencode、hermes、qwen code）进行对比。每个 agent 的任务都是生成自包含的 HTML/JS 2D 太阳系模拟器，包含脚本化轨道、对用户发射彗星的引力、响应式画布；行星与太阳各自独立绕行，引力与体积成正比，行星间不相互作用。该实验凸显了即便模型和提示完全一致，Agent 脚手架也能显著改变输出结果。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ucmndc/same_model_same_prompt_4_different_agents/)
- **NEX-N2-mini：没有帕累托前沿，我就是帕累托** — 一则 Reddit 帖子声称，NEX-N2-mini MoE 微调模型以更少 tokens 达到 3.5/3.6 级别的推理能力。作者宣称不存在传统意义上的帕累托前沿，并认为该模型已达到类似帕累托的性能，同时附上基准测试和 HuggingFace 页面供验证。讨论凸显了开源模型的潜力，并展示了与其他模型的性能对比图。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ucnorl/nexn2mini_there_is_no_pareto_frontier_i_am_pareto/)
- **Gemma 4 QAT 31B 通过 KV Cache 量化获得提升** — 根据 Reddit 用户 /u/justicecurcian 的帖子，对 Gemma 4 31B 进行 KV cache 量化后，基准表现反而更好。作者指出，与此前基准相比，该方案提升了性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ucgrxh/gemma_4_qat_31b_responds_better_to_kv_cache/)

### RL

- **TMax 发布开放 RL 数据集与 Terminal 模型** — TMax 推出两个开放组件：TMax-15k，一个包含 14,600 个 RL 环境的数据集，可显式控制难度和多样性；以及一套仅基于结果（outcome-only）的 RL 训练配方，可将 2B 至 27B 的开放模型训练为 terminal agent。在 Terminal Bench 2.0 中，TMax-9B 得分 27.2%，是 10B 以下最强的开放权重模型，超越了 32B 级别的 open-terminal agent，并接近 Claude Haiku 4.5。将规模扩展到 27B 后，得分达 42.7%，逼近 Kimi K2.5 的 43.2%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uco0aa/tmax_a_simple_recipe_for_terminal_agents/)

### 行业动态

- **Compile 大会主题演讲披露与 SpaceX 一起训练新模型** — Cursor AI 在 Compile 大会的主题演讲中分享了三项重要更新，其中包括与 SpaceX 合作训练新模型的细节。帖子强调了与 SpaceX 的合作关系以及正在进行的 AI 模型训练项目。 [来源-twitter](https://x.com/cursor_ai/status/2069149296436330776)

### 开源项目

- **DeusData 发布用于代码库智能的 Memory MCP** — DeusData 推出 codebase-memory-mcp，这是一款高性能代码智能 MCP 服务器，可将代码库索引到持久化知识图谱中。该工具支持 158 种语言，查询延迟可低至毫秒级，并可在约 3 分钟内完成 Linux 内核的索引，同时实现零依赖，并通过单一静态二进制支持 macOS、Linux 与 Windows。其基于 tree-sitter AST 分析和 Hybrid LSP 语义类型推断，映射函数、类、调用链、HTTP 路由和跨服务链接，并预置 14 个 MCP 工具，可即插即用地支持 11 种编码 Agent。 [来源-github](https://github.com/DeusData/codebase-memory-mcp)
- **Recall：为 Claude Code 提供本地项目记忆** — Recall 是一款开源工具，可为 Claude Code 项目提供本地记忆功能，使代码片段和上下文信息的存储与检索都在本地完成。该项目托管在 GitHub（raiyanyahya/recall），并以 Show HN 形式登上 Hacker News，获得不少互动。其目标是在 Claude Code 工作流中，通过本地化上下文来提升隐私与效率。 [来源-hackernews](https://github.com/raiyanyahya/recall)

### 开源 AI

- **Top-N-Sigma：移除无条件 softmax+sort 加速 LLaMA.cpp** — 一则 Pull Request 移除了在 Top-N-Sigma 采样器末尾、在接上 Dist 时仍无条件执行的 softmax+sort 步骤，从而避免无效计算。根据测试，在 M3 Max MacBook Pro 上，该改动让 google_gemma-4-E4B-it-Q8_0 的速度从约 30 tokens/s 提升到约 45 tokens/s，每 token 时间缩短约 10 ms。提交者同时提醒，这可能影响串联采样器的 API 合约，并呼吁对不同后端和模型进行更广泛验证。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ucqs1k/topnsigma_remove_unconditional_softmaxsort_by/)

### AI 工具

- **Sakana Fugu 发布单一 API 的多智能体编排系统** — Sakana AI Labs 发布 Sakana Fugu，一个通过单一模型 API 即可访问的完整多智能体编排系统。据称 Fugu Ultra 的性能可与 Fable 和 Mythos 等前沿模型相当，同时规避出口管制风险。公司邀请用户在 sakana.ai/fugu 上进行试用。 [来源-twitter](https://x.com/SakanaAILabs/status/2068861630327443966)

## ⚡ 快讯速览

- **奥运金牌得主 Alysa Liu 将加入 OpenAI** — 一则推文称，奥运金牌得主 Alysa Liu 将于下周加入 OpenAI，消息来自 Alisa Liu 的个人账号。帖子提到一段艰难但有收获的求职过程，并附上其个人博客，分享经验与教训，希望帮助他人求职。 [来源-twitter](https://x.com/yifever/status/2068849358888677718)
- **Hermes Agent 将 GUI 控制扩展到 Windows 与 Linux** — Hermes Agent 现已支持在 Windows 和 Linux 上使用任意模型控制桌面 GUI 应用，扩展了此前对 macOS 的支持。该更新使用户可通过 TryCua 在 Windows 和 Linux 上实现跨平台电脑操作，进一步拓展 Hermes 的自动化能力。 [来源-twitter](https://x.com/Teknium/status/2069126072504074356)
- **Google DeepMind 与 A24 启动 AI 研究合作** — Google DeepMind 宣布与电影制片厂 A24 开展研究合作，旨在确保未来的 AI 工具由实际使用它们的创作者共同塑造。此次合作希望让工具开发更好地对齐创意工作者与整个创意行业的实际需求。 [来源-twitter](https://x.com/GoogleDeepMind/status/2069066675895337405)
- **微调 Qwen 3:0.6B LLM 进行问题分类** — 一篇文章介绍了通过微调本地 LLM（Qwen 3:0.6B）来对问题进行分类，并取得良好效果的方法。该实践强调了离线/隐私友好型 AI 的优势，以及轻量级、本地运行模型的潜力，并展示了早期正向结果。 [来源-hackernews](https://www.teachmecoolstuff.com/viewarticle/fine-tuning-a-local-llm-to-categorize-questions)
- **我取消了法语家教，自己做了更好的 LLM 工具** — 作者讲述了如何放弃传统法语家教课程，转而构建一款个性化的、基于 LLM 的辅导工具，并认为其效果更佳。文章探讨了自动化学习系统如何提供可扩展的练习与反馈机制，并在 Hacker News 上获得关注（54 分，24 条评论）。 [来源-hackernews](https://alshe.substack.com/p/i-canceled-my-french-tutor-and-built)
- **欧盟 DDR5 价格下跌；德荷价差扩大利好 LLM 搭建者** — 过去 25 天中，DDR5 内存价格在四个欧盟国家（德国、荷兰、西班牙、比利时）持续下跌，多款套条录得两位数降幅。德国在许多入门套条上仍比荷兰和比利时便宜 10–20%，使 DDR5-6000 2×16GB 成为高性价比 LLM 推理的新甜点档。面向欧盟的价格跟踪网站 pricesquirrel.com 已上线，但数据仍处于测试阶段。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ucixz9/been_tracking_eu_ddr5_data_for_25_days_prices_are/)
- **质疑 Claude Code Extended Thinking 输出文本的真实性** — 一篇批评文章认为，Claude Code 的 Extended Thinking 功能展示的文本并不真实可信。作者讨论了这些输出究竟是实际推理过程，还是经过“摆拍”的内容，并链接到 Patrick McCanna 的原帖和 Hacker News 上的相关讨论。 [来源-hackernews](https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/)
- **本地 LLM 专用硬件何时会变得可负担？** — 一则 Reddit 帖子询问，面向消费者、专门用于本地 LLM 推理的专用硬件是否会在不久的将来到达可负担价位。帖子以 qwen 27b dense 为典型模型，讨论当前成本门槛、潜在的中国厂商参与，以及在制造、内存和软件生态方面的挑战，并征求大家对时间表与市场影响的看法。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uce2pz/do_you_think_dedicated_hardware_for_running_local/)

---

*由 AI News Agent 生成 | 2026-06-22*