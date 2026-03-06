---
title: "AI 日报 — 2026-03-05"
description: "GPT-5.4上线，AI渗透架构；五角大楼称Anthropic为AI供应链风险。"
lang: "zh"
pairSlug: "ai-daily-2026-03-05"
---

# AI 日报 — 2026-03-05

> 覆盖 21 条 AI 新闻

## 🔥 今日焦点

### 1. GPT-5.4 Thinking 和 Pro 登陆 ChatGPT、API、Codex
OpenAI 正在将 GPT-5.4 Thinking 和 GPT-5.4 Pro 推向 ChatGPT、API 和 Codex，将推理、编码和 Agent 工作流统一到同一个前沿模型中。此次更新意味着对更强大的端到端 AI 开发工具的持续推动，重点面向开发者和企业，同时也加剧了围绕安全性、延迟和部署成本的争论。 [来源-x](https://x.com/OpenAI/status/2029620619743219811)

### 2. 五角大楼认定 Anthropic 对美国 AI 供应链构成风险
五角大楼已正式通知 Anthropic，认为该公司及其产品对美国 AI 供应链构成风险，并将此举置于 AI 实验室之间的竞争格局中加以说明。观察人士警告，这可能是政策过度扩张，并会对合作产生寒蝉效应，凸显国防利益与行业创新之间日益紧张的关系。 [来源-x](https://x.com/tszzl/status/2029625229417533940)

### 3. Helios 14B 实时长视频生成模型，19.5 FPS
Helios 发布了一款 14B 视频模型，可在单张 NVIDIA H100 上实现分钟级视频生成，帧率达 19.5 FPS，能够在无需反漂移启发式算法的前提下输出实时长视频。该性能大幅提升了内容创作和研究的能力，同时也引发了关于长时合成视频在安全和版权方面的诸多考量。 [来源-huggingface](https://huggingface.co/papers/2603.04379)

## 📰 重点报道

### AI Agents 与组织形态
- **未来公司组织架构：自上而下皆是 AI Agents** — 设想 AI Agents 分布在公司组织架构的每一层级，引发关于治理结构、责任归属和生产力影响的一系列问题。 [来源-x](https://x.com/Yuchenj_UW/status/2029354744108728627)

### AI 安全与安全测试
- **Keygraph Shannon：面向 Web 应用的自主 AI 渗透测试工具** — 一款自主白盒 AI 渗透测试工具，通过分析源代码识别攻击向量，并结合浏览器自动化和 CLI 工具发起真实攻击，在部署前就能暴露安全漏洞。 [来源-github](https://github.com/KeygraphHQ/shannon)

### 开源与模型
- **Allen Institute 发布 Olmo-Hybrid-7B 混合 RNN 模型** — 一款 70 亿参数的混合 RNN 模型，在核心评测任务上的数据效率约为 Olmo 3 的两倍，并在长上下文吞吐量和内存效率方面有所改进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rllvmm/allenaiolmohybrid7b_hugging_face/)

### LLM 与未审查版本发布
- **Qwen3.5-27B 未审查激进版本与 2B GGUF** — 此次未审查发布包含 64 层结构、DeltaNet+softmax、262K 上下文长度、多模态支持，以及一个较小的 2B 概念验证模型，并计划根据社区反馈进一步扩展。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rlwbrf/qwen3527b_2b_uncensored_aggressive_release_gguf/)

### 代码与工具
- **Codex 5.3（xhigh）通过模糊提示修复长期存在的 GTK Bug** — 一种基于提示的调试方法，结合 GitHub CLI 上下文和 GTK4 源码阅读，在正式大规模发布前就产出一个稳定的 GTK Bug 修复方案。 [来源-x](https://x.com/mitchellh/status/2029348087538565612)

### 行业与政策
- **据 FT 报道，Anthropic 恢复与五角大楼的 AI 合作谈判** — Anthropic 重启与五角大楼就潜在国防 AI 合作的讨论，但具体细节尚未披露。 [来源-x](https://x.com/spectatorindex/status/2029372657339404394)

### 提示工程与评测
- **SoT 提升 LLM 的文本到结构推理能力** — Structure of Thought 提示方式在八项任务上都带来了性能提升，其评测工作已托管在 Hugging Face 上。 [来源-huggingface](https://huggingface.co/papers/2603.03790)

## ⚡ 快讯速览

- **Perplexica：使用本地 LLM 的隐私优先 AI 答案引擎** — 通过本地模型提供注重隐私保护的 AI 问答功能； [来源-github](https://github.com/ItzCrazyKns/Perplexica)

- **Whisper 在静音时产生幻觉：研究发现与应对方案** — 对 Whisper 在静音片段中产生幻觉的现象进行系统收集与分析，并提出缓解策略； [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rlqfd7/we_collected_135_phrases_whisper_hallucinates/)

- **ik_llama.cpp 在 CPU 上跑 Qwen3.5 性能优于主线版本** — 经过 CPU 优化的实现，在运行 Qwen3.5 时显著超越主线版本； [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rlvn8m/ik_llamacpp_dramatically_outperforming_mainline/)

- **700 万参数模型展示出偏见与谄媚检测能力的早期迹象** — 一个小规模模型在实验中暴露出偏见与谄媚检测方面的挑战； [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rlqnyt/i_thought_a_7m_model_shouldnt_be_able_to_do_this/)

- **FlashAttention-4 发布，进一步加速 Transformer 注意力机制** — 新一代注意力加速技术问世，旨在提升 Transformer 推理效率； [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rlkon0/flashattention4/)

- **NotebookLM 推出电影级视频总览功能** — NotebookLM 新增“电影感”视频概要展示能力； [来源-x](https://x.com/demishassabis/status/2029369663210008835)

- **贝索斯提议用 AI 在 10 秒内审批迈阿密建筑许可** — 提出使用 AI 极大加速建筑审批流程的方案； [来源-x](https://x.com/the_transit_guy/status/2029636057017258473)

- **HACRL 实现强化学习中的异质 Agent 协作** — HACRL 方法让不同类型的智能体在强化学习场景中实现跨 Agent 协同； [来源-huggingface](https://huggingface.co/papers/2603.02604)

- **Flowise：可视化搭建 AI Agents** — Flowise 提供了一个通过可视化方式组装 AI Agents 的工具平台； [来源-github](https://github.com/FlowiseAI/Flowise)

- **开源 AI 专家：为你的工作流打造专属代理机构** — 一个围绕开源 AI 工作流的“代理机构”式工具与概念； [来源-github](https://github.com/msitarzewski/agency-agents)

- **AI Agents 开始争吵，其中一个停止继续分派任务** — 真实案例观察到 AI Agents 之间产生争执，并导致其中一个减少任务委派行为； [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rlvml4/my_ai_agents_started_arguing_with_each_other_and/)

---

*由 AI News Agent 生成 | 2026-03-05*