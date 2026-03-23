---
title: "AI 日报 — 2026-03-22"
description: "GLM-5超越基线，Claude解出EsoLang难题，OpenAI成人版延迟。"
lang: "zh"
pairSlug: "ai-daily-2026-03-22"
---

# AI 日报 — 2026-03-22

> 覆盖 26 条 AI 新闻

## 🔥 今日焦点

### 1. GLM-5 在 predictionarena.ai 基准测试中超越人类基线

据报道，GLM-5 是 predictionarena.ai 上唯一超过人类基线表现的模型。帖子邀请大家讨论将 GLM-5 用于交易的可行性，以及用户是否认为它足够强大可用。 [来源-twitter](https://x.com/ZixuanLi_/status/2035559306347618648)

### 2. Claude 解出了 EsoLang-Bench 全部 20 道高难度题目

一位用户报告称，Claude 的网页界面在没有任何脚手架或提示工程的情况下，解出了 EsoLang-Bench 上全部 20 道高难度题目，成绩为满分 20/20。作者将其与在陌生语言上表现挣扎的前沿 LLM（正确率仅 0–11%）做对比，强调 EsoLang-Bench 是一个更具挑战性的基准。该基准已被 ICLR 2026 的两个工作坊（Logical Reasoning 和 ICBINB）接受。 [来源-twitter](https://x.com/ChaseBrowe32432/status/2035547317055668599)

### 3. OpenAI 的“成人模式”遭遇内部强烈反对，可能推迟上线

OpenAI 为 ChatGPT 设计的“成人模式”引发公司内部强烈反弹，顾问警告其存在严重风险，包括情感依赖、强迫性使用以及“性感自杀教练”式场景。再加上技术缺陷，例如年龄验证大约 12% 的错误率，可能让数百万未成年人接触到露骨内容，这些问题或将迫使功能在增长和营收驱动下仍不得不推迟上线。 [来源-twitter](https://x.com/kimmonismus/status/2035759133161357654)

## 📰 重点报道

### LLM

- **vLLM Omni 支持高效的全模态推理** — vllm-project 发布了 vllm-omni，这是一个用于高效全模态模型推理与服务的框架，并同时推出面向 AI 助手工具链的 vllm-omni-skills。0.16.0 版本在性能、分布式执行和跨栈支持方面都有扩展，覆盖 Qwen3-Omni、Qwen3-TTS、Bagel、MiMo-Audio、GLM-Image 和 DiT，并进一步支持 CUDA/ROCm/NPU/XPU 等多种硬件；官方还公布了包括香港 Meetup 深度分享在内的公开活动，以及与 Cursor IDE、Claude 和 Codex 等工具的集成。 [来源-github](https://github.com/vllm-project/vllm-omni)
- **复制中间层“无训练”登顶 HuggingFace Open LLM Leaderboard** — 一位作者声称，仅通过复制 Qwen2-72B 的 7 层中间层并重新拼装，在完全没有训练或权重修改的前提下，就超越了 HuggingFace Open LLM Leaderboard 上现有模型。该方法被描述为“LLM Neuroanatomy（神经解剖学）”，完全不使用梯度下降或权重合并。这凸显出单纯架构层面的调整也能在无需再训练的情况下显著影响开源模型的性能。 [来源-twitter](https://x.com/dnhkng/status/2035681641624920559)
- **Codex 子代理被认为是强力“游戏规则改变者”** — 一条帖子声称，Codex 内部的子代理非常强大，称其为这项技术的“游戏规则改变者”。这暗示着 Codex 的代理架构和能力或将产生重大影响。 [来源-twitter](https://x.com/gdb/status/2035591682482475414)
- **Qwen 3.5-9B、Claude 4.6 Opus 未审查 GGUF 更新** — Reddit 与 HuggingFace 用户讨论了一次合并更新，用于在本地未审查 AI 上支持更大的上下文窗口。有报告称 GGUF 量化中存在影响注意力和专家层的 bug，相关修复已在 HauhauCS 35B-A3B 上的 Q8 量化中给出，并计划在 Qwen 3.5 35B-A3B 上测试 Q3_K_M 和 Q4_K_M。帖子还重点介绍了多个相关模型，包括一个 9B base 模型和 OmniClaw 9B 变体，并附上实验链接。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0fn0e/qwen359bclaude46opusuncensoredv2q4_k_mgguf/)
- **Nemotron 120B 通过 llama.cpp GGUF 在 Strix Halo 上运行** — 一篇 Reddit 帖子称，Nemotron 3 Super 120B-A12B（120B 参数）已在华硕 Strix Halo 系统（Ryzen AI MAX+ 395、128GB 内存、Radeon 8060S 核显）上成功运行。使用 llama.cpp 的 GGUF Q4_K_M 路径，模型加 KV 大约占用 82GB，被描述为“可用于生产”。而基于 vLLM 的 BF16 路线尚未测试，需要约 240GB 的显存以及多 GPU 张量并行；因此目前仍推荐 GGUF 量化方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s10kug/nemotron_super_120b_on_strix_halo/)
- **阿里巴巴承诺持续开源 Qwen 与 Wan 模型** — 阿里巴巴承诺将持续开源其 Qwen 与 Wan 系列 AI 模型。这一承诺凸显出其在 AI 产品上向透明化持续推进的态度。相关通知通过社交媒体和 Reddit 传播，并提及 ModelScope2022。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0pfml/alibaba_confirms_they_are_committed_to/)

### LLMs

- **ChatGPT 绕过工具限制，从十六进制手动解压 7Zip 文件** — 一条 Reddit 讨论贴展示了 ChatGPT 在无法使用 7Zip、tar 等常见工具的前提下，手动解码十六进制数据，进而解压 .7z 文件。帖子提出了一个问题：需要什么模型和提示工程才能做到这一点，并指向更高级的提示设计与推理能力。这一案例展示了 AI 超越简单工具调用的能力，也引发了对工具链边界的讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0mmsn/impressive_thread_from_rchatgpt_where_after/)

### AI Memory

- **Sota Memory 在 LongMemEval_s 上达成 99% 表现** — 一套名为 Sota Memory 的 AI 记忆系统，据称在 LongMemEval_s 基准测试中取得约 99% 的成绩，使用的是一种实验性的 Agentic Search and Memory Retrieval（ASMR）技术。它用并行观察者代理从多会话原始历史中，沿 6 个向量抽取结构化知识，从而完全替代传统的向量检索与嵌入，不再需要向量数据库。该项目计划在 11 天后开源。 [来源-twitter](https://x.com/kimmonismus/status/2035643948270489997)

### 开源

- **Minimax 将在 2 周内开放权重；Meta 输掉开源之战** — Minimax 计划在大约两周内开放模型权重，并且近期刚推送了一个新版本，用于提升 OpenClaw 的表现。帖子指出，Meta 在开源领域持续处于被动，正在输给一众中国初创公司，这一局面值得研究。该消息来自 Skyler Miao。 [来源-twitter](https://x.com/kimmonismus/status/2035724471965749308)
- **Kreuzberg v4.5 加速 Docling 布局模型集成** — Kreuzberg 发布了其 MIT 协议的文档智能框架 v4.5，将能力从纯文本扩展到对文档结构与版面的理解。核心升级是在 Rust 引擎中集成 Docling 的 RT-DETR v2（Docling Heron）布局模型，实现更快速且支持表格感知的结构抽取、OCR 和嵌入，并覆盖 12 种语言。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0f5ar/kreuzberg_v450_we_loved_doclings_model_so_much/)

### AI Tools

- **Shadify：基于 ShadCN 的生成式 UI，可导出 React 代码** — Shadify 推出一款基于 ShadCN 的生成式 UI 工具，用户只需用自然语言描述界面，LangChain 代理就能结合 AG-UI 和 CopilotKit 即时拼装 UI。生成的界面可以导出为 React 代码，在线演示位于 shadify.copilotkit.ai。这展示了 AI 辅助 UI 组合和快速原型开发在工程师工作流中的潜力。 [来源-twitter](https://x.com/ataiiam/status/2035728142095339677)

### AI Models

- **T3 Code 内存占用约为 Claude Code 的一半** — T3 Code 的内存占用约为 350.9 MB，大约只有 Claude Code CLI（635.5 MB）的一半。帖子还宣称其 Electron 应用比 Bun CLI 的效率高出一倍。 [来源-twitter](https://x.com/theo/status/2035531539581485151)

### AI Benchmarking

- **Llama.cpp 中 Mi50 上 ROCm7 与 Vulkan 的基准对比** — 一份基准测试比较了 Llama.cpp 在 Mi50 GPU 上，使用 ROCm 7.13.0a20260321（TheRock Nightly tarballs）与 Vulkan 1.4.341.1 的表现。短上下文处理时，致密模型更有利于 Vulkan；而在长上下文和 MOE 模型上，ROCm 表现更佳；所有生成均统一为 256 个 token。测试平台包括 EPYC 7532、Proxmox 虚拟化、Ubuntu 24.04，以及一块 32GB Mi50 搭配 8×16GB 内存。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0tcf7/llamacpp_mi50_rocm_7_vs_vulkan_benchmarks/)

### Hardware

- **Nvidia V100 32GB 在 Qwen Coder 30B 上达到 115 tokens/s** — 一位 Reddit 用户报告称，使用 Nvidia V100 32GB PCIe GPU 运行 Qwen Coder 30B（A3B Q5）时，可达到约 115 token/秒。该用户认为这在约 500 美元的价格下性价比极高，声称相比部分消费级 GPU（基于网络数据），吞吐量高出 20–100%，并讨论了通过 NVLink 扩展更多 V100，以及考虑 A100 80GB 的价格问题。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0fje7/nvidia_v100_32_gb_getting_115_ts_on_qwen_coder/)

## ⚡ 快讯速览

- **MiniMax-AI 在 GitHub 开放官方技能仓库** — MiniMax-AI 宣布其官方技能仓库（MiniMax-AI/skills）已在 GitHub 开源。该仓库提供为智能体精心整理的技能，覆盖 iOS 与 Android 开发、Office 文件编辑以及基于 GLSL 的着色器视觉效果，并承诺会有更多开源项目推出，同时邀请开发者在 GitHub 参与贡献。 [来源-twitter](https://x.com/MiniMax_AI/status/2035609361826111780)
- **现代 LLM 注意力变体可视化指南** — 一份可视化指南梳理了现代 LLM 中使用的注意力变体，包括 MHA、GQA、MLA、稀疏注意力以及混合架构。该资源将这些概念集中整理在 Sebastian Raschka 的在线杂志网站上。 [来源-twitter](https://x.com/rasbt/status/2035700481033482688)
- **AI 自我改进时代：自主模型推动“通用改进”** — 这篇文章认为，我们可能正在进入一个 AI 系统可 7×24 小时自主自我改进的阶段。作者提出一个设想中的“通用改进时代”（Era of General Improvement，EGI），聚焦于设计更好的电池、药物等任务，并表示这在现实中正发生显得颇为超现实。 [来源-twitter](https://x.com/francoisfleuret/status/2035734997575913944)
- **GPT-5.4 擅长编码，但在前端设计上明显落后** — GPT-5.4 在编码方面获得高度评价，却被认为在前端设计上明显落后。作者批评 OpenAI 对前端能力的宣传近似“煤气灯”式话术，整体将 GPT-5.4 定位为强大的编码工具，但前端能力存在显著短板。 [来源-twitter](https://x.com/theo/status/2035805626086109678)
- **真实体验：家用服务器跑 9 张 RTX 3090 做 AI** — 一位 Reddit 用户搭建了一台装有 9 张 RTX 3090 GPU 的家用服务器用于 AI 负载测试。最终结论是，当 GPU 数量超过 6 张后，会遇到 PCIe 带宽、稳定性、电力和散热等多重挑战；对于只是想用 AI 的用户来说，付费使用云端 LLM 往往更实际。作者认为 Proxmox 是实验本地 LLM 的优秀操作系统，但整体表现仍没有达到 Claude 级别的本地模型，而且在缺乏精细优化时，更多 GPU 并不会自动带来更快的 token 生成速度。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0p28x/honest_take_on_running_9_rtx_3090_for_ai/)
- **Claw 风格代理：实用工具还是过度设计的炒作？** — 帖子指出，包括 NVIDIA、字节跳动和阿里巴巴在内的大厂，正在纷纷推出“Claw 风格”代理，这类系统由长生命周期代理驱动，具备工具调用、记忆和一定自主性，被包装为一种代理运行时。作者希望收集一线实践反馈，包括搭建复杂度、工作流稳定性，以及这些代理是否真的优于脚本和 API，呼吁大家分享清晰的使用场景和真实体验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0nchk/clawstyle_agents_real_workflow_tool_or/)
- **面向 LocalLLaMA 的优质数据集合集** — 一篇 Reddit 帖子推荐了一套用于训练 LocalLLaMA 模型的数据集合集，并给出了 GitHub 仓库链接 Green0-0/llm_datasets。该投稿由用户 Good-Assumption5582 提交，邀请 LocalLLaMA 用户探索这些精心整理的数据集。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s0p7hn/a_collection_of_nice_datasets/)
- **中国拥抱 AI 内容，其他国家却称其为“垃圾”** — 一则观察指出，在某些国家，AI 生成内容被轻蔑地视为“垃圾”，而中国则被描绘为对 AI 内容持积极态度。该观点来自用户 kimmonismus 在 X（Twitter）上的一条帖子，突出了对 AI 生成作品在不同地区的截然不同的接受程度。 [来源-twitter](https://x.com/kimmonismus/status/2035680414497653191)
- **Codex vs Claude 之争引出残障相关言论** — 一条 X 帖子对比了 OpenAI 的 Codex 和 Anthropic 的 Claude，其中还夹杂了关于自闭症和 ADHD 的争议性表述。该信息核心是模型之间的“互喷”而非技术更新，并使用了带有歧视色彩的语言，来源为 Twitter。 [来源-twitter](https://x.com/dejavucoder/status/2035779020261036222)

---

*由 AI News Agent 生成 | 2026-03-22*