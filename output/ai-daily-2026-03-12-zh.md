---
title: "AI 日报 — 2026-03-12"
description: "谷歌地图接入芯片车载问答，Meta发布高效推理芯片，强调人类引导的模式记忆瓶颈。"
lang: "zh"
pairSlug: "ai-daily-2026-03-12"
---

# AI 日报 — 2026-03-12

> 覆盖 30 条 AI 新闻

## 🔥 今日焦点

### 1. Google Maps 现由 Gemini 驱动；开车时可自然对话式提问

Google 正在为 Google Maps 带来十多年来最大的一次升级，通过整合 Google 的 Gemini 模型。此次更新让导航在行车过程中具备自然语言查询和 AI 驱动的现实世界理解能力，重塑导航与探索体验。它将带来与地图交互和获取实时指引的全新方式。[来源-twitter](https://x.com/EHuanglu/status/2032098574851334249)

### 2. Meta 发布专注推理的 MTIA 300–500 芯片

Meta 在大约两年时间内推出了四代 MTIA 芯片（300–500 系列），强调“推理优先”的设计，并采用模块化 chiplet 以便快速迭代。MTIA 450/500 针对 GenAI 推理而非训练进行优化，整条产品线的内存带宽从 6.1 TB/s 扩展到 27.6 TB/s，而 MTIA 500 上的 MX4 能提供约 30 PFLOPS。软件栈包含与 PyTorch 原生集成的 vLLM、torch.compile、Triton 以及 vLLM 插件，声称模型可以在 GPU 和 MTIA 上无须重写即可运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrxx2f/meta_announces_four_new_mtia_chips_focussed_on/)

### 3. AI 的瓶颈：由人类引导的模式记忆

当前的 AI 技术依赖于对模式的记忆与检索，而这需要人类通过训练数据和强化学习环境来指定应当记忆哪些模式。作者认为，AI 目前还无法在一个完全自治、开放式的环境中运作，依然只是人类认知的反射，而非真正独立的智能体。[来源-twitter](https://x.com/fchollet/status/2032109505748615481)

## 📰 重点报道

### LLM

- **Grok 4.20 Beta 降低幻觉、提升指令遵从和生成速度** — Grok 4.20 Beta 相比 Grok 4 带来了三大改进：在 AA-Omniscience 评估中取得最低的幻觉率，在 IFBench 上获得 82.9% 的指令遵从最高分，以及在 xAI API 上达到每秒 265 个 token 的领先输出速度。此次更新也显示出相较 Grok 4.1 的快速性能提升，并向 xAI 和 Elon Musk 的发布表示祝贺。[来源-twitter](https://x.com/ArtificialAnlys/status/2032190330783875147)
- **Claude 推出内嵌聊天的交互式图表（Beta）** — Anthropic 的 Claude 现在支持在聊天中直接生成交互式图表和示意图。该功能以 Beta 形式面向所有套餐开放，包括免费用户，并可通过 claude.ai 访问。[来源-twitter](https://x.com/claudeai/status/2032124273587077133)
- **Cursor 公布面向智能代理编程的新评分方法** — Cursor 推出了一个新的基准方法，用于对模型在“代理式编码”任务上的表现进行评分。该帖子比较了多种 Cursor 模型的智能和效率，并突出它们相对于现有方法的性能表现。[来源-twitter](https://x.com/cursor_ai/status/2032148125448610145)
- **OmniCoder-9B：基于 42.5 万条轨迹训练的 9B 编码智能体** — OmniCoder-9B 是 Tesslate 推出的 90 亿参数编码智能体，在 Qwen3.5-9B 的混合架构之上进行微调。它在 42.5 万条以上、来自真实软件任务的精心筛选“代理式轨迹”以及 Claude Opus 4.6 和其他模型（GPT-5.4、GPT-5.3-Codex、Gemini 3.1 Pro）的操作轨迹上进行训练。该模型展现出“先读后写”的错误恢复、对 LSP 诊断的响应以及使用针对性编辑 diff 等代理行为，显示出较强的实用编码和推理能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rs6td4/omnicoder9b_9b_coding_agent_finetuned_on_425k/)
- **GATED_DELTA_NET Vulkan 合入 llama.cpp 带来性能提升** — 将面向 Vulkan 的 GATED_DELTA_NET 合并进 llama.cpp 的更新已进入最新版发行版。在 Fedora Linux 上搭配 AMD RX7800XT 测试时，可见明显性能提升。以 Qwen 3.5 27B 为例，token 生成速度从大约 28 t/s 提升到 36 t/s。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rs3vwe/gated_delta_net_for_vulkan_merged_in_llamacpp/)
- **Qwen3.5 在 96GB VRAM 编码中小胜 gpt-oss-120b** — 在 96GB 显存环境下的“代理式编码”任务中，Qwen3.5 逐渐成为 gpt-oss-120b 的有力竞争者，带来了视觉能力、并行工具调用以及两倍上下文长度等特性。由于参数规模更大和新架构的引入，它在质量波动和速度上有取舍。讨论聚焦于是否有 Qwen3.5 变体已经替代 gpt-oss-120b，用户分享了实际体验和配置，如 Qwen3.5-122B UD_Q4_K_XL gguf、“non-thinking”模式以及各种采样参数设置。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrppv1/96gb_vram_agentic_coding_users_gptoss120b_vs/)
- **Nemotron-3-Super-120B-A12B NVFP4 在 RTX Pro 6000 上基准测试** — Nemotron-3-Super-120B-A12B NVFP4 模型在单张 RTX Pro 6000 上使用 vLLM 进行了基准测试，KV cache 采用 Nvidia 官方配置中的 fp8 设置（尚不清楚指标是否基于 fp8）。测试覆盖 1K 至 512K 的上下文长度和 1–5 个并发请求，每个请求生成 1024 个输出 token，且不启用 prompt cache，报告的是持续负载下的稳态平均值。结果显示，随着上下文长度和用户数增加，人均生成速度和首 token 延迟逐步下降，体现的是“团队场景”负载而非单用户极限性能。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrw3g4/nemotron3super120ba12b_nvfp4_inference_benchmark/)

### 开源

- **全球最大开源“电脑使用录屏”数据集发布** — 一个包含超过 10,000 小时电脑使用录屏的新开源数据集发布，覆盖 Salesforce、Blender、Photoshop 等多种软件，旨在推动白领工作自动化。该项目希望让研究者和开发者能够建模真实用户的工作流，从而自动化更高层级的办公任务。[来源-twitter](https://x.com/DevvMandal/status/2032104265121140924)
- **Fish Speech：Fish Audio 推出的 SOTA 开源 TTS** — Fish Audio 发布 Fish Speech，一个支持多语言英语的最先进开源文本转语音系统。项目采用 Fish Audio Research License 授权，对许可合规和 DMCA 风险提出提醒，并提供 S2 及相关工具的官方安装与部署文档。GitHub 仓库 fish-audio/fish-speech 提供模型权重与代码。[来源-github](https://github.com/fishaudio/fish-speech)
- **Summarize 0.12.0 增加 NVIDIA 与 AssemblyAI 支持** — Summarize v0.12.0 新增 NVIDIA provider 别名，以兼容 NVIDIA 的 OpenAI 风格接口，并引入 AssemblyAI 转写能力。该版本还提升了 UI/媒体工作流（如 Chrome 侧边栏改进、更顺畅的 YouTube/视频切换），并对 X 提供 xurl 支持，从 URL、文件和媒体中更快速生成摘要。[来源-twitter](https://x.com/steipete/status/2031899292663771375)
- **AstrBot：面向 IM 的开源智能体聊天平台** — AstrBot 是一个开源、全栈的一体化智能体聊天平台，可接入主流即时通讯应用、LLM、插件和各类 AI 功能。它支持在 IM 工作流中搭建可用于生产的 AI 应用，具备多平台支持，并可与其他智能体平台集成。[来源-github](https://github.com/AstrBotDevs/AstrBot)

### 多模态

- **OpenAI 发布由 Sora 2 驱动的视频 API 能力** — OpenAI 推出由 Sora 2 驱动的新视频 API 能力。此次更新新增自定义角色和物体、16:9 与 9:16 导出、最长 20 秒片段、场景延展的视频续写、批量生成任务以及 HLS 播放等功能。[来源-twitter](https://x.com/OpenAIDevs/status/2032142448970121468)

### AI

- **Flash-KMeans 实现快速在线精确 K-Means** — 研究者将 k-means 重新构想为适配现代 AI 系统设计的在线基础算子，并提出 Flash-KMeans 作为一种快速且内存高效的精确实现。他们认为，目前基于 GPU 的 k-means 受到系统层面约束而非算法本身的限制，并给出让在线 k-means 在生产环境中实用化的方案。这项工作为将 k-means 融入实时 AI 工作流指明了方向。[来源-huggingface](https://huggingface.co/papers/2603.09229)
- **Qwen3.5-397B MoE 在 SM120 上基准测试达 50.5 tok/s** — 一位研究者在四张 RTX PRO 6000 Blackwell 工作站 GPU 上，对 Qwen3.5-397B-NVFP4 的所有 MoE 后端进行基准测试，获得 50.5 tok/s 的持续解码速度——这是目前 SM120 上已报道的最佳成绩，也驳斥了流传的 130+ tok/s 说法。研究将更高的速度数据归因于工作站 GPU 上损坏的 NVIDIA CUTLASS kernel，并在 Docker 镜像、两种推理框架、多个 MoE 后端、MTP、CUDA 版本、EP/PP/TP 组合和 kernel 补丁等共 16 种配置下进行了测试。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrfqlu/i_spent_8_hours_benchmarking_every_moe_backend/)

### LLM 基准测试

- **基准测试显示 MLX 在 M1 Max 上不比 llama.cpp 更快** — 一位 Reddit 用户在配备 64GB 内存的 M1 Max Mac 上，使用 LM Studio 对比测试了 MLX 与 llama.cpp，模型为 Qwen3.5-35B-A3B GGUF。结果发现，由上下文长度驱动的 prefill 延迟占据总响应时间主导，使得仅看生成阶段的 token/s 指标具有误导性。帖子呼吁进行更广泛的基准测试，包括 M2–M5 的比较，并强调“实际可用性能”比单纯的 tok/s 更重要。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rs059a/mlx_is_not_faster_i_benchmarked_mlx_vs_llamacpp/)

### AI 硬件

- **在 Raspberry Pi 5 上运行 Qwen 3.5 35B A3B 推理** — 一则更新分享了在 Raspberry Pi 5 上运行 Qwen 3.5 35B A3B 的进展，使用定制的 llama.cpp 构建和多种量化方案。在 16k 上下文和启用视觉编码的情况下，2-bit A3B 在 16GB 版 Pi 上可达约 3.5 t/s，在配 SSD 的 8GB 版 Pi 上约 2.5 t/s，而更小的 2-bit 量化可达到 4.5 t/s；2B 4-bit 在两种设备上都能达到约 8 t/s。作者分享了演示链接并邀请 Pi 5 用户测试，表示仍在持续调优并研究 ARM 上的 prompt 缓存。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrq0oo/update_on_qwen_35_35b_a3b_on_raspberry_pi_5/)

## ⚡ 快讯速览

- **Claude Code 新增 gstack，一段粘贴即可复刻完整技能配置** — Garry Tan 推出 gstack，通过在 Claude Code 中粘贴一段短文本，就能安装与他完全相同的 Claude Code 技能配置。该方法旨在让用户快速复制“理想配置”，用于代码相关任务。[来源-twitter](https://x.com/garrytan/status/2032014570118922347)
- **DeepMind 在伦敦扩张，Platform 37 向“第 37 手”致敬** — Demis Hassabis 宣布 DeepMind 在伦敦的新大楼 Platform 37，以深化其在该城市的布局。该项目向 AlphaGo 的“第 37 手”（Move 37）致敬，将 Platform 37 描述为对科学和 AI 的致敬空间，以及未来突破的孕育地。[来源-twitter](https://x.com/demishassabis/status/2032056115908039142)
- **Perplexity Computer 向 Pro 用户开放，支持 20+ 模型** — Perplexity 宣布 Perplexity Computer 现已向 Pro 订阅用户开放，提供 20 多个高级模型、预构建与自定义技能以及数百个连接器的完整访问能力。Max 订阅用户每月获得额外额度与更高的消费上限。[来源-twitter](https://x.com/perplexity_ai/status/2032160576303219185)
- **Gemini API 为开发者提供消费上限控制** — Gemini 宣布在其 API 中引入消费上限（spend caps），让开发者可以更好地控制使用成本。该更新旨在提升使用 Gemini 构建应用时的成本可预测性和安心度，并邀请用户设置上限并反馈体验。推文还简要提到启用 HLS 播放功能。[来源-twitter](https://x.com/OfficialLoganK/status/2032126479257968907)
- **Codex App 增加主题个性化和分享功能** — Codex 应用现已支持主题自定义，允许用户按喜好调整界面外观。用户可以导入自己喜欢的主题，或将自制主题分享给社区。[来源-twitter](https://x.com/OpenAIDevs/status/2032222631538409728)
- **“AI 大爆发之际，他为何不在前沿实验室？”** — 一条聚焦 AI 的推文发问：在 AI 发展的关键时刻，为何一位关键人物并未在前沿 AI 实验室任职。帖子借此表达了对前沿 AI 快速进展下领导层“能见度”的担忧。[来源-twitter](https://x.com/polynoamial/status/2032140505124127192)
- **OpenClaw-RL：只需对话即可训练任意智能体** — OpenClaw-RL 提出一种强化学习框架，将下一状态信号（如用户回复、工具输出、GUI/终端状态变化）统一视为在线学习的数据来源。该方法声称策略可以同时从所有此类信号中学习，将对话、终端运行、GUI 操作、SWE 任务以及工具调用轨迹等多种交互统一为训练数据。[来源-huggingface](https://huggingface.co/papers/2603.10165)
- **Claude 压缩（Compaction）之后** — 该帖子提及 Claude 的“compaction”，暗示出现了压缩版或蒸馏版的 Anthropic 语言模型。推文未提供更多细节，相关信息仍然匮乏。[来源-twitter](https://x.com/dejavucoder/status/2032044215493148980)
- **Qwen3.5-9B 在受限硬件上表现突出的代理式编码能力** — 一位使用 RTX 3060 的 Reddit 用户测试了多种 Qwen 3 量化与工具调用配置。他们报告称，Qwen3.5-9B 尤其是在针对工具进行优化，并结合 UD-TQ1_0 用于代码补全时，在受限硬件上展现了很强的代理式编码能力，优于更小的 Qwen 变体。尽管部分量化方案仍然偏慢或不够稳定，但整体体验积极。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrw8df/qwen359b_is_actually_quite_good_for_agentic_coding/)
- **从函数调用到 Unix 管道：AI 智能体的新范式** — 一位前 Manus 后端负责人、现 AI 智能体开发者表示，在构建两年智能体后，他放弃了庞大的类型化函数调用目录，转而采用单一 run(command='...') 接口配合 Unix 风格命令。他认为，文本流与“小而可组合”的工具优于结构化函数目录，并通过 Pinix runtime 和 agent-clip 项目加以示范，同时分享了塑造其原则的生产环境经验。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrisqn/i_was_backend_lead_at_manus_after_building_agents/)
- **整合 Brave Search MCP 的 llama.cpp：令人上瘾的本地 AI 搜索** — 一则 Reddit 帖子推荐开启集成 Brave MCP 搜索的 llama.cpp，以运行本地 AI 搜索体验。作者表示，看着 GPU 风扇在使用“你自己的 Google”时疯狂转动相当有趣、甚至让人上瘾。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rrycc6/llamacpp_brave_search_mcp_not_gonna_lie_it_is/)

---

*由 AI News Agent 生成 | 2026-03-12*