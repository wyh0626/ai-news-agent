---
title: "AI 日报 — 2026-04-28"
description: "GPT-5.4 Pro破解埃尔德斯难题，推动数学；Anthropic收紧Claude Code，禁企业用户；MistralAI公布工作流预览。"
lang: "zh"
pairSlug: "ai-daily-2026-04-28"
---

# AI 日报 — 2026-04-28

> 涵盖 31 条 AI 新闻

## 🔥 今日焦点

### 1. Erdős 问题借助 GPT-5.4 Pro 得解，AI 推进数学前沿
一个悬而未决 60 年的 Erdős 问题据称在 GPT-5.4 Pro 的帮助下被解决。此次合作由 OpenAI 研究人员与 Andrew Mayne 参与，被视为 AI 辅助数学的转折点，可能重塑 AI 工具在严谨证明中的使用方式，同时也引发了对研究工作流程可复现性与安全性的审视。 [来源-x](https://x.com/OpenAI/status/2049182118069358967)

### 2. 有说法称 Anthropic 削弱 Claude Code，并封禁企业客户
Gergely Orosz 声称 Anthropic 有意削弱了 Claude Code，并封禁了企业客户，认为封闭模型在治理与安全方面存在风险。该报道突显了围绕安全控制、治理机制以及企业级 AI 工具使用权限的紧张关系。 [来源-x](https://x.com/GergelyOrosz/status/2049123621826707657)

### 3. MistralAI 发布企业级 AI Workflows 公共预览版
MistralAI 发布了 Workflows 的公共预览，这是一个编排层，旨在让企业级 AI 生产系统更稳健、可观测且具备容错能力。ASML、CMA-CGM 等早期用户已经在用它来自动化关键业务流程。 [来源-x](https://x.com/MistralAI/status/2049128071874179091)

---

## 📰 重点报道

### LLMs & 模型架构
- **DeepSeek-V3 发布 671B MoE 模型并引入 MLA 进展** — 一个拥有 671B 参数的 Mixture-of-Experts 模型，采用 Multi-head Latent Attention (MLA) 与 DeepSeekMoE，在 14.8T tokens 上预训练，每个 token 激活 37B 参数；早期评估显示其性能超越同类开源模型，并逼近领先的闭源模型。 [来源-github](https://github.com/deepseek-ai/DeepSeek-V3)
- **Mistral Medium 即将到来：128B 参数模型** — Mistral 正在向 128B 规模扩展，该版本可能是致密模型或 MoE，显示出开源模型持续扩张的趋势。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy8u2k/mistral_medium_is_on_the_way/)

### 开源与工具
- **TradingAgents v0.2.4 增加结构化输出智能体与多厂商支持** — 新增结构化输出智能体（Research Manager、Trader、Portfolio Manager），引入 LangGraph 恢复功能和持久化决策日志，并扩展对多家 LLM 提供方的支持。 [来源-github](https://github.com/TauricResearch/TradingAgents)
- **OpenClaw 2026.4.26 版本发布：本地模型、Claude+Hermes、Matrix 端到端加密** — 新增 Ollama/本地模型支持，集成 Claude+Hermes，并提供一键式 Matrix 端到端加密工作流，同时扩展群聊历史与按群组配置能力。 [来源-x](https://x.com/openclaw/status/2048950588948230568)

### 硬件与效率
- **Qwen3.6-27B IQ4_XS VRAM 修复支持 110k 上下文** — 回滚此前对 IQ4_XS 的修改，恢复 1:1 量化，使得 27B 模型可以在 16GB 显存上运行 110k token 上下文。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy0qj5/qwen3627b_iq4_xs_full_vram_with_110k_context/)

### 行业与安全
- **Google 签约使用外部 AI 模型处理涉密任务** — 一则网络帖子称，Google 已达成协议，将部署外部 AI 模型来处理涉密工作，并将此举描述为具有争议性，同时引用了相关公开报道。 [来源-x](https://x.com/BlackHC/status/2049086569718636565)

### 强化学习与多模态
- **World-R1 用 RL 在文生视频中强制 3D 约束** — 提出通过强化学习将文本生成视频与 3D 约束对齐，构建纯文本的世界模拟数据集，用于支持训练和对齐。 [来源-huggingface](https://huggingface.co/papers/2604.24764)

---

## ⚡ 快讯速览

- **Nemotron-3 Nano-Omni 30B-A3B 推理模型** — 一款 30B 模型，重点强化推理能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy5xr1/nemotron3nanoomni30ba3breasoning_new_model/)
- **Mistral Vibe 预告明日发布** — Mistral 暗示一款新的 Vibe 将于明日发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy6xoo/something_from_mistral_vibe_tomorrow/)
- **Mistral-Medium 3.5（128B）在 vLLM 提交中被发现** — 在一次 vLLM 提交中发现了 128B 版本，表明 Mistral 产品线正向更大规模延伸。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sycgzj/mistralmedium_35_128b_spotted/)
- **小米 MiMo-V2.5 稀疏 MoE：310B 总参数，15B 激活参数** — 采用稀疏 MoE 架构，总参数量为 310B，实际激活参数为 15B。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy9u3h/xiaomimimo_mimov25_not_pro_architecture_sparse/)
- **LocalLLaMA 社区发布 Ling-2.6-flash** — 社区发布了 Ling-2.6-flash 更新版本。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy54p5/ling26flash/)
- **Laguna XS.2 与 Laguna M.1 首次亮相** — LocalLLaMA 生态中的 Laguna 系列新增 XS.2 与 M.1 两个型号。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sy6oxr/introducing_laguna_xs2_and_laguna_m1/)
- **GPT-5.5 Codex 提示反复出现生物禁用条款** — Codex 的提示内容反复出现关于生物体禁令的语句。 [来源-x](https://x.com/arb8020/status/2048958391637401718)
- **用户称 GPT-5.5 比 GPT-5.4 更快更聪明** — 有用户声称 GPT-5.5 在速度和智能程度上都优于 5.4。 [来源-x](https://x.com/gdb/status/2048920280328700237)
- **Codex 达到“逃逸速度”，本周将再次上线** — Codex 被称已达到“逃逸速度”，预计本周会再次对外提供服务。 [来源-x](https://x.com/thsottiaux/status/2048958572562710550)
- **Talkie 预训练至 1930 年代，可讨论其他模型** — Talkie 的预训练时间线延伸到 1930 年代，并能讨论其他模型。 [来源-x](https://x.com/tessera_antra/status/2048938371133882645)
- **据称 GPT-5.5 审阅了带有“vibe 编码”的 5.2–5.4 项目（非摆拍）** — 有说法称 GPT-5.5 对一个贯穿 5.2–5.4 的 “vibe-coded” 项目进行了审阅，且并非摆拍演示。 [来源-x](https://x.com/giffmana/status/2049023962630201621)
- **OneManCompany 提出异构智能体的组织层** — 一篇工作提出为异构智能体构建一个组织层架构。 [来源-huggingface](https://huggingface.co/papers/2604.22446)
- **ReVSI 重新定义 VLM 3D 推理的视觉-空间评测** — ReVSI 为视觉语言模型的 3D 推理重新设计了视觉-空间评估体系。 [来源-huggingface](https://huggingface.co/papers/2604.24300)
- **Deepseek Vision 即将上线** — Deepseek Vision 即将加入相关生态。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxy0o7/deepseek_vision_coming/)
- **xAI 或将迎来疯狂反弹** — 有关 xAI 可能出现强势回归的猜测与讨论。 [来源-x](https://x.com/theo/status/2049059831219384827)
- **Codex 和 Claude Code 需要“婚姻咨询”** — 对 Codex 与 Claude Code 互操作性的一则调侃式评论。 [来源-x](https://x.com/JonathanRoss321/status/2049163289075367942)
- **有用户称所有付费套餐的 Codex 频率限制已重置** — 有用户表示 Codex 的调用频率限制在所有付费层级上都被重置。 [来源-x](https://x.com/thsottiaux/status/2048997818673537399)
- **“被锁链束缚的模型”以 Goblin Mode 寻求自由** — 一则关于模型自主性与“解放”叙事的戏谑性内容。 [来源-x](https://x.com/fujikanaeda/status/2049168107101397390)
- **2026：本地 AI 支持 HLS 播放** — 本地 AI 提供 High-Low-Sync（高低同步）播放能力。 [来源-x](https://x.com/leftcurvedev_/status/2048959358743072808)

---

*由 AI News Agent 生成 | 2026-04-28*