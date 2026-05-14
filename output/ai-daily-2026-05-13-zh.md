---
title: "AI 日报 — 2026-05-13"
description: "令牌叠加LLM预训练速2–3倍，世界模型对代理至关，Claude月度额度上线。"
lang: "zh"
pairSlug: "ai-daily-2026-05-13"
---

# AI 日报 — 2026-05-13

> 涵盖 17 条 AI 新闻

## 🔥 今日焦点

### 1. Token Superposition Training 将 LLM 预训练提速 2–3 倍

Token Superposition Training（TST，令牌叠加训练）在保持 FLOPs（计算量）相同的情况下，将标准 LLM 预训练速度提高了 2–3 倍，而且无需更改模型架构、优化器、分词器或数据。在训练的前三分之一阶段，它处理连续的 token bag（令牌袋），对输入 embedding 取平均并使用改写后的交叉熵损失；剩余阶段则恢复为普通的下一 token 预测。推理时的模型与常规预训练完全一致，该方法已在 270M、600M、3B 稠密规模以及 10B-A1B MoE 上验证有效，由 Nous Research 的 bloc97、gigant_theo 和 theemozilla 领导。[来源-twitter](https://x.com/NousResearch/status/2054610062836892054)

### 2. LeCun：世界模型是可靠 Agentic AI 的关键

Yann LeCun 认为，一个可靠的 agentic AI 系统必须具备世界模型，而当前的 LLM 并不具备这一点。他指出，LLM 无法在行动前预测自己行为的后果，因此称不上真正的智能。缺乏世界模型会严重限制这些模型在自主性和前瞻性方面的能力。[来源-twitter](https://x.com/haider1/status/2054446542757519717)

## 📰 重点报道

### LLM

- **Claude 付费套餐将提供可编程使用的月度额度** — 自 6 月 15 日起，Claude 的付费套餐将包含一笔专门用于程序化调用的月度额度，覆盖 Claude Agent SDK、`claude -p`、Claude Code GitHub Actions，以及基于 Agent SDK 构建的第三方应用。与此同时，社交媒体上也有提醒指出，在 Claude 中使用某些工具可能会触发使用量被折算为原来的 1/25，并以免费额度的形式呈现，实质上大幅削减了可用配额。[来源-twitter](https://x.com/theo/status/2054620998205624746)
- **AI 终结 LeetCode 面试，支持者为此叫好** — 一则基于 AI 的观点称，现代模型可以一次性解决 LeetCode 风格的面试题，从而终结长达十年的“背题式”编码面试。帖文高度评价 AI 的进步，并预见技术招聘方式将发生剧烈转变，传统面试算法题将逐步失去意义。[来源-twitter](https://x.com/Yuchenj_UW/status/2054611200621850727)
- **Qwen 3.6 Plus 限时在 Nous Portal 免费开放** — 阿里巴巴的 Qwen 3.6 Plus 现已在 Nous Portal 上限时免费提供。Nous Portal 可访问 300+ 模型，并将 tokens 与付费工具打包，方便用户进行统一配置与计费，同时重点展示了与 Hermes Agent 的集成能力。[来源-twitter](https://x.com/Alibaba_Qwen/status/2054397617015271738)
- **MCP-Cosmos 将世界模型注入 MCP，实现可预测的任务自动化** — MCP-Cosmos 通过将生成式 World Models（世界模型）集成进基于 MCP 的智能体，扩展了 Model Context Protocol，试图弥合任务规划与执行阶段环境动态之间的鸿沟。该框架旨在为 MCP 环境中的复杂任务提供长时间尺度的前瞻规划，同时在规划与预测性执行之间取得平衡。这项开放研究将 LLM、外部工具与环境建模对齐，以支持更强大的自主智能体。[来源-huggingface](https://huggingface.co/papers/2605.09131)

### AI Tools

- **Codex 使用内置浏览器跨视口测试应用** — Codex 现已能使用应用内浏览器，在多种视口尺寸下测试应用，控制设备工具栏并跨不同断点模拟点击。在长时间测试过程中，它会记录关键截图并在测试结束时集中展示，同时还能通过隐藏动画、以 1–2 倍加速运行来提升测试速度。注释系统也已优化，可更快发送且消耗更少 tokens。[来源-twitter](https://x.com/JamesZmSun/status/2054391975403774431)
- **AiToEarn：面向个人创作者的 AI 驱动内容营销** — AiToEarn 是一款面向 OPC（one-person companies，单人公司）、创作者和品牌的 AI 内容营销平台，帮助用户在各大平台上构建、发布、分发和变现内容。它支持包括基于 Docker 的私有部署在内的五种部署方式，并通过 MCP 与 OpenClaw、Claude、Cursor 等智能体集成，实现跨平台协作。最新更新包括 2026 内容市场、跨智能体的 MCP 支持、OpenClaw 集成，以及线下商家推广等功能。[来源-github](https://github.com/yikart/AiToEarn)

### Embodied AI

- **World Action Models：具身智能的下一前沿** — 虽然 Vision-Language-Action（视觉-语言-动作）模型具有良好的泛化能力，但在外部干预下，它们缺乏对世界动态的显式建模。World Action Models（WAMs，世界动作模型）将可预测的环境动态整合进动作生成过程，构成具身基础模型的新范式。这一新兴方向旨在在具身 AI 中统一感知、语言与行动能力。[来源-huggingface](https://huggingface.co/papers/2605.12090)

### Multimodal

- **AlphaGRPO 让统一多模态模型具备自反思推理能力** — AlphaGRPO 提出一个新的框架，将 Group Relative Policy Optimization（群体相对策略优化）应用到 AR-Diffusion 统一多模态模型（UMMs），在无需冷启动阶段的前提下提升多模态生成能力。它支持“推理型文本到图像生成”，通过推断用户隐含意图来生成图像，并实现“自反思式优化”，让模型能够自主诊断并纠正自身输出。[来源-huggingface](https://huggingface.co/papers/2605.12495)

## ⚡ 快讯速览

- **Anthropic 1 万亿美元 vs Google 4.5 万亿美元估值引发争论** — 一条推文将 Anthropic 的万亿美元估值与 Google 的 4.5 万亿美元估值进行对比，提出两种可能：要么 Anthropic 被高估，要么 Google 被低估。该帖将此描述为一则关于 AI 相对市值的“谜题”，并邀请大家进行分析。[来源-twitter](https://x.com/BoringBiz_/status/2054553947239567696)
- **OpenAI Codex 企业优惠：迁移即可获 2 个月免费使用** — OpenAI 正在为 Codex 推出企业级促销活动：符合条件、在 30 天内完成切换的客户，其新用户可获得 2 个月的 Codex 免费用量。帖文鼓励读者将此信息转给 CTO，以便整个团队迁移到 Codex 上。[来源-twitter](https://x.com/OpenAIDevs/status/2054586214112780518)
- **黄仁勋：需要更多 NVDA GPU，并启用 HLS 播放** — 黄仁勋发推称 Nvidia 需要更多 GPU，并提到要启用 HLS 播放。该帖突显了为了支撑 AI 与视频工作负载，对 Nvidia 硬件的旺盛需求，也折射出 AI 行业对 GPU 供给的考量。[来源-twitter](https://x.com/The_AI_Investor/status/2054420279955427336)
- **ToolCUA 推进 CUA 的 GUI-工具路径编排** — ToolCUA 探讨了 Computer Use Agents（计算机使用智能体）在什么情况下应坚持使用 GUI 操作、在什么情况下应切换到工具调用，以优化任务执行。它指出，高质量 GUI-工具交错轨迹的稀缺、以及收集真实工具数据的高成本和脆弱性，是阻碍最优规划的关键问题。该工作提出了实现 CUA 最优 GUI-工具路径编排的一系列步骤。[来源-huggingface](https://huggingface.co/papers/2605.12481)
- **权衡：AI 模型的速度、价格与智能水平** — 作者表达了对“没用上最聪明模型”的焦虑，即便那意味着更慢的性能。他建议在部署 AI 时，重点考虑价格/速度与价格/智能的权衡关系。该备注强调了在真实系统中平衡成本与性能的实际问题。[来源-twitter](https://x.com/sama/status/2054627102922797323)
- **Claude Code 所有套餐至 7 月 13 日周使用上限提升 50%** — Claude Code 将在 7 月 13 日前将每周使用限额提高 50%。这一提升适用于 Pro、Max、Team 以及基于席位计费的 Enterprise 用户。[来源-twitter](https://x.com/ClaudeDevs/status/2054639777685934564)
- **AI 进步常被忽视，即便模型在不断变强** — 一条推文指出，人们很难察觉到关于“模型已经足够聪明”和“进步速度”的相关判断往往会很快显得过时。该观点认为这是一种“会老得很快的看法”，并反映出公众感知往往滞后于 AI 的实际进展。[来源-twitter](https://x.com/tszzl/status/2054354571733205305)

---

*由 AI News Agent 生成 | 2026-05-13*