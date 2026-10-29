---
title: "AI 日报 — 2026-10-28"
description: "多尺度策略优化助长程智能体训练，三位一体促多模态递归自改进，视频基准测代码生成。"
lang: "zh"
pairSlug: "ai-daily-2026-10-28"
---

# AI 日报 — 2026-10-28

> 涵盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. Ψ-0.6 借助自适应推理统一视觉、语言与世界建模

研究人员介绍了 Ψ-0.6，这是一个统一的视觉-语言世界模型，可对词语、深度、运动、相机姿态和想象场景进行推理，并使用 RL 学习何时使用每种模态。它报告了在空间推理和物体运动预测上的零样本提升，以及从模拟房间到真实机器人桌面的迁移。代码和论文的发布使其成为自适应多模态推理和具身世界模型的有用测试平台。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xgwq9u/ψ06_adaptive_streams_of_thought_in_a_unified/)

### 2. Papers with Code 以开源 Apache 2.0 项目重新启动

Papers with Code 已重新启动为一个开源 Apache 2.0 项目，托管在 Hugging Face 旗下的 GitHub 上，带有 FastAPI 后端、React 前端、公共 API 和 MCP server。此次重启恢复了面向论文、基准和 SOTA 结果的关键发现层，同时邀请社区贡献。对于从业者而言，如果维护者保持势头，它可能成为一个更开放、更协作的研究索引。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xgoadu/papers_with_code_is_now_opensource_p/)

### 3. 审稿人警告半数 AI 会议同行评审由 AI 生成

一位长期为 NeurIPS、ICML、AAAI 和 ICLR 审稿的审稿人报告称，他们现在看到的同行评审中约有一半似乎完全或部分由 AI 生成，同时还有更多由 AI 撰写的投稿。他们将审稿流程描述为处于“危急状态”，并呼吁对保障措施和流程设计给予更多关注。这一轶事并非正式研究，但它凸显了 AI 会议和研究诚信日益增长的治理风险。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xh2wzt/the_paper_reviewing_process_is_now_in_critical/)

## 📰 重点报道

### 智能体与训练

- **多尺度策略优化提升长时程 LLM 智能体训练** — MPO 在轮次级别对齐信用分配与策略更新，以改善长时程智能体训练；该方法针对基于 critic 的 RL 在多轮智能体中的一个已知弱点。[来源-huggingface](https://huggingface.co/papers/2610.35013)
- **The Trinity 实现多模态智能体的递归自我改进** — 该框架利用跨模态和任务形式之间共享的能力需求，减少昂贵的环境构建和手动 harness 迭代。[来源-huggingface](https://huggingface.co/papers/2610.36077)

### 多模态、具身 AI 与基准测试

- **VibeVideoBench 对代码驱动视频生成中的多模态智能体进行基准测试** — 该基准评估通过编写代码来渲染帧并合成音频的智能体，涵盖 239 个英文和中文任务，针对扩散视频模型经常错失的精确输出。[来源-huggingface](https://huggingface.co/papers/2610.35864)
- **PDRVLA 为视觉-语言-动作模型加入物理动态 token** — 一个轻量级物理动态模块从视觉-语言特征中提取 token，以条件化机器人动作生成，而无需在线视频生成的延迟。[来源-huggingface](https://huggingface.co/papers/2610.37381)
- **ChronoReplay 应对流式空间 VLM 中的接口锁定** — 该论文识别出对单一读出接口的后训练特化，并提出回放异构监督以保留多种空间读出。[来源-huggingface](https://huggingface.co/papers/2610.34283)

### 音频与基准测试

- **EmbeddingGemma-2 通过 Null-Space PCA 登上 MAEB 音频基准第一** — 一种零训练 PCA 投影到模型未使用的零空间中，使一个 577M 嵌入模型在 30 项任务音频基准上从第 #26 名升至第 #1 名，表现优于规模大得多的多模态模型。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xho7pr/r_taking_embeddinggemma2_577m_from_rank_26_to_1/)

### 工具与框架

- **Superpowers 为编码智能体提供智能体技能框架** — 该开源框架和方法论引导编码智能体在编码前澄清规格，并适用于 Claude Code、Codex、Cursor、Gemini CLI 和 GitHub Copilot CLI。[来源-github](https://github.com/obra/superpowers)

## ⚡ 快讯速览

- **HKUDS 发布 DeepTutor，用于终身个性化 AI 辅导** — DeepTutor 是一个用于终身、个性化 AI 辅导的开源系统。[来源-github](https://github.com/HKUDS/DeepTutor)
- **GitHub 合集发布 31 个针对 25+ AI 模型的越狱提示** — 该仓库记录了针对 25 个以上 AI 模型的越狱提示。[来源-github](https://github.com/togg53192-cmd/jailbreaks)
- **在金融推理的事后自蒸馏中，通用反馈可匹敌自我批评** — 一项研究发现，在金融推理的事后自蒸馏中，通用反馈可以匹配自我批评。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhv8yp/how_much_does_the_hint_matter_a_generic_feedback/)
- **鸡尾酒会音频 CAPTCHA 显示人类以微弱优势胜过语音模型** — 一项使用鸡尾酒会音频的反向图灵测试发现，人类以微弱优势胜过语音模型。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhuado/cocktailparty_audio_as_a_reverse_turing_test/)
- **Pandora M1：用于跨 64 个节点分布式训练的桌面监控器** — Pandora M1 是一个用于跨 64 个节点分布式训练的桌面监控盒。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhkli0/pandora_m1_a_training_monitor_box_64_nodes_x_8/)
- **Harness 在执行前记录 LLM 智能体工具参数溯源** — 该 harness 在执行前记录 LLM 智能体工具参数的来源。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhnoo2/a_harness_that_records_where_an_llm_agents_tool/)
- **面向 Claude Code、Cursor 和其他编码工具的 AI 设计技能合集** — 该仓库收集面向 Claude Code、Cursor 和其他编码工具的 AI 设计技能。[来源-github](https://github.com/elayadesign/ai-design-skills)
- **哈佛大学的 Stephen Casper 主持关于 AI 保障与治理的 AMA** — Stephen Casper 正在主持一场关于 AI 保障与治理的 AMA。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhpnfs/ama_this_wednesday_stephen_cas_casper_harvard/)
- **Reddit 用户询问如何为经 CPT 的 Qwen 9B 法律模型加入推理和工具使用** — 一位从业者询问如何为经过持续预训练的 Qwen 9B 法律模型加入推理和工具使用。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xi21f9/cptd_qwen9b_on_polish_legal_data_how_to_make_it/)
- **在 PyTorch 中逐步构建 Transformer 的手动 Autograd** — 一篇教程在 PyTorch 中逐步手动构建 Transformer Autograd。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xh1z1p/understanding_transformer_autograd_by_building_it/)
- **AI 检测会触及基本数学极限吗？** — 一场讨论询问 AI 检测最终是否会面临基本数学极限。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhtabq/could_ai_detection_eventually_become_a/)
- **开源仓库记录 20 项 NCM 与 Transformer 可解释性研究** — 该仓库记录了 20 项关于下一概念建模（NCM）和 Transformer 可解释性的研究。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xh3e7o/exploring_nextconcept_modeling_ncm_transformer/)
- **博士生寻求关于为工作流自动化入门智能体 AI 的指导** — 一名博士生询问如何针对特定的工作流自动化用例入门智能体 AI。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xhso7k/how_do_you_start_with_agentic_ai_for_a_specific/)
- **Reddit 用户寻求用于自蒸馏的非 EMA 教师方法** — 一位从业者询问除 EMA 之外用于自蒸馏的教师方法。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xgwagz/teachers_other_than_ema_for_distillation_r/)

---

*由 AI News Agent 生成 | 2026-10-28*