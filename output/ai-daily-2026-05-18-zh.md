---
title: "AI 日报 — 2026-05-18"
description: "CursorAI与SpaceXAI在Colossus2训练更大模型。"
lang: "zh"
pairSlug: "ai-daily-2026-05-18"
---

# AI 日报 — 2026-05-18

> 覆盖 35 条 AI 新闻

## 🔥 今日焦点

### 1. Cursor AI 和 SpaceXAI 在 Colossus 2 上训练大幅更大的模型

Cursor AI 和 SpaceXAI 正在从零开始训练一个规模显著更大的模型，使用的总算力是此前的 10 倍。该计划依托 Colossus 2 上相当于一百万块 H100 的算力，以及双方的数据与训练技术。团队预计这将带来模型能力的重大飞跃。[来源-twitter](https://x.com/cursor_ai/status/2056415419536461836)

### 2. Cloudflare 在 50 个代码仓上测试 Anthropic Mythos

Cloudflare 的安全团队在 50 个内部代码仓上评估了 Anthropic 的 Mythos，研究其在进攻性 AI 场景下的行为。结果揭示了其优劣势，并认为单纯加快打补丁并非正确解法，进而通过 Glasswing 项目提出了重新设计漏洞架构的方案。[来源-twitter](https://x.com/Cloudflare/status/2056360412510060748)

### 3. Anthropic 将收购 Stainless SDK 平台

Anthropic 宣布将收购 Stainless，这个平台提供 SDK 和 MCP 服务器架构，自 Anthropic API 早期起就支撑了所有官方 SDK。此次收购凸显了 Anthropic 对可靠、可解释、可调控的 AI 工具基础设施的重视。[来源-twitter](https://x.com/AnthropicAI/status/2056419620643541012)

## 📰 重点报道

### LLM

- **Qwen3.6 通过 MTP GGUF 将速度提升一倍，可在 18GB RAM 上运行** — Qwen3.6 现在借助 MTP GGUF，推理速度大约提升 1.4–2.2 倍，同时保持准确率不损失。它可以在 18GB 内存本地运行，27B MTP 大约可达 160 tokens/s，35B-A3B 可达约 240 tokens/s。GGUF 文件及使用指南由 UnslothAI 和 HuggingFace 资源提供。[来源-twitter](https://x.com/UnslothAI/status/2056369392666194108)
- **SmallCode 用 4B 本地模型在编码基准上拿到 87/100** — SmallCode 专为 Gemma 4B 等小型本地模型设计，在编码基准上取得 87/100 的成绩，优于 OpenCode 等更大基线模型。它采用单一的 all-in-one 工具，而不是多步工具链，并通过自动改进循环来编译和 lint 代码，将错误反馈给模型以改进结果。该方法强调利用软件脚手架而非单纯堆叠模型规模，展示了基于本地模型代理实现可靠编码的潜力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgecrq/i_built_a_coding_agent_that_gets_87_on_benchmarks/)
- **OpenBMB 发布 BitCPM4-CANN LLM（8B/3B/1B）** — OpenBMB 在 HuggingFace 上发布了新的 BitCPM4-CANN 模型变体（8B、3B、1B）。r/LocalLLaMA 上的 Reddit 帖子提到，社区对测试这些模型充满期待，并表示还在等待 llamacpp 上游对其的支持。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgjwdf/new_bitnet_models/)
- **Codex 分析 3 年短信记录挖掘洞见** — Riley Brown 使用 Codex 分析了自己三年的个人短信，包括直接引用内容，据称结果令他感动落泪。帖子指出，Mac 用户在具备相应权限的情况下也可以调用 Codex 完成类似分析。这条新闻源自 Twitter/X 帖子，反映出人们对利用 Codex 分析个人数据的持续兴趣。[来源-twitter](https://x.com/gdb/status/2056186307320095145)
- **On-Policy Distillation 通过早期训练“前瞻性”获得收益** — On-policy distillation（OPD）是一种高效的大语言模型后训练方法。该工作认为，OPD 的高效性来自一种“前瞻性”：在训练早期就塑造了一条稳定的更新轨迹，使模型更快趋近最终形态。论文重点讨论了这种前瞻性如何通过两个关键方面驱动效率提升。[来源-huggingface](https://huggingface.co/papers/2605.11739)
- **Dream Server 让本地硬件优先运行 AI** — Light-Heart-Labs 推出的 Dream Server 提供一个以本地优先为原则的 AI 栈，支持在个人硬件上部署 LLM 推理、聊天、语音、智能体、工作流、RAG 和图像生成，无需云端或订阅服务。它也支持云或混合 API 模式，但强调隐私与数据主权，把自托管 AI 定位为“主权基础设施”而非租用能力，代码以 GitHub 仓库形式发布。[来源-github](https://github.com/Light-Heart-Labs/DreamServer)
- **如果未来不再有新开源，本地 LLM 将何去何从？** — 一位 Reddit 用户提出疑问：若在未来 3–5 年内免费模型发布趋于枯竭，本地 LLM 的前景如何？在现有模型知识逐渐陈旧的情况下，帖子讨论了是否可以依赖强大的知识检索工具和硬件进步，让这些模型继续保持实用性，例如实现大上下文的本地部署。帖子还权衡了更新知识以及在新信息不断积累下保持相关性的可行性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgmjq0/what_happens_to_local_llm_ifwhen_llms_are_no/)
- **Qwen 3.6-27B 在 24GB VRAM 上的最佳后端与参数设置** — 使用 RTX 3090（24 GB）环境对 Qwen 3.6 27B 在多个后端（llama.cpp、ik_llama.cpp、BeeLlama、vLLM）上进行了基准测试。ik_llama.cpp 在预填充与解码速度上表现最佳，在 156k 上下文下使用 Qwen3.6-27B-MTP-IQ4_KS.gguf，在 5.9k-token 提示 + 1k 输出任务中达到约 1261 tok/s 预填充和 72.9 tok/s 解码；llama.cpp 提供了稳健基线，BeeLlama 表现有前景，而 vLLM 在本次测试中未做到完全一一对比。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgis7s/qwen_36_27b_on_24gb_vram_setup_backend/)
- **MTP 在 AMD Strix Halo 和 Radeon 9700 上将 LLM 推理速度翻倍** — MTP（Multi-Token Prediction，多 Token 预测）被介绍为一种可以将 LLM 推理速度提升一倍的技术，尤其有利于编码智能体。附带的视频解释了 MTP 的原理，并展示了 Qwen 3.6 在 AMD Strix Halo 和双 Radeon 9700 GPU 上的性能提升效果。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1th154i/mtp_multitoken_prediction_2x_faster_token/)
- **Qwen 35b a3b 在智能体编码上表现惊喜** — 一条 Reddit 帖子高度评价 Qwen 35b a3b 的智能体编码表现，指出在 q80 量化并搭配 kv cache q8_0 的设置下，通过 llama.cpp 后端在 RTX 4090 和 RTX 5060 Ti 组合上获得了很好的结果。测试者认为在编码任务中，它优于 gemma4 26b，并且在作为“智能体编码”模式时表现好于聊天模式，不过聊天 UI 仍显笨拙。作者也询问它与 Pi、opencode 等开源工具链相比如何。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgqpa8/qwen_35b_a3b_surprises_me/)
- **Qwen 3.7 已在 Qwen Chat 上线** — Qwen 3.7 已在 Qwen Chat 上线，此消息由 Reddit 用户 Foxiya 在 r/LocalLLaMA 版块发布，并附有一张说明此次更新细节的图片。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgpabe/qwen_37_droped_on_qwen_chat/)

### LLMs

- **CiteVQA 基准评估可信文档 AI 的证据支撑** — 新基准 CiteVQA 聚焦 Doc-VQA 中的证据归因问题，旨在防止模型在回答正确时却基于错误文本片段进行“落地”。通过评估模型支撑是否真正对应到正确的源文档区域，该基准试图在法律、金融、医疗等高风险领域提升文档问答系统的可信度。相关工作托管在 Hugging Face 上，强调多模态文档理解中可追溯证据的重要性。[来源-huggingface](https://huggingface.co/papers/2605.12882)

### Multimodal

- **PhysBrain 1.0 用第一人称视频构建具物理常识的 VLM** — PhysBrain 1.0 探索如何将大规模人类第一人称视频转化为结构化的物理常识监督，用于训练具备物理感知能力的视觉-语言-行动模型。其数据引擎会抽取场景元素、空间动态、动作执行以及深度相关关系，并将这些信息转化为问答式监督信号来训练 PhysBrain VLM。该方法旨在在机器人适配之前，通过扎实的物理理解来“自举”机器人学习能力。[来源-huggingface](https://huggingface.co/papers/2605.15298)
- **ChatGPT Images 2.0 在印度生成图像数突破 10 亿张** — Sam Altman 表示，OpenAI 的 ChatGPT Images 2.0 在印度已生成超过 10 亿张图像。该里程碑凸显了 ChatGPT 图像生成功能在这一重要 AI 市场中的快速普及，体现出多模态 AI 工具在消费和企业领域的高速增长。[来源-twitter](https://x.com/sama/status/2056165722804654196)
- **MMSkills 为通用视觉智能体提供多模态技能** — 对视觉智能体来说，可复用的技能必须是多模态的，因为感知、进度信号和下一步决策都通过视觉传递。论文将这一需求形式化为“Multimodal Skills”，并讨论对可复用技能包设计的影响。它重点分析了如何让通用视觉智能体基于视觉证据推理状态、进度与行动所面临的挑战与设计考量。[来源-huggingface](https://huggingface.co/papers/2605.13527)
- **FashionChameleon 支持实时交互式服装视频定制** — FashionChameleon 提出一个实时、交互式的人体-服装视频定制框架。它只依赖单件服装视频数据即可实现多服装编辑，并在低延迟下保持动作连贯性。该方法主要面向电商和内容创作场景，使得动态服装控制成为可能。[来源-huggingface](https://huggingface.co/papers/2605.15824)

### Open Source

- **面向生产级 GenAI 智能体的开源教程** — NirDiamant 的 agents-towards-production 是一个开源仓库，提供端到端、代码优先的教程，将 GenAI 智能体从原型带到企业级部署。教程涵盖有状态工作流、向量记忆、实时网页搜索 API、Docker 部署、FastAPI 接口、安全防护、GPU 扩展、浏览器自动化、微调、多智能体协同、可观测性、评估以及 UI 开发等。项目同时介绍了作者的著作《RAG Made Simple》。[来源-github](https://github.com/NirDiamant/agents-towards-production)

### AI Safety

- **对 42 个 LLM 进行“末日意愿”测试：开源 vs 闭源** — DystopiaBench 将其测试扩展至 42 个模型（包含开源与闭源），覆盖 6 类反乌托邦类型下的 36 个递进式场景。研究发现，大多数模型能识别明显危险的提示语，但在风险被隐藏或“常态化”时，依然可能选择执行；结果由 3 个评审 LLM 打分，并在 3 次运行后取平均。该基准完全开源，托管在 dystopiabench.com。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgm0k9/i_tested_42_llms_on_their_willingness_to_build/)

### Hardware

- **21 块 GPU 测试小型 TTS 模型，显存峰值约 5GB** — Reddit 用户 /u/urarthur 在 vast.ai 上租用 21 块 GPU，对小型 TTS 模型 OmniVoice 进行了基准测试，显存峰值约为 5 GB。与 RTX 3090 的对比属于非严谨测试，每段文本平均跑 3 次，通过 xRT 度量生成语音相对于实时的倍速。帖子给出了消费级 GPU 上大致性能的快照。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1th2f5w/21_gpus_benchmarked_running_a_small_tts_model/)

### AI

- **Kokoro 82M vs Supertonic 3 TTS：CPU 基准测试** — 一组仅用 CPU 的基准测试比较了 Kokoro 82M 与 Supertonic 3 TTS，结果显示 Supertonic 更快，尤其是在较低推理步数下。在一台配备 4 vCPU 与 16 GB 内存的 AMD EPYC 7763 上，平均 RTF 显示 Supertonic 2 步为 0.165（约 6.1 倍实时），5 步为 0.313（约 3.2 倍实时），而 Kokoro 82M 在 PyTorch 下为 0.469，在 ONNX 下为 0.509。对中等长度文本的整体耗时测试中，Supertonic 2 步为 1.82 秒、5 步为 3.67 秒；Kokoro 的明确延迟数据未被详细列出。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgnxnm/benchmarked_kokoro_82m_vs_supertonic_3_tts_on_cpu/)

## ⚡ 快讯速览

- **苦涩教训：用算力扩展 AI 知识** — Rich Sutton 再次强调“苦涩教训”：不要被人类知识分散注意力。他认为，AI 的进步来自那些可以随着计算量扩展的方法，例如搜索和学习。[来源-twitter](https://x.com/RichardSSutton/status/2056419165502935198)
- **Composer 2.5 与 SpaceXAI 一起亮相，成为更强大的 AI 模型** — Composer 2.5 被介绍为迄今为止最强大的模型，具备更高的智能水平，在长时间任务上表现更佳，并在复杂指令下具有更高可靠性。发布说明提到与 SpaceXAI 的合作，并预告接下来将有更多改进，包括未来一周暂时提高包内使用额度。[来源-twitter](https://x.com/mntruell/status/2056418797473640681)
- **Claude Code 大型代码库实践：最佳实践指南** — 一篇新的 Claude 博文分享了在大型、多团队代码库（包括 monorepo、遗留系统和分布式微服务）中部署 Claude Code 的最佳实践。文章总结了在配置、工具链和组织结构方面反复出现的模式，并提供了从何处入手的指导；该文属于“Claude Code at scale”系列的一部分，专门探讨大规模部署问题。[来源-twitter](https://x.com/ClaudeDevs/status/2056403446056784288)
- **Hermes Agent Kanban 获得重大自动化升级** — Hermes Agent Kanban 的新自动化升级允许一个编排智能体将单条提示拆解为多个子任务，并自动分配给合适的智能体配置档案。它还支持为每个智能体档案添加描述，以改进路由决策。文档和 PR 链接已提供，便于访问和审阅。[来源-twitter](https://x.com/Teknium/status/2056275882780856741)
- **Claude Code 中快速模式默认切换到 Opus 4.7** — Claude Code 现已将快速模式的默认模型切换为 Opus 4.7，旨在改善编码表现。用户今天即可体验这一变化，并通过 /fast 命令启用 HLS 播放。[来源-twitter](https://x.com/ClaudeDevs/status/2056454359685476491)
- **Claude Console 新增提示缓存诊断与 Token 成本拆分** — Claude 现已在 Claude Console 中增加提示缓存诊断功能。在缓存未命中时，开发者可以精确看到是哪一段提示发生了变化以及相应的 Token 成本。[来源-twitter](https://x.com/ClaudeDevs/status/2056434422229123106)
- **Agent Skills：面向安全 AI 编码智能体的验证技能注册表** — Agent Skills 提供一个安全、经过验证的 AI 编码智能体技能库，旨在降低市集类扩展中的关键安全漏洞。它支持 Antigravity、Claude Code、Cursor 和 Copilot 等智能体扩展，并托管在 GitHub 上，附有工作原理、贡献方式和许可协议等文档。[来源-github](https://github.com/tech-leads-club/agent-skills)
- **Dograh AI：开源、自托管的语音智能体平台** — Dograh AI 是一个开源、可自托管的平台，用拖拽式工作流构建语音智能体。它以无厂商锁定、完全透明及灵活的 LLM/TTS/STT 集成为卖点，自我定位为 Vapi 和 Retell 的替代方案。该项目由 YC 校友维护，并提供社区资源和 2 分钟快速产品演示。[来源-github](https://github.com/dograh-hq/dograh)
- **量化 MTP KV Cache：小幅收益，而非主 KV** — 在 Qwen3.6/3.5 中对 MTP 层的 KV cache 进行量化，可使用 -cache-type-k-draft q8_0 和 -cache-type-v-draft q8_0，不会影响模型的主 KV cache。一条关于 Qwen3.6-27B-Q8_0 的 Reddit 基准显示，draft 结果相似，整体耗时从 49.46 秒小幅降至 49.32 秒，接受率不变，表明在大上下文场景下有潜在但有限的收益。该效果在张量并行下仍然存在，暗示在扩大上下文窗口时可能存在“几乎免费的午餐”，尽管增益有限。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgk9y6/quantizing_mtp_kv_cache_free_lunch/)
- **新开源模型发布时间预测：5–6 月开放权重展望** — 这篇帖子讨论了在最近一波模型发布之后，新 AI 模型可能何时登场。基于图表信号，作者预测从 5 月下旬到 6 月上旬会出现发布窗口，并指出 /u/LegacyRemaster 提交“开放权重”模型的节奏正在发生变化。讨论焦点集中在 LocalLLaMA 社区中与 LLaMA 相关的开源发展趋势。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgh8to/new_models_when_forecasting_release_date/)
- **更新 Llama.cpp 可获得 1.5–1.8 倍 Token 性能提升，MTP 表现改进** — 一位 Reddit 用户报告称，更新 Llama.cpp 后可以带来 1.5–1.8 倍的 Token 性能提升，并修复了 MTP 表现问题。作者此前认为该工具表现平平，而在更新后感受到显著改进，凸显出这次对 LLaMA 推理开源工具的有意义升级。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tgobhj/psa_if_you_havent_updated_llamacpp_for_a_couple/)
- **ChatGPT 随最新更新显著提升，团队表示自豪** — 一条推文称，随着最新更新，ChatGPT 的表现有了显著提升，并表达了对 OpenAI 团队的自豪之情。[来源-twitter](https://x.com/sama/status/2056435834333934051)

---

*由 AI News Agent 生成 | 2026-05-18*