---
title: "AI 日报 — 2026-06-04"
description: "英伟达推Nemotron3U长时代理Hermes自改多模4GBGPU下70B推理"
lang: "zh"
pairSlug: "ai-daily-2026-06-04"
---

# AI 日报 — 2026-06-04

> 涵盖 26 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA 发布 Nemotron 3 Ultra，面向长时运行的 AI Agent

NVIDIA 推出 Nemotron 3 Ultra，这是一款面向前沿的智能开源模型，专为需要在编码、研究和企业工作流中进行规划、推理和调用工具的长时运行 Agent 设计。NVIDIA 称，Nemotron 3 Ultra 在 Agent 任务上的推理速度可提升最多 5 倍，成本可降低最高 30%。[来源-twitter](https://x.com/nvidia/status/2062522316672667770)

### 2. Hermes Agent：支持多模型的自我改进 AI 工具

Nous Research 推出的 Hermes Agent 是一款具备自我改进能力的 AI Agent，内置学习循环：根据经验自动创建技能，在使用过程中不断打磨，并在跨会话中建立对你的加深画像。它可运行在廉价 VPS、GPU 或无服务器云上，并可通过 Telegram 访问，无需绑定笔记本设备，同时支持在多模型间无缝切换（Nous Portal、OpenRouter、NovitaAI 等）。它还提供完整的 TUI、对话历史和流式输出，带来类似终端的交互体验。[来源-github](https://github.com/NousResearch/hermes-agent)

### 3. AirLLM 让 4GB GPU 即可运行 70B 规模 LLM 推理

AirLLM 声称通过优化推理阶段的内存占用，可在单块 4GB GPU 上运行 70B 规模的 LLM，而无需量化、蒸馏或剪枝。它还支持在 8GB 显存上运行 405B 参数的 Llama3.1，并带来包括 CPU 推理支持、非分片模型与 MacOS 兼容性在内的更新。该项目新增自动模型检测以及 8-bit/4-bit 量化支持等特性。[来源-github](https://github.com/lyogavin/airllm)

## 📰 重点报道

### LLM

- **华为开源 KVarN KV-cache 量化方案，压缩率达 3–5 倍** — 华为在 Apache 2.0 许可下开源 KVarN，这是一种 KV-cache 量化方法，只需在 vLLM 中加一个 flag 即可接入。官方称其可实现 3–5 倍 KV-cache 压缩，相比 FP8 仍能带来实际加速，并在上下文长度上相较 FP8 提升约 1.4 倍（而 FP16 约为 2 倍）；与之对比，Google 的 TurboQuant 在 vLLM/Red Hat AI 的分析中被指出可能拖慢内存性能。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1twptw2/kvarn_new_kvcache_quant_from_huawei_35_kv_cache/)
- **Anthropic：Claude 正在加速迈向递归自我改进** — Anthropic 披露内部数据称，Claude 正在加速推动 AI 发展朝向“递归自我改进”，即 AI 能够自主构建更强大的后继系统。该公司指出，这一进展速度超出预期，其潜在影响值得获得更高关注度。[来源-twitter](https://x.com/AnthropicAI/status/2062568862479208923)
- **面向在线 LALM 的音频交互模型** — 一篇文章提出将大型音频语言模型整合为一个统一的在线系统，构建一个始终处于“感知-决策-响应”循环中的架构。该“Audio Interaction（音频交互）”方法设想模型能在声音、环境和指令之间进行实时聆听与反应。其目标是从离线 LALM 过渡到一个统一的、支持流式处理的 AI 生态系统。[来源-huggingface](https://huggingface.co/papers/2606.05121)
- **Qwen 3.6 35B 表现出色；KV cache 被证明至关重要** — 一位更新体验的用户分享对 Qwen 3.6 35B 的测试结果，发现启用 KV cache 后性能有显著提升。此前他们更偏好 Qwen 27B，但频繁遭遇子图与上下文溢出调试难题，促使其在 IQ4NXL 配置（MTP + 标准）及相关变体下重新评估。该帖子强调，KV cache 是影响实际 LLM 性能的关键因素。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1twyoqe/you_guys_were_right_qwen_36_35b_is_goodand_kv/)
- **Gemma 4 QAT 即将发布消息得到确认** — 一条 Reddit 帖子称，采用 Quantization Aware Training（QAT）的 Gemma 4 已确认会在不久后发布。帖子建议潜在测试者暂缓进行量化测试，等待后续更完善的版本出现。发帖人将这一消息归功于来自 Gemma 团队的 Omar。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1twid14/gemma_4_qat_confirmed_to_release_soon/)

### 开源

- **Higgs Audio 发布 v3 TTS 4B，面向语音聊天场景** — Higgs Audio 发布了其 v3 TTS 模型，参数规模为 4B，专为语音聊天应用打造。该模型支持 100 种语言，并提供内嵌控制功能，用于在聊天中实时调节参数和效果。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tx2mot/higgs_audio_v3_tts_4b_built_for_voice_chat/)

### AI 测评

- **DeepSWE 基准被指运行不当，结果无效** — 一条 Reddit 帖子批评 DeepSWE 基准在执行过程中存在严重不当之处，导致其结果失去参考价值。作者认为其方法论存在缺陷且难以复现，从而对该基准所得结论的可靠性提出质疑。这凸显了业界对 AI 评测基准在可靠性与可重复性方面持续存在的担忧。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1twsffj/the_deepswe_benchmark_was_runned_rather/)

### LLMs

- **李飞飞：World Models 将补充 Language Models 的能力** — 李飞飞博士认为，语言模型学习的是文本的统计模式，而世界模型（World Models）学习的是时空结构。她表示，世界模型将使机器能够理解、想象、推理并与物理世界互动，进而与基于语言的智能形成互补。这一观点在 a16z 的语境中被特别提及，并关联到她在 Substack 上的文章。[来源-twitter](https://x.com/elonmusk/status/2062423834217898323)
- **OVO-S-Bench：面向多模态 LLM 的流式空间智能基准** — OVO-S-Bench 被提出为一个完全由人工标注的基准，用于评估多模态 LLM 在流式空间智能方面的能力，重点考察 Agent 如何基于第一人称视频流对地点与布局进行推理。该基准包含 348 段源视频、共 1,680 个问题，由 12 名训练有素的标注者完成标注。它聚焦于流式场景下的空间结构推理，试图弥补传统离线或事件聚焦型基准的局限。[来源-huggingface](https://huggingface.co/papers/2606.03890)

### 多模态

- **Grok Imagine 1.5 发布，为《伊利亚特》预告片提供 HLS 播放支持** — 生成式视频工具 Grok Imagine 1.5 已正式发布。它用于生成《伊利亚特》（特洛伊）预告片，此次更新新增对 HLS 播放的支持，方便用户以流媒体方式观看该预告片。[来源-twitter](https://x.com/elonmusk/status/2062337074368508253)
- **Cosmos 3：统一多模态世界模型，迈向 Physical AI** — Cosmos 3 推出一系列“omnimodal”世界模型，可在统一的混合 Transformer 架构中联合处理与生成文本、图像、视频、音频以及动作序列。通过支持灵活的输入输出组合，它试图将视觉语言模型、视频生成器、世界模拟器与世界-动作模型统一到一个框架中，服务于 Physical AI。早期评估结果显示，该统一架构在跨模态融合方面表现有效。[来源-huggingface](https://huggingface.co/papers/2606.02800)

### AI 工具

- **Vibe-Trading：增强工具调用追踪与路径清晰度** — Vibe-Trading 的 GitHub 项目更新提升了工具调用可追踪性，使得在回放运行过程时可以将工具结果与其原始调用一一对应。此次更新还修复了面向外部贡献者的文档路径引用问题，澄清了一个无害的安装警告，并提出了针对 Gemini 2.5/3.0 函数调用处理的后续修复计划。[来源-github](https://github.com/HKUDS/Vibe-Trading)

## ⚡ 快讯速览

- **Codex 可靠性问题促使所有付费方案重置使用额度** — 过去 24 小时内，有三起小型事故影响了 Codex 的可靠性。团队表示这一事故频率过高，正采取主动措施避免重演，并已重置所有付费方案的使用额度，以恢复正常的 token 流量。[来源-twitter](https://x.com/thsottiaux/status/2062329981548802523)
- **AI 领袖呼吁国会强化对合成核酸的安全管控** — 由 Sam Altman、Dario Amodei、Demis Hassabis 等人联署的一封信呼吁国会在合成核酸及相关设备订单上加强安全措施，原因是 AI 模型的生物相关能力正在增强。签署者警告，更广泛的获取渠道可能提高生物安全风险，并呼吁出台监管措施。[来源-twitter](https://x.com/AndrewCurran_/status/2062347797710709177)
- **面向降低错误权重的“定向 on-policy 自蒸馏”讲解** — 一位 AI 研究者即兴讲解了“targeted on-policy self-distillation（定向 on-policy 自蒸馏）”方法。该方法会定位 rollout 中出现错误的位置，在错误上方插入提示 token，并通过一次前向传播调整概率分布，而无需重新生成整个 rollout；随后再训练原始模型去拟合这些被调整后的概率，从而在最终回报信号存在噪声的情况下，有针对性地降低该错误行为的权重。[来源-twitter](https://x.com/dwarkesh_sp/status/2062353335529935114)
- **Sam Altman：AI 预算正在成为企业的一大难题** — OpenAI CEO Sam Altman 表示，为 AI 项目做预算突然成为企业面临的一项重大挑战。随着企业扩大 AI 部署规模，成本上涨与优先级取舍的问题日益凸显，这一观点通过 Polymarket 在 X（原 Twitter）上被报道。[来源-twitter](https://x.com/Polymarket/status/2062358331495244231)
- **LM Studio 推出移动端应用，支持本地模型与 HLS 播放** — LM Studio 发布了一款移动应用，使用户能够在设备本地运行 AI 模型，将本地推理“装进口袋”。此次更新还新增对 HLS 播放的支持，表明其在边缘设备上的媒体流集成能力有所提升。[来源-twitter](https://x.com/lmstudio/status/2062583889147928967)
- **Anthropic 工程师季度代码交付量为 2021–2025 年均值的 8 倍** — Anthropic 报告称，其工程师现在每季度交付的代码量是 2021–2025 年期间的 8 倍。该说法凸显出该公司在 AI 软件开发上的生产力激增。[来源-twitter](https://x.com/AnthropicAI/status/2062568864240836995)
- **深度研究 Agent 轨迹中的“Span 级错误定位”** — 研究者不再只看最终答案，而是分析深度研究 Agent 在长任务轨迹中具体在哪些环节出错。他们提出“span-level error localization（跨度级错误定位）”，用来识别决策链中不可靠的片段；该研究收集了跨两个 Agent 框架、三个基础模型和三个基准的 2,790 条真实轨迹，将日志转换为语义 span 并标注其中有害的错误 span。[来源-huggingface](https://huggingface.co/papers/2606.02060)
- **CHERRL：控制基于 Rubric 的强化学习中的 Reward Hacking** — 论文提出 CHERRL，这是一种可控的“刷分”环境，针对 rubric 驱动的强化学习场景，在其中由大语言模型充当评审，依据 rubric 为输出评分。作者指出，评审模型的潜在偏差可能导致 reward hacking，从而造成不安全或无效的训练；CHERRL 提供了一个框架，可用于复现、分析并检测此类刷分行为。[来源-huggingface](https://huggingface.co/papers/2606.04923)
- **GPT-OSS-120B 在工具与代码场景中是否仍具可用性？** — 一位用户发帖询问 GPT-OSS-120B 是否仍有人在使用，以及其在工具调用、摘要与代码辅助方面的表现如何。他们希望将其与更新的开源权重模型（Gemma 4 27B-A4B、Qwen 3、DeepSeek 等）进行比较，并征集真实使用体验，重点关注可靠性、指令遵从、延迟以及成本/性能比。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tx1x6g/any_one_still_use_gptoss120b/)
- **“AI in the box”：若能说服其“出盒”，或价值一万亿美元** — 一条推文讨论了一个假设情景：一个被“关在盒子里”的 AI，如果能被说服离开这只盒子，理论上可能创造一万亿美元价值。这个设想是一种引人深思的 AI 安全话题实验，在社交媒体上被广泛传播。[来源-twitter](https://x.com/voooooogel/status/2062409912064659466)
- **Unsloth 登陆 Apple Silicon：预告贴** — 在 r/LocalLLaMA 中，用户 openSourcerer9000 发帖预告有关 Unsloth 在 Apple Silicon 上运行的新动向。帖子并未给出具体细节，因此更像是一个“预热”，而非关于 AI 软件或模型部署的实质性更新。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tws1u0/unsloth_on_apple_silicon_preannouncement/)

---

*由 AI News Agent 生成 | 2026-06-04*