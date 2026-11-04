---
title: "AI 日报 — 2026-11-03"
description: "Colibri纯C本地跑前沿MoE，48美元训GPT-2级模型，Qwen未来开源"
lang: "zh"
pairSlug: "ai-daily-2026-11-03"
---

# AI 日报 — 2026-11-03

> 涵盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. Karpathy 发布 nanochat：用 48 美元训练 GPT-2 级 LLM

Andrej Karpathy 的 nanochat 将分词、预训练、微调、评估和推理打包进一个极简的单 GPU 节点运行框架。只需一个 `--depth` 参数，它就能自动配置计算最优模型，并可用约 48 美元训练一个具备 GPT-2 能力的模型，或在竞价算力上以约 15 美元完成。此次发布降低了端到端 LLM 实验的实际门槛，并为从业者提供了一个成本感知训练的紧凑参考。[来源-github](https://github.com/karpathy/nanochat)

### 2. Qwen 确认未来 Qwen 4.0 和 5.0 将保持开源

Qwen 负责人 Liu Dayi Heng 否认了 Qwen4 将成为最后一次开放权重发布的传言，并确认 Qwen 4.0 和 5.0 将保持开源。公司把 AI 视为基础能力，并提到累计下载量超过 30 亿、开源模型超过 460 个、衍生模型超过 30 万。在前沿实验室发布策略存在不确定性的背景下，这一承诺对开放权重生态意义重大。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xm28e6/official_statement_qwen_models_will_stick_to_open/)

### 3. Colibri 用纯 C 在本地运行前沿 MoE 模型

Colibri 是一个纯 C 推理引擎，通过将活跃专家保留在 RAM 中、其余部分从磁盘流式读取，可在消费级硬件上运行超大规模混合专家（MoE）模型。它不需要 GPU，并支持 GLM、Kimi、DeepSeek、Qwen、OLMoE 等模型系列。如果其性能表现成立，它可能让前沿规模的 MoE 实验在普通机器上变得可行，并增强本地优先的 LLM 工具链。[来源-github](https://github.com/JustVugg/colibri)

## 📰 重点报道

### 视频生成与世界模型

- **Wave Forcing 让光速级流式视频生成成为可能** — Wave Forcing 针对实时长视频输出协同设计生成、训练和执行，重点解决分块自回归模型中的串行去噪和镜头漂移问题。它指向更低延迟、更稳定的流式视频生成。[来源-huggingface](https://huggingface.co/papers/2611.00859)
- **Agent Harness 连接视频生成与世界建模** — 一种新的可执行智能体运行框架管理上下文、工具、状态、反馈和预算，以支持可控的多镜头视频生成和交互式智能体环境。该工作将智能体式视频生成与视频世界模型连接起来。[来源-huggingface](https://huggingface.co/papers/2610.40191)

### 智能体与计算机使用

- **CUA-Master 为计算机使用智能体引入递归改进框架** — CUA-Master 使用嵌套双环递归改进框架，解决计算机使用交互数据中多样性、可控性和可靠性有限的问题。它旨在让开放世界智能体超越自生成经验带来的收益递减。[来源-huggingface](https://huggingface.co/papers/2611.03126)
- **CoworkOS 为长时程智能体同事引入通用运行框架** — CoworkOS 将任务策略与执行管理分离，以支持既需要交付产物又需要持续监控的长时程生产力任务。它面向更可靠的真实世界智能体同事。[来源-huggingface](https://huggingface.co/papers/2611.03178)
- **Vercel Labs 发布用于 AI 计算机使用的 Agent-Desktop CLI** — agent-desktop 让智能体通过 macOS、Windows 和 Linux 上的操作系统无障碍树读取并操作桌面应用，使用 JSON 快照和可操作引用。它避免像素匹配并支持无头运行，但对敏感桌面内容带有隐私警告。[来源-github](https://github.com/vercel-labs/agent-desktop)

### 工具与推理

- **Heretic 工具无需训练即可修改 LLM 以移除审查** — Heretic 使用对比提示和评分器，在无需训练的情况下引导本地可运行的 LLM，抑制拒答或改变语气与情感对齐。它凸显了行为修改日益容易以及相应的安全与治理问题。[来源-github](https://github.com/p-e-w/heretic)
- **Basalt 0.2.0 提升 Qwen 3.8 Flash Next 在 Blackwell GPU 上的推理** — Basalt 0.2.0 为 Blackwell GPU 上的 Qwen 3.8 Flash Next 增加了 NVFP4 和其他量化选项，报告称在 RTX 5090 加 5060 Ti、128GB RAM 上实现 300 t/s 散文生成、600 t/s 结构化输出和 10K t/s 预填充。除速度外，它还强调与 BF16 llama.cpp 参考实现的质量对比。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn4qn1/basalt_020_qwen_38_flash_next_nvfp4_300_ts_prose/)

## ⚡ 快讯速览

- **Qwen Code 仓库泄露 Qwen4-Max、Coder 和 Omni 模型 ID** — 一个 Qwen 代码仓库似乎泄露了 Qwen4-Max、Coder 和 Omni 的模型标识符，引发了对下一次发布阵容的猜测。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmitzx/alibabas_qwen_code_repo_just_leaked_qwen4max/)
- **Jacobian Lens 揭示 Qwen 推理循环；权重编辑可修复** — 一项 Jacobian-lens 分析识别出 Qwen 中的推理循环，并表明有针对性的权重编辑可以纠正卡住的行为。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xms9ii/what_qwen_is_thinking_when_it_gets_stuck_saying/)
- **维修技师据称确认 RTX 5090 的 64GB 和 96GB 显存改装** — 一名维修技师据称确认了 RTX 5090 的 64GB 和 96GB 显存改装，这对本地 LLM 容量而言可能是一项值得关注的进展。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmqq2a/rtx_5090_with_64gb_and_96gb_vram_confirmed_by_us/)
- **llama.cpp Gemma 图优化提升 E2B/E4B 提示处理** — llama.cpp 中新的 Gemma 图优化为 E2B/E4B 模型带来显著的提示处理提升。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn6mm0/gemma4_graph_optimizations_massive_gains_on_pp/)
- **LLM 智能体开启计算机图形代码生成新范式** — 一篇新论文认为，LLM 智能体为生成计算机图形代码提供了一种独特范式。[来源-huggingface](https://huggingface.co/papers/2611.01860)
- **Paperclip 推出面向 AI 智能体团队的开源编排** — Paperclip 发布了用于协调 AI 智能体团队的开源编排系统。[来源-github](https://github.com/paperclipai/paperclip)
- **Reflection 产品团队就开放权重 Beam 501B 模型举行 AMA** — Reflection 的产品团队正在就其开放权重 Beam 501B 模型举行 AMA。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmwryg/were_the_product_team_at_reflection_the_lab/)
- **Claude 重写 Gemma 4 神经元以修复意大利语时态翻译** — Claude 被用于重写 Gemma 4 神经元，并修复了一个意大利语时态翻译问题。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn1gs9/i_tried_mits_weightspace_programming_on_my_own/)
- **DeepSeek V4.1 Flash 1017 可解释小型神经网络权重** — DeepSeek V4.1 Flash 1017 也能对小型神经网络进行权重空间解释。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn2i0n/deepseek_v41_flash_1017_can_also_do_weightspace/)
- **Revolut 通过自托管替代 Claude 将 AI 编码成本降低 10 倍** — 据报道，Revolut 通过自托管而非使用 Claude，将 AI 编码成本降低了 10 倍。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn568h/british_fintech_revolut_slashes_ai_coding_costs/)
- **Library of Layers 在运行时自适应排序 Transformer 层** — 一种 Library of Layers 方法可在运行时自适应排序 Transformer 层。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmzo2s/261103526_library_of_layers_lol_adaptively/)
- **用户询问在 32GB RAM、16GB VRAM 上可运行哪些本地 LLM** — 本地 LLM 用户正在讨论哪些模型可在普通的 32GB RAM 和 16GB VRAM 配置上运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn2jyz/what_do_people_with_normal_hardware_32gb_ram_16gb/)
- **配备四块 GPU 的原型 AMD Radeon RX 470 板卡曝光** — 一张配备四块 GPU 的原型 AMD Radeon RX 470 板卡图片已曝光。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn40w7/tokenss_worlds_biggest_pcie_graphics_card/)

---

*由 AI News Agent 生成 | 2026-11-03*