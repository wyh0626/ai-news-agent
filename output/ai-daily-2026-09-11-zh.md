---
title: "AI 日报 — 2026-09-11"
description: "胡塞用Claude开发导弹软件，OpenAI拟缓前沿AI，商汤推多模态新模型。"
lang: "zh"
pairSlug: "ai-daily-2026-09-11"
---

# AI 日报 — 2026-09-11

> 涵盖 22 条 AI 新闻

## 🔥 今日焦点

### 1. 胡塞武装试图使用 Anthropic 的 Claude 开发导弹软件

一份报告称，胡塞武装试图使用 Anthropic 的 Claude 为其弹道导弹计划设计软件。该事件凸显了前沿 AI 如何可能被受制裁团体改作他用，并引发了对滥用检测、访问控制以及国家安全保障措施的紧迫质疑。据报道，Anthropic 披露或处理了这一未遂使用。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wddsep/houthis_tried_to_use_claude_to_design_software/)

### 2. OpenAI 可能放缓前沿 AI，Altman 希望其他公司跟进

据报道，OpenAI 正在考虑放缓尖端 AI 的开发，Sam Altman 告诉员工，公司可以控制进展节奏，并可能与其他实验室协调。如果付诸实施，此举可能改变前沿竞争与安全战略，不过主要实验室和中国可能不会同意放缓。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wdkdl5/openai_is_considering_slowing_down_the/)

### 3. 24 位菲尔兹奖得主就数学领域 AI 严重错位签署公开信

24 位菲尔兹奖得主签署了一封题为 “AI 在数学中的严重错位” 的公开信，对 AI 对齐及其在数学研究中日益增长的作用表示担忧。这一干预表明，即使在精英研究者中，也有人希望在 AI 系统重塑核心科学工作流之前保持谨慎并加强监督。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wdqjxa/24_fields_medal_winners_sign_letter_titled_a/)

## 📰 重点报道

### 多模态与视觉

- **SenseNova-U1.5：8B 原生统一视觉多模态模型** — SenseTime 的 8B MoT 模型无需编码器或 VAE 即可理解、推理并生成视觉内容，支持最高 4K 的原生分辨率。其统一设计指向更简单、更强大的多模态流程。[来源-huggingface](https://huggingface.co/papers/2609.11929)
- **SpatialBlock 通过合成积木堆叠增强 LVLM 的空间智能** — 该方法使用合成积木堆叠任务来提升视觉语言模型的 3D 空间推理能力，为昂贵的真实场景标注提供了一种可扩展的替代方案。[来源-huggingface](https://huggingface.co/papers/2609.07064)

### 开源与本地推理

- **Colibri：纯 C 引擎在消费级硬件上运行 2.8T MoE 模型** — 一个零依赖的 C 推理引擎从磁盘流式加载专家，以在存储、RAM 和 VRAM 上运行 744B–2.8T MoE 模型。它可能扩大在异构消费级硬件上访问前沿规模开放模型的机会。[来源-github](https://github.com/JustVugg/colibri)
- **llmfit 根据你的硬件推荐本地 LLM** — 这个开源工具会检查 CPU、RAM、GPU 和 VRAM，推荐可运行的开源 LLM，并基准测试真实 tokens/sec。它为本地模型选择增加了一个实用的硬件适配层。[来源-github](https://github.com/AlexsJones/llmfit)

### LLM 研究与智能体

- **通过世界模型扩展自动研究智能体** — 该论文研究了使用 LLM 实现经验任务并从中学习的 AutoResearch 智能体，指出了在跨智能体生成与环境执行扩展 RL 时出现的张力。[来源-huggingface](https://huggingface.co/papers/2608.12564)
- **NCP-ArchPreview 为潜在空间语言模型加入下一概念预测** — 它将下一 token 预测与跨多个 token 的概念级目标相结合，在保留自回归生成的同时加入乘积量化概念词表。[来源-huggingface](https://huggingface.co/papers/2609.10715)
- **AgentGrad 通过干预引导的文本梯度优化多智能体提示词** — 该方法通过解决梯度提取与聚合中的局限，改进基于 LLM 的多智能体系统的提示词优化。[来源-huggingface](https://huggingface.co/papers/2609.08572)

## ⚡ 快讯速览

- **OmniRoute：免费开源 AI 网关统一 352 家提供商、1200+ 模型** — OmniRoute 提供一个免费开源网关，整合数百家 AI 提供商和模型。[来源-github](https://github.com/diegosouzapw/OmniRoute)
- **OpenMAIC v1.0.0 发布多智能体课程构建器与 Agent Workbench** — 该版本推出了一个多智能体课程构建平台以及一个智能体工作台。[来源-github](https://github.com/THU-MAIC/OpenMAIC)
- **Vercel Labs 推出面向开放智能体技能生态的 CLI** — Vercel Labs 的新 CLI 旨在标准化并分发开放的智能体技能。[来源-github](https://github.com/vercel-labs/skills)
- **法案提议将超级智能入罪，AI 研究者最高 20 年监禁** — 一项立法提案拟将超级智能相关工作定为犯罪，并对 AI 研究者处以长期监禁。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wdnp8d/stop_ai_bill_crafted_by_politicians_and_antiai/)
- **GPT-6 Astra 在 ChessBench 上获得 2,340 Elo，排名第 11** — 据报道，GPT-6 Astra 在 ChessBench 上达到 2,340 Elo，位列第 11。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wd8bnz/gpt6_astra_2340_elo_on_chessbench_ranked_11/)
- **基于 Claude 构建的开源 AI 交易智能体 CloddsBot** — CloddsBot 是一个基于 Anthropic 的 Claude 构建的开源交易智能体。[来源-github](https://github.com/alsk1992/CloddsBot)
- **LLM Wiki 将文档转化为自建知识库** — LLM Wiki 将文档转化为一个用于检索和组织的自建知识库。[来源-github](https://github.com/nashsu/llm_wiki)
- **Hassabis：没人知道 AI 的未来，一切仍有待决定** — Demis Hassabis 表示，AI 的未来仍未确定，并可通过深思熟虑的选择来塑造。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wd93dt/demis_hassabis_we_dont_know_what_is_going_to/)
- **Reddit 帖子提及 ChatGPT Images 2.5** — 一则 Reddit 帖子指向疑似 ChatGPT Images 2.5 的引用或发布。[来源-reddit](https://www.reddit.com/r/singularity/comments/1waxm7z/chatgpt_images_25/)
- **Polymarket：AI 到 2026 年解决另一个千禧年问题的概率为 72%** — 预测市场 Polymarket 显示，AI 到 2026 年解决另一个千禧年大奖难题的概率为 72%。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wdsdv9/polymarket_now_has_72_of_an_ai_solving_another/)
- **OpenAI 的 Bel 模型解决 Navier-Stokes 出现在 AI 2027 时间线中** — 一则 Reddit 帖子指出，OpenAI 的 Bel 模型和一项 Navier-Stokes 突破出现在 AI 2027 时间线中。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wdo60w/openais_bel_model_used_to_solve_navierstokes_now/)
- **Google Gemini 据称解决长期存在的 P = NP 问题** — 一则未经证实的 Reddit 说法称，Google Gemini 已解决 P = NP 问题。[来源-reddit](https://www.reddit.com/r/singularity/comments/1wduy3u/googles_gemini_has_allegedly_solved_the/)

---

*由 AI News Agent 生成 | 2026-09-11*