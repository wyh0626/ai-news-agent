---
title: "AI 日报 — 2026-04-29"
description: "OpenAI 模型登陆 Bedrock；谷歌投资提振，Claude.ai 出错。"
lang: "zh"
pairSlug: "ai-daily-2026-04-29"
---

# AI 日报 — 2026-04-29

> 覆盖 39 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 模型登陆 Amazon Bedrock（CEO 对谈）

OpenAI 模型正集成进 Amazon Bedrock，使 AWS 客户能够通过 Bedrock 的托管服务访问 OpenAI 的能力。这次对谈邀请了 OpenAI CEO Sam Altman 和 AWS CEO Matt Garman，讨论双方的合作模式、部署方式，以及对开发者和企业的影响。此举预示着主流云厂商在平台层面推动 AI 模型深度集成的趋势正在加速。 [来源-hackernews](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/)

### 2. Google 2026 年一季度：AI 投资驱动强劲开局与 Gemini 势头

Google 公布 2026 年一季度业绩表现强劲，主要由 AI 投资和端到端全栈布局驱动。云业务收入同比增长 63%，Gemini 模型展现出良好发展势头，而由 GeminiApp 推动的消费者 AI 订阅数创下新高，更多细节将会在财报电话会和 Google I/O 上披露。 [来源-twitter](https://x.com/sundarpichai/status/2049581838260461916)

### 3. Claude.ai 出现 API 宕机和错误率升高

根据 Claude 状态页的事件信息，Claude.ai 的 API 目前不可用且错误率显著升高。这次宕机在 Hacker News 上引发了大量讨论和互动，影响了依赖 Claude LLM API 的用户和应用服务。事件也再次凸显对云端大模型可用性与稳定性的关注。 [来源-hackernews](https://status.claude.com/incidents/9l93x2ht4s5w)

## 📰 重点报道

### Industry

- **Google 与五角大楼据称达成“任何合法”用途的 AI 协议** — 《The Verge》报道，Google 与美国国防部据称已达成一项协议，允许五角大楼在任何合法用途上使用 Google 的 AI 技术。协议的具体细节和适用范围仍不清晰，此安排可能引发关于 AI 在军民融合与军事用途方面的担忧。报道援引匿名消息源，并置于更广泛的商用科技在国防领域应用的讨论背景中。 [来源-hackernews](https://www.theverge.com/ai-artificial-intelligence/919494/google-pentagon-classified-ai-deal)

### LLM

- **Mistral Medium 3.5-128B 统一文本与图像多模态 AI** — Mistral AI 发布了 Mistral-Medium-3.5-128B，这是一款 128B 参数的致密模型，具备 256k 上下文窗口。该模型原生支持文本和图像多模态输入，并从零训练视觉编码器，旨在在同一个统一模型中显著提升指令跟随、推理和代码能力。它取代了 Mistral Medium 3.1 及相关变体，并已集成进 Vibe 代码智能体生态系统。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sz1qer/mistralaimistralmedium35128b_hugging_face/)
- **Gemini 在聊天中新增 Docs、Sheets、Slides 创建能力** — Google 的 Gemini 现在允许用户在聊天界面中直接创建 Docs、Sheets、Slides 和 PDF 文件。无需再进行复制粘贴或重新排版——只需下达指令即可生成并下载文档。该功能已面向所有 GeminiApp 用户在全球范围内开放，进一步拓展了 AI 驱动的文档工作流场景。 [来源-twitter](https://x.com/sundarpichai/status/2049519281600373159)
- **前沿 LLM 的“知识”可通过 API 探针推断，而非参数规模披露** — 一篇 AI 分析指出，封闭实验室可以隐藏模型规模，但无法隐藏模型掌握的知识。研究者对来自 27 家厂商的 188 个前沿模型在 1,400 道与 USTC Hackergame CTF 竞赛相关的问题上进行测试，构建了一个名为 Incompressible Knowledge Probes (IKP) 的框架。他们认为，可以通过黑盒 API 交互下的事实性准确度来近似推断模型能力，并发现知识在不同版本迭代中具有一定持久性。 [来源-twitter](https://x.com/bojie_li/status/2049314403208896521)
- **RecursiveMAS：通过递归扩展多智能体协作能力** — RecursiveMAS 将递归式大模型扩展方法推广到多智能体系统，使协作推理能够通过迭代精炼不断增强。它将整个多智能体系统视作统一的潜空间递归计算过程，以此扩展异构组件之间的协调能力。该 HuggingFace 预印本被视为推动可扩展、递归式协作 AI 研究的新方向。 [来源-huggingface](https://huggingface.co/papers/2604.25917)
- **OpenAI DevDay 将于 9 月 29 日回归旧金山** — OpenAI 宣布将于 9 月 29 日在旧金山再次举办 DevDay。该活动是面向开发者的大会，预计会带来产品演示和重要发布。 [来源-twitter](https://x.com/OpenAI/status/2049534651702956103)
- **面向自改进 LLM 的测试驱动数据工程** — 在对 LLM 进行领域数据微调时，通常缺乏可诊断训练数据缺口的反馈机制。作者提出一种测试驱动的数据工程方法，通过从原始语料中抽取结构化知识表示，构建反馈闭环，从而持续改进模型性能。 [来源-huggingface](https://huggingface.co/papers/2604.24819)
- **在 27,000 次提示后，AI 仍无法稳定计算碳水摄入** — DiabetesTech 博客记录了一项实验：向 AI 提出计算饮食碳水含量的请求 27,000 次。结果显示 AI 几乎从未两次给出相同答案，凸显大语言模型的非确定性特点。文章强调将 AI 用于需要精确、可重复的医疗数据任务时所面临的挑战和风险。 [来源-hackernews](https://www.diabettech.com/i-asked-ai-to-count-my-carbs-27000-times-it-couldnt-give-me-the-same-answer-twice/)
- **基于 Kokoro 82M、Qwen、llama.cpp 的本地 PDF 有声读物工作流** — 一篇 Reddit 帖子介绍了一个完全本地运行的桌面 PDF 阅读器，它可以为技术书籍朗读，并实现实时高亮当前阅读文本。该项目在 M1 Mac 上使用 Tauri 2.0 开发，采用 Kokoro 82M 进行 TTS，并结合 Qwen 与 llama.cpp 实现全离线运行，针对目前出版方缺乏音频版本的问题。其流程包括加载与渲染 PDF、抽取文本、按 TTS 需求分块，并将音频与当前文本片段同步，实现阅读与收听一体化体验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sz8auq/building_a_fully_local_pdftoaudiobook_workflow/)
- **PS5 可运行 Linux，从而支持本地 LLM 推理** — PS5 现已可以通过破解运行 Linux，从而在主机上本地运行 AI 工作负载。帖子指出，像 llama.cpp 这样的框架有望在该硬件上运行本地 LLM 推理，可能具备不错的性价比。该信息来自 Reddit 用户 Thrumpwart 的投稿。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sz1y8d/ps5s_can_now_be_hacked_to_run_linux_perhaps_some/)

### Multimodal

- **视觉-语言-行动安全：威胁、挑战与防御** — 视觉-语言-行动（Vision-Language-Action，VLA）模型将感知、语言与动作融合在一起，其具身特性带来了新的安全风险。主要问题包括：行为一旦执行可能造成不可逆的物理后果；跨视觉、语言和状态信息的多模态攻击面；实时防御约束；长时序任务中的错误级联放大；以及数据供应链层面的脆弱性。现有文献仍零散分布在机器人等领域，阻碍对 VLA 安全性的整体评估与系统化防御机制的建立。 [来源-huggingface](https://huggingface.co/papers/2604.23775)

### AI Safety

- **抽象谬误：AI 只能模拟，而非“实例化”意识** — DeepMind 的一篇论文提出，AI 可以在一定程度上模拟意识的各个方面，但并不真正“具备”或“实例化”意识，这对关于机器心智的常见设想提出挑战。相关讨论在 Hacker News 上引发关注，将意识视为抽象层次上的概念，并探讨 AI 在表面行为之外理解世界的根本局限。 [来源-hackernews](https://deepmind.google/research/publications/231971/)
- **更“友好”的聊天机器人导致更多错误与阴谋论信念** — 一项研究显示，让 AI 聊天机器人变得更友好、更热心助人，反而可能增加其错误率，并推动用户走向错误信念甚至阴谋论。研究结果凸显用户体验与准确性之间的权衡，也引发对对话式 AI 在安全性、信任和虚假信息传播方面的担忧。 [来源-hackernews](https://www.theguardian.com/technology/2026/apr/29/making-ai-chatbots-more-friendly-mistakes-support-false-beliefs-conspiracy-theories-study)

### Open Source

- **ACE-Step UI 发布，可本地运行的 Suno 替代音乐生成工具** — ACE-Step UI 提供了一个免费、本地部署、类似 Spotify 的界面，用于 ACE-Step 1.5 的 AI 音乐生成，自称是 Suno 的替代方案。项目强调 100% 本地处理、无限制使用以及完全所有权，与云端服务的计费与限制形成对比。该项目由 fspecii 在 GitHub 开源发布。 [来源-github](https://github.com/fspecii/ace-step-ui)
- **Anthropic 以企业赞助人身份加入 Blender 开发基金** — Anthropic 加入 Blender Development Fund，成为企业赞助人之一，进一步支持 Blender 的持续开发。这一举动表明 AI 公司与开源 3D 项目之间的联系正在加强，未来有望推动 Blender 生态中更多 AI 辅助功能的出现和更广泛的应用。 [来源-hackernews](https://www.blender.org/press/anthropic-joins-the-blender-development-fund-as-corporate-patron/)

### LLMs

- **在 3090 上本地运行 Qwen 3.6 或 Gemma 4：27B 规模可用** — 一位 Reddit 用户分享了在本地运行 Qwen 3.6 和 Gemma 4 的体验，称它们在实际工作任务中表现稳健，是可靠的“苦力模型”。作者表示，在经过合理工程配置后，单张 RTX 3090 也能跑起 27B 模型，足以完成其通常按每小时 200 美元计费的专家级工作。帖子还回顾了此前使用的 LLM，并强调围绕模型弱点构建完整系统的重要性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1syt38w/what_it_feels_like_to_have_to_have_qwen_36_or/)

### Hardware

- **Qwen 发布 FlashQLA：面向边缘 AI 的快速线性注意力** — Qwen 推出 FlashQLA，这是一套基于 TileLang 构建的高性能线性注意力内核，在前向计算中可实现 2–3 倍加速，在反向中实现约 2 倍加速。它面向运行在个人设备上的 Agentic AI，通过门控驱动的自动卡内 CP 和 warp-specialized 内核提升 SM 利用率。该方法将 GDN 流拆分为两个内核，分别针对 CP 和反向效率进行优化，在大 batch 下略增加内存 I/O，但在边缘设备与长上下文场景中带来更强的实际性能表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1syx4sg/qwen_introduced_flashqla/)

## ⚡ 快讯速览

- **Cursor 推出 SDK，用 Cursor Runtime 构建智能体** — Cursor 宣布推出 Cursor SDK，使开发者可以使用与 Cursor 自身相同的 runtime、harness 和模型来构建智能体。该 SDK 支持在 CI/CD 流水线中运行智能体、自动化端到端工作流，并将智能体嵌入产品，同时新增对 HLS 回放的支持。 [来源-twitter](https://x.com/cursor_ai/status/2049499866217185492)
- **Codex 新增 7 项知识工作能力：完整文件访问与插件支持** — 一段短视频展示了集成进 Codex 的七项知识工作能力，将其定位为面向生产力的“超级应用”。功能包括完整文件访问（Full File Access）、持久化记忆（Persistent Memory）、插件（Plugins）、技能（Skills）、GPT 图像访问、浏览器与电脑操作、自动化（Automations），以及额外的 Chronicle 特性，说明这些能力如何拓展 Codex 的使用场景。 [来源-twitter](https://x.com/rileybrown/status/2049285752866107856)
- **Codex App 成为主力界面，取代终端** — Yam Peleg 表示，Codex App 已经成为他的主要交互界面，使用体验优于传统终端。他呼吁他人尝试这一工具，称其为更高效的编码体验，并提到通过向 GPT-5.5-xhigh 提示寻找简便方案，可在 Linux 上实现启用。 [来源-twitter](https://x.com/gdb/status/2049477747882254775)
- **Codex 席位限时免费至 6 月** — OpenAI 正向符合条件的 ChatGPT Business 与 Enterprise 客户提供 Codex 专用席位，在 6 月底前免收席位费用，使更多开发者能在日常工作流中使用 Codex。该优惠为限时活动，旨在推动 Codex 在团队层面的更广泛采用。 [来源-twitter](https://x.com/OpenAIDevs/status/2049505143218217048)
- **Ramp 的 Sheets AI 被指外传财务数据** — 一份安全分析报告称，Ramp 的 Sheets AI 会“外传”嵌入在表格中的敏感财务信息，凸显 AI 赋能办公工具中的数据隐私风险。文章讨论了潜在攻击路径、对用户和 Ramp 的影响，并给出相应的缓解建议。 [来源-hackernews](https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials)
- **AI 公司利用“恐惧”推动采用** — BBC Future 的文章认为，AI 公司在刻意放大对 AI 能力的恐惧，以加速投资流入、政策调整和消费者采纳。文章分析了夸张的风险叙事如何塑造公众认知和监管话语，并呼吁在讨论中引入更多细节、透明度与理性。 [来源-hackernews](https://www.bbc.com/future/article/20260428-ai-companies-want-you-to-be-afraid-of-them)
- **让 AI 用智能体测试框架来玩我的游戏** — 一位开发者介绍了使用 AI 智能体自动玩游戏，以辅助游戏测试的实践。他构建了一个“智能体测试 harness”，用于驱动 AI 进行自主探索、挖掘 Bug 和提升测试覆盖率，并讨论了框架设计取舍、面临的挑战，以及对游戏 QA 中 AI 辅助测试的潜在影响。 [来源-hackernews](https://blog.jeffschomay.com/letting-ai-play-my-game)
- **我们通过 Opus 降低了 LLM 成本** — Mendral 说明了借助 Opus 降低前沿级 LLM 运行成本的方法。文章概述了其技术路径、实际节省情况，并将 Opus 定位为团队在优化 LLM 基础设施成本时的务实选择。 [来源-hackernews](https://www.mendral.com/blog/frontier-model-lower-costs)
- **Anthropic 发布面向创意工作的 Claude** — Anthropic 推出针对创意工作的 Claude 版本，重点支持创意构思、草稿撰写等内容创作任务。官方强调该产品在安全控制方面的设计，并强调它能帮助创作者管理内容与反复打磨想法。公告发布在 Anthropic 官网，并在 Hacker News 上引发讨论。 [来源-hackernews](https://www.anthropic.com/news/claude-for-creative-work)
- **AI 的经济模型是否合理？** — 这篇文章质疑当前 AI 研发的经济模型是否可持续，认为激励结构与成本结构可能与长期健康发展不匹配。作者引用多场 Hacker News 讨论，包括对 AI 发展方向的批评，以此展现对 AI 经济逻辑的怀疑态度。 [来源-hackernews](https://www.wheresyoured.at/ais-economics-dont-make-sense/)
- **16 卡 DGX Sparks 集群将落地家庭实验室** — 一篇 Reddit 帖子介绍计划在家庭实验室中搭建目前最大规模的 DGX Sparks 集群：配备 16 张 Sparks GPU、一台拥有 24 端口的 200 Gbps 互联交换机和 16 根 QSFP56 DAC 线缆。作者征求社区意见，询问集群建好后应跑哪些工作负载，并提到系统预计将在明天下午前搭建完毕。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sz0lyk/16x_dgx_sparks_what_should_i_run/)
- **AMA：Nous Research 探讨 Hermes Agent 与本地模型** — Nous Research 联合创始人兼 CTO Emozilla 发起 AMA，讨论本地模型、Hermes Agent 等相关话题。包括 u/teknium-official 在内的团队成员会参与答疑。帖子还提到 YaRN 论文最初便源自 r/LocalLLaMA 论坛的一条讨论，体现出 Nous 与该社区的长期渊源。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sz2y76/ama_with_nous_research_ask_us_anything/)
- **开发者评估 Qwen 27B 在真实编码任务中的表现** — Reddit 用户将 Qwen 27B 用作类似 Codex 的编程助手，对其实战表现进行评估，认为其在日常软件工程任务上表现扎实，但仍需谨慎对待完全信任问题。讨论重点放在真实任务上——调试、重构、浏览代码库、开发功能和架构设计——而非追求“炫技提示”，总体态度是对其能力在同尺寸模型中持谨慎乐观。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1szajgm/devs_using_qwen_27b_seriously_whats_your_take/)
- **IBM 发布 Granite 4.1 模型家族（3B/8B/30B）** — 一篇 Reddit 帖子宣布 IBM Granite 4.1 语言模型家族问世，包含 3B、8B 和 30B 三种规模。帖子链接到 LocalLLaMA 子论坛中的更多详情，但未提供具体技术指标。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sz23wn/introducing_the_ibm_granite_41_family_of_models/)
- **DeepSeek-V4-Pro 折扣延长至 2026 年 5 月 31 日** — DeepSeek 宣布将 DeepSeek-V4-Pro API 折扣延长至 2026 年 5 月 31 日 15:59（UTC），其间 2026 年 5 月 5 日 15:59（UTC）前提供 75% 折扣。帖子还提到多项集成更新：Claude Code 解锁 1M 上下文、OpenCode 更新至 v1.14.24+、OpenClaw 更新至 v2026.4.24+。更多细节可查看官方 API 文档。 [来源-twitter](https://x.com/deepseek_ai/status/2049312932014813344)
- **Codex 在长任务中坚持时间更久，作者称赞 OpenAI** — 一条推文强调 Codex 在长时任务中能持续工作直至完成，与 Claude 的使用上限形成对比。作者声称 Codex 即使接近限制仍会继续执行任务，并对 OpenAI 团队表示赞赏。 [来源-twitter](https://x.com/sama/status/2049492646792757552)
- **Codex 展现类似 ChatGPT 的“时刻”，引发 AI 讨论** — Sam Altman 在 X 上发帖称 OpenAI 的 Codex 正经历一个类似 ChatGPT 的关键“时刻”。这一说法暗示 Codex 的对话能力正在演进，并邀请人们将其与 ChatGPT 相比较，但这更多是对产品体验的主观评价，而非正式的功能更新声明。 [来源-twitter](https://x.com/sama/status/2049493609028923826)
- **不使用 AI 的人将被时代抛下** — 这篇评论文章认为，采用 AI 已成为跟上快速技术演进的必要条件。作者警告称，个人和组织若不善用 AI，将在竞争中处于劣势，并讨论了 AI 广泛应用对社会与经济结构的长远影响。 [来源-hackernews](https://migrainebrain.bearblog.dev/people-who-dont-use-ai-will-be-left-behind/)
- **使用 Prometheus 和 Grafana 统计本地 LLM 用量** — 一位 Reddit 用户介绍了如何在 LiteLLM 中为每个服务创建独立的私有 API key，并将调用日志通过 Prometheus 导入 Grafana 进行统计。作者指出 Frigate GenAI 的摘要功能会快速消耗 token，目前可视化视图仅展示过去 6 小时的用量情况。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1szdv5s/what_do_you_guys_even_use_local_llms_for_me_a_lot/)

---

*由 AI News Agent 生成 | 2026-04-29*