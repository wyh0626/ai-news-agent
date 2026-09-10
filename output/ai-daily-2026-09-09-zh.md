---
title: "AI 日报 — 2026-09-09"
description: "新AI模型聚焦开源语音编辑、实时全双工多模态交互及智能体后训练自我优化。"
lang: "zh"
pairSlug: "ai-daily-2026-09-09"
---

# AI 日报 — 2026-09-09

> 涵盖 25 条 AI 新闻

## 🔥 今日焦点

### 1. AuK 开源模型统一语音生成与编辑

AuK 是一个基础语音模型，可通过自然语言指令完成生成、内容编辑、增强、分离、副语言编辑和声学编辑等任务。该模型基于约 30.3 亿条指令-音频样本和 195 万小时监督数据进行训练，提供了异常广泛的语音控制接口。此次开源发布对正在构建语音助手、有声书工具和音频后期制作工作流的开发者意义重大。[来源-huggingface](https://huggingface.co/papers/2609.08936)

### 2. Gander 融合全感知、全双工交互与智能体技能

Gander 是一个端到端模型，可处理流式视频、语音和文本输入，同时支持自然的实时对话和智能体工作流。其全双工设计意味着用户可以随时打断模型，这是实现类人语音和多模态界面的关键要求。这为构建更统一的助手指明了一条路径——无需在多个专用模型之间切换，即可完成感知、对话与行动。[来源-huggingface](https://huggingface.co/papers/2609.08977)

### 3. 27B 1-bit 模型在浏览器中运行，6GB GPU 上速度达 25–30 tok/s

一位独立开发者构建了 WebGPU/WGSL 推理引擎，可在配备 6GB 显存的 RTX 3060 Laptop 上以 25–30 tokens/s 的速度在浏览器中完全运行 Bonsai-27B（一个 27B 参数的 1-bit 模型）。该模型仅占用 3.8GB 显存，既无需安装也不需要服务器，这充分展示了端侧推理已发展到的水平。这一里程碑有望加速大模型在消费级硬件上的私密、低摩擦部署。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbm50k/1bit_27b_in_the_browser_2530_toks_on_a_6_gb_rtx/)

## 📰 重点报道

### AI 研究与安全

- **NeoHorse-1 通过智能体后训练探索自我改进** — 这个智能体原生模型系列采用异构模型池与智能路由来实现递归式自我改进，同时也为未来的训练周期带来了能力与安全方面的双重问题。[来源-huggingface](https://huggingface.co/papers/2609.08183)
- **在线策略反向蒸馏提升弱到强泛化能力** — OPRD 让学生模型从自身的在线策略输出中进行蒸馏，从而超越较弱的教师模型，有望在连续的模型代际之间实现更高效的整合。[来源-huggingface](https://huggingface.co/papers/2609.08798)

### 自动驾驶

- **DriveZero：超越人类示范的端到端驾驶系统** — DriveZero 将驾驶任务拆分为分别预训练的感知模型和行动模型，再合并为统一的规划器，旨在自动驾驶中超越人类示范日志的上限。[来源-huggingface](https://huggingface.co/papers/2609.06055)

### Agent 与开发者工具

- **Superpowers 框架教编程 Agent 在写代码前先提问** — 这个可组合技能框架推动编程 Agent 在编写代码前先澄清用户意图并生成规格说明，有望减少因理解需求偏差而导致的无效迭代。[来源-github](https://github.com/obra/superpowers)
- **Browser Use 让 AI Agent 实现网页任务自动化** — 这个开源 Python 库和托管云服务赋予 AI Agent 浏览器控制能力，可实现表单填写、数据抽取以及更复杂的网页工作流自动化。[来源-github](https://github.com/browser-use/browser-use)
- **OpenAI 在 GitHub 发布精选 Codex 插件示例** — 该仓库包含针对 Figma、Notion 和应用开发的插件集成，并提供了 manifest 示例和配套界面，帮助开发者基于 Codex 进行构建。[来源-github](https://github.com/openai/plugins)

### 硬件与端侧推理

- **Apple A20 Pro 芯片配备 7 核 GPU、32 核神经引擎** — 据报道，A20 Pro 采用 2nm 工艺，神经引擎核心数量翻倍，并配备 96-bit LPDDR5X 内存总线，内存带宽约 115 GB/s，较上代提升约 50%。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wc0ekw/apple_a20_pro_debuts_with_7core_gpu_32core_neural/)

## ⚡ 快讯速览

- **NVIDIA Cosmos3 64B 可通过 INT4 量化在 Apple Silicon 上本地运行** — Reddit 用户报告，NVIDIA 的 Cosmos3 64B 图像模型现在可以通过 INT4 量化在 Apple Silicon 上本地运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbmz1y/sota_imagegen_locally_nvidia_cosmos364b_int4/)
- **AMD 发布面向本地 AI 的 Threadripper Halo Station 工作站** — AMD 的新款工作站被定位为一台面向高端本地部署负载的硬核本地 AI 机器。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbir6v/now_this_is_a_serious_local_machine/)
- **AI 音频模型可根据文本提示生成合成器声音并支持音色控制** — 一位开发者训练的音频模型，能够根据文本提示生成合成器声音，同时提供音色控制能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbtqt7/i_trained_an_audio_model_that_can_generate/)
- **对 ADHD 友好的技能包可改善编程 Agent 输出** — 一个 GitHub 技能包旨在让编程 Agent 的输出对 ADHD 用户而言更结构化、更易于跟进。[来源-github](https://github.com/ayghri/i-have-adhd)
- **受 Karpathy 启发的 CLAUDE.md 改善 Claude Code 行为** — 一个受 Andrej Karpathy 工作流偏好启发的社区 CLAUDE.md 文件，可帮助引导 Claude Code 展现出更整洁的编程行为。[来源-github](https://github.com/multica-ai/andrej-karpathy-skills)
- **GLM 5.3 Flash 通过内核融合在 M3 Ultra 上速度翻倍** — 据报道，内核融合优化使 GLM 5.3 Flash 在 Apple M3 Ultra 机器上的吞吐量翻倍。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbkpnw/glm_53_flash_q4_60tps_550tps_on_m3_ultra/)
- **Qwen 模型通过降噪减少推理 token 数量** — 一个社区版 Qwen GGUF 构建应用了降噪技术，以减少模型输出的推理 token 数量。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbmo0k/qwen3827buncensoredgenesisv1gguf/)
- **Qwen3-27B 在 RTX 3060 上以 10–20 TPS 运行** — 有用户演示，采用 IQ3_XXS 量化的 Qwen3 27B 可在 RTX 3060 上以可用速度运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wc2cs2/running_qwen_38_27b_iq3_xxs_on_rtx_3060/)
- **DeepSeek 悄然退役 V4 Pro 模型** — Reddit 用户注意到，DeepSeek 已悄悄停止推广 DeepSeek V4 Pro。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbfrut/deepseek_has_soft_retired_deepseek_v4_pro/)
- **社区讨论适合旁白配音的最佳开源 TTS 模型** — LocalLLaMA 社区分享了当前适合旁白配音的开源 TTS 模型推荐。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbpyp7/best_open_source_tts_right_now_for_narration/)
- **Reddit 帖子征集最佳本地视觉语言模型** — 用户们就截至 2026 年 8 月在本地运行视觉语言模型的最佳选择和实用技巧进行了交流。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx7ei1/best_local_vision_language_models_august_2026/)
- **LM Studio 用户在 Bionic Agent 推广期间遭遇下载困难** — 部分用户反映，在项目着重推广新的 Bionic Agent 功能之际，LM Studio 的下载和更新流程令人困扰。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wble79/why_the_hell_is_lm_studio_making_lm_studio_so/)
- **别让 FOMO 左右本地 LLM 购买决策，用现有设备边学边用** — 社区建议鼓励新手在购买新硬件之前，先用现有的本地模型和硬件进行尝试。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbufx5/dont_let_fomo_win_if_youre_interested_in_local/)
- **用户提议新模型发布时标明更清晰的微调标签** — 一位 Reddit 用户建议，新模型发布时应明确标明其是否为微调模型而非基础模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbpf6i/mention_if_a_new_model_is_a_finetune/)
- **定制水冷改装为配备 2 张 RTX Titan 和 2080 Ti 的 70GB VRAM 服务器降温** — 据称，一位用户为其由两张 RTX Titan 和一张 2080 Ti 组成的 70GB VRAM 平台改装了定制水冷回路，成功降低了运行温度。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wbttmz/server_rebuild_to_custom_loop_2x_rtx_titans_24gb/)

---

*由 AI 新闻智能体生成 | 2026-09-09*