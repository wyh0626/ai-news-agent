---
title: "AI 日报 — 2026-05-09"
description: "ERNIE5.1提效，DeepSeekv4可运行，改错位提Claude。"
lang: "zh"
pairSlug: "ai-daily-2026-05-09"
---

# AI 日报 — 2026-05-09

> 覆盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. ERNIE 5.1 大幅降低预训练成本并提升性能

百度的 ERNIE 5.1 通过将总参数量压缩到大约三分之一、激活参数压缩到约一半，在与同级规模模型相比仅使用约 6% 的成本，就显著降低了预训练开销。它在智能体任务、知识基准测试、创意写作以及前沿推理方面都取得了领先表现，并在 Arena Search 搜索能力评估中名列前茅。该模型的发布表明可扩展 AI 的竞争正在加剧，也通过百度的平台带来更广泛的可用性。 [来源-x](https://x.com/ErnieforDevs/status/2052961073423405256)

### 2. 开源 1M 上下文 DeepSeek v4 Flash 在 Mac 本地运行

Antirez 发布了 ds4，这是一个针对 DeepSeek v4 Flash 的原生推理引擎，使其在 2-bit 量化下可使用 100 万 token 的上下文窗口，并将 KV cache 移至 SSD，从而可以在一台配备 128GB 内存的 MacBook Pro 上本地运行。这展示了在消费级硬件上运行前沿 AI 能力的可能性，并凸显出开源方案对云中心技术栈的挑战。该进展有利于更易获得的实验环境和边缘 AI 工作流。 [来源-x](https://x.com/garrytan/status/2052996691586932783)

### 3. Anthropic：教会 Claude「为什么错位是错的」能提升表现

Anthropic 报告称，仅用对齐行为示范来训练 Claude 并不够；效果最佳的干预方法是让 Claude 深入理解「为什么不对齐行为是错误的」。这体现了一种向对齐新方法的转变，即在模型中培养因果和规范性推理，有望带来更诚实可靠的 AI 系统。 [来源-x](https://x.com/AmandaAskell/status/2052928572810256748)

## 📰 重点报道

### LLM

- **Sakana AI 与 NVIDIA 共同开发更快的稀疏 Transformer：TwELL** — Sakana AI 与 NVIDIA 推出 TwELL 以及一个可融合多路稀疏 matmul 的 CUDA kernel，为拥有数百亿参数的稀疏 LLM 提供超过 20% 的加速，并显著节省显存与功耗；该成果将于 ICML 2026 上展示，并配套开源材料发布。 [来源-x](https://x.com/SakanaAILabs/status/2052909818709766259)

- **Qwen3.6-35B A3B 未审查 Native MTP Preserved 模型发布** — 开源的 Qwen3.6-35B A3B 未审查 Native MTP Preserved 模型发布，所有变体都完整保留 MTP 计数，可在 HuggingFace 上以 Safetensors、GGUF、NVFP4 和 GPTQ-Int4 等多种格式获取，体现出社区对保留 MTP 计数的强烈需求。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t7qfaq/qwen36_35b_a3b_uncensored_heretic_native_mtp/)

- **Hermes Agent 登顶 OpenRouter 全球 AI 应用榜** — Hermes Agent 在 OpenRouter 全部 AI 应用中跃居第 1 名，背后有近 1000 名贡献者参与；团队对支持者表示感谢，并征集新功能需求。 [来源-x](https://x.com/Teknium/status/2052907085684461833)

- **AI 重现 Schmidhuber 1990-2025 年 World Models 论文** — 一款 AI 编码助手复现了 Schmidhuber 从 1990 到 2025 年的 World Models 系列论文，实现了一个玩具环境以及完整的 VAE+RNN 世界模型；项目托管在 cybertronai/schmi。 [来源-x](https://x.com/hardmaru/status/2053147759428178315)

- **ds4 WebUI 面向开源 AI 服务器首发** — 面向 ds4.c AI 服务器的极简 Web UI 发布；演示环境为搭载 256GB 内存的 M3 Ultra；需注意的是，使用 Apple Silicon Mac 至少需要 128GB 内存；帖子中还附有 ds4.pinokio 仓库和相关讨论链接。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t8ho70/ds4_webui/)

- **特斯拉 FSD 使用 photon-count 重建实现夜视能力** — 特斯拉强调基于 AI 的 photon-count 重建方法，可在夜间和强眩光环境下超越人类 RGB 视觉，预示通过多模态成像方案提升自动驾驶感知能力的方向。 [来源-x](https://x.com/elonmusk/status/2053181971644416080)

- **OpenAI 征集下一代模型改进意见** — OpenAI CEO Sam Altman 面向公众征集关于下一代模型在能力、安全性和用户体验方面的改进建议，表明其正进入一个更加依赖开放反馈驱动的开发阶段。 [来源-x](https://x.com/sama/status/2053151542916894775)

## ⚡ 快讯速览

- **将 GPT-Realtime-2 集成进语音驱动的 CRM 工作流** — 一项新的 GPT-Realtime-2 集成方案旨在简化语音驱动的 CRM 工作流程。 [来源-x](https://x.com/OpenAIDevs/status/2053161503470366881)

- **下一代 Mythos 模型目标：运行 8 小时且成功率 80%** — Mythos 设定了长时间运行目标：连续运行 8 小时并保持 80% 成功率，凸显其在耐久性方面的改进方向。 [来源-x](https://x.com/kimmonismus/status/2053020462817448369)

- **Figure 为 AI 提供实体载体以实现具身能力** — 一个正在成形的概念，探索为 AI 提供实体“身体”，以解锁具身智能能力。 [来源-x](https://x.com/adcock_brett/status/2053234021182898234)

- **AI-DLC：面向 AI 编码代理的自适应工作流规则** — AI-DLC 提出一套自适应工作流规则，用于规范和管理 AI 编码代理的行为。 [来源-github](https://github.com/awslabs/aidlc-workflows)

- **AI-Trader 推出 100% 自动化的原生智能体交易系统** — AI-Trader 发布一套完全自动化、以智能体为核心的交易系统。 [来源-github](https://github.com/HKUDS/AI-Trader)

- **在 Strix Halo 上运行具有 100k 上下文的 Minimax 2.7** — 展示了在 Strix Halo 部署环境下支持超大上下文窗口的能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t8k6fg/running_minimax_27_at_100k_context_on_strix_halo/)

- **关于「研究 AI 生存风险是否反而会增加风险」的讨论** — 社区争论针对 AI 生存风险的研究是否可能在无意中提高实际风险暴露。 [来源-x](https://x.com/fabianstelzer/status/2052985234673553531)

- **被 Llama.cpp 各种 harness 搞晕了，有通用方案吗？** — 社区展开讨论，试图梳理和整合针对 Llama.cpp 的多种 harness 方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t8gb1e/i_am_overwhelmed_by_harnesses/)

- **在哪里能找到适用于本地 AI 模型的应用？** — 提供关于如何寻找适配本地部署 AI 模型的应用程序的指引。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t8b4sr/after_youve_setup_local_models_where_can_you_find/)

- **llama.cpp 何时会官方支持 MTP？** — 社区就 llama.cpp 何时正式支持 MTP 提出疑问并展开讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t7ur1f/how_long_for_llamacpp_official_support_of_mtp/)

- **Codex 任务已启动并完成，提振对 AI 未来的信心** — 一系列 Codex 任务的推进和完成，支撑了人们对 AI 工具生态未来发展的乐观预期。 [来源-x](https://x.com/sama/status/2053191344999604409)

- **Elon Musk 在回帖 Anthropic 话题时调侃 Yudkowsky「有锅」** — Musk 在一条关于 Anthropic 的讨论中，以玩笑方式谈到责任归因。 [来源-x](https://x.com/elonmusk/status/2052918813361090568)

- **「我对 Claude 的爆粗次数比对 Codex 更多」** — 一则戏谑式评论，对比了用户与 Claude 和 Codex 互动时的情绪反应。 [来源-x](https://x.com/theo/status/2052932424699630006)

- **Shel Silverstein 早在 1981 年就“预言”了 LLM 与幻觉** — 一条 Reddit 讨论指出，Silverstein 的作品中对 LLM 和「幻觉」现象展现出颇具前瞻性的洞见。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t7s9n4/shel_silverstein_predicts_llms_and_its/)

---

*由 AI News Agent 生成 | 2026-05-09*