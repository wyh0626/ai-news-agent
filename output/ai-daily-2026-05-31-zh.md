---
title: "AI 日报 — 2026-05-31"
description: "Rosalind生物防御上线机器人进展；ParakeetSTT移植至ggml提速"
lang: "zh"
pairSlug: "ai-daily-2026-05-31"
---

# AI 日报 — 2026-05-31

> 涵盖 19 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 面向审查通过的开发者和政府伙伴推出 Rosalind Biodefense

OpenAI 扩大对 GPT-Rosalind 的可信访问范围，将其开放给通过审查的开发者和美国政府合作伙伴，用于推进生物防御、公共卫生以及疫情应对能力。该计划旨在通过为获批用户提供由 AI 驱动的防御和公共卫生工具，提升社会的整体韧性。 [来源-x](https://x.com/sama/status/2061101875303530871)

### 2. OpenAI Robotics 取得进展；招聘工程师构建物理世界 AI

OpenAI 表示，其机器人项目正在演进为 OpenAI Robotics，并在迈向能在物理世界中运作的 AI 方面取得快速进展。该团队正在招聘全栈硬件、运营、系统和机器学习工程师，帮助编程与制造机器人以服务社会，初期聚焦支持技术工人，之后将进一步发展为个人机器人。该项目由 Aditya Ramesh 领导，强调硬件与机器学习研究的协同共设计，并邀请应聘者通过邮件发送个人背景与成果进行申请。 [来源-x](https://x.com/gdb/status/2061145994121871656)

### 3. Parakeet 语音转文本移植至 ggml，与 NeMo 输出一致且更快

NVIDIA 的 Parakeet 语音转文本模型已被移植到纯 C++/ggml，从而在无需 Python 或 PyTorch 的前提下即可在 CPU 和 GPU 上运行。其输出在字节级与 NeMo 完全一致，在 f32/f16 路径上字错误率（WER）为 0，并且运行速度显著更快（大型模型在 GPU 上最高快约 5 倍、量化后在 CPU 上约快 1.86 倍），同时占用更少内存。该项目提供量化的 GGUF 变体（f16、q8_0、q6_k、q5_k、q4_k），支持缓存感知流式处理、实时话语结束检测、带置信度的词级时间戳，并提供一个精简的 C API 以便集成。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tt6oja/i_ported_nvidia_parakeet_speechtotext_to_ggml/)

## 📰 重点报道

### Open Source & LLM Development
- **GitHub 上从零训练开源 LLM 的项目** — 一个 GitHub 项目展示了如何使用 PyTorch 在单块 GPU 上从零开始训练基于 Transformer 的 LLM。该项目有望降低研究者在小到中等规模模型上进行实验的门槛，尽管真正的大规模训练依然需要高昂资源投入。 [来源-github](https://github.com/FareedKhan-dev/train-llm-from-scratch)

- **Llama Studio v0.2.0 新增按模型脚本、多 GPU 与自动加载** — Llama Studio v0.2.0 对 llama-server 的 WebUI 进行了更新，改为按模型使用独立 shell 脚本，并增加了多 GPU 支持、会话存储，以及为无头服务器提供启动自动加载功能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tt4pag/llama_studio_v020/)

### AI Safety & Evaluation
- **13 个 Abliterated Gemma-4 E2B 变体在 44 GPU 小时内完成评测** — Abliterlitics 对 9 位作者贡献的 13 个 abliterated Gemma-4 E2B 变体进行了评测，总耗时 44 GPU 小时；其中 coder3101 的变体在保持模型能力的同时实现了 96% 的 ASR，而 treadon 的变体虽达到了 100% ASR，却在 GSM8K 上丢失了 3 分，这对各变体“能力完全保留”的说法提出质疑。完整数据集、图表与日志已发布在 HuggingFace。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tsvs3j/13_abliterated_gemma_4_e2b_variants_44_gpu_hours/)

### AI Ethics & Research / IP
- **三位图灵奖得主重发关键 AI 方法论文，署名争议浮现** — 三位图灵奖得主在重新发表一些具有深远影响的 AI 方法时，没有向最初的创作者致谢，引发关于学术归功的持续争议，而这些争议正被 IDSIA 的 AI priority 页面持续追踪。 [来源-x](https://x.com/osanseviero/status/2061097229813743984)

### Tools & Agentic AI
- **Codex 实时控制浏览器，演示效果极具冲击力** — 演示展示了 Codex 实时控制浏览器执行超出原有测试环境范围的任务，被描述为一个“震撼时刻”，并附带了关于 HLS 播放与浏览器自动化方面的说明。 [来源-x](https://x.com/gdb/status/2060978248792907818)

### LLM Models & Industry
- **Claude 试用对比 Codex XHigh；5.5 仍被认为更胜一筹** — 一位 AI 爱好者表示，在尝试使用 Claude 几天后又回到了 Codex XHigh，认为 5.5 版本在整体体验上依旧明显优于 Claude 和 Codex XHigh。 [来源-x](https://x.com/blader/status/2060920535245324479)

### Open Source & LLM Tools
- **GitHub 上从零训练开源 LLM 的项目** —（已在 “Open Source & LLM Development” 下列出）这里进一步强调其在社区共建学习与可复现性方面的作用。 [来源-github](https://github.com/FareedKhan-dev/train-llm-from-scratch)

### Hardware & WebUI
- **Llama Studio v0.2.0 新增按模型脚本、多 GPU 与自动加载** —（已在前文提及）此处补充指出，它持续改进多 GPU 工作流相关工具链。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tt4pag/llama_studio_v020/)

### Platform Updates & Open Access
- **数百万用户因明日限额重置而欢呼** — 一条社交媒体帖子庆祝即将到来的使用配额重置，同时对模型能力进行了比较，从侧面反映现实平台使用中的竞争与动态。 [来源-x](https://x.com/thsottiaux/status/2060964284117782996)

### Models, Code & Community
- **Claude 试用对比 Codex XHigh；5.5 仍被认为更胜一筹** —（也被归入 “LLM Models & Industry”）凸显社区对模型性能与对齐趋势的持续讨论与分歧。 [来源-x](https://x.com/blader/status/2060920535245324479)

## ⚡ 快讯速览

- **当 LLaMA 从显存溢出到系统内存时会发生什么** — 解释了当 LLaMA 的数据从显存溢出至系统内存时，内存分页机制如何运作以及由此带来的性能权衡。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tt50bu/whats_actually_happening_when_a_model_spills_out/)

- **家庭数据中心驱动 9 张 GPU 用于机器学习实验** — 介绍了一个家庭环境下运行 9 张 GPU 以进行机器学习实验的搭建方式，以及其中的实际取舍。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tshmxa/my_home_data_center/)

- **Qwen3.6-35B-A3B-Claude 的 APEX-MTP GGUF 发布** — 发布 GGUF 权重，以便在多种模型上实现更高推理速度。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tslv3b/mudlerqwen3635ba3bclaude47opusreasoningdistilledap/)

- **Computex 上确认搭载 NVIDIA N1X 的 Dell XPS** — Dell 在 Computex 上确认其笔记本产品线将配备 NVIDIA N1X。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tsifgs/dell_confirms_xps_laptop_with_nvidia_n1x_at/)

- **GPT Realtime 2 让你用语音控制电脑** — 通过 GPT Realtime 2 增加了基于语音的电脑控制能力。 [来源-x](https://x.com/gdb/status/2060955146952077653)

- **Hermes Agent 内置 100+ 预启用技能** — Hermes Agent 预装并启用了 100 多种技能，方便智能体直接调用。 [来源-x](https://x.com/theo/status/2061019720552525963)

- **G7 就开源 AI 与开放权重 AI 的共同表述达成一致** — G7 试图在如何表述开源 AI 和开放权重方面建立统一框架。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tt7t1x/g7_agrees_on_shared_language_around_opensource_ai/)

- **征求对 Qwen3.6b-27b KV Cache 量化的看法** — 社区正在征求对于不同 Qwen 模型 KV cache 量化方案的意见与经验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tt5gqv/whats_this_sub_geebral_opinion_on_quantisizing/)

- **LLM 推理轨迹中的语义步骤预测** — 探讨多步 LLM 推理路径中的语义步骤预测问题。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ttalm9/semantic_step_prediction_multistep_latent/)

---

*由 AI News Agent 生成 | 2026-05-31*