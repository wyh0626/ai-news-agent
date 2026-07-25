---
title: "AI 日报 — 2026-07-24"
description: "Claude Opus 5 首发，半价，NVIDIA 倡导开源，黄谈蒸馏。"
lang: "zh"
pairSlug: "ai-daily-2026-07-24"
---

# AI 日报 — 2026-07-24

> 共收录 18 条 AI 新闻

## 🔥 今日焦点

### 1. Claude Opus 5 正式发布，以半价逼近 Fable 5

Anthropic 发布 Claude Opus 5，将其定位为一个深思熟虑、具有主动性的模型，据称在能力上接近 Fable 5 等前沿模型，但价格约为其一半。如果早期基准测试结果能保持，Opus 5 可能会加剧价格与性能的竞争，并让更多人能够使用顶级 AI。此举也让安全与治理的讨论进一步升温，买家在评估时必须在能力与风险之间权衡。[来源-x](https://x.com/kimmonismus/status/2080709519424766199)

### 2. NVIDIA 联署公开信：为何开放模型至关重要

NVIDIA 发布并签署一封公开信，主张开放模型对于安全、网络安全、快速创新以及广泛的 AI 发展至关重要。信中认为，AI 将重塑每一个行业，并由多国共同构建，因此需要前沿开放模型与前沿闭源模型并存的混合格局。附带的 PDF 提供了更深入的论证和政策背景。[来源-x](https://x.com/JensenHuang/status/2080643682408321103)

### 3. 黄仁勋谈 AI 蒸馏：开源与闭源模型之争

在接受 Axios 采访时，Jensen Huang 讨论了蒸馏问题，认为 AI 必须持续从人类、其他 AI 以及多元知识源中学习。他指出，互联网未来可能大部分内容都由 AI 生成，这意味着 AI 系统将从其他 AI 中进行知识蒸馏。他也探讨了开源模型开发者是否应从闭源模型中蒸馏能力，凸显这一话题在行业内持续引发争论。[来源-x](https://x.com/rohanpaul_ai/status/2080526596847587839)

---

*由 AI News Agent 生成 | 2026-07-24*

## 📰 重点报道

### LLMs & Benchmarking

- **Fugu-Ultra v1.1 发布，基准成绩与能力显著提升** — Fugu 系列的升级带来了更强的基准表现（尤其是在 ProgramBench 和 Terminal Bench 2.1 上），同时编码与 Agent 能力也有所增强，而价格保持不变。[来源-x](https://x.com/SakanaAILabs/status/2080448772778373586)
- **GPT-5.6 Pro 被称为应对高难度任务的顶级模型** — 有观点称 GPT-5.6 Pro 是处理困难任务时“最聪明”的模型，排名高于 Fable 5 Ultracode 和 GPT-5.6 Sol Ultra，不过整体产品线被形容为“令人困惑”。[来源-x](https://x.com/sama/status/2080683119959757243)

### Hardware & Training

- **SLAI T-Rex：在 Ascend SuperPOD 上进行全参数后训练** — 对 MoE 模型进行全参数训练，暴露出系统瓶颈（如内存压力、通信无法充分重叠等）；在 Ascend 上结合 DeepSeek-V4 负载进行的硬件感知优化，展示了大规模训练在该平台上的可行性。[来源-huggingface](https://huggingface.co/papers/2607.20145)

### Embodied AI & Multimodal

- **ReferTrack 实现 EVT 场景中的“先指代再跟踪”** — 该方法主张先解析目标指代再进行跟踪，以便让推理过程与显式检测结果对齐，从而弥补现有依赖潜在表征的视觉-语言-动作策略在精确指代和跟踪方面的不足。[来源-huggingface](https://huggingface.co/papers/2607.20061)

### Open Source Tools & Productivity

- **ego-lite 浏览器为你与 AI Agent 提供并行浏览体验** — 这款浏览器专为人类与 AI agent 同时使用而设计，agent 在独立的 Spaces 中运行，而你的标签页保持私密；目前已上线 macOS 版本，并规划 Windows/Linux 支持；仓库中提供演示与安装步骤。[来源-github](https://github.com/citrolabs/ego-lite)

### Cheap, Fast Tool-Use Models

- **AntLing-3.0-flash：面向工具调用、廉价且高速的 AI 模型** — 这一 124B 模型专注于工具调用执行，而非重型推理；目前仅通过 OpenRouter API 提供，并在 8 月 3 日前可免费使用，这也体现出中国实验室在推出“便宜又快”的工具型模型方面的趋势。[来源-reddit](https://www.reddit.com/r/DeepSeek/comments/1v54ct3/chinese_labs_keep_shipping_cheap_fast_models_ants/)

### Open Weighting & Safety Advocacy

- **美国科技公司在公开信中呼吁支持 Open Weighting 模型** — 该信主张 Open Weighting 模型对于健康的 AI 生态至关重要，并警告称如果完全依赖封闭式 AI 模型可能会带来系统性风险与创新受限的问题。[来源-reddit](https://www.reddit.com/r/DeepSeek/comments/1v5c12w/big_news_american_technology_company_issued_an/)

---

## ⚡ 快讯速览

- Anthropic：停止突出 Claude 人设，转而专注扩展上下文窗口 — [来源-x](https://x.com/johnennis/status/2080513411037741252)
- AREX：面向深度研究的递归自我改进 Agent — [来源-huggingface](https://huggingface.co/papers/2607.21461)
- 删除了 80% Claude Code 提示词后的经验教训 — [来源-x](https://x.com/trq212/status/2080710971228918066)
- K12-KGraph 构建对齐课程体系的知识图谱，用于教育场景 LLM — [来源-huggingface](https://huggingface.co/papers/2605.09635)
- Visual Contrastive Self-Distillation 通过输入条件消除非对称性 — [来源-huggingface](https://huggingface.co/papers/2607.21556)
- Earthtojake text-to-cad 推出 AI CAD Agent 能力库 — [来源-github](https://github.com/earthtojake/text-to-cad)
- Harper：Automattic 推出的离线、隐私优先 Rust 语法检查工具 — [来源-github](https://github.com/Automattic/harper)
- DeepSeek CEO：6 倍利润上限与开源政策 — [来源-reddit](https://www.reddit.com/r/DeepSeek/comments/1v4waf4/deepseeks_ceo_says_6x_profit_is_their_restraint/)

---