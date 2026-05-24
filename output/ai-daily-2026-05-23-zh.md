---
title: "AI 日报 — 2026-05-23"
description: "通用人工智能近在眼前，估值高，推出4–8倍更快的任务模型。"
lang: "zh"
pairSlug: "ai-daily-2026-05-23"
---

# AI 日报 — 2026-05-23

> 覆盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. Demis Hassabis：奇点或在数年内通过 AGI 到来

Demis Hassabis 表示，技术奇点可能只剩下几年时间，有望由真正的 AGI 出现所触发。他认为，这种技术的变革性影响将使其成为有史以来最重要的技术。[来源-twitter](https://x.com/kimmonismus/status/2057975137518158253)

### 2. Anthropic 估值 615 亿美元，xAI 估值 800 亿美元

一条长贴梳理了 Anthropic 最新估值大约 615 亿美元，以及 Elon Musk 的 xAI 估值约 800 亿美元，并指出这两家公司都仍是私人公司且收入有限。讨论还涉及数据中心使用情况、本地影响，以及相关政治人物和媒体发言的评论。[来源-twitter](https://x.com/scaling01/status/2058259364360667399)

### 3. ZeroEntropy 打造快 4–8 倍的任务特定 AI 模型

仅有六人团队的 ZeroEntropy 正在构建任务特定 AI 模型，该团队声称其速度比 OpenAI 或 Anthropic 快 4–8 倍。该项目在 HuggingFace 上已获得约 50 万次下载，专注于面向生产的 AI 系统，提供最先进的 reranker、embedding，以及定制训练模型，同时实现更高精度、更低延迟和更低成本。[来源-twitter](https://x.com/garrytan/status/2058187750705418448)

## 📰 重点报道

### LLM

- **Command A+ 218B MoE 通过 MLX 移植在 Apple Silicon 上运行** — Cohere 发布了 Command A+（总参数 218B，激活 25B，128 个专家取 top-8），并为 mlx-lm 新增了 cohere2_moe 端口，使其可在 Apple Silicon 上运行。帖子包含架构说明、量化注意事项（W4A4 伪影 vs BF16）以及性能数据，并在 ml-explore 上开了一个 PR。在更大的机器上，从 BF16→Q8 的工作实现了约 22.9 token/s 的生成速度和约 57.6 token/s 的提示处理速度，峰值显存约 241GB。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlqxeh/command_a_218b_moe_running_on_apple_silicon_mlx/)
- **GPT-5.5 获赞实力强劲，在对比中略胜 Opus 一筹** — 一位 AI 评论者在 5 月 22 日称赞 GPT-5.5 是非常好的模型，指出其在复杂智能体任务上有重大提升。该用户表示 GPT-5.2 远落后于 Opus，而在体验了 5.5 之后再切回 Opus 4.7 会感觉在“降级”。帖子称赞了竞争格局，并认为 OpenAI 正在上演一次强势回归。[来源-twitter](https://x.com/gdb/status/2058048121674907670)
- **DSA 稀疏注意力加入 LLMs-from-Scratch 仓库** — DeepSeek Sparse Attention（DSA）的从零实现已被加入 LLMs-from-scratch 仓库，得益于一位读者的贡献。帖子包括动机和整体概览，并提供一个 GPT 风格模型的参考实现，作为独立示例代码。[来源-twitter](https://x.com/rasbt/status/2058206420927951191)
- **DeepSeek 将 V4 Pro API 降价举措转为永久** — DeepSeek 已将其对自家 V4 Pro API 暂时 75% 的降价变为永久，将输入成本降至每百万 token 0.435 美元、输出成本降至每百万 token 0.87 美元，综合约为每百万 token ~0.18 美元。运行人工分析智能指数（Reasoning, Max Effort）在 V4 Pro 上约需 268 美元，远低于 Gemini 3.1 Pro Preview、GPT-5.5 和 Claude Opus 4.7。公司将 V4 Pro 与 V4 Flash 一同定位在“智能指数 vs 运行智能指数成本”的帕累托前沿上。[来源-twitter](https://x.com/ArtificialAnlys/status/2058021452465799403)
- **Hermes Agent 支持跨会话记忆与自我学习** — Hermes Agent 被描述为最早一批能在多次会话间“记住一切”并通过使用不断改进的 AI 项目之一。它主打多层记忆、自我进化技能和可 24/7 自主运行的智能体，具备跨会话回忆能力，旨在让用户感觉它更像一位“操作员”而非工具。[来源-twitter](https://x.com/RoundtableSpace/status/2057978566457934032)
- **llama.cpp server 获得内置原生工具以处理 AI 任务** — llama.cpp server 中的实验性标志 --tools 现可启用一系列原生工具，包括 read_file、file_glob_search、grep_search、exec_shell_command、write_file、edit_file、apply_diff 和 get_datetime。这使得 llama-server 成为一个用于本地 AI 工作的迷你智能体框架，但目前尚无安全沙箱或允许命令白名单机制。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tluma3/llamacpp_server_have_builtin_native_tools_exec/)
- **Chrome Gemma4 在无 GPU 的 PC 上本地运行 Gemini Nano** — 一款 Chrome 扩展允许通过 Google Chrome 在 PC 上完全本地运行 Gemini Nano（Gemma4），无需 GPU。该方案 reportedly 使用约 16 GB 内存，每个会话约 9216 token，不需要 llama.cpp 或其他复杂配置；它以“一键安装扩展”Dobby 的形式在 Chrome 应用商店发布并在 Reddit 上分享。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlnqzj/run_chromes_tiny_gemma4_aka_gemini_nano_directly/)
- **可在无 GPU 条件下运行的最佳小型 LLM** — 一则 Reddit 帖子征询当下在仅用 CPU（无 GPU）条件下可运行的“最佳小语言模型”推荐，希望在准确性和速度之间取得平衡。作者同时希望了解部署技术栈以及在纯 CPU 环境下实际部署的经验。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tli757/what_is_the_current_best_small_language_model/)
- **用户报告：MOE 在 RAG 任务上优于致密模型** — 一位在构建“大一统”RAG 系统并处理海量数据集的 Reddit 用户对 Mixture-of-Experts（MOE）和致密模型进行了比较。他们表示，qwen3.6 35b APEX 相比某致密模型给出的答案更好、信息更丰富，并且在单张 RTX 3090 上吞吐量更高。讨论还涉及错误信息与可审计性等顾虑，以及在实际每秒 token 数表现上的差异。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlkgq6/any_reason_to_run_dense_over_moe_for_rags/)

### Industry

- **计算机解决 Erdős 问题，AI 进展加速** — 一条 Twitter 帖子声称，计算机正在“开口说话”并解决 Erdős（埃尔德什）问题，这标志着 AI 逐步迈向自动化解决问题的阶段。帖子还指出，对深度神经网络使用梯度下降的进展尚未出现停滞迹象，暗示 AI 正在快速前进，并将此作为对 AI 发展速度的“警钟”。[来源-twitter](https://x.com/willdepue/status/2058103681124282509)
- **美国绿卡政策打断持临时签证研究人员的工作** — 许多在 OpenAI、Anthropic、Google 和 Meta 工作的顶尖 AI 研究人员目前持临时签证居留美国，但美国政策要求他们必须回国才能申请绿卡。这为 AI 发展以及美国吸引全球人才的能力增加了不确定性、延迟和风险。作者指出，这对前沿实验室以及美国在 AI 领域的国家竞争力都有重要影响。[来源-twitter](https://x.com/kimmonismus/status/2058211601753505951)

### Open Source

- **LongCat-Video-Avatar 1.5 引入 Whisper-Large 编码器** — LongCat-Video-Avatar 1.5 是一个开源的“语音驱动人像视频生成”升级版本，基于 LongCat-Video，原生支持 AT2V、ATI2V 和视频续写功能。它用 Whisper-Large 取代 Wav2Vec2，以获得更平滑的唇部动作动态，并强调面向生产环境的稳定性、身份一致性，以及包括二次元动画和真实场景在内的广泛领域泛化能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tl4wpi/meituanlongcatlongcatvideoavatar15_hugging_face/)

## ⚡ 快讯速览

- **xAI 要想凭算力“弯道超车”还缺什么？** — Data Noir 在回复 @yacineMTB 时提出一个严肃问题：在算力充足的前提下，xAI 还需要什么才能实现领先？这条推文追问这样的跨越目前是否不可能，还是在合适人才的加持下有望一年内实现。该贴由此引出关于 AI 进步与资源需求、尤其围绕 xAI 的更广泛讨论。[来源-twitter](https://x.com/yacinelearning/status/2058253994053566478)
- **Codex 实现 iPhone 模拟器端到端构建与调试** — 一条基于 Codex 的工作流展示了如何端到端构建并调试 iPhone 模拟器。示例中 Codex 驱动模拟器对新构建的特性进行“打虫”（bug bash），并启用 HLS 播放功能。[来源-twitter](https://x.com/gdb/status/2058232892266836141)
- **使用 Qwen 0.6B 为 NVIDIA Nemotron Personas 生成向量嵌入** — 一则 Reddit 帖子介绍如何使用 Qwen 0.6B 为 NVIDIA 的 Nemotron-Personas 数据集生成 embedding 向量，以实现语义搜索和 K 近邻聚类。帖子提到已为韩国、日本、法国和美国预计算好了 embedding，并给出了 HuggingFace 数据集链接和 Web 演示地址。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlqcbi/embeddings_for_nvidias_nemotron_personas/)
- **本地 LLM 配合 Claude 处理会计任务** — 一则 Reddit 帖子介绍使用 Qwen 3.6 27B 完成月度结账、银行对账、应付/应收等会计任务，并搭配自建的 SQLite 数据库。作者还通过 anthropics/financial-services GitHub 仓库集成了 Claude 的技能，并指出在预算有限的硬件上，本地模型终于开始变得实用。他们提到在一块中等水平 GPU 上运行 MTP 版本一整夜，并对本地 AI 模型的实用性表示乐观。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tluvwg/local_model_doing_accounting_tasks/)
- **在小米 12 Pro 24/7 服务器上对比 Llama.cpp 与 LiteRT（V2）** — 一则更新帖子介绍在小米 12 Pro 上 24/7 无头运行 Llama.cpp 与 LiteRT 的 AI 服务器，并展示 V2 版本在散热和供电方面的重新设计。帖子描述了带背板风扇的铜散热片、前置铝板和两枚风扇以及导热垫，并设置在 40°C 启动、35°C 停止的温控方案。同时还介绍了接入手机 BMS 的定制电源，配有保险丝、4.3V 触发的 crowbar 保护、备用电源风扇以及 3D 打印的铝制支架。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlgxms/llamacpp_vs_litert_on_a_custom_xiaomi_12_pro_247/)
- **30 轮基准测试找出 MI60 上 Llama 最优配置** — 一位 Reddit 用户在 MI60 GPU 上使用预构建 docker 容器，对两个模型 Gemma4 和 Qwen3.6 进行了 30 轮 llama-bench 测试，以优化速度与效率，服务于 Frigate 和 HomeAssistant 的使用场景。帖子指出了在 MI60/MI50 上不同量化方式的性能差异。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlliw4/did_a_30_runs_of_llamabench_to_find_optimal/)
- **Karpathy 的 nn-zero-to-hero：从基础到 Transformer 的神经网络课程** — 这是一个托管在 GitHub 上的教育项目，规划了一门由 Karpathy 授课的神经网络课程。项目通过 YouTube 讲座与 Jupyter 笔记本讲解反向传播（micrograd）和语言建模（makemore），并计划扩展到 GPT 等 Transformer 风格模型。[来源-github](https://github.com/karpathy/nn-zero-to-hero)
- **用户称 Gary Marcus 阻止 AI 辩论** — 一位 X 用户声称，Gary Marcus 坚持不与任何人就 AI 进行辩论。作者表示自己分享了观点后就被其拉黑。帖子还特别说明推文中的配图与此事无关。[来源-twitter](https://x.com/theo/status/2058024420061692225)

---

*由 AI News Agent 生成 | 2026-05-23*