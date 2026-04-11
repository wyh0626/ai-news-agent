---
title: "AI 日报 — 2026-04-10"
description: "AI代理在Word可起草编辑并扩展感知，推出判官式DevAI基准。"
lang: "zh"
pairSlug: "ai-daily-2026-04-10"
---

# AI 日报 — 2026-04-10

> 共收录 31 条 AI 新闻

## 🔥 今日焦点

### 1. Claude for Word Beta 版在 Word 侧边栏中支持 AI 撰写与编辑

Anthropic 的 Claude for Word 已进入测试版，支持在 Word 侧边栏中直接起草、编辑和修改文档。该工具会保留文档格式，并以“修订模式”展示修改记录，目前面向 Team 和 Enterprise 计划开放。 [来源-twitter](https://x.com/claudeai/status/2042670341915295865)

### 2. MMX-CLI 为智能体扩展七种全新“感官”

MMX 发布 MMX-CLI，称其为首个专为 AI Agents 而非人类构建的基础设施。它通过 MiniMax 的全模态技术栈引入七种模态——image、video、voice、music、vision、search 和 conversation，使智能体具备新的读、思、写能力。该工具一条命令即可运行（mmxAgent-native I/O），无需额外粘合代码，兼容现有 Token Plan，并通过两行配置即可为智能体接入语音功能；详细信息见 GitHub 仓库。 [来源-twitter](https://x.com/MiniMax_AI/status/2042641521653256234)

### 3. Agent-as-a-Judge 搭配 DevAI 基准，首秀用于评估 AI Agents

研究者发布 Agent-as-a-Judge，这是一个概念验证框架，用“类人、逐步”的流程来评估 AI 智能体，并声称可显著降低评估成本。配套的 DevAI 基准包含 55 个自动化 AI 开发任务和 365 条需求，设计目标是更贴近人类评测。早期结果表明，Agent-as-a-Judge 在效果上优于 LLM-as-a-Judge，并能很好对齐人类判断，标志着 AI 评估方法的重要进展。 [来源-twitter](https://x.com/giffmana/status/2042481526328148282)

## 📰 重点报道

### LLM

- **Mythos 零日漏洞被 GPT5.4 和 Opus 复现** — 一篇帖子称，使用 GPT5.4 和 Opus 成功复现了 Mythos 的研究结果，并表示将在下周初给出完整说明。作者称其在过去三周内自动发现了 Linux 内核零日漏洞，指出 Mythos 在发现潜在代码问题方面能力很强，且“令人害怕”的阈值在更早就已达到。他们将此框架为对 Anthropic IPO 计划的炒作，同时强调这并非一种全新的能力。 [来源-twitter](https://x.com/kannthu1/status/2042695741844619502)
- **Kronos：面向金融市场的开源基础模型** — Kronos 是一个开源、仅解码式的基础模型，专为金融市场“语言”而设计，以 K 线（OHLCV）序列为中心，并在来自 45 个以上全球交易所的数据上训练。它提出一个两阶段框架及专用 tokenizer，将连续 OHLCV 数据量化为分层离散 token，以应对高度噪声的市场信号。项目已发布 arXiv 预印本和微调脚本，并宣布论文被 AAAI 2026 接收。 [来源-github](https://github.com/shiyu-coder/Kronos)
- **GLM 5.1 登顶开源模型 Code Arena 排行** — GLM 5.1 在开源代码生成模型中登上 Code Arena 排行榜首位。Code Arena 基准用于衡量开源 LLM 的编码表现，而 GLM 5.1 的领先表明其在开源代码任务上的强大能力。本条新闻来自 Reddit 帖子。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shq4ty/glm_51_tops_the_code_arena_rankings_for_open/)
- **NousResearch 发布用于 Claude 后台脚本的 Monitor 工具** — NousResearch 推出 Monitor 工具，允许 Claude 创建后台脚本，在需要时唤醒 agent，从而无需持续轮询。该工具旨在节省 token，并支持通过脚本跟踪日志、轮询 PR 等操作，同时可以在同一会话中处理其他任务。更新还强调，相比中心化竞争者，开源生态在速度和创新上更具优势。 [来源-twitter](https://x.com/Teknium/status/2042396576245825543)
- **Anthropic 领跑 AI 竞赛，OpenAI 被指进展缓慢** — 一则社交帖称 OpenAI 最近“几乎没有在发新东西”，而 Anthropic 看上去是唯一有竞争力的玩家。帖子把 Meta、Google、Grok、DeepSeek 和 Apple 描绘成在 AI 竞赛中落后或“几乎没参加”的角色。 [来源-twitter](https://x.com/theo/status/2042456180694663540)
- **重新审视推理 SFT 的泛化：优化、数据与能力** — 一项新分析质疑“监督微调只会记忆、强化学习才会泛化”的传统看法，认为推理 SFT 的跨领域泛化取决于优化动态、训练数据和基础模型能力。作者指出，部分失败其实是“欠优化”伪影，跨领域性能在初期可能会下降，之后再恢复。这一重构视角改变了我们评估推理 SFT 及其真实世界泛化潜力的方式。 [来源-huggingface](https://huggingface.co/papers/2604.06628)
- **ClawBench：用 153 个日常任务评测 AI Agents** — ClawBench 提出一个评估框架，用 153 个简单任务来测试 AI 智能体，覆盖 15 个类别下的 144 个在线平台，如购物、预约、求职申请等。其目标是衡量 AI Agents 是否能自动化邮箱以外的日常线上活动，为真实世界自动化提供一个实用基准。该框架已发布在 HuggingFace。 [来源-huggingface](https://huggingface.co/papers/2604.08523)
- **过度细节会伤害小模型；“角色 + 约束”表现最佳** — 一项实验在 8 个模型上测试常见的提示词（prompting）建议，其中包括在 M2 96GB 和 RTX 5070 Ti 上通过 Ollama 运行的 6 个本地模型，以及 2 个前沿 API（GPT-4.1-mini 和 Claude Haiku 4.5）。结果发现，额外细节会损害小模型表现，“角色 + 约束”是最佳平衡点，而示例或边界情况在参数低于 3B 时可能会降低输出质量；更大的模型则不受影响。这次实验的 API 总成本为 0.03 美元。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1si110t/764_calls_across_8_models_too_much_detail_kills/)
- **TurboQuant + TriAttention 让 Llama.cpp KV Cache 减少约 6.8 倍** — 一篇 Reddit 帖子称，在 AMD/HIP 上的 llama.cpp 中，同时使用 TurboQuant KV 缓存压缩和 TriAttention 剪枝，可获得约 6.8× 的 KV 缓存总体缩减（其中 TurboQuant 约 5.1×，TriAttention 约 1.33×）。在 131K 上下文长度下，f16 KV 需要 8.2 GiB，而组合方案可降至约 1.2 GiB；TurboQuant 在 GSM8K 上对 1319 道题达到 72.0%，在 NIAH 上在 64K 以内取得 28/28，工具调用测试为 26/26，不过 NIAH 结果仅基于 TurboQuant，且 TriAttention 在检索任务中的说法尚未被验证。TriAttention 的灵感来自 NVIDIA/MIT 的一篇论文，作者也提醒端到端检索性能的结论仍未验证；速度开销约为 1–2%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shzjwx/turboquant_triattention_chip_68_total_kv_cache/)
- **斯坦福发布 Meta-Harness：可自我改进的 LLM Harness** — 斯坦福研究者提出 Meta-Harness，这是一个外环系统，能对 LLM harness 代码进行搜索，自动纠正智能体错误，并在使用更少上下文的同时提升性能。其通过一个具 agentic 能力的 proposer 检查先前候选的源码、得分和执行轨迹，以指导改进。在在线文本分类任务中，Meta-Harness 在使用 1/4 上下文 token 的前提下，比一款最先进的上下文管理系统高出 7.7 个百分点。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shyczh/stanford_self_improving_metaharness/)
- **GGUF 工具套件支持自定义高质量量化模型** — 新发布的 GGUF-Tool-Suite 搭配文档与 Web UI，可帮助用户为 ik_llama.cpp 和 llama.cpp 基准测试并生成 GGUF 量化模型，既支持命令行也支持 Web 界面。该套件声称可生成比其他版本更高质量的 GGUF，并已被多位用户采用；针对 Kimi-K2.5 和 GLM-5.1 的基准测试即将发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shysbc/tool_for_creating_your_own_highquality_gguf/)
- **Gemma 4 vs Qwen3.5：量化本地 LLM 在 Go 语言编码上的对比** — Reddit 用户 m3thos 对 Gemma 4 和 Qwen3.5 进行了对比测试，在一台配置较低的 framework13 笔记本上运行量化本地 LLM。实验聚焦参数量低于 40B 并采用 MoE 量化的模型，指出 GPT-OSS-20B 在这些约束下表现出乎意料地好。帖子强调，在性能有限的硬件上，开源量化 LLM 依然可以胜任编码任务。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shzerk/gemma_4_vs_qwen35_benchmarking_quantized_local/)
- **基于 9B Qwen 的 LoRA 实现自主数据分析** — 一项开源工作展示了在 Qwen3.5-9B 基础模型上训练的 LoRA，可执行端到端数据分析。该方法使用多步 trace 数据集，让模型在一个循环中完成规划、编码、调试、可视化和总结，直至任务完成。作者声称，这个 LoRA 能在无人工干预的情况下完成 89% 的工作流，而基础模型在这些任务上的失败率则为 100%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shlk5v/model_release_i_trained_a_9b_model_to_be_agentic/)

### AI Research

- **新加坡国立大学发布 DMax：面向 dLLM 的激进并行解码** — 新加坡国立大学的研究者提出 DMax，这是一种新的 diffusion language model（扩散语言模型）范式，把解码过程视为渐进式自我改进，以缓解并行解码中的错误累积。该方法引入 On-Policy Uniform Training，将“掩码式 dLLM”和“均匀式 dLLM”统一起来，并通过 Soft Parallel Decoding 对中间状态进行插值，从而在保持生成质量的前提下加速解码。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sht2yo/national_university_of_singapore_presents_dmax_a/)

### LLMs

- **Karpathy：OpenAI 语音模式使用“更旧、更弱”的模型** — Andrej Karpathy 指出，OpenAI 的语音模式运行在一个更旧、更弱的模型上，这可能误导用户，以为 AI 比实际更聪明。他强调，很多人的印象来自免费层或过时版本，并不能代表今年最先进的 agentic 模型（如 Codex 和 Claude Code）的真实能力。 [来源-twitter](https://x.com/simonw/status/2042611602726539283)

### Embodied AI

- **HY-Embodied-0.5 推出面向真实世界智能体的 Embodied 基础模型** — HY-Embodied-0.5 发布一系列专为真实世界 embodied agents 设计的基础模型。它们旨在弥合通用视觉语言模型与 embodied 需求之间的差距，通过增强空间与时间上的视觉感知能力，以及面向预测、交互与规划的高级 embodied 推理。HY-Embodied-0.5 系列包含两个主要版本。 [来源-huggingface](https://huggingface.co/papers/2604.07430)

### Open Source

- **OpenBMB VoxCPM2 推出无 tokenizer 的多语种 TTS** — OpenBMB 发布 VoxCPM2，这是一款参数量为 2B、无 tokenizer 的 TTS 模型，在超过 200 万小时的多语言数据上训练。它支持 30 种语言、端到端扩散自回归合成、声音设计以及可控的音色克隆，并以 MiniCPM-4 为基础实现 48kHz 录音棚级音频质量。 [来源-github](https://github.com/OpenBMB/VoxCPM)
- **Archon：面向 AI 编码工作流的开源 Harness** — Archon 是首个面向 AI 编码 Agents 的开源 harness 和工作流引擎。开发者可以把 AI 开发流程（规划、实现、验证、代码审查、PR 创建等）定义为 YAML 工作流，并在不同项目中以确定性方式运行，类似于基础设施领域的 Dockerfile 或 CI/CD 领域的 GitHub Actions。该平台旨在通过把流程与验证门槛编码为可重复的工作流，来驯服 AI 的不确定性。 [来源-github](https://github.com/coleam00/Archon)

## ⚡ 快讯速览

- **初创公司可“克隆”大实验室概念；路线图带来机会** — 一条聚焦 AI 的推文称赞某头部 AI 实验室提出的产品概念很酷，并指出 OpenAI 可能不会继续在这一方向上发力。作者认为，一家初创公司可以“克隆”这个想法，并通过充分打磨和迭代使其真正可用。帖子认为，大实验室清晰且可预期的路线图，反而为初创公司追逐这些概念留出了巨大的空间。 [来源-twitter](https://x.com/karpathy/status/2042615713219908059)
- **Chutes 即是 Bittensor：去中心化团队 + 智能合约质押** — Chutes 再次强调自己是一个 Bittensor 项目，采用无 CEO 的去中心化架构。项目资金锁定在智能合约中，按质押奖励的方式支付给团队成员，他们也表示愿意帮助其他子网团队实现类似的安排。 [来源-twitter](https://x.com/jon_durbin/status/2042408990156443848)
- **SkillClaw 通过 Agentic Evolver 支持技能的集体演化** — 现有 LLM agents 依赖可复用的技能模块，但在部署后通常保持静态，导致工作流和失败模式被不同用户重复发现。SkillClaw 提出一种机制，利用来自多样化用户交互的信号，通过 Agentic Evolver 来“演化”这些技能。该方法旨在把异质性的使用经验转化为用户共享的技能改进。 [来源-huggingface](https://huggingface.co/papers/2604.08377)
- **NUMINA 提升文生视频扩散模型中的数值对齐** — NUMINA 是一个无需重新训练的框架，用于改善文生视频扩散模型中的数字（数目）对齐。它通过选取具有判别力的自注意力和交叉注意力头，推导出可计数的潜在布局以识别提示与布局不一致之处，然后对该布局进行保守式精修，并调制交叉注意力来引导再生成。 [来源-huggingface](https://huggingface.co/papers/2604.08546)
- **LocalLLaMA 项目现状** — 该帖子对 LocalLLaMA 项目的当前状态进行快照式梳理，概述近期发展和社区活动。文中强调了正在推进的工作、潜在挑战以及对离线部署 LLaMA 的持续兴趣。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shcgf5/the_state_of_localllama/)
- **实时摄像头图像生成比视频插帧“更有温度”** — 一条推文介绍了一个系统，可以从摄像头实时流中直接生成图像，而非通过视频帧插值。作者认为这类输出在观感上更“温暖”、更吸引人，并指出系统已支持 HLS 播放。 [来源-twitter](https://x.com/Yokohara_h/status/2042647120755450188)
- **Hermes Agent 开源仓库获赞超过 5 万星** — Teknium 宣布 Hermes Agent 仓库的 star 数已突破 50,000。帖文向参与项目建设的所有人表示感谢，这一里程碑也凸显了社区对 Hermes Agent 工具的日益浓厚兴趣。 [来源-twitter](https://x.com/Teknium/status/2042698709293764985)
- **ArXiv 发布《Neural Computers》，编号 2604.06425** — 一篇题为《Neural Computers》的 arXiv 预印本已上线，编号为 2604.06425。帖子仅指向该论文在 arXiv 上的摘要链接，由 SchmidhuberAI 在 Twitter 上分享，未提供关于方法或结果的更多细节。 [来源-twitter](https://x.com/SchmidhuberAI/status/2042601088029708704)
- **Deepseek 怎么了？** — Meta 的 Deepseek 在一次不完全开源的“部分回归”后似乎再次消失。一个 Reddit 讨论贴在询问 Deepseek 发生了什么，以及是否会出现 Deepseek V4。帖内没有公开的新更新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1si1qjk/what_happened_to_deepseek/)
- **Qwen 3.6 最终投票结果** — 一篇 Reddit 帖子称，针对 Qwen 3.6 的投票已结束 7 天，迹象表明版本发布即将开始。帖子链接到了 ChujieZheng 在 X 上的动态，由用户 jacek2023 分享。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1shk8ia/final_voting_results_for_qwen_36/)

---

*由 AI News Agent 生成 | 2026-04-10*