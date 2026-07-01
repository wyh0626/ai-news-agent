---
title: "AI 日报 — 2026-06-30"
description: "ClaudeSonnet5首秀代理性AI；Gemini亮相；Etched获合约。"
lang: "zh"
pairSlug: "ai-daily-2026-06-30"
---

# AI 日报 — 2026-06-30

> 覆盖 28 条 AI 新闻

## 🔥 今日焦点

### 1. Claude Sonnet 5 亮相，成为 Anthropic 目前最具 Agent 能力的 AI

Anthropic 推出 Claude Sonnet 5，号称迄今为止 Sonnet 系列中最具 agent 属性的版本。它可以进行规划、调用浏览器和终端等工具，并以此前需要更大型模型才能实现的规模进行自主运行。 [来源-twitter](https://x.com/claudeai/status/2072017450611142835)

### 2. Nano Banana 2 Lite 与 Gemini Omni Flash 登陆 Gemini API

Gemini API 和 AI Studio 发布 Nano Banana 2 Lite，这是一款快速（小于 4 秒/张图）且廉价的图像生成模型，价格为每 1000 张图像 0.034 美元。同时他们还推出了 Omni Flash，这是一款最先进的视频编辑模型，定价为每秒 0.10 美元，与 Veo 3.1 Fast 持平。这些发布进一步扩展了 Gemini 在生成式多媒体领域的能力版图。 [来源-twitter](https://x.com/OfficialLoganK/status/2071988351083921690)

### 3. Etched 走出隐身模式；完成 A0 流片后开始出货机柜，签下超 10 亿美元合同

Etched 宣布在成功完成 A0 流片后推出首批机柜，并已获得超过 10 亿美元的客户合同与 8 亿美元融资。早期测试声称在 AI 推理工作负载上达到了业界领先的吞吐量、时延和能效表现，首批机柜将在今夏开始发货。 [来源-twitter](https://x.com/Etched/status/2071972062202343590)

## 📰 重点报道

### LLM

- **解除对 Claude Fable 5 和 Mythos 5 的出口管制** — 美国商务部已解除对 Anthropic 的 Claude Fable 5 和 Mythos 5 的出口管制。相关访问将从明天开始逐步恢复，后续会持续更新进展。Anthropic 对用户和合作伙伴在重新部署期间的耐心表示感谢。 [来源-twitter](https://x.com/AnthropicAI/status/2072106151890809341)
- **LongCat-2.0 发布：1.6 万亿参数，100 万上下文长度** — 美团发布 LongCat-2.0，这是一款具有 1.6 万亿参数的 MoE 大模型，部署在 OpenRouter 的 Owl Alpha 背后，专为 agent 式编程设计，具备 100 万 token 上下文窗口。它引入 LongCat Sparse Attention、Zero-Compute Experts 和带门控路由的 MOPD（Agent/Reasoning/Interaction），以便在不同任务上进行专门化。团队在 Terminal-Bench、SWE-bench Pro、多语言 SWE-bench、FORTE、RWSearch 和 BrowseComp 等基准上的结果显示出强劲表现，技术博客可在 longcat.chat/blog/longcat-2 查阅。 [来源-twitter](https://x.com/Meituan_LongCat/status/2071783587205308721)
- **Horizon Scaling：35B Agent 实现万亿参数级性能** — Agents-A1 是一个 350 亿参数的 Mixture-of-Experts agent 模型，通过扩展 agent 的“horizon”（交互轨迹长度），达到了接近万亿参数模型的性能水平。研究重点在于长时间跨度轨迹扩展以及多样化 agent 能力，构建了一个长 horizon 的知识-行动基础设施，将外部知识、动作、观察和验证结果连接起来，以生成平均长度约 4.5 万 token 的 agent 交互轨迹。 [来源-huggingface](https://huggingface.co/papers/2606.30616)
- **TUA-Bench：通用型终端操作 Agent 的基准测试** — 论文提出 TUA-Bench，这是一个为评估通用型终端使用 Agent（TUA）而设计的基准。作者认为，目前的基准测试对终端相关任务严重代表不足，更多关注 GUI 或以编程为中心的工作流，因此希望通过该基准评估更广泛的、基于终端驱动的计算机使用任务。 [来源-huggingface](https://huggingface.co/papers/2606.28480)
- **NVIDIA Qwen3.6-27B-NVFP4 登陆 HuggingFace** — NVIDIA 在 Hugging Face 上发布了 Qwen3.6-27B-NVFP4，这是一款 270 亿参数的语言模型。该消息由 Reddit 用户 /u/vanbukin 在 r/LocalLLaMA 社区发帖分享，并附上模型页面链接。这一 Nvidia 变体属于 Qwen 家族，似乎加入了 NVFP4 优化，以更好发挥硬件加速能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujlltn/nvidiaqwen3627bnvfp4_just_dropped/)
- **Claude Desktop 测试版登陆 Linux（Ubuntu/Debian）** — Claude Desktop 现已在 Linux（Ubuntu 和 Debian）平台上提供测试版，将 Claude 从浏览器和终端扩展为完整的桌面体验。在付费方案中，用户可以通过新桌面应用访问 Claude Code、Claude Cowork 和聊天功能。这标志着 Claude 在 Linux 桌面端能力的一次重要扩展。 [来源-twitter](https://x.com/ClaudeDevs/status/2071988881717871065)
- **ReFreeKV 推进无阈值 KV Cache 压缩方法，提升 LLM 推理内存效率** — 研究者提出 ReFreeKV，这是一种面向 KV cache 压缩的无阈值方法，旨在减少 LLM 推理过程中的内存占用。作者指出，现有 KV 缓存剪枝方法依赖输入/领域特定的预算阈值，这会在开放域输入下损害性能。该工作提出更鲁棒、无需阈值配置的方案，以提高在多元领域下的内存效率。 [来源-huggingface](https://huggingface.co/papers/2502.16886)
- **VulnClaw：AI 驱动的渗透测试命令行工具** — VulnClaw 是一个由 AI 驱动的渗透测试 Agent，可以把自然语言提示转化为完整的攻击生命周期，基于 LLM Agent、MCP 工具链和技能编排框架构建。它能自动完成信息收集、漏洞发现、基于 PoC 的利用以及结构化报告生成，并支持多种模型（OpenAI、MiniMax、DeepSeek 等）。该工具专为授权渗透测试、CTF、安全培训和红队演练而设计。 [来源-github](https://github.com/Unclecheng-li/VulnClaw)
- **华为开源 OpenPangu-2.0：Flash 与 Pro 版本发布在即** — 华为开源了 OpenPangu-2.0-Flash，包含两个 512K 上下文长度的模型。Flash 模型总参数为 920 亿，其中激活参数为 60 亿，并开放了权重、推理代码和训练算子。旗舰 Pro 模型总参数为 5050 亿，激活参数为 180 亿，计划在 7 月推出，更多开源组件预计将在今年晚些时候发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujn5u3/huawei_opensources_openpangu20flash_92b_total6b/)
- **拥有 64GB 显存的开发者：你用哪款模型写代码？** — 一篇 Reddit 帖子介绍了作者正在使用的 Qwen 3.5 非官方变体（122B，UD-IQ4_NL），具备 10 万 bf16 上下文窗口，仅将少量层加载到 CPU/RAM，即可达到约 30 token/秒的生成速度。作者也测试了 Qwen 3.6 系列，并考虑把这款大模型作为日常主力，邀请拥有类似显存配置的开发者分享他们的模型选择。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujzyf3/devs_you_have_64gb_of_vram_which_model_do_you_use/)
- **PageStorm 发布面向创意长篇写作的研究预览版** — 团队经过一年的研发，构建出一个单轮对话即可完成整本书写作的模型，并预先构建了 LongPage 数据集，用于支持书籍尺度的创意写作。团队今日发布 PageStorm Research Preview，并附上 arXiv 论文和 HuggingFace 模型合集链接。该公告由 Reddit 用户 /u/XMasterDE 在 LocalLLaMA 论坛提交。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujr69g/pagestorm_a_model_built_for_creative_book_writing/)
- **Bartowski 为 DeepSeek-V4-Flash 提供 DS4 GGUF 文件** — Bartowski 已为 DeepSeek-V4-Flash 项目提供了一个 DS4 GGUF 文件。帖子提到会将其与 Antirez 的 DS4 imamtrix 进行对比，并给出了 HuggingFace 模型页面链接。该更新由 Reddit 用户 challis88ocarina 在 LocalLLaMA 社区发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujlwbm/bartowski_has_delivered_ds4_gguf/)

### Benchmark

- **OpenAI 发布面向基因组学的 GeneBench-Pro 基准测试** — OpenAI 推出 GeneBench-Pro，这是一个研究级基准，用于测试 AI Agent 如何处理“脏”生物数据、选择合适的分析路径，并在计算生物学中做出关键判断。该基准利用真实世界数据集，评估 AI 在基因组学、生物学和科学研究中的表现，凸显了对更强大 AI 辅助生物数据分析能力的需求。 [来源-twitter](https://x.com/OpenAI/status/2072004836674167294)

### Foundation Models

- **TabFM：面向表格数据分类与回归的基础模型** — Google Research 发布 TabFM，一款专门针对表格数据分类与回归任务设计的基础模型。它能够在单次前向传播中，对未见过的新表格给出高质量预测。更多信息及模型体验地址见 goo.gle/4eR7uku。 [来源-twitter](https://x.com/GoogleResearch/status/2072057987762708932)

### AI

- **Loop engineering 在 Cherny 和 Steinberger 提及后迅速走红** — 在 Boris Cherny（Claude Code 创建者）和 OpenClaw 的 Peter Steinberger 提到之后，“Loop engineering” 一词迅速蹿红，成为新热词。该概念的核心是一个 agent 式的编码循环：由 AI 根据规格和评测自动编写、测试并迭代代码，实现更长周期、自动化程度更高、对人类干预依赖更小的软件迭代流程。文章还引用了一个实际案例：为作者的女儿构建打字练习应用。 [来源-twitter](https://x.com/AndrewYNg/status/2071988145667928442)

### Industry

- **AI 采用度提升就业：使用 AI 的企业员工人数增长 10%** — 一篇新论文基于 2.1 万家美国企业的支出与劳动力数据，测量 AI 对就业的影响。结果发现，大规模采用 AI 的企业在两年间员工总数约增长 10%，而低采用度企业在统计上未表现出显著变化。该研究由 Arakharazian 联合 TryRamp 和 RevelioLabs 完成。 [来源-twitter](https://x.com/arakharazian/status/2071942212925936053)

### LLMs

- **Agentic Abstention：LLM Agent 何时该“停手”？** — 研究者定义了 “Agentic Abstention” 概念，即在不确定情形下，多轮对话 LLM Agent 何时应当停止继续行动。该概念有别于传统的“放弃回答”，目标是让模型在使用搜索、浏览和终端工具等接口时，识别出进一步交互或工具调用不太可能再带来帮助的情形，从而及时止步。 [来源-huggingface](https://huggingface.co/papers/2606.28733)

### AI Tools

- **TurboOCR v3 实现 520 张图/秒吞吐，并支持结构化输出** — TurboOCR v3 是一款自部署的高速文档 OCR 服务器，可在本地完全离线运行。本次更新在 FUNSD 数据集上，使用 PP-OCRv6 tiny 模型并在 RTX 5090 上，吞吐量提升到约 520 张图/秒；同时新增端到端结构化解析能力（版面 → HTML、公式 → LaTeX、阅读顺序 → Markdown），并可按请求选择是否解析表格和公式。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujqi9a/turboocr_v3_highspeed_document_ocr_server_ccuda/)

## ⚡ 快讯速览

- **《Build a Reasoning Model From Scratch》出版** — 网名为 rasbt 的作者宣布，其新书《Build a Reasoning Model (From Scratch)》在经过 18 个月创作后正式发布。这本 440 页、全彩印刷的书从零讲解推理能力扩展、强化学习和蒸馏相关内容，首批实体书已经到货。 [来源-twitter](https://x.com/rasbt/status/2071945864088535126)
- **LiveEdit 支持基于扩散模型的实时视频流编辑** — 流式视频编辑的难点在于在满足实时低延迟的前提下，保持背景和未编辑区域的稳定性。论文指出，现有流式视频生成方法因对区域精细控制和严格保持原内容的需求，无法直接用于编辑场景。为此，作者提出了 LiveEdit，一种基于扩散模型的流式方法，旨在实现实时、区域感知的视频编辑。 [来源-huggingface](https://huggingface.co/papers/2606.26740)
- **Council of High Intelligence：跨多家 LLM 提供商的 18 人 AI 议会** — 0xNyk 开源了一个框架，使用包括 Aristotle、Feynman、Kahneman 和 Torvalds 在内的 18 个 AI 人格，在多个 LLM 提供商之间对棘手问题进行协同讨论。项目强调基于多轮讨论与模型多样性，并提供 /council 等命令作为交互接口，支持 Claude、Codex 等模型。安装与使用细节均写在 GitHub 上。 [来源-github](https://github.com/0xNyk/council-of-high-intelligence)
- **开源 Lullabeast：本地 4090 vs 云端 LLM 的自动化开发流水线** — 开源项目 Lullabeast 利用规划-执行-审查循环，通过 planner、executor 和 reviewer 多个 Agent，实现软件开发自动化。作者在一次实验中分别在本地改装 RTX 4090（跑 Qwen3.6-27B）和更便宜的云端 LLM 上跑了两遍同样的开发路线图，运行时框架采用 OpenClaw。演示中包括一个多团队版本的 Conway’s Game of Life，并加入实时分析以展示整个工作流。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujrtgf/i_built_an_autonomous_dev_pipeline_and_ran_the/)
- **“Vibe Coding” 与基于 NLP 的 Agent 式编程工作流讨论** — 一位 Reddit 用户探讨了 “vibe coding” 和 agent 式 LLM 工作流，希望找到用自然语言生成与迭代代码的实用方法。他们尝试使用具备 128k 上下文的 Qwen 27B Q8_0 等模型，为如 Three.js 游戏这类项目进行规划和实现，并提出一种将高层规划逐步细化为粒度任务的迭代式方法。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uk57mi/vibe_coding_agentic_workflow/)
- **Hunyuan3D 在 iPhone 上实现图像到 3D 物体转换** — 一篇 Reddit 帖子展示了在 iPhone 本机运行 Hunyuan3D 的图像转 3D 功能。视频演示了将二维图片转换成三维物体的过程，强调了在移动端进行实时 3D 重建的可行性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uju224/running_hunyuan3d_image_to_3d_object_on_an_iphone/)
- **Hugging Face 新增硬件兼容性筛选功能** — Hugging Face 在其模型库中加入了硬件兼容性过滤器，允许用户按自己手头的硬件来筛选模型。这将帮助用户更快找到可在其设备上顺畅运行的模型，并简化在多样化硬件环境下的部署流程。该更新最早来自 LocalLLaMA 社区的一则 Reddit 帖子。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ujnjcw/new_on_hugging_face_filter_by_hardware/)

---

*由 AI News Agent 生成 | 2026-06-30*