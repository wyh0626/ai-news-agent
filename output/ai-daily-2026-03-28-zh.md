---
title: "AI 日报 — 2026-03-28"
description: "VibeVoice开源ASR+Transformer；本地达云端；演示零日。"
lang: "zh"
pairSlug: "ai-daily-2026-03-28"
---

# AI 日报 — 2026-03-28

> 覆盖 30 条 AI 新闻

## 🔥 今日焦点

### 1. VibeVoice ASR 开源，并集成 Transformers

微软的 VibeVoice 开源了 VibeVoice-ASR，这是一个统一的语音转文本模型，可以一次性处理 60 分钟音频，并输出结构化的转写结果（Who, When, What），同时支持用户自定义上下文。它支持 50 多种语言，并已通过 Hugging Face Transformers 提供，附带微调代码和 vLLM 加速支持。此次发布还配有一篇技术报告。 [来源-github](https://github.com/microsoft/VibeVoice)

### 2. 3-bit KV cache 让 MacBook 本地推理媲美云端 AI 质量

一位 M2 MacBook 用户报告称，在应用 3-bit KV cache 压缩后，本地 AI 推理效果与云端服务相当，并能进行 10 万 token 的长对话，质量与云服务等同。此前他们每月为云端 AI API 支付 200 美元，如今已取消全部订阅从而节省费用。该优化参考了一篇免费论文中的算法和一篇 TurboQuant 的解析文章。 [来源-twitter](https://x.com/k1rallik/status/2037936518862446694)

### 3. Anthropic 的 Claude 在大会演示中展示零日漏洞挖掘能力

在一次现场大会演示中，Anthropic 展示了 Claude 在 Ghost 和 Linux 内核中定位零日漏洞的过程。演示声称 Claude 在 90 分钟内识别出一次盲 SQL 注入，并疑似窃取了一个管理员 API 密钥，突出了 AI 辅助网络安全的能力。 [来源-twitter](https://x.com/chiefofautism/status/2037951563931500669)

## 📰 重点报道

### LLM

- **GLM-5.1 将会开源，李子璇确认** — 李子璇在推文中表示 GLM-5.1 将会以开源形式发布。该帖一方面安抚关注者不要紧张，另一方面也释放出 GLM-5.1 模型即将开源的信号。 [来源-twitter](https://x.com/Zai_org/status/2037726285900742790)
- **TurboQuant 登陆 MLX：4.6 倍 KV cache 压缩** — TurboQuant 已在 MLX 上实现，采用融合 Metal 内核来加速 KV cache 压缩。在一台搭载 48GB 内存的 M4 Pro 上，以 Qwen2.5-32B 进行测试，达成了 4.6 倍压缩，推理吞吐为 FP16 的 0.98 倍且质量一致；在 16K 上下文长度下，KV cache 从 4.2GB 缩减到 897MB。该工作包含技术说明、开源代码以及一个 MLX-LM 的 PR。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5vhf6/turboquant_on_mlx_46x_kv_cache_compression_with/)
- **LLM 能为双方辩护，帮助形成观点** — 一位博主撰写文章草稿，并在数小时内反复借助 LLM 加强论证。模型能令人信服地为议题的双方提供论点，甚至反驳原有立场，展示出 LLM 在激发和探索观点方面的作用。读者认为它是塑造个人看法的有用工具，同时提醒要避免偏见和“拍马屁式”迎合。 [来源-twitter](https://x.com/karpathy/status/2037921699824607591)
- **LLM 与人类文本：检测中的线性可分性** — 一位正在训练自定义 AI 检测模型的用户发现，在大多数情况下，LLM 生成文本与人类撰写文本在特征空间中呈线性可分。如果这一发现得到验证，简单分类器就有可能区分 AI 写作和人类写作，这将影响检测工具与安全讨论。 [来源-twitter](https://x.com/liquiditygoblin/status/2037709825824694417)
- **Hermes Agent v0.5.0 上线，通过 Nous Portal 接入 400+ 模型** — Hermes Agent v0.5.0 已上线，本次更新重点是优化、性能提升、代码清理以及基础能力建设。Nous Portal 目前已提供 400 多个模型，完整接入 HuggingFace 的模型套件。GPT-5.4 被“趣味性地敲了一下脑袋”（bonk）以鼓励其响应更积极，同时对 Nix 环境也做了改进。 [来源-twitter](https://x.com/Teknium/status/2037987210478383161)
- **Qwen 3.5 27B Dense 搭配 Hermes Agent 表现亮眼** — 一条推文称赞 Qwen 3.5 27B（Dense）在与 Hermes Agent 搭配时的表现。帖子认为该组合展现出很强的能力，突显了 AI Agent 与工具调用方面的进展，也反映出业界对将先进 LLM 与自治 Agent 深度集成的持续兴趣。 [来源-twitter](https://x.com/TheAhmadOsman/status/2037712643528482905)
- **突发：llama-server 迁移到 HuggingFace cache，导致脚本失效** — 一位 Reddit 用户报告称，最新构建的 llama-server 会触发一次性迁移，将旧版 llama.cpp 缓存迁移至 HuggingFace cache。迁移会将使用 -hf 下载的模型移动并把 .gguf 模型转换为 blob，从而破坏依赖旧文件路径的启动脚本和模型管理流程。使用 --model-url 下载的模型不受影响，但诸如“failed to load model”之类的报错说明此次变更带来了干扰。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s62el8/breaking_change_in_llamaserver/)
- **Nemotron 3 Super：在 llama.cpp 与 vLLM 之间存在巨大质量差距** — 一份私下基准测试显示，Nemotron 3 Super 在不同推理后端上的结果差异较大。在约 400 道问题的测试中，vLLM 的准确率为 55.4%，而 llama.cpp 仅为 40.2%，表明这两种 LLM 执行引擎之间存在显著质量差距。除与 gguf 相关的差异外，日志看上去都较为正常，整体结果也与其他大模型相近。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s69tfk/nemotron_3_super_large_quality_difference_between/)

### 开源

- **Cohere 将 SOTA 开源转写模型带入浏览器端** — Cohere 已经让一款最先进的开源语音转写模型可以直接在浏览器中运行。模型权重已在 HuggingFace 上提供，并附有链接，同时支持 HLS 播放。 [来源-twitter](https://x.com/nickfrosst/status/2037914966305493286)
- **AI Scientist-v2 通过 Agentic Tree Search 实现自动化科学发现** — AI Scientist-v2 是一个通用的端到端 Agentic 系统，能够自主生成假设、运行实验、分析数据并撰写科学论文。它被视为一个里程碑：首篇完全由 AI 撰写并通过同行评审接收的研讨会论文。与前代相比，它移除了人为编写的模板，可以在不同 ML 领域中泛化，并采用由实验管理器引导的渐进式 agentic tree search。该项目已在 GitHub（SakanaAI/AI-Scientist-v2）开源，并与 ICLR2025 的研讨会相关联。 [来源-github](https://github.com/SakanaAI/AI-Scientist-v2)
- **Onyx 开源 AI 平台：自部署聊天 UI** — Onyx 是一个可自部署的开源 AI 平台，提供与任意 LLM 兼容的聊天 UI。它包含自定义 Agents、Web 搜索、RAG 以及连接 40 多种知识源等功能，并可在物理隔离（airgapped）环境中运行。该项目强调通过一条命令即可轻松部署，并能广泛互操作外部数据源。 [来源-github](https://github.com/onyx-dot-app/onyx)

### 硬件

- **每周更新：适合你硬件的最佳 AI 模型** — 这是一个每周系列，列出可在不同硬件档位（8GB、16GB、24GB）上运行的 AI 模型，并提供示例模型和 Hugging Face 链接。它重点介绍轻量级自动补全、多模态选项和强大的 Agent 能力模型，如 Qwen 3.5 和 NVIDIA Nemotron-3-Nano-4B-GGUF，强调其开源可用性。帖子倡导开放科学，并邀请读者关注持续的每周精选。 [来源-twitter](https://x.com/0xSero/status/2037837722094641610)

### AI 研究

- **Calibri：通过参数高效校准提升 Diffusion Transformers** — 研究者展示，仅一个可学习的缩放参数就能在去噪过程中显著改善 Diffusion Transformer（DiT）模块的表现。随后他们提出 Calibri，这是一种参数高效的校准方法，用于优化 DiT 各组件、提升生成质量，并将 DiT 校准问题构建为黑盒优化任务。 [来源-huggingface](https://huggingface.co/papers/2603.24800)

## ⚡ 快讯速览

- **AI 将用户“推向中间”：Grok 偏右但仍具去极化效应** — 新分析表明，在所研究的多个模型中，AI 模型整体上会通过将人们的观点“推向政治中间地带”来降低两极化。Grok 展现出比其他模型更明显的右倾偏见，但依然产生去极化效果。文章署名为 @jburnmurdoch。 [来源-twitter](https://x.com/StefanFSchubert/status/2037795164186390769)
- **Codex Use Cases 画廊将技能扩展给所有人** — OpenAI 推出 Codex Use Cases，这是一个涵盖编程与非编程任务的实用示例画廊，展示 Codex 在真实场景中的使用方式。合集为每个用例提供起始提示，并可直接在 Codex 应用中打开。 [来源-twitter](https://x.com/gdb/status/2037732675897770123)
- **大厂与初创公司每天在 LLM tokens 上花费超 1000 美元** — 有消息称，大型科技公司和初创公司每天在 Claude Code 或 Codex tokens 上的支出超过 1000 美元，年化约为 36.5 万美元。如果这一趋势持续，token 成本可能会超过对人类员工的支出，凸显出 AI 工作流中日益壮大的 token 经济。 [来源-twitter](https://x.com/Yuchenj_UW/status/2037938224535155046)
- **本地 16GB 内存可运行的代码自动补全模型亮相** — 有帖子重点介绍了一款可在本地、且设备内存为 16GB 或以下系统上运行的代码自动补全模型。示例指向 Hugging Face 上的 zed-industries/zeta-2，这是一个能力不错的开源选项，尽管尚不如 Cursor tab 强大。帖子强调 Hugging Face 推广的开源与开放科学价值观。 [来源-twitter](https://x.com/0xSero/status/2037693094754213897)
- **闭源模型从开源模型获利却不回馈生态** — 这条推文认为，专有（闭源）AI 模型从开源模型中受益，却不以开放分享或贡献的方式回馈。它将这一动态视为伦理和生态系统问题，凸显了 AI 行业在开放性与商业激励之间的紧张关系。 [来源-twitter](https://x.com/ylecun/status/2037891419197628608)
- **开源 Deep-Live-Cam 实现实时换脸** — 开源项目 Deep-Live-Cam 2.1 能够基于单张图像实现实时换脸与视频深度伪造。开发者强调要负责任地使用该工具，并内置安全检查、伦理准则以及在法律要求时添加水印或关闭功能的可能性。 [来源-github](https://github.com/hacksider/Deep-Live-Cam)
- **IBM Granite-4.0-3B-Vision 支持多模态文档抽取** — Granite-4.0-3B-Vision 是一款为企业级文档数据抽取而设计的视觉-语言模型，专注于图表、表格抽取以及语义键值对抽取等难点任务。它以 LoRA adapter 的形式构建在 Granite 4.0 Micro 之上，使单次部署即可同时支持多模态文档理解和纯文本工作负载；基础模型在无需加载 adapter 的情况下可处理纯文本请求。该模型支持 Chart2CSV、Chart2Summary 和 Chart2Code，并能以 JSON、HTML 或 OTSL 格式输出结果。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6axvb/ibmgranitegranite403bvision_hugging_face/)
- **AI 功能炒作周期：狂热、退化、重复** — 一篇 Reddit 帖子认为，AI 功能发布遵循固定的炒作周期：最初是极具震撼力的演示，随后进入输出质量退化但宣传仍继续、却不正视缺陷的第二阶段。帖子举例提到 VEO 3、逼真的图像编辑和 GPT-5.4，认为公司不断推出新功能以重置这一周期。文章将这一模式视为系统性问题，而非偶然现象，并呼吁对炒作保持怀疑态度。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5te4q/the_ai_releases_hype_cycle_in_a_nutshell/)
- **不要使用混合 KV cache 量化** — 一篇 Reddit 帖子反对通过混合 KV cache 量化来在节省内存的同时维持精度。作者引用了一组基准测试，并附上长文博客解释该方法为何不正确，重点讨论在 Vulkan 后端上针对 qwen35 9B 模型使用 Q6_K / Q8_0 的配置，在不同 batch size 与设置下的吞吐结果，这些结果与该方法宣称的收益相矛盾。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6a488/do_not_use_mixed_kv_cache_quantization/)
- **Qwen 3.5 在用于打码的 OCR 边界框任务中表现可期** — Qwen 3.5 在用于打码流程的 OCR 边界框准确性方面进行了测试，此前曾测试过 Qwen 3 VL 8B Instruct。评测覆盖 4 个可在 24GB VRAM 以内运行的 Qwen 模型，在 3 个与手写相关的高难度任务上进行评估，并使用 doc_redaction 仓库；初步结果显示，在用于打码的手写文本 OCR 上具有改进潜力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6cmll/testing_qwen_35_for_ocr_and_redaction_tasks/)
- **llama.cpp 在卸载到 CPU 时预取权重** — 一个针对 llama.cpp 的实验性 PR 增加了在将计算卸载到 CPU 时的权重预取机制，旨在减少密集模型和较小 MoE 模型在处理提示阶段的内存瓶颈。作者表示，该改动在内存充足但 GPU 资源有限的配置上带来了好处，并邀请其他人试用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s5xcmw/llamacpp_prefetching_weights_when_offloading_to/)
- **Turbo3 与 gfx906 分支合并进 Llamacpp，支持 Qwen 3.5 122B** — 一位开发者对 llamacpp 进行了新的 fork，将 Turbo3 和 gfx906 分支合并，使得可以运行 Qwen 3.5 122B。该配置 reportedly 能在四块 16GB 的 MI50 GPU 上运行。更新由 Reddit 用户 Exact-Cupcake-2603 分享。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s67k6v/turbo3_gfx906_4_mi50_16gb_running_qwen35_122b/)
- **TurboQuant 解析：用于减小内存占用的向量量化** — 一篇 Reddit 解释文章指出，TurboQuant 是一种用于降低内存使用的向量量化算法。文中强调，该方法的核心在于对向量进行量化，而不是依赖极坐标，并通过一个简单的“截断数字”示例来说明，同时指出更复杂的方案（如分块分组）也已存在。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s62g5v/a_simple_explanation_of_the_key_idea_behind/)
- **为何 TurboQuant 的热度被夸大了** — 一篇 Reddit 帖子质疑围绕 TurboQuant 的高热度，认为它在上下文适配方面可能只带来边际改进。作者将其与已经非常高效的混合模型进行对比，并指出社区中围绕其发布时间表及与 llama.cpp 和自定义实现集成的广泛讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s658kv/whats_with_the_hype_regarding_turboquant/)

---

*由 AI News Agent 生成 | 2026-03-28*