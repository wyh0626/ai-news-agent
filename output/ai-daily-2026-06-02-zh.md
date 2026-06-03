---
title: "AI 日报 — 2026-06-02"
description: "MAI发布模型，ClaudeCode升级，OpenAI接入Codex至Sites"
lang: "zh"
pairSlug: "ai-daily-2026-06-02"
---

# AI 日报 — 2026-06-02

> 涵盖 32 条 AI 新闻

## 🔥 今日焦点

### 1. MAI 发布由 MAI-Thinking-1 领衔的七款全新世界级模型
MAI 一口气发布七款全新世界级模型，其中旗舰是拥有 350 亿激活参数、支持 256K 上下文窗口的 MoE 模型 MAI-Thinking-1，并针对 MAIA 200 芯片做了优化，相比 GB200 实现每美元性能提升 30%、每瓦性能提升 1.4 倍。这一产品阵容表明 MAI 正在打造面向硬件深度优化的广泛 AI 产品组合，目标是在大规模场景中提升效率，并扩大其在模型生态中的竞争版图。 [来源-x](https://x.com/mustafasuleyman/status/2061880164498428188)

### 2. Claude Code 推出 Workflows，为自 Skills 以来最大升级
Claude Code 新增 Workflows 功能，这是自 Skills 和子代理以来最重大的升级，使其能够对非技术任务和端到端流程进行自动化处理。此举显著拓宽了 Claude Code 在纯代码开发之外的实际应用场景，或将推动企业级采用，但也会引发对其可靠性与成本的更多审视。 [来源-x](https://x.com/trq212/status/2061907538741006796)

### 3. OpenAI 在 Codex 中上线 Sites，支持端到端软件开发
OpenAI 在 Codex 中引入 Sites，帮助不同技术水平的用户构建端到端的软件应用。Sites 可以部署到一个 URL，且仅在所属工作区内可见，内置用户认证、静态文件托管和动态数据存储，并将先面向商务版和企业版团队小范围预览，之后再在整个工作区全面开放。 [来源-x](https://x.com/TheRohanVarma/status/2061872164442403139)

## 📰 重点报道

### LLM

- **MAI 发布由 MAI-Thinking-1 领衔的七款全新世界级模型** — MAI 推出一套围绕 350 亿参数、支持 256K 上下文窗口的 MoE 模型构建的多模型阵容，并针对硬件进行了深度优化；效率提升是其关键差异点。 [来源-x](https://x.com/mustafasuleyman/status/2061880164498428188)
- **Claude Code 推出 Workflows，为自 Skills 以来最大升级** — Workflows 扩展了 Claude Code 超越既有 Skills 的自动化能力，使其能够执行完整的端到端任务流程。 [来源-x](https://x.com/trq212/status/2061907538741006796)
- **OpenAI 在 Codex 中上线 Sites，支持端到端软件开发** — 通过 Codex Sites 实现端到端软件创建，支持仅工作区可见的 URL、身份认证以及数据托管；目前向商务版与企业版提供预览访问。 [来源-x](https://x.com/TheRohanVarma/status/2061872164442403139)
- **Anthropic 扩大 Project Glasswing，延长 Claude Mythos 预览期** — Glasswing 的访问范围扩展到超过 15 个国家的约 150 家机构，进一步扩大了 Mythos 预览版本的可用范围。 [来源-x](https://x.com/AnthropicAI/status/2061796327986454883)
- **Microsoft 在 Build 上宣布七款新 AI 模型** — 一组覆盖推理、编程、图像处理、转写和语音等领域的七个模型，被设计为一个协同工作的工具家族。 [来源-x](https://x.com/MicrosoftAI/status/2061887500541366489)
- **多智能体 RL 改进 LLM 工作流：共享策略 vs 隔离策略** — 比较 Shared-Policy 与 Isolated-Policy 强化学习在端到端 LLM 工作流中的表现，强调稳定性与不同方案的权衡。 [来源-huggingface](https://huggingface.co/papers/2605.24202)
- **75M 参数 KeyLM 在 IFEval 上击败 135M Instruct 模型** — 一个使用 180 亿 tokens 训练的 7500 万参数小模型，在指令跟随基准上超越了 1.35 亿参数模型，凸显小模型在效率与性能上的潜力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuyb8s/i_trained_a_75m_parameter_llm_from_scratch_on_18b/)
- **TASTE 任务合成提升智能体基准覆盖度** — 提出通过 Task Synthesis（任务合成）拓展超越自然语言到工具映射的基准覆盖度，以应对现有基准饱和与成本过高的问题。 [来源-huggingface](https://huggingface.co/papers/2605.28556)
- **Domino：在推测生成中解耦因果建模与草稿生成** — Domino 在推测解码中将草稿生成与因果建模分离，以提升整体效率，并在草稿质量与生成成本之间寻找更优平衡。 [来源-huggingface](https://huggingface.co/papers/2605.29707)

## ⚡ 快讯速览

- **线性集成可抹除 LLM 水印** — 提出一类方法可通过线性集成抹除 LLM 输出中的水印，凸显潜在滥用与安全风险。 [来源-huggingface](https://huggingface.co/papers/2605.30501)
- **TradingAgents v0.2.5 新增情绪分析与双区域支持** — 为量化/交易智能体新增基于事实的情绪分析能力，并支持双区域部署。 [来源-github](https://github.com/TauricResearch/TradingAgents)
- **《Machine Learning for Trading》第二版——GitHub 代码** — 在 GitHub 上发布《Machine Learning for Trading》第二版配套代码。 [来源-github](https://github.com/stefan-jansen/machine-learning-for-trading)
- **在多智能体编排器中用本地 Qwen3.6-27B 替换 Claude** — 有用户在多智能体编排系统中用本地运行的 Qwen3.6-27B 替代 Claude，以测试本地 LLM 的可行性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tunmam/replaced_claude_with_local_qwen3627b_in_my/)
- **在 6GB RTX 4050 上对 20 个小型 LLM 做基准测试** — 在一块 6GB 显存的 RTX 4050 上对 20 款小型 LLM 进行并列基准测试对比。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuvs6l/benchmarks_of_20_small_llms_on_a_6gb_rtx_4050/)
- **Gemma 4 E4B 搭配 LiteRT 文本生成提速约 2.4 倍** — 使用 LiteRT 引擎的 Gemma 4 E4B 在文本生成任务中可获得约 2.4 倍速度提升。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuygn6/using_gemma_4_e4b_with_the_litert_engine_24x/)
- **1-bit 与 Ternary Bonsai Image 4B：面向本地设备的微型扩散模型** — 提供轻量级的 1-bit 与三值量化 Bonsai Image 4B 扩散模型，方便在本地设备上运行。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tusnh5/1bit_bonsai_image_4b_and_ternary_bonsai_image_4b/)
- **简单编码基准：Step 3.7 对比 Qwen 3.5/3.6** — 一份快速基准对比 Step 3.7 与 Qwen 3.5/3.6 在编程任务上的表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuxspu/a_simple_coding_benchmark_step_37_vs_qwen_35/)
- **Claude Opus 4.8 Max 质疑自身内容声明** — Claude Opus 4.8 对自己生成内容中的部分声明提出质疑，引发讨论。 [来源-x](https://x.com/davidad/status/2061858258046898518)
- **Natol Lambert 在 Ai2 工作 2.5 年后离职** — 在 Ai2 工作多年的研究员 Natol Lambert 宣布在任职约两年半后离开。 [来源-x](https://x.com/natolambert/status/2061813361848029631)
- **Perplexity Computer 推出混合式智能体推理** — Perplexity 为其智能体引入混合式 agentic inference 推理模式。 [来源-x](https://x.com/perplexity_ai/status/2061861293569765847)
- **OpenCode 的一个分支通过 Chipotle 未加固的 AI 端点路由请求** — 安全问题曝光：某 OpenCode 分支的请求会通过 Chipotle 未加安全防护的 AI 接口路由。 [来源-x](https://x.com/thdxr/status/2061828564773740999)
- **Hermes WebUI 为 Hermes Agent 提供 Web 界面** — Hermes WebUI 项目为 Hermes Agent 提供基于浏览器的可视化交互界面。 [来源-github](https://github.com/nesquena/hermes-webui)
- **Minimax M3 似乎没有政治审查** — 有用户声称 Minimax M3 在内容生成中似乎不进行政治相关审查。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuv1sv/minimax_m3_appears_to_have_no_political_censorship/)
- **以 200 英镑在游戏 PC 中插上一块数据中心 GPU** — 有玩家以 200 英镑购入数据中心级 GPU，并成功安装到家用游戏 PC 中。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuxy5f/i_put_a_datacenter_gpu_in_my_gaming_pc_for_200/)
- **你为自己的智能体使用什么记忆系统？** — 社区讨论不同智能体的记忆架构与实现方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tv4xi0/what_memory_system_are_you_using_for_your_agents/)
- **哪家 Web 搜索 API 为本地 RAG 提供最干净的 Markdown？** — 围绕哪种搜索 API 能为本地 RAG 场景返回更干净 Markdown 结果展开讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tv6quu/which_web_search_api_gives_the_cleanest_markdown/)
- **LLaMA.cpp 增加带推理等级的 Thinking 模式开关** — LLaMA.cpp 现已支持 Thinking 模式切换，并能调整不同等级的推理强度。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1turt87/ui_add_thinking_mode_toggle_with_reasoning_effort/)
- **Ollie：号称“世界首个能管理家庭生活”的 AI 家庭助手** — 发布 Ollie，一个定位为家庭场景、帮助管理日常生活的 AI 助手。 [来源-x](https://x.com/blennon_/status/2061868938443550842)
- **Harness-1：面向 RL 搜索智能体的状态外化 Harness** — Harness-1 为强化学习搜索智能体引入状态外化能力。 [来源-huggingface](https://huggingface.co/papers/2606.02373)
- **StepFun 3.5 MTP 对 Llama.cpp 的 PR** — 针对 Llama.cpp 提交集成 StepFun 3.5 MTP 的 Pull Request。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tuv0lv/stepfun_35_mtp_by_pwilkin_pull_request_23274/)
- **想象 80 年代就有 LLM，并启用 HLS 播放** — 一种怀旧式的概念设想：为 LLM 引入类似高层综合（HLS）的“播放”模式。 [来源-x](https://x.com/beffjezos/status/2061699865365934215)

---

*由 AI News Agent 生成 | 2026-06-02*