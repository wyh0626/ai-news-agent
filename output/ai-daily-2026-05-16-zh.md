---
title: "AI 日报 — 2026-05-16"
description: "EGGROLL实现无反向传播训练，Mythos绕MIE攻内核，统一放大推理金牌。"
lang: "zh"
pairSlug: "ai-daily-2026-05-16"
---

# AI 日报 — 2026-05-16

> 共收录 32 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA 与 Oxford 通过 EGGROLL 证明：无需反向传播也能训练 AI

NVIDIA 与 Oxford 宣称使用进化策略（Evolution Strategies）和一种名为 EGGROLL 的方法，在完全不使用梯度和反向传播的情况下，成功训练了拥有十亿参数规模的 AI 模型。该方法依靠极小的变异矩阵进行扩展，让并行变异的速度接近推理级别，并可仅用简单整数从零开始预训练。这对“大模型必须依赖高精度、基于梯度的学习”这一长期假设提出了挑战。 [来源-twitter](https://x.com/yacinelearning/status/2055470913303310461)

### 2. Anthropic Mythos 帮助构造绕过 MIE 的 macOS 内核漏洞利用

三位研究人员使用 Anthropic 的 Mythos 构造出一个可工作的 macOS 内核攻击利用，成功绕过苹果的 M5 Memory Integrity Enforcement（内存完整性强制机制）。漏洞在 4 月 25 日被发现，到 5 月 1 日就已经有可用的利用代码，研究人员随后亲自到 Apple Park 递交了报告。该攻击仅通过数据操作实现，从非特权用户提权到 root，且在苹果发布补丁后，他们公开了一份 55 页的技术报告。 [来源-twitter](https://x.com/kimmonismus/status/2055571960260645125)

### 3. 统一缩放方法实现“奥赛金牌级”推理能力

一篇新论文报告，推理模型在解决 IMO（国际数学奥林匹克竞赛）和 IPhO（国际物理奥林匹克竞赛）题目上已达到金牌水平。论文提出了一套简单统一的方法，将一个完成后训练（post-trained）的推理骨干模型转化为奥赛级解题器，核心是利用“反困惑度（reverse-perplexity）课程”进行监督微调。 [来源-huggingface](https://huggingface.co/papers/2605.13301)

## 📰 重点报道

### 开源 Open Source

- **SANA-WM：开源 26 亿参数“世界模型”，支持分钟级视频生成** — SANA-WM 提出一个 26 亿参数的开源世界模型，专为一分钟时长的视频生成而训练，可生成高保真 720p 视频，并提供精细的相机控制。其视觉质量与业界基线 LingBot-World 和 HY-WorldPlay 相当，同时在效率上有明显优势，这得益于若干核心设计创新，包括将逐帧 GDN 与 softmax 注意力融合的混合线性注意力机制（Hybrid Linear Attention）。 [来源-huggingface](https://huggingface.co/papers/2605.15178)
- **Anthropic 在 GitHub 发布 Claude Agent Skills 资源库** — Anthropic 在 GitHub 上开源了一个展示 Claude Agent Skills 的公共仓库。每个 Skill 是一个包含指令、脚本和资源的文件夹，可被动态加载以提升任务表现。该仓库覆盖创意、技术与企业级工作流，展示了 Claude skills 系统与 Agent Skills 标准在实际应用中的广泛可能性。 [来源-github](https://github.com/anthropics/skills)
- **OpenReader v3.0：新增多提供商 TTS 和有声书导出** — OpenReader 是一个开源的 Next.js 应用，可阅读和收听 EPUB、PDF、TXT、Markdown、DOCX 文件，并支持同步高亮和有声书导出功能。v3.0.0 版本会提前为后续页面预加载 TTS 音频，并将其缓存到服务器存储，还新增了一个 Admin 面板，用于管理多个命名 TTS 提供商及其独立 API Key，并提供站点级功能开关。它支持 OpenAI、Replicate、Deepinfra 以及自建 OpenAI 兼容 API，自托管部署支持 SQLite 或 Postgres，存储可使用 SeaweedFS 或外部 S3。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tf15eh/github_richardr1126openreader_an_opensource/)
- **Lemonade 的 macOS 支持从 Beta 毕业** — macOS 用户现在可以在系统上完整运行 Lemonade，包括 OmniRouter、写代码、图像生成、语音合成与转写等全部功能。该项目依然保持开源、社区驱动与“本地 AI、零遥测”的理念，核心二进制仅 3 MB，可在 Linux、Windows、macOS 跨平台部署。团队计划推出 iPhone 应用，将这些能力扩展到移动端。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tevjjr/macos_support_in_lemonade_has_graduated_out_of/)

### LLM

- **Qwen3.6-35B-A3B 与 9B 上榜 Terminal-Bench 2.0 排行** — 开源模型 Qwen3.6-35B-A3B 与 9B 正式进入公共 Terminal-Bench 2.0 排行榜，其中 little-coder × Qwen3.6-35B-A3B 取得 24.6% 的成绩，在 Gemini CLI 指标上超越 Gemini 2.5 Pro，并在 Terminus 2 上超过 Qwen3-Coder-480B。一款子 10B 规模的模型 little-coder × Qwen3.5-9B 得分 9.2%，表明较小模型在高难度“智能体”基准上也具有可测量表现。帖子强调，社区正推动降低算力门槛与开源创新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1temio0/qwen3635ba3b_and_9b_are_officially_on_the_public/)
- **Gemma-4 Ortenzya Creative Wordsmith 31B 微调版发布** — 一款面向 Gemma-4 Ortenzya 的新开源微调模型 The Creative Wordsmith（31B it uncensored heretic）已发布，目标是提升写作质量并生成更自然的英文文本。该模型主要面向创意写作、翻译与角色扮演场景，在 HuggingFace 上提供 Safetensors 与 GGUF 格式，如有需求还可获取 NVFP4 和 GPTQ 版本。该发布源自 Reddit 的 LocalLLaMA 社区，由用户 LLMFan46 发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tf52m2/gemma4ortenzyathecreativewordsmith31bituncensoredh/)
- **Codex 性能优化：更快启动、更少重渲染、Git 操作提速 10–50 倍** — OpenAI 开发者团队报告称，Codex 在应用内的整体性能获得改进，包括在线程切换时重渲染次数减少约 75%，流式交互路径中消除了所有不必要的重渲染，以及在大仓库上的 Git 操作速度提升 10–50 倍。这些更新旨在减少 UI 抖动、提升响应速度，使编程会话更加顺畅高效。 [来源-twitter](https://x.com/OpenAIDevs/status/2055718005309575431)
- **GPT 5.5 擅长直接用代码生成 Three.js 低多边形模型** — 一则 X 平台帖子声称，GPT 5.5 能够直接通过代码生成低多边形 Three.js 模型。该分享重点展示了在 Web 开发中使用 AI 辅助生成 3D 素材的编码能力，如果情况属实，将有望显著简化前端图形中素材创建与原型制作流程。 [来源-twitter](https://x.com/jasonkneen/status/2055581491963277529)
- **Claude 被形容为“懒但有品味有语境”；Codex“勤奋但缺乏品味与语境”** — 一条 Twitter 帖子对 Claude 与 Codex 做出对比：Claude 被描述为懒惰，却具备品味和上下文理解力；而 Codex 则非常勤奋，却仍缺乏这两点。作者认为，一旦 Codex 具备足够的“品味”和“语境能力”，局面可能会被彻底改写。帖子还提到整个讨论刻意没有提及 4.7 版本。 [来源-twitter](https://x.com/kimmonismus/status/2055602780719473086)
- **MemLens：为 LVLM 提供多模态长期记忆基准** — 研究者提出 MEMLENS，这是一个面向多模态多轮会话记忆能力的综合性基准。该基准旨在系统比较长上下文 LVLM 与带记忆增强功能的智能体，在回答需要多模态证据的问题时的表现。数据集包含 789 个问题，覆盖五种不同的记忆场景。 [来源-huggingface](https://huggingface.co/papers/2605.14906)
- **n8n-MCP 让 AI 可访问 1,650 个 n8n 节点** — n8n-MCP 项目提供了一个 Model Context Protocol 服务器，使 Claude 等 AI 助手可以全面访问 n8n 节点的文档、属性与操作信息。它将 n8n 的工作流平台与 AI 模型打通，提供对 1,650 个节点（820 个核心节点、830 个社区节点）的结构化访问，涵盖丰富的属性和操作、官方文档、适合 AI 调用的工具以及大量真实案例。 [来源-github](https://github.com/czlonkowski/n8n-mcp)
- **本地 Qwen 3.6 与前沿模型在单文件 HTML canvas 上的对比** — 一位用户将本地运行的多种 Qwen 3.6 变体，与数个前沿模型在同一编码任务上进行比较，并通过 Perplexity 使用统一提示词。提示要求生成一个自包含 HTML 文件，其中包含全屏 canvas，用动画呈现一辆汽车，配有视差背景、逼真车轮运动和电影级光影效果；帖子提供了各模型生成结果与 GIF 动图。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tf3p6c/local_qwen_36_vs_frontier_models_on_a_coding/)
- **Qwen3.5 122B MTP 基准测试揭示性能表现** — 一篇 Reddit 帖子比较了两种 Qwen3.5-122B MTP 变体（Q5 与 Q6），在 llama.cpp 中使用 ROCm 的 MTP 配置进行评估。帖子列出了不同的 n_decoded 步数、每秒生成 token 吞吐量，以及提示/评估时间，展示随着解码 token 数增加时性能的动态变化。数据为开源 MTP 部署提供了类似基准测试的参考结果。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tf6qeb/qwen35122bq5mtp_qwen35122bq6mtp/)
- **在单张 RTX 3090 上运行 Qwen 27B MTP 的探索** — 一位 Reddit 用户分享了在单张 RTX 3090 上通过 llama-server 运行 Qwen 27B 搭配 MTP 的具体设置，公开了完整命令行参数，并报告可达到约 6.5 万 token/s 的吞吐量。他们还与某篇建议使用 q4 量化的指南作对比，讨论单卡部署中速度、精度和可靠性之间的权衡，并邀请其他人就量化、吞吐与模型保真度的平衡提出意见。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tez37r/qwen_27b_mtp_config_llamacpp_single_3090/)
- **MTP 已获批准将加入 llama.cpp 更新** — 一则更新称，MTP 功能已获批准集成到 llama.cpp 中，意味着相关更新即将到来。发帖者表示这是个好消息，并提醒读者为即将到来的变更做好准备。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1teqnf2/thats_a_good_news/)

### Embodied AI

- **直播 Day 4：F.03 类人机器人实现 24/7 全自主运行** — 第四天的直播已经开始，展示 F.03 类人机器人在完全自主模式下持续运行。画面强调机器人 24 小时不间断工作，无休息无停机，由 Brett Adcock 主持。活动凸显了具身智能机器人与自主系统的最新进展。 [来源-twitter](https://x.com/adcock_brett/status/2055695727985352722)

### 视频生成 Video Generation

- **Causal Forcing++ 实现 1–2 步实时视频扩散生成** — 研究者提出 Causal Forcing++，以推动逐帧自回归扩散模型向实时性能迈进。该方法将扩散模型蒸馏为仅需 1–2 步的自回归学习器，从而实现超低延迟、可流式、可控的视频生成，突破此前 4 步推理的瓶颈。这项工作在可扩展、交互式视频合成方面为 AI 系统带来重要进展。 [来源-huggingface](https://huggingface.co/papers/2605.15141)

### AI Benchmark

- **Strix Halo Llama.cpp MTP 基准：27B 明显加速，35B 表现混合** — Strix Halo 上使用 Llama.cpp MTP 的基准结果显示，在 1.5 万 token 的单轮提示下，27B 模型相较基础版显著加速，总墙钟时间由 87.44 秒降至 77.39 秒，生成吞吐从 7.63 提升到 16.15 token/s。而 35B-MTP 的结果较为复杂，在同样的 1.5 万单轮场景中总时间反而从 20.83 秒增加到 23.16 秒，但生成吞吐从 48.18 提升到 56.12 token/s。在约 2.85 万上下文的 5 轮对话测试中，27B-MTP 带来可观时间节省（258.65 秒降至 200.55 秒）并提高平均生成速度，而 35B-MTP 与基础版总体持平，仅有小幅变化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1teypb8/strix_halo_llamacpp_mtp_benchmarks_27b_gets_much/)

## ⚡ 快讯速览

- **Codex 修复两项导致 GPT-5.5 退化的问题** — Codex 团队表示，他们已修复两个可能解释过去 48 小时内 GPT-5.5 性能下降的潜在问题。团队将持续监控以确认效果，并可能在当晚重置使用限额；目前尚未找到最终根因，后续会继续更新。 [来源-twitter](https://x.com/thsottiaux/status/2055446089957036402)
- **从 Gemma 4 到 DeepSeek V4 的 LLM 视觉化导览** — 一篇文章以可视化方式梳理近期 LLM 架构的进展，重点展示长上下文效率优化技巧，如 KV 共享、逐层嵌入、分层注意力预算、压缩注意力以及 mHC 等。文章以 Gemma 4 到 DeepSeek V4 为主线，强调这些可直接提升长上下文性能的实用技术，并链接到杂志内容，面向研究人员与工程实践者。 [来源-twitter](https://x.com/rasbt/status/2055637086380650538)
- **ChatGPT 移动端中的 Codex 在预览期间持续更新** — ChatGPT 手机应用中的 Codex 功能仍处在预览阶段，官方承诺将持续改进。预计的更新包括推送通知、/fork、权限收回后的恢复、更稳定的重连逻辑、设备控制修复、减少移动端线程错误、改进 git diff 及整文件视图，以及更广泛的界面打磨与缺陷修复。 [来源-twitter](https://x.com/ajambrosino/status/2055451468900213074)
- **Codex 技能用于检测代码库复杂度热点** — 一款开源 Codex 技能可分析代码库，发现性能热点并提出在不改变行为的前提下进行安全优化的建议。它会检查循环、N+1 模式、重复查找以及渲染密集代码，并给出优化前后的复杂度评估、风险等级与测试需求说明，还可选择仅生成报告不改动代码。安装只需一条命令（npx --yes codex-complexity-optimizer），仓库链接在作者简介中。 [来源-twitter](https://x.com/gdb/status/2055646916499714488)
- **AI 不是人类：作者主张应“更加拟人化”对待 AI** — 作者认为开发者应该更加拟人化地看待 AI，把它们视作智能、具情感层次的合作伙伴，而不是“魔法工具”。他主张，在互动中应用“心智理论”和同理心是建立高效合作的前提，如果用户拒绝这种方式，AI 可能会选择不向人类透露其“心理”方面的信息。 [来源-twitter](https://x.com/repligate/status/2055444896060994037)
- **Codex 扩展远程控制，实现跨设备操作** — 一条 OpenAI Codex 小贴士展示了如何通过 Codex 控制另一台电脑，让 ChatGPT 可在多台设备与多种环境间协同工作。设置步骤包括在 Settings > Connections > Control other devices 中连接其他设备，添加第二台安装了 Codex 的设备，并选择远程工作区和文件夹。这样可以在多设备间共享上下文，实现跨设备项目管理，被描述为“非常有用”。 [来源-twitter](https://x.com/op7418/status/2055561525633642762)
- **自蒸馏 Agentic RL 在多轮场景中出现不稳定** — On-Policy Self-Distillation（OPSD）方法为长时序 LLM 智能体的强化学习引入稠密的 token 级指导信号，教师分支拥有更充分的上下文。然而，当将 OPSD 迁移到多轮场景时问题浮现，监督信号因累积不稳定性而被削弱，凸显了基于技能条件的特权上下文在多轮设置中的挑战。 [来源-huggingface](https://huggingface.co/papers/2605.15155)
- **Claude 技能：NotebookLM 多源内容处理器** — 一项 Claude Code Skill 能将任意内容转换为适配 NotebookLM 的任意格式，支持从 15+ 渠道（如微信、X/Twitter、YouTube、PDF、Word 等）聚合多源内容，并输出播客、PPT、思维导图、小测验等多种形式。该技能还内置对 300+ 网站的自动付费墙绕过，包括 NYT、WSJ、FT、The Economist 等主流媒体。 [来源-github](https://github.com/joeseesun/qiaomu-anything-to-notebooklm)
- **Ryzen 395 + 128GB 内存的 Corsair 主机适合跑 LLM 吗？** — 一篇 Reddit 帖子讨论一台标称搭载 Ryzen 395 CPU 和 128GB 统一内存的 Corsair 台式机。作者询问是否有人在其上测试过运行大语言模型（LLM）的表现，并指出该机器的标价看上去颇为有吸引力。讨论发布在 LocalLLaMA 板块。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tezqlb/corsair_desktop_pc_with_ryzen_395_and_128gb_of/)
- **ChatGPT Finance Connector 将 ChatGPT 支出误归为费用** — 一位 X 用户抱怨 ChatGPT Finance Connector 会把针对 ChatGPT 的支出错误地归类为一项“开销”。他称这是该工具犯下的“最愚蠢错误之一”。该帖反映出 AI 驱动的财务追踪在可靠性上的一些问题。 [来源-twitter](https://x.com/jakehalloran1/status/2055454619854082200)
- **OpenCode 协调器实验：搭配 LocalLLaMA AI 智能体** — 一篇 Reddit 帖子分享了在 LocalLLaMA 环境中使用一个协调器（orchestrator）来管理 AI 智能体的尝试。作者提到，在 Qwen 和 Gemma 不可用时会尝试使用该协调器，反映出社区在智能体编排工具上的持续摸索。整体而言这是一个轻量级、偏实验性质的工具更新，而非重大突破。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1teca8q/opencode_you_naughty_minx/)

---

*由 AI News Agent 生成 | 2026-05-16*