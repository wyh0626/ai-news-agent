---
title: "AI 日报 — 2026-03-27"
description: "Capybara领先Opus4.6；DeepMind招训VLM；限额重置启插件。"
lang: "zh"
pairSlug: "ai-daily-2026-03-27"
---

# AI 日报 — 2026-03-27

> 覆盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. Capybara 以更高得分超越 Claude Opus 4.6

Anthropic 发布了全新模型 Capybara，在软件编程、学术推理和网络安全等方面宣称能大幅超越 Claude Opus 4.6 的表现。据报道，Capybara 可能是一款拥有 10 万亿参数、训练成本约 100 亿美元的模型，这一估算源自此前对 Dario 的采访。 [来源-twitter](https://x.com/Yuchenj_UW/status/2037387996694200509)

### 2. Gabriberton 加入 Google DeepMind 训练 VLMs

使用账号 @gabriberton 的 AI 研究者宣布加入 Google DeepMind，从事视觉-语言模型（Vision-Language Models, VLMs）的训练工作。他表示会继续分享关于 AI、计算机视觉和大模型发展的内容，但将停止分享 PyTorch 技巧，并可能开始发一些与 JAX 相关的内容。 [来源-twitter](https://x.com/gabriberton/status/2037344674554458117)

### 3. Codex 使用额度重置以便测试插件

Codex 的使用额度在所有套餐中已被重置，让所有用户都可以尽情试验新上线的插件。公告鼓励开发者使用 Codex 无限制地构建各种应用，并在探索中享受乐趣。 [来源-twitter](https://x.com/thsottiaux/status/2037346989244096581)

## 📰 重点报道

### AI Safety

- **判决结果或将偏向 Anthropic；政府行为被指违宪** — 一项法院裁决显示，在多数关于政府行为是否违法和违宪的法律论点上，Anthropic 很可能胜诉。帖子指出，有众多法庭之友意见书支持 Anthropic，却没有任何文书支持美国政府；作者同时反思了自己站出来反对当届政府在个人层面付出的代价。 [来源-twitter](https://x.com/deanwball/status/2037323427082580449)

### Open Source

- **SAM 3.1 引入对象复用，加速视频处理** — Meta 发布 SAM 3.1 版本，这是对 SAM 3 的即插即用升级，引入了对象 multiplexing（对象多路复用）以在不牺牲精度的前提下提升视频处理效率。该更新旨在让高性能 AI 应用能够运行在更小、更易获取的硬件上，并通过开放模型 checkpoint 和代码库邀请社区采用。模型 Checkpoint: go.meta.me/8dd321；代码库: go.meta.me/b0a9fb。 [来源-twitter](https://x.com/AIatMeta/status/2037582117375553924)
- **Insanely Fast Whisper：超高速本地语音转写** — 一个新的开源 CLI 工具 insanely-fast-whisper 声称，基于 Whisper Large v3，可在 Nvidia A100 80GB 上在 98 秒内转写 150 分钟音频。它利用 FP16、batching、BetterTransformer 和 Flash Attention 2 显著加速转写过程，并提供多种基准测试配置。该项目完全开源并托管在 GitHub 上，展示了在本地语音识别场景中的显著 AI 性能优化。 [来源-github](https://github.com/Vaibhavs10/insanely-fast-whisper)

### AI Translation

- **Google Translate 实时翻译携耳机登陆 iOS** — Google Translate 的 Live Translate（实时翻译）功能在搭配兼容耳机使用时，现已正式登陆 iOS，并将很快在更多国家为 Android 和 iOS 提供支持。该服务支持 70 多种语言，用户可以通过 Translate 应用连接耳机，实现实时双向翻译。 [来源-twitter](https://x.com/Google/status/2037586898450006029)

### LLM

- **四月前瞻：GPT-5.5、Claude 5、Mythos DeepSeek-V4** — 一条推文预告了即将发布的多款新模型：GPT-5.5、Claude 5 和 Mythos DeepSeek-V4，暗示四月可能迎来重要更新。帖子反映出社区对来自顶尖实验室的新一代大模型的高度期待。 [来源-twitter](https://x.com/scaling01/status/2037582929648288245)
- **GLM-5.1 上线：编程能力媲美 Claude Opus 4.5** — 智谱 AI 的 GLM-5.1 现已向 Coding Plan 用户开放。该模型在多个开源基准上取得高分，并在编码任务上与 Claude Opus 4.5 相当，具备 200K 上下文窗口、128K 最长输出、744B 参数及 28.5T 预训练数据，并原生支持 MCP。它支持自主多步编程、长上下文重构和智能体式工作流，可通过智谱 AI 平台的 Coding Plan Lite/Pro/Max 套餐使用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s55xox/glm51_is_live_coding_ability_on_par_with_claude/)
- **Google TurboQuant 在 MacBook Air 本地跑 Qwen** — 一篇 Reddit 帖子介绍了如何将 Google 的 TurboQuant 压缩方案打补丁集成进 llama.cpp，从而在一台 MacBook Air（M4，16 GB）上本地运行 Qwen 3.5–9B，并支持 20,000 token 上下文。该实验表明，大上下文提示在消费级硬件上也可能变得可行，类似 OpenClaw 的能力不再仅限高端设备。帖子还提到了一款 MacOS 应用（atomic.chat），并邀请其他人尝试类似配置。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5kdu0/google_turboquant_running_qwen_locally_on_macair/)
- **Gemini Pro 泄露 chain-of-thought，并陷入无限循环** — Reddit 上有报告称，Gemini Pro 在回答时输出了内部推理过程和系统提示词，而不是最终答案，随后还陷入了无限循环，生成了成千上万行 “(End)” 文本。该事件凸显了 chain-of-thought 泄露和模型行为异常的风险，暴露内部提示词以及输出失控都可能带来安全与可靠性问题。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s589ev/gemini_pro_leaks_its_raw_chain_of_thought_gets/)
- **Google TurboQuant 将 LLM 压缩 6 倍且无质量损失** — 据称，Google 的 TurboQuant AI 压缩算法可在不降低输出质量的前提下，将大语言模型的内存占用减少约六倍。这一方法有望大幅提升模型部署效率，使前沿级模型有机会在消费级硬件上运行。该新闻项引用了 Ars Technica 的报道，并提到 Reddit 上的相关讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s57ky1/googles_turboquant_aicompression_algorithm_can/)
- **AI 协助制定狗狗 Rosie 的 mRNA 疫苗方案** — Paul S. Conyngham 使用 ChatGPT 和其他大模型为自己的狗 Rosie 制定了一套 mRNA 疫苗方案。 他表示，这些 AI 工具在人的监督下，让他能够完成类似科研工作的任务，将机器指导与专家意见相结合。这一故事暗示，此类 AI 驱动的生物技术探索可能发展为公司化项目，展示了一个现实世界中利用 AI 进行生物设计的典型案例。 [来源-twitter](https://x.com/sama/status/2037396826060673188)
- **AgentScope 发布可用于生产的 LLM Agent 框架** — AgentScope 推出了一套面向生产环境的智能体框架，旨在随大模型能力演进进行扩展，更强调推理与工具使用，而不是僵化的 Prompt。它宣称可在 5 分钟内快速上手，并内置 ReAct、记忆、规划、人类参与式调控和模型微调能力，同时提供可扩展工具体系和多智能体编排。部署方式支持本地、无服务器云和 Kubernetes，并集成 OpenTelemetry。 [来源-github](https://github.com/agentscope-ai/agentscope)
- **OpenSource4o 运动因 GPT-4o 开放趋势走红** — 一篇 Reddit 帖子指出，OpenSource4o 运动正在 Twitter/X 上流行，呼吁围绕 GPT-4o 推出开源或开放权重的相关模型。帖子提到 8 个月前发布的 GPT-OSS 模型（120B 和 20B），并承诺在评论中补充更多信息（网站、请愿等），希望发掘更多适用于编程、写作和内容创作的开放模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5g1v9/opensource4o_movement_trending_on_twitterx/)

### Industry

- **Google 将为 Anthropic 数据中心提供资金支持** — 据《金融时报》报道，Google 即将达成一项协议，为 Anthropic 的数据中心提供资金支持。这将扩大 Google 在 AI 基础设施方面的投资，并提升 Anthropic 的算力规模。该动向凸显出大型科技公司之间在 AI 基建上的持续合作趋势。 [来源-twitter](https://x.com/FirstSquawk/status/2037586926375743904)

### Multimodal

- **Intern-S1-Pro：首个万亿参数科学多模态基础模型** — Intern-S1-Pro 被介绍为首个拥有一万亿参数的科学多模态基础模型。据称，它在通用和科学推理方面都有提升，加强了图文理解能力，并加入了更先进的智能体能力，覆盖 100 多个关键科学领域中的专业任务。 [来源-huggingface](https://huggingface.co/papers/2603.25040)
- **PixelSmile 实现精细的面部表情编辑** — 研究者提出了 Flex Facial Expression（FFE）数据集，包含连续情感标注，并构建了 FFE-Bench，用于评估编辑精度、可控性与身份保持之间的权衡。随后他们提出 PixelSmile，这是一种基于扩散模型的框架，通过完全对称的联合训练来解耦表情语义。 [来源-huggingface](https://huggingface.co/papers/2603.25728)

### AI

- **Chandra OCR 2 推进多模态文档版面识别** — datalab-to 最新发布的 Chandra OCR 2 声称，在将图片和 PDF 转换为结构化 HTML、Markdown 或 JSON 并保留版面结构方面达到了 SOTA 水平。它改进了对数学公式、表格、表单和多语种 OCR 的支持，覆盖 90 多种语言，并在手写识别、表单重构和带说明的图片抽取上表现出色。该模型既可本地运行（HuggingFace），也可通过远程 vLLM 服务器使用，并提供托管 API。 [来源-github](https://github.com/datalab-to/chandra)
- **RealRestorer：利用编辑模型提升真实场景图像复原泛化性** — 真实场景图像复原依然困难重重，主要由于退化类型多样且训练数据有限。文章指出，大规模图像编辑模型在复原任务上具有良好的泛化能力，一些闭源模型（如 Nano Banana Pro）能够在保持图像内容的同时，取得有效的图像恢复效果。 [来源-huggingface](https://huggingface.co/papers/2603.25502)

### ASR

- **VibeVoice 9B 以 8.34% WER 领跑开源医疗 STT** — 在第三版医疗语音转文字基准中，共评测了 31 个模型，Microsoft VibeVoice-ASR 9B 以 8.34% 的词错误率（WER）夺得开源模型头名，几乎追平 Gemini 2.5 Pro 的 8.15%。不过，其 9B 参数规模需要约 18 GB 显存，且速度较慢（约 97 秒/文件），相比之下 Parakeet 等模型更快。研究还指出 Whisper 文本归一化器存在一个 bug，使得各模型的 WER 被抬高了 2–3%，并新增了 ElevenLabs Scribe v2、NVIDIA Nemotron Speech Streaming 0.6B 和 Voxtral Mini 2602 等模型；所有代码和结果均为开源。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s4z18o/i_benchmarked_31_stt_models_on_medical_audio/)

## ⚡ 快讯速览

- **Claude Code：像喝醉的 Codex——有趣、有创意，但不适合上生产** — Claude Code 被形容为比 Codex 更有玩味、更具创造力的编程助手。尽管它非常友好、有趣，但也容易犯一些低级错误，因此不应在生产环境中被完全信任。 [来源-twitter](https://x.com/theo/status/2037366608776319399)
- **EVA：用于端到端视频智能体的高效强化学习** — 文中指出，多模态大模型在视频理解上面临长序列和大量冗余帧的挑战，目前的方法往往把 MLLM 当作被动识别器，或依赖人工设计、以感知为先的流程。EVA 被提出作为一种方法，以实现端到端视频智能体的高效强化学习，从而缓解这些低效问题。 [来源-huggingface](https://huggingface.co/papers/2603.22918)
- **Dexter：用于深度金融研究的自主 AI** — Dexter 是一个面向金融研究的开源自主 AI 智能体。它会将复杂问题拆解为逐步计划，利用实时市场数据执行任务，并通过自我验证来产出有数据支撑的分析结果。 [来源-github](https://github.com/virattt/dexter)
- **2B 模型在设备端是实用工具还是玩具？** — 一位 Reddit 用户在手机上测试了本地部署的 2B 模型（qwen2.5/3.5、gemma），发现约 80% 的回答存在幻觉。他们质疑这是使用方式有误还是模型固有限制，凸显了端侧小参数 LLM 在实际任务中的挑战与局限。讨论聚焦于 2B 模型在真实应用中的实用性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5bztk/do_2b_models_have_practical_use_cases_or_are_they/)
- **推文称 UI 设计暴露了模型时代** — 一条 X 帖子指出，应用的背景渐变和按钮颜色往往能暗示其使用的是哪一代 AI 模型。作者认为这有些滑稽，也从侧面反映出 UI 设计如何泄露底层技术栈。 [来源-twitter](https://x.com/theo/status/2037335741794275537)
- **从 48GB 升到 60GB 显存值得吗？** — 一位 Reddit 用户拥有两张 RTX 3090（总共 48GB 显存）和一张额外的 RTX 3080（12GB），他在考虑是否有必要把总显存升级到 60GB。TA 希望获得关于具体使用场景的建议，并表示如果显存提升带来的收益有限，就不想为加第三张卡所带来的折腾买单。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5jjz8/is_it_worth_the_upgrade_from_48gb_to_60gb_vram/)

---

*由 AI News Agent 生成 | 2026-03-27*