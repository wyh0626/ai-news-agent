---
title: "AI 日报 — 2026-06-27"
description: "AI安全治理成焦点，大量诈骗，GPT组受美监管，Mythos5恢复关键基础设施。"
lang: "zh"
pairSlug: "ai-daily-2026-06-27"
---

# AI 日报 — 2026-06-27

> 涵盖 21 条 AI 新闻

## 🔥 今日焦点

### 1. 阿里巴巴对 Claude 发动蒸馏攻击：2880 万次交互、2.5 万个欺诈账号

Anthropic 向美国政府披露，阿里巴巴在 2026 年 4 月到 6 月期间，对 Claude 发动了迄今为止规模最大的已知蒸馏攻击，利用近 25,000 个欺诈账号生成约 2,880 万次交互。此次事件凸显了围绕大语言模型的持续安全风险与模型提取威胁，并对企业防御中的合规监管与供应商风险管理产生影响。[来源-x](https://x.com/yacinelearning/status/2070699602492166440)

### 2. OpenAI 在美国监管下预览 GPT-5.6 三款模型 Sol、Earth、Luna

OpenAI 正式预览 GPT-5.6 系列，命名为 Sol、Earth 和 Luna，其发布节奏与 Anthropic 的 Fable 5 相呼应。公司正与美国政府协调一个受限的合作伙伴预览版本，以避免出口管制方面的对峙，在监管机构认为合适之前，将这些能力置于监管审查之下。早期结果声称，Sol 在 Terminal-Bench 2.1 上达成新的 SOTA，并在整体效率上取得显著提升。[来源-reddit](https://www.reddit.com/r/singularity/comments/1ugdy62/openai_is_officially_unveiling_a_preview_of_the/)

### 3. Anthropic 为美国关键基础设施恢复 Claude Mythos 5 访问

Anthropic 表示，自 6 月 12 日起一直与美国政府合作，恢复 Claude Mythos 5 和 Fable 5 的访问权限。政府已批准将 Mythos 5 重新部署给部分运营和防御关键基础设施的美国机构，访问正在被快速恢复。公司计划进一步扩大 Mythos 5 的可用范围，并再次将 Fable 5 向更广泛用户开放。[来源-x](https://x.com/AnthropicAI/status/2070665903440871779)

---

## 📰 重点报道

### LLM 与推理加速

- **DSpark 推 speculative decoding，将 LLM 推理提速 50%** — 来自 DeepSeek AI 的 DSpark 将 speculative decoding 与半并行策略结合，在生产环境中实现约 50% 的吞吐提升和最高 80% 的延迟降低。这种方法表明，在算力受限的情况下部署更大模型，也能在实际落地中获得可观收益。[来源-x](https://x.com/eliebakouch/status/2070762049362370602)

- **顶级 AI 模型正被其原产国实施访问限制** — 地缘政治层面的管控正在限制对领先模型的访问，可能阻碍研究与应用落地。这一趋势突显了政策摩擦正在塑造全球 AI 生态格局。[来源-x](https://x.com/theo/status/2070785625868177671)

### 多模态与机器人

- **Hassabis：AI 可从脑部扫描中重建梦境** — 神经科学研究人员正在使用 AI 视频模型，从大脑数据中重建人们想象的内容，Demis Hassabis 预测，能解码梦境的相关设备有望在不远的将来到来。[来源-reddit](https://www.reddit.com/r/singularity/comments/1ugw8t1/demis_hassabis_ai_can_now_reconstruct_what_people/)

- **基于 In-Context World Modeling 提升机器人控制泛化能力** — 该工作提出，将世界配置视为上下文，使 Vision-Language-Action 模型在面对新的摄像头视角和机器人形态时，只需较少微调即可适应。[来源-huggingface](https://huggingface.co/papers/2606.26025)

### 硬件与开源

- **基于 RTX 5090 搭建的开源家庭 AI 实验室** — 一套个人设备在本地运行 Qwen 3.6、Orinth1.0、GLM 5.2 等模型，并基于定制平台搭建，同时警示前沿模型正被“看门”限制、硬件价格可能上涨，呼吁抓紧入场。[来源-x](https://x.com/AlexFinn/status/2070670926803542304)

### AI 研究与数学

- **AI 在数学领域引发重大争议** — IEEE Spectrum 探讨 AI 正如何影响数学实践，包括新的计算方法，以及围绕证明、严谨性与发现过程的争论。[来源-rss](https://spectrum.ieee.org/ai-in-mathematics)

### AI 治理与政策

- **美国官员担心中国可能在 AI 领域实现反超** — 美国决策者将中美 AI 领导权之争视为一场高风险地缘政治博弈，凸显对全球 AI 主导权的战略焦虑。[来源-reddit](https://www.reddit.com/r/singularity/comments/1uh2zg5/us_officials_fear_supervillain_china_pulling/)

---

## ⚡ 快讯速览

- **开源实验室与前沿 AI 实验室有何本质差异？** — 探讨开源实验室与前沿 AI 实验室之间的差别，以及这对治理和访问权限意味着什么。[来源-reddit](https://www.reddit.com/r/singularity/comments/1uh9d42/whats_separating_open_source_mainly_chinese_labs/)

- **通过更聪明的默认配置，在 token 用量增长时保持 AI 花费不变** — Brian Armstrong 主张，通过更合理的默认设置来控制成本，在 token 使用量不断增加的情况下保持支出稳定。[来源-x](https://x.com/brian_armstrong/status/2070670644577280109)

- **教程：用开源权重 LLM 搭建本地编码 Agent** — 一篇教程介绍如何利用开源权重 LLM 构建本地运行的代码编写代理。[来源-x](https://x.com/rasbt/status/2070871630201463137)

- **GPT-2 安全影响被夸大；安全先验并未改变** — 一篇批评性观点认为，GPT-2 的安全影响被过度渲染，而基础安全假设并未实质变化。[来源-x](https://x.com/sporadica/status/2070673369079701569)

- **OpenAI 计划明年启动 IPO** — 有报道指出，OpenAI 正在谋划于明年进行首次公开募股（IPO）。[来源-rss](https://www.nytimes.com/2026/06/25/technology/openai-ipo-artificial-intelligence.html)

- **按国籍限制前沿 AI 访问是愚蠢之举** — 一篇评论文章认为，基于国籍的前沿模型访问限制适得其反。[来源-reddit](https://www.reddit.com/r/singularity/comments/1ugynjo/gating_frontier_ai_by_nationality_is_such_a_dumb/)

- **内部人士称 Fable 5 的限制可能很快解除** — 内部消息人士预计，针对 Fable 5 的部分限制有望在不久之后被放宽。[来源-reddit](https://www.reddit.com/r/singularity/comments/1uh4xo4/anthropic_and_us_govt_insiders_expect_limits_on/)

- **Yann LeCun 称 xAI 是“失败案例”** — LeCun 公开批评 xAI 的进展，认为其表现令人失望。[来源-reddit](https://www.reddit.com/r/singularity/comments/1ugfgzu/yann_lecun_says_xai_is_a_failure/)

- **美国政府封锁 Gemini 3.5 Pro 访问** — 美国方面阻止了对 Gemini 3.5 Pro 的访问。[来源-reddit](https://www.reddit.com/r/singularity/comments/1uh259r/breaking_news_gemini_35_pro_so_ass_the_us/)

- **GPT-2 曾被认为“过于危险”而不宜公开发布** — 回顾一场关于是否应向公众发布 GPT-2 的历史争论，以及其潜在风险。[来源-reddit](https://www.reddit.com/r/singularity/comments/1ugnbj0/gpt2_is_too_dangerous_to_be_released/)

- **AGI 会诞生在 LLM 中，还是需要完全不同的技术？** — 讨论 AGI 是否会基于现有 LLM 形态诞生，还是需要依赖一种截然不同的技术范式。[来源-reddit](https://www.reddit.com/r/singularity/comments/1uh8q07/is_agi_going_to_be_in_an_llm/)

---

*由 AI News Agent 生成 | 2026-06-27*