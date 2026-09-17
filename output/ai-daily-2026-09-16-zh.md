---
title: "AI 日报 — 2026-09-16"
description: "三款AI新模型发布：科研智能体、开源7B数学搜索、视觉语言物理融合。"
lang: "zh"
pairSlug: "ai-daily-2026-09-16"
---

# AI 日报 — 2026-09-16

> 涵盖 22 条 AI 新闻

## 🔥 今日焦点

### 1. Qwen3.8 Max 以 Intelligence Index 45 分登顶中国排行榜

Qwen3.8 Max (0902) 在 Artificial Analysis Intelligence Index 上得分 45，一个月内提升 5 分，重新夺回中国排行榜榜首，领先 GLM-5.3（44.9）和 Kimi K3（43.8）。这个 2.4T MoE 模型的 30 天升级表明中国前沿模型迭代迅速，并加大了对全球实验室的压力。它也为可能发布的 Qwen 4.0 设定了预期。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wi0dme/qwen38_max_0902_scores_45_on_the_artificial/)

### 2. ZGCM-1：面向数学与智能体搜索的完全开放 7B 基础模型

ZGCM-1 是一个完全开放的 7B 稠密基础模型，从零开始训练，并在数据、系统和算法效率上达到极致。它在 256K 上下文中将内部思考与主动的外部工具使用结合起来，并由端到端开放训练配方支持。其发布之所以重要，是因为它为从业者提供了一条可复现、紧凑的路径，无需专有依赖即可实现强大的数学和智能体搜索能力。 [来源-huggingface](https://huggingface.co/papers/2609.13356)

### 3. Atria Dawn Preview：面向科学研究的智能体语言模型

Atria Dawn Preview 是一个为基础智能体语言模型，专为科学研究和工程工作流设计。它通过 Verifiable Experience Pipeline 训练，该流程将工具介导的交互与可执行环境连接起来。如果这种可验证训练能够泛化，它可能加速自动化实验和真实世界科学智能体的生产力。 [来源-huggingface](https://huggingface.co/papers/2609.15818)

## 📰 重点报道

### 具身与多模态 AI

- **PhysBrain 1.5 连接视觉-语言与物理基础模型** — 一个统一模型通过自回归下一 token 预测，将语言响应、末端执行器运动和稠密视觉目标作为离散序列联合训练，旨在将视觉-语言模型与物理基础模型连接起来。 [来源-huggingface](https://huggingface.co/papers/2609.14973)

### 智能体与开发者工具

- **LibreChat v0.8.8-rc3 增加 Agent Management API 和工作区** — 这个开源 ChatGPT 替代品增加了测试版 Agent Management API、OIDC 机器客户端认证，以及实验性的附加工作区，支持文件检查、搜索、创作和 Bash 执行。 [来源-github](https://github.com/danny-avila/LibreChat)
- **Addy Osmani 发布面向 AI 编码智能体的 Agent Skills** — 这个开源项目打包了生产级工程工作流和质量门禁，将九个斜杠命令从 /spec 和 /plan 映射到 /test 和 /ship，以实现更一致的智能体流程。 [来源-github](https://github.com/addyosmani/agent-skills)

### 研究与持续学习

- **持续学习机制组合用于长时程 LLM 记忆** — 一个新设置表明，语言模型通过持续监督微调学习 100 个查询-答案任务时会遭受灾难性遗忘，并且没有任何一个被评估的持续学习机制能保持强保留率。 [来源-huggingface](https://huggingface.co/papers/2609.06986)

### 硬件、本地推理与行业

- **Qwen 3.8 27B 在 RTX 3090 上运行 63 小时求解黎曼假设** — 一位 Reddit 用户让 4-bit Qwen 3.8 27B 在 100K 上下文下自主运行了 63 小时、处理超过 5000 万 token；它没有解决该问题，但据报道从未幻觉出答案，并纠正了自己的错误。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wi9fau/qwen_38_27b_running_for_63_hours_on_a_rtx_3090_to/)
- **通过 RAM KV Cache 卸载在 3 块 RTX 3090 上实现 1M 上下文** — 自定义 vLLM 补丁将 Qwen3.8-Flash-Next 的大部分 KV cache 卸载到系统 RAM，使三块 RTX 3090 能实现 1M token 上下文，解码速度约为 60–80 tok/s，并已发布补丁/模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1whx5xi/you_can_offload_most_of_qwen38flashnexts_kv_cache/)
- **Apple 可能携 Nvidia AI 硬件重返服务器市场** — 据报道，Apple 正在考虑一款基于 M8 的 AI 服务器，配备 Nvidia 网络用于本地推理，这可能标志着继 Xserve 之后重返服务器市场，不过计划尚未最终确定，2029 年发布可能被取消。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1why9ao/apple_may_return_to_server_market_with_nvidia/)

## ⚡ 快讯速览

- **Mozilla 报告：中美 AI 模型能力差距缩小至 4.4 个月** — 一份 Mozilla 报告称，中美 AI 模型能力差距已缩小至 4.4 个月。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1whsw2g/mozilla_report_chinaus_ai_model_capability_gap/)
- **基础模型重塑整个游戏生命周期中的 AI** — 一篇新论文认为，基础模型正在重塑整个游戏生命周期中的 AI，从资产生成到测试和在线运营。 [来源-huggingface](https://huggingface.co/papers/2609.16679)
- **Atlas：面向 AI 编码智能体的带检查点源代码控制** — Atlas 提供专为 AI 编码智能体量身定制的源代码控制，增加检查点以跟踪和回滚智能体生成的更改。 [来源-github](https://github.com/pacifio/atlas)
- **Pi Agent Harness：带统一 LLM API 的开源 AI 智能体工具包** — Pi Agent Harness 是一个开源工具包，用于通过统一的 LLM API 构建 AI 智能体。 [来源-github](https://github.com/earendil-works/pi)
- **Qwen 4B Logits 在公开演示中几乎匹配 Jev 模型** — 一个公开演示显示 Qwen 4B 的 logits 几乎匹配 Jev 模型，凸显了小模型的质量提升。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1whzy7j/qwen35_4b_grabbing_logits_is_almost_jev_or_even/)
- **12GB RTX 5070 以 15 tokens/s 运行 Qwen3.8 Flash** — 一块 12GB RTX 5070 能以 15 tokens/s 运行 Qwen3.8 Flash，显示消费级显存上的本地推理持续进步。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wi46on/qwen38_flash_on_12gb_vram_15_tokenss/)
- **Xiaomi MiMo 2.6 实时训练仪表盘在 Reddit 上被发现** — Reddit 上发现了 Xiaomi MiMo 2.6 的实时训练仪表盘，暗示即将发布新模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wi9ebm/xiaomi_mimo_26_live_training_dashboard/)
- **Meta 推迟 Muse Spark 开放权重发布** — 根据社区报告，Meta 已推迟 Muse Spark 的开放权重发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1whqm2c/hey_meta_wheres_those_muse_spark_weights/)
- **r/LocalLLaMA 开设双周项目展示集中帖** — r/LocalLLaMA 推出了一个双周集中帖，用于社区项目展示。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wgcpww/biweekly_megathread_project_showcase/)
- **Reddit 帖子批评“pace the frontier”AI 发展推动** — 一篇 Reddit 帖子批评“pace the frontier”AI 发展推动，认为它将速度置于安全性和可及性之上。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wi5rx2/frontier_llm_development_simplified_for/)
- **Reddit 用户开玩笑飞往台湾购买 RTX 5090** — 一位 Reddit 用户开玩笑说，要飞往台湾购买 RTX 5090，而不是支付虚高的美国价格。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1whf7ov/dont_buy_a_9k_rtx_5090_instead/)
- **开发者发布 OpenJev：用于游戏游玩的开源 Crossencoder 模型** — 一位开发者发布了 OpenJev，这是一个用于游戏游玩的开源 Crossencoder 模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wib9kj/openjev/)

---

*由 AI News Agent 生成 | 2026-09-16*