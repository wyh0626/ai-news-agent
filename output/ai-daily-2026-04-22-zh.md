---
title: "AI 日报 — 2026-04-22"
description: "ChatGPT工作区代理推动工作流，谷歌以Gemini与TPU8t8i提升AI。"
lang: "zh"
pairSlug: "ai-daily-2026-04-22"
---

# AI 日报 — 2026-04-22

> 覆盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. 推出用于共享工作流的 ChatGPT Workspace Agents
OpenAI 发布了 ChatGPT workspace agents，这是一类可共享的智能体，能够在多种工具和团队之间处理复杂任务和长时间运行的工作流。该功能旨在简化跨工具协作，并在组织内自动化多步骤任务。[来源-x](https://x.com/sama/status/2047017964105597009)

### 2. Google Cloud 借助 Gemini Enterprise Platform 每分钟处理超 160 亿 tokens
Google Cloud 披露，其通过直接 API 使用每分钟处理的 tokens 数量已超过 160 亿，高于上一季度的 100 亿，同时还推出了 Gemini Enterprise Agent Platform 以及一个新的 “mission control”，用于构建、扩展、治理和优化智能体，并发布第八代 TPU。此举凸显了 Google 希望通过端到端工具链大规模承载企业级 AI 工作负载的战略。[来源-x](https://x.com/sundarpichai/status/2046930927482482789)

### 3. Google 发布 TPU 8t 和 8i：双芯片 AI 加速器
Google 推出 TPU 8t（训练）和 TPU 8i（推理），其中 8t 在单个 pod 上提供的算力几乎是 Ironwood 的三倍，而 8i 则可实现高吞吐、低延迟推理，以更具成本效益地扩展至数百万个智能体。该组合使硬件与 Google 的端到端 AI 栈保持一致，从软件到模型再到应用层形成闭环。[来源-x](https://x.com/Google/status/2046993420841865508)

---

## 📰 重点报道

### LLM 与评测基准
- **Qwen3.6-35B 搭配合适智能体在 Polyglot Benchmark 中表现出色** — 当与 Little-Coder 脚手架搭配使用时，Qwen3.6-35B 在 Polyglot benchmark 上取得了 78.7% 的成绩，跻身顶尖梯队，并与云端模型展开竞争；文中指出脚手架与模型的对齐问题是一个重要因素，也为未来基准设计提供了方向。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ssilc3/qwen3635b_becomes_competitive_with_cloud_models/)

- **Kimi K2.6 登顶 OpenRouter 编程榜单** — K2.6 位列 OpenRouter 编程能力排行榜首位，凸显其在代码生成方面的强劲表现，并进一步提升其在 AI 开发者社区中的关注度。[来源-x](https://x.com/Kimi_Moonshot/status/2046915283206709581)

### AI 安全与产业动态
- **Anthropic 遭遇 Claude Mythos 泄露，OpenAI 借势占优** — Claude Mythos 在 Discord 上被意外曝光，引发了对安全性和公众观感的担忧；与此同时，OpenAI 凭借 Image Gen 2、Codex 使用量增长以及关于后续版本的讨论而持续积累势头。[来源-x](https://x.com/kimmonismus/status/2046874230529180092)

### 多模态视觉与交互界面
- **Flipbook 展示从模型直接进行实时像素流式渲染** — 一个原型系统实现了从 AI 模型直接流式输出每一个像素，绕过传统 UI 渲染流水线，从而探索由 AI 主导的全新实时界面渲染范式。[来源-x](https://x.com/zan2434/status/2046982383430496444)

- **ChatGPT Images 2.0 生成与 Wikipedia 关联的二维码骰子** — 一则走红的多模态演示中，骰子每一个面上都包含可用的二维码，并分别链接到不同的 Wikipedia 词条，生动展示了跨模态创意玩法和能力边界。[来源-x](https://x.com/goodside/status/2046979039412318504)

### 工具与自动化 / 企业应用
- **OpenClaw Codex 授权问题修复，OpenAI 模型集成得到改进** — 新一轮迭代正在修复 OpenClaw 中 Codex 的认证问题，恢复了可靠的测试框架行为并提升了智能体表现；同时支持与 ChatGPT 订阅搭配使用，并预告下周将有更多更新。[来源-x](https://x.com/thsottiaux/status/2047000994354241562)

### 时尚科技与视觉
- **Tstars-Tryon 1.0：大规模逼真虚拟试衣系统** — 提出一个面向商业规模的虚拟试穿系统，被描述为稳健且高效，能够在极端姿态与光照条件下生成逼真的试穿效果，从而支持大规模服饰虚拟试穿场景。[来源-huggingface](https://huggingface.co/papers/2604.19748)

---

## ⚡ 快讯速览

- **AnyRecon 通过视频扩散实现任意视角 3D 重建** — 展示了如何将视频扩散模型的输出转换为任意视角的 3D 重建结果。[来源-huggingface](https://huggingface.co/papers/2604.19747)

- **TEMPO 将测试时训练扩展到大型推理模型** — 提出 TEMPO 方法，用于将测试时自适应扩展到大规模推理模型。[来源-huggingface](https://huggingface.co/papers/2604.19295)

- **Claude Context MCP 支持跨代码库的语义代码搜索** — Claude Context MCP 可在大型代码库中进行语义级代码搜索。[来源-github](https://github.com/zilliztech/claude-context)

- **RAG-Anything 发布集成 VLM 的多模态 RAG 框架** — 该多模态 RAG 框架集成视觉-语言模型，用于检索增强生成任务。[来源-github](https://github.com/HKUDS/RAG-Anything)

- **3.6-27B 发布后 Dense 与 MoE 性能差距缩小** — 随 3.6-27B 发布，致密模型与 Mixture-of-Experts 模型之间的性能差距正在明显缩小。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ssw45q/dense_vs_moe_gap_is_shrinking_fast_with_the_3627b/)

- **Qwen3 TTS 被低估，本地实时流式合成已实现** — Qwen3 TTS 已实现本地实时流式语音合成，凸显其在端侧语音合成上的高效表现。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ssugid/qwen3_tts_is_seriously_underrated_i_got_it/)

- **近期开源 LLM（2025 年 11 月–2026 年 4 月）综述** — 一篇梳理 2025 年末到 2026 年初发布的开源大模型的调研综述。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sskmhv/recent_open_models_from_last_6_months_nov_2025/)

- **Qwen 3.6-27B 大语言模型发布** — Qwen 3.6-27B 正式发布，进一步扩展了开源模型的可选范围。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ssl1xh/qwen_36_27b_is_out/)

- **小米发布 MiMo-V2.5** — 小米发布 MiMo-V2.5，进一步提升端侧多语言模型能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ssqkha/mimov25_has_released/)

- **CoInteract 支持物理一致的人物-物体交互视频合成** — CoInteract 在物理一致性的人体与物体交互视频生成方面取得进展。[来源-huggingface](https://huggingface.co/papers/2604.19636)

- **AgentSPEX：用于智能体的规格与执行语言** — 提出 AgentSPEX，用于对自主智能体进行形式化规格描述和执行控制。[来源-huggingface](https://huggingface.co/papers/2604.13346)

- **Microsoft 推出 AI Agents for Beginners 课程** — 一门面向入门者的教育课程，用于系统介绍 AI 智能体概念及实践。[来源-github](https://github.com/microsoft/ai-agents-for-beginners)

- **TrendRadar：AI 驱动的舆情与趋势监测工具** — 一个开源工具，用于追踪与 AI 相关的公众舆论与趋势走向。[来源-github](https://github.com/sansan0/TrendRadar)

- **为何 27B 模型可以在 Qwen 中击败 397B MoE** — 讨论为什么更小的致密模型在 Qwen 体系中能够超越规模更大的 MoE 模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1st11lp/forgive_my_ignorance_but_how_is_a_27b_model/)

- **Claude 的高需求正在考验供给能力约束** — 报道指出，Claude 的高需求正对其算力与服务供给造成压力。[来源-x](https://x.com/tszzl/status/2047007351266476397)

- **Anthropic 的 Claude 更新广受关注但 Bug 不少** — Claude 的新改动已经被广泛注意到，但由于问题较多而引发用户质疑。[来源-x](https://x.com/theo/status/2046765840477945942)

- **Claude Code 的 token 预算在一些岗位上已高于总薪酬** — 有用户调侃称，Claude Code 的 token 预算额度已经超过不少人的总薪酬水平。[来源-x](https://x.com/bryancsk/status/2046858559607238876)

---

*由 AI News Agent 生成 | 2026-04-22*