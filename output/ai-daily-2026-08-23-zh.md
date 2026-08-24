---
title: "AI 日报 — 2026-08-23"
description: "OpenAI发布终端编程代理，Anthropic的Claude新模型将推出。"
lang: "zh"
pairSlug: "ai-daily-2026-08-23"
---

# AI 日报 — 2026-08-23

> 本期覆盖 39 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 发布终端专用 Codex CLI 编程代理

OpenAI 发布了 Codex CLI，这是一款轻量级编程代理，可在终端本地运行，支持 Mac、Linux 和 Windows，并额外提供 IDE 集成、桌面应用和云端 Web 版本。通过将 Agent 编程带入开发者的原生环境，OpenAI 正与 Anthropic 的 Claude Code 直接竞争，并将赌注押在终端优先的 AI 辅助软件开发工作流上。[来源-github](https://github.com/openai/codex)

### 2. 新 Claude 模型 Marshmallow 和 Melon 现身，发布在即

Anthropic 平台上出现了两款未发布的 Claude 模型，代号分别为 Marshmallow 和 Melon，表明发布已迫在眉睫，可能包括 Opus 更新，甚至可能推出新的 Haiku 层级。这次现身表明 Anthropic 正在准备一次重大模型更新，可能重新洗牌前沿大语言模型能力与定价的竞争格局。[来源-x](https://x.com/kimmonismus/status/2091599817084412221)

### 3. Ollama 与 Poolside 和 Nvidia 合作推动开放模型

Ollama 宣布与 Poolside AI 合作，并对 Nvidia 的 Nemotron 系列表达了高度兴趣，据《华尔街日报》报道，双方达成了一项广泛协议，旨在美国构建开放的 AI 生态系统。该合作旨在强化开放模型栈，以对抗封闭的前沿实验室，可能加速企业采用自托管和本地运行的大语言模型。[来源-x](https://x.com/ollama/status/2091344612980060304)

## 📰 重点报道

### 编程代理与开发者工具

- **Anthropic 的 Claude Code 将 Agent 编程带入终端** — Anthropic 发布了 Claude Code，这是一款可在终端中通过自然语言执行日常任务、解释代码和处理 Git 工作流的 Agent 编程工具，支持 MacOS、Linux 和 Windows。在不断整合的 Agent 编程领域中，它为开发者提供了 OpenAI Codex 之外一个直接的 CLI 替代方案。[来源-github](https://github.com/anthropics/claude-code)

### 开源与 AI 经济

- **开源 AI 从 OpenAI 和 Anthropic 手中夺取 Token 份额** — Vercel 数据显示，开源 AI 的 Token 份额在两个月内从 28% 跃升至 62%，超过了 OpenAI 和 Anthropic 的总和，不过封闭前沿模型的 Token 预计仍将保留 60–90% 的经济价值。这一转变表明，随着企业混合使用开源和封闭模型，对 AI 基础设施的需求强劲。[来源-x](https://x.com/GavinSBaker/status/2091542026072338623)
- **Claude 订阅每月价值高达 8000 美元；OpenAI 的 Token 价值高达 14000 美元** — SemiAnalysis 发现，Anthropic 和 OpenAI 每月 200 美元的订阅计划，对于长期任务而言，每月可提供分别高达 8,000 美元和 14,000 美元的 Token 价值。该分析突显了订阅定价与重度用户的原始 Token 经济价值之间正在急剧脱钩。[来源-x](https://x.com/SemiAnalysis_/status/2091631658973671900)

### 研究与基准

- **SemComp-Bench：面向结果导向的视频生成新基准** — 提出了 Semantic Task Completion Video Generation，这是一个结果导向的基准，通过参考图像的语义锚定来评估生成的视频是否达到了预期结果，无需中间任务步骤。它将视频评估从视觉保真度转向了高层语义对齐。[来源-huggingface](https://huggingface.co/papers/2608.17426)
- **研究人员将于明日发布完整的大语言模型强化学习指南** — 一份全面的 LLM 强化学习指南计划于明早发布，内容综合了 RLHF Book、Sutton & Barto、OpenAI 的 Spinning Up 以及 Sebastian Raschka、John Schulman 等人的工作。该指南有望成为从业者在碎片化的 RL 文献中导航的统一资源。[来源-x](https://x.com/cwolferesearch/status/2091570446164733962)

### 硬件与推理

- **RTX 5090 以 24 tok/s 运行 284B 模型，预示 2027 年本地 AI 前景** — 单张 RTX 5090 现在可以原生 mxfp4 精度运行 DeepSeek-V4-Flash 284B 模型，速度约 24 tokens/s，而 2024 年 RTX 4090 上 4-bit Llama 3 70B 的速度仅约 2 tokens/s。这一发展轨迹表明，到 2027 年消费级本地 AI 将具备前沿级推理能力。[来源-x](https://x.com/Yuchenj_UW/status/2091577203335307450)

### 多模态与创意 AI

- **Reddit 用户发现 H3 生成 2D 精灵表动画的简单提示词** — 为 H3 模型编写的一个简单提示词即可生成游戏可用的 2D 精灵表动画，包括一只带有待机动画的可爱龙。该演示凸显了 H3 在游戏资源工作流中不断增强的创意多模态生成能力。[来源-x](https://x.com/andrew_n_carr/status/2091560238558429560)

## ⚡ 快讯速览

- **EnvHarness：用于动态代理训练环境的新框架** — 一个用于构建动态环境以训练 AI 代理的新框架。[来源-huggingface](https://huggingface.co/papers/2608.19880)
- **高效闭环具身框架助力自进化物理智能** — 论文提出了一种闭环具身框架，可实现自进化的物理智能。[来源-huggingface](https://huggingface.co/papers/2608.16590)
- **2026 年：企业将模型效率与可靠性视为关键基础设施** — 行业观察人士指出，随着模型被视为关键基础设施，效率和可靠性已成为最高优先级。[来源-x](https://x.com/thsottiaux/status/2091581575108653374)
- **FACET 在终端任务中保留源意图与可执行状态** — 一种在基于终端的代理任务中保留源意图和可执行状态的新方法。[来源-huggingface](https://huggingface.co/papers/2608.18580)
- **n8n：拥有 1500+ 集成的 AI 原生工作流自动化平台** — 开源自动化平台 n8n 持续扩展 AI 原生能力，目前已拥有超过 1,500 个集成。[来源-github](https://github.com/n8n-io/n8n)
- **TextGen v4.7 带来原生桌面应用和多 GPU 张量并行** — TextGen v4.7 新增了原生桌面应用以及用于多 GPU 推理的张量并行功能。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t29ztv/textgen_v47_released_portable_builds_now_run_as_a/)
- **TextGen v4.6 发布：工具调用确认、MCP 服务器等新功能** — 更名后的 TextGen 新增了工具调用确认、MCP 服务器支持以及其他改进。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1st7nkz/textgenerationwebui_has_been_renamed_to_textgen/)
- **Figure 人形机器人在总部办公室自由行走** — 视频画面显示 Figure 人形机器人在公司总部内自主导航行走。[来源-x](https://x.com/adcock_brett/status/2091559896315740376)
- **SemaPLC：用于 PLC 代码生成的验证门控代理框架** — 一种带有形式化检查的验证门控框架，用于生成 PLC 代码。[来源-huggingface](https://huggingface.co/papers/2608.18565)
- **Sub2API：AI 订阅共享的开源网关** — 一个开源网关，通过统一 API 实现 AI 订阅共享。[来源-github](https://github.com/Wei-Shaw/sub2api)
- **Karpathy 的 LLM 陷阱清单被制成 Claude Code 的 CLAUDE.md** — Andrej Karpathy 的 LLM 陷阱清单已被打包成适用于 Claude Code 的 CLAUDE.md 技能文件。[来源-github](https://github.com/multica-ai/andrej-karpathy-skills)
- **教程：在 TextGen 中使用 Exllamav3 + DFlash 投机解码** — 社区指南介绍了如何在 TextGen 中配置 Exllamav3 与 DFlash 投机解码。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t5698m/howto_exllamav3_dflash_speculative_decoding_in/)
- **Project Zora：Text-Generation-WebUI 的实验性 AI 伴侣记忆架构** — 一个面向 TextGen 的实验性本地 AI 伴侣记忆架构。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t3teky/project_zora_experimental_local_ai_companion/)
- **Parallelogram Linter 在 GPU 运行前捕获损坏的 LLM 微调数据** — 一个严格的 linter 可在昂贵的 GPU 训练之前验证 LLM 微调数据集。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t1s8ef/parallelogram_a_strict_linter_for_llm_finetuning/)
- **TextGen v4.8 发布：修复多项 Bug 并带来 Gemini 风格聊天输入** — TextGen 最新版本包含多项 Bug 修复和一个重新设计的 Gemini 风格聊天输入框。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t6jr50/textgen_v48_released_many_bug_fixes_restyled_chat/)
- **Anthropic 承认 Opus 回答冗长，提供简洁输出修复** — Anthropic 针对 Opus 过度详尽的问题，为用户提供了简洁输出的修复方案。[来源-x](https://x.com/bcherny/status/2091591570982371454)
- **Malik 呼吁机器人领域术语精确：VLM 与 World Models 之辨** — Jitendra Malik 呼吁在机器人领域使用更清晰的术语，以区分 VLM 和世界模型。[来源-x](https://x.com/JitendraMalikCV/status/2091582134955991348)
- **评论：生成式 AI 威胁就业，而中国在快速交付房屋** — 评论文章将生成式 AI 的就业替代风险与中国快速的实体建筑产出进行了对比。[来源-x](https://x.com/suchenzang/status/2091631636744138918)
- **用户询问 TextGen 是否支持 MTP 投机解码** — 社区用户询问 TextGen 是否支持多 Token 预测（MTP）投机解码。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1tbxexu/mtp_speculative_decoding_support/)
- **财富 500 强科技公司仍无法访问 GPT 5.6 Sol** — 据报道，一家财富 500 强科技公司仍然无法访问 OpenAI 的 GPT 5.6 Sol。[来源-x](https://x.com/reach_vb/status/2091549320818372939)
- **推特用户畅想 Ox Alpha 运行于 DGX Spark** — 一条推测性帖子畅想在 Nvidia 的 DGX Spark 硬件上运行 Ox Alpha。[来源-x](https://x.com/kimmonismus/status/2091546117825560907)
- **下一代 AI 模型预计将引发本体论冲击** — 有预测称下一代模型将超出当前预期，引发本体论冲击。[来源-x](https://x.com/skirano/status/2091652181870973309)
- **用户提议 Oobabooga 增加"从上次编辑处重新生成"功能** — 社区成员建议在 Oobabooga 中增加"从上次编辑处重新生成"的功能。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t2vhdw/would_love_if_a_bug_was_brought_back_but_as_a/)
- **用户寻求在 ARM64 Linux 上运行 Oobabooga 的帮助** — 用户询问如何在 ARM64 Linux 上运行 Oobabooga，特别是 Nvidia DGX Spark。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1t0o5x4/oobabooga_for_linux_on_arm64_nvidia_dgx_spark/)
- **Gemma 4 EXL3 加载问题已在 v4.6.0 中修复** — TextGen v4.6.0 已解决 Gemma 4 EXL3 模型的加载问题。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1srapvj/issue_with_loading_gemma_4_exl3/)
- **Oobabooga 社区寻求 Gemma 4 采样参数** — 用户正在寻求 Gemma 4 模型的最优采样参数。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1soekcx/optimal_sampling_parameters_for_gemma_4_models/)
- **Oobabooga 运行 Qwen3 8B 时 GPU 利用率为 0%** — 一位用户报告在运行 Qwen3 8B 时 GPU 利用率一直停留在 0%。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1silnvg/gpu_utilisation_stuck_at_0/)
- **Oobabooga 用户寻求 Pocket TTS 播放问题帮助** — 一位用户就 Ooba/Pocket TTS 的播放问题寻求建议。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1sghru4/need_some_advice_with_an_oobapocket_tts_issue/)
- **如何在 Oobabooga 上使用 Rotorquant 或 Turboquant？** — 用户询问如何在 Oobabooga 中使用 Rotorquant 或 Turboquant 量化方法。[来源-reddit](https://www.reddit.com/r/Oobabooga/comments/1smze7e/rotorquant_or_turboquant_on_oobabooga/)

---

*由 AI 新闻代理生成 | 2026-08-23*