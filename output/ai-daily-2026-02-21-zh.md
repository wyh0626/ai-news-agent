# AI 日报 — 2026-02-21

> 覆盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. LoopViT：借助循环变换器的小型 AI 以少量权重实现对大模型的超越

A collaboration between HKUST, CASIA, and UC Santa Cruz introduces LoopViT, a looped transformer that reuses a small set of weights to simulate an internal chain of thought. The 18M-parameter model stops computing when predictions become certain and achieves 65.8% on the ARC-AGI visual reasoning benchmark, outperforming a larger 73M-parameter model on the same task. The paper is available on arXiv and code on GitHub. [來源-twitter](https://x.com/jiqizhixin/status/2025414242011382041)

### 2. Llama 3.1 70B 通过 NVMe-GPU 绕过 CPU 在 RTX 3090 上运行

A Show HN demonstrates that Llama 3.1 70B can run on a single RTX 3090 by bypassing CPU and RAM with an NVMe-to-GPU setup. The project links a library (ntransformer) and reports it works on consumer GPUs, with better performance expected on professional GPUs. It highlights a hardware-focused approach to running large transformers outside traditional CPU-based memory paths. [來源-hackernews](https://github.com/xaskasdf/ntransformer)

### 3. CPU 训练的 2970 万参数 LLM 在 40 小时内击败 GPU 基线

FlashLM v5 'Thunderbolt' 在 CPU（AMD Ryzen 7950X3D）上训练约 40 小时，达到困惑度 1.36、BPC 0.44，参数量 29.7M。它击败 TinyStories-1M 基线（PPL 1.59），标志着首个在 CPU 上训练的模型超过该基准。该模型使用一种不含 MatMul 的架构 ParallelGatedRecurrence，权重为三进制 BitLinear；CPU 硬件由 arki05 提供。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbafs8/i_trained_a_language_model_on_cpu_for_40_hours_it/)

## 📰 重点报道

### 大型语言模型

- **ChatGPT Pro Lite 定价为每月 100 美元，结账提示** — 开发者发现的推文指出，ChatGPT 网页应用现在提及一项名为 'ChatGPT Pro Lite' 的计划，定价为每月 100 美元。结账页面描述似乎尚未完成，暗示该计划仍处于开发或测试阶段，尚未正式宣布。若确认，Pro Lite 将为 ChatGPT 用户引入更低价位的选项。 [來源-twitter](https://x.com/btibor91/status/2025332472511189059)
- **Tidy：云托管的 AI 代理学习使用任意应用** — Tidy 是一个个人代理，能够学习使用你使用的任意应用，从而执行你的工作流程。该系统云托管，通过 iMessage 向你提供更新，并提供一个持久化文件系统。它可以被教授在不编写代码的情况下安全地操作网站，将自己定位为 OpenClaw 的云端替代方案。 [來源-producthunt](https://www.producthunt.com/products/tidy-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)
- **Taalas 将 LLM 印在芯片上** — Taalas 概述了一种将大型语言模型直接嵌入硬件的方法。文章讨论了硬件-软件协同设计，使 LLM 能在芯片上运行，可能提升效率和部署能力。它强调了 LLM-on-chip 方法对产业界和研究的影响。 [來源-hackernews](https://www.anuragk.com/blog/posts/Taalas.html)
- **Qwen 团队指出 GPQA 与 HLE 评测存在严重数据质量问题** — 关于 DeepSeek-Overclock 的讨论表明，该模型可能推导出与 gold-standard 标签相冲突的正确推理，暴露评测集的数据质量问题。Qwen 团队已确认 GPQA 与 Humanity's Last Exam (HLE) 基准存在严重数据质量问题，凸显这些测试的潜在可靠性问题。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbnczy/the_qwen_team_verified_that_there_are_serious/)
- **O-TITANS：为 Gemma 3 提供正交 LoRA 的 TITANS** — 本帖介绍 O-TITANS，这是一个用于 Gemma 3 的正交 LoRA 方法，利用 Google 的 TITANS 内存架构。它概述 MoOLE-T，即通过一个 8B 路由器从一个或多个 O-LoRA 中进行并行推理并在出口节点运行一个更大（20B-80B）模型以解决冲突。设计承诺提供可扩展、互不干扰的技能模块，并具备训练 100+ 个 O-LoRAs 的潜力。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rb4luf/otitans_orthogonal_loras_for_gemma_3_using/)
- **Ouro 2.6B GGUF 模型发布：Q8_0 与 Q4_K_M 就绪** — Ouro 在 HuggingFace 发布了其 2.6B GGUF 模型（Q8_0 与 Q4_K_M），与 LM Studio、Ollama、llama.cpp 兼容。Ouro 是一个循环推理模型，在最终输出前执行多轮推理，其推理过程在结果中可见。发行说明澄清 GGUF 格式遵循标准的 Llama 架构，但 Ouro 包含三个自定义特性；值得注意的是，此版本跳过了早期退出门张量。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbbmcl/ouro_26b_ggufs_are_up_q8_0_and_q4_k_m_release/)
- **Nanbeige 4.1 冠军小型 LLM，胜过 Qwen 4B** — Reddit 用户声称 Nanbeige 4.1 是最佳的小型语言模型，并在给予足够“思考”空间时据称胜过 Qwen 4B。该帖将 Nanbeige 定位为本地 LLM 的首选，显示出对 Qwen 4B 的有利对比。来源归属：/u/Individual-Source618 在 r/LocalLLaMA。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rb61og/nanbeige_41_is_the_best_small_llm_it_crush_qwen_4b/)
- **Anthropic 的 Claude Code：用于编码和 Git 的终端 AI** — Claude Code 是一个在终端中运行、理解你代码库并通过执行常规任务、解释复杂代码以及通过自然语言命令管理 Git 工作流来加速编码的智能编码工具。它可在终端、IDE 或通过 GitHub 提及（@claude）使用。安装说明强调推荐的方法，并警告 npm 安装已弃用，指向设置文档。 [來源-github](https://github.com/anthropics/claude-code)

### AI 在销售

- **Ashera AI 分析 GTM 电话以将事实转化为行动** — Ashera AI 使用 AI 来分析 go-to-market 的销售电话，提供可执行的指导而非泛泛的摘要。它在通话中提供指导，提取每次通话后的风险/异议/下一步，自动更新你的 CRM，并对账户进行评分以显示交易健康状况。其独特之处在于在整个销售旅程中提供一个“唯一事实来源”，以让团队对所说的话保持一致；Product Hunt 上提供免费计划。 [來源-producthunt](https://www.producthunt.com/products/index-of-ashera?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)

### 开源

- **zclaw：ESP32 上 888 KB 以下的个人 AI 助手** — Zclaw 是一个开源的个人 AI 助手，设计在 ESP32 MCU 上运行，重量不足 888 KB。它展示了微控制器上的超轻量级 AI，能够在设备本地推理，无需云端。该项目托管在 GitHub，并在 Hacker News 讨论，表明社区对嵌入式 AI 的兴趣。 [來源-hackernews](https://github.com/tnm/zclaw)
- **Kon 发布了微型开源编码代理** — Kon 推出一个名为 kon 的新开源编码代理，在消费级硬件（i7-14700F、64GB RAM、RTX 3090）上运行 glm-4.7-flash-q4。该项目强调一个紧凑的框架，约有 215 个系统提示 token 与 600 个工具定义 token，在上下文前将对话控制在 1k token 以内。截止 2026 年 2 月 22 日，该仓库大约有 112 个文件，被定位为一个最小、Fork 并可扩展的编码代理。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rblce7/i_created_yet_another_coding_agent_its_tiny_and/)

### LLMs

- **IQ2 量化实现 LLM 的速度与质量平价** — Reddit 用户在 Qwen3-30B-A3B（10.3 GB）上测试 UD-IQ2_XXS，报告在全 GPU 卸载下速度提升约 5 倍（100 TPS vs 20 TPS），且在中学/大学主题的质量与 Q4_K_M 相当。在诸如哥德尔不完备性定理等细分领域，IQ2 略逊（81/100 对 92），一个 10 GB 的 IQ2 模型甚至解决了 Claude Opus 4.6 与 Sonnet 4.6 未解决的图形题目。帖子质疑为何极低量化并未得到更多炒作。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbio4h/has_anyone_else_tried_iq2_quantization_im/)

## ⚡ 快讯速览

- **批评者称 Frontier Labs 的 AI 声称会产出有缺陷、资源密集的软件** — 一则帖子嘲讽 Frontier Labs 声称 AI 能编写他们的代码，认为所发布的产品存在 bug 且资源消耗大。作者表示这曲解了他们的产品及其世界观。 [來源-twitter](https://x.com/mitchellh/status/2025350212014014564)
- **AI 应增进知识，而非外包认知** — Francois Chollet 主张 AI 应作为信息界面，帮助人们深化和提升知识与认知模型。他警告不要让 AI 成为依赖思考、削弱个人认知能力的拐杖。 [來源-twitter](https://x.com/fchollet/status/2025351708227108998)
- **Codex API 通过应用服务器实现本地 iPhone 集成** — 一名开发者描述 Codex 提供一个通过运行“codex app-server”即可访问的友好 API。他们还意外构建了一个原生 Codex iPhone 应用，能够在本地网络上启动并与 Codex 实例对话，Codex 集成直接在 iPhone 上运行。 [來源-twitter](https://x.com/gdb/status/2025265698587734432)
- **Figure 的自主机器人 24/7 运行并具备 HLS 回放** — 一则推文强调 Figure 的自主机器人持续运行、风雨无阻。系统据称支持 HTTP 实时流回放，凸显自主机器人领域的持续进展。 [來源-twitter](https://x.com/adcock_brett/status/2025282340159979591)
- **你的护城河：你 + AI，而非害怕被替代** — 一条 AI 相关推文认为，工人应停止担心 AI 替代他们。相反，应最大化与 AI 合作的优势——“你 + AI” 与 “他人 + AI” 的差距将成为他们的护城河。该信息强调将 AI 增强作为就业市场中的战略差异化因素。 [來源-twitter](https://x.com/Yuchenj_UW/status/2025270134903029862)
- **Straion 将 AI 编码代理的规则集中化以提升速度** — Straion 提供集中化的规则管理，覆盖 Claude Code、Github Copilot、Cursor 等 AI 编码代理。平台会自动为每个任务选择合适的规则，从而实现更快的企业级代码交付。它定位 Straion 为 AI 编码工具的编排层。 [來源-producthunt](https://www.producthunt.com/products/straion?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)
- **Cloudflare 发布由 Durable Objects 支撑的 AI Agents 平台** — Cloudflare 推出 AI Agents 平台，在其边缘网络上部署持久化、具状态的代理工作负载，借助 Durable Objects。代理提供实时通信、调度、AI 模型调用、MCP 与工作流，空闲时进入休眠且在不活跃时具备巨大的可扩展性且免费。开发者可通过 npm create cloudflare@latest -- --template cloudflare/agents-starter 开始，或通过 npm install agents 将其添加到现有项目中。 [來源-github](https://github.com/cloudflare/agents)
- **GitNexus：基于浏览器的代码知识图谱与 AI 代理** — GitNexus 是一个客户端工具，将一个 GitHub 仓库或 ZIP 索引成在浏览器中运行的知识图谱，捕捉依赖、调用链和执行流程。它提供交互式网页 UI 以供探索，以及 Graph RAG Agent，辅以 CLI 工具（MCP），为 AI 代理提供更深的体系结构视图以实现可靠的代码理解。 [來源-github](https://github.com/abhigyanpatwari/GitNexus)
- **AI uBlock 黑名单推出开源 AI 阻断清单** — Hacker News 的讨论聚焦开源项目 ai-ublock-blacklist，该清单托管在 GitHub，旨在在 uBlock Origin 中阻断与 AI 相关的域名。讨论获得大量互动，显示出对隐私导向、与 AI 相关的广告拦截工具的显著兴趣。该项目为用户提供了一个经过筛选的资源，用以在浏览器中屏蔽 AI 服务。 [來源-hackernews](https://github.com/alvi-se/ai-ublock-blacklist)
- **PSA：最新 Cline 版本中注入 OpenClaw** — 公共代理工具快速更新质量参差不齐。一则 Reddit 帖子称最近的 Cline 版本包含 OpenClaw 安装程序，暗示 OpenClaw 的广泛暴露和对 VSCode 扩展的不安全影响。此信息呼吁对工具进行更严格的审查，并建议关闭 VSCode 扩展的自动更新。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rb270r/psa_on_public_agentic_tools_and_the_speed_they/)
- ** Culture 和执行力推动伟大的 AI 产品。** — 作者认为成功的 AI 产品需要创造力和严格的技术执行力，强调文化与空间对想法成长以及强执行力的驱动作用。警告不要为虚构用户开发，而应来自真实用户需求的个人、以用户为中心的项目。文中提到 Pedro Domingos，并提及 Anthropic 及 Claude Code、Cowork、MCP 等产品在 Twitter 上的讨论。 [來源-twitter](https://x.com/ibab/status/2025304388877910082)
- **关于 AI 与数学的思考，受 First Proof 启发** — 本帖就 AI 与数学的关系作简短反思，灵感来自 First Proof。探讨数学思想如何为 AI 研究提供启发，以及 AI 如何照亮数学思维。 [來源-twitter](https://x.com/littmath/status/2025277247725199417)
- **寻找适用于本地 AI 模型的可靠编码代理** — Reddit 用户批评本地模型的编码代理选择，指出 Claude Code 频繁的上下文重新计算，以及 OpenCode 缺乏权限模型。他们还提到 Cline 的 OpenClaw 安装在用户机器上，主张需一个稳定、具有权限感知、可与本地模型共同运行的代理。他们请求推荐，并提及 Roo 与 Pi 作为竞争对手。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbmnw7/is_there_any_good_coding_agent_software_for_use/)
- **2026 年单张 RTX 3090 的最佳 LLM** — Reddit 帖子征求在单张 RTX 3090（24GB VRAM）上用于编码与推理的最佳综合模型的推荐。优先考虑点包括强代码生成（Go/TypeScript）、深度推理、保持在 24GB 内（允许量化）以及本地推理的可接受延迟。作者希望获得具体的模型名称和量化设置，并把 Qwen 与 DeepSeek 作为潜在选项。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbdsds/best_model_for_single_3090_in_2026/)
- **你在等待哪种 AI 模型：9B 还是 35B？** — Reddit 讨论请读者选择他们偏好的 LocalLLaMA 模型大小，是 9B 还是 35B 参数版本。帖子链接到 LocalLLaMA 的讨论串并征求对发布时间与可用性的意见。暂未提供具体公告。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbkeea/which_one_are_you_waiting_for_more_9b_or_35b/)
- **律师称谷歌在 NotebookLM 上传后关闭 Gmail、Voice、Photos** — Reddit 用户 /u/Thrumpwart 指控谷歌在将内容上传到 NotebookLM 之后不久便禁用了他的 Gmail、Voice 与 Photos。该贴将此事作为本地 LLM 讨论中的数据处理问题，但尚未得到独立核实。主张基于社交媒体帖子。 [來源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rbculq/lawyer_says_google_shut_down_his_gmail_voice_and/)
- **Anthropic 的内部工具据称包含 Slack、Zoom、Figma 等** — 一条非正式推文声称 Anthropic 使用如 Slack、Zoom、Figma、Notion、Workday 与 Google Workspace 等主流协作工具。作者请 Anthropic 纠正，暗示这些工具是公司日常工作流程的一部分。此贴展示了 AI 实验室的工具栈常接近企业级软件。 [來源-twitter](https://x.com/fchollet/status/2025343064991301705)
- **Gemini 3.1 Pro 被誉为最聪明，但用户表示不满** — 一条推文称 Gemini 3.1 Pro 是至今最聪明的模型，但作者表示讨厌使用它。帖子还请求开启 HLS 回放。 [來源-twitter](https://x.com/theo/status/2025401265682018578)
- **AI 数学领域狭窄；作者怀念真正的做数学** — 一条推文感叹 AI 依赖于少量数学思想，渴望从事更深入、真正的数学研究。作者反思 AI 的理论广度及其对有限数学的依赖。 [來源-twitter](https://x.com/jxmnop/status/2025248838907560440)

---

*由 AI News Agent 生成 | 2026-02-21*