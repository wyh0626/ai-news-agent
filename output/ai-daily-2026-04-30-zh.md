---
title: "AI 日报 — 2026-04-30"
description: "向防御者推出GPT-5.5-Cyber，增强Codex提示与ChatGPT安全。"
lang: "zh"
pairSlug: "ai-daily-2026-04-30"
---

# AI 日报 — 2026-04-30

> 共收录 29 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 向关键网络防御方推出 GPT-5.5-Cyber

OpenAI 即将在未来数日内向关键网络防御机构开始部署 GPT-5.5-Cyber，这是一款前沿级网络安全模型。公司表示将与更广泛的生态系统以及政府合作，为网络行动建立可信访问机制，目标是在最短时间内帮助企业和基础设施实现安全加固。 [来源-twitter](https://x.com/sama/status/2049712078836170843)

### 2. Codex 为日常办公提供基于角色、应用关联的提示工作流

最新的 Codex 更新支持基于角色的工作流，允许用户先选择一个角色，再关联日常使用的应用，并尝试系统推荐的提示词。它通过与各类应用的集成，支持从调研、规划到文档、幻灯片和电子表格等各类日常任务。该功能强调以 Codex 作为核心助手，帮助用户显著简化流程、提升工作效率。 [来源-twitter](https://x.com/OpenAI/status/2049928776147230886)

### 3. OpenAI 为 ChatGPT 推出高级账号安全功能

OpenAI 正在为 ChatGPT 账号推出“高级账号安全”可选功能，主要面向更易遭受数字攻击的高风险用户。此次更新增加了抗钓鱼登录方式、更强的账号找回能力，以及更完善的防护机制，以保护敏感数据并防止账号被接管。 [来源-twitter](https://x.com/OpenAI/status/2049902506881462613)

## 📰 重点报道

### LLM

- **GPT-5 中“地精输出”的来源，OpenAI 给出解释** — OpenAI 公开解释了模型输出中所谓“goblins（地精）”现象，详细说明了这类由“人格”驱动的怪异行为如何在包括 GPT-5 在内的模型间扩散。文章梳理了该现象出现的时间线、深层原因以及拟采取的修正方案，以限制此类行为。OpenAI 将这些怪癖视为需要在未来模型中加以理解与解决的问题。 [来源-twitter](https://x.com/OpenAI/status/2049690533845663830)
- **GLM-5V-Turbo 推进多模态基础模型发展** — GLM-5V-Turbo 被视为面向多模态智能体的原生基础模型的一大进展。该方法把多模态感知视为推理、规划、工具调用与执行的核心组成部分，使智能体能够在图像、视频、网页、文档和 GUI 等多种媒介上进行操作。相关工作已发布在 HuggingFace，作为将感知与推理一体化到基础模型中的持续探索。 [来源-huggingface](https://huggingface.co/papers/2604.26752)
- **2026 年 4 月：本地 LLM 迎来迄今表现最佳的一个月** — /r/LocalLLaMA 上的一篇帖子称 2026 年 4 月是本地 LLM 的一个“高光月份”，并邀请社区讨论被低估的模型。文中指出，MiniMax-M2.7 已从 MIT 许可证转为非商业许可证，因此被从对比图中移除，并特别感谢用户 pmttyji 汇总模型列表和绘制图表。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t06y43/open_models_april_2026_one_of_the_best_months_of/)
- **Qwen-Scope 发布 Qwen 3.5 官方稀疏自编码器套件** — Qwen 团队发布了 Qwen-Scope，这是面向 Qwen 3.5 系列（2B–35B MoE）的稀疏自编码器（Sparse Autoencoders）工具集。它将残差流中的特征映射到一个“内部概念字典”，从而让人可以观察诸如“法律语气”或“Python 代码”等高层语义概念，而不只是原始数值。该工具包支持精确的“手术式消除（Surgical Abliteration）”，用来抑制特定概念，以及“特征操控（Feature Steering）”，在生成时强制激活某些概念；项目使用 Apache 2.0 许可，但作者提醒不要用它来移除安全过滤。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1szrbub/qwenscope_official_sparse_autoencoders_saes_for/)
- **Mistral 3.5 128B MLX 4-bit：当前存在问题，需要打补丁** — 一位用户报告将 Mistral Medium 3.5 128B 转换为 MLX 4-bit 后遇到多项问题。目前 MLX 路径尚不支持 Eagle 推测解码模型，一个清洗器（sanitizer）Bug 导致视觉模块中有 438 个参数被跳过，同时还存在性能和采样方面的限制；帖子描述了本地补丁方案，具体细节写在 Hugging Face 的 readme 中。该用户目前不建议下载或使用该版本模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t09anw/mistral_medium_35_128b_mlx_4bit_70_gb/)

### Multimodal

- **GPT Image 2“笨拙重画”提示走红** — 一条面向 GPT Image 2 的提示词在 X/Twitter 上疯传，它要求将图像以刻意笨拙、类似 MS Paint 的风格重画。提示说明中强调输出要刻意“低质量”、像素化，整体上与原图大致相似但又明显“画歪”，从而产生幽默效果。这条爆款帖子来自 X 用户 arrakis_ai。 [来源-twitter](https://x.com/arrakis_ai/status/2049689793118998717)
- **RADIO-ViPE 在单目视频中实现开放词汇语义 SLAM** — RADIO-ViPE 是一个在线语义 SLAM 系统，可在开放词汇的自然语言查询下实现具备几何感知的语义定位。它直接在原始单目 RGB 视频上运行，无需相机内参、深度传感器或位姿初始化，这得益于其紧耦合的多模态融合机制。该方法将自然语言提示与动态环境中的局部 3D 区域和目标物体建立对应。 [来源-huggingface](https://huggingface.co/papers/2604.26067)
- **DeepSeek 发布基于视觉原语的多模态推理框架** — DeepSeek 与北京大学、清华大学合作发布论文《Thinking with Visual Primitives》及其开源仓库，提出一种新的多模态推理框架。该框架将空间 Token（坐标点和边界框）提升为最小“思维单元”，并与模型的思维链（chain-of-thought）交织，使模型在推理过程中可以“指向”图像中的具体位置。该项目已在 GitHub 上以 deepseek-ai/Thinking-with-Visual-Primitives 名义开源。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1szwi1d/deepseek_released_thinkingwithvisualprimitives/)

### Industry

- **TIME：Alphabet 通过 AI-first 战略完成自我重塑** — 报道回顾了 2016 年 Sundar Pichai 宣布 Google 将转型为“AI-first 公司”，并开始大力投资定制芯片、云计算、YouTube 以及搜索之外的前沿 AI 研究等项目。TIME 在 TIME100 Companies 特辑中认为，这些围绕 AI 的下注已经开始回报，推动了 Alphabet 的重塑与影响力扩张。 [来源-twitter](https://x.com/NewsFromGoogle/status/2049839561971273923)

### AI Safety

- **在 PyTorch Lightning 中发现 Shai-Hulud 恶意软件** — Semgrep 报告称，在 PyTorch Lightning 这一 AI 训练库中发现了恶意依赖项。这款以 “Shai-Hulud” 为主题的恶意软件凸显了开源机器学习工具链和依赖体系中的安全风险。研究人员建议开发者审计项目依赖并更新受影响包，以降低在 AI 训练过程中被恶意利用的风险。 [来源-hackernews](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/)

### Open Source

- **jcode：新一代 Coding Agent Harness** — 由 1jehuang 开源的 jcode 是一款面向多会话工作流的新一代编码智能体“挂架”（harness），强调高度可定制性与高性能。它支持跨平台安装（macOS/Linux 可通过脚本安装；Windows 和其他环境则提供详细安装指南），并提供 RAM 与启动时间基准测试，对比 Codex CLI、OpenCode、GitHub Copilot CL 等工具，展示其资源效率优势。 [来源-github](https://github.com/1jehuang/jcode)
- **Llama-swap 新增矩阵分组以并行运行多模型** — Llama-swap 新增“矩阵（matrix）”特性，允许用户以矩阵的形式对模型进行分组，从而实现并发执行。此前每个模型只能属于一个分组；现在可以自定义多类分组（如“大模型组”“STT+大模型组”“RAG 使用场景组”等），调度器会基于成本卸载模型。配置示例展示了基于 solver 的做法，并提示配置文件必须二选一：要么使用 matrix，要么使用旧版分组方式。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1szwjrp/psa_llamaswap_released_a_new_grouping_feature/)

### Hardware

- **单卡 RTX 3090 跑 Qwen3.6-27B，支持 218K 上下文并稳定调用工具** — 在一张 RTX 3090 上，Qwen3.6-27B 文本和代码场景下可达到约 218K 上下文，吞吐约 50–66 TPS；视觉场景下支持约 198K+ 上下文，吞吐约 51–68 TPS。输出约 25K Token 规模的工具调用任务现已可以在不 OOM 的情况下完成，表明稳定性明显提升。这些进展得益于 genesis-vllm 补丁中的 PN12 锚点漂移问题被修复（PR #13），使高上下文配置重新可用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t07su1/followup_qwen3627b_on_1_rtx_3090_pushing_to_218k/)
- **32 张 AMD MI50 组成集群，运行 Kimi-K2.6 达到 9.7/264 tok/s** — 一个由两节点、共 32 块 AMD MI50 GPU 组成的配置，在 vllm 分支上运行 Kimi-K2.6 时，输出速度约为 9.7 tokens/s，输入速度约为 264 tokens/s。整机功耗从约 640W（空闲）到约 4800W（峰值）不等。作者指出，这种配置非常小众，除非电力几乎免费，否则性价比并不高，并在文中给出 GitHub 链接和精确的启动命令。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t0b0ie/final_monster_32x_amd_mi50_32gb_at_97_ts_tg_264/)

## ⚡ 快讯速览

- **Claude Code 在 JSON 中屏蔽 OpenClaw 提及，并额外计费** — 一则轶事贴称，如果提交的 JSON 中某次提交记录提到 OpenClaw，Claude Code 要么会拒绝请求，要么会多收费用。测试者使用的是空仓库，并直接调用 Claude Code，将这一结果形容为“疯狂”。该贴凸显了围绕 OpenClaw 相关代码可能存在的安全或策略触发点。 [来源-twitter](https://x.com/sama/status/2049715178611380317)
- **AI 自动化的是任务，而非整份工作；放射科医生收入反而上涨** — AI 更倾向于自动化具体任务，而不是替代整个岗位。当某项任务成本下降后，与之相关的工作需求往往反而会上升。由于当前 AI 在自主性方面有限且仍需人类监督，实现对整份工作的端到端自动化仍非常困难，放射科医生在 AI 进步背景下仍然加薪就是一个例子。 [来源-twitter](https://x.com/fchollet/status/2049644995293163830)
- **Mira：戴在脸上的 AI，记录每一次对话** — 一则推广信息介绍了一款名为 Mira 的 AI 产品，被描述为“住在你脸上的 AI”，能够捕捉用户的每一次对话，以此打造高度个性化的 AI 体验。推文中包含“立即下单”的号召，并提到启用了 HLS 播放功能。 [来源-twitter](https://x.com/AnhPhuNguyen1/status/2049874217051853013)
- **Exploratory Sampling 提升大模型语义多样性** — 研究者提出 Exploratory Sampling（ESamp）这一解码方法，以推动大模型输出在语义层面而非表层词汇层面实现多样化。ESamp 基于这样一种假设：神经网络在处理与训练分布相似的输入时表现更佳，因此在生成过程中显式鼓励多样且具有语义意义的输出。 [来源-huggingface](https://huggingface.co/papers/2604.24927)
- **Z 世代用 AI 越多，对 AI 的厌恶感也越强** — The Verge 的一篇文章探讨：Z 世代对 AI 的使用不断增加，但对 AI 的负面情绪也在加剧。文中分析了可能原因，包括隐私担忧、对未来被颠覆的恐惧等，并指出一种“悖论”：越来越多的年轻人离不开 AI，却又愈发不喜欢它。文章将这种态度置于关于 AI 社会影响的更广泛争论之中。 [来源-hackernews](https://www.theverge.com/ai-artificial-intelligence/920401/gen-z-ai)
- **Warp 开源基于 GPT 的智能体开发环境与工作流** — Warp 是一个诞生于终端的“智能体化开发环境”，现已在新的 Warp 仓库下开源，并由 OpenAI 赞助。该项目提供基于 GPT 的智能体管理工作流，支持内置编码智能体或集成第三方 CLI 智能体，如 Claude Code、Codex、Gemini CLI 等。安装程序和 UI 组件采用 MIT 许可证，并提供基于 Web 的仪表盘和依托 GitHub 的协作能力。 [来源-github](https://github.com/warpdotdev/warp)
- **Zig 解释其反 AI 贡献政策背后的原因** — Zig 项目发布文章，阐述其“反 AI 贡献”政策的来龙去脉。文中说明了其治理思路，以及该政策将如何塑造贡献方式和维持项目标准。官方将这一举措定位为 Zig 在社区建设与代码质量目标上的重要一环。 [来源-hackernews](https://simonwillison.net/2026/Apr/30/zig-anti-ai/)
- **Mike：开源法律 AI 项目** — 有帖子重点介绍了一个名为 Mike 的开源法律 AI 项目，网站为 mikeoss.com。该项目在 Hacker News 上引发了大量讨论，目前获得 189 个赞和 92 条评论。 [来源-hackernews](https://mikeoss.com/)
- **基准对比：Claude Code Caveman 插件 vs 简短提示词** — 一位博主对 Claude Code 的 Caveman 插件与“简要提示词”方式进行基准测试。对比内容包括输出啰嗦程度、准确性和开发体验，并给出在插件辅助与纯提示词工作流之间做选择的实践性建议。 [来源-hackernews](https://www.maxtaylor.me/articles/i-benchmarked-caveman-against-two-words)
- **Hipfire 使用 Docker 在 RX 7900 XTX 上配合 llamacpp 运行** — 一名 Reddit 用户将 hipfire 制作成 Docker 镜像，与现有的 llamacpp 栈并行运行，从而缓解 Qwen3.6 27B 在长上下文下的失败问题。他在 RX 7900 XTX 上运行 Qwen3.6 27B MQ4，日志显示 TriAttention 辅助模块和 DFlash 草稿加载均已启用，实际自回归生成约 40 tokens/s，但 DFlash 是否真正参与推理尚未确认。其 CLI 为一个 Bun/TypeScript HTTP 服务器，通过子进程方式启动引擎，并表示有意分享 Dockerfile 与 compose 配置。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t09hbr/got_hipfire_running_in_docker_on_my_rx_7900_xtx/)
- **CUDA+ROCm 同时运行 GGML 后端** — 一位 Reddit 用户展示了在 Windows 上使用 CUDA 和 ROCm 同时运行 Minimax 2.7 Q4 模型的方案，从而绕过 Vulkan。其配置实现了 63/63 的全层卸载，并同时分配了较大的 CUDA 与 ROCm 缓冲区，突出其在预填充阶段的优势。该方案通过启用 GGML_BACKEND_DL，并在 CMake 中切换 GGML_HIP 与 GGML_CUDA 以完成配置。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t0bkaf/cuda_rocm_simultaneously_with_dggml_backend_dlon/)
- **新隐身模型 Owl Alpha 曝光，被怀疑来自中国** — 一则 Reddit 帖子讨论了名为 Owl Alpha 的“隐身模型”，并根据其对部分提示的拒答行为推测其可能来自中国。帖子还声称该模型拥有 100 万上下文窗口，由用户 /u/Kingwolf4 提交并提及 LocalLLaMA。围绕该模型的来源和实际能力，目前社区仍存在不少猜测与不确定性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t00dmk/new_stealth_model_owl_alpha/)

---

*由 AI News Agent 生成 | 2026-04-30*