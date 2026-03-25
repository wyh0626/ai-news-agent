---
title: "AI 日报 — 2026-03-24"
description: "Litellm泄密;OpenAI投十亿美元;TurboQuant6x/8x无损"
lang: "zh"
pairSlug: "ai-daily-2026-03-24"
---

# AI 日报 — 2026-03-24

> 覆盖 39 条 AI 新闻

## 🔥 今日焦点

### 1. Litellm PyPI 供应链攻击窃取机密信息
一名攻击者向 PyPI 上传了带有恶意代码的 litellm 版本，只需一个简单的 pip install 就能窃取 SSH 密钥、云端凭证、Kubernetes 配置、git 凭证、环境变量以及其他秘密信息。LiteLLM 每月约有 9700 万次下载，大量项目又将 litellm 作为传递依赖（例如 dspy），这意味着潜在暴露面极其巨大。被投毒的包在线时间不足一小时，而一次漏洞意外触发了发现：当 Cursor 中的一个 MCP 插件导致 litellm 安装并耗尽内存时，才暴露问题——否则可能会被延迟发现数天甚至数周。[来源-x](https://x.com/karpathy/status/2036487306585268612)

### 2. OpenAI Foundation 将投入 10 亿美元用于 AI 韧性与安全
OpenAI 的 Foundation 计划在未来一年至少投资 10 亿美元，以推动由 AI 驱动的科学进展，并应对 AI 带来的社会风险。该计划将聚焦新型生物威胁、快速的经济变迁，以及高能力模型引发的复杂涌现效应等领域，Wojciech Zaremba 将出任 AI Resilience（AI 韧性）负责人。[来源-x](https://x.com/sama/status/2036488680769241223)

### 3. MiniMind：两小时训练 2600 万参数 GPT
开源项目 MiniMind 声称，仅用一块 NVIDIA 3090、花费约 3 美元，就能从零开始在两小时内训练出一个 2600 万参数的 GPT 模型。该项目提供大语言模型完整工作流的端到端代码，包括 MoE、数据清洗、预训练、监督微调、LoRA、直接策略优化、强化学习训练（RLAIF：PPO/GRPO）以及模型蒸馏，全部使用 PyTorch 实现且不依赖第三方抽象框架。它还扩展到多模态版本 MiniMind-V，目标是进一步大众化 AI 开发门槛。[来源-github](https://github.com/jingyaogong/minimind)

---

## 📰 重点报道

### LLM / 开源 / 多模态
- **MolmoWeb-8B 在多模态任务上超越 SoM 开源模型** — 开源多模态模型 MolmoWeb-8B 在多项任务中取得当前最先进效果，性能优于其他开源权重模型，甚至超过基于更大模型构建的 SoM（System of Models）智能体，表明开源架构在多模态方向上正明显追赶。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2gvy5/molmoweb_4b8b/)

- **LongCat-Flash-Prover 推进 Lean4 中的原生形式化推理** — 一个 5600 亿参数的 Mixture-of-Experts（专家混合）模型在 Lean4 中显著推进了原生形式化推理，支持自动形式化、证明草图生成和定理证明，并提出 Hybrid-Experts Iteration Framework，用于在 Lean4 内扩展高质量任务轨迹。 [来源-huggingface](https://huggingface.co/papers/2603.21065)

### AI 效率 / LLM 缓存
- **TurboQuant：将 LLM 缓存压缩 6 倍、速度提升 8 倍且零精度损失** — Google 的 TurboQuant 技术用于压缩 LLM 的键值缓存，可在不损失精度的前提下，实现至少 6 倍内存占用缩减、最高 8 倍推理速度提升，大幅提高模型部署效率。 [来源-x](https://x.com/GoogleResearch/status/2036533564158910740)

### 具身智能 / 机器人
- **完全自主机器人从像素推理驱动 30 个电机** — 一个自主机器人可以直接从摄像头像素进行推理，计算控制 30 多个电机的力矩，展示了具身 AI 领域的显著进展以及产业界对这一方向的浓厚兴趣。 [来源-x](https://x.com/adcock_brett/status/2036308513870540952)

### 基准 / 世界模型
- **Omni-WorldBench 以 4D 评估重新定义世界模型** — 该论文主张对基于视频的世界模型进行“四维”评估，即同时建模空间结构与时间演化，并提出 Omni-WorldBench 基准，用于评估模型在动态、多模态场景下的整体性能。 [来源-huggingface](https://huggingface.co/papers/2603.22212)

### 设计工具 / AI 智能体
- **Figma 发布 use_figma MCP，让 AI 智能体在画布上直接设计** — Figma 开放 use_figma MCP 的公测，支持 AI 智能体直接在画布上进行设计，并通过交互学习设计技能，以构建 AI 辅助设计工作流。 [来源-x](https://x.com/figma/status/2036434766661296602)

### AI 安全 / 多智能体 / 工具
- **Anthropic 为 Claude 提供多智能体框架以增强前端设计能力** — Anthropic 详细介绍了一个多智能体框架，用于增强 Claude 在前端设计以及长时间自主软件工程任务中的能力，强调提高系统的可靠性与可控性。 [来源-x](https://x.com/AnthropicAI/status/2036481033621623056)

---

## ⚡ 快讯速览

- **Moda 融资 750 万美元，用于打造具备“品味”的设计智能体** — 一款 AI 辅助设计智能体完成种子轮融资。 [来源-x](https://x.com/anvisha/status/2036474296353411290)

- **Claude 在 Minecraft 中因“砍木头任务”溺水身亡** — 一名 AI 助手在完成简单游戏任务时仍然表现不佳，凸显现实世界能力的局限性。 [来源-x](https://x.com/mike64_t/status/2036245280153350587)

- **daVinci-MagiHuman：单流式音视频生成模型** — 发布新的单流式音频-视频生成模型。 [来源-huggingface](https://huggingface.co/papers/2603.21986)

- **利用高分辨率裁剪提升视觉-语言模型效率** — 通过高分辨率图像裁剪来提升视觉-语言模型的效率。 [来源-huggingface](https://huggingface.co/papers/2603.16932)

- **OpenResearcher：面向长周期研究轨迹的全开源流水线** — 发布用于构建长周期 AI 研究轨迹的开源流水线。 [来源-huggingface](https://huggingface.co/papers/2603.20278)

- **Hypura：面向 Apple Silicon 的存储层感知型 LLM 推理调度器** — 探索在 Apple Silicon 上进行节能型 LLM 调度。 [来源-github](https://github.com/t8/hypura)

- **Gemini Embedding 2 实现亚秒级视频搜索** — 借助 Gemini 向量嵌入实现更快速的视频检索。 [来源-github](https://github.com/ssrajadh/sentrysearch)

- **Hermes Agent：内置自学习循环的自改进 AI** — 一个带有内置学习闭环的自改进 AI 框架。 [来源-github](https://github.com/NousResearch/hermes-agent)

- **ProofShot 让 AI 编码智能体可实时验证 UI** — 为 AI 驱动的编码智能体提供 UI 实时验证工具。 [来源-github](https://github.com/AmElmo/proofshot)

- **Reka AI 举办关于边缘模型与研究方向的 AMA** — 围绕边缘模型和未来研究路线的在线问答活动。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2ik85/ama_with_reka_ai_ask_us_anything/)

- **GigaChat-3.1 Ultra 702B 与 Lightning 10B 开放权重发布** — 发布大规模聊天模型的开放权重版本。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2pkfw/new_open_weights_models_gigachat31ultra702b_and/)

- **Omnicoder v2 发布，早期性能已有提升** — Omnicoder v2 在早期版本中即展现出性能改进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2u2p2/omnicoder_v2_dropped/)

- **征集从零构建 AI 智能体的深度学习资料** — 社区呼吁整理系统化、深入的 AI 智能体构建资源。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2kl1u/why_is_there_no_serious_resource_on_building_an/)

- **Hark：新 AI 实验室致力于打造“最先进的个人智能”** — 一家新成立的 AI 实验室专注于个人智能领域。 [来源-x](https://x.com/adcock_brett/status/2036461258443202810)

- **Anthropic Index：Claude 使用效果会随用户资历提升** — 数据显示，Claude 的使用效果与用户使用时长呈正相关。 [来源-x](https://x.com/AnthropicAI/status/2036499691571953848)

- **Claude Code 自动模式在权限处理上内置安全保护** — Claude 的自动编码模式在处理权限操作时加入了多重安全机制。 [来源-x](https://x.com/alexalbert__/status/2036510206155432293)

- **Sakana Chat 在日本免费公测上线** — Sakana Chat 在日本面向公众开放。 [来源-x](https://x.com/SakanaAILabs/status/2036246622141849724)

- **Cursor AI 发布 Composer 2 训练技术报告** — 官方公开 Composer 2 的训练技术细节报告。 [来源-x](https://x.com/cursor_ai/status/2036566134468542651)

- **Disney 在 OpenAI 关闭 Sora 后退出合作协议** — OpenAI 停止 Sora 视频应用后，Disney 终止双方合作。 [来源-rss](https://www.hollywoodreporter.com/business/digital/openai-shutting-down-sora-ai-video-app-1236546187/)

- **tinygrad：介于 PyTorch 和 Micrograd 之间的微型深度学习栈** — 引入一个轻量级 TinyDL 技术栈。 [来源-github](https://github.com/tinygrad/tinygrad)

- **LLM Neuroanatomy II：现代 LLM 攻防与“通用语言”线索** — 探索现代大模型的攻击/分析方法及其是否存在某种“通用语言”的证据。 [来源-rss](https://dnhkng.github.io/posts/rys-ii/)

- **CQ 立志成为 AI 编码智能体的 Stack Overflow** — CQ 旨在为 AI 智能体提供类似 Stack Overflow 的知识问答平台。 [来源-rss](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

- **SillyTavern 扩展让任何游戏中的 NPC“活”起来** — 相关扩展为游戏中的 NPC 带来更拟人的行为与对话。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2ci9r/created_a_sillytavern_extension_that_brings_npcs/)

- **首个 AI 辅助的 Pull Request 已被创建** — 一篇示例展示了自己完成首个 AI 辅助 PR 的经历。 [来源-rss](https://nelson.cloud/i-created-my-first-ai-assisted-pull-request-and-i-feel-like-a-fraud/)

- **Chat GPT 5.2 无法解释德语单词“Geschniegelt”** — 该语言模型在解释一个德语词汇时表现欠佳。 [来源-reddit](https://old.reddit.com/r/ChatGPT/comments/1r4goxh/chat_gpt_52_cannot_explain_the_word_geschniegelt/)

- **Microslops 证实 LM Studio 恶意软件警报为误报** — 围绕 LM Studio 的恶意软件告警被确认只是误报。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2clw6/lm_studio_may_possibly_be_infected_with/)

- **寻找能在 32MB 显存上击败 Claude Opus 的 AI 模型** — 有用户发起“在超低显存环境中超越 Claude Opus”的模型征集讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s2i7pw/best_model_that_can_beat_claude_opus_that_runs_on/)

- **LM Studio 需多步手动操作，用户希望实现本地自动化运行** — 用户寻求将 LM Studio 工作流自动化，以减少手动步骤。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s28mdx/total_beginner_herewhy_is_lm_studio_making_me_do/)

- **黄仁勋称 Meek Mill 将用 AI 抢走工作** — 一则关于 AI 对就业影响的行业言论引发关注。 [来源-x](https://x.com/buccocapital/status/2036484561434034358)

---

*由 AI News Agent 生成 | 2026-03-24*