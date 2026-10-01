---
title: "AI 日报 — 2026-09-30"
description: "VoxMem音频大模型记忆HF开源WebGPU浏览器内核Oído胜Whisper"
lang: "zh"
pairSlug: "ai-daily-2026-09-30"
---

# AI 日报 — 2026-09-30

> 涵盖 22 条 AI 新闻

## 🔥 今日焦点

### 1. 中国实验室发布 Ling-3.1-Flash：560B MoE、1M 上下文、开源

该模型将 560B 参数的 MoE 与每 token 约 25B 激活参数以及最高 1M token 上下文结合在一起，并将在开源前免费提供两周。其报告的 GDPVal-AA v2.1、FrontierSWE 和 HealthBench Professional 分数表明，长上下文推理领域又出现了一个强大的中国开放权重竞争者。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wuboum/another_ling_model_comes_out_same_receipt_2_weeks/)

### 2. Hugging Face 开源面向浏览器 AI 的快速 WebGPU 内核

Hugging Face 发布了覆盖 200 多种常见 ML 操作的 WebGPU 内核，使本地 AI 推理可以完全在浏览器中进行，并计划上游集成到 Transformers.js、ONNX Runtime Web、LiteRT.js 和其他运行时中。这降低了客户端 AI 的延迟和隐私门槛，并可能加速 Web 原生模型部署。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wu8tpg/we_just_opensourced_the_worlds_fastest_webgpu/)

### 3. DeepSeek 现在使用华为昇腾 950 训练模型

一份 Reddit 报告称，DeepSeek 现在正在华为昇腾 950 芯片上训练其模型，这与梁文锋过去关于迈向前沿的表态相呼应。如果得到证实，这将标志着中国领先 AI 实验室向国产算力的重大转向，并加剧外界对中国 AI 硬件栈的审视。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wtz1i3/deepseek_now_trained_on_ascend_950/)

## 📰 重点报道

### 音频、语音与多语言 AI

- **VoxMem 基准测试大型音频语言模型中的多模态记忆** — VoxMem 测试音频 LLM 对谁说了什么、如何说的以及什么可被听到的记忆；它表明，仅基于转录文本的评估会遗漏关键的声学和说话人信息。 [来源-huggingface](https://huggingface.co/papers/2609.32607)
- **Oído 语音识别在 5 美元微控制器上超越 Whisper-tiny** — Lokutor 的开源 Oído 在 ESP32-S3 上运行 13M 参数的 Conformer-CTC 模型，无需 GPU 或 NPU，报告 LibriSpeech WER 为 3.7/8.2，并且在噪声条件下的表现优于 Whisper tiny.en。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wu2jjy/oído_speech_recognition_that_beats_whispertiny/)
- **BiliBili Index LLM 团队发布 Index-Translate、多语言配音模型** — Index-Translate 套件覆盖 150 种文本语言以及文档和视频翻译，包含 2B/9B/35B-A3B 预览版，以及专门的配音、字幕和语音到语音模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wugf2t/indextranslate_150_text_languages_plus_document/)

### 智能体、安全与检索基础设施

- **NVIDIA 发布用于安全自主 AI 智能体的 OpenShell 运行时** — OpenShell 对文件访问、系统调用和网络连接执行内核级策略，并在应用前对策略变更进行形式化验证。 [来源-github](https://github.com/NVIDIA/OpenShell)
- **PageIndex 推出基于无向量推理的 RAG 文档索引 SDK** — PageIndex 用树结构推理索引替代向量数据库和分块，新增本地/云端 SDK 模式、Flash 索引生成，以及面向大型语料库的文件级索引。 [来源-github](https://github.com/VectifyAI/PageIndex)
- **Omni-IO Skills：面向全原生多模态智能体的即插即用框架** — 该框架通过可复用技能协调文本、图像、音频、视频、文档、3D 和代码生成，旨在让通用智能体无需重新训练基础模型即可具备多模态能力。 [来源-huggingface](https://huggingface.co/papers/2609.31847)

### 训练与扩展研究

- **研究分析同策略蒸馏的扩展特性** — 该论文考察了 RL 诱导推理中的弱到强、同基座和强到弱的师生迁移，识别出早期同策略蒸馏中存在一个规律性的有用迁移区间。 [来源-huggingface](https://huggingface.co/papers/2609.32722)

## ⚡ 快讯速览

- **Framework 开放 AMD Ryzen AI Max 400 192GB 台式机预购** — Framework 已开放 192GB Ryzen AI Max 400 台式机预购，扩展高内存本地 AI 选择。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wue339/preorder_for_new_amd_ryzen_ai_max_400_series/)
- **GLM-5.3-Flash 支持已加入 llama.cpp，可供本地使用** — llama.cpp 新增 GLM-5.3-Flash/GLM-5-Next 支持，使该模型更容易在本地运行。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wu0bdf/add_glm53flash_glm5next_support_by_timkhronos/)
- **分块 KV-Cache 压缩引入周期性相位敏感性** — 研究发现，分块 KV-cache 压缩会产生周期性相位敏感性，影响长上下文推理可靠性。 [来源-huggingface](https://huggingface.co/papers/2609.36322)
- **新语料地图方法改进 LLM 跨文档智能体搜索** — 一种语料地图方法通过为 LLM 智能体提供大型集合的结构化概览，改进了智能体文档搜索。 [来源-huggingface](https://huggingface.co/papers/2609.37226)
- **Yandex/AliceAI 80B-A3B 微调完成 40%，损失曲线已分享** — 社区对 Yandex/AliceAI 80B-A3B 的微调已完成 40%，并发布了损失曲线以供跟踪。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wu9ksu/update_yandexaliceai_80ba3b_fine_tune_progress/)
- **FastFlowLM 在 AMD NPU 上以 1 tps 运行 Qwen 3.8 27B** — FastFlowLM 演示了 Qwen 3.8 27B 在 AMD NPU 上以约每秒 1 token 的速度运行。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wud77g/you_can_now_run_qwen_38_27b_on_amd_npus_via/)
- **Reddit 用户比较本地 AI 电费与前沿 API 定价** — 一名用户将本地 AI 电费与前沿 API 定价进行基准比较，发现某套配置下约为每小时 0.12 美元。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wuhrop/if_one_hour_of_ai_is_costing_me_012_is_paying_for/)
- **用户感谢 Mradermacher 提供快速的本地 Gemma 4 26B 量化** — 一位社区成员特别提到 Mradermacher 为 Gemma 4 26B 提供的快速本地量化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wtvx1g/thank_you_mradermacher/)
- **NVIDIA DGX Spark 因库存短缺价格跳涨 2K 美元** — 由于库存短缺持续，DGX Spark 的价格近几周上涨了 2,000 美元。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wudurg/whats_going_on_with_dgx_spark_price_up_2k_in_1/)
- **Reddit 用户使用 Claude 绘制 eBay 上 32GB VRAM GPU 价格图** — 一名用户使用 Claude 绘制 eBay 上现代 32GB 显存 GPU 的价格图，追踪本地 AI 硬件市场。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wuk9so/least_to_most_expensive_somewhat_modern_gpus_with/)
- **Qwen3.8-27B-pi：面向智能体编码的按努力排序推理** — Qwen3.8-27B-pi 引入按努力排序的推理，面向智能体编码工作负载。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wufzrh/qwen3827bpi_effortordered_reasoning_for_agentic/)
- **Reddit 梗图：Anthropic 事件被誉为 GLM 的最佳广告** — 一张 Reddit 梗图将 Anthropic 的一起事件解读为 GLM 模型的意外广告。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wth4iz/anthropic_just_dropped_the_greatest_advertisement/)

---

*由 AI 新闻智能体生成 | 2026-09-30*