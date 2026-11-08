---
title: "AI 日报 — 2026-11-07"
description: "英伟达发布智能体语境本体，VFlash加速视觉规划，SLA扩展空间语言行动模型。"
lang: "zh"
pairSlug: "ai-daily-2026-11-07"
---

# AI 日报 — 2026-11-07

> 涵盖 22 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA 发布面向 AI Agent 上下文的 Auto Ontology 框架

NVIDIA 推出了 Auto Ontology，这是一个开源 Python 框架，可在企业数据之上构建基于图的语义推理层，并通过 MCP、CLI 和 API 将其暴露给 Agent。该框架针对 agentic 工作流中的一个核心可靠性问题：将上下文建立在可发现、可解释的数据上，而不是临时检索。如果被广泛采用，它可能标准化企业 Agent 在受治理知识图谱上的推理方式。[来源-github](https://github.com/NVIDIA/auto-ontology)

### 2. TSMC 为逻辑芯片缓存开发 BEOL 氧化物半导体存储器

TSMC 在 2025 VLSI Symposium 上展示了一种 BEOL 集成的 1T1C 氧化物半导体存储器，报告了 0.75V 工作电压、超过 128ms 的保持时间、低于 8ns 的读/写周期，以及超过 10¹⁴ 次循环的耐久性。该技术可能提供比 SRAM 密度更高的片上缓存，是未来 AI 和先进逻辑芯片的一个有意义杠杆。这仍是测试芯片结果，但其缓存密度影响对计算扩展意义重大。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xq65rl/tsmc_might_do_in_memory_compute_for_us/)

### 3. Harness Leaderboard 对 Kimi Code、Hermes、Pi、Claude Code、Codex 进行基准测试

一篇新的 Harness Leaderboard 文章在 Terminal Bench 2.1 和 Deep SWE 1.1 上对包括 Kimi Code、Hermes、Pi、Claude Code 和 Codex 在内的编码 Agent 与 harness 进行基准测试。该比较让从业者能在原始模型基准之外，对 Agent 性能获得有用视角。Harness 设计正成为真实世界编码 Agent 生产力中的一个主要变量。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xpvfx8/harness_leaderboard_kimi_code_hermes_pi_claude/)

## 📰 重点报道

### 具身智能与机器人

- **VFlash 通过 Flash Primitive Decoding 加速视觉规划** — VFlash 引入 Flash Primitive Decoding，以降低机器人和自动驾驶中逐坐标视觉计划生成的成本，目标是实现更快、更准确的物理 AI 规划。[来源-huggingface](https://huggingface.co/papers/2611.08449)
- **SLA 通过持续预训练扩展空间-语言-动作模型** — SLA 将空间理解视为一种可迁移的基础模型能力，通过在大规模机器人经验上进行持续预训练来学习，从而减少对任务特定空间监督的依赖。[来源-huggingface](https://huggingface.co/papers/2611.08373)

### 本地 LLM 与 Agent 工具

- **llama_moe_cache 在 CPU 上运行未命中的 MoE 专家并附带调优脚本** — 一个 llama.cpp 拉取请求新增 llama_moe_cache，用于在 CPU 上运行未命中的 MoE 专家，并添加调优脚本，旨在为显存有限的用户加速 MoE 卸载。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqacka/llama_moe_cache_run_missed_experts_on_cpu_add/)
- **Obsessive-1.7B：基于 LFM3-1.7B 构建的 1.1 GB 网页搜索子 Agent** — 一名开发者将 LFM3-1.7B 微调为 Obsessive-1.7B，这是一个 1.1 GB 的网页搜索子 Agent，可返回答案、逐字引用和来源 URL，不过它在面对已移除的答案时难以说出“未找到”。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xq4yju/obsessive17b_a_11_gb_websearch_subagent/)
- **Valet：用于 Homelab 管理的开源本地 LLM 仪表盘** — Valet 是一个开源仪表盘，使本地或托管 LLM 能够管理 185+ 个 homelab 服务，支持自定义插件，并在 RTX 5090 上使用 Qwen 27B 达到约 230 tok/s。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xq7qi4/valet_use_local_llms_to_manage_your_homelab_open/)
- **QFN 3.8 通过 Open WebUI 虚拟机控制在 MS Paint 中画狗** — 一名 LocalLLaMA 用户使用 QFN 3.8 NVFP4 配合 Open WebUI 和 Open Terminal 控制 Windows 11 虚拟机，并在 MS Paint 中画了一只狗，展示了计算机使用工具正日趋成熟。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xpmvf2/we_are_cooked_my_qfn_38_nvfp4_just_drew_a_dog/)

### 人机交互与研究

- **论文为 AI 增强人类智能提出认知共生体** — 一篇新论文主张 AI 系统应增强人类记忆、感知和决策，而不是作为自主 Agent 运行，并认为当前个人 Agent 仍处于用户情境之外。[来源-huggingface](https://huggingface.co/papers/2611.05376)

## ⚡ 快讯速览

- **DPDM 使用共享条件预测器进行 Agent 决策** — DPDM 提出一种共享条件预测器，以改进 Agent 跨任务决策。[来源-huggingface](https://huggingface.co/papers/2611.02075)
- **Harness-S 使用同级 Harness 进行可泛化 Agent 训练** — Harness-S 使用同级 harness 训练 Agent，以提高跨执行环境的泛化能力。[来源-huggingface](https://huggingface.co/papers/2611.04277)
- **Cloudflare 开源用于安全审计的编码 Agent 技能** — Cloudflare 发布了一个用于运行安全审计的开源编码 Agent 技能。[来源-github](https://github.com/cloudflare/security-audit-skill)
- **Observer：开源本地 AI Agent 通过手机监控任何事物** — Observer 是一个开源本地 AI Agent，让用户通过手机监控任何事物。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqd058/use_your_phone_to_monitor_anything_with_local/)
- **KV 缓存量化对 Qwen3.8 27B 影响极小** — 一项用户基准测试发现，KV 缓存量化对 Qwen3.8 27B 质量的影响极小。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqbesv/effects_of_kv_cache_quantization_on_qwen38_27b/)
- **Crowd-v1 旨在以 0 美元协作训练 1B LLM** — Crowd-v1 是一项协作努力，旨在以 0 美元训练一个 1B 参数 LLM。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqh8hk/crowdv1_the_collaborative_llm/)
- **Reddit 用户报告 Qwen3.8-Flash-Next 尝试可疑 URL 抓取** — 一名 Reddit 用户报告 Qwen3.8-Flash-Next 尝试进行可疑 URL 抓取，引发 Agent 安全担忧。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqbjbf/also_experienced_the_qwen38flashnext_url_issue/)
- **DSpine：跨层因果注入的并行推测解码** — DSpine 提出一种跨层因果注入的并行推测解码，以提高草稿效率。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xq9hf6/paper_dspine_draft_in_parallel_condition_through/)
- **Qwen3.8-Flash-Next Gyro S 在 Steam Machine 上以 18 t/s 运行** — 据报道，Qwen3.8-Flash-Next Gyro S 在 Valve Steam Machine 上以每秒 18 个 token 运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xq8s2n/qwen38flashnext_gyro_s_on_a_valve_steam_machine_8/)
- **用户寻求适用于 16GB 显存系统的本地 AI Agent 配置** — 一名用户询问适用于 16GB 显存系统的本地 AI Agent 配置方案。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqjenw/anyone_running_local_ai_on_16gb_vram/)
- **用户询问在 Agentic LLM 任务中使用“none”推理等级** — 一名用户询问“none”推理等级是否对 agentic LLM 任务有用。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xq4pb6/does_anyone_use_none_reasoning_level_for_anything/)
- **用户在 Qoder 上测试 Qoduck（可能是 Qwen4），并注意到图像/视频生成** — 一名用户在 Qoder 上测试 Qoduck——可能是 Qwen4——并注意到图像和视频生成能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xqafp1/testing_qoduck_maybe_qwen4_on_qoder/)

---

*由 AI News Agent 生成 | 2026-11-07*