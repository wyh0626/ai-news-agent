---
title: "AI 日报 — 2026-03-29"
description: "新进展：MLB用鹰眼判球，MistralAITTS，MacBookPro跑基准。"
lang: "zh"
pairSlug: "ai-daily-2026-03-29"
---

# AI 日报 — 2026-03-29

> 覆盖 23 条 AI 新闻

## 🔥 今日焦点

### 1. MLB 使用 Sony Hawk-Eye AI 判定好球与坏球

美国职业棒球大联盟开始使用计算机视觉 AI 系统来判定好球与坏球，使 Hawk-Eye 首次与裁判一起成为权威判罚来源。Sony 的这套系统通过读取棒球缝线图案和旋转指标，在从采集到输出的一整套 AI 模型流水线中对投球进行裁决。在最近的一场比赛中，多次裁判判罚被推翻，观众为机器判罚的精确度欢呼。 [来源-twitter](https://x.com/TheRundownAI/status/2038308673437512172)

### 2. MistralAI Voxtral TTS 通过约 3 秒参考音频生成富有表现力的多语种语音

MistralAI 推出 Voxtral TTS，将语义内容与声学音色分离，从而实现富有表现力的语音合成。该系统使用 Voxtral Codec 将语音压缩为超低比特率 token，并支持 9 种语言，可基于约 3 秒的参考音频完成高质量的声音克隆。据称，在声音克隆任务中，它相较 ElevenLabs Flash v2.5 的胜率达到 68.4%。 [来源-twitter](https://x.com/TheTuringPost/status/2038285318827413800)

### 3. M5-Max MacBook Pro 128GB RAM 跑 Qwen3-Coder-Next 8-Bit 基准测试

两个本地推理后端——MLX（Apple 原生框架）和 Ollama（基于 llama.cpp）——在 Apple Silicon 上搭配 Qwen3-Coder-Next 8-Bit 进行测试，以测量吞吐量、首 token 延迟（TTFT）和编码能力。测试方法是每个提示跑三次并取平均值，同时剔除第一次的 TTFT。报告中强调的亮点是，配备 128GB 内存的 M5-Max 使用 MLX 时，吞吐量约为每秒 72 个 token。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6wsy7/m5max_macbook_pro_128gb_ram_qwen3_coder_next_8bit/)

## 📰 重点报道

### LLM

- **Google 的 TurboQuant 压缩 KV Cache，提升推理性能** — Google 的 TurboQuant 旨在将 KV cache 压缩到 3–4 bit，号称在精度零损失的前提下加速本地 LLM 推理，并不是压缩模型权重本身。讨论中有人质疑，它的主要收益究竟是让超大上下文窗口成为可能，还是能带来更广泛的速度提升，以及声称在 H100 上实现 8 倍加速的结果在消费级 GPU 和 Apple Silicon 上能否同样扩展。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s76bjg/what_will_googles_turboquant_actually_change_for/)
- **本地模型已超越 GPT-3.5 的说法在网上流传** — 一则网络讨论串声称本地 AI 模型大约在 18 个月前就已经超过 GPT-3.5，挑战 GPT-3.5 的主导地位。讨论中提到 Openclaw 和一个搜索工具，并且以闲聊方式讨论本地模型未来如何在相对 GPT-3.5 的比较中进一步提升。 [来源-twitter](https://x.com/Teknium/status/2038378060635140404)
- **Anthropic Mythos 传闻推动开源权重 AI 的进展** — Andrew Curran 在 X 上发文表示，关于 Anthropic 完成其最大规模训练并产出一个超出尺度预期表现的模型的传闻看起来可信，很可能指向 Mythos。传闻还提到某前沿实验室在架构层面上取得突破。他认为，当前沿算力变得昂贵且难以精细计量时，开源权重模型反而更具优势，从而推动对更多模型与基础设施的需求。 [来源-twitter](https://x.com/edsim/status/2038352387987939551)
- **KV Rotation PR 恢复了 AIME25 上 Q8 量化的性能表现** — llama.cpp 最近的 kv-rotation Pull Request 显示，在 AIME25 基准测试中，Q8 KV 量化性能曾明显下降，但通过 KV 旋转可以在很大程度上恢复。讨论指出，这对现有 Q8 用户可能是利好，尽管作者本人计划在可见未来仍然坚持使用 FP16。该见解源自 Betadoggo_ 在该 PR 下的一条评论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s720r8/in_the_recent_kv_rotation_pr_it_was_found_that/)
- **Zinc：基于 Zig 的 LLM 推理，在 AMD GPU 上运行 35B 模型** — 一个名为 Zinc 的新 LLM 推理引擎正用 Zig 编写，目标是在 AMD GPU 上通过 Vulkan 运行 350 亿参数的模型。它强调可以直接通过 C ABI 访问 Vulkan、利用 comptime 做按量化级别的调度、自动化 GLSL 着色器编译，以及统一的单二进制构建流程，旨在让消费者级硬件上运行本地 LLM 更加可行。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s79w6u/zinc_llm_inference_engine_written_in_zig_running/)
- **Tinylora LoRA 以 13 个参数完成训练，验证相关设想** — Tinylora 展示了 LoRA 风格微调在极少参数下也能显著改变模型行为。一篇关于 Qwen-3.5 的 Reddit 复现发现，将 13 个共享参数分配给所有 MLP 层、再将 13 个共享参数分配给所有注意力层（总计 26 个参数），在收敛效果上优于使用更大规模的全局参数数目。作者计划下一步探索按层分配参数的策略。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6z9f8/tinylora_shows_lora_training_works_at_13/)
- **Kimi K2.6 即将发布；K3 目标对标美国模型** — 来自 Moonshot 内部人士的消息称，Kimi K2.6 将在 10–15 天内发布，属于一次小幅升级。K3 的开发正在推进，目标是在参数规模上对标美国同行模型，从而实现可比的性能水平。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6stgl/kimi_k26_will_drop_in_the_next_2_weeks_k3_is_wip/)
- **Meta 预告 Avocado 开源模型族** — Meta 的内部模型选择器显示，多种 Avocado 配置正在评估中，包括 Avocado 9B、Avocado Mango（多模态，带有 agent/子 agent 标签）、Avocado TOMM（Tool of Many Models）、Avocado Thinking 5.6，以及 Paricado（纯文本）。这些信息来自内部模型选择器和一篇 TestingCatalog 文章，并被一篇 Reddit 帖子引用和讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6v5n3/meta_new_open_source_model_is_coming/)

### 多模态 AI

- **JEPA 家族扩展：跨模态的潜空间预测** — 一条 X 线程概述了多种 JEPA 变体，目标是在多种模态上实现高效的自监督学习。它解释了各个变体如何将潜空间预测应用于视觉、视频、音频和 3D 数据——包括分层结构的 H-JEPA、高效语义表征的 I-JEPA，以及面向自动驾驶和机器人领域的针对性版本（MC-JEPA、V-JEPA、Point-JEPA、3D-JEPA、ACT-JEPA、V-JEPA 2）。该线程强调通过对 patch 做掩码和利用潜在表示来降低算力需求，从而支持可扩展的动作追踪与模仿学习。 [来源-twitter](https://x.com/JulianSaks/status/2038316821267530203)

### AI

- **Linux 上的推理速度远快于 Windows（Ollama/LLaMA 测试）** — 一位 Reddit 用户使用 Ollama 搭配 LLaMA 变体，对比了在 Linux（Ubuntu 22.04 LTS）和 Windows 10 上运行 AI 模型的推理性能。在两个基准测试场景中，Linux 的吞吐量高出 72% 至 118%（例如 31 t/s 对比 18 t/s，以及 105 t/s 对比 48 t/s）。帖子邀请其他人分享类似经验，凸显操作系统对 AI 推理性能的影响。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6hb1h/friendly_reminder_inference_is_way_faster_on/)

## ⚡ 快讯速览

- **《Build A Reasoning Model From Scratch》所有章节已开放抢先体验** — 《Build A Reasoning Model From Scratch》的所有章节现已提供早期访问阅读。该书正在制作中，预计未来数月以全彩印刷并带语法高亮的形式正式出版，目前可在 Amazon 上预购。 [来源-twitter](https://x.com/rasbt/status/2038249832020586534)
- **递归自我改进将以阶段跳跃与 S 曲线推进** — 文章认为，递归自我改进会以断断续续的方式沿 S 曲线演进，进展会被周期性的停滞阶段打断。它还强调了 AI 寒冬现象以及下一代芯片上市前不可避免的时间滞后，将技术发展刻画为非线性的过程。 [来源-twitter](https://x.com/tszzl/status/2038359228709306659)
- **Carlini：当前 AI 模型在发现漏洞方面已胜过我本人** — Alex Palcuie 在 X 上提到，他长期关注 Nicholas Carlini 的漏洞研究工作，也很高兴看到 Carlini 公开演讲。Palcuie 引述 Carlini 的话称，当前的 AI 模型在漏洞挖掘方面已经比他更强，他本人以前在这方面多少算是“专业人士”。帖子还链接了一场公开演讲，并突出 Carlini 对模型漏洞的看法。 [来源-twitter](https://x.com/AlexPalcuie/status/2038286354715414881)
- **AI Doomsday Toolbox v0.932 增加基准测试、数据集与 Termux 工作流功能** — 一款用于在安卓上运行本地 AI 的应用迎来一次大版本更新：为本地 LLM 提供基准测试功能，可调整线程数量来优化环境并比较不同配置。它还新增数据集创建器，可以导入文本或 PDF、生成问答对，并以 Alpaca JSON 格式导出数据集，同时加强了 Termux/proot 工作流，支持 SSH 和应用内工具管理，并提供基于本地后端的新 AI agent 工作空间。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s776li/ai_doomsday_toolbox_v0932_update/)
- **欧洲应被视为全球 AI 强国** — Oliver Molander 的帖子主张，欧洲应被认可为全球 AI 强国，质疑将 AI 领导力简单归于其他地区的观点。他认为，众多在 Transformer 和 LLM 发展中起关键作用的人物都是欧洲人，呼吁对当前叙事进行重新审视。 [来源-twitter](https://x.com/OliverMolander/status/2038140606153674842)
- **AI 领域重视 NeurIPS 同行评审，与未审稿工作形成对比** — 有推文将 NeurIPS 视为严谨同行评审的典范，并与对未经过同行评审工作所遭受的批评形成对照。该条内容将此视为 AI 领域强调正式验证的一种体现，同时也承认线上围绕此问题的激烈争论。 [来源-twitter](https://x.com/iScienceLuvr/status/2038351183316930910)
- **围绕 Alec 在 GPT-1 预训练中的角色的争论** — 社交媒体上有人声称，是 Alec 推动了 Transformer 语言模型的预训练，并构建了 GPT-1，认为所有 LLM 都可追溯到他。该帖子反驳说，把他称作预训练的发明者有些言过其实，也有失对其他贡献者的尊重，从而引发关于 AI 发展史与荣誉归属的争议。 [来源-twitter](https://x.com/A_K_Nain/status/2038230148282294665)
- **AI Dot Engineer 新加坡大会将于 5 月 15–17 日举办** — 公告宣布 AI Dot Engineer 大会将在新加坡于 5 月 15–17 日举行。预告称这将是一场由 aiDotEngineer 社区组织的、有趣且聚焦 AI 的聚会，目前尚未披露更多细节。 [来源-twitter](https://x.com/gabrielchua/status/2038201806422200446)
- **在同一机箱中安装两张 RTX 3090 的实操求助** — 一位 Reddit 用户询问，在第一张显卡部分挡住第二个 PCIe 插槽的情况下，如何才能在同一台家用服务器机箱中安装两张 NVIDIA GeForce RTX 3090。TA 列出三种方案，包括使用低位延长线、移动电源（PSU）或采用竖装方案，并说明两张卡都限制在 220W，存在风道与散热的顾虑。用户还考虑重新安置电源以改善气流，并寻求在安装和固定方式上的实际建议。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s748ho/need_help_with_the_logistics_of_two_big_3090s_in/)
- **LocalLLaMA 2026 帖子：“We Are Doomed”** — r/LocalLLaMA 中一则题为“LocalLLaMA 2026”的 Reddit 帖子，只包含用户 /u/jacek2023 发出的简短信息“we are doomed”，并附带讨论区评论的链接。除这种情绪化表述外，帖子几乎未提供关于 LocalLLaMA 2026 的更多信息。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s6r5gn/localllama_2026/)

---

*由 AI News Agent 生成 | 2026-03-29*