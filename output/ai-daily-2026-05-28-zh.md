---
title: "AI 日报 — 2026-05-28"
description: "Opus 4.8提升判断力/独立性；Mythos即将推出；128K上下文优化。"
lang: "zh"
pairSlug: "ai-daily-2026-05-28"
---

# AI 日报 — 2026-05-28

> 覆盖 34 条 AI 新闻

## 🔥 今日焦点

### 1. Claude Opus 4.8 发布：判断力更锐利、更自主

Claude Opus 4.8 已发布，此次更新针对 4.7 版本的用户反馈进行了修复和增强，在判断力、进度反馈透明度以及长时间独立运行能力上都有提升。该版本进一步强化了其在代码编写、知识型工作以及端到端任务处理上的吸引力，同时官方基准表对比了 Opus 4.8 与其前代以及同类模型在代码能力、Agent 能力、推理和实际任务等方面的表现。[来源-x](https://x.com/alexalbert__/status/2060043196655362358)

### 2. Anthropic 将在安全担忧与推理算力激增背景下推出 Claude Mythos

Anthropic 计划在未来几周内推出 Claude Mythos，将这一举措定位为回应安全担忧，同时据称已为其锁定数百亿级别规模的推理算力。此次推出发生在业界持续讨论该模型网络攻防能力以及其在企业场景中安全影响的背景之下。[来源-x](https://x.com/menhguin/status/2060060425031696387)

### 3. Zai 部署 ZCube 以提升 GLM-5.1 推理性能

Zai 在一个拥有上千 GPU 的 GLM-5.1 集群上，将原有网络拓扑替换为 ZCube，通过移除 Spine 层实现成本节省、吞吐提升和时延下降。改动带来约 33% 交换机成本下降、15% GPU 吞吐提升，以及 P99 首 Token 延迟降低 40.6%。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq35a0/zai_replaced_the_network_architecture_running/)

## 📰 重点报道

### LLM

- **LFM2.5-8B-A1B 登场：面向设备优化、支持 128K 上下文的 AI 模型** — 一款面向设备侧的 8B MoE 模型，提供 128K 上下文，目标是覆盖各类边缘设备；在 38T token 上训练，结合大规模 RL，并支持单卡快速工具调用与定制，且以 open-weight 许可方式发布。[来源-x](https://x.com/liquidai/status/2060023455290974474)

- **Claude Code 新增动态工作流，实现多 Agent 编排** — 当在提示中使用 “workflow” 时，Claude Code 可以生成严格的编排方案，从而在数百个 Agent 之间实现可靠的端到端自动化工作流。[来源-x](https://x.com/_catwu/status/2060054180379689074)

- **双向进化搜索助力自我改进型语言模型** — 该工作提出 Bidirectional Evolutionary Search 方法，以拓展搜索空间，在后训练阶段提升样本生成质量和推理表现，特别面向各类 Agent 系统；相关内容已在 Hugging Face 上托管。[来源-huggingface](https://huggingface.co/papers/2605.28814)

### AI

- **AlphaGo 激发数学突破，与围棋实力提升呈镜像效应** — 在 AlphaGo 之后，人类在数学领域的表现似乎通过 AI 辅助方法正在加速提升，尤其与单位距离猜想相关的研究进展，被认为在某种程度上呼应了当年围棋领域的跃迁式增长。[来源-x](https://x.com/polynoamial/status/2059932468820816354)

### Industry

- **斯皮尔伯格：不要把 AI 当作创意的最终裁决者** — 这位导演认为，AI 应该只是影视制作工具箱中的一个工具，而不应成为对白、镜头调度或场景设计的最终权威。他强调，人类创意和审美仍应在创作流程中占据核心地位。[来源-x](https://x.com/Variety/status/2059804529378607105)

### RL

- **ProRL：用修正策略梯度推动主动推荐中的强化学习进展** — ProRL 提出一种基于修正策略梯度的强化学习方法，以提升主动推荐系统在长期回报上的表现，使系统在多轮交互中做出更优的决策与推荐。[来源-huggingface](https://huggingface.co/papers/2605.28293)

### Multimodal

- **GEM：通过生成式监督弥合具身视觉-语言鸿沟** — GEM 针对 Vision-Language-Action 任务，试图缩小高层语义预训练与低层空间知识之间的差距，以便在具身机器人场景中实现更协调的感知、理解与动作执行。[来源-huggingface](https://huggingface.co/papers/2605.28548)

## ⚡ 快讯速览

- **MoneyPrinterTurbo：一键式 AI 视频生成器** — 一款一键生成 AI 视频的工具，能够快速完成各类 AI 视频内容制作。[来源-github](https://github.com/harry0703/MoneyPrinterTurbo)

- **Claude Code Harness 实现“计划-执行-复盘”循环** — 该 Harness 为 Claude Code 工作流提供“计划-执行-复盘”的闭环能力，从而提升任务可追踪性与过程管理。[来源-github](https://github.com/Chachamaru127/claude-code-harness)

- **LiquidAI 发布 LFM2.5-8B-A1B 端侧混合 LLM** — LiquidAI 推出一款面向边缘设备的端侧混合 LLM，主打在本地设备上的高效推理与部署。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq8a40/liquidailfm258ba1b_hugging_face/)

- **Mimo 2.5 Pro 在 8x GB10 集群上实现 83 t/s** — 在 GB10 集群上取得的高吞吐表现，展示了该方案在本地部署和扩展性方面的潜力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqf5mi/mimo_25_pro_40ts_on_8x_nvidia_sparkgb10_cluster/)

- **西方开源权重 SOTA：Gemma4-31B vs Nemotron3-Super-120B** — 社区讨论围绕这两款模型在各项基准上的表现，试图厘清当前开源权重 SOTA 的格局。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq41pa/western_openweight_sota_is_between_gemma431b_and/)

- **Qwen-Image-Bench 推出 Q-Judger 评估图像质量** — Qwen-Image-Bench 新增 Q-Judger 组件，用于系统性评估生成图像的质量与表现。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tpww8m/qwenqwenimagebench_hugging_face/)

- **VLLM 比 Llama 快 5 倍；量化状态尚不明朗** — VLLM 报告相较 Llama 可实现约 5 倍加速，但关于量化支持和实际效果的讨论仍在持续。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq633w/vllm_gives_5x_speed_of_llama_but_quants_not/)

- **发现影响 VLLM 与多种 LLM 工具的底层框架漏洞** — 研究者在支撑 VLLM 及相关 LLM 工具的框架中发现安全漏洞，官方将提供后续修补与加固指南。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tpp2th/vulnerability_found_in_framework_used_by_vllm/)

- **PaddlePaddle 发布 PaddleOCR-VL-1.6** — PaddleOCR-VL-1.6 为 PaddlePaddle 的 OCR 组件带来一系列新特性与修复，增强多模态识别能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq1jpt/paddlepaddlepaddleocrvl16/)

- **SpaceX 自研 AI 栈接近 V1.0，号称较 JAX 快 10 倍** — SpaceX 宣称其自研 AI 栈相较 JAX 可实现约 10 倍加速，显示其在内部 AI 基础设施上的大力投入。[来源-x](https://x.com/elonmusk/status/2059884150187053488)

- **红队测试有助于在发布前改进新 AI 模型** — 报道强调红队测试是新模型发布前的重要安全环节，可帮助发现潜在风险与问题。[来源-x](https://x.com/claudeai/status/2060074627032838438)

- **公开：SWE-Bench 每个测试背后的提示设计** — 详细披露了 SWE-Bench 测试所使用的提示模版与设计思路，有助于社区更好理解其评测逻辑。[来源-x](https://x.com/theo/status/2059851108450025539)

- **用于多模态 Agent 推理的探索式策略优化** — 提出一种探索式策略优化方法，旨在提升多模态 Agent 在复杂推理任务中的决策质量。[来源-huggingface](https://huggingface.co/papers/2605.28774)

- **DenoiseRL：通过自举式推理从噪声前缀中恢复** — DenoiseRL 针对输入前缀存在噪声的情形，改进模型的推理稳定性和恢复能力。[来源-huggingface](https://huggingface.co/papers/2605.28421)

- **obra/superpowers：Agent 化编程能力框架与方法论** — 仓库中整理了一套关于 Agent 化编程技能的框架和方法论，用于指导工具与 Agent 的能力设计。[来源-github](https://github.com/obra/superpowers)

- **Reachy Mini 实现完全本地化的语音 Agent** — Reachy Mini 现已支持完全本地运行的语音 Agent 能力，不再依赖云端推理。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq4x48/reachy_mini_goes_fully_local/)

- **从 4 张 RTX 3090 升级托管 LLM 的硬件路径** — 社区分享从 4x RTX 3090 机型升级以更好托管 LLM 的实用硬件选型与迁移方案。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqfzvs/upgrade_path_from_4x_3090s/)

- **Qwen3.6 35B：TXT vs Markdown vs HTML vs HTML+CSS 表现比较** — 针对 Qwen3.6 35B，在纯文本、Markdown、HTML 与 HTML+CSS 等不同文本表示方式下进行对比测试。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq7yeq/qwen36_35b_txt_vs_markdown_vs_html_vs_htmlcss/)

- **Claude CLI 2.1.154 导致 vLLM 异常；补丁已修复角色问题** — 新版本 Claude CLI 与 vLLM 集成时出现角色处理异常，最新补丁已对该问题进行修复。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqiewb/claude_cli_21154_breaks_local_use_with_vllm_by/)

- **HuggingFace 模型页新增“仅 Base”筛选** — HuggingFace 模型页面新增“Base only”过滤选项，方便用户只浏览基础模型版本。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tq2ce9/hf_models_page_now_has_a_base_only_toggle_to/)

- **CHAEWON 在 Android 上使用 Gemini 做 Spotify 情绪推荐** — 通过 CHAEWON，Gemini 在 Android 端为 Spotify 提供基于情绪的音乐推荐体验。[来源-x](https://x.com/Android/status/2060059255252631876)

- **投票：本地跑 AI 模型需要多少 VRAM？** — 一项社区投票，探讨在本地运行模型所需的 VRAM 或共享内存容量需求。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tqh44n/how_much_total_vram_or_shared_ram_for_machaloetc/)

- **Anthropic 声称找到了“惰性”问题的解药** — Anthropic 宣称在 AI 工作流中找到了对抗“惰性”的解决方案，不过相关说法仍需进一步审视与验证。[来源-x](https://x.com/scaling01/status/2060043010943942989)

- **家庭办公室“暖气片”：4 块 RTX Pro Max-Q 高温配置** — 一位用户展示了配备 4 张 RTX Pro Max-Q GPU 的家庭办公设备，整机运行时温度极高，形象地被称为“暖气片”。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tpx984/my_new_home_office_radiator/)

---

*由 AI News Agent 生成 | 2026-05-28*