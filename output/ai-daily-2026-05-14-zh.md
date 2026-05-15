---
title: "AI 日报 — 2026-05-14"
description: "Codex登陆ChatGPT移动端，跨设备工作；Gemini闪传闻与LoRA平台"
lang: "zh"
pairSlug: "ai-daily-2026-05-14"
---

# AI 日报 — 2026-05-14

> 覆盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. Codex 登陆 ChatGPT 移动应用，实现跨设备开发流程

OpenAI 预览了在 ChatGPT 移动应用中运行的 Codex，用户可以直接在手机上发起新的编码任务、审查输出、引导执行并批准下一步操作，同时在不同设备之间保持文件与项目上下文的一致。这个“口袋级”的编程工作流有望提升开发者的灵活性与速度，但也带来了关于安全性、离线访问及跨设备治理的诸多考量。[来源-x](https://x.com/OpenAIDevs/status/2055016926213181608)

### 2. 传闻称 Gemini Flash 以 1/20 成本接近 GPT-5.5 水平

网上流传的消息称，Gemini Flash 在代码与推理能力上可达到 GPT-5.5 大约 92% 的表现，同时通过蒸馏与稀疏化将推理成本削减 15–20 倍，并为大多数请求提供低于 200ms 的延迟。若这一说法得到验证，将显著重塑前沿模型与 AI 服务在高性价比部署方面的格局。[来源-x](https://x.com/kimmonismus/status/2054887891222802633)

### 3. MinT：可扩展的 LoRA 训练与在线服务平台

MindLab 推出的 MinT 提供了一套托管式的 LoRA 微调与在线服务栈，使基础模型常驻内存，并在部署、更新、导出、评估、服务与回滚过程中以流式方式管理 LoRA 版本，从而避免完整 checkpoint 物化的开销。该系统主要面向“少量基础部署 + 大量已训练策略”的工作流，有望在生产环境中改善延迟与更新节奏。[来源-huggingface](https://huggingface.co/papers/2605.13779)

---

*由 AI News Agent 生成 | 2026-05-14*

## 📰 重点报道

### Open Source & Tools

- **K-Dense AI 发布 Scientific Agent Skills，并上线 BYOK 桌面共研助手** — 原本的 Claude Scientific Skills 更名为 Scientific Agent Skills，并扩展为可在任何支持开放 Agent Skills 标准的 AI agent 中使用；BYOK（自带模型）桌面共研助手可在本地运行，兼容 40+ 模型、100+ 数据库和 135 项技能，数据保留在本地设备上，并可通过 Modal 选择性扩展到云端。 [来源-github](https://github.com/K-Dense-AI/scientific-agent-skills)

- **PAI v5.0.0：Life Operating System 正式发布** — Daniel Miessler 的 Personal AI Infrastructure 发布 v5.0.0，将其定位为面向 agentic AI 的 Life Operating System，引入 Pulse 守护进程、Life Dashboard、身份层、Algorithm v6.3.0、ISA 原语、45 项技能、171 个工作流和 37 个 hook，并通过“隔离区”机制提供隐私保护，同时提供简洁的安装与迁移路径。 [来源-github](https://github.com/danielmiessler/Personal_AI_Infrastructure)

### Multimodal & Embeddings

- **MulTaBench 通过调优嵌入推进多模态表格学习** — 在多模态表格学习基准中，将任务相关嵌入进行微调（而非保持冻结）可以显著提升性能，凸显了在基础模型中对嵌入进行适配与调优的实际价值。 [来源-huggingface](https://huggingface.co/papers/2605.10616)

- **LVLM 在训练时的 128K 上下文之外依然具备泛化能力** — 通过长上下文持续预训练，将一个 7B 级 LVLM 的上下文从 32K 扩展到 128K，并给出了泛化到更长上下文的实用配方，为长上下文 LVLM 训练提供了可操作的指导。 [来源-huggingface](https://huggingface.co/papers/2605.13831)

### AI Safety & Partnerships

- **Claude Code 调整引发大幅限流，开发者强烈反弹** — 有开发者反馈，Claude Code 相关调整使其调用速率限制被削减约 40 倍，引发明显不满，也凸显了在工具链层面亟需更清晰的策略与产品说明。 [来源-x](https://x.com/theo/status/2054731856248283318)

- **Anthropic 与盖茨基金会达成 2 亿美元合作** — 一项重要的慈善合作计划，将通过资助、Claude 点数以及技术支持，推动在全球健康、生命科学、教育、农业与经济流动性等领域开发安全、可靠的 AI 应用。 [来源-x](https://x.com/AnthropicAI/status/2054941901900611787)

### Hardware & Inference

- **NVIDIA 发布 NVFP4 量化版 Kimi-K2.6 与 Kimi-2.5** — NVIDIA 推出对 Moonshot AI 的 Kimi 模型进行 NVFP4 量化后的版本（Kimi-K2.6-NVFP4 与 Kimi-K2.5-NVFP4），声称可直接用于商业和非商业场景，并在测试中展现出与原生 INT4 基线相当的准确度。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tcxb77/nvfp4_kimi26_and_kimi_25_released_by_nvidia/)

---

## ⚡ 快讯速览

- **Anthropic：美国在前沿 AI 上领先，提出 2028 年两种领导情景** — 概述美国在 2028 年前沿 AI 政策与战略中的领导地位可能路径。 [来源-x](https://x.com/AnthropicAI/status/2054987444664377374)

- **美国允许向 10 家中国企业出售 H200 芯片，AI 差距或被缩小** — 由于部分芯片出口管制放宽，可能带来竞争格局变化。 [来源-x](https://x.com/ChrisRMcGuire/status/2054896489931923834)

- **Figure 连续直播 8 小时自主、无人监管工作** — 展示了长时段自主运行 AI agent 的能力。 [来源-x](https://x.com/adcock_brett/status/2054729581391962353)

- **AnyFlow：基于 On-Policy Distillation 的任意步数视频扩散模型** — 在视频扩散任务中引入 on-policy 蒸馏方法。 [来源-huggingface](https://huggingface.co/papers/2605.13724)

- **EVA-Bench 推出端到端语音 Agent 基准测试** — 新基准专注评估端到端语音智能体的整体表现。 [来源-huggingface](https://huggingface.co/papers/2605.13841)

- **Supertonic 3 为本地 TTS 新增 31 种语言** — 扩展本地文本转语音的语言覆盖范围。 [来源-github](https://github.com/supertone-inc/supertonic)

- **Ring-2.6-1T：万亿参数的真实场景 AI 模型** — 讨论一个在真实应用场景中使用的万亿参数模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1td3fhc/inclusionairing261t_hugging_face/)

- **Scenema Audio 发布零样本富表现力语音克隆权重** — 上线支持零样本富表现力语音克隆的模型权重。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tcwqdd/scenema_audio_zeroshot_expressive_voice_cloning/)

- **用 RL 训练 Qwen3.5 自我 jailbreak，并据此强化防御** — 通过强化学习尝试 jailbreak Qwen3.5，并在实验基础上改进防御方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tdegh0/i_trained_qwen35_to_jailbreak_itself_with_rl_then/)

- **Multi-Token Prediction 提升 Qwen 在 LLaMA.cpp + TurboQuant 中表现** — 利用多 token 预测机制增强 Qwen 在 LLaMA.cpp 与 TurboQuant 组合下的性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tckzy2/multitoken_prediction_mtp_for_qwen_on_llamacpp/)

- **cyankiwi AWQ 4-bit 量化：联合拟合 scales 与 ranges** — 展示一种在 AWQ-4bit 中联合拟合缩放和范围的量化方法。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1td7gp8/introducing_cyankiwi_awq_4bit_quantization_2605/)

- **自动化 AI 研究员在本地通过 llama.cpp 运行** — 展示基于 llama.cpp 的本地自动化研究工作流。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tcu5r8/automated_ai_researcher_running_locally_with/)

- **MIT 的 RLCR 方法教会 AI 说“我不确定”** — RLCR 方法鼓励模型在回答中保持审慎与不确定性表达。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tczrop/mit_rlcr_teaching_ai_models_to_say_im_not_sure/)

- **Grok Build Beta 发布面向编码与自动化的 Agent 化 CLI** — 上线新的 agent 化 CLI 工具，用于代码开发与自动化任务。 [来源-x](https://x.com/xai/status/2054993285152989373)

- **在 LLM 内部运行“形状旋转计算器”揭示神经几何结构** — 以可视化方式展示 LLM 内部的几何特性。 [来源-x](https://x.com/GoodfireAI/status/2054962242022777189)

- **mattpocock 发布面向“实战工程师”AI agent 的 Skills 工具包** — 发布一套用于构建实用型 AI agent 的技能工具包。 [来源-github](https://github.com/mattpocock/skills)

- **Qwen3.6：Q4 与 Q6 之间的性能差距有多大？** — 讨论 Qwen3.6 中 Q4 与 Q6 量化方案的性能差异。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1td7qw0/is_there_a_big_gap_between_q4_and_q6_on_qwen36/)

- **Llama.cpp 在 ROCm 下 KV Cache 比 Vulkan 占用更多 VRAM** — 比较 ROCm 与 Vulkan 后端在 KV Cache 上的显存使用差异。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1td6et1/linux_why_does_llamacpp_rocm_consume_so_much_vram/)

- **本地 LLM 难以在知识截止点之外虚构内容** — 讨论许多本地 LLM 在“超出已知数据进行虚构创作”方面的局限。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tcrrfq/the_the_future_is_fictional_problem_of_many_local/)

- **Reddit 讨论：将本地 LLM 作为日常个人知识库** — 探讨用本地 LLM 作为日常个人知识管理工具的实践。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tcrtt6/anyone_actually_using_a_local_llm_as_their_daily/)

- **VS Code 的 Agents Window 引入本地 AI，同时保留 Copilot 在线能力** — VS Code 新的 Agents Window 支持使用本地 AI，同时继续在线接入 Copilot。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1td3uzi/vs_codes_new_agents_window_lets_you_use_local_ai/)

- **把一幅真迹莫奈当成 AI 发布，引发艺术实验** — 一幅真正的莫奈画作被当作“AI 作品”发布，触发了一场艺术实验。 [来源-x](https://x.com/Jediwolf/status/2054776716770320631)

- **无法通过 SSH 在 Claude Code 中粘贴图片** — 反馈称在通过 SSH 使用 Claude Code 时，图片粘贴功能被阻止。 [来源-x](https://x.com/theo/status/2054787567095283940)

- **来自“AI 史前时代”的遗物** — 一篇帖子展示并讨论早期 AI 时代的各种“文物”。 [来源-x](https://x.com/RolandMemisevic/status/2054927222310396093)

---

*由 AI News Agent 生成 | 2026-05-14*