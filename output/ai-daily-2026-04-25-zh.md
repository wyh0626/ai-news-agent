---
title: "AI 日报 — 2026-04-25"
description: "AI招聘偏好AI简历；Qwen首发，80TPS在RTX5090，218k上下文。"
lang: "zh"
pairSlug: "ai-daily-2026-04-25"
---

# AI 日报 — 2026-04-25

> 覆盖 19 条 AI 新闻

## 🔥 今日焦点

### 1. AI 招聘工具更偏好 AI 写的简历而非真人简历

在多种模型的成对评估中，AI 生成的简历更受偏爱，这表明 AI 驱动的招聘流程中存在潜在偏见，并引发了关于如何区分真人与 AI 生成简历质量的担忧。该研究强调，AI 介入的招聘流程可能会扭曲结果，因此迫切需要对这类系统进行严格验证。[来源-x](https://x.com/heynavtoor/status/2048088874686300431)

### 2. Qwen-Image-2.0-Pro 发布；在 Arena 排名第 9

Qwen-Image-2.0-Pro 提供更高的图像质量、多语言文本渲染能力，以及在多种风格下更强的指令遵从能力，其在 Arena 榜单中的排名凸显了多模态技术日益成熟。阿里巴巴 Qwen 的多模态布局正通过 ModelScope API 接入和更广泛的基准测试快速推进。[来源-x](https://x.com/Alibaba_Qwen/status/2048022731548229869)

### 3. Qwen3.6-27B 在 RTX 5090 上以 218k 上下文实现约 80 TPS

据称，Qwen3.6-27B 在单张 RTX 5090 上配合 vLLM 0.19，可在 218k 上下文窗口下实现约 80 TPS，显示出良好的可扩展推理能力；同时 NVFP4-MTP 变体似乎已从 Hugging Face 下架。这类吞吐数据对于大模型在实时场景中的部署具有重要意义。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sv8eua/qwen3627b_at_80_tps_with_218k_context_window_on/)

## 📰 重点报道

将剩余重点新闻按主题分组，每组作为一个 ### 标题，条目用项目列表表示：

### LLM

- **AI 招聘工具更偏好 AI 写的简历而非真人简历** — 在模型成对评估中，AI 生成的简历更受青睐，显示出 AI 辅助招聘中的潜在偏见，以及在人类与 AI 简历质量区分上的挑战。[来源-x](https://x.com/heynavtoor/status/2048088874686300431)

- **GPT-5.5（xhigh）在 Artificial Analysis Index 上比 Sonnet 更便宜** — 定价格局使得高成本模型处于激烈竞争中，而 5.5 在成本效率上优于部分替代方案，同时性能接近小型模型的水准。[来源-x](https://x.com/theo/status/2048134278760857949)

### Multimodal

- **Qwen-Image-2.0-Pro 发布；在 Arena 排名第 9** — 提供更高图像质量、多语言渲染，以及扎实的指令遵从能力，体现出成熟的多模态能力。[来源-x](https://x.com/Alibaba_Qwen/status/2048022731548229869)

- **类 Gemini 的多模态预训练停滞；DeepSeek 仍未达到该水平** — 受限于数据和基准测试，被认为是 DeepSeek 无法实现 Gemini 级多模态预训练的主要障碍，相关讨论还提及受 NSA 启发的方法以及对口型同步的更新。[来源-x](https://x.com/teortaxesTex/status/2047881964519063841)

### AI Policy

- **AI 数据中心暂停建设法案预计今年通过（概率 85%）** — 市场与政策制定者围绕 AI 基础设施政策展开争论，在全国范围内就地方/州/联邦层面的暂停建设范围进行讨论，当前预计有 85% 的通过概率。[来源-x](https://x.com/bernhardsson/status/2048046771817861420)

### Hardware / GPUs

- **DeepSeek V4 和 Rubin Ultra 显示出 NVIDIA 的前瞻性** — 分析人士认为，NVIDIA 的设计选择与未来 LLM 工作负载和加速器需求高度契合，这为其带来战略优势，并释放潜在合作信号。[来源-x](https://x.com/jukan05/status/2047861732702662741)

### Open Source / Tools

- **Qwen3.6-27B 在 RTX 5090 上以 218k 上下文实现约 80 TPS** — 来自 Reddit 帖子的吞吐量数据展示了在大上下文窗口下的高速推理能力；据称 HF 上的 NVFP4-MTP 变体被下架，为该模型现状增添了更多背景信息。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sv8eua/qwen3627b_at_80_tps_with_218k_context_window_on/)

- **DeepEP：用于 MoE 的高效 Expert-Parallel 通信库** — 开源的 MoE 通信库，提供高吞吐、低延迟的算子，支持 FP8，并对 RDMA/NVLink 做了优化，以加速训练和对延迟敏感的推理场景。[来源-github](https://github.com/deepseek-ai/DeepEP)

- **2h Codex App 走红，被称为超快代码生成工具** — 各类演示对其极速代码生成能力赞不绝口，突出其在效率和生产力上的潜在提升，同时也引发了对代码质量的审视。[来源-x](https://x.com/sama/status/2048165186482389253)

### Platform / Model Zoo

- **Dell-Hugging Face 承载广泛 AI 模型阵列** — Michael Dell 推介 dell.huggingface.co，展示了来自多家实验室和厂商（如 Kimi K2.5、Mistral、Cohere、Arcee AI Trinity Large、Google Gemma 等）的多样模型，表明企业可以便捷接入多元模型生态。[来源-x](https://x.com/MichaelDell/status/2048038736978403772)

## ⚡ 快讯速览

- **MiMo V2.5 Pro 权重发布，在 AI Index 中位列第 54 名** — MiMo 新版本发布，在 AI Index 中取得中游水平的表现。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sv9q8f/weights_are_comingxiaomis_mimo_v25_pro_has_landed/)

- **Darwin-36B-Opus：36B MoE LLM 登顶 GPQA Diamond 榜** — 基于 MoE 的 Darwin-36B-Opus 在 GPQA Diamond 上取得第一，展示了强劲的 MoE 扩展能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1svl1wr/finalbenchdarwin36bopus_hugging_face/)

- **GLM 5.1 在本地 RTX 6000 Pro 上实现 40 tps** — 本地推理在 RTX 6000 Pro 上达到 40 tps，体现了工作站级部署在效率方面的提升。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1svgtlh/glm_51_locally_40tps_2000_pps/)

- **Qwen3.6-35B-A3B：INT/NVFP KLD 基准测试** — 关于 Qwen3.6-35B-A3B 的基准数据为模型对齐和性能评估提供了参考指标。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1svq8lm/qwen3635ba3b_klds_ints_and_nvfps/)

- **对一位 14 岁少年来说，AI 与 Disney 的差距只剩“品味”** — 讨论 AI 驱动媒体在可及性和文化影响方面的意义，认为当下障碍更多在审美和品味层面而非技术门槛。[来源-x](https://x.com/ArthurMacwaters/status/2048081330395897867)

- **Ubuntu 26.04 简化 AMD XDNA2 NPU 上手流程** — Ubuntu 26.04 改善了 AMD XDNA2 NPU 的初始化与环境搭建流程，使开发者更容易上手。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1svfebz/psa_ubuntu_2604_makes_it_easier_to_get_started/)

- **Claude 使用限制被逆向推断；Codex 会步其后尘？** — 有传闻称 Claude 的使用上限已被逆向解析，同时外界也在猜测 Codex 的下一步动作。[来源-x](https://x.com/nrehiew_/status/2048009931757097079)

- **OpenAI Team Ships** — OpenAI 团队宣布推出一款新产品或更新，具体细节尚未公布。[来源-x](https://x.com/gdb/status/2047901060803784865)

- **Codex 也不是一辆车** — 对 Codex 品牌与其实际能力的讽刺性评论，用幽默方式质疑其定位与现实表现。[来源-x](https://x.com/thsottiaux/status/2047877213052342290)

---

*由 AI News Agent 生成 | 2026-04-25*