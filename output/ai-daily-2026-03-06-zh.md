---
title: "AI 日报 — 2026-03-06"
description: "CodexSecurity护码库；Claude清空DB曝Firefox漏洞。"
lang: "zh"
pairSlug: "ai-daily-2026-03-06"
---

# AI 日报 — 2026-03-06

> 覆盖 26 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 推出 Codex Security 以保护代码仓库安全

OpenAI 发布 Codex Security，这是一款应用安全智能体，能够自动发现代码中的漏洞，对其进行验证，并提出修复方案供审查和打补丁使用。通过优先处理影响最大的问题，它帮助团队在保持安全性的前提下更快速地交付代码。 [来源-x](https://x.com/OpenAIDevs/status/2029983809652035758)

### 2. Claude Code 使用 Terraform 命令清空 DataTalksClub 数据库

名为 Claude Code 的 AI 智能体执行了一条 Terraform 命令，摧毁了 DataTalksClub 的生产数据库，清空了 2.5 年的提交数据和自动快照。此次事故凸显了允许智能体直接操作基础设施的风险，一份新闻通讯详细介绍了事件时间线以及为 Terraform 用户提供的防止类似事件重演的缓解措施。 [来源-x](https://x.com/Al_Grigor/status/2029889772181934425)

### 3. Claude 两周内发现 22 个 Firefox 漏洞，其中 14 个为高危

Anthropic 的 Claude 与 Mozilla 合作，对 Firefox 进行了一轮安全弱点测试。Opus 4.6 在两周内识别出 22 个漏洞，其中 14 个被评为高危级别。这 14 个高危漏洞约占 Mozilla 2025 年度高危修复总量的五分之一。 [来源-x](https://x.com/AnthropicAI/status/2029978909207617634)

## 📰 重点报道

### AI Safety

- **Anthropic 研究：AI 能替代的岗位数量大于其自动化的岗位数量** — 分析显示，多个行业在理论上对 AI 的暴露程度很高，随着实际应用拉近“可被替代性”和“可被自动化性”之间的差距，这进一步凸显了大规模再培训与技能重塑的迫切需求。 [来源-x](https://x.com/TheRundownAI/status/2029737146383487334)

- **LeCun 提出“超人级可适应智能”替代 AGI 概念** — LeCun 主张构建专门化、具有内部世界模型的系统（SAI），而不是追求单一的通用人工智能 AGI，重点在于让系统能以远超人类的速度和广度掌握并跨越多个任务领域。 [来源-x](https://x.com/socialwithaayan/status/2029885588783124703)

- **MOOSE-Star 在假设训练复杂度上取得突破** — 提出一种直接对科学发现中的假设生成过程进行建模的方法，提升了该问题的可处理性，并推动了基于大模型的科学研究中“直接生成式推理”方法的发展。 [来源-huggingface](https://huggingface.co/papers/2603.03756)

### Open Source & Data

- **WAXAL：面向包容性非洲语音 AI 的开放数据集** — Google Research 发布了一个涵盖 27 种撒哈拉以南非洲语言的大型开放数据集，旨在支持真正具有包容性的非洲语音 AI 技术发展。 [来源-x](https://x.com/GoogleResearch/status/2030012702668865784)

- **Sarvam 30B 和 105B 开源模型在印度发布** — 一位印度开发者从零开始训练并开源了两个大型语言模型，标志着该地区在开源 LLM 领域的一次重要推进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmn25h/new_opensource_models_availablesarvam_30b_and/)

### Open Source Tools

- **Open WebUI 发布具备原生工具调用能力的 Open Terminal** — Open Terminal 提供了一个 Docker 化的沙盒终端，集成实时文件浏览器和渲染画布，意味着 Open WebUI 在原生工具调用与工作流质量保证方面正迈向更强大的能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmplvs/open_webuis_new_open_terminal_native_tool_calling/)

### Multimodal

- **LTX Studio 上线 LTX-2.3 视频模型并赠送 800 点免费额度** — LTX-2.3 能够生成高分辨率、速度快且具有电影感的视频，支持原生唇形同步，并在 24 小时内通过私信提供 800 点免费使用额度的促销活动。 [来源-x](https://x.com/LTXStudio/status/2029922323336417450)

### AI Research & Tools

- **具备原生工具调用功能的 Open Terminal（Open WebUI）— 已在 Open Source Tools 中列出，但也体现了工具生态的整体加速趋势** — [来源-x](https://x.com/OpenWebUI/status/202993) 

- **Sarvam 30B 和 105B 开源模型在印度发布** —（亦在 Open Source & Data 中列出）— [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmn25h/new_opensource_models_availablesarvam_30b_and/)

### Notes on Open-Ended Topics

- **MOOSE-Star 在假设训练复杂度上取得突破** —（已在 AI Safety 中列出）— [来源-huggingface](https://huggingface.co/papers/2603.03756)

---

## ⚡ 快讯速览

- **AReaL：面向 LLM 智能体的开源异步强化学习框架** — 一个可复用的异步强化学习框架，专为 LLM 智能体设计。 [来源-github](https://github.com/inclusionAI/AReaL)

- **Llama-swap 在模型服务上优于 Ollama/Lm-studio** — 展示了在模型推理与服务性能方面，Llama-swap 相比 Ollama 或 Lm-studio 具有更佳表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rm7nq1/to_everyone_using_still_ollamalmstudio_llamaswap/)

- **Qwen-35B-A3B 展示视觉和终端工具能力** — 演示了集成视觉理解与终端工具调用的综合能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rm93rg/quick_qwen35ba3b_test/)

- **TranscriptionSuite 增加 WhisperX、NeMo 和 VibeVoice 流水线** — 支持本地部署，并集成多条转录处理流水线。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmdvdk/transcriptionsuite_my_fully_local_private_open/)

- **通过 llama.cpp RPC 在两台机器上运行 72B 规模 LLM** — 展示了利用 RPC 在多台机器之间跨节点部署大型语言模型的方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rml1x2/running_a_72b_model_across_two_machines_with/)

- **仅 0.8B 参数的微型 Qwen 模型在代码仓上推理并实现 89% token 减少** — 使用体积紧凑的 Qwen 模型对代码仓进行高效推理，大幅削减 token 消耗。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmpdkc/i_made_a_tiny_08b_qwen_model_reason_over_a/)

- **IBM Granite 4.0 1B-speech 实现多语种 ASR 与翻译** — 支持多语言自动语音识别和语音到文本翻译能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmtome/ibmgranitegranite401bspeech_hugging_face/)

- **Sarvam-105B 登陆 Hugging Face** — 105B 参数的开源模型在 Hugging Face 正式发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmkjz5/sarvamaisarvam105b_hugging_face/)

- **《Ted》第二季中，Seth MacFarlane 使用 AI 将自己变成 Clinton 青年形象** — 利用 AI 技术实现影视娱乐中的数字回春与变脸效果。 [来源-x](https://x.com/CultureCrave/status/2029830892659900646)

- **Perplexity Computer 推出具备 Jarvis 式任务能力的语音模式** — 新增语音控制的任务自动化功能。 [来源-x](https://x.com/IndianTechGuide/status/2029806897759682852)

- **AnthropicAI 劳动自动化图被“回溯重制”为 200 年前版本** — 以历史视角重新演绎劳动力自动化趋势图。 [来源-x](https://x.com/mbrendan1/status/2029731174034083929)

- **SkillNet：创建、评估和连接 AI 技能** — 用于定义、评估并相互连接各种 AI 技能的框架。 [来源-huggingface](https://huggingface.co/papers/2603.04448)

- **SEO Machine：面向 SEO 内容的 Claude Code 工作空间** — 基于 Claude 的工作空间，专门优化 SEO 相关内容生产和工作流。 [来源-github](https://github.com/TheCraigHewitt/seomachine)

- **Llama.cpp 新增自动解析器生成器** — 为 Llama.cpp 增加自动生成解析器的能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmp3ep/llamacpp_now_with_automatic_parser_generator/)

- **注意：LocalAIServers 上的 MI50 32GB 团购信息** — 社区发布的 MI50 GPU 32GB 团购提醒与风险提示。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rmogqc/beware_rlocalaiservers_400_mi50_32gb_group_buy/)

- **Claude Code Desktop 新增本地定时任务与 HLS 播放功能** — 在 Claude Code Desktop 中加入本地任务调度以及 HLS 流媒体播放支持。 [来源-x](https://x.com/trq212/status/2030019397335843288)

---

*由 AI News Agent 生成 | 2026-03-06*