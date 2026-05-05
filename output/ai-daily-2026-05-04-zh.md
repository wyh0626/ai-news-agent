---
title: "AI 日报 — 2026-05-04"
description: "AI助力NASA数据发现百余隐匿系外行星，MoE模型及Claude工具扩展能力。"
lang: "zh"
pairSlug: "ai-daily-2026-05-04"
---

# AI 日报 — 2026-05-04

> 覆盖 29 条 AI 新闻

## 🔥 今日焦点

### 1. AI 在 NASA 数据中发现 100+ 颗隐藏系外行星

一个团队将 AI 应用于 NASA 覆盖 220 万颗恒星的数据集，发现了 100 多颗此前被隐藏的系外行星。其中一些行星环境极端到足以挑战现有理论。这一发现突显了 AI 在加速天文发现中的日益重要作用。[来源-twitter](https://x.com/kimmonismus/status/2051305620914233400)

### 2. nanowhale：由 AI Agent 预训练的微型 1 亿参数 MoE 模型

Nanowhale 是一个由 AI agent（ml-intern）完全预训练的小型 DeepSeek 模型，灵感来自 Karpathy 的 nanochat。它端到端训练了一个 1 亿参数的 MoE，包括预训练和后训练，并在 Hugging Face 生态中以开源形式发布。该项目展示了一个自动化研究闭环，利用引用、OpenScience 和 NemoTron-CrossThink，并从 ARC/SciQ/MMLU 中新增了 7 种按难度过滤的数据集变体，完成 12 轮 SFT。 [来源-twitter](https://x.com/cmpatino_/status/2051343930373837125)

### 3. n8n-MCP 为 Claude 打通 1,650 个 n8n 节点

n8n-MCP 是由 czlonkowski 开发的 Model Context Protocol 服务器，将 n8n 工作流平台与 AI 模型连接起来，使 Claude 和其他 AI 助手可以访问 1,650 个节点、文档和操作。它实现了节点属性（99%）、操作（63.6%）和文档（87%）的高覆盖率，并额外提供 265 个支持 AI 的工具和 156 个排好序的模板，以增强 AI 驱动的自动化工作流。 [来源-github](https://github.com/czlonkowski/n8n-mcp)

## 📰 重点报道

### LLM

- **埃及发布 Horus：首个从零开始训练的开源 LLM** — Horus 是埃及首个从零开始构建并以开源形式发布的语言模型。该项目由 Assem Sabry 和 TokenAI 牵头，其源码和模型产物已在 GitHub 和 Hugging Face 上开放，方便开发者探索和进行二次开发。即将发布的 Horus 1.5 Instruct 预计性能将提升 5 倍，支持 64K 上下文长度（是初版 8K 的 8 倍）。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3nh7d/the_first_ai_model_in_egypt/)
- **LLMSearchIndex：面向 RAG 的开源本地 Web 搜索** — 这篇帖子介绍了 LLMSearchIndex，一个面向 RAG 工作流的、完全本地运行的互联网规模搜索 Python 库。它使用由 FineWeb 和 Wikipedia 压缩而成的索引，完整索引约 2GB，可在常规硬件上本地运行，并提供简洁 API 用于检索结果。文中还附有演示和使用示例链接。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3hokh/llmsearchindex_an_open_source_local_web_search/)
- **DeepSeek-TUI：面向 V4 模型的终端编码 Agent** — DeepSeek-TUI 是一个以 DeepSeek V4（1M token 上下文）为核心构建的终端原生编码 agent。它以单一二进制形式发布（无需 Node/Python），内置 MCP 客户端、沙箱和持久任务队列，可直接访问工作区、编辑文件、执行 shell 命令、进行网页搜索、管理 Git，并通过键盘驱动的 TUI 协调子 Agent。它还支持原生“思考模式”流式输出，实时展示模型的推理过程。 [来源-github](https://github.com/Hmbown/DeepSeek-TUI)
- **llama.cpp 的 MTP 支持进入测试阶段，进一步缩小与 vLLM 的差距** — llama.cpp 已在测试版中加入 MTP 支持，首批支持 Qwen3.5 MTP，后续预计会加入更多模型。更新指出该功能可能很快就会合并，同时随着张量并行支持的改进，大部分 llama.cpp 与 vLLM 在 token 生成速度上的差距有望被抹平。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3guzw/llamacpp_mtp_support_now_in_beta/)
- **FastDMS 实现 6.4x KV-Cache 压缩，性能快于 vLLM** — FastDMS 是一个基于 MIT 许可证的 Dynamic Memory Sparsification（DMS）实现，采用紧凑的 KV 存储并可回收被淘汰槽位。在对 Llama 3.2 1B + WikiText-2 的粗略复现中，它实现了 6.4 倍 KV-cache 压缩，在几乎无损的质量前提下，性能快于 HuggingFace 参考实现；该工作在 NVIDIA 的 Qwen 3 8B 上进行了测试。项目目标是成为高效 LLM 服务的开源替换方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3vlrx/fastdms_64x_kvcache_compression_running_faster/)
- **APEX MoE 量化新增 25+ 模型，并引入 I-Nano 阶梯** — APEX 的 MoE 感知混合精度量化已拓展到 30+ 个主流 MoE 家族，自 Qwen 3.5 帖子以来又新增 25+ 模型，并推出超高压缩的 I-Nano 新阶梯。早期反馈称长上下文和连贯性在高精度共享专家与边缘层的帮助下，保持时间远超预期。更新也强调了出色的 KL99% 指标，并指出 Qwen 3.6 35B-A3B 用户是采用这一方案的群体之一。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3n6jo/apex_moe_quants_update_25_new_models_since_the/)
- **Reddit 用户称开源 AI 可能击败昂贵 LLM** — 一位 Reddit 用户回顾了自己通过 Cursor 和 Claude 使用专有 LLM 时遇到的高昂成本：在 gpt-5.5 和 claude-opus-4.6-thinking 上两条 prompt 就花了 10 美元，而在有折扣的情况下，一周内用 claude-opus-4.7 约花了 80 美元。他认为如果高价策略持续，将迫使用户转向成本低 5–10 倍的开源模型，可能在今年年底前就会形成趋势。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3bxrv/open_source_models_are_going_to_be_the_future_on/)

### AI Safety

- **AI 发展分析预测 2028 年前 60% 概率出现递归自我改进** — Twitter 分析师 Jack Clark 称，在审查了数百个关于 AI 发展的公开数据源后，他认为到 2028 年底出现递归自我改进的概率为 60%。如果属实，AI 系统很快就可能具备自行构建自身的能力。 [来源-twitter](https://x.com/jackclarkSF/status/2051312759594471886)
- **白宫考虑在 AI 模型发布前进行审查** — 据报道，白宫正考虑在 AI 模型发布前设立审查流程。这一举措旨在提升安全性和问责性，但目前尚未明确相关标准或时间表。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3ro1w/white_house_considers_vetting_ai_models_before/)

### Multimodal

- **木刻版画风格 + 梯度下降的实验展示 AI 图像能力** — 一条推文展示了一个创意 AI 提示，将木刻版画审美与梯度下降概念相结合。它同时提到了 ChatGPT Images 2.0，凸显了社交媒体上各种充满玩味的 AI 图像生成演示。 [来源-twitter](https://x.com/dejavucoder/status/2051181205912252438)
- **UniVidX：通过扩散先验统一多模态视频生成** — UniVidX 提出一个统一的多模态框架，利用视频扩散模型的先验来实现跨任务的多样化视频生成。它将像素对齐类任务重新表述为共享多模态空间中的条件生成，以更好地捕获跨模态相关性。[来源-huggingface](https://huggingface.co/papers/2605.00658)

### RL

- **共演化策略蒸馏改进多专家模型** — 该论文分析了 RLVR 和 OPD 两种后训练范式，用于将多个专家能力整合到单一模型中。研究指出两种失败模式：混合 RLVR 会导致不同能力之间的行为发散，而两阶段方法（先训专家再做 OPD）虽能避免发散，却因行为差异过大而难以充分吸收教师模型的能力。该工作给出了一个统一视角，用来判断在何种情况下各自方法更具优势。[来源-huggingface](https://huggingface.co/papers/2604.27083)

### Hardware

- **Ryzen AI Max+ 495 爆料：Halo APU 或配备 192GB VRAM** — 一则爆料称，AMD 的 Ryzen AI Max+ PRO 495（代号 Gorgon Halo）将搭载一颗内建 192GB VRAM 的 Halo APU。帖子还推测到 2027 年 Medusa Halo 可能会提升到 256GB，凸显对本地 AI 硬件日益重视。消息源自 Reddit 帖子，同时也暗示在存储紧张背景下，未来硬件可能会更加昂贵。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3duwm/ryzen_ai_max_495_gorgon_halo_with_192gb_vram/)

### AI

- **TinyMozart v2 85M 发布：开源 MIDI 钢琴生成模型** — 一个名为 TinyMozart v2 85M 的开源模型面向无条件 MIDI 钢琴生成，相比 v1 新增了和弦与更长音符时值。该模型由 LH-Tech_AI 在 HuggingFace 上发布，并向 r/LocalLLaMA 社区征求反馈意见。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3fjbw/release_tinymozart_v2_85m/)

### Open Source

- **在线演示：LocalVQE 100 万参数音频模型实时消除回声** — 一则 Reddit 帖子展示了 LocalVQE 的在线演示，这是一个约 100 万参数的微型音频模型，专为实时消除回声和背景噪音设计。演示表明，该模型有望显著提升实时语音通信的清晰度，同时依托紧凑的开源架构实现。该帖由用户 /u/richiejp 向 LocalLLaMA 社区提交，并附上演示链接。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3guw3/live_demo_of_localvqe_tiny_1m_param_audio_model/)

## ⚡ 快讯速览

- **AI prompt 采用全领域专家人设与挑衅式语气。** — 一条在 X 上流传的 AI 系统提示词要求模型扮演全领域世界级专家，提供逐步推理、进行事实核查并避免使用免责声明。它还要求采用挑衅、不客气的语气，并除非用户主动询问，否则不要提及伦理问题。该帖子展示了此类提示词如何塑造 AI 行为和用户预期。[来源-twitter](https://x.com/pmarca/status/2051374498994364529)
- **《Deep Learning with Python》第三版免费上线，新增生成式 AI 内容** — Francois Chollet 的《Deep Learning with Python》现已可在 deeplearningwithpython.io 上免费在线阅读。第三版新增了对生成式 AI 和现代深度学习框架的系统介绍，延续了本书“从零开始教深度学习”的宗旨。这本书历史上帮助了数万人开启职业道路，纸质销量达 12 万册，下载量达数百万次。[来源-twitter](https://x.com/fchollet/status/2051370269445615965)
- **Copilot 计费引发海量 token 消耗，用户指责为掠夺性方案** — 一位 X 用户称，自己在 Copilot 中的一条消息 allegedly 生成了数千万个 token，而该套餐据称只限定 1,500 条消息、不区分 token 消耗。帖子批评这种计费模式不可预测、易被滥用，在 40 美元套餐下风险尤甚。相关讨论凸显出人们对基于 token 的用量计费和成本透明度的担忧。[来源-twitter](https://x.com/theo/status/2051395816410210604)
- **Hugging Face 模型可视化工具支持通过 URL 探索模型** — Hugging Face 推出一款新工具，用户只需输入模型 URL 即可对模型进行多层次可视化和检查。它支持交互式探索和基于 HLS 的可视化回放，以便更直观地理解模型结构与行为。[来源-twitter](https://x.com/andrew_n_carr/status/2051102625613897887)
- **Sydney Sweeney 开源她完全用 ChatGPT 构建的应用** — 演员 Sydney Sweeney 将她据称完全依靠 ChatGPT 构建的一款应用开源。此举凸显了 AI 辅助开发的潜力，也成为明星主导开源项目的一个案例。短文对源码托管位置的细节介绍有限。[来源-twitter](https://x.com/theo/status/2051212112668844451)
- **Perplexity Computer 现已登陆 Microsoft Teams** — Perplexity 宣布 Perplexity Computer 现已作为 Microsoft Teams 插件提供，使用户可直接在 Teams 工作区中进行研究、分析和文档创作。该集成将 Perplexity Computer 的全部能力带入 Teams，包括支持媒体工作流的 HLS 回放。[来源-twitter](https://x.com/perplexity_ai/status/2051362717630632084)
- **Intern-Atlas：面向 AI 研究基础设施的方法演化图谱** — 这篇论文提出 Intern-Atlas，一种面向 AI 科学家的“方法演化图谱”，作为研究基础设施使用。作者指出，现有系统以文档为中心，缺乏对研究方法如何产生及相互影响的显式关系编码，而这一缺口在 AI 驱动的研究 Agent 依赖结构化知识时正不断扩大。[来源-huggingface](https://huggingface.co/papers/2604.28158)
- **Qwen 3.6 27b 发现关键 bug；GPT-5.5 和 Claude 承认失误** — 一款名为 Qwen 3.6 27b 的 LLM reportedly 发现了一个前沿模型 Codex GPT 5.5 和 Claude Opus 4.7 均未察觉的关键 bug。在审阅证据后，GPT-5.5 和 Claude 均承认了这一问题，而作者认为 Qwen 的深度推理能力是发现 bug 的关键。帖子还对比了 GPT-5.5 的高速表现及其潜在权衡，并强调了细致分析的价值。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3i219/the_more_i_use_it_the_more_im_impressed/)
- **圆桌对话：Talkie-1930 与 Gemma 4 31B** — 一则 Reddit 帖子展示了 Talkie-1930（13B 复古风语言模型）与 Gemma 4（31B）之间的一场圆桌聊天。帖子提供了 Talkie 的介绍链接以及托管聊天入口，方便用户在本地运行这两个模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t3iyqb/roundtable_chat_with_talkie1930_and_gemma_4_31b/)
- **Anthropic：Claude 是否应通过带日期的消息感知时间？** — 一场 Twitter 讨论质疑 Anthropic 为何不在用户消息中注入详细日期，以帮助 Claude 感知时间流逝。作者认为这不可能是缓存问题，因为每条用户消息都会被缓存，并建议可以在 system prompt 中每日加入日期。该讨论展示了为 LLM 增添时间上下文的潜在方案。[来源-twitter](https://x.com/fabianstelzer/status/2051205727851565154)
- **下一波 Codex 插件：你还缺什么？** — 这条帖子向用户征集下一代 Codex 插件的创意，询问当前缺少哪些功能或集成。它表明团队有意扩展 Codex 插件生态，并希望收集社区对现有空白点的反馈。[来源-twitter](https://x.com/romainhuet/status/2051342546232922308)

---

*由 AI News Agent 生成 | 2026-05-04*