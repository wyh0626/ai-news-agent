---
title: "AI 日报 — 2026-09-10"
description: "OpenAI称破解千年难题，NeurIPS误拒178稿，LLM刷新圆堆积纪录"
lang: "zh"
pairSlug: "ai-daily-2026-09-10"
---

# AI 日报 — 2026-09-10

> 涵盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 声称已破解 Navier-Stokes 千禧年难题

据《纽约时报》和 OpenAI 的报道，OpenAI 宣布已破解 Navier-Stokes 存在性与光滑性问题，这是数学界的千禧年大奖难题之一。如果得到验证，这将是一项具有里程碑意义的 AI 辅助数学突破，对面向科学的 AI 研究和自动定理发现具有重大意义。该声明现在面临同行验证和正式数学审查的关键考验。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wavdi7/openal_says_it_has_cracked_one_of_maths/)

### 2. NeurIPS 使用 AI 检测器直接拒稿 178 篇论文，而该检测器会标记其自己的主席

NeurIPS 的立场论文赛道使用专有的 Pangram AI 检测器直接拒稿 178 篇论文，占提交量的 18.4%，且没有人工审查或申诉。独立检查发现，该检测器将赛道主席自己提交的论文标记出来，比例为 24–69%，而其默认设置最初标记了所有提交的 42.7%，调优后才降至 12.7%。该事件引发了对基于 AI 的同行评审筛查和假阳性的严重治理问题。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/)

### 3. LLM 引导的程序演化改进 10 个已知最优圆填充解

一篇 Reddit 帖子描述了使用 LLM 迭代演化一个优化算法，将 N=101 到 114 的 10 个 Packomania csqv 基准的已知最优半径和提升 2.4–5.4%。该方法使用记分板、候选评分和一个独立验证器，LLM 总成本为 $27.72。Packomania 独立接受了这些结果，为在困难优化中低成本 LLM 驱动的算法发现提供了一个具体示例。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/)

## 📰 重点报道

### 世界模型与具身 AI

- **Show-Harness 让 VLM 智能体通过语义接口控制机器人** — 一个具身化框架暴露离散语义动作单元，供 VLM 推理，而确定性解释器则将其落地为本地机器人动作。[来源-huggingface](https://huggingface.co/papers/2609.10522)
- **可编程世界模型将状态演化与视觉生成解耦** — 该框架将持久世界状态程序与视觉观察生成分离，从而为视频世界模型实现直接控制和更好的长期一致性。[来源-huggingface](https://huggingface.co/papers/2609.10540)
- **OpenWAM：用于系统性世界-动作模型预训练的开放模块化栈** — OpenWAM 将骨干、表示、架构、信息流、推理和数据选择模块化，从而将世界-动作预训练转变为受控实验计划。[来源-huggingface](https://huggingface.co/papers/2609.07398)

### 工具与基础设施

- **TradingAgents v0.4.0 发布多智能体 LLM 交易框架修复** — 这个开源框架增加了时点数据修复、更清晰的决策信号、CLI 检查点恢复、交易者价格锚定，并支持 GPT-5.6 和 GLM-5.3。[来源-github](https://github.com/TauricResearch/TradingAgents)
- **EmbedFlow 实现嵌入模型之间的零停机迁移** — EmbedFlow 使用新嵌入模型对旧索引中采样的文档进行重排序，以在迁移过程中保持检索质量，不过选择足够的 K 仍是关键难点。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wabmm7/my_lab_found_a_way_to_migrate_between_embedding/)

### 模型训练与评估

- **从零训练的 348M 模型在多位数算术上表现出色** — 一个 348M 参数模型在 22.7B token 上训练，并在显式列算术上微调，报告在九个 GPT-3 算术子任务上平均达到 99.4%，在若干多位数加法和减法任务上超过 GPT-3 175B 少样本表现。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wc7hmu/i_trained_a_348m_model_trained_from_scratch_on/)
- **Ant Ling 的 Ling-3.0-flash-Sante 在 DiagnosisArena-MCQ 上得分 83.83** — 该医疗推理模型在多项选择诊断中取得强劲分数，但该结果只衡量在四个给定诊断中进行选择，而非开放式鉴别诊断生成或临床决策。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wbkxsa/what_santes_8383_on_diagnosisarenamcq_actually/)

## ⚡ 快讯速览

- **Rustuna 发布：Optuna 的高性能 Rust 实现** — 一个 Rust 原生的 Optuna 替代方案，旨在为 ML 工作流提供更快的超参数优化。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/)
- **将 KV Cache 作为智能体运行时用于交互式 LLM 的探索** — 一项讨论探索将 KV cache 视为智能体运行时，用于交互式 LLM 执行和状态管理。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/)
- **AgentGrad：面向多智能体系统的干预引导提示优化** — AgentGrad 使用干预来指导跨多智能体 LLM 系统的提示优化。[来源-huggingface](https://huggingface.co/papers/2609.08572)
- **Marigold V2 利用扩散 Transformer 增强单目深度估计** — Marigold V2 应用扩散 Transformer 来改进单目深度估计。[来源-huggingface](https://huggingface.co/papers/2609.08084)
- **腾讯推出 TeamAI CLI，让团队 AI 原生** — 腾讯的新 CLI 旨在将 AI 原生工作流嵌入团队开发流程。[来源-github](https://github.com/Tencent/teamai-cli)
- **Pascal Editor：面向 AI 智能体的开源 3D 建筑工具，带 MCP** — Pascal Editor 是一个开源 3D 建筑工具，为 AI 智能体暴露 MCP 接口。[来源-github](https://github.com/pascalorg/editor)
- **开源库为 CAD 和机器人提供 AI 智能体技能** — 一个新库为处理 CAD 和机器人的 AI 智能体打包了文本到 CAD 技能。[来源-github](https://github.com/earthtojake/text-to-cad)
- **Awesome GPT-Image2：包含 530+ 案例的工业级提示引擎** — 该仓库收集了一个工业级提示引擎和 530+ 个 GPT-Image2 示例。[来源-github](https://github.com/freestylefly/awesome-gpt-image-2)
- **开源 AI 工程课程提供 20 个阶段共 523 节课** — 该课程涵盖 523 节课和 20 个阶段，用于从零学习 AI 工程。[来源-github](https://github.com/rohitg00/ai-engineering-from-scratch)
- **PI-Desktop：面向 AI 编码智能体的本地优先桌面工作区** — PI-Desktop 提供面向 AI 编码智能体的本地优先桌面工作区。[来源-github](https://github.com/vastsa/PI-Desktop)
- **果蝇连接组无法学会 Pong；突触审计揭示原因** — 一项实验显示，真实果蝇连接组无法学会 Pong，突触审计指向连接性或可塑性限制。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wc67ci/i_tried_to_make_a_real_fly_connectome_learn_to/)
- **微型 RNN 从单一初始状态自主生成 Bad Apple 视频** — 一个微型 RNN 从单一初始状态自主生成 Bad Apple 视频，凸显了紧凑的动态记忆。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/)
- **ML 研究可复现性因昂贵硬件和不透明 AI 工具面临无关紧要风险** — 一项讨论警告，随着硬件成本和不透明 AI 工具增加，可复现性正走向无关紧要。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1w92eis/reproducibility_seems_to_be_headed_towards/)
- **MLP 利用直方图特征对汽车雷达目标进行分类** — 一个 MLP 分类器使用直方图特征进行汽车雷达目标分类。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1w9m26u/automotive_radar_object_classification_p/)
- **本科生在 Reddit 上为测试时训练寻求合作者和算力** — 一位本科生研究员正在为测试时训练工作寻求合作者和算力。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wcjn2b/anybody_working_on_test_time_training_over_here/)
- **调试 AI 工作流中的静默失败：从哪里开始？** — 从业者讨论如何调试那些产生错误输出但没有显式失败的 AI 工作流。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1waewc3/when_a_run_is_wrong_but_nothing_actually_failed/)
- **机器人专家讨论 LLM 对从演示学习和行为克隆的影响** — 机器人专家争论 LLM 正在如何重塑从演示学习和行为克隆。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1w9lt31/roboticists_working_in_learningfromdemonstrations/)

---

*由 AI News Agent 生成 | 2026-09-10*