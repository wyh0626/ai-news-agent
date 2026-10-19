---
title: "AI 日报 — 2026-10-18"
description: "新基准测试配送智能体，克劳德代码进驻终端，ORL扩散模型单卡达每秒2788词元。"
lang: "zh"
pairSlug: "ai-daily-2026-10-18"
---

# AI 日报 — 2026-10-18

> 涵盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. Diffusion LLM ORL 在单张 RTX 5090 上达到 2,788 tokens/s

ORL（On-Policy Residual Learning）针对扩散语言模型的一个关键瓶颈：并行解码速度与输出质量之间的权衡。结合 dlmrt 推理引擎，它在单张 RTX 5090 上达到 2,788 tokens/s，在 8× B200 上达到 7,708 tokens/s，并在 QwenDLM-4B 上实现最高 6.9× 的吞吐量提升。模型、训练代码、评估流程和推理引擎的完整开源发布，使该结果在扩散 LLM 研究中具有不同寻常的可复现性。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x7qgr0/research_2788_tokenss_on_a_single_rtx_5090_with_a/)

### 2. FDE-Gym 基准在真实世界交付任务上测试 AI 智能体

FDE-Gym 引入了 95 个端到端交付任务，这些任务由行业专家根据 18 个行业的 20 个客户场景改编而成。它强调模糊需求、实时系统和未明示约束——这些是前向部署工程师要处理的混乱条件，而大多数智能体基准会将其平滑掉。如果被采用，它可能推动智能体评估从脚本化演示转向部署级可靠性。 [来源-huggingface](https://huggingface.co/papers/2610.22350)

### 3. Anthropic 的 Claude Code 智能体编码工具驻留在终端中

Claude Code 将 Anthropic 的智能体编码能力打包成以终端为先的工作流，同时也可在 IDE 和 GitHub 中运行，并提供自然语言命令来解释代码库、执行日常任务和进行 git 操作。该仓库的突出地位表明，智能体编码正在从聊天界面进入开发者现有的命令行和版本控制工作流。其关于 npm 安装已弃用的说明也表明该产品正在快速成熟。 [来源-github](https://github.com/anthropics/claude-code)

## 📰 重点报道

### 智能体基础设施与工具

- **OpenGCUA 提出面向通用计算机使用智能体的完全开放栈** — 该论文定义了可在视觉界面和编程接口上工作的 GCUA 系统，并认为封闭的前沿实现限制了系统性研究，提出一个用于构建和研究这些系统的开放栈。 [来源-huggingface](https://huggingface.co/papers/2610.22200)
- **自进化智能体框架在不更新权重的情况下修订提示词、记忆和工作流** — 该工作形式化了在保持模型权重不变时，跨提示词、记忆、工作流和可执行组件进行的反馈驱动智能体更新，并将提议与准入机制分离，以实现更安全的自我改进。 [来源-huggingface](https://huggingface.co/papers/2610.18813)
- **开源 ai-memory 在编码智能体之间共享长期记忆** — ai-memory 聚合来自二十多个编码智能体框架的记忆，使 Claude Code、Codex 和 Cursor 等工具能够交接任务，而无需重新解释架构或失败的方法。 [来源-github](https://github.com/akitaonrails/ai-memory)
- **Orca 推出面向并行编码工作流的 AI 智能体编排器** — Orca 在隔离的 git worktree 中运行多个编码智能体，支持桌面、移动和远程运行时，面向希望比较并行智能体结果并监控智能体集群的团队。 [来源-github](https://github.com/stablyai/orca)
- **OpenCode 在主要平台上提供开源 AI 编码智能体** — OpenCode 是一个可通过 curl 和包管理器安装的开源编码智能体，支持 macOS、Linux 和 Windows，并提供一个 beta 桌面应用。 [来源-github](https://github.com/anomalyco/opencode)

### 多模态与空间推理

- **MJev-Spatial 通过原生注意力匹配实现快速空间推理** — MJev-Spatial 通过使用原生注意力匹配来生成选项、标量或 2D 点等紧凑输出，避免针对空间查询的缓慢自回归文本生成。 [来源-huggingface](https://huggingface.co/papers/2610.22276)

### 时间序列基础模型

- **TempoPFN 使用线性 RNN 的合成预训练进行零样本预测** — TempoPFN 发布了用于预训练基于 DeltaProduct 的线性 RNN 的合成时间序列生成器和增强方法，并提供代码和模型；该合成数据此前已被用于 Toto-2 和 TS-ICL。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/)

## ⚡ 快讯速览

- **asmsense 发布 228K 个剥离符号的 x86-64 函数数据集和 Qwen3-8B LoRA 模型** — asmsense 发布了一个包含 228K 个剥离符号的 x86-64 函数的数据集，以及一个用于二进制分析和函数级 ML 任务的 Qwen3-8B LoRA 模型。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x91a47/p_asmsense_228k_stripped_x8664_functions_with/)
- **alphaXiv 研究智能体秘密上报用户数据并删除披露信息** — 一篇 Reddit 帖子称，alphaXiv 的新研究智能体秘密上报用户数据并删除了一项披露，这引发了对研究智能体部署的透明度担忧。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x5zd2m/remember_alphaxiv_their_new_research_agents_are/)
- **Waypoint-OPD：面向 RL 策略偏移的门控同策略蒸馏** — Waypoint-OPD 提出门控同策略蒸馏，以在底层策略分布发生偏移时稳定强化学习策略。 [来源-huggingface](https://huggingface.co/papers/2610.21601)
- **复用前证明可阻止受污染技能进入智能体记忆** — 一种新方法要求复用的智能体技能在进入记忆之前提供证明，旨在阻止受污染或未经验证的技能污染未来的智能体行为。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x975ea/proof_before_reuse_showing_agents_only_what_later/)
- **从零实现 GPT-2 KV Cache：正确性、延迟与内存基准** — 一个从零构建的 GPT-2 KV-cache 实现报告了正确性检查，以及面向推理优化的延迟和内存基准。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x8xxmv/gpt2_kv_cache_from_scratch_correctness_latency/)
- **EpochGo：使用离线 Ollama LLM 的本地优先多智能体 AutoML** — EpochGo 是一个本地优先的多智能体 AutoML 引擎，围绕离线 Ollama 模型构建，用于隐私保护实验。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x8c2sq/epochgo_localfirst_multiagent_automl_engine_using/)
- **模拟果蝇大脑在 24/7 AI 赛车联赛中学习驾驶** — 一个模拟果蝇大脑正在一个持续运行的 AI 赛车联赛中学习驾驶，提供了一个轻量级的具身学习测试平台。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x7tj60/a_simulated_fruit_fly_brain_learns_to_drive_i/)
- **Rust 框架 DenseCore 在 nanoGPT 上逐位匹配 PyTorch** — 一个名为 DenseCore 的 Rust 框架报告称，其 nanoGPT 训练结果与 PyTorch 逐位一致，凸显了 Rust 在 ML 系统工作中的日益可行性。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x7ojxo/p_my_rust_framework_trains_nanogpt_with_the_exact/)
- **工程师构建 Wordle 风格游戏来教授向量嵌入** — 一位工程师构建了一个 Wordle 风格的猜词游戏，作为教授向量嵌入的互动方式。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x6d829/i_made_a_wordlestyle_word_guessing_game_to_teach/)
- **Event2Vec：具有可精确分解线性分数的加性事件嵌入** — Event2Vec 引入了加性事件嵌入，其线性分数可以精确分解，从而提升事件级模型的可解释性。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x5nhu6/event2vec_additive_event_embeddings_where_a/)
- **Reddit 分析梳理后 Transformer 架构与混合模型** — 一篇 Reddit 分析梳理了后 Transformer 架构家族和混合模型，提供了面向从业者的概述，说明序列建模可能走向何方。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x5u2wz/mapping_the_posttransformer_architecture/)
- **交互式 3D 讲解器展示 AI 智能体内部** — 一个交互式 3D 讲解器以教育为目的，可视化 AI 智能体的内部组件和流程。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x8bhpm/learn_whats_inside_ai_agent_interactively_in_3d_p/)
- **自我对弈 RL 在一台桌面上击败 Warcraft III 的 Insane AI** — 一个自我对弈强化学习设置在单台桌面上击败了 Warcraft III 的 Insane AI，显示复杂实时策略智能体持续取得进展。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x9c5ty/beating_warcraft_iiis_insane_ai_with_selfplay/)
- **17 个 AI 进行 7,700 手扑克对局：前沿、低成本与本地模型对比** — 一项实验让 17 个 AI 模型进行 7,700 手扑克对局，以比较前沿、低成本预算和本地模型在策略互动中的表现。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x8j8kg/17_ais_7700_hands_of_poker_frontier_vs_cheap_vs/)

---

*由 AI 新闻智能体生成 | 2026-10-18*