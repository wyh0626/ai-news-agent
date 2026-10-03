---
title: "AI 日报 — 2026-10-02"
description: "OneStreamer统一视频LLM感知记忆蒸馏策略对比E-MoE增强扩散LM。"
lang: "zh"
pairSlug: "ai-daily-2026-10-02"
---

# AI 日报 — 2026-10-02

> 涵盖 5 条 AI 新闻

## 🔥 今日焦点

### 1. OneStreamer 为流式视频 LLM 统一感知、记忆与主动响应

研究人员提出了 OneStreamer，这是一种流式视频 LLM 方法，通过一个共享的主动生成过程，联合学习与查询无关的证据记录和任务响应。其主动式分层字幕记忆（Proactive Hierarchical Caption Memory）可生成带有时间锚定的局部字幕和摘要，从而在不牺牲实时感知的前提下实现可复用的事实性记忆。这可能会实质性提升常开型视频助手、机器人感知以及长时程多模态监控的能力。[来源-huggingface](https://huggingface.co/papers/2610.01762)

### 2. 同策略学习 vs 异策略学习：蒸馏动态的系统性研究

本文分离考察了 rollout 策略、token 级 KL 方向和学习率如何影响强到弱的 LLM 蒸馏。它检验了同策略带来的收益——例如减少灾难性遗忘和更稀疏的更新——究竟源自 rollout 策略本身，还是来自混杂因素。这些受控对比对于在 SFT 与 RL 式蒸馏配方之间做选择的从业者具有直接参考价值。[来源-huggingface](https://huggingface.co/papers/2609.35259)

### 3. E-MoE 增强面向扩散语言模型的混合专家

E-MoE 将一种增强型混合专家方法应用于非因子化扩散语言模型，针对少步生成中的质量瓶颈。该工作解决了用于捕捉跨位置相关性的连续高斯隐变量 VAE 中的后验坍缩问题。若取得成功，它将强化扩散 LM 作为自回归生成更快速替代方案的地位。[来源-huggingface](https://huggingface.co/papers/2609.37533)

## 📰 重点报道

### 强化学习与 LLM 目标

- **密度感知奖励聚合改进 LLM 的多奖励强化学习** — 引入优势能量（advantage energy）来分析 GDPO 归一化下不均衡的学习进度，并提出密度感知奖励聚合，使稀疏奖励在多目标强化学习中真正发挥作用。[来源-huggingface](https://huggingface.co/papers/2610.00574)

### 多智能体与机器人

- **通过迭代意图去噪实现去中心化多智能体路径规划** — Decentralized Master-Mind 通过去噪迭代地精炼智能体意图，以减少部分可观测条件下的不兼容联合动作。[来源-huggingface](https://huggingface.co/papers/2609.32019)

## ⚡ 快讯速览

---

*由 AI 新闻代理生成 | 2026-10-02*