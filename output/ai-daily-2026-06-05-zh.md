---
title: "AI 日报 — 2026-06-05"
description: "该公司呼吁全球暂停以防自我提升风险；新模型来临，设备端将有开源视觉语言模型。"
lang: "zh"
pairSlug: "ai-daily-2026-06-05"
---

# AI 日报 — 2026-06-05

> 覆盖 40 条 AI 新闻

## 🔥 今日焦点

### 1. Anthropic 呼吁全球暂停 AI 开发，警示自我改进风险

Anthropic 呼吁在全球范围内暂停 AI 开发，警告其在武器、病原体、大规模失业、监控以及生存性威胁等方面的风险。讨论重点突出了 AI 自我改进的风险，WSJ Tech 的报道以及 Mitt Romney 的一条推文将公众注意力进一步聚焦到这个问题上。[来源-twitter](https://x.com/MittRomney/status/2062921818822816080)

### 2. 头部实验室准备即将发布：Claude Mythos、GPT-5.6、Gemini 3.5 Pro

一则社交媒体帖子称，多家顶级实验室的 AI 模型将在短期内发布：Claude Mythos 的衍生模型正处于红队测试阶段，GPT-5.6 似乎也近在眼前。帖子同时提到，谷歌在 I/O 大会上宣布的 Gemini 3.5 Pro 计划在 6 月初上线，暗示 OpenAI、Anthropic 和 Google 之间的竞争将急剧升温。发帖人预计下周会出现一次“量子飞跃”，伴随更密集的测试与炒作。[来源-twitter](https://x.com/kimmonismus/status/2062969974956884405)

### 3. LFM2.5-VL-Extract：开源权重、可在设备端运行的视觉-语言模型

Liquid AI 发布了两个视觉-语言模型：LFM2.5-VL-1.6B-Extract 和 LFM2.5-VL-450M-Extract，它们被设计为返回结构化 JSON，而不是自由文本。用户输入一张图片和一个字段列表，模型会返回一个干净的 JSON 对象作为响应。两个模型均为开放权重，并被设计为可在任何设备 SoC 上运行。[来源-twitter](https://x.com/liquidai/status/2062686748291846307)

## 📰 重点报道

### LLM

- **ArcANE 评估角色扮演式 LLM 的人物弧线演化** — 研究者提出 ArcANE 基准，用来评估角色扮演语言智能体是否会随角色弧线发展而变化，而非一直停留在固定人设上。该基准覆盖 17 部小说、80 个核心角色，用以测试模型是否与叙事轨迹保持一致，弥补现有基准大多只在单一章节上考察事实回忆的不足。其目标是将评估从静态正确性转向对“轨迹一致”回答的考察。[来源-huggingface](https://huggingface.co/papers/2606.05553)
- **AdaPlanBench 评估 LLM 智能体的自适应规划能力** — AdaPlanBench 是一个动态交互式基准，用来测试大语言模型智能体在世界与用户约束逐步暴露的交互过程中，是否能够自适应规划与再规划。它填补了现有基准对“在不断演化的双重约束下的自适应规划”探讨不足的空白，使对 LLM 规划能力的稳健评估成为可能。[来源-huggingface](https://huggingface.co/papers/2606.05622)
- **Sakana AI 推出自我改进 AI 的 RSI Lab** — 总部位于东京的 Sakana AI 公布了 Recursive Self-Improvement（RSI）Lab，这是一个专门用 AI 重新设计 AI 开发流程的小组。该团队称，在过去两年里已为自我改进 AI 打下基础，包括用于自动化研究的 LLM²、支持自主自我修改的 Darwin Gödel Machine、用于程序演化的 ShinkaEvolve，以及 ALE-Agent、Digital Red Queen 等智能体。此举表明其正推动 AI 研究和网络安全协同进化的端到端自动化进程。[来源-twitter](https://x.com/SakanaAILabs/status/2062948403815030850)
- **Code2LoRA：用于代码 LMs 的超网络 LoRA 适配器** — 代码大模型需要仓库级上下文来解析导入、API 和项目约定。Code2LoRA 引入一种超网络，可为特定代码仓库生成对应的 LoRA 适配器，在推理时零 Token 开销的前提下将仓库知识注入模型。这种方法避免了使用超长输入或针对每个仓库单独微调，同时帮助模型适应不断演化的代码库。[来源-huggingface](https://huggingface.co/papers/2606.06492)
- **Show HN：Lowfat 过滤 CLI 输出，节省 LLM Token** — Lowfat 是一个可插拔的 CLI 过滤器，位于命令和其输出之间，在输出送入 LLM 之前先去噪。它以单一二进制形式运行，并提供插件系统可以针对不同命令定制过滤规则，开源托管在 GitHub（zdk/lowfat）。作者称在两个月的实际使用中，在 kubectl、grep、docker 等常用命令上显著节省了 Token 成本。[来源-hackernews](https://github.com/zdk/lowfat)
- **OpenLumara：面向本地模型的轻量级 AI Agent** — OpenLumara 是一个 Token 高效的 AI Agent，专为本地 LLM 设计。作者声称它比 OpenClaw 和 Hermes 更快、更轻量且更安全，从零开始打造，能在普通硬件上结合本地模型运行，并被日常用于日历和任务管理。koboldcpp 与 LocalLLaMA 社区已在实际使用该项目。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txxgpq/openlumara_a_different_kind_of_ai_agent_written/)
- **Gemma 4 QAT 基准：更快、更省 VRAM、无质量损失** — 一项在 AMD 7900 XTX 上对 Gemma 4 QAT 模型进行的 A/B 对比表明：在使用 Q4 权重替代 BF16 时，推理速度更快、显存占用更低，同时模型保真度未出现明显下降。作者在多种工作负载下进行了测试，并记录了墙钟时间趋势，完整分析可在 kmarble.dev 查看。该结果凸显了量化感知训练对较小 Gemma 4 变体的实用价值。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txxd7c/gemma_4_qat_benchmark_results_amd_7900_xtx_faster/)
- **将 KV Cache 卸载到内存，让 GPU 容纳 65K 上下文的 LLaMA** — 一篇 Reddit 帖子探讨使用 llama.cpp 的 -nkvo 选项将 KV Cache 卸载到系统内存，从而在完整模型仍驻留 GPU 的前提下实现 65K 上下文，代价是吞吐量下降。作者在一块 16GB 显存、32GB 内存的 RTX 5060 Ti 上测试了 Qwen3.6-27B-IQ4_XS，比较了启用与禁用卸载两种配置下 TPS 的变化。结论是：在内存占用与速度之间存在权衡，卸载可以解决容量问题，但要付出性能代价。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txpqru/maybe_kv_cache_offload_to_ram_isnt_bad/)
- **BeeLlama.cpp 引入 KVarN KV-Cache 量化，提升 LLaMA 跑分** — 一名独立开发者称在其 llama.cpp 分支（BeeLlama.cpp）中实现了华为 KVarN KV-Cache 量化。他发布了 v0.3.2 预览版以及预构建二进制，并声称在 RTX 3090 上对 Qwen 3.6 27B 和 Gemma 4 31B 测试时，实现了 3–5 倍 KV Cache 压缩和实际速度提升。帖子指出该实现与原始 KVarN 论文保持一致，并分享了具体使用参数。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txlhxu/i_implemented_kvarn_in_my_llamacpp_fork_and_ran/)
- **Qwen3.6-35B-A3B 在 8GB RTX 4060 上运行：调优心得** — 一项实验在一台搭载 8GB RTX 4060 的笔记本上运行 35B MoE 模型 Qwen3.6-35B-A3B。作者报告称，由于该模型采用 10 层注意力 + 40 层 gated delta net 的混合架构，一些常规优化（如 TurboQuant 和 Flash Attention）反而可能有害；成功的关键在于使用 --no-mmap、预留足够显存空间，并关闭 CPU 占用较高的应用。作者声称获得约 26% 的推测式解码加速，与社区基准略有出入，并在文中分享了最终配置和环境细节。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txwff3/running_qwen3635ba3b_on_a_laptop_rtx_4060_8gb/)

### Multimodal

- **VideoKR 发布 31.5 万样本视频知识推理数据集** — VideoKR 推出首个专为知识密集与推理密集型视频理解设计的大规模训练语料。该数据集包含 31.5 万条视频推理样本，覆盖 14.5 万个 CC 授权的专家领域视频，并通过人类参与的流程生成逐步加深的 CoT 推理链。其目标是在样本和解释两方面同时保证难度、多样性与可靠性，详细说明已发布在 Hugging Face。[来源-huggingface](https://huggingface.co/papers/2606.05259)
- **Google Gemini Live 增强实时图像生成与编辑功能** — Google Gemini 现已在 Gemini Live 中支持实时创建和编辑图像。用户可打开 Gemini App、点击 Live、共享摄像头并描述想要看到的内容，适用场景包括房间布置、数学辅导以及表情包创作。该功能凸显了在移动端/内嵌工作流中进行实时多模态图像生成和编辑的能力。[来源-twitter](https://x.com/GeminiApp/status/2062936486509785385)
- **Gemini Omni 支持视频中文字的同步渲染** — Google 的 Gemini Omni 不仅可以提升文本准确性，还能在视频中同步渲染和动画化文本。它提供文本类型、位置、动画、曝光等多种可调选项，还支持逐词提示模式，使每个词以不同的动画风格和节奏出现。帖子同时提到已经支持 HLS 播放。[来源-twitter](https://x.com/Google/status/2062925430290526486)
- **韩国网络论坛将用 AI 审查工具扫描所有图片** — 有报道指出，韩国计划要求在线社区部署基于 AI 的图像审查工具，对所有上传图片进行扫描。此举可能给平台和用户带来新的隐私和内容审核负担，引发人们对准确性、审查范围以及执行方式的担忧。[来源-hackernews](https://discuss.privacyguides.net/t/south-korean-online-communities-will-need-to-scan-every-images-with-ai-censorship-tools/38341)

### LLMs

- **Unsloth 发布面向 Gemma 4 的 MTP GGUF 权重** — Unsloth 为 Gemma 4 发布了多组 MTP GGUF 权重，覆盖 31B、26B-A4B 和 12B 三个规模，并提供 Q8、F16 和 BF16 精度。权重托管在 Hugging Face 上，每个规模对应独立仓库。该 Reddit 帖子由用户 /u/okoyl3 提交。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txnhqp/unsloth_just_dropped_mtp_gguf_weights_for_gemma_4/)

### Open Source

- **dots.tts 2B：RedNote 发布的开源 SOTA 语音合成模型** — RedNote 在 Apache 2.0 许可下发布了参数规模为 2B 的 dots.tts，提供一个无需 Codec Token、端到端连续表示的 TTS 流水线，并支持 48 kHz 语音合成。该系统支持零样本音色克隆以及无需音素流水线的直接文本到语音。演示资源包括博客、GitHub 仓库以及 arXiv 技术报告。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txwbge/dotstts_2b_sota_tts_from_rednote/)
- **NVIDIA Cosmos：面向物理 AI 的开放平台** — NVIDIA Cosmos 是一个由世界模型、数据集和工具构成的开放平台，使开发者能够为机器人、自动驾驶汽车、智慧基础设施等构建 Physical AI。该项目包含模块化组件，例如模型架构、生成器、推理器，并可与 Diffusers、vLLM-Omni、Transformers 和 NIM 等框架集成。[来源-github](https://github.com/NVIDIA/cosmos)
- **Open Notebook：开源、本地运行的 Notebook LM 替代方案** — Open Notebook 是一个注重隐私、开源且可本地运行的 Notebook LM 实现。它支持 18+ 家 AI 服务商，多模态内容处理，以及专业播客生成等功能，重点强调用户对数据的控制与使用灵活性。[来源-github](https://github.com/lfnovo/open-notebook)
- **Anthropic 发布开源 AI 驱动漏洞发现框架** — Anthropic 发布了一个开源框架，旨在让 AI 参与软件漏洞发现流程。该项目名为 defending-code-reference-harness，为在代码分析工作流中集成 AI 提供工具，以识别潜在安全缺陷。[来源-hackernews](https://github.com/anthropics/defending-code-reference-harness)

### Industry

- **Agents.md 标准已存在，但 Anthropic 拒绝采纳** — 社区已有面向 AI 代码智能体指令的 Agents.md 标准，OpenAI Codex 已支持，而 Claude Code 则使用 CLAUDE.md。帖子指出 Anthropic 拒绝采纳 Agents.md，引发对全行业统一标准的呼声。一条社区注释声称 AGENTS.md 是由数千个 GitHub 项目采用的行业标准，尽管 Claude Code 并未原生支持。[来源-twitter](https://x.com/theo/status/2062741740910702764)

### AI Tools

- **阿里巴巴发布 Open Code Review：AI 驱动的 CLI 代码审查工具** — Open Code Review 是一个使用 AI 帮助开发者进行代码审查的命令行工具。该项目由阿里巴巴发布并托管在 GitHub 上，欢迎社区共同参与。它在 Hacker News 上引发了大量讨论和关注。[来源-hackernews](https://github.com/alibaba/open-code-review)

### AI Safety

- **NSA 使用 Anthropic Mythos 执行网络攻击行动** — 《金融时报》报道称，美国国家安全局正在使用 Anthropic 的 Mythos 模型来辅助网络行动。此举凸显了先进 AI 在国家支持网络能力中的角色及其安全隐患。Anthropic 和相关方尚未公开确认细节，这也突出了关于 AI 治理以及政府使用第三方模型的问题争议。[来源-hackernews](https://www.ft.com/content/d02d91b3-2636-454e-9442-dc7e69f51815)

### Hardware

- **LLM 服务器正式装机完成：EPYC 9575F + 4× RTX 3090** — 用户 Nalthis 完成了一台高端 LLM 推理服务器的搭建，配置包括 EPYC 9575F、768GB DDR5 ECC 内存以及四块 RTX 3090 GPU。该机预计用于运行 vLLM 和 llama.cpp，以支持太空模拟类项目的 NPC 规划，显卡功耗被限制在 250W，作者仍在进行持续散热测试。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tx9tf2/finally_finished_my_llm_server_epyc_9575f_4_rtx/)

## ⚡ 快讯速览

- **Schmidhuber：随着开源与算力成本下降，AI 护城河正在消失** — Jürgen Schmidhuber 认为，随着开源生态发展与廉价算力普及，AI 护城河正在被抹平。他以 DeepSeek 与 Sputnik 为例，说明竞争优势正在削弱，并将 AI 的发展轨迹类比智能手机领域：计算成本大约每五年下降一个数量级。他还指出，大型软件巨头可能会逐渐变成类似公用事业的存在，在 AI 数据中心上进行巨额投资。[来源-twitter](https://x.com/ethanCaballero/status/2062792827487097233)
- **TIDE 通过模板实现多问题的前瞻性发现** — 论文提出 TIDE 框架，用于在更广泛的用户上下文中主动发现多个隐藏问题，而不局限于用户的显性请求。它通过模板引导的迭代，将问题发现过程锚定在跨文档、工具和代码的支撑证据上。该方法旨在挖掘用户可能忽略的共存问题。[来源-huggingface](https://huggingface.co/papers/2606.04743)
- **微软希望用户对其 AI 助手 Scout 上瘾** — 一篇 Hacker News 文章称，微软试图让用户对其 AI 个人助手 Scout 形成依赖。文章将 Scout 视为一个“上瘾型”参与工具，引发关于 AI 责任与隐私的讨论。其关注点在于 AI 助手对用户依赖性的影响及其后果。[来源-hackernews](https://disassociated.com/microsoft-users-addicted-ai-personal-assistant/)
- **Ask HN：你使用什么样的 AI 开发栈与工作流？** — 一篇 Ask HN 长帖征集适用于线下入门工作坊的现代 AI 开发工具链和工作流建议。作者是一位偏爱开源与 TDD 等实践的资深开发者，希望找到既适合新手又能满足使用 AI 工具的资深软件工程师的通用方案。[来源-hackernews](https://news.ycombinator.com/item?id=48413629)
- **Claude 是否增加了 rsync 的 Bug 数量？** — 一篇分析文章质疑 Anthropic 的 Claude 是否导致 rsync 文件传输工具中的 Bug 增多，并总结了观察到的行为特征与潜在失效模式。讨论汇总了 rsync 分析博客及 Hacker News 线程中的观点，强调在系统工具中部署 LLM 所带来的风险，以及严格验证的重要性。[来源-hackernews](https://alexispurslane.github.io/rsync-analysis/)
- **把 LLM 微调到写出“1995 年风格”的文档** — 文章探讨如何通过微调大语言模型来生成具有 1995 年怀旧风格的软件文档。作者讨论了这种方式在保持一致性和与旧式工具兼容方面的潜在好处，同时也分析了在可读性与现代文档标准间的权衡。[来源-hackernews](https://passo.uno/fine-tuning-docs-llm/)
- **五角大楼运行针对拉美地区的 AI 宣传机器** — 《The Intercept》报道，五角大楼运营着一个面向拉丁美洲的 AI 驱动宣传网络。该系统通过自动化信息发布与放大来影响区域信息生态与公众舆论。专家警告称，政府主导的 AI 信息操作对伦理、透明度与民主进程构成风险。[来源-hackernews](https://theintercept.com/2026/06/02/la-tilde-propaganda-latin-america-pentagon/)
- **Gemma 4 12B 并非不能写代码——需要正确 chat 模板** — 一则 Reddit PSA 指出，Gemma 4 12B 的工具调用问题可以通过使用特定 chat 模板修复。若要在 llama.cpp 中应用该修复，用户需从源码编译、下载自定义 chat 模板，并在运行 llama-server 时使用指定的 chat-template-file 参数。帖子提醒结果因人而异，但一旦应用模板，工具调用 Bug 基本消失，从而能正常评估该模型的代码能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txro73/psa_gemma_4_12b_is_not_completely_broken_for/)
- **建议 LLM 相关帖子使用注明 VRAM/统一内存的 Flair** — 一则 Reddit 帖子认为，高速内存（VRAM/统一内存）的容量是决定 LLM 性能的最关键因素。作者指出，很多部署都依赖大容量内存，在帖子中包含硬件细节可以提升内容的相关性和可筛选性。其提议是通过帖子 Flair 标出 VRAM/RAM 规格，以提高社区内容的实用度。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txjy24/suggestion_this_sub_should_have_post_flairs_that/)
- **llamacpp 服务器现在可在 30 秒内热切换模型** — llamacpp 服务器现已支持精简且快速的模型热切换 API，并可配合 OpenWebUI 和 Hermes 使用。模型切换可在 30 秒内完成，相比早期部署有显著改进。帖子同时提到在 gemma 模型测试中遇到的小问题，但整体强调了速度提升，并展示了运行服务器的示例命令。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txmg8q/fyi_llamacpp_server_can_hot_swap_models_nowadays/)
- **大学要价 30 万美元教授的技能，LLM 却能免费完成** — 一则颇具争议的帖子指出，高等教育学位费用高达 30 万美元，却主要教授一些 LLM 能免费完成的技能。发帖人呼吁就“在 AI 时代，高等教育是否是对资本的错误配置”这个问题展开坦诚讨论。[来源-twitter](https://x.com/PeterDiamandis/status/2062882655692009961)
- **程序员开始为 Claude 写文档，而不是为同事** — 帖子认为，为 Claude——也就是 AI 模型——编写文档，可能比为人类队友写文档更关键。作者分析了面向 AI 的文档如何提升复现性、提示质量以及项目引导，并质疑以人为中心的传统文档实践，主张转向以 AI 为核心的文档记录方式。[来源-hackernews](https://blog.plover.com/2026/03/09/#documentation-wins-2)
- **Reddit 帖子预测 Qwen 将发布最强 GD 模型** — 一名 Reddit 用户用戏谑口吻推测，AI 模型军备竞赛最终会以 Qwen 发布史上最强 GD 模型收尾，超越包括 Google 在内的竞争对手。帖子在表达对 Qwen 感谢与期待的同时，也用反讽手法放大了围绕“终极顶级模型”的各种炒作。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1txufl9/dont_act_like_yall_aint_thinking_it_im_just/)
- **像对待 LLM 一样对待自己：只回答付费用户的问题** — 有帖子鼓励人们把自己当作 LLM：每次互动都会消耗 Token，因此不应回应低质量提示，除非对方是“付费订阅者”。它把注意力比作一种付费资源，主张对“提示”进行门槛管理和筛选。[来源-twitter](https://x.com/Yuchenj_UW/status/2062745651201630543)

---

*由 AI News Agent 生成 | 2026-06-05*