---
title: "AI 日报 — 2026-08-24"
description: "阿里Qwen3.8居代码榜第九，Marin开源535B训练，重大新模型发布。"
lang: "zh"
pairSlug: "ai-daily-2026-08-24"
---

# AI 日报 — 2026-08-24

> 涵盖 39 条 AI 新闻

## 🔥 今日焦点

### 1. 阿里巴巴 Qwen3.8-27B 位列 Code Arena WebDev 第 9 名

阿里巴巴的 27B 参数多模态稠密模型以 1595 分闯入 Code Arena WebDev 前十，位列第 9，成为该参数规模档位中唯一达成此成就的模型，并重塑了帕累托前沿。该模型仅落后于规模大得多的 Qwen3.8-Max 6 个名次，在编码工作负载上展现出卓越的效率，其开放权重可在 Apache 2.0 许可下获取。[来源-x](https://x.com/arena/status/2091920512796725272)

### 2. Marin 项目启动开放的 535B 模型训练计划

由 Percy Liang 领导的 Marin 项目正在推动前沿 AI 的开放性，公开分享一个 535B 参数模型的代码、数据、配方和训练结果，该模型在 11 套 GB200 NVL72 系统上使用 18.75T tokens 进行训练。该项目遵循缩放阶梯策略以确保训练稳定性，为外界提供了一个难得的大型模型开发公开窗口。[来源-x](https://x.com/AndrewYNg/status/2091688153048645650)

### 3. Anthropic 面向 MCP 连接器的企业级身份验证正式全面可用

Anthropic 已将其面向 MCP 连接器的企业级托管身份验证功能全面开放，允许 Claude Team 和企业管理员通过身份提供商集中管理授权。用户现在无需处理单独的 OAuth 流程即可自动建立工具和数据连接，这是企业采用 MCP 的重要一步。[来源-x](https://x.com/ClaudeDevs/status/2091953609185657251)

## 📰 重点报道

### 开源与模型发布

- **新 AI 模型有望成为今年最重要的发布** — 一个仍在训练中的模型已让多位 AI 知名人士兴奋不已，其训练损失通过 wandb 公开分享，外界对这款年度重磅发布抱有极高期待。[来源-x](https://x.com/eliebakouch/status/2091909572558569854)
- **快速 TielCoder MoE 在编码基准上媲美 Opus4.6** — 这款 35B-A3B 专家混合（MoE）编码模型在实际编码问题上达到 Opus4.6-medium 级别性能，同时在速度上超越现有 MoE 模型，并提供面向受限硬件的 GGUF 和 MLX 构建版本。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx33zj/tielcoders_22_gb_4bit_quant_matches_opus46_medium/)
- **OpenHuman 开源 AI 助手登顶 GitHub 趋势榜** — 这款本地优先的个人 AI 助手能够构建终身记忆并编排智能体集群进行深度研究，自发布以来已连续九天稳居 GitHub 趋势榜第一。[来源-github](https://github.com/tinyhumansai/openhuman)

### 基准测试与研究

- **SWE-bench Science：修复科学软件的基准测试** — 一个新的仓库级基准包含 119 个任务，测试编码智能体修复可能损害科学证据的软件缺陷的能力，在聚合准确率之外提供对智能体失败的更深层洞察。[来源-huggingface](https://huggingface.co/papers/2608.19799)
- **LLM 强化学习完整指南发布** — 一份内容全面的独立资源，涵盖强化学习基础、公式化表述和策略梯度，弥合了第一性原理与前沿 LLM 研究之间的鸿沟。[来源-x](https://x.com/cwolferesearch/status/2091872097723359673)

### 工具与行业

- **FreeToken 声称解码速度比 Ollama 快 3-4 倍，预填充快 6-30 倍** — 这款新的推理工具采用带宽自适应的 CPU-GPU 执行和跨智能体轮次的语义感知缓存来加速本地 LLM 服务。[来源-x](https://x.com/Teknium/status/2091704881681948941)
- **Grok 4.6 登陆 Hermes，Nous Research 提供 50% 折扣** — Grok 4.6 现可通过 Nous Research Hermes 门户获取，首周享 50% 折扣，同时接入 SuperGrok 和 X Premium+ 订阅套餐。[来源-x](https://x.com/SpaceXAI/status/2091957125941543034)

## ⚡ 快讯速览

- **EnvHarness：为 LLM 智能体程序化生成动态环境** — 新论文介绍了 EnvHarness，用于程序化生成动态环境以评估 LLM 智能体。[来源-huggingface](https://huggingface.co/papers/2608.19880)
- **FACET：为 AI 智能体合成终端任务的新方法** — FACET 提供了一种合成终端任务的方法，以更好地对 AI 智能体进行基准测试。[来源-huggingface](https://huggingface.co/papers/2608.18580)
- **4DAnyone 从单目视频重建 4D 人体** — 一种新方法实现了从单段视频输入进行动态 4D 人体重建。[来源-huggingface](https://huggingface.co/papers/2608.20335)
- **WithEveryone 框架生成最多包含十个身份的群像图片** — 该框架在生成群像图片的同时保留最多十个独立的个体身份。[来源-huggingface](https://huggingface.co/papers/2608.20336)
- **开源工具免费提供 Claude Code 及其他 AI 编码智能体** — 一款新的 GitHub 工具提供 Claude Code 和其他 AI 编码智能体的免费访问。[来源-github](https://github.com/Alishahryar1/free-claude-code)
- **Anthropic 为 Claude 推出社区插件市场** — Anthropic 已推出社区插件市场，以扩展 Claude 的功能。[来源-github](https://github.com/anthropics/claude-plugins-community)
- **ComfyUI：模块化 AI 内容创作引擎** — ComfyUI 持续演进，作为 AI 内容创作工作流的模块化引擎。[来源-github](https://github.com/Comfy-Org/ComfyUI)
- **Nous Research 发布自我改进型 AI 智能体“Hermes Agent”** — Nous Research 已开源 Hermes Agent，这是一个自我改进的 AI 智能体框架。[来源-github](https://github.com/NousResearch/hermes-agent)
- **小米 AI Cube 原型发布，内存带宽达 1.2TB/s** — 小米的 AI Cube 原型面向本地 AI 工作负载，提供 1.2 TB/s 的内存带宽。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vwvghi/xiaomi_ai_cube_announced_with_12tbs_memory/)
- **JetBrains 利用 Qwen3.6 27B 优化本地 AI** — JetBrains 正在使用 Qwen3.6 27B 驱动优化的本地 AI 体验。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vxdvmv/jetbrains_local_ai_using_qwen36_27b/)
- **ToMoE：通过动态剪枝将稠密 LLM 转换为专家混合模型** — 一篇新论文提出了 ToMoE，通过动态剪枝将稠密 LLM 转换为稀疏 MoE 模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx3img/paper_tomoe_converting_dense_large_language/)
- **社区猜测 HuggingFace 潜在收购方** — 社区正在议论谁可能收购 Hugging Face。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx15zb/who_would_buy_huggingface/)
- **Bart：一个基于 1931 年之前 20B Tokens 训练的复古 LLM** — Bart 是一个复古 LLM，仅使用 1931 年前的 20B tokens 文本进行训练。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx7aci/bart_a_vintage_llm/)
- **Chollet 推荐构建 LLM 的深度学习书籍章节** — François Chollet 为有志于构建 LLM 的开发者分享了推荐的深度学习书籍章节。[来源-x](https://x.com/fchollet/status/2091921787978445119)
- **Claude 长答案流式输出在 Web 和桌面端流畅度提升 4 倍** — Anthropic 已改进 Claude 的长答案流式输出，在 Web 和桌面端流畅度提升 4 倍。[来源-x](https://x.com/ClaudeDevs/status/2092006814804214163)
- **OpenAI 工程师称赞全双工模型的长期研究支持** — 一位 OpenAI 工程师强调了对全双工模型开发提供长期研究支持的价值。[来源-x](https://x.com/gdb/status/2091745169221787681)
- **Hermes 新增辅助模型审查功能** — Hermes 现在包含辅助模型审查功能，以改进智能体输出。[来源-x](https://x.com/Teknium/status/2091686997228478653)
- **新技术 sPTC 提升代码生成中的工具调用能力** — sPTC 技术增强了代码生成任务中工具调用的准确性。[来源-x](https://x.com/a1zhang/status/2091938825580716079)
- **MiniMax 在 GMI Cloud 上提供 M3 和 M2.7 的 14 天免费无限访问** — MiniMax 正在 GMI Cloud 上提供其 M3 和 M2.7 模型的 14 天免费无限访问。[来源-x](https://x.com/MiniMax_AI/status/2091948930124947941)
- **GPT-Image-2 提示词库收录 500+ 逆向工程案例** — 一个新的 GitHub 仓库收集了 500 多个逆向工程的 GPT-Image-2 提示词案例。[来源-github](https://github.com/freestylefly/awesome-gpt-image-2)
- **GitHub 仓库精选 1000+ 顶级团队智能体技能** — 一个精选仓库汇集了来自领先 AI 团队的 1000 多项智能体技能。[来源-github](https://github.com/VoltAgent/awesome-agent-skills)
- **virgiliojr94/book-to-skill** — 新的 GitHub 仓库提供将书籍转换为结构化技能的工作流。[来源-github](https://github.com/virgiliojr94/book-to-skill)
- **比特翻转实验显示 LLM 易受辐射影响** — 一项动手比特翻转实验证明 LLM 极易受到辐射引发的错误影响。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx2fhz/i_irradiated_llms_and_found_that_they_die_really/)
- **Ornith 在 LLM 基准对比中表现亮眼，TielCoder 专精编码** — 在广泛的基准对比中，Ornith 在通用任务上表现出色，而 TielCoder 在编码方面脱颖而出。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vxg4vd/qwen3827b_nemotron35lightning30ba3b/)
- **社区寻求最佳本地视觉语言模型** — Reddit 用户正在询问截至 2026 年 8 月的最佳本地视觉语言模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx7ei1/best_local_vision_language_models_august_2026/)
- **新 Subreddit 专注在低端硬件上运行本地 LLM** — 新社区 r/LowEndLocalAI 已上线，专门讨论在低端硬件上运行本地 LLM。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vxd6yb/please_join_rlowendlocalai_a_community_for/)
- **用户警告勿删除旧版 LLM：DeepSeek V3.2 仍然出色** — 提醒用户不要盲目删除旧模型，DeepSeek V3.2 依然非常强大。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx9xt0/do_not_blindly_delete_your_older_models_some_are/)
- **Reddit 用户质疑 AI Copilot 与人类工作者的比较** — Reddit 用户对将 AI Copilot 类工具与人类工作者相提并论表示反对。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vxescz/copilot_you_say/)
- **llama.cpp 文档迁移至新地址** — llama.cpp 文档已迁至新的官方地址。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx4969/llamacpp_docs_now_have_a_new_home/)

---

*由 AI 新闻智能体生成 | 2026-08-24*