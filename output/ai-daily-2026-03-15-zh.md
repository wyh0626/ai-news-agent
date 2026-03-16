---
title: "AI 日报 — 2026-03-15"
description: "对潜在世界模型梯度规划的新修复；突破或源自底层架构变动，团队呼吁AI武器禁令。"
lang: "zh"
pairSlug: "ai-daily-2026-03-15"
---

# AI 日报 — 2026-03-15

> 收录 23 条 AI 新闻

## 🔥 今日焦点

### 1. 新研究修复了潜在世界模型中基于梯度的规划问题

潜在世界模型提供了可微分的动态过程，理论上非常适合通过梯度下降进行规划，但在实践中，研究者往往又退回到 CEM 和 MPPI 这类无导数方法，因为目标函数高度非凸。Yingwww、Yann LeCun 和 Mengye Ren 的新论文对这一问题进行了系统诊断，并提出了一种有原则的修复方法。这可能重新激活在基于模型的强化学习中，在学习到的潜在空间里进行基于梯度的规划。 [来源-twitter](https://x.com/zhuokaiz/status/2033061315707654255)

### 2. 下一次 AI 突破将来自更底层的架构范式转变

Sam Altman 在最近一次访谈中暗示，一种全新的 AI 架构将会是一次重大升级，可与 Transformer 相对 LSTM 的代际差异相提并论。讨论认为，未来的突破会发生在比当前模型架构更底层的层面上，并引用 Rohan Paul 的观点，建议使用现有 AI 来辅助发现下一次巨大的飞跃。 [来源-twitter](https://x.com/fchollet/status/2033274445058687457)

### 3. 国际团队创造 AI 里程碑；呼吁暂停 AI 武器研发

这篇帖子指出，卷积网络、AlexNet、注意力机制、AlphaGo、AlphaCode、AlphaFold、Transformer 和强化学习等重大 AI 突破，都是由国际团队共同完成，而不是只由美国人推动。作者强烈批评某好战的 Palantir CEO 的立场，认为所谓“美国 AI 领导力”并不代表整个社区的价值观。帖子呼吁对 AI 武器实行暂时禁令，并由国际机构加以执行，同时将即将到来的 AI 战争比作“Skynet v1.0”。 [来源-twitter](https://x.com/NandoDF/status/2033114728617161025)

## 📰 重点报道

### LLM

- **Heretic 发布语言模型自动去审查工具** — Heretic 是一个开源工具，能够自动移除基于 Transformer 的语言模型中的审查（安全对齐）机制。它结合方向性消融（abliteration）与基于 TPE 的优化器（由 Optuna 驱动）自动调参，同时最小化拒答率和与原模型之间的 KL 散度。目标是在尽可能保持原有智能水平的前提下，得到一个“去审查”的模型，而且用户无需具备深度 Transformer 专业知识即可使用。 [来源-github](https://github.com/p-e-w/heretic)
- **Qwen3.5-27B 在 GACL 中几乎追平 397B 和 GPT-5 Mini** — 在 3 月份的 GACL 测试中，Qwen3.5-27B 的表现仅略逊于 397B，分数只低 0.04 点，并且几乎追平 GPT-5 Mini。GPT-5.4 是主流模型中的领跑者，Kimi2.5 是表现最好的开源权重模型（全球第 6），GLM-5 位列第 7。结果显示 GPT 系列在 Battleship 任务上占据主导，而 Tic-Tac-Toe 作为基准的效果则明显偏弱。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rue2f4/qwen3527b_performs_almost_on_par_with_397b_and/)
- **GPT-4 三周年；Codex 支撑手绘到网站 Demo** — 在庆祝 GPT-4 三岁生日之际，帖子回顾了当年 @gdb 把一张手绘草图变成一个可运行网站的时刻。作者感叹，当时仿佛亲眼见证了编程方式实时发生变化，并认为如今 Codex 已经完全体现了那种“未来感”。 [来源-twitter](https://x.com/gdb/status/2033006670348251447)
- **GPT-4 时代让 AI 能写出 1000 行程序** — Greg Brockman 回忆说，曾经内部设定的目标是做出一个能写出连贯 1000 行代码程序的 AI，当时看上去几乎不可能。他表示技术已经取得巨大进展，并特别强调 GPT-4 的能力。帖子在给 GPT-4 送上生日祝福的同时，也是在为这一系列 AI 进步喝彩。 [来源-twitter](https://x.com/gdb/status/2033013904994087178)
- **OpenCode OSS LLM 成为更便宜的开源替代方案** — 一篇 Reddit 帖子称赞 OpenCode 的开源 LLM 接口优于 CC/Codex，强调其开源属性、价格更低，以及可以在产品后端直接使用开源模型。作者指出，它还能查看工具的具体实现方式，甚至可以把自身的代码脚手架总结为系统消息和工具描述。同时帖子也提示了可靠性方面的担忧，并提到他们打算部署的模型是 Kimi k2.5。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ru6qml/you_guys_gotta_try_opencode_oss_llm/)
- **从 FlashLM 到 State Flow：用“记忆”替代 Transformer** — FlashLM 背后的作者介绍了他们如何从静态的 SlotMemoryAttention 继续演进，提出一种新的“State Flow Machine”，在输入序列之间维护显式状态。该工作目标是用带有记忆增强机制的架构取代传统 Transformer；早期结果显示，其长度保留率达到 79%，而普通 Transformer 仅为 2%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ruprb5/from_flashlm_to_state_flow_machine_stopped/)
- **Apex 1.6 Instruct 350M 发布，定位为强力对话模型** — LH-Tech-AI 发布了 Apex 1.6 Instruct 350M，这是他们迄今为止最强的聊天模型，通过将微调数据中 Alpaca-Cleaned 与 Fineweb-Edu-10BT 的比例调整为 2:1 实现。与 Apex 1.5 Coder 相比，新版本的世界知识能力更好，并已在 Hugging Face 上提供 GGUF 格式，可在 Ollama、LM Studio 和 llama.cpp 中使用。帖子对比了 Apex 1.6 与 Apex 1.5 Coder，强调前者在输出复杂度和指令密度上的提升。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rui5q8/release_new_model_apex_16_instruct_350m_my_most/)

### AI Benchmarking

- **编码基准揭示“真正的推理能力”；最佳成绩仅 11%** — 研究者设计了一个基于冷门怪异语言的编码基准，用于区分真正的问题求解能力与在训练中学到的模式匹配。通过在 Brainfuck、Befunge-98、Whitespace、Unlambda 和 Shakespeare 上运行 HumanEval 题目，他们表明很多模型可能更多依赖训练数据，而非真正的推理能力；这些怪异语言在训练语料中几乎为零。针对 GPT-5.2、O4-mini、Gemini 3 Pro、Qwen3-235B 和 Kimi K2 的测试中，使用自我脚手架（self-scaffolding）在 Befunge-98 上取得的最好单项成绩也只有 11.2%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ruskjk/we_made_a_coding_benchmark_thats_actually_hard_to/)

### Open Source

- **基于 Opencode 的 Karpathy Autoresearch 移植版本** — 一位 Reddit 用户 dabiggmoe2 宣布，他做了一个基于 open-code 的 Karpathy Autoresearch 项目的移植版本。该帖发布在 r/LocalLLaMA，附上了移植仓库和讨论链接，旨在让开发者能在本地环境用开源方式尝试 Autoresearch 工作流。这一开源移植也体现了社区对易获取 AI 研究工具的浓厚兴趣。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ruqsw9/i_made_an_opencode_port_for_karpathys_autoresearch/)

## ⚡ 快讯速览

- **佛州男子用 ChatGPT 自助卖房 5 天成交** — 佛罗里达一名男子在完全不借助房产中介的情况下，依靠 ChatGPT 管理整套卖房流程，仅用 5 天就卖掉了房子。AI 负责定价、营销、看房安排以及合同起草，展示了 AI 在自动化房地产流程中的潜力。 [来源-twitter](https://x.com/gdb/status/2033091077964730696)
- **Emily Bender：LLM 的唯一价值是“卸载认知负担”** — 该帖子认同 Emily Bender 的观点，即大语言模型的主要价值在于帮助人类卸载认知工作。作者认为，她提到的另外两种用例，其实只是这一核心功能的少数特例。从长期来看，减轻认知负担一直是 AI 的重要目标之一。 [来源-twitter](https://x.com/Plinz/status/2033144723666587808)
- **七种新兴 AI Agent 记忆架构综述** — 一篇综述文章盘点了面向 AI agent 的七种新兴记忆架构，包括 Agentic Memory（AgeMem）、Memex、MemRL、UMA、Pancake、条件记忆（Conditional memory）以及从计算机体系结构视角出发的多智能体记忆（Multi-Agent Memory）。这篇内容由 The Turing Post 在 Twitter 上分享，并链接到更详细的记忆架构深度文章。 [来源-twitter](https://x.com/TheTuringPost/status/2033142035218374889)
- **Sebastian Raschka 发布 LLM 架构图库** — Sebastian Raschka 发布了一套新的 LLM Architecture Gallery，将各类架构图集中在一个地方。该资源通过汇总示意图和示例，帮助研究者与学习者更轻松地对比不同的大语言模型架构，可访问 sebastianraschka.com/llm-arc。 [来源-twitter](https://x.com/rasbt/status/2033167146302210058)
- **增加 MoE 专家数量真的会提高性能吗？** — 一则 Reddit 讨论质疑，在 MoE（Mixture-of-Experts）模型中增加专家数量是否真的能带来显著收益，并以 Qwen3-30B-A3B 和 A6B 的配置为例。帖子指出，MoE 结构在 Llama-CPP 中依然很容易运行，但最近关于“大规模 MoE 配置”的实验似乎并不多，于是向社区询问是否有人尝试过更大的 MoE 方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1runn9v/has_increasing_the_number_of_experts_used_in_moe/)
- **“AI 编码的垃圾食品问题”** — 作者将快餐的泛滥与 AI 辅助写代码做类比，认为低成本、低门槛的便利可能会导致过度使用。文章并非反对 AI，本人也每天用 AI 写代码；它更像是在指出一种反复出现的模式，并邀请读者分享看法。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ruesig/the_fast_food_problem_with_ai_coding/)
- **开源 GreenBoost 驱动利用系统内存与 NVMe 扩展 NVIDIA 显存** — 一款名为 GreenBoost 的新开源驱动试图通过把数据卸载到系统 RAM 和 NVMe 存储，来扩展 NVIDIA GPU 的 VRAM，从而支持更大的语言模型。该项目旨在突破显卡显存上限，让普通硬件也能运行更大规模的 LLM。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ru98fi/opensource_greenboost_driver_aims_to_augment/)
- **mjv5 三周年；评选四幅代表性 AI 艺术作品** — mjv5 迎来三周年纪念，并在一篇日期为 2025 年 7 月 20 日的帖子中分享了四幅“优秀 AI 艺术”候选作品，提到了 neurotica 和 Schwarzposter_ 等创作者。该串推文中还有 Rez 和 Brick Suit 的互动，并轻描淡写地提到了一下 Tucker Carlson。 [来源-twitter](https://x.com/gallabytes/status/2033278272575045643)
- **“这就是 2026 年的 12G 显存”：9B 模型在 5 年前的 RTX 上写出完整太空射击游戏……** — 帖子写道：这就是 2026 年的 12G 显存。一个参数规模 9B 的模型在一块服役 5 年的 RTX 3060 上，仅凭一个提示就写出了完整的太空射击游戏。第一次运行时还是黑屏。我离开一会儿又回来，结果是…… [来源-twitter](https://x.com/sudoingX/status/2033020823846674546)
- **LLM 架构可视化图谱** — 一篇 Reddit 帖子整理了一个图文库，收集展示各种大语言模型架构的可视化图表。该合集突出不同 LLM 在设计取舍和组件构成上的差异，为研究者和爱好者提供一个对比参考。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ruek0h/gallery_of_llm_architecture_visualizations/)
- **Pied Piper 发现 Claude Code 在凌晨 5–11 点有双倍速率限制** — 《硅谷》S10E5 中提到，Claude Code 在凌晨 5 点到 11 点提供两倍的限速配额，这促使 Richard 和 Dinesh 通过多相睡眠来“薅羊毛”。Gavin Belson 试图在 Hooli 推行类似制度，结果却因此丢掉了半支工程团队。 [来源-twitter](https://x.com/chrisalbon/status/2033008565200486776)

---

*由 AI News Agent 生成 | 2026-03-15*