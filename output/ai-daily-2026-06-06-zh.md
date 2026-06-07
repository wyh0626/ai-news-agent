---
title: "AI 日报 — 2026-06-06"
description: "Claude Mythos5 将发布；CVPR2026 最佳论文获奖。"
lang: "zh"
pairSlug: "ai-daily-2026-06-06"
---

# AI 日报 — 2026-06-06

> 覆盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. Claude Mythos 5 传将发布，定位高于 Opus

有传言称 Anthropic 即将发布 Claude Mythos 5，被吹捧为高于 Opus 的新等级。帖子称 Mythos 5 将从 Claude v5 起步，取代 Opus 成为顶级模型，据说在发帖者的个人主页上曾短暂出现过预览内容。[来源-twitter](https://x.com/kimmonismus/status/2063239490240487884)

### 2. 搭载世界模型的 VLA-JEPA 登陆 LeRobot

VLA-JEPA 通过在训练中集成基于 JEPA 的世界模型来增强动作学习，将其预测器基于 V-JEPA2 进行条件建模，从而学习与动作相关的动力学并支持在人类视频上进行预训练。在推理阶段，世界模型被丢弃，仅保留一个带有 Qwen 主干网络和动作头的标准 VLA。一个仅用 13 个样例微调的演示已在 NVIDIA DGX Spark 上实现实时运行，这标志着首个世界模型成功移植到 LeRobot 上。[来源-twitter](https://x.com/LeRobotHF/status/2063171227288510532)

### 3. CVPR2026 最佳论文奖得主公布

CVPR 2026 大会宣布了本届最佳论文奖得主，并向作者在计算机视觉领域的里程碑式贡献表示祝贺。相关讨论也提出了可复现性方面的担忧，指出目前缺乏可用代码、公开 API 和易访问的数据集，一些人认为这会影响研究在实践中的可复现性及其在 AI 研究中的实际影响力。[来源-twitter](https://x.com/pesarlin/status/2063151890230075510)

## 📰 重点报道

### AI Safety

- **头部 AI 实验室呼吁协调暂停自我改进能力研发** — 多家大型 AI 实验室的负责人警告，系统可能很快会具备递归自我改进能力，建议在建立足够安全保障前，协调实施一次可验证的开发暂停。要落实这样的暂缓措施，需要跨国、跨公司的协作，其中 Anthropic 被视为在这一方向上起到示范作用。《华尔街日报》指出，Anthropic 呼吁各实验室放缓开发节奏以降低对社会的潜在风险。[来源-twitter](https://x.com/Yoshua_Bengio/status/2063292262293844119)
- **Meta 确认数千个 Instagram 账号被通过 AI 聊天机器人入侵** — Meta 证实有数千个 Instagram 账号被滥用其 AI 聊天机器人所入侵。攻击者据称利用聊天机器人的交互方式，获取了用户账号的未授权访问权限。[来源-hackernews](https://this.weekinsecurity.com/meta-confirms-thousands-of-instagram-accounts-were-hacked-by-abusing-its-ai-chatbot/)
- **PewDiePie 的 AI 工具再曝一键接管管理员账号漏洞** — Reddit 讨论披露了 PewDiePie 的 AI 工具中存在一个安全漏洞，可一键接管管理员账号，该漏洞在 LocalLLaMA 社区中被提及。帖子同时提醒相关演示视频包含 NSFW 语言。本条新闻凸显了面向用户的 AI 工具在安全性方面持续存在的问题。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tys1wj/another_1click_admin_account_takeover_in/)

### AI

- **CopilotKit 发布跨平台 Agentic 框架，支持生成式 UI** — CopilotKit 宣布推出跨平台 SDK，用于在 Web、移动端和 Slack 上构建 agentic 应用和 Generative UI，兼容 React、Angular、Vue 和 React Native。该项目推进 AG-UI Protocol 的普及，并强调已被 Google、LangChain、AWS 和 Microsoft 等主要玩家采用。它主打具备流式对话、工具调用和共享状态的聊天 UI，以加速 AI 能力在应用中的集成。[来源-github](https://github.com/CopilotKit/CopilotKit)
- **Gemma 4 12B QAT 搭配 MTP 在 12GB 显存上跑出 120 tok/s** — Google 发布了 Gemma 4 12B 的 QAT 变体。在一块 12GB RTX 4070 上，使用打过补丁的 llama.cpp 和转换为 GGUF 的 QAT 模型，通过 mtp-bench.py 跑出了每秒 120 token 的速度。测试细节包括使用 Unsloth 量化、Google 的 QAT 助手以及系统规格（CachyOS、Ryzen 7 9700X、32GB 内存）。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1typjmc/120_toks_on_12gb_vram_with_gemma_4_12b_qat_mtp/)

### LLM

- **模型能力差距缩小速度快于价格差距** — 到 2026 年，顶级开源/开放模型与闭源模型之间的能力差距缩小速度，比价格差距缩小得更快。对于每月消耗 10 亿输入 token 和 10 亿输出 token 的公司而言，成本区间从约 2,740 美元（DeepSeek R1）到 105,000 美元（GPT-5.5 Pro）不等，其中 Claude Opus 4.8 约为 30,000 美元，DeepSeek V4 Pro 约为 5,220 美元。一则类似 ChatGPT 风格的观点建议：大规模推理场景优先选择 DeepSeek V4 Pro/R1，高可靠高端工作流选择 Claude Opus，而 GPT-5.5 Pro 只在其额外能力足以对冲高额 token 成本时才值得使用。[来源-twitter](https://x.com/chamath/status/2063292917964517830)
- **Harness-1：具状态外化“安全带”的 20B 搜索智能体** — Harness-1 是一个 200 亿参数的搜索智能体，通过“状态外化安全带”进行训练，从而实现前沿水准的长视野搜索能力。据称其表现可与 Opus-4.6 比肩，并优于 GPT-5.4，同时在将候选方案、证据、验证过程和搜索历史外化存储的情况下，成本与时延仍保持在接近 Context-1 的水平。该项目开源，并支持 HLS 播放。[来源-twitter](https://x.com/patpcj/status/2063298457398636570)
- **Cohere 未公开的 30B 代码模型开放本地早期测试** — Cohere 宣布其首个代码模型，是一个 300 亿参数、其中 30 亿为激活参数的模型，现已面向早期访问和本地测试做好准备。该模型目前托管在 Hugging Face 上，尚未正式公开发布，团队邀请社区在官方上线前进行测试并反馈。他们表示，该模型在速度和 token 生成方面表现令人鼓舞，与同尺寸模型相当。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tylzy2/coheres_unreleased_coding_model_early_access_for/)
- **KVarN KV Cache：6-bit 精度媲美 q8_0，4-bit 媲美 q5_0** — 最新基准测试表明，KVarN KV cache 量化在各个尺寸上都优于标准 llama.cpp 量化方案，其精度可匹配更高比特量化。在 BeeLlama v0.3.2 预览版中，5-bit、6-bit 和 8-bit 的 KVarN 配置可以达到与 q8_0 或 q5_0 相当的准确率，同时显著降低内存占用。注意：当前二进制文件较为陈旧，如需复现请从源码构建。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyockn/kv_cache_quant_benchmarks_kvarn_6bit_matches_q8_0/)
- **DeepSeek V4 Flash 获得 llama.cpp 初步支持（WIP PR 24162）** — DeepSeek V4 Flash 正在通过一个初期 PR 被集成至 llama.cpp。作者将模型量化到 3-bit，以便在保持全尺寸张量布局的同时测试表现，并称赞其在本地推理方面的强大潜力，尽管当前性能较慢且 GPU/FA 支持尚不完整。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyb3np/deepseek_v4_flash_is_amazing_wip_llamacpp_pr_24162/)
- **MoQ GGUF 与 GSQ：低比特 GGUF 量化即将大幅升级** — 一则讨论指出，通过 MoQ 和 GSQ，低比特 GGUF 量化将迎来显著改进。这些更新有望提升以 GGUF 格式存储的量化 LLM 在效率和性能方面的表现，从而利好开源工作流。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyjkfh/moq_ggufs_and_gsq_lowbit_ggufs_are_about_to_get/)

### Open Source

- **Supervision GitHub Star 达 4 万，赋能 6,500 个 CV 项目** — 开源库 Supervision 在 GitHub 上的 Star 数正式达到 40,000。它目前已为超过 6,500 个开源计算机视觉项目提供支撑，其中包括如篮球 AI 等演示案例。[来源-twitter](https://x.com/skalskip92/status/2063313658533511184)

### Tools

- **人工分析图表显示 MAI-Transcribe-1.5 远超同类** — ArtificialAnalysis 发布的一张图表显示，MAI-Transcribe-1.5 在转写任务中表现独树一帜。该说法反映出其被认为具有极强性能，不过摘要中并未提供具体细节和评测方法。[来源-twitter](https://x.com/mustafasuleyman/status/2063170571966222383)

### AI Regulation

- **美国众议院起草法案，禁止各州自行制定 AI 规则** — 该法案草案将禁止各州颁布或执行与 AI 相关的监管规则，以建立统一的联邦框架。这显示出立法者更倾向于由联邦层面统一监管 AI，而非允许各州自行其是。[来源-hackernews](https://www.reuters.com/business/us-house-lawmakers-release-draft-bill-regulate-ai-2026-06-04/)

### AI Tools

- **Agent Reach 让 AI Agent 能读懂整个互联网** — Agent Reach 是一个开源 CLI 工具，为 AI agent 提供跨平台的互联网浏览能力，支持 Twitter、Reddit、YouTube、GitHub、Bilibili 和小红书等站点，而且无需支付 API 费用。它试图通过统一的安装与更新流程，解决常见的浏览障碍（付费墙、登录、IP 封锁等）。这降低了 AI agent 从网络获取信息的环境搭建门槛。[来源-github](https://github.com/Panniantong/Agent-Reach)

### AI Policy

- **标普 500 拒绝接纳 SpaceX，间接挡住 OpenAI 与 Anthropic 入口** — 标普 500 指数委员会否决了将 SpaceX 纳入指数的提议，坚持执行其资格规则。委员会不会为尚未盈利的 AI 企业破例，这实际上也将 OpenAI 和 Anthropic 拦在指数之外。该报道引用了 Ars Technica 的文章以及 Hacker News 上的相关讨论。[来源-hackernews](https://arstechnica.com/tech-policy/2026/06/sp-500-blocks-fast-spacex-entry-wont-waive-rule-for-unprofitable-ai-firms/)

### AI Hardware

- **dvlt.cu：面向 NVIDIA DVLT 模型的 CUDA/C++ 推理引擎** — dvlt.cu 是一个为 NVIDIA DVLT 3D transformer 打造的轻量级 CUDA/C++ 推理引擎。它以 5MB 的二进制形式发布，依赖仅包括 cuBLASLt 和 cuTLASS，并使用 mmap 方式加载 bf16 权重，从而实现一次性上传到 GPU，无需 Python 或常规机器学习运行时。权重约 1.17 亿参数，作为 NVIDIA 的非商业资产，在安装时获取；该项目由用户 yassa9 在 GitHub 托管。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyu79c/dvltcu_inference_engine_written_from_scratch_in/)

### Hardware

- **Debian Testing 上的 AMD MI50 交出亮眼 AI 跑分** — 在 Debian Testing 上，作者使用两块 32GB 的 AMD MI50 GPU，通过 llama.cpp 和 llama-benchy 进行了基准测试。该环境采用更新的 Vulkan 以及混合的 ROCm/HIP 库，据称可在无需用户额外调整的情况下正常支持 MI50，且 llama.cpp 已更新到 9413 版本。作者表示稍后会分享完整的并发基准测试表格。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1typr7o/amd_mi50_on_debian_testing_is_doing_great_and/)

## ⚡ 快讯速览

- **PS2 风格图像提示词引爆 agentic AI 使用量** — 一则帖子展示了用于图像生成的 PS2 风格趣味提示词，折射出对 agentic AI 的兴趣。发文称输出量出现巨大跃升、并已被完全采用，这一趋势还被 Jeremy Howard 和 Jen Zhu 的转发进一步放大。[来源-twitter](https://x.com/dejavucoder/status/2063170475568873775)
- **OpenAI 硬件负责人跳槽至 Anthropic** — 一位 OpenAI 硬件工程师（第二位硬件早期员工）宣布在任职 2.4 年并参与定制芯片项目后离职。他将加入 Anthropic 迎接新挑战，并盛赞原团队的才华和价值观。帖子还提到，他对芯片将成为 AGI 的关键引擎感到兴奋，并希望开启一段“从零构建”的新阶段。[来源-twitter](https://x.com/itsclivetime/status/2063356118525792542)
- **ChatGPT 支持从写作模块直接发送邮件** — ChatGPT 现在允许用户在网页界面的写作模块中直接撰写并发送邮件，无需离开对话页面。该功能支持在对话上下文中一边撰写、一边修改、并最终发出邮件，相关更新在 X（原 Twitter）上的一则帖子中被讨论。[来源-twitter](https://x.com/gdb/status/2063056196735504796)
- **代码行数不等于生产力，agentic AI 让输出激增但采用率持平** — 该条内容指出，代码数量并不是衡量生产力的真实指标。帖子提到，agentic AI 让产出出现显著激增，但整体采用率依然基本持平。[来源-twitter](https://x.com/fchollet/status/2063288883052491011)
- **英格兰与威尔士警方被要求暂停在法庭陈述中使用 AI** — 英格兰和威尔士的相关机构已被指示，暂时停止在撰写提交法庭的陈述文件时使用 AI。此举旨在回应外界对 AI 生成内容在法律语境下的可靠性与公平性的担忧，据称目前正在进行相关政策审查，以指导未来的使用规范。[来源-hackernews](https://www.ft.com/content/229e5949-3ebc-4151-8a86-a01b5e259241)
- **Meta 再次推迟向开发者开放其最新 AI 模型** — Meta 再度延后向开发者开放其最新 AI 模型的计划，进一步拉长了发布时间表。报道指出产品一再延迟，且采取谨慎的发布策略，反映出 Meta 在 AI 部署及对第三方开放方面极为小心。[来源-hackernews](https://www.wsj.com/tech/ai/meta-keeps-delaying-the-release-of-its-new-ai-model-to-developers-f8569c8c)
- **“We Need Air Again”：GLM GGUF 前沿推理的呼声** — 一篇在线帖子感叹自 Air 4.5 之后迟迟没有新版本升级，同时提到 GLM 4.7 Turbo 和 GLM 5.1 在代码场景中的表现，但也指出其体积和延迟等问题。作者询问未来是否会有新的 Air frontier 模型或 turbo 版本，能在 agentic 编码中以更少的 token 超越 Qwen 3.6 35B，并暗示可以借鉴 Gemma 那样的 QAT 路线，来反超 Qwen。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyresc/zai_we_need_air_glm_gguf_wen/)
- **16GB 显存 + 64GB 内存的 AI 配置应该跑什么？** — 一则 Reddit 帖子询问，在配备 16GB 显存和 64GB 内存（RTX 5080、DDR5）的系统上，适合跑哪些软件和模型配置，用于编程和 agentic AI 工作流。作者希望了解应选择哪些模型与量化等级，以及 llama.cpp 的示例命令，并邀请用户分享自己的量化方案、模型选择和实用设置。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyqet9/what_are_you_running_on_16gb_vram_64gb_ram/)
- **AI 让周末能造出 67 个“无用 App”** — 一则借 AI 调侃的帖子称，以前一个周末只能做出一个无用 App，而现在借助 AI，一个周末能堆出 67 个，个个都有 logo 和精美网页——却一个用户也没有。该帖子借此批评“快而浅”的原型开发，反思在 AI 辅助开发时代，软件的价值、质量和真实使用率问题。[来源-twitter](https://x.com/Yuchenj_UW/status/2063315896421274076)
- **Ask HN：为什么 Hacker News 社区这么“反 AI”？** — 一位 Hacker News 用户质疑该社区对 AI 编程长期持怀疑态度，认为最终的产品与迭代速度比代码优雅程度更重要。他主张 AI 辅助开发可以更快推出版本获取真实反馈，并以 Claude Code 为例，称其极大加速了迭代周期。[来源-hackernews](https://news.ycombinator.com/item?id=48420827)
- **本地模型能否取代 Claude 处理简单 HTML 任务？** — 该 Reddit 讨论询问，本地语言模型是否足以胜任为在线学习内容生成基础 HTML 的任务，从而不再依赖 Claude 或 Codex 等云端助手。作者希望了解本地模型在实际应用中的能力边界，以及与更强大的云端模型之间的差距，讨论重点围绕真实使用体验和本地模型与现有头部服务之间的鸿沟。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tyt63g/are_local_models_good_enough_to_replace/)
- **AA 对 3×3090 GPU 环境下最新本地 LLaMA 系模型进行对比** — 一篇 Reddit 帖子针对配备三块 RTX 3090 GPU 的本地环境，梳理了可用的 LLaMA 家族模型，并排除了 300B（以及大概率 200B）级别的超大模型。帖子指出 MiniMax 和 Step 在 Q3 配置下速度较快，而 Gemma-4 12B 仍未出现，并链接了 LocalLLaMA 中的相关讨论。讨论重点在于结合硬件条件做模型选型，而非介绍新模型发布。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tya05j/aa_comparison_of_the_latest_local_models/)
- **通过 Codex 使用电脑更好玩了** — 一条推文声称，通过 OpenAI 的 Codex 来操作电脑会让使用体验更有趣。作者暗示 Codex 能提升与计算机交互的趣味性和直观性，使各类计算任务更易上手。[来源-twitter](https://x.com/gdb/status/2063102501847757197)

---

*由 AI News Agent 生成 | 2026-06-06*