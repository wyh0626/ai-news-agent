---
title: "AI Daily — 2026-02-17"
description: "LLM 技术进展 · 开源模型与工具链 · 多语言与多模态"
pubDate: "2026-02-17"
category: "daily"
lang: "en"
pairSlug: "ai-daily-2026-02-17"
---

> A total of 16 AI-related news items were collected

## 🔥 Top Stories

### 1. High Internal Fidelity in LLMs: Using Probes to Reduce Hallucinations
Latest research shows that LLMs' internal encoding of truth is more reliable than their outputs. GoodfireAI's related paper puts this finding into practice: training probes at model activation layers to detect hallucinations, and using probe scores as reinforcement learning rewards to reduce hallucinations. This approach promises to improve intrinsic control of truth and reduce the spread of misinformation. [Source-x](https://x.com/OrgadHadas/status/2023596564443226313)

### 2. Qwen3.5NVFP4 Goes Live (Blackwell)
Qwen3.5NVFP4 (Blackwell) goes live, using NVIDIA Model Optimizer to quantize the model to FP4, checkpoint around 224GB, total parameters 17B, and released under the Apache 2.0 license. The article also mentions Speculative Decoding and built-in multi-token prediction head, suitable for lower-concurrency scenarios. [Source-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r77fz7/qwen35_nvfp4_blackwell_is_up/)

### 3. Daily Mixed Use of Opus and Codex
A blogger compares and shares the daily mixed usage of Opus and Codex, emphasizing their complementarity and trade-offs in real-world work, providing guidance for selection. For developers, this is instructive for choosing applications for different tasks. [Source-x](https://x.com/theo/status/2023729264256782601)

## 📰 Featured

### LLM 技术进展
- **High Internal Fidelity in LLMs: Using Probes to Reduce Hallucinations** — The latest research shows that LLMs' internal encoding of truth is more reliable than their outputs. GoodfireAI's related paper puts this into practice: training probes at model activation layers to detect hallucinations, and using probe scores as reinforcement learning rewards to reduce hallucinations. [Source-x](https://x.com/OrgadHadas/status/2023596564443226313)
- **Qwen3.5NVFP4上线** — Qwen3.5NVFP4 (Blackwell) goes live, using NVIDIA Model Optimizer to quantize the model to FP4, checkpoint around 224GB, total parameters 17B, and released under the Apache 2.0 license; the article mentions Speculative Decoding and built-in multi-token prediction head, suitable for lower-concurrency scenarios. [Source-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r77fz7/qwen35_nvfp4_blackwell_is_up/)
- **每日混用Opus与Codex** — A blogger compares and shares the daily mixed usage of Opus and Codex, emphasizing their complementarity and trade-offs in real-world work, providing selection guidance. [Source-x](https://x.com/theo/status/2023729264256782601)

### 开源模型与工具链
- **ACE-Step 1.5 稳定版发布** — ACE-Step team released stable version v0.1.0, adding VRAM detection and automatic model selection/optimization to improve compatibility with low-VRAM GPUs. Also optimized one-click startup script, expanded support for AMD and Intel GPUs, and fixed several bugs and small improvements. [Source-x](https://x.com/acemusicAI/status/2023707545094025227)
- **DAG优化网页代理提效20%** — The study proposes WebClipper, modeling the search process of web proxies as a state graph and pruning it to a minimal directed acyclic graph, thereby reducing tool-call iterations by about 20% without sacrificing accuracy. It also introduces the F-AE Score to evaluate the trade-off between accuracy and efficiency of the proxy trajectory. Training on refined and pruned trajectories can enable the agent to form more efficient reasoning from the start, thereby lowering costs. [Source-x](https://x.com/dair_ai/status/2023554252548051409)

### 多语言与多模态
- **Tiny Aya 小模型潜力** — Cohere Labs推出 Tiny Aya，小型语言模型展现潜力。相比先前的 Aya 版本和同等规模的模型，Tiny Aya 在多语言设计上更具竞争力，证明聚焦多语言研究可在不显著扩大规模的情况下实现更高性能。 [Source-x](https://x.com/Cohere_Labs/status/2023699487110148523)
- **字节跳动发布 Seed-2.0 模型** — 字节跳动宣布 Seed-2.0，在代理、推理和视觉理解等方面较 Seed-1.8 取得显著进展，且未进行蒸馏。目前全球化部署将很快推进。 [Source-x](https://x.com/TsingYoga/status/2023764275874197964)

### 行业应用与安全
- - Note: There are no items categorized under Industry Applications & Security in this issue's Featured section; if you'd like to focus on this direction, we can adjust and add.

## ⚡ Quick Bites

- **Podscript Transcription Tool** — Developer timf34 released podscript, which can convert podcasts or YouTube videos into Markdown transcripts with speaker labels and timestamps, installable via pip install podscript, and using ElevenLabs' high-quality speaker diarization in transcription. [Source-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r76gi7/i_made_a_cli_that_turns_any_podcast_or_youtube/)

- **RTX5070Ti + 5060Ti Achieve 39 t/s** — In an RTX 5070 Ti + 5060 Ti setup (32GB VRAM, 64GB RAM, Windows 11, CUDA 12.4, llama.cpp b8077), Qwen3-Next-80B MoE inference speed was boosted from ~6.5 tokens/s to 39 t/s. Defaults reportedly had CPU bottlenecks and low GPU utilization, addressed by undisclosed adjustments. Source: Reddit. [Source-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r71af3/solution_found_qwen3next_80b_moe_running_at_39_ts/)

- **Leak: BharatGPT is training a 500b non MOE coding + text multilingual multimodal sovereign LLM from scratch** — Leaked information suggests BharatGPT is training a 500B non-MOE coding+text multilingual multimodal sovereign LLM from scratch, with compute costs exceeding tens of millions of dollars, and a web-accessible version will be released. Source: Twitter. [Source-x](https://x.com/kingofknowwhere/status/2023660464631411172)

- **A Friend Gave "V4" a Test** — A friend tested V4 on extracting key points from 30K documents, rating it 7/10, noting clear improvements over 5.2 and G3P, but room for further improvement. Source: Twitter. [Source-x](https://x.com/teortaxesTex/status/2023735703834591312)

- **Moonshot AI (Kimi) Keeps Raising at a Stunning Pace** — Moonshot AI (Kimi) quickly completed a new round of funding exceeding $700 million, led by existing investors including Alibaba, Tencent, and others, with an extremely fast funding pace. Source: Twitter. [Source-x](https://x.com/poezhao0605/status/2023680650386252160)

- **Codex Multi-Agent Parallelism Has Not Hit Quota** — A poster ran more than three agents in parallel on Codex for over two hours, using an 8% of a five-hour window and 2% per week, and still did not hit the limit, indicating the system is not strictly capped. Source: Twitter. [Source-x](https://x.com/theo/status/2023718038198251904)

---

*This report was automatically generated by AI News Agent | 2026-02-17*