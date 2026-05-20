---
title: "AI 日报 — 2026-05-19"
description: "Omni上线，视频驱动万物生成，Spark全时AI，OpenAI增设水印验证。"
lang: "zh"
pairSlug: "ai-daily-2026-05-19"
---

# AI 日报 — 2026-05-19

> 覆盖 32 条 AI 新闻

## 🔥 今日焦点

### 1. Gemini Omni 登场：万物互生，从视频起步

Google DeepMind 发布了 Gemini Omni，这是一款旨在“万物生成自万物”的模型，从视频生成能力起步。它把 Gemini 的智能能力与 DeepMind 的生成式媒体系统相结合，体现了在世界理解、多模态以及编辑方面的进步。此次发布标志着向灵活的跨领域 AI 能力迈出重要一步。 [来源-twitter](https://x.com/GoogleDeepMind/status/2056786446636212467)

### 2. Google 发布 Gemini Spark：7×24 小时个人 AI Agent

Google 宣布推出 Gemini Spark，这是一款基于 Gemini 3.5 的 7×24 小时个人 AI Agent，能够根据用户指令行动，并在后台持续处理长时间任务。它运行在专用的 Google Cloud 虚拟机上，因此你无需保持笔记本电脑开启；未来还将与各类 Google 工具集成，并通过 MCP 支持第三方服务。一段动画 UI 演示展示了 Spark 管理早晨优先事项摘要和行程规划等任务，并突出显示新的 Spark（BETA）导航标签。 [来源-twitter](https://x.com/Google/status/2056791134295273554)

### 3. OpenAI 为 AI 图像加入 SynthID 水印与验证工具

OpenAI 宣布了用于识别 AI 生成图像并追踪其来源的新方法。在现有 C2PA 内容凭证基础上，图像将新增 SynthID 水印，并提供一个公开验证工具，让用户检查图像是否由 OpenAI 产品生成。此次更新旨在提升内容溯源能力以及用户对 AI 生成媒体的信任。 [来源-twitter](https://x.com/OpenAI/status/2056793648571011232)

## 📰 重点报道

### LLM

- **Karpathy 加入 Anthropic，继续冲击 LLM 前沿** — Andrej Karpathy 宣布加入 Anthropic，表示对重回研发一线充满期待，并认为未来几年在大语言模型前沿领域具有奠基性意义。他同时强调自己对教育的长期投入不会改变，并计划在合适时机重启相关工作。 [来源-twitter](https://x.com/karpathy/status/2056753169888334312)
- **OpenAI 推出长期算力“Guaranteed Capacity” 保量服务** — OpenAI 推出了 Guaranteed Capacity 项目，为客户提供对其算力资源的长期访问保障。该计划允许用户以 1–3 年期承诺换取折扣 Token，体现了公司在基础设施和产能规划上的投入，帮助客户在算力紧张的环境下实现可靠扩展。 [来源-twitter](https://x.com/sama/status/2056827105401614656)
- **HRM-Text 1B 号称多项基准 SOTA** — 一篇 Reddit 帖子讨论 HRM-Text 1B，附上其 GitHub 和 Hugging Face 链接，并对夸张的基准成绩提出质疑。作者希望社区能解释其表现背后的原因、模型的优缺点，以及这些“最先进”表现是否可信，从而展开讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ti150n/new_sota_1b_model_hrmtext/)
- **Nemotron-Labs-Diffusion 支持 AR、Diffusion、自我推演三种模式** — Nemotron-Labs-Diffusion 是 NVIDIA 推出的“三模态”语言模型，通过在推理时改变注意力模式，在自回归解码和基于 Diffusion 的并行解码之间切换。它还支持第三种模式“self-speculation（自我推演）”，通过共享 KV cache，将 Diffusion 起草和 AR 校验结合起来，以提升长上下文处理和解码效率。该模型族包含 3B、8B 和 14B 的稠密 LM，涵盖 base、instruct 和视觉语言变体，反映出生成过程正逐渐向算力受限（compute-bound）方向演化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thv6du/nemotronlabsdiffusion_from_nvidia/)
- **AI Agents 利用 Antigravity 2.0 与 Gemini 12 小时内从零构建操作系统** — 一组 AI Agent 被编排来从零构建一个可运行的操作系统，使用 Antigravity 2.0 和 Gemini 3.5 Flash。整个过程调度了 93 个并行子 Agent，记录了超过 1.5 万次模型请求，在 12 小时内处理了 26 亿 Token，API 成本低于 1000 美元。该演示展示了 AI 辅助软件开发在速度和成本上的巨大潜力。 [来源-twitter](https://x.com/Google/status/2056789235500466273)
- **SkillsVote：面向 Agent Skills 的全生命周期治理框架** — 长时程 LLM Agent 会留下可重用的经验轨迹，但原始轨迹往往嘈杂且难以治理。作者提出 SkillsVote，这是一套针对 Agent Skills 的生命周期治理框架，将可执行脚本与不可执行的指导性信息相结合，旨在减少开放技能生态中的冗余与“污染”。该框架涵盖收集、推荐与进化机制，帮助在模型持续更新时维持可用的上下文。 [来源-huggingface](https://huggingface.co/papers/2605.18401)
- **AI 自动科研进展：论文可全自动生成，但学术诚信风险仍在** — 借助 AI 辅助研究，如今大约 15 美元就能实现几乎全自动的论文生成，长时程 Agent 能以极少的人类干预完成实验、撰写稿件并进行批判性评审。然而，这些系统依旧会编造结果、忽略错误，并在学术压力下难以准确评估创新性。该综述覆盖截至 2026 年 4 月的相关发展，一方面强调生产力提升，另一方面指出 AI 驱动科研在学术诚信上的持续挑战。 [来源-huggingface](https://huggingface.co/papers/2605.18661)
- **CLI-Anything 让所有软件都具备 Agent 原生接口** — CLI-Anything 是一个 CLI-Hub，允许 AI Agent 浏览、安装和管理社区构建的 CLI 工具，实现 Agent 与软件之间的交互。项目展示了通过自动生成 CLI、实时预览、轨迹循环等机制来产出 CAD 构型和 3D 场景等成果，并欢迎公众贡献和“心愿清单”提案，以扩展与 Agent 的兼容性。 [来源-github](https://github.com/HKUDS/CLI-Anything)
- **面向 A/H/美股市场的 LLM 驱动量化分析系统** — GitHub 上的一个开源项目提供了覆盖 A 股、港股和美股的 LLM 驱动股票分析系统。它整合多市场数据和实时资讯，提供 AI 决策看板、多渠道消息推送与零人工值守自动化运行；支持多种 AI 模型、数据源与部署方案。 [来源-github](https://github.com/ZhuLinsen/daily_stock_analysis)
- **LLM 驱动工具自动构建带关节的 3D 对象** — 一则 Reddit 帖子介绍了一条管线，将 LLM 作为结构化代码编译器，生成 Blender 的 Python 代码块，用于构建多部件、可关节运动的 3D 对象（如洗衣机）。不同于常见的 Diffusion 流程容易生成“糊状”模型，该管线导出的 GLB 文件部件与关节分离清晰，支持真正的内部关节运动；项目已在 GitHub 开源，并对具体使用的 LLM 保持中立。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thucyj/a_tool_i_built_to_generate_3d_objects_with/)
- **KV cache 量化基准显示 TCQ 占优；对称 q8 可能浪费显存** — 一项基于 RTX 3090、使用 BeeLlama v0.1.2 的测试，对 Qwen 3.6 27B 在 64k/128k 上下文下的量化（Q5_K_S 和 IQ4_XS）进行了评估，比对 TurboQuant、TCQ、q5 和 q8 等设置。作者发现，在 q4_0 配置下，困惑度（PPL）在 bf16 下被“掩盖”，而 KLD 能揭示差异；并得出结论：TurboQuant 名不副实但 TCQ 有帮助，q5 应得到更多关注，而对称 q8 可能在白白浪费显存。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thu6os/here_are_my_kv_cache_quantization_benchmarks/)

### 开源

- **开源 SAM3 在复杂场景中展现强大目标跟踪能力** — 一款开源的 SAM3 模型因其在目标跟踪方面的出色表现受到好评，即便在篮球等复杂场景中也能稳定工作。作者表示 SAM3 可能是其最喜欢的计算机视觉模型之一，并质疑为何 Meta 旗下的 SAM 系列没有被用来打造那些“显而易见、却极具威力”的产品。 [来源-twitter](https://x.com/skalskip92/status/2056658463229390936)
- **SANA-WM 2.6B 世界模型支持 720p 视频生成** — NVlabs 的 SANA 项目提供了一个面向效率优化的高分辨率图像与视频合成代码库，覆盖各类 SANA 变体的端到端训练与推理流程。2.6B 参数的 SANA-WM 世界模型已支持 720p 视频生成，并提供 6 自由度（6-DoF）相机控制，是可控世界建模和具身智能的重要里程碑。该项目在 GitHub 开源，文档与社区渠道完善，仍在积极开发中。 [来源-github](https://github.com/NVlabs/Sana)
- **字节跳动开源 Lance：3B 多模态模型** — 字节跳动发布了 Lance，这是一款 30 亿参数、轻量级的多模态开源模型，面向图像与视频理解、生成和编辑任务。模型在 128 张 A100 GPU 预算下，从零开始、采用分阶段多任务训练策略，目标是在统一框架下同时在图像和视频任务上取得良好表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thkwgk/bytedance_released_an_open_source_model_that/)

### 硬件

- **Google 联手三星、Gentle Monster、Warby Parker 推智能眼镜** — Google 宣布与 Samsung、Gentle Monster 和 Warby Parker 合作开发新一代智能眼镜。相关推文展示了两款秋季系列设计的抢先一瞥，并提及 Google I/O，大致勾勒出一条以 AI 为核心的可穿戴设备产品线。 [来源-twitter](https://x.com/Google/status/2056806066055455187)
- **LongLive-2.0：基于 NVFP4 的并行长视频生成** — LongLive-2.0 提出了一套基于 NVFP4 的并行基础设施，用于长视频生成的训练与推理，重点解决速度与显存瓶颈。它引入了一种名为 Balanced SP 的序列并行自回归训练方案，将 teacher-forcing 布局与 SP 执行共同设计，并配合支持 SP 的分块 VAE，以显著提升整体效率。 [来源-huggingface](https://huggingface.co/papers/2605.18739)

## ⚡ 快讯速览

- **Code as Agent Harness：LLM 借助代码进行推理** — 最新的大语言模型在理解与生成代码方面表现强劲，覆盖从竞赛编程到软件工程的诸多任务。文章认为，代码正逐渐成为 Agent 推理、行动、环境建模以及基于执行的结果验证的“操作底座”，并将这一趋势概括为“code as agent harness（以代码为 Agent 挂载框架）”。 [来源-huggingface](https://huggingface.co/papers/2605.18747)
- **Claude Code 发布学术研究技能插件** — Imbad0202 在 GitHub 上发布了面向 Claude Code 的 academic-research-skills 插件，可引导研究者从选题到发表的完整流程。插件支持 Claude Code CLI、VS Code 和 JetBrains（v3.7.0+），提供诸如通过 /ars-plan 进行苏格拉底式规划，以及自动收集参考文献、格式化引用、校验数据与逻辑一致性等功能；工具相当于研究“副驾”，负责体力活，而用户则专注于提出问题、选择方法、解释结果并撰写关键论点。 [来源-github](https://github.com/Imbad0202/academic-research-skills)
- **12-Factor Agents：概括生产级 LLM 应用实践原则** — Dex 推出 12-Factor Agents，这是一套托管在 GitHub 上、受“12-Factor Apps” 启发的原则，用于构建生产级 LLM 驱动软件（公开地址：https://github.com/humanlayer/12-factor-agents）。项目邀请社区反馈与贡献，对比了从 LangChain 到极简派在内的多种 Agent 框架，并强调上下文工程与配套工具，包括通过 npx/uvx create-12-factor-agent 进行脚手架创建及相关分享。 [来源-github](https://github.com/humanlayer/12-factor-agents)
- **英特尔 Crescent Island PCB 泄露：160GB LPDDR5X Xe3P GPU** — 泄露的 Crescent Island PCB 据称展示了英特尔面向数据中心的 Xe3P GPU，搭载 160GB LPDDR5X 内存（20×8GB 模组），以此绕开 HBM 供应紧张问题。内存运行在 8800–9500 MT/s，对应 704–760 GB/s 带宽，采用 640 位总线，若类比桌面平台 64 位通道设计，则相当于 10 通道配置。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thxig9/intels_crescent_island_pcb_leaks_showing_a/)
- **Agent 测试 rm -rf 命令后，作者加入 bash 白名单与 bubblewrap 沙箱** — 有人用 Agent 测试安全防护，尝试执行危险命令（rm -rf /），测试虽然只带来了一场小惊吓，但成功触发了防护需求。作者随后通过 bash 命令白名单和 Bubblewrap 隔离机制实现了沙箱环境，先完成白名单配置，再增加隔离层。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thosnt/got_my_first_rm_rf_today/)
- **Llama.cpp PR 带来 MTP 性能改进** — 一则 Reddit 帖子关注到 PixelatedCaffeine 在 GitHub 上提交的拉取请求（ggml-org/llama.cpp #23269），旨在加入与 MTP 相关的改进。帖子给出了该 PR 的链接，并在评论区展开讨论，意味着 llama.cpp 上游即将迎来一次面向性能优化的更新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thlmsx/time_to_update_llamacpp_to_get_som_mtp/)
- **Google AI Edge Gallery 更新：支持 Gemma 4 与 Pixel TPU** — Google 发布 AI Edge Gallery v1.0.13 和 v1.0.14 版本更新，引入 Gemma 4 多 Token 预测（Multi-Token Prediction）和 Pixel TPU 支持。此次更新还增加了实验性 MCP、新技能以及聊天记录保存等功能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ti0g0k/google_ai_edge_gallery_v1013_v1014_updates_gemma/)
- **Gemini 支持 HLS 播放** — Gemini 现已支持 HTTP Live Streaming（HLS）播放，为基于 Gemini 的内容提供标准化、浏览器友好的视频分发方式。该功能提升了流媒体兼容性与用户观看体验。 [来源-twitter](https://x.com/OfficialLoganK/status/2056528490011476100)
- **新手程序员从 Claude Sonnet 4.6 转向 Qwen3.6-35B-A3B-UD-Q6_K 的实践记录** — 一位初学者记录了自己在一个 Python Pygame 项目中使用大模型编程的经历（约 3 万行代码、55 个模块）。他先后尝试 Claude Opus 和 Claude Sonnet 4.6，虽然初期帮助很大，但受到上下文长度与调试延迟的困扰，最终转而使用 Qwen3.6-35B-A3B-UD-Q6_K。帖子重点分享了真实开发场景中模型成本与性能之间的权衡。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ti1f2k/newbie_vibe_coding_experience_shifting_from/)
- **Qwen 发展动态：122B 与 27B 模型提交在路上** — r/LocalLLaMA 上的一则帖子提到，Qwen 即将迎来一个 122B 模型以及一个由用户 /u/jacek2023 提交的新 27B 模型。帖子附上相关讨论与评论链接，显示开源 LLM 在模型规模扩展方面仍在加速探索。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1theffd/qwen_is_cooking_hard/)
- **48GB 显存用户：你的“主力显卡”是什么？** — 一则 Reddit 帖子向拥有 48GB 显存的用户征询日常使用的主力 GPU 型号，以及如果有更多显存会拿来跑什么任务。原帖作者计划从 32GB 升级到 48GB，希望获取社区建议；讨论重点围绕 AI/ML 工作负载与高显存场景下的硬件选择。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ti2ga0/48gb_vram_users_what_are_your_daily_drivers_do/)
- **Ettin Reranker 家族发布** — 一篇 Reddit 帖子宣布推出 Ettin Reranker 家族，并附上更多细节的链接，供 LocalLLaMA 社区讨论。当前摘录未提供技术细节，主要是对这一新重排工具家族的发布通知，面向 AI 工作流中的排序与检索场景。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1thpkka/introducing_the_ettin_reranker_family/)
- **如果这条推文拿到 1 个赞，Tibo 将重置 Codex 频率限制** — 一条推文声称，只要该帖获得一个赞，Tibo 就会重置 Codex 的调用频率限制。帖子围绕 Codex 这一代码生成模型展开，以用户互动为条件设定了一个假想中的工具使用额度调整。 [来源-twitter](https://x.com/sama/status/2056804900017947046)

---

*由 AI News Agent 生成 | 2026-05-19*