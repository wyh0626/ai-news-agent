---
title: "AI 日报 — 2026-10-03"
description: "OpenAI安全主管因文化崩坏辞职，低成本AI战胜战略棋，Qwen升级工具调用。"
lang: "zh"
pairSlug: "ai-daily-2026-10-03"
---

# AI 日报 — 2026-10-03

> 涵盖 40 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 安全负责人辞职，警告公司文化已“崩坏”
一位 OpenAI 安全负责人已辞职，并警告称公司文化已经崩坏，这使外界对该公司的内部安全优先事项和治理展开新的审视。此次离职之际，前沿实验室正因风险管理、透明度以及速度与安全之间的平衡而面临越来越大的压力。这可能会加剧企业和监管机构对 OpenAI 内部监督的担忧。 [来源-rss](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken)

### 2. AI 终于以低成本击败最强 Stratego 玩家
一个 AI 系统攻克了 Stratego，这是一款长期难以被强 AI 掌握的隐藏信息游戏，并以低成本击败了历史上最强的人类玩家。这项工作在《Nature》论文和 arXiv 预印本中有详细说明，其重要性在于：不完全信息博弈更接近现实世界中不确定性下的规划。它可能推动谈判、安全和多智能体决策方面的进展。 [来源-rss](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/)

### 3. Google 终止对 Gemini Flash 和 Pro 模型的免费访问
据报道，Google 正在取消对 Gemini Flash 和 Pro 的免费访问，引发依赖此前免费层级的用户强烈反弹。此举凸显了提供高性能模型所面临的成本压力，以及行业向商业化变现的转变。开发者可能会越来越多地测试开放权重替代方案，用于原型开发和生产。 [来源-reddit](https://www.reddit.com/r/GeminiAI/comments/1wwalmc/wtf_google_getting_rid_of_free_gemini_flash_and/)

## 📰 重点报道

### 开源模型

- **Qwen3.8-27B Humanlike Chat 2.0 增加工具调用并提升指令遵循能力** — 更新后的 LoRA 微调保留了类人语气，同时加入可用的工具调用和更强的指令遵循能力。这表明社区微调正在缩小与基础模型之间的实用性差距。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wvxl4n/qwen3827bhumanlikechat_20_texts_like_a_human_now/)
- **Aleph Alpha 发布 Kolibri-1：78B 开源模型，支持 1M 上下文** — Kolibri-1 是一个 Apache-2.0 模型，总参数量 78B，激活参数量 3.46B，并支持最多 1M tokens 上下文。它面向长上下文企业和研究工作负载，采用开放许可证。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwl7y6/alephalphakolibri1_hugging_face_78b_parameters/)

### 推理与效率

- **两个 300B MoE 模型在一台 128GB 迷你 PC 上运行** — Kyojin 基于 ExLlamaV3 的引擎将 GLM-5.3-Flash 和 MiMo-V2.6-Flash 装入 AMD Strix Halo，报告预填充最高 580 tok/s，解码 44 tok/s。这让前沿级 MoE 推理进入桌面级硬件。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwocik/two_300b_moe_models_each_on_one_128_gb_mini_pc/)
- **Rank-8 LoRA 将 Transformer 链式跟随能力提升至 99% 准确率** — 在冻结基础模型上，于一个早期层应用 rank-8 LoRA，将 Qwen3-8B 在 24 行上下文链上的精确准确率从 15.5% 提升到 99%。该结果表明，受深度限制的引用跟踪可以低成本修补。 [来源-huggingface](https://huggingface.co/papers/2609.36585)
- **Caveman Skill 将 AI 编程智能体 token 用量削减 65%** — 开源 caveman skill 和代理通过以“穴居人风格”语言压缩智能体通信，在测试中没有测得质量损失的情况下将 token 用量最多减少 65%。它凸显了提示词和协议设计如何能实质性降低智能体成本。 [来源-github](https://github.com/JuliusBrussee/caveman)

### 多模态与视频

- **OneStreamer 为流式视频 LLM 统一感知、记忆与主动响应** — OneStreamer 通过共享的主动生成过程联合学习与查询无关的证据记录和任务响应，并使用 PHCM 实现基于时间的记忆。它旨在让流式视频 LLM 既实时又可复用。 [来源-huggingface](https://huggingface.co/papers/2610.01762)

### AI 安全与行业争论

- **LeCun 对 AI 灭绝风险“零担忧”，称 Amodei“妄想”** — Yann LeCun 驳斥了 AI 灭绝风险和失控 AI 事件，同时升级了与 Dario Amodei 等关注安全的领导者之间的公开分歧。此番交锋凸显了围绕生存风险框架的分歧正在加深。 [来源-rss](https://fortune.com/2026/10/01/ai-godfather-yann-lecun-has-zero-concerns-about-human-extinction-says-anthropic-ceo-dario-amodei-is-deuded/)

## ⚡ 快讯速览

- **Redis 创始人发布 ds4 工具，用于本地运行 LLM** — Redis 创始人发布了 ds4，一个用于在本地运行 LLM 的工具。 [来源-rss](https://dwarfstar.sh/)
- **电力审批延迟 Oracle 威斯康星州 AI 数据中心** — 电力审批瓶颈正在推迟 Oracle 威斯康星州 AI 数据中心的建设。 [来源-rss](https://www.theregister.com/on-prem/2026/10/02/power-approval-set-to-delay-oracles-wisconsin-ai-datacenter/5300832)
- **GPT-6 Astra 通过 agent-wow 玩《魔兽世界》** — GPT-6 Astra 已通过 agent-wow 框架展示玩《魔兽世界》。 [来源-rss](https://agent-wow.sh/gpt-6-astra-plays-world-of-warcraft-for-the-first-time-with-agent-wow/)
- **Google 为 Google Cloud 和 AI 智能体发布 Agent Skills 仓库** — Google 发布了一个技能仓库，用于帮助构建 Google Cloud 和 AI 智能体。 [来源-github](https://github.com/google/skills)
- **Cursor 发布官方插件规范与开发者插件** — Cursor 推出了官方插件规范和开发者插件。 [来源-github](https://github.com/cursor/plugins)
- **176B Qwen MoE 通过 TensorSharp 在 16GB 笔记本 GPU 上运行** — TensorSharp 在一台 16GB RTX 3080 笔记本 GPU 上运行 176B Qwen MoE。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwwmy1/running_qwen38_flash_next_176b_on_a_16gb_rtx_3080/)
- **Ninfer 4080 让 100k 上下文 Qwen 27B 在 16GB GPU 上运行** — Ninfer 4080 将 100k 上下文 Qwen 27B 推理带到 16GB 级 GPU 上。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwv0fj/i_built_ninfer_4080_for_16gb_class_gpus/)
- **iPhone 被用作第二 GPU 加速 Mac 本地 LLM 推理** — 一位开发者将 iPhone 用作第二 GPU，以加速 24GB Mac 上的本地 LLM 推理。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wvz1ex/i_made_my_iphone_a_second_gpu_for_my_24_gb/)
- **Hugging Face 发布开放模型多框架 RL 指南** — Hugging Face 分享了一份关于开放模型多框架强化学习的指南。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwk49n/the_ultimate_guide_to_multiharness_rl/)
- **系统性研究分离 LLM 蒸馏中的 rollout 策略作用** — 新研究系统性地分离了 LLM 蒸馏中 rollout 策略的作用。 [来源-huggingface](https://huggingface.co/papers/2609.35259)
- **E-MoE 增强非分解扩散语言模型的专家混合** — E-MoE 改进了非分解扩散语言模型的专家混合路由。 [来源-huggingface](https://huggingface.co/papers/2609.37533)
- **面向 LLM 多奖励 RL 的密度感知奖励聚合** — 一种密度感知奖励聚合方法针对 LLM 中的多奖励 RL。 [来源-huggingface](https://huggingface.co/papers/2610.00574)
- **Astral Codex Ten 的《Our AI Midwife》探讨 AI 在分娩中的应用** — Astral Codex Ten 的文章考察了 AI 在分娩中的辅助作用。 [来源-rss](https://www.astralcodexten.com/p/our-ai-midwife)
- **在 Claude 和 Claude Code 中最大化 Opus 5.5** — 一篇 Claude.dev 指南详述了如何在 Claude 和 Claude Code 中充分利用 Opus 5.5。 [来源-rss](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/)
- **Agent Reach 通过一个 CLI 为 AI 智能体提供互联网访问** — Agent Reach 通过单个 CLI 为 AI 智能体提供互联网访问。 [来源-github](https://github.com/Panniantong/Agent-Reach)
- **Superpowers：面向编程智能体的智能体技能框架与软件开发方法论** — Superpowers 为编程智能体打包了智能体技能和一套软件开发方法论。 [来源-github](https://github.com/obra/superpowers)
- **System76 禁止 AI 生成代码进入 COSMIC 代码库** — System76 将不接受许多 COSMIC 代码库中的 AI 生成代码。 [来源-rss](https://www.neowin.net/news/system76-bans-ai-generated-code-across-many-of-its-cosmic-codebases/)
- **开源工具使用 LLM 生成 LDraw LEGO 模型** — ldraw-nova 使用 LLM 生成 LDraw LEGO 模型。 [来源-github](https://github.com/anteloc/ldraw-nova)
- **Greg Kroah-Hartman – LLM 时代的安全 [视频]** — Greg Kroah-Hartman 讨论了 LLM 时代的安全挑战。 [来源-rss](https://www.youtube.com/watch?v=NnV_cWeoo5Q)
- **投票：哪些 Hacker News AI 挑战已被实现** — 一项投票询问哪些 Hacker News AI 挑战实际上已被实现。 [来源-rss](https://stoppels.ch/goalposts/)
- **OpenID 发布面向智能体 AI 的身份管理论文** — OpenID 发布了一篇关于智能体 AI 身份管理的论文。 [来源-rss](https://openid.net/wp-content/uploads/2025/10/Identity-Management-for-Agentic-AI.pdf)
- **Impeccable：面向 AI 编程智能体的设计指导** — Impeccable 提供专为 AI 编程智能体量身定制的设计指导。 [来源-github](https://github.com/pbakaus/impeccable)
- **Corey Haines 发布面向 AI 编程智能体的营销技能** — Corey Haines 发布了面向 AI 编程智能体的营销技能。 [来源-github](https://github.com/coreyhaines31/marketingskills)
- **过拟合推理引擎为极致性能而兴起** — 一场讨论考察了为极致性能而优化的过拟合推理引擎的兴起。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwu6zj/the_rise_of_overfit_inference_engines/)
- **Strata Qwen 3.8 Flash Next 提供快速本地 LLM 推理** — Strata Qwen 3.8 Flash Next 因快速本地 LLM 推理而受到关注。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wx1bi1/strata_qwen_38_flash_next_is_the_biggest_thing/)
- **Anyworld：由本地 LLM 担任地下城主的自托管多人文字 RPG** — Anyworld 是一款自托管多人文字 RPG，其中本地 LLM 担任地下城主。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwkudj/anyworld_a_selfhosted_multiplayer_text_rpg_where/)
- **Sopro V2 Turbo 2610：克隆语音更干净，仍为同一 120M CPU 模型** — Sopro V2 Turbo 2610 提升了克隆语音的干净度，同时保留 120M CPU 模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwrw0v/sopro_v2_turbo_2610_cleaner_cloned_voices_same/)
- **本地 Qwen 模型与 Claude Opus 4.6 在三项编程任务上的对比** — 一项对比在三个编程任务上将本地 Qwen 3.8 27B Unsloth Q6 和 Qwen Flash 与 Claude Opus 4.6 进行较量。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwrgx1/two_local_qwen_38_27b_unsloth_q6_and_qwen_flash/)
- **llama.cpp PR 将 Qwen 索引器分数内存减半，降低 VRAM 占用** — 一个 llama.cpp PR 将 Qwen 的索引器分数内存减半，从而减少 VRAM 使用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwfyv6/qwen4exp_halve_the_indexer_score_memory_by/)
- **用户注意到较新 LLM 趋向于密集、扩展词汇的写作风格** — 用户观察到较新 LLM 越来越多地采用密集、扩展词汇的散文风格。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wwdsce/has_anyone_noticed_this_trend_toward/)

---

*由 AI News Agent 生成 | 2026-10-03*