---
title: "AI 日报 — 2026-11-08"
description: "Claude技能库开源、蚂蚁灵发560B多模态MoE、DrexMax称SOTA。"
lang: "zh"
pairSlug: "ai-daily-2026-11-08"
---

# AI 日报 — 2026-11-08

> 涵盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. Anthropic 发布 Claude Agent Skills 公共仓库

Anthropic 已在 GitHub 发布一个公共仓库，其中包含其面向 Claude 的 Agent Skills 实现，以及模型可动态加载的说明、脚本和资源，以便在创意、技术和企业工作流中可重复地执行专门任务。该仓库还指向 agentskills.io 上更广泛的 Agent Skills 标准，表明其正推动可复用、可移植的智能体能力，而非一次性提示词。这可能加速标准化，并使企业智能体部署更易于审计、共享和复现。 [来源-github](https://github.com/anthropics/skills)

### 2. Ant Ling 发布 Ling-3.2-flash：560B 多模态 MoE，支持 1M 上下文

Ant Ling 推出了 Ling-3.2-flash，这是一个原生多模态专家混合模型，总参数 560B，激活参数 25B，并具有支持文本、图像和视频输入的 1M token 上下文窗口。报告的基准测试分数包括 MathVision 96.80、OmniDocBench 1.5 92.21 和 AndroidWorld 85.63，同时还展示了 PDF 转代码、GUI 操作、3D 重建和多智能体工作流。文档同时记录了 OpenAI 和 Anthropic 兼容的 API 访问方式，将该发布定位为长上下文多模态智能体应用。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xpye7g/ant_ling_introduces_ling32flash_560b25b_native/)

### 3. Drex Max v1.1 声称在多模态决策模型上达到 SOTA 并位于帕累托前沿

Nace 发布了 Drex Max v1.1，这是一款多模态决策模型，其称根据 Artificial Analysis 达到了最先进结果并位于帕累托前沿。该公司还在论文中发布了训练细节，在 Hugging Face 上提供了此前的开放权重，并计划通过 Kapitsa 提供支持本地 Mac 推理的 v1.1 权重；该模型支持约 256K 上下文窗口。这一声明为新兴的多模态决策模型细分领域增添了竞争压力，其中基准排名和可部署性都很重要。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xr4hkm/artificial_analysis_multimodal_decision_model/)

## 📰 重点报道

### 多模态与具身智能

- **VFlash 通过 Flash Primitive Decoding 加速视觉规划** — VFlash 引入 Flash Primitive Decoding，以降低为物理 AI 任务生成点、边界框和轨迹的逐 token 成本，目标是在机器人和自动驾驶中实现更快、更准确的视觉规划。 [来源-huggingface](https://huggingface.co/papers/2611.08449)
- **SLA 通过持续预训练扩展空间-语言-动作模型** — SLA 是一个空间-语言-动作基础模型，通过在广泛的机器人经验上进行持续预训练来学习可迁移的 3D 空间理解，旨在将空间推理从任务特定适配转变为基础模型的通用能力。 [来源-huggingface](https://huggingface.co/papers/2611.08373)

### 智能体与持续学习

- **Harness-S 通过从同级 Harness 学习来训练可泛化智能体** — Harness-S 使用多个同级 harness 变体来选择性地挽救失败，并将能力迁移到单一策略中，使其在原始 harness 下仍然有效，解决 harness 演化中的局部性、互补性和非平稳性问题。 [来源-huggingface](https://huggingface.co/papers/2611.04277)
- **8B 模型在第 1 天新闻上保持 90.7% 准确率，LoRA 为 26.7%** — 一项据称使用 Apertus-8B 的持续学习实验将四天真实新闻保留在权重中，第 1 天准确率为 90.7%，而反复训练的 LoRA 为 26.7%，同时 GSM8K 保持在基线附近；不过该方法未公开，并计划进行封闭复跑。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xq748x/continual_learning_on_4_days_of_real_news_an_8b/)

### 高效长上下文与训练

- **Muir 线性注意力将 10M token KV 状态压缩至 25MB** — Google Research 的 Muir 使用敏感度分配门控和匹配滤波读出，将 10M token 历史压缩为 25MB 状态，同时提升回看范围和门控效率，解决慢通道眩光以及写入-擦除敏感性问题。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xplbuu/muir_linear_attention_with_sensitivityallocated/)
- **Hugging Face 发布使用 Megatron-LM 的 MoE 训练手册** — Hugging Face 的指南涵盖硬件测试、稠密基线、MoE 层内部结构、服务和 RL，并附有来自约 80 万 GH200 GPU 小时的代码和建议，使前沿 MoE 训练更可复现。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xorgq0/the_ultimate_moe_training_handbook_training/)

### 实时多模态接口

- **Boson AI 发布 Higgs Realtime Duplex 全双工 45B MoE 语音模型** — Boson AI 的 45B MoE 模型可边听、边看、边说，同时运行后台思考、工具调用和任务委派，以 160 毫秒块处理音频、视频、人脸和文本；该模型非开放权重，Duplex API 访问需通过候补名单。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xpn5pv/higgs_realtime_duplex_a_45b_moe_fullduplex_model/)

## ⚡ 快讯速览

- **DialFork 基准测试瞄准对话式智能体中的程序性幻觉** — DialFork 推出一个用于对话式智能体中程序性幻觉的基准测试。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xofjrn/dialfork_a_benchmark_for_procedural_hallucination/)
- **AI 智能体向增强人类能力的认知共生体演进** — 一篇新论文将 AI 智能体定义为增强人类能力的认知共生体。 [来源-huggingface](https://huggingface.co/papers/2611.05376)
- **解耦预测决策使用共享条件预测器服务智能体** — 该工作提出面向智能体的解耦预测决策，并采用共享条件预测器。 [来源-huggingface](https://huggingface.co/papers/2611.02075)
- **OpenMausBot 推出开源本地 AI 机器人团队替代方案** — OpenMausBot 提供开源本地 AI 机器人团队替代方案。 [来源-github](https://github.com/milind-soni/OpenMausBot)
- **Billion-Context：面向长会话的 LLM 上下文压缩插件** — Billion-Context 是一个面向长会话的 LLM 上下文压缩插件。 [来源-github](https://github.com/ranxianglei/billion-context)
- **NVIDIA 预览面向 GPU 裸金属的 Kubernetes Engine** — NVIDIA 预览面向 GPU 裸金属工作负载的 Kubernetes 引擎。 [来源-github](https://github.com/dsx-ai-factory/nvke)
- **扩散模型在实验性 POC 中生成神经网络权重** — 一项实验性概念验证探索扩散模型生成神经网络权重。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xqsl8d/what_if_diffusion_models_generates_neural_network/)
- **爱好者使用极简注意力视觉编码器训练本地 VLA 模型** — 一名爱好者使用极简注意力视觉编码器训练了本地 VLA 模型。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xqrtcz/locally_trained_vla_model_with_minimal_attention/)
- **GRFNet：用于多通道时间序列分类的轻量级 PyTorch 模型** — GRFNet 是一个用于多通道时间序列分类的轻量级 PyTorch 模型。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xqqj67/grfnet_pytorch_model_for_multichannel_timeseries/)
- **可玩的 Pokémon Red 扩散世界模型搭配 System 1/2 智能体 Harness** — 一个可玩的 Pokémon Red 扩散世界模型与 System 1/2 智能体 harness 搭配。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xqt0pk/i_trained_a_playable_diffusion_world_model_of/)
- **CASP-DREAM TAP 挑战赛推出 TCR–肽-MHC 激活预测基准** — CASP-DREAM TAP 挑战赛推出 TCR–肽-MHC 激活预测基准。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xpn4gp/caspdream_tap_challenge_tcr_peptidemhc_activation/)
- **GAP Transformer 将注意力和 MLP 合并为一个门控模块** — GAP Transformer 将注意力和 MLP 处理合并为一个门控模块。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xr47tw/i_merged_attention_and_mlp_processing_into_a/)
- **稀疏预测层级在无反向传播的国际象棋上未能匹敌 Lc0** — 一项实证评估发现，在没有反向传播的情况下，稀疏预测层级在国际象棋上未能匹敌 Lc0。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xov58r/empirical_evaluation_of_sparse_predictive/)
- **Reddit 讨论跨 6 个流的持续保留** — 一场 Reddit 讨论考察跨六个流的持续保留。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1xr9d9y/continual_retention_across_6_streams_r/)

---

*由 AI 新闻智能体生成 | 2026-11-08*