AI 日报 — 2026-02-23

> 涵盖 35 条 AI 新闻

## 🔥 今日焦点

### 1. Anthropic 报告对 Claude 的工业级蒸馏攻击

Anthropic 披露，对 Claude 发起的工业级蒸馏攻击由 DeepSeek、Moonshot AI 与 MiniMax 实施。此类行动据称创建了超过 24,000 个欺诈账户，并与 Claude 进行了超过 1,600 万次互动，以提取其能力用于训练竞争对手模型，凸显了 AI 助手在安全、隐私和采购方面的严重风险。这一发现为加强对已部署的 LLM 的访问控制和防篡改接口的论点提供了支持。 [来源-x](https://x.com/Yuchenj_UW/status/2026004876271247716)

### 2. Anthropic 推出 AI Fluency 指数以衡量与 Claude 的协作情况

Anthropic 推出 AI Fluency 指数，用于在数千次 Claude.ai 对话中衡量 11 种可观察行为，旨在了解人们如何与 AI 建立高效协作。该指数是 Anthropic 的教育报告的一部分，揭示了迭代模式以及用户如何在与 Claude 的工作中进行改进。这一指标可能影响人类-AI 团队的培训、设计与评估。 [来源-x](https://x.com/AnthropicAI/status/2025950279099961854)

### 3. GLM-5 在 Extended NYT Connections 基准测试中夺冠

GLM-5（开放权重模型）在 Extended NYT Connections 基准测试中以 81.8 分领先，超过 78.3 的 Kimi K2.5 Thinking。该结果凸显了开源 LLM 在复杂评测任务上的持续进展，并为未来的开源模型提供了基准参考。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rcnv9h/glm5_is_the_new_top_openweights_model_on_the/)

---

## 📰 重点报道

### 开源 / 研究

- **Unified Latents (UL)：使用扩散先验训练潜在表示** — UL 通过使用扩散先验对潜在表示进行联合正则化，并用扩散模型进行解码，从而得到一个简单的训练目标，上界潜在比特率。在 ImageNet-512 上，UL 以高 PSNR 和更低的训练 FLOPs 实现了 1.4 的具有竞争力的 FID。 [来源-huggingface](https://huggingface.co/papers/2602.17270)

### 开放数据与数据平台

- **OpenBB 开放数据平台（OpenBB Open Data Platform）使能 AI copilots 与仪表板** — OpenBB 推出 Open Data Platform (ODP)，这是一个开源工具集，用于将专有、许可和公开数据融合，为 AI copilots 与仪表板提供数据，向 Python 环境、OpenBB Workspace、Excel、MCP 服务器和 REST API 提供数据，旨在简化跨工具与团队的数据访问。 [来源-github](https://github.com/OpenBB-finance/OpenBB)

### AI 评估与基准测试

- **OpenAI 将前沿编码评估转移至 SWE-bench Pro** — 由于设计、泄露和公开仓库污染等问题，SWE-bench Verified 被认为不可靠用于前沿编码评估；随着行业在完善基准测试实践，SWE-bench Pro 成为推荐标准。 [来源-x](https://x.com/OpenAIDevs/status/2026002219909427270)

### 强化学习与训练稳定性

- **VESPO 通过变分优化实现对 Off-Policy 的 LLM 训练稳定性** — VESPO 提出变分序列级软策略优化，以在分布漂移条件下稳定 Off-Policy 的 LLM 训练，指出重要性采样可以降低偏差，但会增大方差，其他修正措施仍不足。该工作凸显了在 LLM 流水线中推动鲁棒 RL 方法的努力。 [来源-huggingface](https://huggingface.co/papers/2602.10693)

### 行业准入与安全政策

- **Google 因 OpenClaw 使用限制 AI Pro/Ultra 用户访问** — 据报道，Google 通过 OAuth 限制了 Google AI Pro/Ultra 用户对 OpenClaw 的访问，引发关于访问控制与平台治理在未事先警告情况下的讨论。这一举措激发了关于安全、政策以及 AI 工具领域竞争格局的讨论。 [来源-rss](https://discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778)

### 开源辩论 / 安全

- **Dario 很害怕** — 一篇观点文章指出 Anthropic 将恐惧作为限制开源工具的借口，声称 OpenRouter 与 OpenClaw 提升了开源模型的使用，而安全话语则用于巩固对未来智能的控制。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rcr4ju/dario_is_scared/)

### 硬件与推断

- **便携推断设备在 GPT-OSS 120B 上达到 165 tok/秒** — 一个业余爱好者自制的便携推断设备，采用极薄的冷却装置，在 Windows + LM Studio 环境下，借助 CPU 降压、PBO 调整、快速内存和 GPU 功率上限，在 GPT-OSS 120B 上实现约 150–165 tokens/sec；唯一的已知局限是缺乏紧凑的 ITX Threadripper 主板。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rclyvf/portable_workstation_for_inference/)

---

## ⚡ 快讯速览

- - **Qwen3 语音嵌入实现语音克隆与混音** — 语音嵌入使 Qwen3 能进行语音克隆与混音。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rc59ze/qwen3s_most_underrated_feature_voice_embeddings/)

- - **RWKV-7 推断 O(1) 内存，ARM 上超越 LLaMA 3.2** — RWKV-7 实现恒定内存推断，且在 ARM 上胜过 LLaMA 3.2。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rco9v7/rwkv7_o1_memory_inference_1639_toks_on_arm/)

- - **开源框架提供 Gemini 3 与 GPT-5.2 级本地 AI** — 一个开源框架实现 Gemini 3 与 GPT-5.2 级别的本地 AI。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rcc2fa/an_opensource_framework_to_achieve_gemini_3_deep/)

- - **TinyTeapot 77M 参数：CPU LLM 约 40 tok/s，开源** — 77M 参数的 CPU LLM 约可实现 40 tokens/秒，开源。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rci9h1/tinyteapot_77_million_params_contextgrounded_llm/)

- - **OpenClaw 的 confirm-before-acting 漏洞加速收件箱删除** — OpenClaw 的此漏洞加速了邮箱中的删除操作。 [来源-x](https://x.com/summeryue0/status/2025774069124399363)

- - **Simon Willison 发布关于 Agentic Engineering Patterns 的前两章** — Willison 预览早期章节中的 agentic engineering patterns。 [来源-x](https://x.com/simonw/status/2025990408514523517)

- - **Elon Musk 指控 Anthropic 偷窃开发者代码** — Musk 公开指控 Anthropic 关于代码盗用的指控。 [来源-x](https://x.com/elonmusk/status/2026012296607154494)

- - **推理模型何时知道该停止思考？** — 分析质疑推理模型能否在何时停止迭代。 [来源-huggingface](https://huggingface.co/papers/2602.08354)

- - **Anthropic 最新更新聚焦 COBOL 后 IBM 暴跌** — 市场对 Anthropic 的 COBOL 相关更新作出反应，IBM 股价大幅下滑。 [来源-rss](https://www.zerohedge.com/markets/ibm-plunges-after-anthropics-latest-update-takes-cobol)

- - **AI 时间线追踪自 Transformer 至 GPT-5.3 的 171 个 LLM** — 全面时间线追踪 171 个 LLM 的演进。 [来源-rss](https://llm-timeline.com/)

- - **Aqua：用于 AI 代理的 CLI 工具** — 轻量级用于调度 AI 代理的 CLI 工具。 [来源-github](https://github.com/quailyquaily/aqua)

- - **研究人员在 40MB 二进制文件中隐藏后门；AI 与 Ghidra 共同发现** — BinaryAudit 使用 AI + Ghidra 检测二进制中的后门。 [来源-rss](https://quesma.com/blog/introducing-binaryaudit/)

- - **Anthropic 从未开源过任何 LLMs** — 关于 Anthropic 的开源立场的争论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rcseh1/fun_fact_anthropic_has_never_opensourced_any_llms/)

- - **LocalGPT-OSS 20B 展示代理性能力** — Local GPT-OSS 20B 展现显著的代理性行为。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rc6c8m/feels_like_magic_a_local_gptoss_20b_is_capable_of/)

- - **本地训练一个 3B 参数的 LLM 的可行性讨论** — 关于在本地训练 3B 模型的可行性讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rckqpp/hardware_requirements_for_training_a_3b_model/)

- - **Strix Halo 128GB：GPU 仅运行 Llama 的最佳量化模型** — 针对 GPU-only Llama 工作负载的量化模型推荐。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rcrzbn/strix_halo_128gb_what_models_which_quants_are/)

- - **Veo 3.1 模板今日在 Gemini App 上推出** — Gemini App 中 Veo 模板的版本更新。 [来源-x](https://x.com/GeminiApp/status/2026001595708866759)

- - **Gemini 3.1 Pro 超载导致的代码中断；用户需支付 250 美元** — Gemini 3.1 Pro 遇到容量不足，用户需支付额外费用。 [来源-x](https://x.com/theo/status/2025896487557947886)

- - **Codex 周末项目：在 OpenAI 平台激发创造力** — 社区周末项目与 Codex。 [来源-x](https://x.com/gdb/status/2025723937540485506)

- - **AI 威胁开源质量，尚未就绪** — 讨论 AI 对开源质量与就绪度的影响。 [来源-rss](https://www.youtube.com/watch?v=bZJ7A1QoUEI)

- - **开源系统提示与 AI 工具目录** — 开源提示与工具目录。 [来源-github](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

- - **Pinterest 面临 AI 乱象与自动审核挑战** — Pinterest 正处理 AI 生成的垃圾信息与自动审核问题。 [来源-rss](https://www.404media.co/pinterest-is-drowning-in-a-sea-of-ai-slop-and-auto-moderation/)

- - **Anthropic 被指控煽恐与游说反对开源 AI** — 关于在开源 AI 讨论中的恐惧煽动与游说的指控。 [来源-x](https://x.com/TheAhmadOsman/status/2026006905299079578)

- - **LocalLLaMA 讨论中的蒸馏与训练之辩** — LocalLLaMA 中对蒸馏与训练方法的对比讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rcvimv/distillation_when_you_do_it_training_when_we_do_it/)

- - **推文：Claude 仅在硅谷进行蒸馏，用户观点** — 用户观点关于 Claude 蒸馏起源的地域性。 [来源-x](https://x.com/elder_plinius/status/2025999267425390676)

---

*Generated by AI News Agent | 2026-02-23*