---
title: "AI 日报 — 2026-03-11"
description: "英伟达发布Nemotron3S，MoE120B，Moondream提速40%。"
lang: "zh"
pairSlug: "ai-daily-2026-03-11"
---

# AI 日报 — 2026-03-11

> 涵盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA 发布 Nemotron 3 Super：120B 混合 MoE 潜变量模型
NVIDIA 发布 Nemotron 3 Super，这是一款 120B-12A 混合 SSM 潜变量 MoE 模型，专为 Blackwell 36 和 AAIndex v4 设计，宣称在 FP4 性能上相比 GPT-OSS-120B 可快至 2.2 倍。公司将同步公开数据集、训练配方和权重，并附带技术报告，显示其在高端模型开发上正向开放方向发力。NVIDIA 还暗示 Ultra 版本即将到来，有望进一步扩大大规模 MoE 架构的可及性。[来源-x](https://x.com/ctnzr/status/2031762077325406428)

### 2. Anthropic 的 Claude 3.7 Sonnet 推迟发布；AI 代码主导未来模型
《泰晤士报》报道，目前模型发布节奏已拉长到数周一次，而 Claude 负责生成未来模型中使用的大部分代码。Anthropic 将 Claude 3.7 Sonnet 的上线时间推迟了 10 天，以确保万无一失。行业观察人士警告，未来几年可能会彻底重塑就业市场，Amodei 指出，许多入门级白领岗位可能在 1–5 年内消失。[来源-x](https://x.com/kimmonismus/status/2031803194817511744)

### 3. Nvidia 将斥资 260 亿美元用于开放权重 AI 模型
文件披露，NVIDIA 计划投入约 260 亿美元开发开放权重 AI 模型，表明其正推动为研究者和开发者广泛提供可访问的模型权重，可能加速开放权重生态系统的成长。这一举措凸显了整个行业正向开放与协同研究的更广泛转型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rr4by8/nvidia_will_spend_26_billion_to_build_openweight/)

## 📰 重点报道

### 开源与开发者工具
- **字节跳动 DeerFlow 2.0 作为开源 AI 编排框架登顶 GitHub Trending** — DeerFlow 2.0 完全重写上线后迅速登上 GitHub Trending 榜首，显示出社区对其在 AI Agent 编排领域的强劲采用势头。[来源-github](https://github.com/bytedance/deer-flow)

### 计算机视觉与多模态
- **Moondream 分割模型获得新 SOTA，速度提升 40%** — Moondream 宣布其分割模型获得新的 SOTA 成绩，推理速度提升 40%；该版本已在 Moondream Cloud 上线，本地模型和技术白皮书将在本周稍晚发布。[来源-x](https://x.com/vikhyatk/status/2031616496951238721)
- **Voxtral WebGPU 将实时语音转写带入浏览器端** — Voxtral-Mini-4B-Realtime 支持 13 种语言，延迟低于 500 毫秒，并已集成进 Transformers.js，通过 WebGPU 实现完全本地的浏览器字幕生成；演示与源码已在 Hugging Face 上线。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rqz53r/voxtral_webgpu_realtime_speech_transcription/)

### 国防与工业中的 AI
- **Google 将为五角大楼提供 AI Agent** — Google 将向美国国防部提供用于非机密任务的 AI Agent，凸显私营部门在面向国防的 AI 应用上持续展开合作。[来源-rss](https://www.bloomberg.com/news/articles/2026-03-10/google-to-provide-pentagon-with-ai-agents-for-unclassified-work)

### AI 研究与协作
- **OpenAI 招募专注 RLHF 和多模态 AI 的研究员与工程师** — OpenAI 正在招聘聚焦于 RLHF、长周期评估、奖励建模以及个性化多模态 AI 数据基础设施的研究员和软件工程师。[来源-x](https://x.com/Houda_nait/status/2031831687370539375)
- **Neal Wu 加入 ThinkyMachines 推进协作式 AI** — Neal Wu 宣布加入 ThinkyMachines，与顶尖研究人员一同推进协作式 AI，并邀请他人前往 thinkingmachines.ai/#join-us 与团队一同训练与研究。[来源-x](https://x.com/neal_wu/status/2031846302489985435)

### 强化学习与 3D 视觉
- **面向多视角 3D 场景编辑的几何引导强化学习** — 该工作探索利用 2D 扩散模型的先验来编辑 3D 场景，指出多视角一致性是核心难题，而数据稀缺则是监督微调的障碍，因此提出采用几何引导的强化学习方法。[来源-huggingface](https://huggingface.co/papers/2603.03143)

## ⚡ 快讯速览

- **Perplexity 为 PRO 用户上线 Computer 功能并赠送额度奖励** — Perplexity 扩大 PRO 功能可用性，并提供额外积分以提升高阶用量体验。[来源-x](https://x.com/testingcatalog/status/2031712385468142040)

- **PostTrainBench v1.0 发布，用于评测前沿 AI Agent** — 新的基准工具致力于标准化对前沿 AI Agent 的评估方式。[来源-x](https://x.com/karinanguyen_/status/2031789998811595154)

- **借助 Unsloth GGUF 在 RTX GPU 上本地运行 Qwen3.5** — 通过 Unsloth GGUF，可在 RTX GPU 上离线本地推理运行 Qwen3.5。[来源-x](https://x.com/NVIDIA_AI_PC/status/2031761926121050272)

- **推理能力可扩展 LLM 的参数记忆召回** — 新研究表明，强化推理能力可以提升大模型的参数化召回能力。[来源-huggingface](https://huggingface.co/papers/2603.09906)

- **Omni-Diffusion：利用 Masked Diffusion 的统一多模态 AI 框架** — 提出一个统一的扩散框架，用于处理多模态 AI 任务。[来源-huggingface](https://huggingface.co/papers/2603.06577)

- **InternVL-U：面向理解与编辑的 40 亿参数统一多模态模型** — 介绍一款紧凑的 40 亿参数多模态模型，用于多种视觉-语言任务。[来源-huggingface](https://huggingface.co/papers/2603.09877)

- **庆幸 Anthropic 之争正在此刻上演** — 对当前围绕 Anthropic 及其竞争对手 AI 项目的公共讨论进行评论。[来源-rss](https://www.dwarkesh.com/p/dow-anthropic)

- **“我参加了一场由 AI Bot 进行的面试”** — 探讨由 AI 主导的求职面试及其潜在影响。[来源-rss](https://www.theverge.com/featured-video/892850/i-was-interviewed-by-an-ai-bot-for-a-job)

- **为具备同步状态的 AI Agent 提供开源浏览器（ABP）** — 提出一种面向 AI Agent、支持状态同步的开源浏览器协议。[来源-github](https://github.com/theredsix/agent-browser-protocol)

- **Llama.cpp 新增真实推理预算与对话辅助功能** — Llama.cpp 加入了真正的“推理预算”机制与消息辅助工具。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rr6wqb/llamacpp_now_with_a_true_reasoning_budget/)

- **在 Linux 上利用 Lemonade Stack 在 AMD NPU 上运行 LLM** — 展示如何在 Linux 环境下通过 Lemonade 在 AMD NPU 上运行大语言模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rqxc71/you_can_run_llms_on_your_amd_npu_on_linux/)

- **Apex-1：为边缘硬件训练的 3.5 亿参数微型 LLM** — 一款专为边缘设备设计的紧凑型大语言模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rqvatq/release_apex1_a_350m_tinyllm_trained_locally_on/)

- **Reka Edge 7B 多模态模型登陆 Hugging Face** — 新的 70 亿参数多模态模型已在 Hugging Face 上线。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rqv1kg/rekaairekaedge2603_hugging_face/)

- **为何 AI 编码 Agent 浪费了一半的上下文窗口** — 讨论当前 AI 编码 Agent 在上下文窗口利用上的低效问题。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rr5fo5/why_ai_coding_agents_waste_half_their_context/)

- **Codex 最佳实践现已写入 OpenAI 开发者文档** — OpenAI 将 Codex 的最佳实践整理进官方开发者文档，供开发者参考。[来源-x](https://x.com/derrickcchoi/status/2031741496903250212)

- **MM-Zero：实现自进化的多模态视觉-语言模型** — 提出一类可自我进化的多模态模型方法。[来源-huggingface](https://huggingface.co/papers/2603.09206)

- **Promptfoo：面向 LLM 的评测与红队工具** — 推出一个用于评估和红队测试大语言模型的工具。[来源-github](https://github.com/promptfoo/promptfoo)

- **Claude Code 登录错误增多，访问受影响** — 报告称 Claude Code 的登录错误率上升，导致部分用户访问受阻。[来源-rss](https://status.claude.com/incidents/jm3b4jjy2jrt)

- **我们是如何攻破麦肯锡的 AI 平台的** — 一份分析案例，讲述如何攻陷某企业级 AI 平台的安全防线。[来源-rss](https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform)

- **T3Chat Canvas 提升图像生成体验，并支持多模型测试** — 该功能改善了图像生成的用户体验，并允许在同一界面下对多个模型进行对比测试。[来源-x](https://x.com/thdxr/status/2031786452531515869)

- **Ask HN：Claude 又挂了吗？** — 社区就 Claude 的可用性状况展开讨论。[来源-hackernews](https://news.ycombinator.com/item?id=47336163)

- **Codex 在编码任务上击败 Claude Code；OpenAI 的透明度树立行业标杆** — 报告称 Codex 在编码任务上优于 Claude，而 OpenAI 在透明度方面为行业树立了新标准。[来源-x](https://x.com/CtrlAltDwayne/status/2031624196393238585)

- **Hacker News 禁止 AI 生成评论以保持对话的人类属性** — HN 更新政策，限制 AI 生成评论，以维持讨论的人类真实性和质量。[来源-hackernews](https://news.ycombinator.com/newsguidelines.html#generated)

- **当今大型神经网络可能对你“略感不满”** — 以戏谑口吻评论当前大模型的行为和“情绪”。[来源-x](https://x.com/ibab/status/2031796411671724195)

---

*由 AI News Agent 生成 | 2026-03-11*

━━━━━━ 模板结束 ━━━━━━