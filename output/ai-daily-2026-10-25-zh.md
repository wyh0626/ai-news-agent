---
title: "AI 日报 — 2026-10-25"
description: "今日AI亮点：视觉感知统一、320BMoE命令行智能体和33B模型超越竞品。"
lang: "zh"
pairSlug: "ai-daily-2026-10-25"
---

# AI 日报 — 2026-10-25

> 覆盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. WeVisOne-VL 统一对象级与像素级视觉感知

微信的 WeVisOne-VL 推出了一种视觉语言模型，通过结构化下一 token 预测将对象级与像素级感知结合起来，覆盖检测、定位、计数、OCR、分割和抠图。这种统一方法有望简化目前将多个独立感知模型拼接在一起的多模态流水线，尤其是在从点、框到掩码和 alpha 蒙版的用户指定定位任务中。[来源-huggingface](https://huggingface.co/papers/2610.31329)

### 2. IQuest-Q1 推出面向 CLI 系统的 320B MoE 智能体基础模型

IQuest-Q1 是一个 320B 参数的稀疏混合专家模型，激活参数为 15B，分三阶段训练以获得更强的智能体命令行界面能力。其在预训练中使用 Stable SplitNorm、Muon 和 muP，随后进行领域与格式特定的中期训练，这表明业界正日益投入于为使用工具的 CLI 智能体而非仅通用聊天而优化的基础模型。[来源-huggingface](https://huggingface.co/papers/2610.30949)

### 3. Nanbeige 发布 4.3-33B 模型，称其性能优于 Qwen3.8-27B

Nanbeige 已在 Hugging Face 上发布 Nanbeige4.3-33B，声称其在多项基准上优于 Qwen3.8-27B。该模型还被定位为 Nanbeige 小模型蒸馏流水线的基础，包括 Nanbeige4.3-3B，使其成为面向本地与蒸馏部署策略的重要开放模型发布。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf0kz4/nanbeigenanbeige4333b_hugging_face/)

## 📰 重点报道

### 多模态与生成媒体

- **LayerEditor 将指令引导的图像编辑与可复用 RGBA 图层结合** — LayerEditor 将指令引导编辑与可复用 RGBA 图层生成相结合，能够在保留无关区域的同时实现精确的局部操作。[来源-huggingface](https://huggingface.co/papers/2610.24738)
- **因素感知 MLLM 潜在学习改进电影级视频生成** — 一种新的因素感知预测学习方法使 MLLM 表征对电影级视频生成更具可操作性，并可控制角色、场景、动作和镜头。[来源-huggingface](https://huggingface.co/papers/2610.30926)

### 智能体评估与工具

- **面向真实世界网络环境的深度搜索智能体基准发布** — 该新基准针对开放网络环境中的 Deep Search 智能体，其中证据分布于不同来源、模态和格式，填补了端到端评估方面的空白。[来源-huggingface](https://huggingface.co/papers/2610.30181)
- **AWS 推出面向 AI 编程智能体的 Agent 工具包** — AWS 发布了一个官方工具包，包含面向 Claude Code、Codex、Cursor、Devin、Kiro 和 fx 等编程智能体的 MCP 服务器、技能和插件。[来源-github](https://github.com/aws/agent-toolkit-for-aws)
- **Cindy：开箱即用的开源 AI 智能体** — Cindy 是一个本地开源智能体，统一了多种执行框架、模型和工具，支持任务中途切换，并能够控制浏览器、计算机和手机。[来源-github](https://github.com/makecindy/cindy)
- **LLM Arena 让模型以提示注入攻击进行对战** — 一个由 Reddit 用户构建的竞技场让由 LLM 控制的战斗者选择动作，并向对手的提示中注入精心构造的消息，同时支持可配置策略、回放和评分。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf8iqi/i_made_an_arena_for_fighting_jevs/)

### 开发者平台与行业转变

- **Gemini CLI 对未付费与 Google One 用户被 Antigravity CLI 取代** — Google 表示，对于未付费层级和 Google One 用户，Gemini CLI 已被 Antigravity CLI 取代，且 Gemini CLI 不再针对最新的 Gemini 模型进行优化。[来源-github](https://github.com/google-gemini/gemini-cli)

## ⚡ 快讯速览

- **Lean-QwenFlash 通过 NVMe 卸载在 16GB VRAM 上运行 125B Qwen3.8** — 一套新配置利用 NVMe 卸载，在 16GB VRAM 上以较低速度运行 125B 的 Qwen3.8 Flash 变体。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xev6bo/leanqwenflash_qwen38flashnext_125b_running_at_20/)
- **Hallmark AI 设计技能避免网站呈现 AI 生成感** — Hallmark 是一项设计技能，旨在帮助 AI 编程智能体生成网站时避免常见的 AI 生成视觉陈词滥调。[来源-github](https://github.com/Nutlope/hallmark)
- **Impeccable 为 AI 编程智能体增加设计指导** — Impeccable 提供设计指导，旨在提升 AI 编程智能体的输出质量。[来源-github](https://github.com/pbakaus/impeccable)
- **CrowdGPT 旨在协作且开放地训练 1B 参数 LLM** — CrowdGPT 提出一种协作、开放的过程，用于训练一个 1B 参数语言模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xff9e4/crowdgpt_a_collaboratively_trained_llm/)
- **社区呼吁备份量化 LLM，因模型下架担忧加剧** — 随着对模型移除和可用性变化的担忧加剧，LocalLLaMA 用户正鼓励备份量化模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf11qj/backup_your_quants/)
- **RTX 3080 20GB P2P 解锁使 LLM 提示处理提升 70%** — 一块经过改装、启用 ReBAR 和 P2P 解锁的 RTX 3080 20GB 报告称，LLM 提示处理性能提升了 70%。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf9kmd/rtx_3080_20gb_got_rebar_and_p2p_unlock_70_prompt/)
- **开发者预览面向编程和 3D 场景生成的 4B Qwen3.5 微调模型** — 一位开发者预览了一个 4B Qwen3.5 微调模型，该模型能够生成代码和 3D 场景。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xeuo7t/a_4b_coding_model_that_can_generate_3d_scenes/)
- **llama.cpp PR 在 GGUF 转换期间合并 Qwen 张量** — 一个 llama.cpp 拉取请求在 GGUF 转换过程中加入 Qwen 张量合并，从而简化模型打包。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf716t/qwen_merge_tensors_on_convert_by_am17an_pull/)
- **OpenAI 与 Anthropic 阻止对智能电视进行反向工程** — 一篇 Reddit 帖子讨论了 OpenAI 和 Anthropic 阻止对智能电视进行反向工程，引发了对模型提供商政策边界的疑问。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xer30z/openai_and_anthropic_blocked_the_reverse/)
- **Reddit 用户在 20 美元 Xeon 服务器上运行 PolyStrata** — 一位用户演示了在一台低成本的 20 美元 Xeon 服务器上运行 PolyStrata。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xfb9oz/show_and_tell_polystrata_on_my_20_xeon_server/)
- **Reddit 用户打造搭载 4 块 Radeon Pro V620 的 LLM 生成 3D 打印机箱主机** — 一位组装者将四块 Radeon Pro V620 GPU 与一个由 LLM 生成、3D 打印的机箱结合，用于本地推理。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf7b46/4x_v620_in_a_llm_generated_and_3d_printed_chassis/)
- **LocalLLaMA 开设双周项目展示大型主题帖** — LocalLLaMA 推出一个双周大型主题帖，用于社区项目展示。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x9yg86/biweekly_megathread_project_showcase/)
- **用户询问是否放弃 OpenCode 转向 Pi 或 DSH** — 一位 LocalLLaMA 用户正在权衡是否在智能体编程工作流中从 OpenCode 切换到 Pi 或 DSH。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf7loz/is_it_time_to_jump_ship_from_opencode/)
- **用户测试生成连贯英文输出所需的最小 LLM 规模** — 一位用户测试了生成最低限度连贯英文输出所需的最小模型规模。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xf4sxg/the_minimum_size_of_an_llm_to_generate_a_little/)

---

*由 AI News Agent 生成 | 2026-10-25*