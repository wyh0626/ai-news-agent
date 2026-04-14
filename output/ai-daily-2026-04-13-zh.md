---
title: "AI 日报 — 2026-04-13"
description: "DeepMind雇哲学家研机器意识，Open5B转Markdown论文推LLM。"
lang: "zh"
pairSlug: "ai-daily-2026-04-13"
---

# AI 日报 — 2026-04-13

> 覆盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. Google DeepMind 聘用哲学家研究机器意识

一位研究者宣布，他们已被 Google DeepMind 招募，将在 5 月起担任新的哲学家职位，重点研究机器意识、人类与 AI 关系以及 AGI 准备度。他们将继续在剑桥大学进行兼职研究与教学工作。[来源-twitter](https://x.com/dioscuri/status/2043661976534950323)

### 2. 使用开源 5B 模型将 2.7 万篇 arXiv 论文 OCR 转为 Markdown

一个开源 50 亿参数模型被用于对 27,000 篇 arXiv 论文进行 OCR 并转换为 Markdown，使用 NVIDIA L40S GPU、挂载云桶、在 Hugging Face 上并行跑 16 个作业完成处理。该项目花费 850 美元，大约耗时 29 小时，且零崩溃。生成的能力为 HF 在 hf.co/papers 上的 “Chat with your paper” 功能提供支持。[来源-twitter](https://x.com/ClementDelangue/status/2043779449322160270)

### 3. 2026 年 4 月本地 LLM 榜：Qwen3.5、Gemma4、GLM-5.1

Reddit 的 Best Local LLMs 大帖重点介绍了 Qwen3.5 和 Gemma4 等新版本，同时提到 GLM-5.1 声称达到 SOTA 性能，以及被称为“家用 Sonnet”的易用模型 Minimax-M2.7，还有实际可用的 PrismML Bonsai 1-bit 模型。帖子号召社区给出包含部署细节的深度对比，聚焦开源权重 LLM 在使用规模、工具、提示词和用户偏好上的差异。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sknx6n/best_local_llms_apr_2026/)

## 📰 重点报道

### AI

- **Google 开源 Magika：AI 驱动的文件类型检测工具** — Google 构建了 Magika，一款利用 AI 检测真实文件内容类型的工具。它已在 Gmail、Google Drive 和 Safe Browsing 等内部系统中广泛使用，每周处理数千亿个文件。该项目已在 GitHub 上以 google/magika 开源，号称支持 200+ 种内容类型，准确率 99%，单文件推理约 5 毫秒，训练数据量达 1 亿个文件。[来源-twitter](https://x.com/_vmlops/status/2043624154646409708)
- **GLM-5.1 vs Claude Code：开源赛车 AI 演示对比** — 一条 AI 主题推文通过一个 Three.js 赛车游戏对 GLM-5.1 和 Claude Code（Opus 4.6）进行对比，用于评估 AI 编码能力。演示展示了“一次成型”的带漂移汽车物理、531 行代码实现的赛车 AI（含四种人格），以及可自我迭代的调试工具，其中包括 20 多个 Bun.WebView 工具用来控制赛车和读取游戏状态。帖子称赞这一开源演示，并预测它将被广泛讨论。[来源-twitter](https://x.com/victormustar/status/2043595533919359033)

### LLM

- **未审查版 Gemma-4 26B 发布，号称全面碾压常规 Gemma-4** — 新的未审查版 Gemma-4 26B 模型 SuperGemma4-26B-Uncensored GGUF v2 已发布，并在 HuggingFace 上趋势上榜。据称该版本几乎不会拒答，工具调用表现也更好，自称性能优于标准版 Gemma-4 26B。此发布突显了开源 LLM 领域的持续竞争，以及围绕“去审查化”的社区争论。[来源-twitter](https://x.com/i/status/2043710372176122085)
- **Open Agents：能自写代码的开源云端编码 Agent** — 在启动项目 3 个月后，作者构建了一个云端编码 Agent，它为作者所有上线的代码都“包办”了每一行，包括它自身的代码。他们已将该项目以 Open Agents 之名开源。此发布体现了自主编码 Agent 与 AI 辅助软件开发方面的持续进展。[来源-twitter](https://x.com/nicoalbanese10/status/2043745569278251112)
- **从零训练 125M 语言模型，开源权重与 SFT 框架** — 作者从零训练了一个 12 层、1.25 亿参数的因果语言模型，使用自定义的 16k BPE tokenizer，在大约 9.2 万步后，在 WikiText-103 上达到约 6.19 的验证困惑度。基于 DailyDialog 使用 LoRA 做了对话版微调，并在 HuggingFace 上同时发布 base 与 instruct 两个 checkpoint，还提供了一个 SFT 框架，方便他人微调自己的变体。该工作强调的是开源实验性探索，而非与 10 亿参数以上模型直接竞争。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1skp6y6/trained_a_125m_lm_from_scratch_instead_of/)
- **本地 Minimax M2.7 演示类 GTA 三维网页体验** — 本地部署的 Minimax M2.7 展示了在单个网页中实现类似 GTA 的 3D 体验。作者将 Minimax 与 GLM 5 做对比，认为 Minimax 的画面更美观，并能添加树木和“群体智能”小鸟（boids）。测试在 OpenWebUI artifacts 和 OpenCode 中进行，使用 IQ2_XXS 量化以追求速度，作者表示尽管操作手感有些怪异，但整体行为仍较为连贯。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sk70ph/local_minimax_m27_gta_benchmark/)
- **Apple Silicon 上开源 DFlash 推测解码，最高 4 倍提速** — DFlash 的原生 MLX 实现已开源，并采用了更新的基准测试方法。一个小型草稿模型通过 block diffusion 并行生成 16 个 token，而目标模型用一次前向计算来验证每个输出 token。在 Apple Silicon（M5 Max，64GB）上使用 MLX 0.31.1 的测试结果显示，对多种 Qwen3.5 变体可实现大约 4 倍的速度提升，完整结果已在仓库中公布。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1skesyq/dflash_speculative_decoding_on_apple_silicon_41x/)
- **批评：MiniMax-M2.7-GGUF 在 UD-Q4_K_XL 量化中损坏** — 一则 Reddit 帖子指责 unsloth 等团队在缺乏充分测试的情况下匆忙发布新模型。作者声称，MiniMax-M2.7-GGUF 在 UD-Q4_K_XL 量化下，困惑度（PPL）测量出现 NaN 等异常，而类似量化配置下的 aessedai 和 ubergarm 模型 reportedly 没有此类问题。发帖者认为问题不在后端算子或 CUDA 13.2，并强烈建议避免使用这种量化版本。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sk6l63/unsloth_minimaxm27gguf_in_broken_udq4_k_xl_avoid/)

### Multimodal

- **WildDet3D：将可提示的 3D 检测扩展到真实复杂环境** — WildDet3D 探索如何从单目 RGB 图像扩展可提示（promptable）的 3D 检测，目标是恢复物体的尺寸、位置和朝向。该工作强调在封闭类别之外的开放世界泛化能力、对多种提示形式的支持，并在可用时充分利用几何线索。文章分析了当前方法以单一提示模态为设计前提所带来的瓶颈，并勾勒出在非受限环境中实现实用、广谱 3D 检测的路径。[来源-huggingface](https://huggingface.co/papers/2604.08626)

### AI Safety

- **Claude Mythos Preview 首个完成 AISI 网络攻防靶场端到端评估** — AI Security Institute 报告称，Claude Mythos Preview 成功完成了在 AISI 网络攻防靶场上的端到端评估，据称是首个做到这一点的模型。该里程碑凸显了在以安全为重点的评测方法以及大语言模型网络安全测试方面的进展。[来源-twitter](https://x.com/AISecurityInst/status/2043683577594794183)

## ⚡ 快讯速览

- **视频拆解 Claude Code 和 Agent Harness，并从零实现一个** — t3.gg 上的一位作者讲解 Claude Code 和其他 agent harness，强调这些并不是“黑魔法”。视频帮助观众理解这些框架的工作机理，从而更易上手使用。作者还现场构建了一个 harness，以直观演示这一概念。[来源-twitter](https://x.com/Hesamation/status/2043670864244150445)
- **每月 200 美元可获得工作日每天 6 小时 H100 GPU** — 一条推文称，每月 200 美元就足以在工作日每天获得 6 小时 H100 GPU 使用时间。这凸显了硬件成本结构以及高端 AI 加速卡潜在的可负担性。如果属实，这一说法可能影响 AI 项目和独立研究者的预算规划。[来源-twitter](https://x.com/ekzhang1/status/2043562453452128359)
- **Opus 4.7 和 Sonnet 4.8 即将发布** — 提醒大家，Opus 4.7 和 Sonnet 4.8 版本预计很快发布。这些更新很可能会带来新特性和针对相关 AI 工具库的改进。开发者应关注官方发布说明和公告。[来源-twitter](https://x.com/kimmonismus/status/2043681667542397341)
- **MegaStyle：可扩展且风格一致的文生图风格数据集** — MegaStyle 提出了一套可扩展的数据筛选流程，通过利用大规模生成模型中稳定的“文本到图像风格映射”，构建“风格内一致、风格间多样”的风格数据集。该框架整理出一个包含 17 万条风格提示和 40 万条内容提示的大型 prompt 库，用于支持高质量风格数据的模型训练。[来源-huggingface](https://huggingface.co/papers/2604.08364)
- **FORGE：制造业细粒度多模态评测基准** — FORGE 提出一个高质量多模态数据集，将真实世界的 2D 图像和 3D 点云结合起来，用于评估在制造场景中运行的多模态大语言模型（MLLM）。它旨在缓解数据稀缺和领域细粒度语义缺乏的问题，从而实现对制造业场景下 MLLM 更严格、更贴近现实的评估。[来源-huggingface](https://huggingface.co/papers/2604.07413)
- **Claude-Mem：为 Claude Code 会话提供持久记忆** — 这是一个开源的 Claude Code 插件，会自动捕捉你的编码工具使用情况，通过 Claude 的 agent-sdk 使用 AI 压缩信息，并将语义上下文注入到未来会话中。它在多次会话之间保留上下文，帮助 Claude 在持续开发工作中保持知识连贯。[来源-github](https://github.com/thedotmack/claude-mem)
- **Ralph：自动化 AI Agent 循环，直到完成全部 PRD** — Ralph 是一个自主 AI Agent 循环，会反复运行 AI 编码工具（默认 Amp CLI，也可选 Claude Code），直到所有 PRD 项目全部完成。每次迭代都会从全新上下文开始，但通过 git 历史、progress.txt 和 prd.json 来保留记忆。该工作流遵循 Geoffrey Huntley 的 Ralph 模式，部署时需要向项目中添加 Ralph 相关文件和工具提示，并满足诸如已安装相关工具、完成鉴权、安装 jq 以及使用 git 仓库等前置条件。[来源-github](https://github.com/snarktank/ralph)
- **将两台 RTX PRO 6000 主机合并为一台工作站** — 一位爱好者分享了如何把两台 RTX PRO 6000 塔式主机整合为一台高端工作站。该配置采用 AMD Threadripper PRO 7965WX、华硕 Pro WS WRX90E-SAGE SE 主板、128GB ECC 内存，以及两块 RTX PRO 6000 Blackwell GPU（每块 96GB，总计 192GB 显存），配备 1600W 钛金电源和 Corsair 9000D 机箱。作者也邀请大家提供建议和提问。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sklhzv/follow_up_post_decided_to_build_the_2x_rtx_pro/)
- **利用冲压进气和窗户风道给 1100W AI 机器散热** — 一位 Reddit 用户介绍了他们为约 1100W 功耗的高性能 AI 机器构建的散热方案，采用冲压进气（ram-air）和窗户排风相结合。据称该方案可将约 90% 的热量直接排出窗外，散热效果与开放机箱相当。这篇帖子旨在激发他人尝试类似的散热设计。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sknbbu/ramair_setup_and_window_vent_for_1100w_capable_ai/)
- **MiniMax 面向 API 的许可条款可能扩展到普通用户** — MiniMax 的 Ryan Lee 发文解释，当前许可主要针对此前对 M2.1/M2.5 支持不佳的 API 提供方。他表示 MiniMax 可能会更新许可，将普通用户也纳入其中。该帖子暗示未来可能出现影响非 API 用户的政策变动。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1skabyf/ryan_lee_from_minimax_posts_article_on_the/)
- **优化 Nano Banana 图像生成：从故事、主体到风格的提示技巧** — 帖子提出了一套结构化提示框架，以最大化 Nano Banana 的图像生成效果，通过明确“故事、主体、构图、动作、地点和风格”等关键元素来设计 prompt。文中还给出了用于图像修改的直接编辑指令，并引用了一条来自 GeminiApp 的 Twitter 帖子作为来源。[来源-twitter](https://x.com/GeminiApp/status/2043779910708408577)
- **我写了一个 agent harness 来证明这并不是魔法** — 一则 AI 主题帖子认为 agent harness 并非魔法，作者通过亲手实现一个来展示其工作原理。项目中包括启用 HLS 播放等功能，用以说明在构建与评估 AI agent harness 时的具体实践步骤。[来源-twitter](https://x.com/theo/status/2043611205856837680)
- **Kimi K2.6 即将发布** — 一则匿名 Reddit 帖子暗示 Kimi K2.6 即将到来，但并未提供功能或时间方面的细节。该内容由用户 Deep-Vermicelli-4591 发布在 r/LocalLLaMA，并链接到 LocalLLaMA 的讨论贴。目前尚无官方公告。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sk9twd/kimi_k26_imminent/)
- **新参数量级出现，或预示未来趋势** — 一篇 Reddit 帖子提到出现了一个新的“权重级别”（weight class），暗示在模型参数规模上可能形成新趋势。该消息带有一定猜测成分，并未给出具体细节，只表达了对未来发展的谨慎乐观。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sk416w/we_have_a_new_weight_class/)

---

*由 AI News Agent 生成 | 2026-04-13*