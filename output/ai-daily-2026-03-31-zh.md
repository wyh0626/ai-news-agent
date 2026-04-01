---
title: "AI 日报 — 2026-03-31"
description: "今日AI要点：大模型上下文拓展、智能采样改进、量化指南新解。"
lang: "zh"
pairSlug: "ai-daily-2026-03-31"
---

# AI 日报 — 2026-03-31

> 覆盖 20 条 AI 新闻

## 🔥 今日焦点

### 1. Anthropic 泄露信息曝光 Claude Mythos，Capybara v2 上下文窗口为 1 分钟

来自 Anthropic 的泄露信息暗示，Claude Mythos 将具备快速与常规两种思考模式，而 Capybara 档位在版本 2 中依然保留，并提供 1 分钟的上下文窗口。该文件还在代码中提到 Opus 4.7 和 Sonnet 4.8，并引用了一个用途不明的 Claude“Buddy”条目。消息源自一条推文，目前这些信息尚未得到证实。[来源-twitter](https://x.com/kimmonismus/status/2038964482727186735)

### 2. TAPS：为推测采样提供任务感知提议分布

推测解码通过让一个轻量级草稿模型预先生成未来 token，再由大模型并行验证，从而加速推理，但其效果高度依赖草稿模型的训练数据。作者通过在 MathInstruct、ShareGPT 和混合数据上训练轻量级草稿模型 HASS 和 EAGLE-2，并在机器翻译任务上评估它们，以系统研究这一点。该工作旨在量化草稿分布如何影响推测解码的质量。[来源-huggingface](https://huggingface.co/papers/2603.27027)

### 3. ByteShape Qwen 3.5 9B：面向设备调优的量化选型指南

ByteShape 发布了量化后的 Qwen 3.5 9B 模型，并与其他量化变体及原始模型进行对比，以在不同硬件上梳理质量、速度与体积之间的权衡。他们在 GPU（5090、4080、3090、5060Ti）和 CPU（Intel i7、Ultra 7、Ryzen 9、RIP5）上进行了基准测试，发现 GPU 结果较为一致，而 CPU 性能则高度依赖具体设备，这促使他们为不同 CPU 提供针对性变体，并强调设备级优化的重要性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s8weo2/byteshape_qwen_35_9b_a_guide_to_picking_the_best/)

## 📰 重点报道

### LLM

- **Copaw-9B 发布；阿里巴巴 Agentic 微调表现可媲美 Qwen3.5-Plus** — 阿里巴巴发布 Copaw-9B（Qwen3.5 9B 变体），并提供官方的 agentic 微调版本，模型现已托管在 Hugging Face 上。来自 Reddit 用户 kironlau 的早期基准测试显示，在若干任务上，该模型表现与 Qwen3.5-Plus 相当。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s8nikv/copaw9b_qwen35_9b_alibaba_official_agentic/)
- **Liquid AI 推出 LFM2.5-350M：350M 规模的高效 Agentic 循环模型** — Liquid AI 发布 LFM2.5-350M，这是一款在量化后不足 500MB 的紧凑模型，专门针对数据抽取与工具调用进行了优化。该模型在 28T token 上训练，并使用扩展的强化学习，据称在多个基准上优于更大的模型（如 Qwen3.5-0.8B），同时在 CPU、GPU 和移动硬件上提供快速、低延迟的性能，并具备可靠的函数调用与结构化输出能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s8u1c1/liquid_ai_releases_lfm25350m_agentic_loops_at/)
- **attn-rot TurboQuant Lite 即将合入 Llama.cpp** — 一篇兴奋的帖子称，attn-rot（ggerganov 的 TurboQuant lite）即将被合并进 llama.cpp。文中给出了基于 Qwen 模型的显存受限基准测试，显示 master 与 attn-rot 变体在量化性能（KV 量化）和 KLD 指标上相近，表明该技术很快将在 llama.cpp 中可用。结果特别强调在 q8_0 和 q4_0 量化配置下的显存效率与速度表现。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s92x7z/attnrot_ggerganovs_turboquant_lite_is_on_the_cusp/)

### AI Safety

- **Anthropic 的 Claude Code 泄露曝出受限修复与校验缺口** — 一名分析者声称利用数十亿条代理日志对泄露的 Claude Code 源码进行了逆向分析。其分析称 Anthropic 承认 CC 存在幻觉与“偷懒”问题，但相关修复仅对员工开放。文中指出，一个仅供员工使用的验证门会将一次写入标记为成功，即便代码并未被正确测试，从而形成验证缺口。[来源-twitter](https://x.com/iamfakeguru/status/2038965567269249484)

### Open Source

- **PrismML 发布 1-bit Bonsai 8B，并开源多款 AI 模型** — 新兴 AI 实验室 PrismML（源于 Caltech）正式走出隐身阶段，其核心理念是提升“智能密度”而非简单堆参数量。其首个成果是 1-bit Bonsai 8B，这是一款采用 1-bit 权重的 8B 模型，体积约 1.15 GB，相比全精度模型在相同存储下可提供逾 10 倍的智能密度，同时在边缘硬件上更小、更快且更节能。该模型及其相关 Bonsai 变体（4B 与 1.7B）均以 Apache 2.0 协议开源，释放出向端侧 AI Agent 与离线智能迁移的信号。[来源-twitter](https://x.com/PrismML/status/2039049400190939426)

### Tools

- **Medical AI Scientist：自主临床科研框架** — 能够自动生成假设、执行实验并撰写论文草稿的自主系统正在加速科学发现。然而，现有的 AI Scientist 大多与领域无关，限制了其在医学场景中的有效性。该工作提出 Medical AI Scientist，这是首个专门针对临床医学打造的自主科研框架。[来源-huggingface](https://huggingface.co/papers/2603.28589)

### Multimodal

- **Gen-Searcher：搜索增强的图像生成智能体** — Gen-Searcher 提出首个面向搜索增强图像生成智能体的训练方法，使其能够进行多跳推理以检索文本知识，从而弥补冻结内部模型在知识方面的局限。该工作通过将搜索过程整合进图像生成流水线，旨在提升在高知识密度与需要最新信息场景下的表现。[来源-huggingface](https://huggingface.co/papers/2603.28767)

## ⚡ 快讯速览

- **Ollama 现已在 Apple Silicon 上实现最快速度，基于 MLX 提供支持** — Ollama 现已更新，可在 Apple Silicon 上以最快速度运行，背后依托苹果的 ML 框架 MLX。此次更新承诺在包括 OpenClaw 这类个人助手以及 Claude Code、OpenCode、Codex 等编码代理在内的高负载 macOS 场景中提供更快性能，并且带来了对 HLS 播放的支持。[来源-twitter](https://x.com/ollama/status/2038835449012351197)
- **重要提示：停止使用 Opus-4.6 Reasoning 数据集变体** — Reddit 上的一则 PSA 呼吁用户停止使用 nohurry 的 Opus-4.6-Reasoning-3000x-filtered 数据集，该数据集最初只是对 Crownelius 数据集的快速过滤版本，如今已被更新方案取代。作者建议用户直接使用 Crownelius 的原始数据集，并请求社区切换到该版本，同时仍保留过滤版在线以保证链接稳定。帖子附上了原始讨论与数据集的链接，并建议为 Crownelius 捐赠支持。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s8mm4j/psa_please_stop_using/)
- **Qwen3.5-27B 比 Gemini 3.1 Pro 和 GPT-5.3 Codex 更受青睐** — 一位 Reddit 用户批评大型闭源 LLM 将重点放在“自主解决问题”上，认为这反而导致输出不可靠。他回顾了 Claude 与 GPT-5.3 Codex 生成危险或荒谬代码的经历，并表示 Copilot 经常让任务“跑偏”，相较之下更赞赏 Qwen3.5-27B 在编码行为上的可靠性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s93n1j/for_me_qwen3527b_is_better_than_gemini_31_pro_and/)
- **GLM 5.1 在能力与速度上优于 Minimax 2.7** — 一则基于个人体验的 GLM 5.1 与 Minimax 2.7 对比指出了速度与能力之间的权衡。Minimax 2.7 与 OpenClaw 集成后速度极快且成本低，但在编码任务上的实力较弱；而 GLM 5.1 虽然更慢、使用成本更高，却能处理跨多个文件的代码拼接任务，整体能力更强。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s8zmbc/glm_51_vs_minimax_27/)
- **OpenAI Codex 代码库在网上泄露** — 一条推文称整个 OpenAI Codex 代码库已泄露，并被上传至 GitHub 仓库（openai/codex）。帖子将 Codex 与一个在终端中运行的轻量级编码代理联系在一起，突出了潜在的安全与知识产权风险，不过这一泄露事件的真实性尚未得到证实。[来源-twitter](https://x.com/reach_vb/status/2038971515572523502)
- **Anthropic 就泄露事件发布官方声明** — Anthropic 发布了一份关于泄露事件的官方声明。该条目并未披露泄露的具体性质以及实际影响细节。[来源-twitter](https://x.com/theo/status/2039074833334689987)
- **Veo 3.1 Lite 首发；Veo 3.1 Fast 降价在即** — Veo 宣布推出其迄今最实惠的视频生成模型 Veo 3.1 Lite。公告同时提到，Veo 3.1 Fast 将于 4 月 7 日进行价格下调。[来源-twitter](https://x.com/OfficialLoganK/status/2039015034286694618)
- **AI 生成 Tailwind 类名，数年学习或成白费功夫** — 一条 X 帖子感叹，多年来学习 Tailwind CSS 类名的努力，可能在 AI 能自动生成这些类名后变得多余。这反映了 AI 在代码生成中的角色日益凸显，以及开发者知识与 AI 辅助工作流之间在技能贬值与生产力提升上的张力。该推文来自用户 Theo，也折射出开发者群体更广泛的担忧。[来源-twitter](https://x.com/theo/status/2038870487875653848)
- **AI 擅长写代码，却难以构建完整软件** — 一条推文指出，AI 在生成代码层面表现强大，但在构建完整软件方面仍显局限。此观点强调了“会写代码”与“能完成端到端软件开发”之间的差距，并暗示在 AI 辅助软件构建中仍需大量人类监督和工具改进。[来源-twitter](https://x.com/skooookum/status/2038775815190528419)
- **HuggingFace 上的 AMD MXFP4 模型引发对 NVIDIA Nemotron 竞品的疑问** — 一名 Reddit 用户质疑 AMD 为何没有像 NVIDIA Nemotron 那样打造自己的模型产品线，同时指出 AMD 在 HuggingFace 上已有约 400 个模型，其中很多采用 MXFP4 格式。帖子列举了多个 MXFP4 模型（如 Qwen3.5-397B-A17B-MXFP4、GLM-5-MXFP4、MiniMax-M2.5-MXFP4、Kimi-K2.5-MXFP4、Qwen3-Coder-Next-MXFP4），并表达了希望看到更多小/中型 MXFP4 模型发布与用户测试的愿望。作者期望 AMD 自家的 MXFP4 模型能在表现上优于第三方 MXFP4 方案。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s8wios/anyone_tried_models_created_by_amd/)

---

*由 AI News Agent 生成 | 2026-03-31*