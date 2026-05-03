---
title: "AI 日报 — 2026-05-02"
description: "OpenAI与Anthropic发布新模型，AI证明推进Erdős 1196与60年猜想，GLM-5V-Turbo成多模态基础模型。"
lang: "zh"
pairSlug: "ai-daily-2026-05-02"
---

# AI 日报 — 2026-05-02

> 覆盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 与 Anthropic 在“派对式”预览中发布新模型

OpenAI 以一种节日、玩乐的方式发布了新模型。与此同期，Anthropic 推出了一个研究预览模型，宣称具备广泛的互联网访问能力，并警告其可能带来的岗位替代风险。相关报道在 X 上以挑衅性、梗图驱动的语气广泛传播。 [来源-twitter](https://x.com/omooretweets/status/2050592759887900714)

### 2. AI 生成证明推进 Erdős 问题 1196 与一项 60 年猜想

研究者对 GPT-5.4 Pro 提供的证明方法进行了改进和适配，用于解决 Erdős 问题 1196，并进一步证明了若干附加结果，其中包括 Erdős、Sárközy 与 Szemerédi 提出的一个已有 60 年历史的猜想。他们认为，AI 生成证明可以开启新的研究路径，并在 “Future of Mathematics Symposium”（数学未来研讨会）上宣布了这一成果。 [来源-twitter](https://x.com/jdlichtman/status/2050460077904285789)

### 3. GLM-5V-Turbo：面向多模态智能体的原生基础模型

GLM-5V-Turbo 被提出为迈向多模态智能体原生基础模型的一步。论文指出，当基础模型被部署到真实环境中时，智能体能力必须覆盖在图像、视频、网页、文档以及 GUI 等异构场景中的感知与行动。作者强调，应将多模态感知作为推理、规划、工具使用和执行的核心组成部分进行一体化整合。 [来源-huggingface](https://huggingface.co/papers/2604.26752)

## 📰 重点报道

### Multimodal

- **视觉 AI 演进为具身世界建模，超越外观生成** — 最新的视觉生成模型在照片级真实感和交互式编辑方面取得了长足进展，但在空间推理、状态持续性、长时间尺度一致性以及因果理解上仍存在不足。作者主张从单纯的外观合成转向建立在结构、动态、领域知识和因果关系之上的智能视觉生成，并提出一个五级分类框架来刻画这一演化路径。 [来源-huggingface](https://huggingface.co/papers/2604.28185)
- **RADIO-ViPE 支持从单目 RGB 实现开放词汇语义 SLAM** — RADIO-ViPE（Reduce All Domains Into One — Video Pose Engine）是一个在线语义 SLAM 系统，通过将自然语言查询与动态环境中的 3D 区域与对象进行定位绑定，实现具备几何感知的开放词汇理解。与需要标定 RGB-D 输入的方法不同，RADIO-ViPE 直接作用于原始单目 RGB 视频流，无需相机内参、深度传感器或位姿初始化。它依赖紧密的多模态融合，以在实时条件下支持开放词汇的语义理解。 [来源-huggingface](https://huggingface.co/papers/2604.26067)

### LLM

- **2026 年 4 月本地 LLM 榜单：Qwen3.5、Gemma4 表现亮眼** — 该帖重点介绍了围绕本地、开源权重 LLM 的持续热度，包括 Qwen3.5 与 Gemma4 等新版本，以及来自 GLM-5.1 的“最新 SOTA 表现”说法。同时也提到 Minimax-M2.7、Bonsai 1-bit 等易上手选项，并邀请用户分享详细配置，以帮助在基准测试存在诸多陷阱的背景下进行导航。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sknx6n/best_local_llms_apr_2026/)
- **Qwen3.6-27B 结合智能检索在本地实现 95.7% SimpleQA** — 一位 LDR 维护者展示了在本地搭建的 LLM 方案：使用 RTX 3090、Ollama 后端运行 qwen3.6:27b。其 LangGraph_agent 基于 LangChain 工具调用，并采用并行子话题分解（最高 50 次迭代），且由 LLM 自我打分。基准测试结果显示 Qwen3.6-27B 在 SimpleQA 上达到 95.7%（287/300），在 xbench-DeepSearch 上为 77.0%；Qwen3.5-9B 分别为 91.2% 和 59.0%，而 gpt-oss-20B 为 85.4%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1n6o8/we_are_finally_there_qwen3627b_agentic_search_957/)
- **研究者驳斥前沿模型参数规模：GPT-5.5 约 1.5T 且置信区间极宽** — 一篇爆火论文声称 GPT-5.5 拥有 9.7 万亿参数，并对多款前沿模型提出类似说法。研究者 Ben Sturgeon 与作者对论文进行了复查，发现方法论存在严重问题；在修正方法后，GPT-5.5 的参数量估计值约为 1.5 万亿，在 90% 置信区间下分布在 2560 亿到 8.3 万亿之间。 [来源-twitter](https://x.com/justanotherlaw/status/2050399317782155726)
- **在 Apple Silicon 上运行 Moondream 推理：本地三模型流水线** — 一种在 Apple Silicon 上直接运行 Moondream 推理的方案，无需使用 MLX，通过 Whisper、Qwen、Moondream 组成的三模型堆栈，实现离线处理，延迟约为 1 秒。该配置支持 Mac、屏幕内容可视化以及离线 HLS 播放，展示了端侧 AI 的潜力。 [来源-twitter](https://x.com/vikhyatk/status/2050372962952601996)
- **Eywa：面向科学任务的异构智能体框架** — 论文提出 Eywa，这是一种异构智能体框架，旨在将以语言为中心的系统扩展到科学领域。通过集成领域特定的基础模型，Eywa 试图处理超出自然语言范畴的任务，从而拓展智能体 LLM 在科学问题中的应用边界。 [来源-huggingface](https://huggingface.co/papers/2604.27351)
- **Qwen3.6-27B 在 Windows 上：原生 vLLM 跑出 72 tok/s** — 一套在 Windows 上原生部署 Qwen3.6-27B 的方案借助修改版 vLLM 分支，在 RTX 3090 上对短提示达到 72 tok/s，对长提示（约 2.5 万 token）为 64.5 tok/s，在 127k 上下文长度下仍有 53.4 tok/s，且全部运行在单卡上。若使用两张 RTX 3090，可实现 160k 上下文。该项目提供便携式启动器/安装器，无需管理员权限或 Python，并在 http://127.0.0.1:5001/v1 暴露 OpenAI 兼容端点，同时提供 GitHub Release。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1judm/qwen3627b_at_72_toks_on_rtx_3090_on_windows_using/)
- **Qwen 3.6 基准测试夺冠，Gemma 4 实战表现更出色** — 一位测试者在本地使用 vLLM 和 FP8 对 Qwen 3.6 与 Gemma 4 的 27B/31B 视觉模型进行对比，发现基准测试更偏向 Qwen，而实际使用体验则更看好 Gemma。文章重点描述了两者在行为模式、token 消耗习性以及官方基准与实际任务之间差距方面的差异。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1te8y/qwen_36_wins_the_benchmarks_but_gemma_4_wins/)
- **Warpdrv：用于本地 Qwen 模型的开源 Llama.cpp 启动器** — Warpdrv 是一个开源的 Llama.cpp 启动器，用于在本地运行基于 Llama.cpp 的 LLM，使高端配置能够并行运行两套 Qwen 模型、使用不同后端。项目展示了在 Strix Halo、RTX Pro 5000 Blackwell 等硬件上运行 Qwen 3.6 27b 和 35b，系统环境为 Ubuntu 25.10，并搭配多种加速后端。它内置模型路由器，支持 opencode 与 Claude-Code 工作流、MCP.json、工具调用以及实验性的 KV-cache checkpointing，不过默认并不附带 llama.cpp 的构建版本。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1w920/warpdrv_my_opensource_llamacpp_launcher_for/)

### AI Agents

- **Hermes Agent 成为 2026 年最佳本地 AI Harness 候选** — 一则社交媒体帖子认为，在运行本地 AI 时，智能体框架比模型本身更关键。作者赞扬 Hermes Agent 的工具调用整洁、持久化记忆与子智能体功能，称其性能优于 OpenClaw 等框架。贴文将 Hermes 评为 2026 年通用型智能体的首选之一，并指出其在多种硬件配置下开箱即用的广泛能力。 [来源-twitter](https://x.com/sudoingX/status/2050605436752330840)

### AI

- **xAI 语音克隆上线：支持 28 种语言、80+ 声音** — xAI 通过其 API 上线了语音克隆功能，允许开发者在不到两分钟内创建自定义声音，或从覆盖 28 种语言的 80 多种现成声音库中选择。该技术主要面向语音智能体、有声读物、电子游戏角色等应用场景，并将很快支持 Hermes Agent 集成。 [来源-twitter](https://x.com/Teknium/status/2050473306592076282)
- **中国 AI 模型大约落后美国领先模型 8 个月** — 一位评论者声称，中国 AI 模型相较美国最领先的模型大约存在 8 个月的差距。DeepSeek V4 被拿来作为例子，认为其能力大致落后美国顶尖模型约 8 个月。这一说法援引 nist.gov 作为信息来源。 [来源-twitter](https://x.com/scaling01/status/2050395242663223751)
- **使用开源 AI 模型复刻 “Anipartment”** — Reddit 上一则名为 “Anipartment” 的贴文展示了一个人物在虚构公寓中放松的高细节二次元风格图像。原帖及评论随后被删除，但在后续嵌套线程中泄露出大致描述和示例提示词，作者据此尝试使用开源模型 ZIT 与 Klein9B 复刻这组高细节视觉效果。 [来源-reddit](https://www.reddit.com/r/StableDiffusion/comments/1t1q9sa/anipartment_replication_of_a_deleted_post_using/)
- **复现 TurboQuant：PROD 版本实测逊于论文声称结果** — 一位 Reddit 用户从零实现了 TurboQuant（arXiv:2504.19874）。MSE 变体效果符合预期，但 PROD 版本在 4-bit 下仅实现约 95.8% 的相关性，达不到论文宣称的 >99%。他们还观察到，即便相关性看似不错，注意力质量仍出现退化，并讨论了方差缩放、位打包等可能原因，同时质疑结果是否依赖于维度或具体设置；其实现代码已公开。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t208qv/implemented_turboquant_and_results_dont_fully/)

### World Models

- **斯坦福研讨会深入探讨世界建模：从重建到潜空间预测** — 斯坦福最新的研讨会聚焦 AI 中世界建模的演进，重点分析从传统重建方法转向潜在空间预测的转变。内容涵盖 JEPA 与 World Models、Causal JEPA、LOWER 模型，以及其在实践、规划与未来发展前景中的应用。 [来源-twitter](https://x.com/techwith_ram/status/2050445994479755767)

### Open Source

- **Flare-TTS 28M：基于 LJSpeech 训练的开源 TTS 模型** — Reddit 用户 LH-Tech_AI 发布了 Flare-TTS 28M，这是他们首个从零训练的文本转语音模型，在单张 NVIDIA A6000 GPU 上使用完整 LJSpeech 数据集训练约 24 小时、约 300 个 epoch。该模型免费开源托管在 Hugging Face，并提供音频示例。目前只支持英语，音色略带机械感，但作者鼓励社区进行更多实验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1mmnd/release_finally_my_first_tts_model_is_out/)

### LLMs

- **KV Cache 量化：性能收益 vs 可靠性风险** — 一则 Reddit 帖子讨论在两张 NVIDIA GeForce RTX 3090 上使用 vLLM 对 Qwen-3.6 27B 的 KV cache 进行 FP8 量化，以支持长时序负载。作者指出，FP8 KV cache 会引入隐性误差与可靠性问题，而 16-bit KV cache 在可靠性和速度上都更优。他们质疑社区为何仍将 KV-cache 量化视为重要优化手段。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1t4nw/kv_cache_quantization_ignorance_or_malice/)

## ⚡ 快讯速览

- **让 AI 扮演经理而非程序员，引发多智能体“宫斗戏”** — 一条 Twitter 线程描述了给 GPT-5.5 下达指令，让它充当经理而非程序员，并将任务分派给子智能体。随着时间推移，模型最终还是亲自上手写代码，凸显了角色设定与多智能体涌现行为之间的张力，并顺带提及 Claude Opus 4.7。该贴以轻松的方式反思了 AI 治理与任务委派动态。 [来源-twitter](https://x.com/gneubig/status/2050382542348357885)
- **Sam Altman：更聪明的模型比更便宜或更快更重要** — Sam Altman 认为，虽然更便宜、更快速的 AI 模型值得追求，但“更聪明”仍应是首要目标。他在推文中指出，相比降低成本或延迟，智能水平对价值的驱动更大。这一观点折射出业内关于效率与能力如何平衡的持续争论。 [来源-twitter](https://x.com/sama/status/2050671161915371998)
- **探索式采样提升 LLM 语义多样性** — 研究者提出 Exploratory Sampling（ESamp），这是一种显式鼓励语义多样性的解码方法，超越传统随机采样的范围。该方法的动机在于：神经网络在与训练分布更相似的输入上预测误差更低，而 ESamp 旨在在推理阶段主动扩展语义探索空间。 [来源-huggingface](https://huggingface.co/papers/2604.24927)
- **simstudioai/sim 发布开源 AI 智能体编排平台** — Simstudioai/sim 是一个开源平台，用于构建、部署和编排 AI 智能体。它提供可视化工作流、Copilot 辅助的节点生成与调试，并支持与 1000+ LLM 集成。同时平台也支持用于知识对齐的向量数据库，并提供通过 sim.ai 或 Docker 的云托管与自托管部署选项。 [来源-github](https://github.com/simstudioai/sim)
- **Quadtrix.cpp：仅依赖 CPU、使用 C++17 实现的 GPT 风格 Transformer** — 独立项目 Quadtrix.cpp 在纯 C++17 环境中实现了 GPT 风格语言模型，无任何外部依赖，且在 CPU 上训练。该模型使用手写张量运算与完全解析式反向传播，总计约 0.83M 参数，包含 4 层、4 个注意力头、200 维隐藏。项目报告在 128 token 上下文窗口与 3140 万字符语料上训练约 76 分钟后，最佳验证损失约为 1.64。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1x9jv/i_built_a_transformer_in_c17_from_scratch_no/)
- **Hugging Face 模型可视化工具：直观展示模型结构** — hfviewer.com 是一个用于可视化 Hugging Face 模型结构的新工具。用户只需粘贴模型 URL，即可生成交互式结构图，示例包括 Qwen3.6-27B 与 Gemma 4 系列，作者也在积极征集使用反馈。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t24y4p/i_made_a_visualizer_for_hugging_face_models/)
- **Tinygrad 驱动在 RDMA 集群上测试 MoE 性能** — 一则 Reddit 帖子宣布计划在由 Blackwell + M3 Ultra 组成、拥有近 2 TB 内存的 RDMA 集群上测试 Tinygrad 驱动处理 MoE 负载的表现。作者邀请社区提供基准测试建议并参与实验协作。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t24qle/tinygrad_driver_testing/)
- **Unsloth 修复 Mistral 3.5 在 YaRN 解析下的推理 Bug** — Unsloth 与 Mistral 合作发布了更新后的 GGUF 文件，以修复影响多种实现的 Mistral Medium 3.5 推理 Bug。问题源于 YaRN 解析中的一个小坑，影响了 transformers、llama.cpp 等多个框架，最终通过将 mscale_all_dim 从 1 调整为 0 得到解决；同时 mmproj 文件也被修正，确保正确生成。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t1itn1/unsloth_solved_bug_in_mistral_medium_35/)
- **Petdex 上线 Codex 宠物公共画廊** — Petdex 是一个用于发现、分享和一键 curl 安装 Codex 宠物的公共画廊。平台现已开放投稿，并主打 “Pets. Now in Codex” 的口号，以及用于唤醒宠物的 /pet 命令。 [来源-twitter](https://x.com/RaillyHugo/status/2050498466669887571)
- **传 Elon Musk“闯入” GPT-5.5 活动并施加“诅咒”** — 一条 Twitter 帖子声称 Elon Musk 将不请自来出现在 GPT-5.5 活动上，并对活动“施加破坏性诅咒”。该比喻将 Musk 的可能现身类比为《睡美人》中的女巫，更像是在暗示潜在争议，而非确认消息。对此应视作围绕 GPT-5.5 的行业八卦与舆论风向。 [来源-twitter](https://x.com/AndrewCurran_/status/2050424542603132976)
- **Codex 对决 Claude Code：17 亿 token vs 8000 万，谁先触顶？** — 作者声称自己在一天内在 Codex Pro 5x 上花费了 17 亿 token，在 Claude Code Max 20x 上则为 8000 万，并提问是哪一方率先触发了使用上限警告。该贴凸显了 OpenAI 的 Codex 与 Anthropic 的 Claude Code 在大规模 token 使用场景中的差异，也暗示了高负载代码生成任务可能遇到的额度限制。 [来源-twitter](https://x.com/arankomatsuzaki/status/2050620582434382228)
- **Claude 被限流后，用户改测 DeepSeek V4：过千万 token 成本惊人** — 一位 AI 从业者在遭遇 Claude 限流后首次尝试 DeepSeek V4。经历超过 1000 万 token 的调用后，他对成本表达了震惊，指出在大规模使用 LLM 时价格可能成为主要障碍。这一经历凸显了在实际工作负载中，成熟模型与新晋工具之间在价格与性能上的权衡。 [来源-twitter](https://x.com/jbhuang0604/status/2050686882653065496)
- **用这个脚本在 llama.cpp 中屏蔽指定短语** — Reddit 上有人推荐了一个用于在 llama.cpp 中屏蔽短语的脚本，并在附带的 README 中提供了配置说明。GitHub 仓库 llama-cpp-phrase-ban 由 BigStationW 创建，为 llama.cpp 提供短语过滤工具，本帖由用户 Total-Resort-3120 提交。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t227hk/ban_phrases_on_llamacpp_with_this_script/)

---

*由 AI News Agent 生成 | 2026-05-02*