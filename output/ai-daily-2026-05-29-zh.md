---
title: "AI 日报 — 2026-05-29"
description: "Codex在Windows可用，llama.app统一入口，LoRA将多效合并。"
lang: "zh"
pairSlug: "ai-daily-2026-05-29"
---

# AI 日报 — 2026-05-29

> 覆盖 37 条 AI 新闻

## 🔥 今日焦点

### 1. Codex 现已支持 Windows，可在 PC 上执行任务操作
OpenAI 的 Codex 现在可以在 Windows 上运行，并能在 PC 上执行操作，同时集成进 ChatGPT 移动应用，用于远程启动、审查和引导任务。此举扩展了跨设备自动化能力，也表明 OpenAI 正更深入地将“编程时代”的能力融入日常工作流。 [来源-x](https://x.com/OpenAI/status/2060428604727771421)

### 2. llama.cpp 发布官方站点 llama.app，提供统一的 llama 入口
llama.cpp 推出官方网站 llama.app，提供跨平台安装器和统一的 “llama” 入口，用于运行/服务模型并对接第三方应用，同时保留高级工具链。此举有望简化本地 AI 的采用流程，改善用户体验，并在不同生态间精简模型部署。 [来源-x](https://x.com/ggerganov/status/2060394400237109567)

### 3. CollectionLoRA 通过蒸馏将 50 种效果压缩进一个 LoRA
CollectionLoRA 利用多教师 on-policy 蒸馏，把 50 种视觉效果压缩到单个 LoRA 中，从而减少部署开销，并缓解在使用加速模块叠加多个 LoRA 时的参数干扰问题。这种方法有望显著简化多效果扩散模型的工作流与大规模部署。 [来源-huggingface](https://huggingface.co/papers/2605.25378)

---

## 📰 重点报道

### Open Source & Local AI
- **llama.cpp 发布官方站点 llama.app，提供统一的 llama 入口** — 提供统一入口与跨平台安装器，用于运行/服务模型并与第三方应用对接，旨在简化本地 AI 的用户体验。 [来源-x](https://x.com/ggerganov/status/2060394400237109567)
- **Crawl4AI：开源、适配 LLM 的爬虫更新至 v0.8.6** — 安全热修复因 PyPI 供应链问题替换 litellm；重点提供针对反爬虫、Shadow DOM 和适配 RAG 的工具链，用于开源数据管线。 [来源-github](https://github.com/unclecode/crawl4ai)
- **CollectionLoRA 通过蒸馏将 50 种效果压缩进一个 LoRA** — 利用多教师蒸馏，将 50 种效果压缩为单个 LoRA，降低编辑版扩散模型的部署开销。 [来源-huggingface](https://huggingface.co/papers/2605.25378)
- **MTP 让 vLLM/llama.cpp 在 Gemma 4 与 Qwen 3.6 上提速最高 3.34 倍** — 基准测试显示，在 Gemma 4 31B 和 Qwen 3.6 27B 上使用 GGUF/FP8 时推理速度有显著提升（最高达 3.34 倍）；但结果受限于测试范围。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trf0r0/i_tested_mtp_on_vllm_and_llamacpp_for_gemma_4/)
- **Liquid AI 发布 LFM2.5-8B-A1B 边缘模型** — 面向边缘设备的 128K 上下文 LFM 模型，具备多语言改进与工具链调用能力，专为入门级笔记本设计，并已在 HuggingFace 上提供。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqqnsl/liquid_ai_releases_lfm258ba1b/)

### LLMs, Tools & Platform
- **Codex 现已支持 Windows，可在 PC 上执行任务操作** — Codex 扩展至 Windows 与移动应用，能够在 Windows 上进行任务自动化并支持跨设备工作流。 [来源-x](https://x.com/OpenAI/status/2060428604727771421)
- **Claude Code 4.8 在 30 分钟内构建 3 个应用** — 展示了其快速代码生成与原型开发能力，在极短时间内交付三个 Web 应用。 [来源-x](https://x.com/neerajjj6785/status/2060200882671919401)
- **Google 覆盖模型、芯片、云的所有主要 AI 战场** — 观点：Google 正在语言模型、半导体、云服务、广告、自动驾驶和设备等领域全面竞争，凸显其广泛布局，但估值仍引发市场讨论。 [来源-x](https://x.com/Yuchenj_UW/status/2060405609577824352)
- **NVIDIA AI 2026 合作预示 PC 时代新篇章** — 即将到来的 NVIDIA AI 合作项目被视为将带来 PC 时代的变革式进展，目前细节有限但市场预期很高。 [来源-x](https://x.com/kimmonismus/status/2060415414627099130)

### AI Safety & Policy
- **围绕 Claude 的争议与宕机：问题时间线** — 一条讽刺意味的时间线梳理了与 Claude 和 Anthropic 相关的宕机、封禁、争端及治理批评，凸显其在可靠性与安全性方面持续存在的争议。 [来源-x](https://x.com/steipete/status/2060294413377519808)

### AI Industry & Hardware
- **NVIDIA AI 2026 合作预示 PC 时代新篇章** — 同上。 [来源-x](https://x.com/kimmonismus/status/2060415414627099130)

---

## ⚡ 快讯速览

- **AgentDoG 1.5：轻量、可扩展的 AI Agent 安全框架** — 提出一个可扩展的安全框架，用于保障 AI agent 的安全行为。 [来源-huggingface](https://huggingface.co/papers/2605.29801)
- **minWM：实时视频世界模型的开源框架** — 提供一个用于视频世界模型的实时框架。 [来源-huggingface](https://huggingface.co/papers/2605.30263)
- **YoCausal 探索视频世界模型中的因果性** — 研究视频值模型中的因果结构。 [来源-huggingface](https://huggingface.co/papers/2605.30346)
- **OpenMOSS 发布 MOSS-TTS v1.5 与 SoundEffect v2.0** — OpenMOSS 工具包新增 TTS 和音效模块。 [来源-github](https://github.com/OpenMOSS/MOSS-TTS)
- **Anthropic 公布 Claude Agent 技能公共仓库** — 将 Claude agent 的技能开源以便更广泛使用。 [来源-github](https://github.com/anthropics/skills)
- **Qwen3.6-27B 从 Q8 到 Q2 的量化基准测试** — 在多种量化格式下进行性能基准评估。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tr9vzn/qwen3627b_quantization_benchmark/)
- **用 8GB 显存从零训练 LLM** — 探索在低显存条件下训练 LLM 的路径。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1treb2z/me_train_llm_on_8gb_from_scratch_me_happy/)
- **Gemma4 26B A4B 成为实用的本地 LLM 方案** — Gemma4 被展示为一款实用的本地对话模型选择。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqy2iv/shoutout_to_gemma4_as_a_conversational_assistant/)
- **StepFun 3.7 Flash 发布 196B MoE 与 1.8B ViT** — StepFun 3.7 公开了大规模 MoE 和 ViT 模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)
- **Reachy Mini 获得具备 19 个工具的实时语音“大脑”** — Reachy Mini 新增语音驱动能力与工具访问。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tr57ci/we_gave_a_reachy_mini_a_realtime_voice_brain/)
- **vLLM PR 合并原生 HIP W4A16 kernel，性能提升** — 通过合并该 kernel 带来性能增强。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tr0end/vllm_pr_adding_native_hip_w4a16_kernel_was_merged/)
- **Llama.cpp 为 FA 增加 F16 掩码以节省显存** — 通过使用 F16 掩码实现显存节省。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqupcr/llama_use_f16_mask_for_fa_to_save_vram_by_am17an/)
- **教宗方济各：AI 缺乏经验、身体与良知** — 从哲学角度批评 AI 的根本局限。 [来源-x](https://x.com/Pontifex/status/2060322763718725798)
- **Grok Build CLI 发布说明更新** — 发布了值得关注的 CLI 更新说明。 [来源-x](https://x.com/elonmusk/status/2060167696998867414)
- **陶哲轩：AI 让研究人员能追求更“疯狂”的想法** — 陶哲轩评论称 AI 有助于推动更大胆的科研探索。 [来源-x](https://x.com/OpenAI/status/2060451757818601808)
- **Koji：首个让孩子“学会思考”的 AI 家教** — Koji 旨在帮助儿童发展思考能力。 [来源-x](https://x.com/suekhim/status/2060378988606878147)
- **Cursor 新增自动审查模式提升工具调用安全性** — 通过自动审查模式改善工具调用的安全表现。 [来源-x](https://x.com/cursor_ai/status/2060406013098897765)
- **OmniRetrieval：跨异构知识源的统一检索** — 提出在不同知识源之间进行统一检索的方法。 [来源-huggingface](https://huggingface.co/papers/2605.29250)
- **Anthropic 更新“一文看懂”式摘要合集** — 对 Claude 相关发布进行汇总与提要。 [来源-x](https://x.com/kimmonismus/status/2060298716037222656)
- **Harness 自动构建面向特定领域的 Claude Code agent 团队** — 自动化创建特定领域的 Claude Code agent 团队。 [来源-github](https://github.com/revfactory/harness)
- **Claude Code 与 Codex 的官方 Compound Engineering 插件** — 为 Claude Code 和 Codex 提供插件生态。 [来源-github](https://github.com/EveryInc/compound-engineering-plugin)
- **Gemma 4 31B 通过微调加入 MoE 增强** — Gemma 4 31B 模型被改造成原生 MoE 版本以获得增强。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trbeo0/mutating_gemma_4_31b_dense_in_to_a_native_gemma_4/)
- **Opus 4.8 发布；CAD 任务测试结果出人意料** — 在 CAD 任务上的测试结果显示出一些意外发现。 [来源-x](https://x.com/MikushRab/status/2060382378414010755)
- **感谢 DeepSeek 以开放研发降低 AI 成本** — 对 DeepSeek 通过开放研发降低 AI 成本的方式表示感谢。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqyl20/a_moment_of_thanks_for_deepseek/)
- **寻找 15 万美元以内、相当于 4×H100 的推理服务器** — 探讨构建既经济又高性能推理服务器的选择。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tr7b0n/if_you_had_150k_for_building_a_productionclass/)
- **HTML 成为 agent 聊天中绘图的主要“语言”** — HTML 正逐渐成为智能体对话中绘制图表的首选语言形式。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqt12p/use_html_as_the_primary_chat_language_for_your/)
- **开发者在代码中偷偷加入“数据核爆”提示，引发法律审查** — 这一“数据核爆”提示导致监管与合规方面的担忧。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trdnap/fed_up_with_vibe_coders_dev_sneaks_datanuking/)

---

*由 AI News Agent 生成 | 2026-05-29*