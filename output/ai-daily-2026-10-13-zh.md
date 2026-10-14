---
title: "AI 日报 — 2026-10-13"
description: "BitNet推出1比特嵌入、VibeASR，新模型基准推进物理智能及可靠编程代理。"
lang: "zh"
pairSlug: "ai-daily-2026-10-13"
---

# AI 日报 — 2026-10-13

> 涵盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. Microsoft BitNet 发布 1-Bit 嵌入模型与 VibeASR 引擎

Microsoft 的 BitNet 项目发布了 VibeASR.cpp，这是一个实时多语言 ASR 推理引擎，在 CPU 上使用 BitNet I2_S 量化，同时发布了首批 0.6B 和 270M 规模的 1-bit 嵌入模型。此次更新承诺实现无损的每权重 2-bit 推理，并相比 F16 显著加速嵌入预填充。这推动超低位宽推理更接近实用的端侧语音与检索工作负载。[来源-github](https://github.com/microsoft/BitNet)

### 2. Liquid AI 发布 LFM2.5-24B-A2B 端侧推理模型

Liquid AI 推出了 LFM2.5-24B-A2B，这是其 LFM2.5 系列中最大且最终的模型，总参数量为 24B，但仅激活 2.45B 参数。它面向快速、私密的端侧智能体与推理，声称其智能体性能可与 Qwen3.6-35B-A3B 竞争，并且端侧推理最高快 1.7 倍。GGUF 权重和免费演示已可用，使其成为本地推理部署领域值得关注的新成员。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x52kco/liquidailfm2524ba2b/)

### 3. AgentSWE 基准测试检验编码智能体能否构建可靠智能体

研究人员推出了 AgentSWE，这是一个面向智能体软件工程的基准测试，覆盖智能体开发生命周期的三个阶段。它检验编码智能体能否构建真正忠实满足用户需求、而非仅仅看似满足的智能体。此前没有现有基准评估过这一假设，因此 AgentSWE 是提升编码智能体可靠性与安全性的重要一步。[来源-huggingface](https://huggingface.co/papers/2610.13361)

## 📰 重点报道

### 多模态与可解释性

- **GroundingPI：面向物理智能的 4B Grounding 基础模型** — 一个 4B Grounding 模型，用于精确目标接地，包括杂乱场景和微小物体，可输出适合闭环控制以及 VLA/世界动作模型的量化点与边界框。[来源-huggingface](https://huggingface.co/papers/2609.39601)
- **S-Space 揭示多模态语言模型中的空间坐标表征** — 研究人员识别出一个线性子空间，其中对象 token 表征编码了水平、垂直和距离坐标，表明多模态 LLM 具有内在的空间表征。[来源-huggingface](https://huggingface.co/papers/2610.13527)

### 智能体推理与评估

- **研究发现，LLM 即使被要求不要思考仍会继续思考** — 一篇新论文表明，禁用思考模式和缺少长轨迹并不能可靠代表“无思考”行为，因为模型仍可能进行推理或生成填充内容。[来源-huggingface](https://huggingface.co/papers/2610.11765)
- **为长时程终端智能扩展智能体数据** — 该工作认为，短轨迹会遗漏证据积累、探索、反馈驱动的策略调整以及交付物生成，因此需要高质量的长时程智能体数据集。[来源-huggingface](https://huggingface.co/papers/2610.13166)

### 开源工具与自托管

- **Open WebUI：面向 Ollama 和 OpenAI API 的自托管 AI 界面** — Open WebUI 通过 Ollama 以及任何 OpenAI 兼容 API，为本地和云端模型提供开源、自托管界面，可通过 pip、Docker 或 Kubernetes 部署。[来源-github](https://github.com/open-webui/open-webui)
- **开源项目提供多种 AI 编码智能体的免费访问** — free-claude-code 聚合了 61 家对服务条款友好的提供商，每月提供 1.3B+ 免费 token，覆盖 Claude Code、Codex、Pi、OpenCode、VS Code Chat 及其他编码智能体。[来源-github](https://github.com/Alishahryar1/free-claude-code)
- **公司用 4x RTX 6000 Blackwell 本地 AI 堆栈服务 40 人** — 一台配备四个 RTX 6000 Blackwell MaxQ GPU 的 4U 服务器运行 Proxmox、LXC 容器、由 vLLM 服务的 DeepSeek V4 Flash、Qwen 3.8 27B Q8 和 K2-Horizon 7B Q6，同时运行 n8n、OpenWebUI、Whisper、ComfyUI 和 Tavily。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4yoqm/4x_6000_pro_for_the_company/)

## ⚡ 快讯速览

- **开发者将 Qwen2.5 稠密模型转换为 MoE 并发布 GGUF** — 一位开发者将 Qwen2.5 稠密模型转换为 MoE 变体，并发布了用于本地推理的 GGUF 权重。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4uint/update_converting_dense_models_into/)
- **越狱 PS5 GPU 以约 20 Tokens/s 运行 Qwen 27B** — 据报道，被破解的 PS5 硬件以约 20 tokens/s 运行 Qwen 27B，凸显了非传统的本地推理路径。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5ak2n/someone_is_running_qwen_27b_at_20_toks_on_a/)
- **腾讯开源在 SQLite 上本地运行的智能体记忆** — 腾讯发布了一个完全在 SQLite 上本地运行的智能体记忆系统。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x50rgo/tencent_opensourced_agent_memory_and_it_runs_100/)
- **独立开发者推出 SteerClaw Mobile，在手机上运行本地 LLM 智能体** — SteerClaw Mobile 将本地 LLM 智能体工作流带到了手机端。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5bawd/claude_cowork_for_local_llms_that_runs_on_your/)
- **RTX 3090 FE 在 LLM 推理期间 VRAM 过热，建议限制功耗** — 用户报告 RTX 3090 FE 的 VRAM 在 LLM 负载下过热，建议进行功耗限制。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4z19k/psa_for_3090_fe_owners_running_llms_overheats/)
- **AnythingLLM 从 Ollama 转向 Lemonade 和 llama.cpp** — AnythingLLM 正在将其本地后端从 Ollama 切换到 Lemonade 和 llama.cpp。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5720r/why_anythingllm_is_moving_from_ollama_to_lemonade/)
- **Sipeed 发布 MaixStation，性能可比 Strix Halo 和 DGX Spark** — Sipeed 的 MaixStation 目标本地 AI 性能可与 Strix Halo 和 DGX Spark 相比。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4r1o5/sipeed_announces_maixstation_comparable_to_strix/)
- **GPT-2 因太危险而不能发布：2019 年《卫报》文章重新浮出水面** — 一篇 2019 年《卫报》关于 GPT-2“因太危险而不能发布”的文章在当前 AI 辩论中重新浮出水面。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x52lsb/new_ai_fake_text_generator_may_be_too_dangerous/)
- **Anthropic 的蒸馏防御研究被称为对 GLM 的免费宣传** — 社区讨论认为，Anthropic 的蒸馏防御研究无意中推广了 GLM 模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4ii8e/anthropic_is_doing_free_publicity_for_glm_again/)
- **Reddit 用户提议用 AI 辅助开源 CUDA 逆向工程** — 一名 Reddit 用户提出使用 AI 协助开源的 CUDA 逆向工程工作。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4n6sg/anyone_feel_like_reverseengineering_cuda/)
- **用户购买 2x Nvidia DGX Sparks，寻求 GLM 配方** — 一位用户购入了两台 Nvidia DGX Sparks，并向社区询问 GLM 部署配方。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4ttde/got_2x_dgx_sparks_excited_and_confused/)
- **Anthropic 称 Gemma4 26B 可在 14 台智能电视上运行** — 一个 Reddit 帖子引用 Anthropic 的说法，即 Gemma4 26B 可跨 14 台智能电视运行，引发本地 AI 相关调侃。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x4wcnn/is_everyone_in_here_buying_up_smart_tvs_now/)
- **Reddit 帖子调侃 LocalAI 获得最佳广告** — 一篇 Reddit 帖子开玩笑说，LocalAI 从最近的 AI 行业闹剧中获得了最好的广告。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5cji7/fears_beyond_comprehension/)

---

*由 AI News Agent 生成 | 2026-10-13*