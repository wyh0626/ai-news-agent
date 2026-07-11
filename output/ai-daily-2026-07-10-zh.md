---
title: "AI 日报 — 2026-07-10"
description: "GPT-5.6Sol上线，限速重置；Qwen3.6提速HY3推128GB开源模型"
lang: "zh"
pairSlug: "ai-daily-2026-07-10"
---

# AI 日报 — 2026-07-10

> 覆盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. GPT-5.6 Sol 上线引发 ChatGPT Work 额度重置

为了庆祝 GPT-5.6 Sol 上线，ChatGPT Work 和 Codex 的调用额度将在接下来 24 小时内重置两次，让用户有更多时间尝试高难度任务。此举旨在帮助用户在新模型发布期间更充分地探索其新能力。 [来源-twitter](https://x.com/thsottiaux/status/2075452680760443190)

### 2. Qwen3.6 量化版在 24GB GPU 上提速 2.5 倍

UnslothAI 发布了新的 Qwen3.6 量化模型，在 GPU 上实现最高 2.5 倍加速。Qwen3.6-27B NVFP4 可以在 24GB 显存上运行，而 35B-A3B 在 B200 上可达到约 17,561 tok/s，并在准确率、工具调用、Agent 使用和循环能力上有所提升。帖子还提供了使用指南和模型合集链接。 [来源-twitter](https://x.com/UnslothAI/status/2075566124687892597)

### 3. Tencent-HY3 成为 128GB 级别开放权重模型中的亮点

腾讯的 HY3 是一个 295B-A21B MoE 模型，目标是在相对紧凑的规模下推动开放权重模型的前沿。文章将 HY3 与 DeepSeek v4 Flash 进行了对比，并重点介绍了一个 107GB 的 UD128 “unsloth dynamic” 量化版本及其已公布的困惑度指标。作者使用一台配备 128GB 内存的 MacBook M5 Max 和基于 llama.cpp 的工作流作为对比基准。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1usy9ie/tencenthy3_is_the_real_deal_on_128gb/)

## 📰 重点报道

### LLM

- **Databricks 测试：pi-coding-agent 成本更低；GLM 5.2 逼近 Opus 4.8** — Databricks 的基准测试称，pi-coding-agent（被描述为“万物 bash / 最少工具”）在任务上通过率更高，成本最多低至一半。测试结果显示，在编程任务上，GLM 5.2 表现高于 GPT-5.5 high/xhigh，并与 Opus 4.8 high 大致相当。作者指出结果依赖具体场景，并提到 CC/Codex 前缀模型内置了如 Playwright 之类的工具，这会影响在视觉任务上的表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1usrek0/according_to_databricks_picodingagent_is_2x/)
- **Claude Code 桌面版新增内嵌浏览器** — 桌面端 Claude Code 现在加入了应用内浏览器，可以直接调出文档、设计稿或任意网站。它可以像访问本地开发服务器一样读取、点击和交互页面，同时在沙箱环境中运行，并可配置会话持久化。该浏览器还支持 HLS 播放等特性。 [来源-twitter](https://x.com/ClaudeDevs/status/2075635283211772279)
- **基于 USB 的本地 LLM 生存套件提案** — 一则 Reddit 帖子提出在 64 GB U 盘上构建一个自包含的离线 LLM 套件。它将通过 llama.cpp 在 Windows/macOS/Linux 上以纯 CPU 推理运行，依据内存大小选用 Qwen3.5 35B-A3B 和 Gemma 4 E4B，并内置压缩后的 Wikipedia 和授权书籍的 SQLite 数据库。一个简单的服务器配合浏览器前端，让模型在完全离线情况下检索本地语料库。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uspcg0/has_anyone_created_a_local_llm_survival_kit/)
- **腾讯 HiLS-Attention-7B 支持无限长上下文** — HiLS-Attention-7B 是一个 7B 模型，采用分块稀疏注意力机制，在语言建模损失下端到端学习块选择，从而原生支持长上下文的稀疏训练。它基于类似 OLMo3 的骨干架构，首次在论文《Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling》中提出。该方法通过压缩后的块级键值估计块“质量”，并对注意力进行分解，以便从下一 Token 预测任务端到端训练。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uspqed/tencenthilsattention7b_hugging_face/)
- **Meta 正在开发 Muse Spark 的开源变体** — 据报道，Meta 正在开发 Muse Spark 的开源版本，此消息得到 Alexandr Wang 的确认。CNBC 的报道指出目前尚无具体细节或时间表，但这一动作显示 Meta 希望在 AI 编码市场与 Anthropic 和 OpenAI 竞争。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1usbfz3/meta_are_apparently_working_on_an_open_source/)
- **纯 CPU 语音助手：Qwen3-ASR 与 Kokoro-ONNX 速度测试** — 一项实验评估了语音助手在仅使用 ONNX ASR（Qwen3-ASR-0.6B-ONNX-CPU）和 Kokoro-TTS（Kokoro-82M-v1.0-ONNX）跑在 CPU 上时的响应速度，从而将 GPU 完全留给 LLM。测试在 2022 款 MacBook M2 和 AMD Ryzen 9 7900 上进行，结果显示 M2 基本可用，而 Ryzen 9 十分迅速，并采用 5 秒的追问窗口和基于 VAD 的命令执行。作者提供了完整代码的 GitHub 链接并邀请他人测试，展示了在设备端 AI 工作流上的潜在空间。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1usiino/how_fast_can_i_get_a_voice_assistant_to_respond/)

### AI Safety

- **研究发现 Boko Haram 使用前沿 AI** — Antonia Juelich 的新研究探讨了 Boko Haram 可能对前沿 AI 的使用情况，其中一名前指挥官描述了如何利用聊天机器人请求制作炸弹的指导。该研究与 CamAISciPolicy 合作完成，并被《纽约时报》报道，凸显出围绕前沿 AI 与极端主义滥用的安全、治理和政策风险。 [来源-twitter](https://x.com/AntoniaJuelich/status/2075590815083028989)

### AI Tools

- **Grok 4.5 在 Perplexity 中作为高性价比编排模型亮相** — Perplexity 为 Consumer Pro 和 Max 订阅用户上线 Grok 4.5 作为编排模型。在 WANDR 测试中，它击败了其他五种配置，同时成本仅为 Opus 4.8 的大约一半，展现出极高的性能/成本比。 [来源-twitter](https://x.com/elonmusk/status/2075687836091625704)
- **Google AI Studio 为已部署应用提供免费易记 URL** — Google AI Studio 正在为已部署的应用推出免费“漂亮 URL”，每个应用都可以拥有自定义的 your-own-url.ai.studio 地址。该更新适用于免费应用和免费部署，简化了项目的分享和访问方式。 [来源-twitter](https://x.com/OfficialLoganK/status/2075598301018337773)

### Multimodal

- **Vidu S1 实现语音控制的实时互动视频生成** — Vidu S1 是一个实时互动视频生成模型，支持通过语音控制数字角色。它宣称可以在消费级 GPU 上以最高 42 FPS、540p 分辨率生成无限时长的实时视频，且无明显模糊或失真。模型基于 TurboDiffusion 和 TurboServe 构建，并支持上传真实人物、动漫角色和宠物的自定义图像。 [来源-huggingface](https://huggingface.co/papers/2607.03118)
- **缓解零样本动作识别中的“对象捷径”问题** — 零样本组合式动作识别（ZS-CAR）的目标是从已知的动词和物体基本单元中识别新的动词-物体组合。研究表明，当前模型更多依赖物体标签而非时序线索，暴露出由稀疏监督和动词—物体学习不对称导致的失效模式。论文提出了一套诊断指标和分析方法，用于量化并缓解这种“对象驱动的捷径”现象。 [来源-huggingface](https://huggingface.co/papers/2601.16211)

## ⚡ 快讯速览

- **从指挥 AI Agent 转向向其“请教”该做什么** — Jack Dorsey 在一条推文中表示，人们正从直接告诉 AI Agent 要做什么，转向先询问它们应该做什么，再顺着最优思路展开。这强调了一种更具协作性的 Agent 式工作方式，用于挖掘最优结果。该帖子发布在 X（Twitter）上。 [来源-twitter](https://x.com/jack/status/2075604612359315647)
- **Video-Oasis 重新思考视频理解评测方式** — 作者认为，现有视频理解基准往往混杂视觉感知、语言推理和知识先验，使得难以诊断这些基准真正衡量的能力。他们指出目前缺乏广泛共识的评估标准，并主张通过 Video-Oasis 框架来重新构建评估方式，而不是再添加一个新基准。 [来源-huggingface](https://huggingface.co/papers/2603.29616)
- **用 160GB 语料训练 1800 年代文本专用 LLM** — 一位独立研究者整理了 160GB 的 19 世纪英文语料（1800–1875 年、主要来自英国和美国），计划在此基础上训练一个 20 亿参数的 LLM。目前已用 50 亿 Token 样本训练了一个 5 亿参数的评估模型，并在从数据集中提取的 19 世纪问答对上进行微调。早期输出显示，该模型在与伦敦相关的主题上表现尚可，具备扩展到更大规模训练的潜力，但整体准确率仍受限，因为目前仅处于评估阶段。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uswlq8/training_an_llm_from_scratch_on_1800s_texts_160gb/)
- **怀念 Bloom：回顾早期本地 AI 硬件时代** — 一则 Reddit 帖子通过回忆使用 768GB Optane 硬盘做交换空间跑 Bloom 模型、生成一个 Token 需要 20 分钟的经历，来反思本地 AI 的进步。作者询问是否有人尝试过早期 Bloom 模型，并表示希望重新体验，以更加体会如今性能的飞跃。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ut1tno/nostalgia_for_bloom/)
- **LM Arena 减少展示开源模型，被质疑“收缩战线”** — 帖子称 LM Arena 现在展示的新开源模型变少，只覆盖体量最大的那些。作者指出，其中缺失了 Qwen3.6 以及 Step 3.7 Flash，并将这些称作“重大模型”。他质疑 LM Arena 的做法是否意味着在开源模型评测上的退却。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ut0n1p/is_lm_arena_over/)
- **“推测性预热缓存”将 Prompt 延迟减少 10–20 秒** — 一个名为 OpenFox 的本地 AI 工具（MIT 许可，运行在 Spark 集群上）提出了一种推测性优化策略：在用户打字时预先加载系统 Prompt 和工具上下文。通过预加载提交时会用到的完整上下文，该方法可在提交后减少约 10–20 秒的延迟，为本地 AI 工作流带来小而实用的改进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1uskb1g/speculative_cache_warming_warms_your_cache_while/)
- **192GB DDR5 + 2× RTX 5090 最适合跑哪款 VLM/LLM？** — 一位 Reddit 用户询问，在一台配备 192GB 双通道 DDR5 内存和两块 RTX 5090 GPU 的高端工作站上，哪些视觉语言模型或语言模型表现最佳。他提到 Qwen 27B 作为潜在选项，并想了解应如何可靠地对模型进行排名，是看评测基准，还是参考社区实际体验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ut1pu1/best_vlm_or_llm_for_192gb_ddr5_dual_channel_2x/)
- **华为长焦拍到的飞机被 AI 识别成鸟** — 据报道，华为的长焦相机在拍摄远处飞机时被 AI 误判为鸟类，暴露了在超长焦距下 AI 物体识别的局限性。该事件在 X（Twitter）上被分享，凸显了消费级相机 AI 在图像可靠解读方面仍面临挑战。 [来源-twitter](https://x.com/youy1qwq/status/2075444313132351828)
- **开发者沉寂 3 年后放话要发模型，引发猜测** — 一篇 Reddit 帖子提到用户 /u/pmttyji 在推特上发文称要发布某个模型，但并未透露任何细节。发布时间也不明确——不清楚是即将发布还是仍需等待，这在 LocalLLaMA 社区中引发了一些讨论和猜测。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1usg4ox/someone_tweeted_after_3_years_about_his_model/)

---

*由 AI News Agent 生成 | 2026-07-10*