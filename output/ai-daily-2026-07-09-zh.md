---
title: "AI 日报 — 2026-07-09"
description: "OpenAI 新品：ChatGPT Work、GPT-5.6、GPT-Live。"
lang: "zh"
pairSlug: "ai-daily-2026-07-09"
---

# AI 日报 — 2026-07-09

> 覆盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 发布 ChatGPT Work：跨应用任务的新型 Agent
OpenAI 推出 ChatGPT Work，这是一个由 Codex 和 GPT-5.6 驱动的 ChatGPT 新型 Agent，能够在不同应用和文件之间执行操作，持续跟进一个项目数小时，并将高层目标转化为完整成品。这标志着向持续化、目标驱动型 AI agents 转变，它们可以在多种工具之间自动化复杂工作流。[来源-x](https://x.com/OpenAI/status/2075274271845404744)

### 2. OpenAI 发布 GPT-5.6：前沿 AI 随雄心扩展
OpenAI 将 GPT-5.6 宣传为“能随你雄心扩展的前沿智能”，承诺每个 token 带来更高智能、每美元取得更佳性能，并在高需求任务中提供更强的按需能力。这一发布强化了 OpenAI 的路线：为企业负载推出高效率、高影响力的模型。[来源-x](https://x.com/sama/status/2075266471316615436)

### 3. GPT-Live 推向 ChatGPT Go、Plus、Pro
OpenAI 新的语音生成能力 GPT-Live 已全面推送至 ChatGPT Go、Plus 和 Pro，并正向免费用户逐步开放；用户需要更新应用并开启声音以使用语音交互。这将自然、免手操作的交互方式扩展到多个产品层级。[来源-x](https://x.com/OpenAI/status/2075019750569378007)

---

## 📰 重点报道

### Open Source & Local AI
- **TencentDB-Agent-Memory 提供本地长期 AI 记忆能力** — 通过四层级流水线为 AI agents 提供完全本地的记忆能力，可减少最多 61.38% 的 token 使用，相对提升 51.52% 的通过率，并在集成到 OpenClaw 后将 PersonaMem 准确率从 48% 提升到 76%。[来源-github](https://github.com/TencentCloud/TencentDB-Agent-Memory)
- **MiMo v2.5 成为快速却被低估的本地 LLaMA 模型** — 在一台配备 192GB 内存和 RTX 4090 的服务器上，MiMo v2.5 据称在推理性能上超越本地的 30B–400B 量级模型，表明为其配置一台专用服务器可获得最佳本地性能。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1us4gim/mimo_v25_is_underrated_feels_like_the_tokens_are/)
- **OpenMed 1.8 本地化：Android、iOS、浏览器端设备内去标识化** — 通过 OpenMedKit 为临床文本提供完全在设备端执行的去标识化，支持 Android/iOS/React Native 的桥接以及浏览器运行环境，实现零服务器调用，并兼容广泛的模型生态。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urt5o4/openmed_18_apache20_clinical_deidentification/)

### LLMs & Agentic AI
- **Muse Spark 1.1 通过 Meta API 推出 Agentic 编码模型** — Muse Spark 1.1 通过 Meta Model API 和 Meta AI 提供 agentic 与代码生成能力，以极低价格面向开发者，强调便捷调用与工具构建能力。[来源-x](https://x.com/finkd/status/2075218444056707458)
- **Elon Musk 承认 Anthropic 领先 AI，称赞 Mythos/Fable** — Musk 改口承认 Anthropic 在 AI 领域处于领先地位，称赞 Mythos 和 Fable，并暗示即将到来的 Mythos 2，同时强调对开放且具竞争性的访问格局的态度。[来源-x](https://x.com/elonmusk/status/2075278580955685036)

### AI for Science & Industry
- **OpenAI Deep Native Structural Reasoning？未列入顶级组别；此处仅作背景呈现。** — （Deep Native Structural Reasoning for Accurate Structure–Property Understanding）主张在生物学、化学和材料科学等领域中，整合立体化学、键合、对称性与能量学，以改进对结构-性质关系的理解，同时指出实现这种跨领域整合所面临的挑战。[来源-huggingface](https://huggingface.co/papers/2607.07708)

### AI Hardware & Inference
- **Puzzle-75B-A9B NVFP4 在 3×3090 上达到 132 t/s** — 通过高度缓存优化的配置，在三块 RTX 3090 GPU 上实现约 132 t/s 的吞吐（每路约 65 t/s），功耗约 500W，显示出以较低成本获得高吞吐 75B MoE 模型推理能力的一条可行路径。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uru9ja/nvidia_puzzle75ba9b_nvfp4_at_132_ts_on_33090_why/)

---

## ⚡ 快讯速览

- Scaling MoE Video Pretraining for Embodied Intelligence — 探索在具身智能视频预训练中扩展 Mixture-of-Experts 规模的方法。[来源-huggingface](https://huggingface.co/papers/2607.07675)
- Gemma 4 推出开源权重多模态 LLM 套件 — 提供开放权重的多模态 LLM 能力，便于研究与实验。[来源-huggingface](https://huggingface.co/papers/2607.02770)
- Obra's Superpowers: Agentic AI Coding Framework — 一个 agentic AI 编码框架，用于加速 AI 驱动的软件开发流程。[来源-github](https://github.com/obra/superpowers)
- Desktop Commander MCP 启用 AI 控制终端与文件 — 支持由 AI 驱动的终端操作和文件控制工具链。[来源-github](https://github.com/wonderwhy-er/DesktopCommanderMCP)
- GLM-5.2 开源 AI 引发安全担忧 — 开源的 GLM-5.2 模型在社区和媒体中引发安全风险讨论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urhzox/glm52_fearmongering_in_the_press/)
- 6x MI50 对比 6x P40：MiniMax M2.7 REAP 139B — 针对 139B 规模 REAP 模型的硬件对比测试，性能结果依赖具体配置与负载类型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urymln/6x_mi50s_96gb_vs_6_p40s_144gb_running_minimax_m27/)
- OpenMOSS MOSS-Transcribe-Diarize 0.9B：端到端多说话人转写 — 使用 0.9B 参数模型实现多说话人场景的端到端语音转写与说话人分离。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uru6wf/openmossteammosstranscribediarize_hugging_face/)
- Reasoning-Medical0.1-27B 微调 Qwen3.5-27B，自称超越 MedGemma — 一个医疗领域的 27B 微调模型，声称在相关任务上性能超过 MedGemma。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urni78/reasoningmedical0127b_qwen3527b_medical_finetune/)
- KoboldCpp v1.117 发布 — KoboldCpp 的最新版本更新，带来一系列改进和修复。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1us5p0b/koboldcpp_v1117_released/)
- Grok 4.5 获得正面评价 — 关于 Grok 4.5 的早期使用体验整体偏向积极。[来源-x](https://x.com/elonmusk/status/2075130137817825315)
- AI 成本优化：每任务 5.6 SOL 显示显著效率提升 — 针对 AI 工作流的单任务成本下降，突出多倍效率改进空间。[来源-x](https://x.com/sama/status/2075267201058426944)
- Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation — 在视觉-语言-动作（VLA）模型中引入双潜在记忆结构，以改进机器人操作任务表现。[来源-huggingface](https://huggingface.co/papers/2607.07608)
- 付费用 LLM？本地 Embeddings 与 Reranker 更划算 — 强调通过本地 embeddings 与 reranker 方案，可在保持效果的前提下降低对云端 LLM 的依赖与成本。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1us3li5/if_you_already_pay_for_an_llm_service_running/)
- 开发者讨论：Mistral Medium 3.5 128B Dense 表现如何 — 社区分享对 Mistral Medium 3.5 128B 致密模型的使用体验与评价。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urzsnk/devs_do_you_use_mistral_medium_35_128b_dense_and/)
- RTX GPU 无法从 FlashAttention-3/4 优化中获益 — 研究发现 RTX 系列硬件在某些 FlashAttention-3/4 优化上几乎没有性能提升。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urucz1/exploring_flashattention34_optimizations_on_rtx/)
- 将 Codex 变成 ChatGPT Desktop 是一次“失误” — 批评观点认为直接把 Codex 改造成桌面端 ChatGPT 的产品方向不佳。[来源-x](https://x.com/theo/status/2075312087723876556)
- Flash IQ4 XS GGUF with preserve_thinking — 围绕使用 preserve_thinking 选项的 IQ4 XS GGUF 量化方案的讨论与实验结果。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1urqd5i/step_37_flash_iq4_xs_gguf_with_preserve_thinking/)

---

*由 AI News Agent 生成 | 2026-07-09*