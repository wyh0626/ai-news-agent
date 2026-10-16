---
title: "AI 日报 — 2026-10-15"
description: "美国最强开源权重模型Muse发布，英伟达与Apertus推出多模态长上下文模型。"
lang: "zh"
pairSlug: "ai-daily-2026-10-15"
---

# AI 日报 — 2026-10-15

> 涵盖 20 条 AI 新闻

## 🔥 今日焦点

### 1. Muse Spark Open 发布，成为美国最强开放权重模型

Muse Spark Open 是一个新的 816B 参数开放权重模型，具有 42B 激活参数和 1M token 上下文窗口，面向编码、智能体工作和多步推理，并支持文本、图像、视频和音频。其发布提高了美国开放权重系统的门槛，并通过让大型多模态智能体更易在本地和私有环境中部署，向专有实验室施压。它还附带自定义 Helion GPU 内核以及针对主要推理引擎和硬件的优化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6r9pz/introducing_muse_spark_open_the_most_capable_us/)

### 2. NVIDIA 发布 Nemotron 3.5 Super VL 120B A12B 模型系列

NVIDIA 发布了 Nemotron 3.5 Super VL 120B A12B 系列，包括基础版、NVFP4、BF16 和 LiLiCorr 推测解码变体。该大型视觉语言模型面向多模态和本地 AI 应用，延续了 NVIDIA 将硬件与优化开放检查点配对的策略。NVFP4 变体尤其适合在较新 NVIDIA 硬件上部署高效推理的从业者。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6nl8m/nvidianvidianemotron35supervl120ba12b_model/)

### 3. Apertus 1.5 将开放模型扩展至多模态推理，具备 262K 上下文

Apertus 1.5 将完全开放的 Apertus 系列从文本扩展到多模态推理，增加图像和音频理解，同时将上下文窗口扩大四倍至 262,144 个 token。8B 模型使用额外 4T token，70B 使用 2T，突显了公共、有文档记录的开放基础设施作为依赖少数提供商之外的替代方案。长上下文多模态开放模型对文档、音频和智能体工作流日益重要。 [来源-huggingface](https://huggingface.co/papers/2610.15542)

## 📰 重点报道

### 开放权重模型与多模态系统

- **Black Forest Labs 发布 FLUX.3 Image Klein 开放权重图像模型** — FLUX.3 Image Klein 是一个 5.6B 开放权重文本到图像和编辑模型，接受提示词以及最多 10 张参考图像，使用 Qwen3-VL-4B-Instruct 作为文本编码器；它将文本到图像、单参考编辑和多参考合成整合到一个模型中。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6s7el/flux3_image_klein_is_now_out/)
- **Ternary Bonsai 2 模型发布，支持浏览器本地 WebGPU 推理** — Ternary Bonsai 2 系列包括 2B、4B 和 9B 模型，其中 2B 模型通过自定义 WebGPU 内核完全在浏览器中运行，并在 M4 Max 上达到最高 500 tok/s，表明客户端侧推理能力日益增强。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6w658/ternary_bonsai_2_2b_4b_and_9b_just_released_on/)
- **IBM 发布带适配器的 Granite Switch 4.1 30B 模块化 LLM** — Granite Switch 4.1 30B 将一个 128K 上下文基础模型与用于决策和护栏的按需 aLoRA 适配器以及嵌入式语音转文本组合在一起，全部采用 Apache 2.0，并由 HuggingFace Transformers 和 vLLM 支持。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6wwx2/ibmgranitegraniteswitch41_30b8b/)

### 语音与多模态生成

- **Fish 发布 Drama 3 35B3A 文本转语音模型** — Fish 的 Drama 3 是一个 35B MoE TTS 模型，具有 3B 激活参数，可在 NVIDIA DGX Spark 上运行，并提供与原始版本高度接近的 4-bit 量化，附带 Hugging Face 演示和本地下载。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6f9p2/new_tts_king_in_town_fishs_drama_3_35b3a/)

### LLM 研究、记忆与推理

- **Cortex：将上下文整合为 LLM 的参数化记忆** — Cortex 将记忆巩固定义为将上下文驱动的收益内化到参数化记忆中，同时保留非目标能力，并提供一个包含五类任务的测试平台，用于单次、批量和顺序更新。 [来源-huggingface](https://huggingface.co/papers/2610.20399)
- **RuleTrek：在复杂场景中对智能体规则推理进行基准测试** — RuleTrek 评估当场景信息分散在多个文件中时，LLM 智能体能否识别并应用领域特定规则，解决仅依赖少数事实陈述的基准问题。 [来源-huggingface](https://huggingface.co/papers/2610.19698)
- **方法从 LLM 推荐器的 GRPO 中去除响应者噪声** — 该论文表明 Rank-GRPO 的优势主要反映采样到的是哪个回复，而不是列表质量，并提出为 LLM 推荐器在请求上训练，而不是在单个答案上训练。 [来源-huggingface](https://huggingface.co/papers/2610.17771)

## ⚡ 快讯速览

- **CLASHarness 对计算机使用中的多智能体冲突进行基准测试** — CLASHarness 引入了一个用于计算机使用场景中多智能体冲突的基准。 [来源-huggingface](https://huggingface.co/papers/2610.19128)
- **Scientific Agent Skills 库将任何 AI 智能体变成 AI 科学家** — 一个新库为 AI 智能体提供可复用的科学技能，以执行研究工作流。 [来源-github](https://github.com/K-Dense-AI/scientific-agent-skills)
- **CLI-Anything 让所有软件对 AI 智能体成为智能体原生** — CLI-Anything 旨在通过暴露命令行界面，使任意软件成为智能体原生。 [来源-github](https://github.com/HKUDS/CLI-Anything)
- **iFixAi：在 120 秒内对业务 KPI 进行 AI 智能体审计** — iFixAi 在不到两分钟内根据业务 KPI 审计 AI 智能体。 [来源-github](https://github.com/ifixai-ai/iFixAi)
- **PentAGI：用于复杂渗透测试的开源自主 AI 智能体** — PentAGI 为复杂渗透测试任务提供开源自主智能体。 [来源-github](https://github.com/vxcontrol/pentagi)
- **售价 300 英镑的 Snapdragon 迷你 PC 在 CPU 上运行 35B/80B 本地 LLM** — 一台售价 300 英镑的 Snapdragon 迷你 PC 可在 CPU 上运行 35B 和 80B 本地 LLM，展示了低成本本地推理的进展。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6stod/what_a_300_35w_snapdragon_mini_pc_can_actually_do/)
- **Nvidia 发布 Qwen3.8-Flash-Next 的 FP4 QAD 量化** — NVIDIA 发布了 Qwen3.8-Flash-Next 的 FP4 QAD 量化版本，用于高效本地推理。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6vqft/fp4_qad_quant_of_qwen38flashnext_from_nvidia/)
- **配备 128GB RAM 的 HP RTX Spark 笔记本电脑降价至 3,832 美元** — 一台配备 128GB RAM 的 HP RTX Spark 笔记本电脑降价至 3,832 美元，降低了高内存本地 LLM 开发的成本。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6trqq/128gb_rtx_spark_laptop_for_3832/)
- **DeepSeek-V4-Flash 在 4 块 R9700 上以约 79 tok/s 运行** — DeepSeek-V4-Flash 在四块 AMD R9700 GPU 上以约 79 token/秒运行。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x70e5r/deepseekv4flash0731_on_4x_radeon_ai_pro_r9700/)
- **NVIDIA 预告本周推出自己的 AI 模型** — 在一波模型发布浪潮中，NVIDIA 预告本周将推出自己的 AI 模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x6ijlk/nvidia_ai_so_many_models_launching_this_week_and/)

---

*由 AI News Agent 生成 | 2026-10-15*