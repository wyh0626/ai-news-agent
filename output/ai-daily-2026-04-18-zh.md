---
title: "AI 日报 — 2026-04-18"
description: "Anthropic封禁60余Claude；新模胜Qwen；Code免费本地运行。"
lang: "zh"
pairSlug: "ai-daily-2026-04-18"
---

# AI 日报 — 2026-04-18

> 覆盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. Anthropic 一夜之间关闭 60 多名员工的 Claude 访问权限
Anthropic 突然为一个超过 60 人的整个组织关闭了 Claude 的访问权限，除了邮件通知外没有给出任何理由。若想申诉必须填写 Google Form，所有基于 Claude 搭建的集成、历史记录和工作流都被迫停用或暂停。此事件凸显了在关键业务流程上过度依赖单一 AI 供应商所带来的风险。[来源-x](https://x.com/minchoi/status/2045542832241262602)

### 2. Amodei：中国将在 12 个月内复刻 Mythos
Dario Amodei 预测中国将在一年内复刻 Mythos 的能力，这意味着其 AI 能力将快速提升。他强调 AI 发展没有任何放缓迹象，以此反驳“中国版 Mythos 落后”的疑虑。这一说法突出了全球 AI 竞赛的加速以及可能带来的地缘政治与科技政策格局变化。[来源-x](https://x.com/kimmonismus/status/2045550820159045871)

### 3. 新 18B「拼接 Frankenstein」模型在 44 项测试中击败 Qwen 3.6-35B-A3B
一个在 Hugging Face 发布的 18B Frankenstein 模型宣称，在 44 项测试中表现优于 Qwen3.6-35B-A3B，同时在单张 RTX 3060 上仅需 12GB 显存即可运行。该模型融合了 Opus 4.6 和 GLM-5.1 的推理能力，在中端 GPU 上可达每秒 66+ tokens，GGUF 体积为 9.8GB。其被描述为未进行额外训练的实验性模型，主要面向 12–16GB 显存用户。[来源-x](https://x.com/leftcurvedev_/status/2045449352827580602)

## 📰 重点报道

### Open Source & Local Deployment
- **Claude Code 在 MacBook 上 100% 本地运行且零费用** — Claude Code 现在可以在 Apple Silicon 上完全离线运行，通过一个轻量级 API 封装在本地对接 API，从而实现私有、零费用的实验。但这也带来了关于安全性、模型更新，以及对开源封装依赖等方面的问题。[来源-x](https://x.com/hasantoxr/status/2045444005375377491)
- **Craft Agents OSS：开源 AI Agent 平台** — 该项目提供了一个用于多任务 AI agent 的开源框架，支持会话共享并提供以文档为中心的 UI，采用 Apache 2.0 许可。[来源-github](https://github.com/lukilabs/craft-agents-oss)
- **Chrome DevTools MCP 让 AI Agents 控制浏览器** — 这个 MCP 服务器让 AI agents 能够驱动并检查一个实时运行的 Chrome 浏览器，支持高级调试和基于 Puppeteer 的自动化，不过同时也指出 MCP 客户端可以访问内容。[来源-github](https://github.com/ChromeDevTools/chrome-devtools-mcp)

### AI Agents & Tools
- **Ollama 0.21 新增 Hermes Agent 支持** — 此版本允许在 Ollama 内运行 Hermes Agent，扩展了跨平台 agent 的互操作性。[来源-x](https://x.com/NousResearch/status/2045304840645939304)
- **Prefill-as-a-Service 为下一代模型提供跨数据中心 KV Cache** — 该方案将 prefill/拆分能力扩展到跨数据中心和异构硬件环境，从而降低 token 成本并提升吞吐量；在 20 倍扩展实例上展示了 1.54× 吞吐提升以及 P90 TTFT 降低 64%。相关工作收录于 arXiv:2604.15039v1，并在 Reddit 上进行了讨论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sp216x/prefillasaservice_kvcache_of_nextgeneration/)

### Evaluation & Benchmarks
- **DR3-Eval 支持更真实的 Deep Research 评测** — 提出一个真实且可复现的基准，用于评估 Deep Research Agents 在多模态、多文件报告生成上的表现，评测使用真实用户材料。[来源-huggingface](https://huggingface.co/papers/2604.14683)
- **Qwen3.6-35B-A3B 解出 Qwen3.5-27B 无法解决的编程题** — 有用户经验反馈称，Qwen3.6-35B-A3B 能够解决 Qwen3.5-27B 曾经难以应付的编程任务，显示出 Qwen 系列的显著进步。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1soxyfi/qwen3635ba3b_solved_coding_problems_qwen3527b/)

## ⚡ 快讯速览

- **Grok 4.3 获得新一轮训练；4.4 将基于 1T 数据，预计 5 月发布。** — Grok 4.3 已完成训练升级，预计 4.4 将在 5 月以 1T 数据规模亮相。[来源-x](https://x.com/elonmusk/status/2045590599206875216)
- **用 NVIDIA AI 构建完全本地的 AI 助手** — NVIDIA AI 现已支持构建完全本地运行的 AI 助手，强调在设备端推理能力。[来源-x](https://x.com/ollama/status/2045303660264280561)
- **Codex 演进为用于 iOS App 构建的完整 Agent 化 IDE** — Codex 进一步扩展为支持 iOS 应用开发的 agent 化 IDE 工作流。[来源-x](https://x.com/gdb/status/2045375289560007029)
- **简历上写 PyTorch 或 JAX 被视为优秀 AI 候选人的标志** — 越来越多雇主在 AI 岗位简历筛选中关注 PyTorch/JAX 技能。[来源-x](https://x.com/fchollet/status/2045524796298101077)
- **Tracer-Cloud 开源 OpenSRE：自建 AI SRE Agents** — Tracer-Cloud 发布 OpenSRE，用于构建自定义 AI SRE agents。[来源-github](https://github.com/Tracer-Cloud/opensre)
- **T3 Code：面向 Codex 和 Claude 的极简 GUI** — 一个为 Codex/Claude 工作流设计的轻量级 GUI 工具。[来源-github](https://github.com/pingdotgg/t3code)
- **4B 或 8B 参数下的最佳编程模型？** — 社区讨论在较小参数规模（4B/8B）下的最佳代码模型选择。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1spc7k1/what_best_coding_model_at_4b_or_8b_parameters/)
- **10B 参数以下用于网页搜索的最佳本地 LLM** — 讨论在 10B 参数以下，适合执行网页搜索任务的本地 LLM 最佳选项。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sp6qy7/best_local_llm_for_web_search/)
- **LM Studio：CPU 线程池大小 vs 关闭 MoE Offloading 后的 Tokens/s** — 分析 LM Studio 中 CPU 线程数与 MoE offloading 配置对吞吐率的权衡。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1soz24h/lm_studio_cpu_thread_pool_size_vs_tks_with_some/)
- **Claude Design 设计效果良好，但出现数据丢失事故** — Claude 的设计产出受到好评，但一次数据丢失事故引发了用户担忧。[来源-x](https://x.com/theo/status/2045314903293182252)
- **波兰村民讨论 Claude 是否优于 Gemini** — 当地社区围绕 Claude 与 Gemini 的表现优劣展开讨论。[来源-x](https://x.com/MillionInt/status/2045547647889727868)
- **小型 LLM 的本地 Tool-Calling 在实践中真的可用吗？** — 社区围绕小型 LLM 在本地环境中进行 tool-calling 的可行性展开争论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sp631h/are_you_guys_actually_using_local_tool_calling_or/)
- **KIMI K2.6 即将发布** — 社区对 KIMI K2.6 的到来表示期待。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sp10oa/kimi_k26_soon/)
- **Claude 在高难度问题上表现吃力；用户呼吁支持 HLS 回放** — 有反馈称 Claude 在解决复杂问题时遇到困难，同时有人希望增加 HLS 回放功能。[来源-x](https://x.com/dejavucoder/status/2045371142811377722)

---

*由 AI News Agent 生成 | 2026-04-18*