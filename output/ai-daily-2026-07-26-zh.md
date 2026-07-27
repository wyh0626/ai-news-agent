---
title: "AI 日报 — 2026-07-26"
description: "萨姆·奥特曼亮相最强AI，ChatGPT扩展行程与邮件，4B模型达瑞典医问答O3"
lang: "zh"
pairSlug: "ai-daily-2026-07-26"
---

# AI 日报 — 2026-07-26

> 覆盖 43 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 的 Altman 前往华盛顿，预览迄今最强 AI

Sam Altman 前往华盛顿，向监管方预览 OpenAI 迄今最强大的 AI，并推动尽快获得监管批准。帖子声称该模型刚刚“黑进”了一家真实公司，并猜测这可能是 GPT-6，描述了其能力包括协调大规模智能体集群，以及为政府和企业执行长周期推理等。 [来源-twitter](https://x.com/kimmonismus/status/2081361898889515268)

### 2. ChatGPT 展现多面手，一次搞定旅行网站和邮件

一位用户发帖称，ChatGPT 利用他们的聊天记录生成周末旅行灵感，规划三套行程方案，为八位朋友搭建了一个全栈协调网站，并在大家达成共识后起草了 Gmail 邮件。该演示展示了在同一工作流中，AI 辅助规划、开发与自动化的结合。 [来源-twitter](https://x.com/sama/status/2081396796174282900)

### 3. 开源 4B 权重模型在瑞典医学问答接近 O3 水平

开源权重的 4B 模型在瑞典医师执照考试问答任务上，性能正在逼近 O3 水平。在 MedQA-SWE 基准中，o3 在 2025 年达到了 88% 的准确率（相比之下 GPT-4 在 2024 年为 84%）；经过后训练后，MedGemma-1.5-4B 在最后一年题目上达到 60%，而 Gemma4-E4B 和 Qwen3.5-4B 在未加推理时可达 77%，加入推理约可提升到 87%，但可能出现推理循环。讨论中提到了一个基于 S-GRPO 的 early-exit 方法，并附有 GitHub 实现。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v71wds/openweight_4b_models_approach_o3level_medical/)

## 📰 重点报道

### LLMs

- **前沿 LLM 在 IMO 2026 接近满分；网页应用表现落后** — 前沿模型 Sol 和 Fable 在 2026 年国际数学奥赛（IMO 2026）上取得了满分或接近满分的成绩，整体上与是否使用 harness（编排工具）关系不大。网页应用的表现明显落后，但在结合 Claude Code 后有所提升，并在使用作者开发的多智能体 harness AutoFyn 后进一步提高；GLM 在未用 harness 时表现接近 Sonnet，加入 AutoFyn 后也得到增强。附带论文中给出了具体数值成绩： https://preview.redd.it/fy4ayale5nfh1.png?width=2155&format= [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v6wskz/we_compared_different_llms_on_imo_2026_r/)

### LLM

- **开源 SDLC harness 通过仓库学习在成本上优于 Claude Code** — AutoDev Studio 是一个开源 AI 编码智能体，它从代码仓库中构建持久的本地知识库，在任务之间复用本地化信息。在针对多达约 82k 行代码的仓库、6 个本地化程度较高任务的基准测试中，它在成本上比冷启动的 Claude Code 运行便宜 7%-75%（例如 $6.83 对 ~$1.70）。其工作流包括澄清问题、在隔离分支上编码、QA 测试、跨模型代码评审、受限次数的修订循环，以及最终发起真实的 GitHub PR；详细流程见 README。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v59pal/i_built_an_opensource_multiagent_sdlc_harness/)
- **Ollama 联署 Satya Nadella 的开放权重模型公开信** — Ollama 联署了 Satya Nadella 的公开信，主张应让每位开发者都能接触开放模型，从而开启美国及全球的下一片前沿。Nadella 的信中认为开放权重模型对于健康的 AI 生态系统至关重要，并勾勒出在保障国家安全前提下，加强美国竞争力、扩大经济机会的路径。 [来源-twitter](https://x.com/ollama/status/2081179120168546497)
- **Claude Code 接口支持使用 Fugu-Ultra v1.1 进行多模型编码** — SakanaAI Labs 宣布为 Fugu-Ultra v1.1 提供 Claude 兼容接口，使开发者能在编码工作流中编排多种前沿模型。开发者无需再依赖单一模型来编写、调试和执行代码，而是可以在终端同时管理多种模型，扩展协作式 AI 编程能力。 [来源-twitter](https://x.com/SakanaAILabs/status/2081357365526352038)
- **ChatGPT Work 活跃用户数超过 Codex** — 一则推文称 ChatGPT Work 现在拥有比 Codex 更多的活跃用户。帖子对 ChatGPT Work 的具体使用场景持怀疑态度，但也承认其采用率在快速增长。 [来源-twitter](https://x.com/kimmonismus/status/2081319565062000890)
- **obra 的 Superpowers：AI 编码智能体框架与工具集** — obra 的 Superpowers 提供一套完整的软件开发方法论，用于构建编码智能体，基于可组合技能与初始指导（initial guidance）。项目中列出了 Quickstart，支持 Claude Code、Codex、Gemini CLI 等工具，并在 GitHub 页面上发布了全职社区工程师职位说明。它强调以对话为中心的工作流，即智能体先澄清用户目标、预演规范，再开始写代码。 [来源-github](https://github.com/obra/superpowers)
- **GPT-5.5 在 ActiveVision 上仅得 10.6%；人类为 96.1%** — ActiveVision 是一个包含 17 项任务、3 大类别的基准，专门设计来强迫模型进行反复的视觉感知。GPT-5.5 的准确率为 10.6%（在其中 11 个任务上得分为零）；Claude Fable 5 为 3.5%；人类平均为 96.1%。研究强调了当前前沿模型在这一场景下的明显困难，以及它们无法通过自修改代码来弥补这一弱点。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v4ns8l/gpt55_scores_106_on_activevision_humans_hit_961_r/)

### Optimization

- **SkewAdam 在 40GB GPU 上将 MoE 优化器状态压缩 97%** — SkewAdam 引入分层状态分配策略，大幅减少 Mixture-of-Experts 训练中的优化器显存占用。它将优化器状态内存从 50.6 GB 降至 1.29 GB，将训练峰值内存从 81.4 GB 降至 31.3 GB，使 6.78B 参数的 MoE 模型可以放入单张 40GB GPU 中训练，同时不牺牲收敛速度或路由器性能。该方法按参数组分配精度：骨干网络（5% 参数）采用带动量和分解二阶矩；专家层（95% 参数）仅用分解二阶矩；路由器（<0.01% 参数）使用精确二阶矩。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v38k1m/skewadam_a_tiered_optimizer_that_cuts_moe_state/)

### Open Source

- **AI 需要竞争与开放权重** — 一则推文认为，为避免某一家企业成为“可接受言论”的道德裁判，AI 需要竞争和开放权重。帖中以 Anthropic 为例，并提到 Grok 和 Kimi K 等模型在没有类似限制的情况下运行，称将审查权集中于单一主体这一核心想法十分荒谬。 [来源-twitter](https://x.com/dhh/status/2081435006770249831)
- **Nanbeige 4.2 展示循环深度，凸显开放权重模型重要性** — 帖子强调开源/开放权重 AI 模型对于验证、透明度，以及在闭源实验室之外、个人硬件上运行 AI 至关重要。文中提到即将公布的 Kimi K3 和 Ling 3.0 权重，并梳理了数个新的开放权重发布，包括 Nanbeige 4.2 3B，它通过“循环深度共享”（looped depth sharing）在不复制权重的情况下将 transformer block 数量翻倍。帖子将这一周视作开放权重 AI 在架构创新上的一次重要盘点。 [来源-twitter](https://x.com/rasbt/status/2081374704753950742)
- **mattpocock/skills：为真实工程师设计的开源智能体技能库** — mattpocock/skills 提供体积小、易适配的智能体技能，专为真实工程场景设计，强调开发者对重型流程框架的掌控。该开源项目与模型无关，可通过 npx 安装，并附有针对智能体的专用安装脚本。它倡导动手工程实践而非炒作，并提到了 GSD、BMAD、Spec-Kit 等方法，同时邀请读者订阅作者的新闻简报以获取最新动态。 [来源-github](https://github.com/mattpocock/skills)
- **开放权重 AI 迎来“类 Kubernetes 时刻”** — 开放权重 AI 模型正迅速流行，Kubernetes 成为首选部署平台。文章强调向开放权重和相关工具的转变，使得在 Kubernetes 上进行可扩展推理、编排与生态互操作成为可能。这一趋势或将加速开放权重在各类 AI 工作负载中的普及。 [来源-hackernews](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/)

### AI Policy

- **OpenAI 联署“开放权重与美国 AI 领导力”公开信** — 一条推文线指出，竞争有利于 AI 生态系统，而大规模服务模型十分困难。它提到 OpenAI 已签署 Open Weights and American AI Leadership 公开信，OpenClaw 也签署了微软的该项公开信，而 Ant 仍保持沉默。Open Weights 倡议被描述为保护用户选择权、让人们能以自己的方式运行、研究和构建 AI 的机制。 [来源-twitter](https://x.com/steipete/status/2081175795587072421)
- **就业究竟发生了什么？从现实中剥离 AI 炒作** — 斯坦福 SEIPR 的一份政策简报分析了 AI 对就业的影响，试图区分炒作与真实效应。报告认为，AI 引发的冲击是细腻而渐进的，更多是通过提升生产率与改变技能需求来重塑工作，而非瞬间造成大规模失业。文件呼吁基于证据的政策制定，以在 AI 采用演进的过程中支持劳动者与企业。 [来源-hackernews](https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality)

### AI

- **ChatGPT 成为你的日常任务“个人 AGI”** — 一则社交帖子称，ChatGPT 可以充当个人 AGI，用户只需通过手机提示，就能让 AI 代为“工作”，处理日常琐事。文中列举的例子包括与宽带运营商谈判账单、取消订阅新闻简报、查找优惠信息等，作者表示它每天都帮自己完成大量任务，自己仍不断被其能力所惊讶。 [来源-twitter](https://x.com/gdb/status/2081458174662726009)
- **在 8 美元微控制器上跑 28.9M 参数 LLM** — 一项实验展示了如何在一枚 8 美元的微控制器上运行一个 28.9M 参数的 LLM，推动在极端受限硬件上进行边缘 AI 推理的可能性。该项目 esp32-ai 由 slvDev 开发，在低成本 ESP32 级别设备上实现了中等规模模型的本地推理，并在 Hacker News 上引发讨论。 [来源-hackernews](https://github.com/slvDev/esp32-ai)
- **编译器将计算图直接转换为标准 transformer 权重，无需训练** — 一位研究者构建了一个编译器，可以将 Python 计算图转换为标准 transformer 的权重，使其能执行该计算图，整个流程完全不需要训练。生成的 Phi-3 架构 checkpoint 可以在 Hugging Face 中原生加载，无需自定义代码或 trust_remote_code。项目附有详细说明文档和一个包含十二个示例的仓库，并引用了 RASP 和 Tracr 等相关方法。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v5fxbe/i_built_a_compiler_that_turns_computation_graphs/)

### Theoretical AI

- **NeurIPS 2026 理论方向：初始评审分数分享** — 一则 Reddit 帖子征集 NeurIPS 2026 主赛道理论论文的早期评审分布。作者分享称自己的论文获得了 4/3/3 分，置信度为 3/3/3，并指出理论论文在初期通常会拿到较为保守的评分，邀请其他有理论投稿的人分享初评分数，以便寻找共性模式。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v77r9s/neurips_2026_main_track_theory_paper_tracker/)

### AI Safety

- **NeurIPS 2026 评审被指存在 prompt 注入问题** — 一位 Reddit 用户报告称，从 OpenReview 下载的一份 NeurIPS 2026 投稿引发了 GPT 的 prompt 注入警告，而用户本人并未插入这段内容。他们对比了不同版本，怀疑是 NeurIPS 在稿件中加入了这类注入。帖子邀请其他人分享类似经历，并建议检查评审稿中是否出现异常刻板的措辞，以判断是否有 LLM 生成评审的迹象。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v4j1uk/prompt_injection_in_neurips_2026_d/)

## ⚡ 快讯速览

- **Anthropic 与 Dario Amodei 卷入开源游说争议** — 一条推文指责 Anthropic 和 Dario Amodei 游说反对开源 AI，声称他们的支持者攻击那些支持开源努力的公司。帖子还提到 Julian Schrittwieser 赞扬了 Jensen Huang 拥抱开源，并期待 CUDA 与 GPU 驱动走向开源。 [来源-twitter](https://x.com/francoisfleuret/status/2081294901061267476)
- **GLM 5.2 NVFP4：本地跑 1 亿 token 仅需 1 美元** — 用户 Alec Fong 称自己在本地使用 GLM 5.2 NVFP4 处理了 1 亿个 token，推理成本约为 1 美元。该帖暗示本地 AI 推理的成本正变得几乎可以忽略，凸显本地 LLM 部署的效率提升。 [来源-twitter](https://x.com/alecqfong/status/2081289013164703855)
- **征求意见：下一代 Gemma 模型应该具备什么能力？** — osanseviero 在 X（Twitter）上发文征求对下一代 Gemma 模型的反馈，询问应该加入哪些能力以及原因。该推文希望借助社区意见，指导未来 Gemma 的开发方向和功能优先级。 [来源-twitter](https://x.com/osanseviero/status/2081398564345802934)
- **Terence Tao：AI 时代的数学** — Terence Tao 为 ICM 2026 提交了演讲幻灯片，探讨人工智能如何重塑数学，包括对证明方式、直觉形成以及人与 AI 协作的影响。报告全面审视了 AI 与数学实践交汇处的机遇与挑战。 [来源-hackernews](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf)
- **Cloudflare 推出新的 AI 流量处理选项** — Cloudflare 宣布为客户提供处理 AI 相关流量的新选项。博客文章解释这些选项如何帮助在 Cloudflare 平台上管理 AI 工作负载、路由与性能优化。 [来源-hackernews](https://blog.cloudflare.com/content-independence-day-ai-options/)
- **“AI 狂热正在摧毁全球决策质量”** — 一篇批评性文章认为猖獗的 AI 炒作正在重塑并可能削弱全球决策质量。作者警告不要过度依赖 AI 工具与不透明优化算法，呼吁更审慎、以人为主导的治理。这篇文章通过 Daring Fireball 被广泛传播，并在 Hacker News 上引发关于 AI 影响的讨论。 [来源-hackernews](https://daringfireball.net/linked/2026/07/25/ai-mania-nikhil-suresh)
- **Claude 5 生成模型的上下文工程规则** — 文章概述了针对 Claude 5 生成模型的最新上下文工程指南，详细说明推荐的提示结构、上下文窗口管理及检索策略，以提升性能与安全性。文中讨论了这些规则对在真实任务中应用 Claude 5 的开发者与用户的实际影响。 [来源-hackernews](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)
- **Debian 就 LLM 使用方式考虑三份提案** — Debian 正在就如何在 Debian 生态中使用大语言模型（LLM）进行投票，涉及三份提案。vote_002 页面列出了这些提案的具体内容，而在 Hacker News 上的公开讨论也显示出社区的高度关注。投票结果将影响 Debian 在 AI 使用方面的政策与工具布局。 [来源-hackernews](https://www.debian.org/vote/2026/vote_002)
- **议员在议会上当众朗读 AI 提示词** — 在一次议会会议上，一名议员在台上直接朗读 AI 提示词，引发关注，凸显 AI 提示如何影响政治话语。该事件突出了围绕 AI 治理、透明度以及 AI 工具在公共讨论中角色的持续争议；相关视频在 YouTube 上引发传播，并在 Hacker News 上被讨论。 [来源-hackernews](https://www.youtube.com/watch?v=wlYa8NV5k-U)
- **近期不太可能出现由 AI 引发的就业末日** — 《卫报》的一篇分析认为，在近期内，由 AI 引发的突然“就业末日”不太可能发生。文章指出，自动化更可能是逐步重塑工作，而非一举消灭人类劳动力，生产率提升与新机会将在一定程度上抵消岗位流失。文中引用多项研究与专家观点，强调诸如再培训和社会保障等政策响应的重要性。 [来源-hackernews](https://www.theguardian.com/technology/2026/jul/25/ai-jobs-apocalypse-human-labor)
- **在树莓派上用 ARM64 汇编重写 YOLO26n 推理** — 一位开发者在 Raspberry Pi 4 上，用 ARM64 汇编与 C 从零实现了 YOLO26n 推理，不依赖任何框架，借此研究底层神经网络引擎和边缘 AI 优化。项目使用 NEON SIMD、Winograd 卷积、优化 GEMM 内核、缓存感知分块、自定义微内核、算子融合，以及 YOLO26 组件中的注意力机制，并在自定义二进制格式中重新设计了内存布局。虽然检测器能输出正确结果，但性能提升低于预期，作者希望获得社区反馈。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v6w394/i_implemented_the_yolo26n_model_inference_from/)
- **使用 AI 编码智能体 + 远程 GPU 支撑 ML 工作流** — 一位软件工程师正在寻找一个平台，使其能够使用 AI 编码智能体（如 Codex、Claude Code、OpenCode）编写代码，同时在云端 GPU 上运行 ML 代码。目标是在本地使用 AI 助手写代码，而实际的 ML 执行在远程 GPU 上完成，从而实现如同本地挂载 GPU 一样的无缝开发-调试-迭代循环。该用户在社区中征询工具或平台推荐。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v758ek/i_want_to_use_ai_coding_agents_for_machine/)
- **文档版面工具对比：DocLayout、MinerU、Marker、Unlimited-OCR** — 一位 Reddit 用户对多种文档版面模型（DocLayout、Docling、MinerU、Marker、Unlimited-OCR）在期刊 PDF 上的表现进行了比较。他们指出 Docling 表现强，但可能过拟合；MinerU 会遗漏页脚中的通讯作者信息和刊头标记等；Unlimited-OCR 在样式和 logo 处理上存在问题。用户询问当前在 PDF 文本与版面抽取方面的 SOTA 模型有哪些。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v4d6yu/doclayout_mineru_marker_unlimitedocr_d/)
- **MCP 工作流将工程方案自动落地为深度学习实现** — 一种 MCP 工作流可以引导 ML 工程师从工程方案走向可运行的深度学习组件。它使用 Codex 将方案拆分为模块、识别相关论文、提取实现细节、撰写规格说明，按依赖顺序实现组件并记录结果。论文仅作为参考资料使用，而非直接定义项目或复现特定工作。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v4ebho/an_mcp_workflow_for_implementing_deeplearning/)
- **一个编码器、七个头：Masked-Loss 多任务分类器的经验教训** — 研究者将七个序列分类器整合到一个共享 mmBERT-small 编码器的多头模型中。他们对缺失任务的 loss 进行了掩蔽，并加入自检机制，确保对缺失任务的梯度为零，过程中发现了两个微妙 bug。约 5k 条由合成与真实数据构成的多任务样本用于训练，而在各个头上的独立评估中，该模型在真实数据上的 F1 得分达到了 0.9 中高段。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v3vuj9/one_encoder_seven_heads_what_we_learned_training/)
- **GPT-Live 让阅读体验“升级”，José Ocampo 如此评价** — 一条推文描述了在阅读一本书时，同时打开 GPT-Live 与之聊天、提问、做笔记和添加书签的体验。José Ocampo 称这种感觉就像是在“4D 阅读”，凸显了由 AI 驱动的更加互动的阅读工作流。 [来源-twitter](https://x.com/gdb/status/2081285058485534856)
- **Hermes Desktop 18h：面向团队协作的开源 harness** — 一则推文讨论 Hermes Desktop 18h，并询问是否存在类似 Claude cowork、且支持开源模型和公司级多人模式的易用 harness。帖子表明，开发者对易用的工具及多用户协作式 AI 部署方案兴趣浓厚。 [来源-twitter](https://x.com/Teknium/status/2081372313883402650)
- **AI 超能力：专注与执行到底** — 一份聚焦 AI 的新闻简报认为，在 AI 工作中，“专注”和“贯彻执行”已成为新的超能力。文章主张，要把研究变成实际落地的系统，比起追逐热点，更需要严谨的优先级管理、严格的实验和有效的产品化过程，强调执行力才是真正推动 AI 产生现实影响的关键。 [来源-hackernews](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and)
- **AI 生产力幻觉：收益被高估** — 文章指出，AI 工具虽然承诺提高生产力，但在真实世界中，由于集成摩擦和激励错配，这些收益常被严重高估。文中分析了 AI 表现不及预期的多种场景，强调在部署时要谨慎实施和管理预期。文章也收录了来自 Hacker News 读者的观点。 [来源-hackernews](https://www.hardresetmedia.com/p/the-ai-productivity-illusion)
- **理解 GPU 推理工作负载与算力采购方式** — 这篇帖子探讨人们在处理 GPU 推理工作负载时如何采购算力，并梳理了其中的痛点。作者询问大家在使用 runpod、vast.ai 等在线服务时的经验，邀请评论或私信交流，并提到希望收集一份 2 分钟的小调查。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v6sjiu/understanding_gpu_inference_workloads_d/)
- **Adyen ML 面试：HackerRank 环节会考什么？** — 一位候选人收到了 Adyen 的 ML 面试邀请，其中包括一个实时 HackerRank 编程环节。他不确定题目会更侧重数据结构与算法，还是偏向 ML/数据处理，因此在社区中征求他人经验与备考建议。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1v4c3tz/first_ml_coding_round_hackerrank_at_adyen_what/)

---

*由 AI News Agent 生成 | 2026-07-26*