# AI 日报 — 2026-02-28

> 覆盖 23 条 AI 新闻

---

## 🔥 今日焦点

### 1. AI 公司与 DoW 签署协议，在 DoW 的机密网络中部署模型

一家具 AI 公司宣布与 Department of War 签署协议，在 DoW 的机密网络中部署其模型。该协议确立了安全原则——禁止国内大规模监控，并确保对武力使用进行人类监督，包括自治武器——以及技术保障和云端部署的限定。它还要求 DoW 向所有 AI 公司提供相同条款。 [来源-twitter](https://x.com/sama/status/2027578652477821175)

### 2. Google 发现更长推理会降低准确性；引入 Deep Thinking Ratio

Google 研究人员在 AIME2024/2025、HMMT 2025 与 GPQA-Diamond 等评测中测试了八种模型变体（GPT-OSS、DeepSeek-R1、Qwen3 等），发现标记长度与准确性呈负相关（-0.54）。他们引入 Deep Thinking Ratio（DTR），用以衡量推理中的深层处理，其与准确性的相关系数达到 0.82。团队还提出 Think@n 策略：对多条推理路径进行采样，基于前 50 个标记估算 DTR，保留高 DTR 的前半部分，并通过多数投票来决定答案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh6pru/google_found_that_longer_chain_of_thought/)

### 3. Qwen3.5-35B-A3B 在 M1 上取代了我的两模型代理式设置

在 Reddit 的一帖中称，Qwen3.5-35B-A3B 能在同尺寸等级内达到或超过更大模型的推理、代理式与编码任务性能，甚至可与参数量高达数百亿级的模型竞争。用户在 Apple Silicon M1 Max（64GB RAM）上，通过 llama.cpp 服务器以 19 GB 的内存占用运行 Qwen3.5-35B-A3B，分析一份六页的 Amazon 2025 年 1 月销售 Excel 表，并为下月提出 10% 的销售提升建议。该单模型设置据称取代了他们先前的两模型代理式工作流，显示出在消费硬件上也具备强大的端到端能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh9k63/qwen35_35ba3b_replaced_my_2model_agentic_setup_on/)

---

## 📰 重点报道

### 行业

- **Anthropic 的 Amodei 在 Pentagon 将 Anthropic 列入黑名单后首次接受采访，表示该实验室爱国且致力于开发用于保卫美国的模型**；文中提到政府对自治武器和大规模监控的无条件访问，以及在紧急状态下的权力运用，包括供应链指定和通过 Truth Social 的六个月逐步退出。文本强调 AI 发展、政策与国家安全交叉处的紧张局势。 [来源-twitter](https://x.com/r0ck3t23/status/2027698383037591957)

### AI 工具

- **Claude Code 将新增 /simplify 与 /batch 两项技能** — Anthropic 的 Claude Code 将引入两项新技能 /simplify 与 /batch。这些功能自动化诸如将拉取请求推送到生产环境、执行可并行化的代码迁移等任务，显著减少人工工作量。作者表示他们每日都在使用，并很高兴公开分享。 [来源-twitter](https://x.com/bcherny/status/2027534984534544489)

### AI 安全

- ** Pentagon 拒绝对军事 AI 使用的否决权** — 五角大楼认为不应赋予对其购买的 AI 工具使用方式的否决权，此举主张在民用控制下的合法使用。文中将此与呼吁设定严格限制（不得进行大规模监控、须人类在环自治）的批评对比，并将美国治理与 PLA 的 AI 部署进行对照，文中提及 Claude 与 Dario Amodei。 [来源-twitter](https://x.com/PalmerLuckey/status/2027863376748286165)
- **DoW 对 OAI 与 Anthropic 的标准不同；Altman 在误导吗？** — 评论者认为 DoW 针对 OpenAI 与 Anthropic 适用不同标准，或称 Altman 在此推文中误导。鉴于 Altman 的历史，发帖者倾向于后者的解释。 [来源-twitter](https://x.com/StephenLCasper/status/2027582022017855686)

### 大型语言模型

- **CodexBar 在 Codex、Claude 等平台上跟踪 AI 使用情况** — CodexBar 是一个 macOS 14+ 菜单栏应用，用于显示来自 OpenAI Codex、Claude Code 和其他 AI 服务的逐提供商使用限制。它显示会话与每周的限制、各提供商状态、重置时间，以及一个可选总览标签，全部可通过设置配置。项目还提供 Linux CLI 支持与 Omarchy 集成，GitHub 上有发布，也提供 Homebrew 安装选项。 [来源-github](https://github.com/steipete/CodexBar)
- **Wei-Shaw Claude Relay 服务实现统一的开源 LLM 访问** — Wei-Shaw 的 claude-relay-service 提供自托管的 Claude Code 镜像，以及一个面向 Claude、OpenAI、Gemini、Droid 的统一开源中继，采用共用成本拼车模式。警告称 v1.1.248 及更早版本存在严重的管理员认证绕过漏洞，建议升级到 v1.1.249+ 或迁移到 CRS 2.0（sub2api），并推广具备多账户支持的自托管 Claude API 中继。该项目还将 pincc.ai 的 Claude/Codex 拼车服务通过 Codex CLI 推广，但提醒须注意 Anthropic 的条款、隐私与第三方镜像的可靠性问题。 [来源-github](https://github.com/Wei-Shaw/claude-relay-service)
- **Bare-Metal AI：无需操作系统/内核即可启动 LLM 推断** — 一则 Reddit 帖子描述了一个基于 UEFI 的应用，直接进入大语言模型推断阶段，不需要操作系统或内核。整个 AI 栈（分词器、权重加载、张量运算和推断引擎）在 freestanding C 环境下运行于 UEFI 启动服务之上，未来计划增加网络驱动并在网络上服务较小的模型。开发者表示目前速度较慢，未来优化以提升性能，主要用于实验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rhg3p4/baremetal_ai_booting_directly_into_llm_inference/)
- **Qwen3 Coder Next 基准测试在 Rust 与 Next.js 中** — 继续在本地生产仓库进行基准测试，作者比较 Qwen3 Coder Next、Qwen3.5 27B、Devstral Small 2 等相关模型在 Rust + Next.js 环境下的表现。先前结果显示 Qwen3.5 27B 在 78 任务的 Next.js/Solidity 基准测试中领跑，Devstral Small 2 则在 Next.js 上略胜一筹；Noctrex 基准测试也将 Qwen3-Coder-Next-UD-IQ3_XXS 与 Mistral、Qwen 系列模型对比。本次更新在 Rust + Next.js 仓库上测试，新增 LM Studio 的 Devstral Small 2 Q8_0，并将 KV Cache 修正为 Q8_0 以降低显存需求。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rhfque/qwen3_coder_next_qwen35_27b_devstral_small_2_rust/)
- **自组织映射实现多方向拒绝抑制** — 一个 Pull Request 提出使用自组织映射在多个方向上抑制拒绝，认为拒绝并非单一潜在方向，而是形成低维流形。关于 gpt-oss-20b 与 oss-120b 的结果显示，在不同的 KL 发散下拒绝抑制有所提升；早前的一维消融实验不足，HuggingFace 模型可视化了拒绝簇。来自卡利亚里大学的研究者参与了此项工作。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh69co/multidirectional_refusal_suppression_with/)
- **LLM Agent 将 KV-缓存传递以减少对令牌的重复处理** — 一位 AI 爱好者认为多代理 LLM 设置会对整个对话进行重分词与重新处理，导致大量令牌浪费（测试中约 47-53%）。他们提出 Agent Vector Protocol（AVP），在代理之间传递 KV-缓存而非文本，消除重分词和冗余的前馈传递。对 Qwen2.5、Llama 3.2、DeepSeek-R1-Distill 的早期测试报告显示令牌节省率为 73-78%，且无额外开销。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh802w/what_if_llm_agents_passed_kvcache_to_each_other/)

### 开源

- **Alibaba OpenSandbox 推出多语言 AI 沙盒平台** — OpenSandbox 是 Alibaba 的通用 AI 应用沙盒平台，提供多语言 SDK、统一沙盒 API，以及 Docker/Kubernetes 运行时。支持编码代理、图形界面代理、代理评估、AI 代码执行和强化学习训练等用例，内置环境与运行时生命周期管理。项目在 GitHub 的 Alibaba/OpenSandbox 仓库上托管。 [来源-github](https://github.com/alibaba/OpenSandbox)
- **InvisPose WiFi DensePose 提供实时隐私保护的人体姿态估计** — ruvnet 已发布 InvisPose 的生产就绪实现，该系统基于 WiFi 的密集人体姿态估计，利用信道状态信息而非摄像头实现全身姿态检测，能够穿墙跟踪。系统在 30 FPS 下延迟低于 50ms，支持多达人群跟踪（最高 10 人），并提供企业就绪的 API，具备跌倒检测、占用监测等分析功能，覆盖医疗、健身、智能家居和安保等场景。 [来源-github](https://github.com/ruvnet/wifi-densepose)

### 多模态

- **DeepSeek V4 将于下周发布，具备图像与视频生成能力** — 《金融时报》报道，DeepSeek 将在下周发布其长期期盼的 AI 模型 DeepSeek V4，新增图像和视频生成能力，标志着在竞争对手对抗中的多模态 AI 推进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh095c/deepseek_v4_will_be_released_next_week_and_will/)

---

## ⚡ 快讯速览

- **Anthropic 的 Amodei 为政府使用 AI 设定红线** — Anthropic 的 CEO Dario Amodei 告诉 CBS News，公司计划就政府对其 AI 技术的使用设定红线，表示越过这些红线将违反美国价值观。他还补充说，与政府的分歧是“世界上最美国的事”。 [来源-twitter](https://x.com/CBSNews/status/2027630480208560245)

- **Meta 的 Llama 4 在 AI 讨论中被边缘化** — 一则 X 帖子声称 Meta 已将 Llama 4 弃置到几乎不再出现在 AI 讨论之中，帖文将 Meta 对待 Llama 4 的方式视为其在竞争模型中地位下降的原因。该贴未提供独立验证。 [来源-twitter](https://x.com/JasonBotterill/status/2027621942858289664)

- **moeru-ai/airi 开源自托 AI Waifu 容器** — moeru-ai/airi 是一个开源项目，将 Neuro-sama 重现为名为 Grok Companion 的自托管 AI Waifu 容器，提供实时语音聊天和游戏支持（如 Minecraft、Factorio），覆盖网页、macOS 与 Windows，具备内存/RAG 功能与 Live2D 工具。该项目是 Project AIRI 的一部分，欢迎通过 Crowdin 进行翻译，并强调没有加密货币代币。 [来源-github](https://github.com/moeru-ai/airi)

- **OpenAI Pivot 获投资者青睐** — 一则匿名 Reddit 帖子指出投资者对 OpenAI 的最近转型充满热情，但未给出具体转型细节，只指市场对该方向的积极反应。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh2lew/openai_pivot_investors_love/)

- **Unsloth Dynamic 2.0 改善 GGUF 层量化** — Unsloth Dynamic 2.0 通过更新 GGUF 以选择性地对模型层进行更智能、更广泛的量化，从而在不牺牲性能的前提下实现更精细的压缩。该更新体现了对开源 AI 的持续优化努力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rh0xwk/unsloth_dynamic_20_ggufs_now_selectively/)

- **训练于猫推文的算法；被 killbot 声称干扰而中断** — 某人描述训练一个偏向猫相关内容的社会化媒体算法。报道称有时会出现非猫相关的帖子，其中包括声称政府计划用 AI 组建 Killbot 与大规模监控的说法，凸显对 AI 驱动推荐系统及其信息安全风险的担忧。 [来源-twitter](https://x.com/dieworkwear/status/2027595858137829616)

- **Small Qwens 更新新增 4 个隐藏条目** — 一则 Reddit 帖子称 unsloth 收藏新增了四个隐藏条目，标记为“13-9=4”。发帖者来自 /u/jacek2023，链接到进一步讨论。帖文中未提及官方 AI 产品或正式公告。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rgzul5/are_you_ready_for_small_qwens/)

---

*由 AI News Agent 生成 | 2026-02-28*