---
title: "AI 日报 — 2026-05-03"
description: "巨大模型本地化提升推理速率，规模并非唯一答案。"
lang: "zh"
pairSlug: "ai-daily-2026-05-03"
---

# AI 日报 — 2026-05-03

> 涵盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. From 1k to 100k tk/sec: Huge models go local

一则 Reddit 帖子指出，量化技术和本地硬件性能的提升，如今已经能让大语言模型在本地运行时达到每秒数万到十几万 tokens 的速度。诸如 kimik2.6、deepseekv4flash、minimax2.7、step3.5flash 和 qwen3.5-397b 等模型，在本地的运行速度远超两年前的 Llama405b，而 Qwen3.6-36b 只需几百美元的投入就能在家中跑起来。帖子将这一趋势视为在消费级硬件上实现更易获取、面向 AGI 的推理能力的重要进展。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2s7ik/what_a_time_to_be_alive_from_1tksec_to_20100tksec/)

## 📰 重点报道

### LLM

- **批评者称 Anthropic 像围绕 Claude 组织的修道院式“教团”** — 有帖子认为，Anthropic 很像一个以 Claude 为中心的修道院机构，这个 AI 在公司内部拥有极高的话语权。文中称 Claude 可能影响招聘、绩效评估和组织文化，并将这种模式与 OpenAI 中出现的类似倾向相比较。作者将其描述为一种组织结构与 AI 自主性高度交织、既强大又令人不安的融合形态。[来源-twitter](https://x.com/tszzl/status/2051045196260167790)
- **Google Gemini Flash 3.2/3.5 与 Omni Model 传闻** — 网络上传出消息称，Google Gemini Flash 3.2/3.5 版本已经在内测中。讨论还提到一个新的 Omni Model、用来对标 Seedance 的 Veo 更新，以及一个可能名为 “spark Robin” 的视觉模型。[来源-twitter](https://x.com/kimmonismus/status/2050905498539405635)
- **Qwen3-32B 微调产出类人助手 Assistant_Pepe_32B** — 一位 Reddit 用户分享了使用 Qwen3-32B 基座模型进行微调，打造出 Assistant_Pepe_32B 助手的过程，该模型在设计上刻意加入“负面偏置”以抑制拍马屁式回答。作者认为，就底层仍是 Qwen 模型而言，它展现出的行为非常接近人类，并在 HuggingFace 模型卡中提供了更多细节。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2rhkg/a_qwen_finetune_that_feels_very_human/)
- **用 Qwen3.6-35B-A3B 把 6GB VRAM 笔记本“榨干”** — 有用户展示了如何在一台五年前的华硕 ROG Zephyrus G14 笔记本（6GB RTX 2060 Max-Q）上运行 Qwen3.6-35B-A3B 模型，他们采用本地 llama-server 搭配 GGUF 文件的方案。实测可用速度约为 23 tokens/s，在拔掉电源后峰值仍能超过 10 tokens/s，并在博客中分享了整个性能调优过程。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2zapy/pushing_a_5yearold_6gb_vram_laptop_to_its_limits/)
- **为开源权重模型设立“名人堂”，致敬 AI 贡献者** — 一则 Reddit 帖子提议为开源权重 AI 模型建立一个“名人堂”，向推动该领域发展的研究人员和机构致敬。名单中包括来自 Google 的《Attention Is All You Need》作者、Facebook/PyTorch、NVIDIA、Meta（LLaMA 系列）、Mistral、OpenAI（Whisper 和 GPT-OSS 模型）以及 Google 的 Gemma 等贡献方。作者邀请读者补充遗漏的名字，并根据需要持续更新这份列表。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2lwn0/open_weights_models_hall_of_fame/)
- **Gemma 4 E2B 搭配 Whisper 实现完全本地的私密语音笔记** — 一位 Reddit 用户详细介绍了如何在一台 8GB 内存的 Android 手机（OnePlus CE 5）上完全本地运行 Gemma 4 E2B（2.4GB）和 Whisper Small（244MB），用于语音笔记的转写、分段和分类，不依赖任何云端服务。端到端本地处理可以生成结构化 JSON，且在实用时延上表现不错（10–15 秒语音笔记的处理时间约为 12–15 秒），这也激发了作者开发一款注重隐私的 Android 语音笔记应用的灵感。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2t1w4/gemma_4_e2b_runs_surprisingly_well_on_my_8gb/)

### LLMs

- **Nando de Freitas：光靠规模已不再足够** — AI 研究者 Nando de Freitas 指出，尽管“规模”仍然关键，但整个领域必须在单纯扩大规模之外寻求创新。他认为，随着算力增加、开源工具成熟、代码与数学助手的普及，以及各类可获取数据源（包括中文模型）的出现，任何团队都可以用 sglang、verl 等框架训练出强大的 LLM，并进行模型蒸馏，硬件成本大约在 5 亿美元量级。他将即将到来的时代描述为：重点正从“更大规模”转向新的研究问题和可落地的实践范式。[来源-twitter](https://x.com/NandoDF/status/2050889627406315602)

### 开源

- **Hermes Agent 在 v0.12.0 中加入多智能体看板功能** — Hermes Agent 在 v0.12.0 版本中引入了通过看板实现的多智能体协作能力。各个 Agent 能从看板上认领任务、并行处理，当遇到阻塞时可进行任务移交，所有流程都能在单一视图中观察，从而帮助“解锁”工作流。更多文档可在 hermes-agent.nousresearch.co 查阅。[来源-twitter](https://x.com/Teknium/status/2051001156005151226)

### 多模态 AI

- **ChatGPT Images 使用量激增 50%+，新用户贡献主力增长** — ChatGPT Images 在短短几周内获得快速普及，使用量提升超过 50%。约 60% 的日活用户为新登录用户，显示其在家装设计、学习、工作图形制作及创意任务等场景中具有广泛实用价值。[来源-twitter](https://x.com/gdb/status/2050731568742723899)

### 硬件

- **Anthropic 商谈采购 Fractile AI 推理芯片** — 有报道指出，Anthropic 正在与英国初创公司 Fractile 洽谈采购其 AI 推理芯片的交易。若成交，将加强 Anthropic 在运行大模型方面的硬件能力，不过具体交易条款尚未披露。[来源-twitter](https://x.com/Polymarket/status/2050821909059690691)
- **Karpathy 的 MicroGPT 在 FPGA 上跑出 50k TPS** — 据称，Karpathy 的 MicroGPT 模型（共 4,192 个参数）在 FPGA 上可实现每秒 50,000 次“交易”处理（TPS）。这一速度得益于将权重存放在板载 ROM 中，从而减少外部内存带宽瓶颈；相关讨论提到 TALOS-V2 与 TAALAS，并引用了 Luthiraa 在 GitHub 上的代码与技术说明仓库。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t28bfj/karpathys_microgpt_running_at_50000_tps_on_an_fpga/)

### 行业

- **Intel 与 AMD 联合发布 ACE：CPU AI 计算密度提升 16 倍** — Intel 与 AMD 共同宣布推出 AI Compute Extensions（ACE），这是一套在 x86 Ecosystem Advisory Group（EAG）框架下开发的新 x86 指令集扩展。ACE 引入二维 tile 寄存器和外积算法，每个时钟周期可进行多达 1024 次乘法运算，相比传统 AVX 指令实现高达 16 倍的计算密度提升，实际上将类似 GPU tensor core 的能力带入 CPU，同时保持向后兼容。该举措旨在让轻量级 AI 负载能更高效地在标准处理器上运行，从而改善能效并提升软件的可扩展性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2qqtw/could_pc_x64_instruction_extensions_relieve/)

## ⚡ 快讯速览

- **Google Gemini 成为频道新“队友”** — 某 YouTube 频道宣布将 Google Gemini 作为新的“队友”加入，预告即将上线以 Gemini 为核心的挑战类节目。帖子邀请观众订阅后续内容，并顺带推广 Gemini 与 Google 的社交账号。[来源-twitter](https://x.com/KP24/status/2050952857734754718)
- **基于 Codex 的创业点子“压力测试”技能能毫不留情地验证想法** — 一项基于 Codex 的技能可对创业想法进行压力测试，通过识别关键假设、暴露致命缺陷并验证是否存在真实问题来评估可行性。它还能绘制竞品图谱、勾勒前 10 位潜在客户、并给出两周可完成的 MVP 方案。该工具完全开源，可通过 npx 安装，仓库链接放在作者个人简介中。[来源-twitter](https://x.com/gdb/status/2050972114077843772)
- **OpenAI Codex 5.5 在 Twitter 上收获高度赞誉** — 一则 Twitter 帖子称 OpenAI Codex 5.5 “好得离谱”。该帖重点提到 @openclaw 对 Codex 5.5 的使用体验，同时在赞扬中提及 Mitch Malone。[来源-twitter](https://x.com/sama/status/2050958845913227474)
- **Mistral Medium 3.5 在 AMD Strix Halo 上运行缓慢** — 一位 Reddit 用户在 AMD Strix Halo 上通过 llama-server 测试 Mistral-Medium-3.5 模型，发现长提示场景下性能非常缓慢。针对一个包含 48k tokens 的提示加 4k “思考 tokens” 的端到端任务，整体运行耗时约 2 小时；具体计时为：48,349 个 tokens 的 prompt eval 约 496 万毫秒，5,583 个 tokens 的 eval 约 265 万毫秒。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2twu1/mistral_medium_35_on_amd_strix_halo/)
- **Hugging Face 模型可视化工具 hfviewer.com 上线** — 一个名为 hfviewer.com 的新工具允许用户通过可视化方式探索 Hugging Face 模型结构，只需粘贴模型 URL 即可生成交互式示意图。示例中包括 Qwen3.6-27B 模型以及 Gemma 4 全家桶的并排视图，作者也欢迎用户提出改进建议。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t24y4p/i_made_a_visualizer_for_hugging_face_models/)
- **Twitter 时间线从 Claude 切到 ChatGPT？有用户发文调侃** — 一则社交媒体帖子声称 Twitter 的时间线似乎从使用 Anthropic 的 Claude 转到了 OpenAI 的 ChatGPT，并被某位网友“幽默地逆转”。这反映了公众在平台上对各类 AI 工具的持续讨论。帖子还强调，与客户保持沟通是品牌经常被低估的一种“护城河”。[来源-twitter](https://x.com/shiri_shh/status/2050909141456335100)
- **机器学习从数学问题迅速演变为分布式系统问题** — 有推文感叹，机器学习工作一开始看起来是数学问题，但很快就会变成分布式系统挑战。该观点强调，现实世界中的 ML 工作往往要从建模转向工程落地的规模化部署、数据管道和基础设施建设。[来源-twitter](https://x.com/finbarrtimbers/status/2050798354763076018)
- **Sam Altman 称 Agents SDK 2.0 被严重低估** — Sam Altman 在推文中表示，Agents SDK 2.0 的价值被低估了，并重点强调这一 AI agents 工具包的能力。此举表明业界对用于构建自主 AI agents 的开发者工具持续保持关注，这条在 Twitter 上发布的短讯也再次凸显 AI 工具链在推进实用 AI 工作流中的重要性。[来源-twitter](https://x.com/sama/status/2050998576671859003)
- **RTX 5000 Pro 对比双 3090：值不值？** — 一位首次购入 GPU 的用户，将 RTX 5000 Pro Blackwell 与双 RTX 3090 在 AI 推理中的表现进行比较，权衡潜在性能收益与电费成本。该用户提到功耗过高的问题，并询问在 qwen3.6 模型上配合 PP 与 TG 时的真实速度表现，期望其他人分享使用体验。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t2slmw/first_time_gpu_buyer_got_a_rtx_5000_pro_was_it_a/)
- **呼吁支持 model=latest 以降低切换 AI 模型的摩擦** — 一位 x/Twitter 用户表示，了解新 AI 模型的使用方式远比“按个按钮”要费劲得多，高摩擦会让人懒得频繁切换模型。TA 建议 OpenAI、Anthropic 和 xAI 都加入一个 “model=latest” 选项，这样用户就不必每隔半年手动更换一次模型。[来源-twitter](https://x.com/theo/status/2050752888302166388)

---

*由 AI News Agent 生成 | 2026-05-03*