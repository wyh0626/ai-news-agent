---
title: "AI 日报 — 2026-09-18"
description: "DeepSeek优化长文本缓存，Prior发布表格模型，GoBench评测围棋。"
lang: "zh"
pairSlug: "ai-daily-2026-09-18"
---

# AI 日报 — 2026-09-18

> 涵盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. DeepSeek-V4.1-Flash 瞄准长上下文智能体的 KV Cache 压缩

DeepSeek 发布了 DeepSeek-V4.1-Flash，这是一个专注于降低长时程智能体 KV cache 内存、存储和带宽成本的模型。通过解决预填充计算以及 HBM/SSD 压力，它可能降低输入密集型工作负载的部署成本，而这类工作负载在智能体和长上下文应用中日益常见。 [来源-huggingface](https://huggingface.co/papers/2609.19969)

### 2. Prior Labs 发布 TabPFN-3.5 SOTA 表格基础模型

Prior Labs 发布了 TabPFN-3.5，声称在 TabArena 和 BeyondArena 上针对多达 100 万行和 2 万特征的数据集达到最先进性能。变体包括 Fast、Thinking 和 Plus，其中 Thinking 通过 API 以计算换取准确率。这增强了基础模型在文本和图像之外的势头，而表格数据仍然是高价值的企业工作负载。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/)

### 3. GoBench 在 9x9 围棋上对照 KataGo 天梯评估 LLM

GoBench 将 LLM 与一系列 KataGo 对手进行基准测试，并报告与 ARC-AGI 2 有强相关性（r=0.83），同时仍未饱和。GPT-6 Astra max 达到 2500 Elo，而 Codex 搭配 Astra 加两小时准备达到 3560 Elo。该基准为通用推理进展提供了一个更清晰、可扩展的代理指标。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/)

## 📰 重点报道

### 结构化数据与模型架构

- **LimiX-2 为结构化数据智能引入 Contextual Mechanism Networks** — LimiX-2 使用 Contextual Mechanism Networks 和 Context-Conditional Masked Modeling，将上下文学习从以目标为中心的预测转向面向机制的联合建模。 [来源-huggingface](https://huggingface.co/papers/2609.17488)

### AI 智能体、科学工具与自动化

- **ScienceIDE 将科学代码库转变为 AI 智能体可学习的环境** — ScienceIDE 将科学代码仓库转换为可编程环境，以减少工具链碎片化，并为科学智能体编码领域特定的正确性标准。 [来源-huggingface](https://huggingface.co/papers/2609.19134)
- **腾讯 BrowserSkill 让 AI 智能体使用你已登录的浏览器** — BrowserSkill 是一个 CLI 和浏览器扩展，允许具备 shell 能力的智能体（如 Cursor、Claude Code、Codex 和 DeepSeek Harness）借用并归还已登录的浏览器标签页，而不会干扰用户。 [来源-github](https://github.com/Tencent/BrowserSkill)
- **腾讯云开源 Octop 自托管多智能体 AI 助手** — Octop 是一个自托管、多用户、多智能体的助手，具有 Web 控制台、CLI、聊天平台集成和 API，强调隐私和可扩展性。 [来源-github](https://github.com/TencentCloud/Octop)
- **n8n：具有原生 AI 能力的 Fair-Code 工作流自动化平台** — n8n 将可视化工作流构建与自定义代码和原生 AI 支持相结合，使自托管或云端智能体和工作流能够访问数百种集成和多个模型提供商。 [来源-github](https://github.com/n8n-io/n8n)

### 强化学习与 LLM 训练

- **PPO Critic 在 LLM 强化学习中遭遇 Value Flattening** — 一篇新论文识别出 Value Flattening 这一失败模式，其中尽管在 Monte Carlo 续接中状态价值发生剧烈变化，PPO critic 估计仍保持平坦，这对 LLM 的 RL 微调具有影响。 [来源-huggingface](https://huggingface.co/papers/2609.18708)

### AI 安全、校准与可靠性

- **面向 LLM 推理与智能体的经验置信度估计** — 该论文提出利用过去的推理和智能体经验来更好地校准置信度，从而改进部署决策，例如发布、升级或重试输出。 [来源-huggingface](https://huggingface.co/papers/2609.17708)

## ⚡ 快讯速览

- **44M 参数量化 LLM 从零训练，在 CPU 上达到 1,900 tok/s** — 据报道，一个从零训练的 44M 参数量化 LLM 在 CPU 上达到每秒 1,900 tokens，凸显了对小型高效本地模型的持续兴趣。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/)
- **论文主张 AI 递归自我改进并非迫在眉睫** — 一项新论点认为递归自我改进不会很快到来，反驳了快速起飞叙事。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wgazy4/rsi_is_not_happening_r/)
- **斯坦福教授推出由志愿者教师授课的 AI 概率课程** — 一位斯坦福教授推出了一门由志愿者授课的 AI 概率课程，扩大了 ML 教育机会。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wbf3ox/teach_ml_community_service_project_from_stanford_n/)
- **LARA：面向冻结 LLM 的可组合低秩行为** — LARA 为冻结 LLM 提出小型可组合低秩行为模块，提供参数高效的控制而无需全量微调。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1whx9tr/lara_small_composable_behaviours_for_frozen_llms_p/)
- **AWS 首席应用科学家主持关于 AI 服务与职业的 AMA** — 一位 AWS 首席应用科学家正在主持关于 AI 服务和职业路径的 AMA，对探索行业角色的从业者有用。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wjuki0/im_a_principal_applied_scientist_at_aws_who/)
- **使用泄漏审计和校准进行 NHANES CHD 预测** — 一个项目根据 NHANES 数据对冠心病风险进行分类，并包含明确的泄漏审计和校准分析。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wjp062/classifying_coronary_heart_disease_risk_from/)
- **Reddit 想法：为训练中的罕见边缘案例增强数据集** — 一个社区想法提议增强大型数据集，以提高训练期间罕见边缘案例的覆盖。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wjnj4a/augmenting_large_datasets_to_have_more_edge_case/)
- **Reddit 用户寻求隔离多 LLM 往复交互的研究** — 一位用户询问隔离 LLM 往复交互效应的研究，指出多智能体评估中的空白。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wjm0rx/what_studies_isolate_backandforth_llm_interaction/)
- **Reddit：通用 LLM 研究与智能体/物理 AI 之间的职业选择** — 一场讨论权衡在通用 LLM 研究与智能体或物理 AI 之间的职业选择。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wj7ltg/future_of_general_llm_work/)
- **开源项目利用剩余 AI tokens 攻克孪生素数猜想** — 一个开源项目邀请贡献者将剩余 AI 算力/tokens 用于孪生素数猜想。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wiggpg/if_you_have_leftover_ai_tokenscompute_theres_an/)
- **Reddit 用户质疑 jev 的 RLCD 是否真的使用 RL** — 一个 Reddit 帖子质疑 jev 的 RLCD 方法是否真的使用强化学习，引发可复现性和命名方面的担忧。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wk6iei/how_is_rlcd_jev_rl_d/)
- **XGBoost 难以匹敌人类市场预测准确率** — 一项实验发现 XGBoost 在市场预测中难以匹敌人类准确率，凸显了金融预测的难度。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wixzts/xgboost_vs_human_markets_p/)
- **寻求将任务歧义与相关 LLM 失败联系起来的指标** — 一位用户寻求将规范歧义与相关 LLM 失败联系起来的指标，这与稳健评估相关。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wi8lla/has_anyone_measured_specification_ambiguity_as_a/)

---

*由 AI News Agent 生成 | 2026-09-18*