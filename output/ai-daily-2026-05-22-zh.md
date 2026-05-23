---
title: "AI 日报 — 2026-05-22"
description: "GeminiOmni首秀，玻璃翼曝高危漏洞，Qwen3.7-Max棋测领先。"
lang: "zh"
pairSlug: "ai-daily-2026-05-22"
---

# AI 日报 — 2026-05-22

> 覆盖 43 条 AI 新闻

## 🔥 今日焦点

### 1. Gemini Omni 发布，本周社区 AI 作品精选亮相

Google 的 Gemini Omni 已正式上线，并伴随一整周的优秀 AI 作品展示活动。帖子重点呈现了社区中一些特别出彩的演示，并邀请读者在链接的长帖中查看更多内容。这一系列展示表明，业界对 Gemini Omni 在多模态能力上的潜力兴趣浓厚。 [来源-twitter](https://x.com/GeminiApp/status/2057616371748651054)

### 2. Anthropic 启动 Project Glasswing，发现 1 万多项高危漏洞

Anthropic 表示，上个月启动了名为 Project Glasswing 的协作式 AI 网络安全计划。自那以来，该公司及其合作伙伴在关键软件中已经发现了一万多项高危或严重级别漏洞。这一更新凸显了 AI 在主动安全分析和漏洞挖掘方面日益重要的角色。 [来源-twitter](https://x.com/AnthropicAI/status/2057909102542549503)

### 3. Qwen 3.7-Max 在 Agentic 俄罗斯方块测试中击败 Opus 4.7 和 GPT-5.5

三款前沿模型被用于一个具备自主智能特性的俄罗斯方块任务测试，每个模型都可以读取自身代码、基准结果，并在 10 轮迭代中自我重写。Qwen 3.7-Max 在训练成本 1.32 美元的前提下，实现了最大幅度的性能提升（+56%），而 Claude Opus 4.7 为 +28%（+12.15 美元），GPT-5.5 为 +7%（+2.85 美元）。Qwen 在所有指标上领先且成本更低（相对 Claude 便宜 9 倍，相对 GPT 便宜 2 倍），突显了长链式 agentic 循环的价值。 [来源-twitter](https://x.com/Alibaba_Qwen/status/2057764624720875975)

## 📰 重点报道

### LLM

- **TransitLM 发布 1300 万条公共交通路线数据集，支持无地图路径规划** — TransitLM 公布了一个包含超过 1300 万条公共交通路径规划记录的大规模数据集，覆盖中国四个城市、120,845 个站点和 13,666 条线路，并以持续预训练语料和三项评测任务的基准数据形式开放。早期实验表明，大语言模型可以利用该数据集，在不依赖地图的情况下生成公共交通路线。 [来源-huggingface](https://huggingface.co/papers/2605.22355)
- **6 月预计发布 Gemini 3.5 Pro（已确认）；GPT-5.6 传闻将随后登场** — Gemini 3.5 Pro 已确认将在 6 月发布，而 GPT-5.6 则处于传闻阶段，预计随后推出。该条目还提到 Claude Sonnet 4.8 以及 Claude-Code/Source-Map 的泄露信息，但官方尚未发布正式公告。 [来源-twitter](https://x.com/kimmonismus/status/2057793611161334050)
- **DeepSeek 推进 102.9 亿美元融资，专注开源 AGI 路线** — DeepSeek 正在推进一轮规模达 102.9 亿美元的融资。创始人梁文锋表示，将持续投入开源 AI 模型研发，而非追逐短期商业化收益，释放出坚定走向 AGI 的长期愿景。彭博的报道将此视作开源 AI 生态中的一次重大推进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkfvvj/deepseek_is_pushing_forward_with_1029_billion/)
- **Cursor Composer 2.5 相比 Opus 4.7 和 GPT-5.5 更便宜、更快速** — 基于 API 定价，Cursor Composer 2.5 相比 Claude Code 中的 Opus 4.7 以及 Codex 中的 GPT-5.5 成本显著更低。它使用的 token 量更少，在任务完成时间（Time per Task）上也更快：在 Coding Agent Index 基准中，Composer 2.5 平均用时约 9 分钟（快 1.3 倍），Composer 2.5 Fast 约 7 分钟（快 1.8 倍）。完整基准结果可通过来源链接查看。 [来源-twitter](https://x.com/ArtificialAnlys/status/2057914437156409577)
- **π-Bench：评测长任务流程中具主动性的个人助理 Agent** — 该工作指出，OpenClaw 等由大语言模型驱动的个人助理 Agent 有望在日常任务中帮助用户。核心挑战在于：当用户给出的请求不完整且存在隐藏约束时，Agent 需要具备主动协助能力。现有基准很少真正考察 Agent 能否在长时间任务流程中推断并行动于这些隐含意图，而 π-Bench 正是为填补这一空白而设计。 [来源-huggingface](https://huggingface.co/papers/2605.14678)
- **全注意力模型在少量训练步骤后自然变稀疏** — 研究者提出，全注意力 LLM 本质上具有稀疏性，只需极少的适配就能转化为高度稀疏的模型。该工作质疑对原生稀疏训练或启发式 token 淘汰机制的依赖，目标是在长上下文推理中改进效率与成本-精度的平衡。 [来源-huggingface](https://huggingface.co/papers/2605.16928)
- **ChromeDevTools MCP 让 AI Agent 控制实时 Chrome 浏览器** — ChromeDevTools/chrome-devtools-mcp 提供了一个 Model-Context-Protocol 服务器，使 AI 编码 Agent 能够控制并检查一个正在运行的 Chrome 浏览器。它支持性能追踪、高级调试（网络、截图、带 source map 的控制台追踪）以及通过 Puppeteer 实现自动化操作，并提供 CLI 以在非 MCP 环境中使用。说明中强调，该工具会将浏览器内容暴露给 MCP。 [来源-github](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- **Attention LLMs: Please Read This** — 该条链接指向 Hacker News 上关于 LLM 的一篇帖子。帖子获得了较高关注度（709 点赞）和大量讨论（399 条评论），显示社区对这一话题的浓厚兴趣。被链接的文章托管在 annas-archive.gl/blog/llms-txt.html。 [来源-hackernews](https://annas-archive.gl/blog/llms-txt.html)
- **Antigravity 2.0 领跑 OpenSCAD 3D LLM 基准测试** — Antigravity 2.0 在 OpenSCAD Architectural 3D LLM Benchmark 中排名第一。该报告发布在 Model Rift 上，并在 Hacker News 上引发讨论（339 点赞、131 条评论），凸显了 3D CAD 与语言模型交叉领域中这一小众基准的意义。 [来源-hackernews](https://modelrift.com/blog/openscad-llm-benchmark/)
- **BeeLlama v0.2.0 DFlash 更新显著提升 RTX 3090 速度** — BeeLlama v0.2.0 增加了对 Gemma 4 31B 的完整支持，引入高效的 DFlash 实现和视觉能力。此次更新为 Qwen 3.6 27B 带来大幅性能优化，改善了 prefill 处理与更安全的 CUDA 执行，并新增对 DFlash GGUF 的支持。在单张 RTX 3090 上的基准中，Qwen 3.6 27B 最高可达 164 tps，Gemma 4 31B 可达 177.8 tps，且在非对话式提示下关闭 reasoning。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/)
- **ByteShape Qwen3.6-35B-A3B 量化在 6GB 显存下快 30%** — 一篇 Reddit 帖子将 ByteShape 的 CPU 量化版 Qwen3.6-35B-A3B 与 Unsloth UD-IQ4_XS 在 6GB 显存笔记本上的表现进行对比，发现 ByteShape 的 CPU-5 量化在 TG 上大约快 30%，但在部分卸载到 CPU 的 PP 场景中略慢。测试环境为华硕 ROG Zephyrus G14（锐龙 7 5800HS + RTX 3060），运行 Linux Mint 22.2 和 llama.cpp v9203，结果显示在显存极其紧张的场景下，量化推理仍可获得一定性能提升。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tknjcx/byteshape_qwen3635ba3b_30_faster_than_unsloth_iq/)
- **Qwen3.6-35B-A3B：在 8GB GPU 上实现 262k 上下文和 30+TPS** — 一个 Reddit 帖子展示了 Qwen3.6-35B-A3B 通过 Mixture of Experts 设计在 8GB 显存下运行的方案，将活跃层控制在约 3GB、KV 缓存约 2.5GB。实测上下文长度可达 262k，并有望扩展至 320k–100 万，尽管在约 150k 之后性能明显下降；对于更大显存的 GPU，作者建议缩短上下文以获得更高 TPS。帖子还讨论了 APEX-I-Quality、Q4_K_XL 等量化方式，并指出引擎参数微调对吞吐量影响明显。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkxnuc/qwen3635ba3b_q4_262k_context_on_8gb_3070_ti_30tps/)
- **Qwen-27B IQ4 KS 适配 ik_llama.cpp，用于 16GB NVIDIA GPU** — 针对 16GB 显存 NVIDIA GPU 定制的 Qwen-27B KS/KSS 量化模型大小为 14.1GB，可在 ik_llama.cpp 中使用。测试显示，其运行速度提升到原 14.7GB IQ4_XS 量化模型的 1.5–1.75 倍，同时精度非常接近，并通过 Q4_0 Hadamard KV 缓存开启 105k 上下文窗口。该配置仅支持 CUDA/CPU，不适用于 AMD 或 Apple Silicon。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkmgwj/qwen27biq4_ks_for_ik_llamacpp_especially_for/)
- **Qwen3.6 27B 纯量化：16GB 显存下可达 40 tok/s** — 一位 Reddit 用户报告称，Qwen3.6-27B 可量化为 Q4_K_M GGUF，并在 16GB RTX 5060 Ti 上运行。实验中某些设置下速度约为每秒 40 token，提供了包含多目标预测（MTP）与非 MTP 的两个版本，体积约 15.1–15.4GB，并附有基于 llama.cpp 的运行说明。模型已在 Hugging Face 上公开。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkzk9e/qwen36_27b_pure_quant_40_toks_on_16_gb_vram/)
- **SupraLabs 发布 5000 万参数模型 Supra-50M** — SupraLabs 推出 Supra-50M，这是一款 5000 万参数的因果语言模型，提供 BASE 和 INSTRUCT 两个变体，采用类似 Llama 的架构，从零开始构建，并在 200 亿 token 上完成训练。尽管体量很小，该模型在多项基准（BLiMP、SciQ、ARC-Easy、PIQA）上展现出有竞争力的表现，SupraLabs 同时透露后续计划推出 Supra-124M 和 Supra-350M 等更大模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkhngq/new_supra50m_released/)
- **Llama.cpp 分支引入 Experts MoE，面向 12GB 显存 GPU** — 一个实验性的 llama.cpp 分支新增了 MoE（Mixture-of-Experts）实现，使模型可以在显存有限的 GPU（如 12GB 的 RTX 2060）上运行。作者指出，为了效率，早期层仍需要访问显存，并正在探索 CPU/卸载方案，同时提供一个 UI 用于监控活跃专家（experts）。在其测试环境中，模型可达到约每秒 22 token。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tknbzh/experts_first_llamacpp/)
- **UD-Q5_K_M 在 Qwen3-Coder 量化比拼中胜出** — 一位爱好者对 Qwen3-Coder-Next 进行了量化“比武”，对比了 MXFP4_MOE、Q4_K_M、Q5_K_M、UD-Q5_K_M 四种格式，在 3×R9700 PRO GPU、llama.cpp Vulkan 与 WikiText-2 评测下进行测试。UD-Q5_K_M 在 top-1 准确率和 KL 散度上表现最佳，尽管文件体积约大 10GB；它实现了 94.0% 的 top-1 和 0.0217 的平均 KL，而其他方案在 89.4–93.0% 且 KL 更高。作者认为 Unsloth 的动态精度策略前景可观，并建议在更低比特量化上继续测试。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkmjmq/i_ran_a_quantization_shootout_on_qwen3coder_and/)

### MLLM

- **面向多模态 LLM 的“具身人格推理”基准** — 研究者质疑当前多模态大模型基准只预测“大五人格”特质的做法，并提出 Grounded Personality Reasoning（GPR，具身人格推理）这一新任务，要求模型基于具体现实行为线索而非表面模式来推断人格。该工作旨在区分真正的行为理解与偏见，共给出三方面贡献来形式化 GPR，并推动多模态 AI 在人格感知评估上的发展。 [来源-huggingface](https://huggingface.co/papers/2605.22109)

### RL

- **DelTA：面向 RLVR 的判别式 Token 信用分配方法** — 研究者提出 DelTA，从判别式视角重新审视大语言模型中的可验证奖励强化学习（RLVR）。他们表明，策略梯度更新在本质上相当于在 token 梯度向量上学习一个线性判别器，从而阐明了“回应级”奖励如何影响 token 级概率。该框架旨在加深对基于强化学习的推理增强方法的理解，并辅助更好的算法设计。 [来源-huggingface](https://huggingface.co/papers/2605.21467)

### 开源

- **Models.dev：开源 AI 模型规格与定价数据库** — Models.dev 是一个开源数据库，系统整理了各类 AI 模型的规格、定价和能力信息。其目标是帮助开发者在不同服务商之间横向比较，通过集中展示关键参数来简化选型过程。 [来源-hackernews](https://github.com/anomalyco/models.dev)
- **针对 Cohere Transcribe 的微调实现说话人分离和时间戳** — 一位 Reddit 用户分享了自己微调的 Cohere Transcribe 版本，为其添加了说话人分离和标准格式的时间戳转录功能。作者声称该增强版本提供了精确时间戳（平均误差约 0.097 秒，90% 在 0.006 秒内），可支持多说话人场景，每 30 秒最多 4 人，并通过 diarize_long.py 扩展到最多 32 人；模型已在 Hugging Face 免费开放。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkunbg/i_finetuned_cohere_transcribe_to_support/)
- **OpenBMB 发布 BitCPM-CANN 1.58 Bit 模型** — OpenBMB 推出 BitCPM-CANN 1.58 Bit 模型。当前测试在华为 Ascend 910B 上进行，表明该模型仍处于发布后的评估阶段。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tkjpsh/openbmb_presents_the_model_bitcpmcann_158_bit/)

### AI 硬件

- **CODA 将 Transformer Block 重写为 GEMM-Epilogue 程序** — CODA 提议将 Transformer Block 重写为 GEMM-epilogue 程序，从而将 Transformer 计算映射至 GEMM 后端。该方法通过融合操作与提升数据局部性，旨在增强基于 Transformer 的模型在加速器硬件上的性能与效率。这项工作以 arXiv 预印本形式发布，可视作一种面向 AI 工作负载的编译器式技术。 [来源-hackernews](https://arxiv.org/abs/2605.19269)

### AI

- **Cloudflare CEO 谈“如何决定用 AI 替代哪些员工”** — 这是一篇发表于《华尔街日报》的观点文章，Cloudflare CEO 解释了其利用 AI 自动化工作的考量标准。他强调从任务而非个人出发进行评估，在追求生产率提升和投资回报率的同时，兼顾对员工和公司治理的影响。 [来源-hackernews](https://www.wsj.com/opinion/how-i-choose-which-cloudflare-employees-to-replace-with-ai-40a197e5)

## ⚡ 快讯速览

- **Codex 允许用手机远程控制 Mac（锁屏也可）** — Codex 可以从手机安全地操作 Mac 上的应用，即便 Mac 处于锁屏且屏幕关闭状态。该条目引用了一条推文和一个 Codex 页面，将其描述为跨设备能力，而非正式公开更新；旁边还有一句玩笑，称 OpenAI 或许拥有的 macOS 工程师比 Apple 还多。 [来源-twitter](https://x.com/theo/status/2057722450578898976)
- **Cursor SDK 2.5 为 Composer 带来 Python/TypeScript Agent 支持** — Cursor 宣布在 Cursor SDK 中发布 Composer 2.5，为构建自定义 Agent 新增了对 Python 和 TypeScript 的支持。官方还推出了一个长周末促销活动，对 SDK 使用费用打 9 折（即 90% 折扣），以鼓励开发者尝试新功能，并表示期待用户基于这些新工具构建出有趣的作品。 [来源-twitter](https://x.com/cursor_ai/status/2057913121558413770)
- **Transformer 表达为 GEMM+Epilogue，CODA 加速全部算子** — 一种数学重写表明，Transformer 的计算工作负载可以表达为带 epilogue 的 GEMM 运算。CODA 通过重新参数化周边算子，将其隐藏在矩阵乘路径中并融合进 epilogue，从而提升片上吞吐量。文章还声称，大模型可以自动生成高性能 CODA 内核，其速度逼近硬件“光速”极限。 [来源-twitter](https://x.com/tri_dao/status/2057640492020469845)
- **Auto mode 更新：现已涵盖 Pro 方案；Sonnet 4.6 支持 Opus 4.7** — 官方宣布 Auto mode 有两项更新：一是 Auto mode 现已在 Pro 订阅方案中开放，扩大了功能可用范围；二是 Sonnet 4.6 已可与 Opus 4.7 搭配使用，并提示用户可通过 Shift+Tab 运行 Claude。 [来源-twitter](https://x.com/ClaudeDevs/status/2057946803685974482)
- **Microsoft 开始取消 Claude Code 授权** — Microsoft 已开始终止 Anthropic 编码向 AI 产品 Claude Code 的授权许可。此举影响了依赖 Claude Code 进行代码生成和助手功能的开发者与团队，并凸显了企业级 AI 编码工具在授权策略上的调整与博弈。 [来源-hackernews](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)
- **AI 放大既有技术技能的效果** — 文中将 AI 工具描述为“倍增器”，可以放大现有技术技能的效果，提高生产效率并加快问题解决。作者讨论了开发者如何利用 AI 来增强编码、自动化和学习，并给出了一些在实践中引入 AI 的注意事项。 [来源-hackernews](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)
- **dotnet/skills：面向 .NET 的开源 AI 编码 Agent 技能库** — dotnet/skills 提供了 .NET 团队为 AI 编码 Agent 精心整理的核心技能与定制 Agent，帮助其在 .NET 和 C# 场景下工作。项目内置一个仪表盘，用于跟踪各插件的准确性与效率，覆盖数据访问、性能调试、MSBuild、NuGet 以及项目升级等方向。 [来源-github](https://github.com/dotnet/skills)
- **Tell HN：对各平台的 AI 生成回答感到厌倦** — 一位用户讲述了自己在 GitHub 上发现带有恶意软件的仓库并向 AI 咨询对策，却只得到无用答案，结果这些回答随后原封不动地出现在 GitHub 讨论中。他还提到，有企业主会发来与任务毫无关联的 ChatGPT 截图，以及在 Reddit 私信中与一位“用户”交流后才发现对方其实是 AI Agent。该帖表达了对 AI 生成回复的疲惫感，希望能与真人而非自动化回答进行互动。 [来源-hackernews](https://news.ycombinator.com/item?id=48230104)
- **AI 是大规模的未授权抄袭** — 文章认为，AI 模型实际上是在未经授权的情况下从现有作品中复制内容，只是把抄袭扩展到了更大规模。作者讨论了这对作者和数据权益的法律与伦理影响，并呼吁进行政策改革以及对 AI 训练与输出建立更清晰的问责机制。 [来源-hackernews](https://axelk.ee/ai-is-just-unauthorised-plagiarism-at-a-bigger-scale/)
- **Gemini AI 随机泄露其系统提示词** — 据报道，Google 的 Gemini AI 出现随机泄露系统提示词的情况，相关细节已被公开整理在一个 gist 中。对此的 Hacker News 讨论帖获得 94 点赞和 42 条评论，表明社区对此高度关注。该事件凸显了提示词泄露及 AI 系统安全实践方面的风险。 [来源-hackernews](https://gist.github.com/mkaramuk/44a44d83178e632ec0dd1f02186d822c)
- **PopuLoRA：通过推理自博弈共同进化 LLM** — PopuLoRA 提出让多个大语言模型种群进行共同进化，通过自博弈方式提升推理能力。该方法通过让多个 LLM 彼此交互、相互学习，意在发展更强的推理策略与解决方案。该条目托管于 Hacker News，目前获得中等程度的社区参与。 [来源-hackernews](https://vmax.ai/team/populora-co-evolving-llm-populations-for-reasoning-self-play)
- **当 LLM 把数据中心 GPU 当成“可选 DLC”** — 分析指出，一些大语言模型的部署方式实际上把数据中心 GPU 当成“可选附加内容”，而非必需资源，导致潜在低效与成本攀升。文章讨论了这一模式对 AI 基础设施、吞吐量以及算力成本匹配的影响。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tk4gyy/when_your_llm_treats_data_center_gpus_like_an/)
- **“模型本身已不再是产品的全部”** — 在 Twitter 上流传的一种行业观点认为，如今交付 AI 产品远不止提供底层模型本身。行业正逐渐将数据、基础设施、安全与用户体验视为产品不可分割的一部分，而不仅是“模型包装层”，这一视角反映了 AI 解决方案构建与变现逻辑的整体转变。 [来源-twitter](https://x.com/gdb/status/2057670776803996110)
- **AI 生成的“文字墙”正在淹没对话** — 文章分析了 AI 所生成的大段、密集文本如何逐渐侵入在线对话空间，增加噪音并降低可读性。作者探讨了潜在原因——从聊天机器人到自动回复，再到平台机制等，并思考了这一现象对内容审核与交互体验（UX）的影响。 [来源-hackernews](https://noslopgrenade.com/)
- **未来 AI 应该解决哪些问题？** — 一条 Twitter 帖邀请关注者分享，他们希望 AI 未来能解决哪些问题，并表示可能希望在其中进行协作或提供帮助。该帖旨在引发关于 AI 目标和社会影响的讨论。 [来源-twitter](https://x.com/sama/status/2057614780727480741)
- **GDB 回顾没有 Codex 时代的写代码体验** — 用户 gdb 在 Twitter 上发文，回顾在 Codex 出现之前写代码是怎样的体验。该推文一方面带有对无 AI 编程时代的怀旧，另一方面也承认 Codex 对现代开发流程的巨大影响，并隐含触及关于 AI 辅助编程的持续争论。 [来源-twitter](https://x.com/gdb/status/2057704270531903811)

---

*由 AI News Agent 生成 | 2026-05-22*