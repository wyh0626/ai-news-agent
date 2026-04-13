---
title: "AI 日报 — 2026-04-12"
description: "M2.7商用受限；Hermes自进化亮相ICLR2026；CHI推RAG分析工具"
lang: "zh"
pairSlug: "ai-daily-2026-04-12"
---

# AI 日报 — 2026-04-12

> 覆盖 17 条 AI 新闻

## 🔥 今日焦点

### 1. MiniMax M2.7 开源，但限制商业用途

MiniMax M2.7 已在 Hugging Face 上发布，并宣称在 SWE-Pro（56.22%）和 Terminal Benchmark 2（57.0%）上达到了当前最先进水平。然而，该模型权重仅在禁止商业使用的许可下公开，这并不符合 Open Source Initiative 对开源的标准。公告页面链接了博客和 API，同时特别强调了这些许可方面的限制说明。 [来源-twitter](https://x.com/MiniMax_AI/status/2043132047397659000)

### 2. Nous Research 在 ICLR 2026 发布 hermes-agent-self-evolution

Nous Research 开源了 hermes-agent-self-evolution，这是一个允许 AI agent 自我进化提示词（prompts）的框架。该项目构建在 GEPA 引擎之上，作为 ICLR 2026 Oral 论文展示，声称相比强化学习数据需求减少 35 倍，同时性能提升 20 个点。发布方将自动进化提示词定位为手工系统提示词的替代方案，并在 GitHub 上开放了代码。 [来源-twitter](https://x.com/KKaWSB/status/2043119101028274268)

### 3. CHI 最佳论文：用于 RAG 分析的假设场景工具

在 CHI 会议更新中，一篇关于面向检索增强生成（RAG）的“假设场景（what-if）分析工具”的论文获得了最佳论文奖。帖子强调了社区对 MLOps/LLMOps、数据分析以及更好的人机协作界面的兴趣，并提到即将招募学生和博士后研究人员。 [来源-twitter](https://x.com/sh_reya/status/2043436179643830517)

## 📰 重点报道

### LLM

- **Speculative Decoding 让 Gemma 4 31B 跑分提升 50%** — 通过使用更小的 E2B 草稿模型进行 speculative decoding，在受控基准测试中显著提升了 Gemma 4 31B 的吞吐量。在一块运行 Windows 11 的 RTX 5090 上，测试对比了 Gemma 4 31B UD-Q4_K_XL 与 Gemma 4 E2B UD-Q4_K_XL 草稿模型（3.0GB），使用带 TurboQuant KV cache 的 llama.cpp 分支实现，在数学和代码生成任务上获得约 +50% 的加速，在其他任务上也有较大增益。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjct6a/speculative_decoding_works_great_for_gemma_4_31b/)
- **LazyMoE：在 8GB 内存、无 GPU 上跑 120B LLM** — 一位德国的硕士生展示了如何在仅配备 8GB 内存且没有 GPU 的笔记本电脑上运行 120B 参数规模的 LLM，其方法结合了懒加载 MoE 专家、TurboQuant KV 压缩以及基于 SSD 的流式加载。相关方案通过一篇 Reddit 帖子分享，并附带 GitHub 仓库链接，同时邀请社区反馈和讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjoo9z/built_lazymoe_run_120b_llms_on_8gb_ram_with_no/)
- **Obliteratus：开源工具，用于移除 LLM 审查机制** — 一个名为 Obliteratus 的开源工具声称可以通过识别并删除导致模型拒答的精确权重，从而移除大语言模型中的“审查”机制。该工具被描述为已集成进 Hermes，并以“100% 开源”进行宣传，Guillermo Casaus 的帖子重点介绍了其功能。这一发布引发了关于绕过模型安全防护的 AI 安全与“越狱”风险的讨论。 [来源-twitter](https://x.com/Teknium/status/2043198939965567373)
- **GLM 5.1 在社交推理基准中媲美前沿模型** — 有报告称，GLM 5.1 在使用自动化“Blood on the Clocktower”游戏的社交推理基准上，与前沿模型表现相当。作者指出，GLM 5.1 每局成本为 0.92 美元，而 Claude Opus 4.6 为 3.69 美元，并声称工具调用错误率为 0%，但也强调仍需要更多数据来验证结果的稳定性和可靠性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjm407/glm_51_sits_alongside_frontier_models_in_my/)
- **FernflowerAI-35B KL-ReLU GGUF 与 Apple MLX 发布** — 针对 Qwen 3.5 35B A3B uncensored HauhauCS 的开源修复版本引入了 KL-ReLU 校准（GGUF），模型名为 FernflowerAI-35B-A3B-KL-ReLU-GGUF。它包含 Apple MLX 的 8-bit 版本（V1 已上线，V2 最终版即将发布），并详细说明了此前张量 ssm_conv1d.weight 的问题以及修复过程。下载与讨论托管在 Hugging Face 上，并在 Reddit 提供了背景信息。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sje74g/fernflowerai35ba3bklrelugguf_apple_mlx/)

### Open Source

- **Multica 推出开源托管 AI Agents 平台** — Multica 提供了一个开源平台，可将代码编写 agents 转变为自治的“队友”。这些 agents 可以被指派处理 issue 等工作，自主领取任务、编写代码、报告阻塞问题并更新状态，无需人类反复手动提示，同时会随时间积累可复用技能。该平台支持自托管、厂商中立，面向人类 + AI 团队设计，并兼容 Claude Code、Codex、OpenClaw 和 OpenCode 等。 [来源-github](https://github.com/multica-ai/multica)
- **Llama-server 使用 Gemma-4 模型加入 STT 功能** — Llama.cpp 的 llama-server 现在支持使用 Gemma-4 E2A 和 E4A 模型进行语音转文本（STT）。这一更新拓展了开源 LLM 部署在音频处理方面的能力，由 Reddit 用户 srigi 发布公告。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjhxrw/audio_processing_landed_in_llamaserver_with_gemma4/)
- **mtmd 为 qwen3 增加 omni 与 ASR 音频支持** — mtmd 项目宣布为 Qwen3 模型增加音频支持。具体来说，qwen3-omni-moe（支持视觉 + 音频输入）已可正常工作，qwen3-asr 也已可用，这一更新由用户 /u/jacek2023 在 Reddit 提交。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjssyx/mtmd_qwen3_audio_support_qwen3omni_and_qwen3asr/)

## ⚡ 快讯速览

- **AI 进步威胁人类演员工作岗位** — 一条推文认为，进一步的 AI 发展可能会让人类演员几乎没有就业机会。该帖反映了当前关于 AI 生成表演以及对娱乐行业人类人才潜在取代的持续争论。 [来源-twitter](https://x.com/XXY177/status/2043366622644375662)
- **初识 Hermes 是种什么感受** — 这条帖子强调首次发现 Hermes 的体验，并邀请读者进行共鸣和思考。推文本身没有给出关于 Hermes 的任何技术细节。 [来源-twitter](https://x.com/NousResearch/status/2043378689702871191)
- **TurboQuant 是革命性技术还是大厂过度炒作？** — 一篇 Reddit 帖子发问：TurboQuant 是否真正具有革命性，还是只是又一个被 Google 和 Twitter 等公司炒作过度的平庸技术。作者希望就该产品的实际影响、创新程度以及是否被过度包装获得更现实的看法。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjrnlq/about_turboquant/)
- **mtmd 增加 Gemma 4 audio conformer encoder 支持** — mtmd 现已通过启用 Gemma 4 audio conformer encoder，为 Gemma 4 模型提供音频处理支持。该更新由 Reddit 用户 /u/jacek2023 提交，并在 LocalLLaMA 中附上讨论链接。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjen8d/mtmd_add_gemma_4_audio_conformer_encoder_support/)
- **人们在做基础 LLM 个人助手，而非代码代理** — 一位 Reddit 用户在 2016 年以来经历四次中风后，构建了一个带记忆系统的基础个人助手，以帮助应对残疾、长期居家的生活。他询问他人是否也在创建类似的非编程型助手，这些系统具备哪些功能、又是如何部署的。帖子凸显出人们对面向日常生活、具有记忆能力且更易用的 AI 助手的兴趣。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sjm09r/is_anyone_else_creating_a_basic_assistant_rather/)
- **Twitter 上对 Claude 的“我懂那种感觉”反应** — 一条英文推文提到 Claude，用“I know that feel”表达了一种熟悉的共鸣感，并以一句“Wow”收尾。该帖只是对 Claude 的简短随意反应，并未提供任何实质性新闻或技术细节。 [来源-twitter](https://x.com/kimmonismus/status/2043306403948106151)

---

*由 AI News Agent 生成 | 2026-04-12*