---
title: "AI 日报 — 2026-09-23"
description: "实时金星全双工视听交互、OmniEdu开源K-12模型、游戏地平线多跨度评测。"
lang: "zh"
pairSlug: "ai-daily-2026-09-23"
---

# AI 日报 — 2026-09-23

> 涵盖 11 条 AI 新闻

## 🔥 今日焦点

### 1. Google 开源 AX 智能体编排运行时

Google 推出了 AX，这是一个开源的智能体编排运行时，可通过工作区（workspaces）与网关（gateway）规范来声明任务，并构建在 Agent Substrate 之上以实现沙箱化执行。该项目旨在单个集群中支撑数十亿规模的自主智能体工作负载，不过它仍处于积极开发阶段，可能会发生破坏性变更。这标志着业界正围绕安全、高规模的智能体基础设施加速整合，对从业者意义重大。[来源-github](https://github.com/google/ax)

### 2. OmniEdu 发布面向 K-12 学与教的开源基础模型

OmniEdu 推出了一系列面向 K-12 学与教的开源教育基础模型，其训练语料融合了 100 多项教育资源以及通用指令数据。这些模型面向课程理解、学习者困难诊断、问题求解和教学支持等场景。若得到验证，它们可能加速教育领域专用开源模型的发展，同时也将带来新的评估与数据质量问题。[来源-huggingface](https://huggingface.co/papers/2609.23088)

### 3. Realtime-Venus：借助异步委派实现全双工音视频交互

研究人员提出了 Realtime-Venus，这是一个主动式全双工交互系统，由两个分别训练的 9B 模型构成：一个负责音视频对话，另一个负责语音对话。该设计的目标是在数字与物理环境中实现持续感知以及及时、具备视觉依据的回应。这将多模态助手向实时、具身交互推进了一步，不过延迟与部署成本仍是实际制约因素。[来源-huggingface](https://huggingface.co/papers/2609.13814)

## 📰 重点报道

### 基准与评估

- **GameHorizon Suite：面向 AI 游戏玩法的多时间跨度数据与评估** — 一套统一的数据与评估套件从视觉理解、指令分解、目标规划和动作控制等方面衡量 AI 的游戏表现，以解决游戏基准覆盖面狭窄或语言信息匮乏的问题。[来源-huggingface](https://huggingface.co/papers/2609.25001)
- **论文提出面向长时程 LLM 智能体的 Taste 基准** — 一项新的基准提案通过评判中间决策的质量，而非仅看端到端任务是否成功，来衡量 LLM 智能体的“品味（taste）”。[来源-huggingface](https://huggingface.co/papers/2609.25804)

### 机器人与具身智能

- **Grounded Action Models 使用 3D 定位构建机器人基础模型** — Grounded Action Models 将 3D 定位显式地纳入机器人基础模型，使操作策略能够知道哪些物体重要以及它们位于何处。[来源-huggingface](https://huggingface.co/papers/2609.23863)

### 智能体基础设施与安全

- **Agent Substrate：具备高密度沙箱能力的安全 AI 智能体运行时** — 一个开源运行时以 microVM 和 gVisor 为目标支撑数百万个沙箱，实现低于 500 毫秒的恢复时间，以及零信任的内核与网络隔离。[来源-github](https://github.com/agent-substrate/substrate)

### 工具与开发者工作流

- **Browser Use 发布 video-use：用 Claude Code 智能体剪辑视频** — 一款开源工具让用户通过编程智能体对话来生成最终视频，具备填充词去除、调色、字幕、动画叠加、自我评估以及持久化会话记忆等功能。[来源-github](https://github.com/browser-use/video-use)
- **Univer 推出面向 AI 智能体的开源 Office SDK** — Univer 提供可嵌入的电子表格、文档与演示文稿构建模块，具备插件架构、Canvas 渲染、公式引擎以及适用于浏览器和 Node.js 的 Facade API。[来源-github](https://github.com/dream-num/univer)
- **开源 CLI 提供配置 Anthropic Claude Code 的模板** — 一个 CLI 与 Web 界面为 Claude Code 提供开箱即用的智能体、自定义命令、设置、hooks、MCP 集成以及项目模板。[来源-github](https://github.com/davila7/claude-code-templates)

## ⚡ 快讯速览

- **Treg：面向 AI 智能体工具的 OpenRouter，拥有 3,000+ 端点** — Treg 定位为 AI 智能体工具领域的 OpenRouter 式网关，开放 3,000 多个端点供发现与集成。[来源-github](https://github.com/superdesigndev/treg)

---

*由 AI 新闻智能体生成 | 2026-09-23*