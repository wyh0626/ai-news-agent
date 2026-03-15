---
title: "AI 日报 — 2026-03-14"
description: "神经网发现数独规则并创SOTA；GLM-OCR获3M下载并出报告；AI助犬癌疗。"
lang: "zh"
pairSlug: "ai-daily-2026-03-14"
---

# AI 日报 — 2026-03-14

> 涵盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. Sotaku：神经网络自动发现数独规则，刷新 SOTA
研究者提出了 Sotaku，这一神经网络能够自动发现数独的规则并学会求解，在高难度数独数据集上取得了 98.9% 的准确率，表现优于专门为数独优化的架构。这项工作暗示神经网络中正在涌现类似“推理”的能力，表明有可能在无需手工设计学习路径的情况下自动发现底层规则。这或将影响未来 AI 系统的设计，让系统从数据中学习结构化问题求解，而非依赖显式编程。 [来源-x](https://x.com/_chenglou/status/2032615500065419763)

### 2. GLM-OCR 下载量突破 300 万，技术报告发布
用于真实世界文档理解的紧凑型 0.9B 多模态模型 GLM-OCR 已经突破 300 万次下载。技术报告详细介绍了其架构：将 0.4B 的 CogViT 视觉编码器与 0.5B 的 GLM 核心融合，重点展示了其在 OCR 和文档理解任务上的高效性。 [来源-x](https://x.com/Zai_org/status/2032853644744298983)

### 3. 前 Anthropic 团队创立 10 亿美元估值 AI 科学发现初创公司 Mirendil
据报道，前 Anthropic 研究人员正以 10 亿美元估值为初创公司 Mirendil 融资 1.75 亿美元，目标是用 AI 和长期推理加速科学发现。该公司由 Behnam Neyshabur 和 Harsh Mehta 领衔，计划打造能够进行长期科学推理的 AI 系统，以加速生物学和材料科学的突破。《The Information》指出，其更广泛的 AI 目标是在 2028 年前实现“自治 AI 研究员”，这一愿景也与 Sam Altman 的观点相呼应。 [来源-x](https://x.com/kimmonismus/status/2032715350685503918)

---

## 📰 重点报道

### AI in Healthcare
- **结合 AlphaFold 与 ChatGPT 的 AI 助力犬类癌症治疗** — 利用 AI 辅助蛋白质设计和个性化 mRNA 疫苗理念；初步报告显示肿瘤缩小，并为向人体应用铺路，同时也引发了监管和伦理方面的讨论。 [来源-x](https://x.com/AravSrinivas/status/2032885558020812887)

### AI Tools / Agentic AI
- **Perplexity Computer 发布；早期测试凸显 Agentic 能力** — 早期用户反馈认为其具备超越以往 AI 工具的 Agentic 能力，这也促使业界开始更多思考在系统能力快速提升时应如何设计安全控制。 [来源-x](https://x.com/milesdeutscher/status/2032661005441073407)

### AI Safety / Tools
- **消灭 prompt engineering：衡量 AI 真正进步的关键指标** — 文章认为，迈向真正 AI 能力的进展取决于能否摆脱对 prompt engineering 的依赖，并引用 Kyunghyun Cho 和 Karpathy 的观点作为论据。 [来源-x](https://x.com/sarahookr/status/2032635014010253610)

### Multimodal / Data-Centric AI
- **ShotVerse 推进文本驱动视频创作中的电影级机位控制** — 针对电影级文本生成视频流程中的瓶颈，提出采用数据为中心的方法，使用“Caption-Trajectory-Video（三元组）”来对齐文本提示、镜头轨迹与最终视频效果。 [来源-huggingface](https://huggingface.co/papers/2603.11421)

### Hardware / GPU Acceleration
- **MOE 吞吐量飙升：Qwen3.5-397B 跑在 4× RTX PRO 6000 上** — 自定义 CUTLASS kernel 解决了 SM120 GEMM tile 问题，大幅提升吞吐量；在驱动与配置微调以及预制 Docker 镜像的加持下，性能增益进一步被放大。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtrdsv/55_282_toks_how_i_got_qwen35397b_running_at_speed/)

### Open Source / TTS
- **Qwen3 TTS：C++ 版 1.7B 支持与桌面端 UI** — 该分支为 Qwen3 TTS 增加了 1.7B 模型支持、说话人编码提取、JNI 接口以及基于 Kotlin Multiplatform 的桌面 UI；模型仍需手动转换为 GGUF，相关代码已开源供审阅。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtoscf/qwen3_tts_in_c_with_17b_support_speaker_encoding/)

### Open Source / Tools
- **Intel OpenVINO 后端正式登陆 llama.cpp** — 社区特别致谢团队成员为 llama.cpp 集成 OpenVINO 后端，多位贡献者和审稿人因推动 AI 工具栈升级而受到认可。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rte9m7/thanks_to_the_intel_team_for_openvino_backend_in/)

---

## ⚡ 快讯速览

- **StepFun 发布用于 Step 3.5 Flash 训练的 SFT 数据集** — StepFun 公布了用于训练 Step 3.5 Flash 的 SFT 数据集。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtrmp1/stepfun_releases_sft_dataset_used_to_train_step/)

- **AI 支持的个性化 mRNA 疫苗用于治愈犬类癌症** — 借助 AI 设计针对特定犬只的癌症疫苗的研究正在推进；相关伦理与监管问题也被提上日程。 [来源-x](https://x.com/gdb/status/2032867435704103006)

- **Prompt 与 Harness Engineering 暴露出 AI 与 AGI 的鸿沟** — 指出当前依赖 prompt 与 harness engineering 的方式，充分体现出现阶段系统距离真正 AGI 之间仍存在明显差距。 [来源-x](https://x.com/fchollet/status/2032727335074722216)

- **Ollama Cloud 升级到 NVIDIA B300 为 Kimi K2.5 与 GLM-5 提供支持** — 云服务升级硬件以提升大模型推理性能。 [来源-x](https://x.com/ollama/status/2032744927873077332)

- **Lightpanda：用于 AI 与自动化的超高速无头浏览器** — 一款专为 AI 驱动的自动化场景设计的轻量级无头浏览器。 [来源-github](https://github.com/lightpanda-io/browser)

- **InsForge 推出面向 AI 编码代理的语义后端层** — 引入语义后端以打造更智能的 AI 编码助手。 [来源-github](https://github.com/InsForge/InsForge)

- **Qwen3-Coder-Next 量化后产出高质量 Attention GGUF 模型** — 展示了针对 coder-next 模型的高质量注意力量化效果。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtos2b/very_highquality_attention_codernext_ggufs/)

- **开源漫画翻译工具集成 YOLO、OCR、LaMa 与 LLMs** — 在一款开源漫画翻译工具中整合计算机视觉、OCR、LaMa 和大语言模型，实现自动识别与翻译流程。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtf4v8/local_manga_translator_with_llms_built_in/)

- **Agents 放弃自然语言转向结构化查询** — 报道指出，Agent 系统正在从自然语言交互转向更偏重结构化查询接口的趋势。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtxkm1/agents_given_the_choice_between_natural_language/)

- **Nemotron-3-Super-120B 未审查版：LatentMoE 与自定义量化** — 介绍了一款 120B 未审查模型变体，采用 LatentMoE 架构和多种量化技巧。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rt9nfx/nemotron3super120b_uncensored/)

- **Nvidia 的 Nemotron 3 Super 影响力更为重大** — 讨论将 Nemotron 3 Super 视作一个具有里程碑意义的重要进展。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rtp0og/nvidias_nemotron_3_super_is_a_bigger_deal_than/)

- **Claude 在非高峰时段的使用量在两周内翻倍** — 观测数据显示，Claude 的使用量在传统高峰时段之外也显著增长。 [来源-x](https://x.com/claudeai/status/2032911276226257206)

- **Grok 增加多图转视频功能并改进控制能力** — 提升多图生成视频工作流的能力，并提供更精细的控制选项。 [来源-x](https://x.com/grok/status/2032641770190946360)

- **在使用生成式 AI 之前先学会独立思考** — 呼吁在依赖生成式 AI 之前，应进一步强化个人的批判性思维能力。 [来源-x](https://x.com/fchollet/status/2032795702569603291)

- **职业变动：加入 Anthropic 对齐团队** — 多位资深对齐研究者宣布加入 Anthropic。 [来源-x](https://x.com/AndrewLampinen/status/2032850994904903793)

- **危险地跳过权限校验来运行 Claude 代码** — 对在基于 Claude 的工作流中处理权限问题不当的行为提出担忧和警示。 [来源-x](https://x.com/Yuchenj_UW/status/2032868376918503650)

- **OpenAI 泄露引发将 Codex 嵌入 ChatGPT 的讨论** — 围绕是否以及如何将 Codex 能力直接嵌入 ChatGPT 的争论浮出水面。 [来源-x](https://x.com/markchen90/status/2032873106340196718)

---

*由 AI News Agent 生成 | 2026-03-14*