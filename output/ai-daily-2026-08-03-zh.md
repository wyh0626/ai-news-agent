---
title: "AI 日报 — 2026-08-03"
description: "OpenAI内部模型十项突破；Qwen权重公开，GPT-Live实现听说。"
lang: "zh"
pairSlug: "ai-daily-2026-08-03"
---

# AI 日报 — 2026-08-03

> 共收录 28 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 内部模型在开放问题上取得 10 项突破性成果

OpenAI 下一个主力模型的内部版本，在数学与理论计算机科学领域一些长期未解的开放问题上给出了 10 个全新结果。实验大致使用了价值 2000 美元的 tokens，按 GPT-5.6 Sol API 计费标准计算，展示了在成本可控前提下进行探索性研究的可行性。这一结果凸显了 AI 辅助数学发现的潜力，即便是在内部早期阶段的模型上也能产生重要进展。 [来源-twitter](https://x.com/OpenAI/status/2084352161404920316)

### 2. Qwen3.8-Max 与 3.8-27B：开放权重，本地 17GB 内存运行

阿里巴巴的 Qwen 发布 Qwen3.8-Max，被称为功能最强大的模型，拥有 2.4 万亿参数以及自主编码能力。Qwen3.8-Max 和 Qwen3.8-27B 的开放权重计划于下周发布，并支持在 17GB RAM/VRAM 的本地环境中运行。本次发布还详细介绍了可用于生产的交付物、多模态循环，以及带隐式缓存的按 token 计费模式。 [来源-twitter](https://x.com/UnslothAI/status/2084110664789024769)

### 3. GPT-Live 在 ChatGPT 规模下实现边说边听

OpenAI 宣布 GPT-Live 现已能在说话的同时进行聆听，这得益于从客户端到模型的语音栈全链路端到端重构。新的架构可以保持音频的连续流动，因此更深度的推理和工具调用不会中断对话，从而在 ChatGPT 级别的规模上实现更自然的实时交互。 [来源-twitter](https://x.com/OpenAI/status/2084378415818579975)

## 📰 重点报道

### 生成式 AI

- **所有像素都将被生成：AI 扩展生成能力版图** — Cristóbal Valenzuela 发布了“所有像素都将被生成”的观点，强调 AI 生成内容领域的快速进展。该串文认为模型正在渗透到众多学科，并支撑起一种看法：美国经济正日益建立在这一前提之上。文中也提出警示，提醒不要低估这些模型在各个领域将会发展到何种程度。 [来源-twitter](https://x.com/c_valenzuelab/status/2084288185215951290)

### LLM

- **云端代理：节省 20-30% tokens，配合电脑使用可达 80%** — Cursor AI 宣布云端代理在效率上取得提升，token 使用效率提高 20-30%，在利用电脑使用的任务中最高可节省 80%。此次更新增强了 MCP、技能以及电脑使用能力，使更具野心的任务和演示可以在预算内完成。同时也简化了本地代理迁移到云端的流程，支持移动端提示，并可通过演示 PR 实现并行运行。 [来源-twitter](https://x.com/cursor_ai/status/2084317547608911986)
- **大规模 Memory Decoder 将参数化长期记忆扩展至 69 亿参数** — 研究者将 Memory Decoder 扩展到 69 亿参数规模，并使用 3000 亿预训练 tokens，从而构建更大的参数化长期记忆。在这一规模下，索引与检索成本让标准的 Faiss 流水线变得难以为继，凸显出对新型检索架构的需求。 [来源-huggingface](https://huggingface.co/papers/2607.27919)
- **antirez/ds4 发布 DeepSeek 4 本地推理引擎** — antirez/ds4 推出 DeepSeek 4，这是一款紧凑的原生推理引擎，为 DeepSeek V4 Flash 做了优化，并在高内存系统上可选支持 V4 PRO。它支持在 96GB 以上内存的 Mac 上通过 Metal 运行，支持 NVIDIA CUDA（多 GPU 与 DGX Spark），以及 ROCm，并内置 GGUF、imatrix、质量与速度等工具。该项目是自包含的，聚焦于模型加载、提示渲染、工具调用以及 HTTP 服务器，并向 llama.cpp 与 GGML 贡献者致谢。 [来源-github](https://github.com/antirez/ds4)
- **中国 AI 实验室的四种路径：Qwen、DeepSeek、Moonshot、蚂蚁 Ling** — 四家中国 AI 实验室并未采用统一策略，而是在押注不同方向。阿里巴巴的 Qwen 强调分发能力和广泛的运行时支持，DeepSeek 则专注于架构设计，Moonshot 选择即便通过非常规发布也要追求长期回报。蚂蚁集团的 Ling 模型则代表另一条战略路径，体现出该领域并不存在单一、统一的路线。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1veipya/the_chinese_labs_everyone_lumps_together_are/)
- **DeepSeek-V4-Flash 前沿模型在 24GB VRAM 家用 PC 上运行** — 有 Reddit 用户报告在一台配备 24GB VRAM 的英特尔 Windows PC 上成功运行前沿模型 DeepSeek-V4-Flash-0731。帖子强调高能力 AI 的快速平民化，指出虽然运行速度较慢，但已经在消费级硬件上实现了本地推理，并预示着从“仅限云端部署”向本地推理转变的趋势。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vehn87/i_cannot_believe_ive_got_deepseekv4flash0731_a/)
- **V4-Flash-0731 在 Q3 量化下表现亮眼，大任务上优于 Qwen** — 一位 Reddit 用户报告称，V4-Flash-0731 的量化权重对性能有显著影响。使用 Q3 权重时，它表现得像一款完全不同的模型，在简单任务上可与 Qwen3.6-27B 比肩，在大型代码库任务中则超越对方。Q2 往往过于激进，而 Q4 仍较少被测试；作者建议，对于 VRAM 充足的用户，Q3 是首选方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vee1ob/v4flash0731_vibes_after_first_weekend_of_use/)
- **Ling-3.0-flash 在 Qwen3.8 27B 发布前完成测试** — 有用户在困难 bug 上测试了 Ling-3.0-flash，发现其修复了 qwen3.6-27b 无法解决的问题。它的运行速度快于 deepseek v4 flash，整体表现与旧版 deepseek v4 flash 相当；帖子强调其问题解决能力和长对话一致性。作者提到 llamacpp 支持，并建议通过 OpenRouter 免费 API 体验，同时指出模型发布推迟到 8 月 6 日。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1veqd5c/ling30flash_is_another_potential_model_to_test/)
- **GLM 5.3 在 z-ai-sdk-java 提交记录中现身** — GitHub 的提交页面显示，在 z-ai-sdk-java 仓库中出现了 GLM 5.3 的字样。该发现由用户 Few_Painter_5588 在 Reddit 的 LocalLLaMA 社区分享。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ve9ms0/glm_53_spotted/)
- **NVIDIA NemotronLabs VoiceChat-11B 在 Hugging Face 上发布（全双工）** — Hugging Face 页面列出了 NVIDIA 的 NemotronLabs VoiceChat-11B，这是一款全双工语音聊天模型。Reddit 用户 u/adefa 在帖子中链接了该页面，并强调这款开源项目在 AI 语音能力方面的意义。这标志着一家主流硬件厂商为开源语音 AI 工具生态新增了重要组件。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1verzxx/nvidianvidianemotronlabsvoicechat11b_hugging_face/)
- **量化对知识的伤害呈非线性：Qwen3.6 27B 案例研究** — 一篇 Reddit 帖子强调，一项案例研究表明，在 Qwen3.6 27B 模型上，量化对知识能力的伤害呈非线性关系。帖子指向 LocalLLaMA 相关讨论串，探讨这一发现对 LLM 量化与模型性能的影响。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vef79c/quantization_hurts_knowledge_nonlinearly_qwen36/)

### 开源

- **MiniMax-H3 现已在 Hugging Face 公开发布** — MiniMaxAI 的 MiniMax-H3 现已在 Hugging Face 上公开可用。模型页面提到支持 HLS 播放与视频下载，意味着其生成的视频输出对用户更加易于访问与使用。 [来源-twitter](https://x.com/MiniMax_AI/status/2084106804032872591)

### 多模态

- **心理世界建模：在 AI 中推断隐藏心理状态** — 一个新概念将世界模型扩展到包括智能体的隐藏心理状态——如信念、欲望、意图与情绪。论文认为，要预测行为，必须建模每个智能体所知与所信，而不仅仅是物理场景本身，并在“心理世界建模（Mental World Modeling）”框架中对这一思想进行形式化。 [来源-huggingface](https://huggingface.co/papers/2607.27201)
- **N_0-VTLA 扩展视觉-触觉-语言-动作模型规模** — 研究者提出 N_0-VTLA，一种视觉-触觉-语言-动作基础模型，可通过触觉感知与触觉反馈控制实现精细的高接触操作，并利用部署数据进行离线策略优化。该方法在视觉主干网络基础上，提供了一套触觉集成训练方案，包括视觉-触觉预训练、分阶段触觉通路集成，以及基于优势函数的离线策略改进。 [来源-huggingface](https://huggingface.co/papers/2607.23782)

### AI 硬件

- **DeepSeek V4-Flash 284B MoE 在 RTX 3090 上的基准测试** — 一篇 Reddit 帖子报告称，在一台二手的四路 Xeon DDR4 服务器上搭载两块 RTX 3090，可运行完整的 DeepSeek V4-Flash-0731 284B MoE checkpoint，单路达 33 tokens/s，总计 68 tokens/s。作者讨论了 decode/prefill 的相关考量，并对比了不同硬件选项（包括内存带宽和价格），以评估该配置作为引擎运行平台的可行性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1veow4b/deepseek_v4flash_284b_moe_at_33_toks_single_68/)

### AI 研究

- **NousResearch 将 Hermes Agent 推进至 0.2，瞄准端到端竞争力** — Reddit 讨论指出，NousResearch 的 Hermes agent 已进展到 0.2 版本，计划在 3 月中旬发布，并从仅支持 HGX 级别模型扩展到多 GPU 工作站。讨论串回顾了 Llama 1/2 的历程，并提出 Hermes 是否有望与 GPT Omni 或 PersonaPlex 这类端到端 omni 模型竞争。帖子表达了对其持续开发的期待，以及对 Hermes 潜在能力的好奇。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1veswt9/nousresearch_keeps_doing_things_on_hermes/)

### 多模态 AI

- **MiniMax-H3 登陆 HuggingFace，用于多模态生成** — MiniMax H3 是一套通用 omni-modal 生成系统，目前已在 HuggingFace 上提供。它支持对多模态上下文进行统一理解——包括文本、图像、视频与音频，并可生成最长 15 秒、最高 2K 分辨率且带原生立体声音轨的视频。H3 在设计上强调任务泛化能力，旨在自预训练阶段起就擅长遵循复杂的多模态指令。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ve1mvh/minimaxh3_now_on_huggingface/)

## ⚡ 快讯速览

- **Opus 5 被用户批评质量下滑** — 在 X 上，一位用户抱怨 Anthropic 的 Opus 5 使用一段时间后质量恶化——开始跑题、做出不必要假设，并通过激进的安全护栏限制输出。帖子将 Opus 5 与 GPT-5.6 进行了不利对比，并提到早期的 Opus 版本（Sonnet 5、Opus 4.6）在质量上也有所退步，凸显出其在可靠性方面的争议，并对 Anthropic 模型产品线的发展方向提出质疑。 [来源-twitter](https://x.com/kimmonismus/status/2084263867270549673)
- **Claude Opus 5 的第一印象** — 一则短视频和推文展示了使用 Claude Opus 5 的体验，并附上演示视频链接。帖子指出可启用 HLS 播放以观看片段，为用户快速了解该模型的使用体验提供了窗口。 [来源-twitter](https://x.com/dejavucoder/status/2084179712230711370)
- **从 RLVR 到 RLSVR：用于 LLM 自我提升的自验证奖励** — 论文提出从 RLVR 转向 RLSVR，以通过任务变换实现开放式 LLM 自我提升中的自验证奖励。作者认为 RLVR 在数学与编码这类确定性领域表现突出，但在依赖人类偏好、奖励模型或基于 LLM 的评判者的开放式任务上遇到困难，因为这些机制可能带来偏差、瓶颈以及额外推理成本。 [来源-huggingface](https://huggingface.co/papers/2607.23802)
- **DeepSeek-Reasonix：具备缓存稳定性的终端 AI 编程代理** — DeepSeek-Reasonix 是一个原生于终端的 AI 编程代理，采用配置与插件驱动，并打包为单一静态 Go 可执行文件。它通过前缀缓存在长会话中保持较低 token 成本，支持在配置中接入多个模型端点，并通过 JSON-RPC 将外部工具作为子进程运行。该开源项目附带 reasonix.toml，提供双语社区支持，并兼容 OpenAI 风格端点而不硬编码特定模型。 [来源-github](https://github.com/esengine/DeepSeek-Reasonix)
- **提醒：你对模型的乐观远远不够；增长是指数级的** — 来自 OfficialLoganK 的一条 X 帖子提醒人们，许多人仍在低估 AI 模型的热度。作者认为，无论你对模型下注多少，进展仍然会沿着指数曲线前进。其核心信息是，在保持乐观的同时，也要正视 AI 发展的惊人速度。 [来源-twitter](https://x.com/OfficialLoganK/status/2084080601762783530)
- **“轮子上的数据中心”：256GB VRAM AI 服务器** — 一篇 Reddit 更新提供了一台一体化 AI 服务器的长期运行报告，该服务器旨在支撑一家小型企业的需求。配置包括 256GB VRAM 与 512GB RAM，作者基于自身 HPC/Beowulf 背景，重点从硬件与系统角度对稳定性与基准测试进行实用评估，而非理论分析。帖子引用了 LocalLLaMA 社区，希望为其他构建 DIY AI 基础设施的人提供可操作的经验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1veg9uq/data_center_in_a_box_on_wheels_256gb_vram512gb/)
- **G9v3-39A5B：具代理能力的重型 MOE，幻觉率低** — 一篇 Reddit 帖子讨论了 G9v3-39A5B，称其为具代理能力的重型混合专家（MOE）模型，并强调其低幻觉率表现。作者引用 Hugging Face 的分析指出，该模型在通用任务上表现强劲，唯一明显逊于 Qwen 的是编码能力。整体而言，帖子认为其通用能力有前景，只是在代码方面存在一定短板。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1veqj1j/g9v339a5b_agentic_heavy_moe_with_low_hallucination/)
- **Agent Programming Interface** — 这条推文提到一个“Agent Programming Interface”。但未提供任何关于功能特性、发布时间或范围的细节，因此其实际意义与影响目前仍不清楚。 [来源-twitter](https://x.com/naval/status/2084117793667178756)

---

*由 AI News Agent 生成 | 2026-08-03*