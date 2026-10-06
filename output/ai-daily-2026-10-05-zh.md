---
title: "AI 日报 — 2026-10-05"
description: "新基准长期AI伴侣，ProWAM规划视觉行动，antirez发多模型本地推理引擎"
lang: "zh"
pairSlug: "ai-daily-2026-10-05"
---

# AI 日报 — 2026-10-05

> 涵盖 25 条 AI 新闻

## 🔥 今日焦点

### 1. antirez 发布面向 DeepSeek、GLM、Qwen 的 DwarfStar 本地推理引擎

Salvatore Sanfilippo（antirez）发布了 DwarfStar（ds4），这是一个自包含的原生推理引擎，面向消费级硬件上的 DeepSeek V4 Flash/PRO、GLM 5.x 和 Qwen3.8 Flash Next。它优先支持 Metal，并支持 CUDA 和 ROCm，还捆绑了 GGUF 文件、imatrix/质量/速度工具、HTTP 服务器以及经过测试的编码智能体。这个定位狭窄、有明确取舍的运行时，可能让高端本地模型更容易运行，并挑战通用推理栈。[来源-github](https://github.com/antirez/ds4)

### 2. Reflection AI 将推出美国开放权重模型，对标 DeepSeek、Qwen

据 Reddit 上对一篇付费墙 Axios 报道的讨论，Reflection AI 据称正在准备一个美国开放权重模型，旨在与 DeepSeek 和 Qwen 竞争。社区反应集中在对其在 200B 以下参数规模下具备强劲性能的期待，以及更多西方开放权重竞争。如果兑现，它将改变开放模型格局，并给美国实验室和中国发布的模型都带来压力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wy0jrc/reflection_ai_is_about_to_release_a_us_openweight/)

### 3. 125B Qwen3.8-Flash-Next 在单台 Strix Halo 迷你 PC 上以 44-59 tok/s 运行

开发者发布了 Qwen3.8-Flash-Next 的 95 GB EXL3 权重，以及基于 ExLlamaV3 构建的开源 Kyojin 推理引擎。在一台配备 128 GB RAM 的 AMD Strix Halo 迷你 PC 上，它达到 44–59 tok/s 解码、约 1,400 tok/s 预填充，并在 64K 和 128K 下的长上下文探针中取得 10/10。结果表明，125B MoE 模型可以在紧凑的本地硬件上实用运行，且与 FP8 的 top-1 一致率达到 94.1%。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wybesy/qwen38flashnext_125b_on_a_single_strix_halo_mini/)

## 📰 重点报道

### 基准测试与评估

- **RealCompanion：在长期聊天中基准测试 AI 伴侣理解能力** — RealCompanion 基于十段真实的人类-AI 伴侣关系构建，涵盖长达 120 天内的 27,218 条消息，测试记忆、身份推断和长期对话推理，同时力求保护隐私。[来源-huggingface](https://huggingface.co/papers/2610.01780)

### 机器人与具身 AI

- **ProWAM：面向世界动作模型的渐进式视觉规划** — ProWAM 通过面向目标进行渐进式规划，而不是密集视频推演或单帧预测，改进了长时程机器人控制。[来源-huggingface](https://huggingface.co/papers/2610.02508)
- **MotorMind 为通用 VLM 搭建脚手架以实现零样本机器人操作** — MotorMind 让通用 VLM 适配零样本机器人操作，减少对专用视觉-语言-动作模型和外部工具的依赖。[来源-huggingface](https://huggingface.co/papers/2609.38078)

### 高效开放模型与边缘 AI

- **Blockway 的 Agens Volundr 32B 预览版使用混合注意力，削减 KV 缓存** — 这个 Apache-2.0 许可的 72 层稠密模型使用 54 个 KDA 线性注意力层、17 个 BCSA 层和 1 个全注意力层，仅留下 18 层带 KV 缓存，以支持长上下文部署。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wy7wn0/agens_volundr_32b_preview_our_small_teams_first/)
- **Cactus Whistle：16.9MB ASR 模型胜过 Whisper base** — Whistle 是一个 55M 参数、2-bit 量化的 ASR 模型，体积仅 16.9MB，报告称在多个基准上 WER 优于 Whisper base，并支持八种语言。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyemcb/whistle_speech_to_text_in_a_169mb_file/)

### LLM 能力与科学推理

- **Clef Flash 9B 在 RTX 5080 上实时玩贪吃蛇** — 一个 9B Q4 模型在 135ms 回合限制下实时玩 Google Snake，没有经过训练，也没有篡改游戏状态，暗示了更广泛的连续决策能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wy55p2/clef_flash_plays_snake_in_real_time_on_rtx_5080/)
- **研究测试蛋白质折叠学习能否泛化到更广泛的推理** — FoldingCorpus 和 Fold2Reason 测试源自蛋白质的结构与拓扑问答能否教会 LLM 可复用的推理技能。[来源-huggingface](https://huggingface.co/papers/2609.38879)

## ⚡ 快讯速览

- **NAVA-WAM 从仅观测视频中原生学习动作先验** — 一种新的世界动作模型直接从仅观测视频中学习动作先验，减少对动作标注数据的依赖。[来源-huggingface](https://huggingface.co/papers/2610.03391)
- **OpenMontage 推出开源智能体视频制作系统** — OpenMontage 为端到端视频制作提供开源智能体流水线。[来源-github](https://github.com/calesthio/OpenMontage)
- **Garry Tan 推出 gstack，为独立构建者提供 23 款 AI 工具** — gstack 打包了 23 款面向单人构建者和独立开发者的 AI 工具。[来源-github](https://github.com/garrytan/gstack)
- **PewDiePie 在构建本地 AI 模型时被 OpenAI 封禁两次** — PewDiePie 表示，他在构建本地 AI 模型时被 OpenAI 封禁两次，引发了对 API 审核的讨论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wymgu6/pewdiepie_getting_banned_twice_by_openai_while/)
- **Anthropic 人工审核团队向警方报告了 Claude 用户日记中的威胁** — 一篇 Reddit 帖子声称，Anthropic 的人工审核团队向警方报告了一名 Claude 用户日记中的威胁，引发隐私担忧。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyjuh0/when_redditors_come_in_here_and_ask_why_we_run/)
- **TinyDecide：10M 参数模型仅 6MB，可在 ESP32 上运行** — TinyDecide 是一个压缩至 6MB 的 10M 参数模型，可在 ESP32 微控制器上运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wybi2y/smallest_jevlike_model/)
- **CivBench 基准：GLM-5.3 在 Civilization V 中领先 Opus-5.5** — CivBench 在 Civilization V 上评估 LLM，据报道 GLM-5.3 表现优于 Opus-5.5。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wynbvq/a_benchmark_for_llms_playing_civilization_v_glm53/)
- **上下文语言模型：LLM 像文件一样编辑上下文** — 一篇新论文提出上下文语言模型，其中 LLM 像编辑文件一样编辑自己的上下文。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyf63m/yall_this_is_a_sexy_paper_context_language_models/)
- **M5 Ultra 256 在 oMLX 上以 68.8 tok/s 运行 GLM 5.3 Flash** — 据一项本地基准测试，M5 Ultra 256 在 oMLX 上以 68.8 tok/s 运行 GLM 5.3 Flash。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wy8k3m/m5_ultra_256_running_glm_53_flash_688_toks/)
- **llama.cpp v0.6.0 为 Qwen4Exp 等新增 MTP 投机解码** — llama.cpp v0.6.0 为 Qwen4Exp 新增 MTP 投机解码及其他改进。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyh03u/llamacpp_v060_released_with_mtp_speculative/)
- **Text-to-CAD 插件为 AI 智能体提供本地 3D 建模工作流** — 一个 text-to-CAD 插件让 AI 智能体运行本地 3D 建模工作流。[来源-github](https://github.com/earthtojake/text-to-cad)
- **pstack 智能体工作流栈已移植到 Claude Code、Codex 等** — pstack 的智能体工作流栈已移植到 Claude Code、Codex 和其他编码智能体。[来源-github](https://github.com/michael-denyer/pstack-claude)
- **AdamW 优化器状态的 FFT 压缩将微调显存降低 50%** — 据报道，用 FFT 压缩替换 AdamW 优化器状态可将微调显存降低 50%。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyihlz/we_swapped_adamws_optimizer_states_for_a_fast/)
- **Reddit：为什么 Qwen 27B 参数更少却能胜过 GPT-4o** — 一个 Reddit 帖子探讨了为什么 Qwen 27B 尽管参数更少，却能胜过 GPT-4o。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyefkt/how_is_it_possible_that_qwen_27b_is_so_good_when/)
- **NVIDIA 因同价销售 64 GB 与 128 GB DGX Spark 而受到批评** — NVIDIA 因以相同价格销售 64 GB 和 128 GB 版 DGX Spark 而面临批评。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wyea30/make_no_mistake_selling_64_gb_dgx_spark_variants/)

---

*由 AI News Agent 生成 | 2026-10-05*