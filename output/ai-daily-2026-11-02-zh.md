---
title: "AI 日报 — 2026-11-02"
description: "金融K线模型开源；Qwen承诺4/5开源；ISTA发763B单比特DS代码模型。"
lang: "zh"
pairSlug: "ai-daily-2026-11-02"
---

# AI 日报 — 2026-11-02

> 涵盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. Qwen 确认 Qwen 4.0 和 5.0 将继续开源

Qwen 负责人 Liu Dayi Heng 正式否认了 Qwen4 将是最后一个开放权重版本的传言，确认 Qwen 4.0 和 Qwen 5.0 将继续开源。这一承诺很重要，因为 Qwen 报告累计下载量超过 30 亿次、460+ 开源模型和 300,000+ 衍生模型，使其路线图成为开放权重生态的风向标。这也强化了对闭源实验室的竞争压力，要求其证明专有访问的合理性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xm28e6/official_statement_qwen_models_will_stick_to_open/)

### 2. ISTA 以约每参数 1 比特发布 763B DeepSeek-V4.1-Flash Coder

ISTA 发布了 DeepSeek-V4.1-Flash-1017 的 Coder 构建，使用 GSQ 和 RCO 压缩，剪枝了一半路由专家，每层保留 384 个中的 192 个。结果是 72.1 GB transformer 权重，约每个原始 transformer 参数 1.05 比特，共享 Engram 文件和视觉投影器保持不变。这是对极端 MoE 压缩以及超大型编码模型本地部署的一次显著压力测试。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xlys6k/release_ista_deepseekv41flash1017_gsqrco_coder_a/)

### 3. 开源稀疏注意力低成本实现 10M Token 上下文

一种完全开源的稀疏注意力方法对 Qwen 3.8 27B 注意力进行稀疏化，未观察到准确率损失，并且可以原生地基于下一 token 预测训练，以匹配全注意力验证损失。团队报告上下文扩展到 10M tokens，仅在特定任务上出现退化，而 NIAH 基准仍然良好，并公开了 kernel 与 SGLang 集成。如果可复现，这将降低小型开放权重模型在本地硬件上进行长上下文推理的成本。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmbj0v/new_sparse_attention_method_for_ultralong_context/)

## 📰 重点报道

### 开源模型与基础设施

- **Kronos：面向金融 K 线数据的开源基础模型** — Kronos 发布了一个仅解码器的开源金融 K 线基础模型，带有分层 OHLCV tokenizer 和 AAAI 2026 接收，为量化研究者提供可复现的预训练基线。 [来源-github](https://github.com/shiyu-coder/Kronos)
- **FreeToken 在消费级硬件上本地运行 290B+ MoE 模型** — FreeToken 是一个边缘原生 MoE 服务引擎，通过带宽自适应协同执行和专家缓存，统一 GPU、CPU、主机内存和互连，用于前沿规模的本地推理。 [来源-github](https://github.com/FlashML-org/FreeToken)

### 多模态与表示学习

- **FrameForge 利用视频基础模型先验实现统一图像生成** — FrameForge 引入统一条件图像生成，利用预训练视频基础模型，并处理跨任务中不同的条件-目标关系。 [来源-huggingface](https://huggingface.co/papers/2610.36545)
- **定理证明 JEPAs 跨模态学习共享的柏拉图表示** — 研究人员证明，单独训练的 Joint-Embedding Predictive Architectures 在不同模态间学习到相同表示（直至旋转），为多模态对齐提供了理论保证。 [来源-huggingface](https://huggingface.co/papers/2610.39302)

### 智能体、具身 AI 与安全

- **R^2Orch：用于智能体编排的递归自博弈** — R^2Orch 提出一种递归自博弈编排范式，带有内层自博弈循环，以改进智能体技能学习，并解决手工设计课程、优势崩塌和逐技能评估噪声问题。 [来源-huggingface](https://huggingface.co/papers/2610.22740)
- **REA：面向异步脑-小脑控制的路由具身智能体运行时** — REA 将缓慢的基础模型推理与快速反应策略配对，用于异步具身控制，针对不兼容的评估栈以及审慎-反射协调问题。 [来源-huggingface](https://huggingface.co/papers/2610.42053)
- **具有可审计 LLM 智能体的开源 AI 安全运营中心** — AiSOC 是一个可自托管的 AI 安全运营中心，具有可审计 LLM 智能体、告警融合、MITRE ATT&CK 调查、可重放决策账本，以及面向 Claude、Cursor 和 Continue 的 MCP server。 [来源-github](https://github.com/beenuar/AiSOC)

## ⚡ 快讯速览

- **Anthropic 收紧 Claude Code 限制以阻止逆向工程和游戏克隆** — 据报道，Anthropic 收窄了 Claude Code 使用限制，以防止逆向工程和游戏克隆，这再次引发自托管争论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xm33gr/yet_another_reason_to_self_host_anthropic_has/)
- **LLMs 可原生读取和写入神经网络权重** — 一项新的权重空间编程演示表明，LLMs 可以直接检查和编辑神经网络权重。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xm6jow/sparks_of_weightspace_programming_llms_can/)
- **协同设计 System-1 与 System-2 以实现可扩展 AGI** — 一篇新论文提出协同设计快速和慢速推理组件，以构建可扩展 AGI 架构。 [来源-huggingface](https://huggingface.co/papers/2610.39497)
- **Handy：面向桌面的开源离线语音转文本应用** — Handy 为桌面用户提供本地、离线语音转文本转录。 [来源-github](https://github.com/cjpais/Handy)
- **Kornia：面向 PyTorch 空间 AI 的可微计算机视觉库** — Kornia 为 PyTorch 空间 AI 工作流提供可微计算机视觉算子。 [来源-github](https://github.com/kornia/kornia)
- **Hex 在桌面平台提供本地 AI 语音听写** — Hex 在桌面平台提供本地 AI 语音听写。 [来源-github](https://github.com/anomalyco/hex)
- **AI Engineering Hub 提供 93+ 个 LLM、RAG 和 Agent 项目** — AI Engineering Hub 收集了 93 个以上面向构建者的实用 LLM、RAG 和 agent 项目。 [来源-github](https://github.com/patchy631/ai-engineering-hub)
- **Qwen 3.8 27B 使用 Blender Python 加速数学推理** — 一位用户报告，Qwen 3.8 27B 有时会使用 Blender Python 辅助数学推理。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmbym0/qwen_38_27b_is_sometimes_so_smart_it_scares_me/)
- **本地量化模型与 Claude 在 9 个真实 CUDA bug 上接受测试** — 一项基准在九个真实 CUDA 修复任务上比较本地量化模型与 Claude。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xlwpqv/not_another_toks_post_local_quants_vs_claude_on_9/)
- **Amazon 据称取消 GPU 订单，并关闭与计算硬件购买相关的账户** — 有报道称，Amazon 取消了 GPU 订单，并关闭了与计算硬件购买相关的账户。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xm8o8g/amazon_is_allegedly_canceling_gpu_orders_and_in/)
- **GPT-6 Astra 编辑 Qwen 权重，将 MATH-500 提升至 48.1%** — 一份报告称，GPT-6 Astra 编辑了 Qwen 权重，并将 MATH-500 性能从 7.9% 提升至 48.1%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xma0tw/gpt6_astra_edits_qwen_weights_math500_79_to_481/)
- **社区提议让私有 LLM 质量基准优先于 Tok/s** — 一项社区提议主张，私有 LLM 评估应优先考虑质量基准，而非每秒 token 数指标。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xlusil/proposal_a_community_revolution_for_private/)
- **Reflection Lab 将就其开放权重 Beam 模型举办 AMA** — Reflection Lab 将就其开放权重 Beam 模型举办 AMA。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xlmkk4/ama_announcement_reflection_the_lab_behind_behind/)

---

*由 AI News Agent 生成 | 2026-11-02*