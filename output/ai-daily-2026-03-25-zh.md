---
title: "AI 日报 — 2026-03-25"
description: "新音乐模型发布、全自动AI研究、人与AI代理力对比显著，AI<1%。"
lang: "zh"
pairSlug: "ai-daily-2026-03-25"
---

# AI 日报 — 2026-03-25

> 涵盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. Google DeepMind 发布 Lyria 3 Pro 音乐模型

Google DeepMind 宣布推出最新、也是目前最先进版本的 Lyria 音乐模型 Lyria 3 Pro。此次更新支持生成最长 3 分钟的音乐曲目，并提供更强的创作控制能力，同时将 Lyria 的可用性扩展到更多 Google 产品中，包括对 HLS 播放的支持。 [来源-twitter](https://x.com/Google/status/2036836307612119488)

### 2. The AI Scientist：全自动 AI 科研成果登上 Nature

Sakana AI Labs 的 AI Scientist 由基础模型驱动，可从研究构思到论文撰写，自动化整个机器学习研究生命周期。根据介绍，AI Scientist-v2 产出了首篇完全由 AI 生成、并通过严格人工同行评审的论文。发表在 Nature 的论文《The AI Scientist: Towards Fully Automated AI Research》详细描述了这一里程碑成果以及支撑自动化 AI 研究的基础模型编排机制。 [来源-twitter](https://x.com/SakanaAILabs/status/2036840833690071450)

### 3. ARC-AGI-3：人类得分 100%，AI 在智能体基准中得分不足 1%

ARC-AGI-3 被称为目前全球唯一尚未“打满分”的智能体智能基准测试。在已公布的结果中，人类得分为 100%，而 AI 得分不足 1%，凸显出距离真正 AGI 仍存在巨大差距。不同于传统基准，ARC-AGI-3 更关注模型“如何学习”，而非“已经知道什么”。 [来源-twitter](https://x.com/arcprize/status/2036860080541589529)

## 📰 重点报道

### LLM

- **Apple 深度接入 Gemini，并在本地蒸馏小模型** — 有消息称 Apple 现已获得对 Google Gemini 模型的完整深度访问权限，从而可以在内部将 Gemini 的知识蒸馏到更小的任务定制模型中。这些小型模型有望直接在 iPhone 等设备上运行，甚至学习 Gemini 的内部推理方式，以提升表现。这种深度访问标志着边缘设备利用大型语言模型方式的一次重大转变。 [来源-twitter](https://x.com/kimmonismus/status/2036839405361738174)
- **Google DeepMind 与 Agile Robots 合作部署 Gemini 基础模型** — Google DeepMind 宣布与 Agile Robots 达成研究合作，将其 Gemini 基础模型与 Agile Robots 的机器人硬件集成，目标是驱动新一代更强大的工业机器人。此次合作旨在部署更加有用、能应对复杂工业挑战的机器人系统。 [来源-twitter](https://x.com/demishassabis/status/2036726283464581343)
- **他们正在把 Claude 打造成 ChatGPT 理想中的那个 App。** — Claude 的移动应用现已将工作流工具直接带到手机上，用户可以通过 Claude 访问 Figma 设计稿、Canva 幻灯片以及 Amplitude 数据看板。此次更新将 Claude 定位为更深度集成的效率助手，对标的是曾希望将 ChatGPT 打造成移动工作流伙伴的思路。下载链接 claude.com/download 邀请用户体验这款移动应用。 [来源-twitter](https://x.com/kimmonismus/status/2036856308410773803)
- **Supermemory AI 推出极速记忆与上下文引擎** — Supermemory 提供一个面向 AI 的记忆与上下文层，将 RAG 和文件处理整合为单一系统。它可从对话中自动学习、提取事实、构建用户画像，处理信息更新与冲突，并在信息过期后自动遗忘，以在大约 50 毫秒每次调用的速度下提供合适上下文。据称在 LongMemEval、LoCoMo 和 ConvoMem 等 AI 记忆基准上取得顶级性能。 [来源-github](https://github.com/supermemoryai/supermemory)
- **Google TurboQuant 声称实现 6 倍 KV Cache 压缩、8 倍注意力加速** — Google 推出 TurboQuant，声称在零精度损失的前提下，将 KV Cache 压缩至 1/6，并在 H100 GPU 上实现最高 8 倍的注意力计算加速，该工作已在 ICLR 2026 上发表。相关帖子询问是否已有开发者实际实现，并讨论其在真实场景中的收益是否能达到论文中的基准表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3ffzo/has_anyone_implemented_googles_turboquant_paper/)
- **Liquid AI LFM2-24B-A2B 在 WebGPU 浏览器中约跑出 50 tokens/s** — Liquid AI 基于 MoE 的 LFM2-24B-A2B 模型在搭载 M4 Max 的浏览器中通过 WebGPU 推理，速率约为每秒 50 个 token。据称其 8B A1B 变体在相同硬件上可超过每秒 100 个 token。HuggingFace Spaces 上提供了演示和源码，并给出了针对 8B-A1B 和 24B-A2B 的优化 ONNX 模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3n5hn/liquid_ais_lfm224ba2b_running_at_50_tokenssecond/)
- **Qwen 3.5 Hybrid Attention 将长上下文速度提升一倍** — 一则 Reddit 帖子使用 qwen3.5-9b-mlx 和 qwen3VL-8b-mlx，在 LM Studio 中以 4-bit 量化配置，对 Qwen 3.5 与早期 Qwen 架构进行了对比测试。结果显示，Hybrid Attention 在长上下文处理方面表现显著更优，在 128K+ 上下文长度下约快一倍。这被视为开源 LLM 在长上下文优化上的重要进展。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3mjly/m5_max_qwen_3_vs_qwen_35_prefill_performance/)
- **litellm 遭遇供应链攻击，替代方案开始涌现** — litellm 在 PyPI 上的 1.82.7 和 1.82.8 版本被植入了窃取凭证的恶意软件。帖子同时介绍了几个开源替代方案：Bifrost（Go 实现，P99 延迟约快 50 倍，Apache 2.0 协议，支持 20+ 提供商）、Kosong（LLM 抽象层，以智能体为中心，支持多种 API）以及 Helicone（带分析功能的 AI 网关，支持 100+ 提供商）。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s34173/after_the_supply_chain_attack_here_are_some/)

### AI Research

- **MinerU-Diffusion：将文档 OCR 重新表述为基于扩散解码的逆向渲染** — 研究者提出将文档 OCR 问题重新表述为逆向渲染，并采用基于扩散的解码方式来替代传统从左到右的自回归方法。这一思路旨在降低长文档识别中的延迟和错误传播，同时更好地捕获版式、表格和公式等结构信息。论文提出的 MinerU-Diffusion 是一种基于扩散的方案，用于提升结构化文档理解能力。 [来源-huggingface](https://huggingface.co/papers/2603.22458)

### Dataset

- **WildWorld 数据集支持基于动作条件的动态世界建模** — WildWorld 是一个面向基于动作条件的动态世界建模的大规模数据集，采用显式状态表示，以支持生成式 ARPG 相关研究。它将世界演化建模为由动作驱动的潜在状态动态过程，视觉观测仅提供部分信息，这一设计与动力系统理论和强化学习框架相契合。作者指出现有数据集存在明显缺口，尤其缺乏多样、语义丰富的动作空间，以及不受底层状态直接中介的动作类型。 [来源-huggingface](https://huggingface.co/papers/2603.23497)

## ⚡ 快讯速览

- **Cursor 在你的基础设施上自托管云端智能体** — Cursor 宣布其云端智能体现可完全在客户自有基础设施上运行。该自托管方案提供与云端相同的智能体框架和使用体验，同时确保代码和工具执行都留在客户内网中。这一举措强调了 AI 工具在安全与本地可控方面的重要性。 [来源-twitter](https://x.com/cursor_ai/status/2036873885665419773)
- **声称：Mary Shelley《Frankenstein》第五章开头 100% 由 AI 生成** — 一条爆火推文声称，Mary Shelley 使用生成式 AI 写出了《Frankenstein》第五章开头的段落，并断言该部分“100% 由 AI 生成”。这一说法未经证实，也引发了关于文学作品中 AI 生成文本的真实性与署名归属问题的讨论。该帖子出自 WrnrWrites，在 X（原 Twitter）上由 DrakeGatsby 带链接转发传播。 [来源-twitter](https://x.com/DrakeGatsby/status/2036770998263972131)
- **SpecEyes 通过“投机式感知”加速智能体级多模态 LLM** — SpecEyes 提出了一种面向智能体级的投机式加速框架，用于降低多模态 LLM 中级联的感知、推理与工具调用循环带来的延迟。其目标是在系统层面“打破智能体深度”，提高并发度与响应速度。该工作作为研究成果发布在 HuggingFace。 [来源-huggingface](https://huggingface.co/papers/2603.23483)
- **last30days-skill 支持跨平台 30 天话题调研** — last30days-skill 是一个 AI 智能体，可在过去 30 天内，跨 Reddit、X、Bluesky、YouTube、TikTok、Instagram、Hacker News、Polymarket 以及网页，对指定话题进行调研，并给出社区“点赞、转发、下注和讨论”的内容及其真实引用。在 2.9.5 版本中，它新增对 Bluesky 的数据源支持（通过 Bluesky 凭证主动授权），并引入对比模式以及配置改进；作者推荐使用 Claude Code 来完成内容生成部分。 [来源-github](https://github.com/mvanhorn/last30days-skill)
- **用算法筛选有用的 AI Reddit 帖子** — 一位 Reddit 用户描述了如何使用 Claude Code 写了一个小算法，用来过滤并筛选高质量的 vibecoding 和 AI 辅助开发相关帖子。系统会抓取 9 个子版块并进行关键词搜索，再根据互动度进行筛选，每天输出 15 篇最有价值的帖子，从而避开低质量内容。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1s38n7x/i_got_tired_of_scrolling_through_ai_slop_on/)
- **Intel 下周将以 949 美元售价推出 32GB VRAM GPU** — Intel 计划在 3 月 31 日发布一款配备 32 GB 显存的低价 GPU，定价 949 美元，带宽为 608 GB/s、功耗 290 W。该显卡主要面向本地 AI 负载和量化模型，例如以 4-bit 精度运行 Qwen 3.5 27B。帖子对 Intel 在 AI 硬件方向的积极动作表示看好。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3e8bd/intel_will_sell_a_cheap_gpu_with_32gb_vram_next/)
- **Intel 发布搭载 32GB GDDR6 的 Arc Pro B70 和 B65** — Intel 公布了专业级 GPU Arc Pro B70 和 B65，两款卡均配备 32GB GDDR6 显存。据称 B70 价格约为 949 美元，主要面向 AI 与专业工作负载，而 B65 则是同系列中定位略低的选项。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3bb3y/intel_launches_arc_pro_b70_and_b65_with_32gb_gddr6/)
- **DeepSeek 预告一款超越 V3.2 的“大模型”** — 一名 DeepSeek 员工在 Reddit 上预告称，一款“体量巨大”的新模型即将发布，并且据称已超越 DeepSeek V3.2。随后该帖子被删除，原因是该员工的回复中“包含了本不该说的内容”。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s39024/deepseek_employee_teases_massive_new_model/)
- **本地 LLM 方案用于总结 500 页 OCR 医疗 PDF** — 一位 Reddit 用户在寻求一套简单、注重隐私的本地 AI 工作流，用于总结约 500 页 OCR 后的医疗记录。他们希望在 Windows 11 环境下，利用 Ryzen 5 5600X、RX 590 和 16GB 内存这套配置，基于 ocrmypdf 生成的 PDF，产出结构化摘要供专科医生使用。其偏好是一键部署和易于清理，而不需要深入折腾本地 LLM。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3qcih/best_local_setup_to_summarize_500_pages_of_ocrd/)
- **完全本地的语音 AI 在 iPhone 15 上设备端运行** — 一名 Reddit 用户展示了一套完全免费、自托管的语音 AI 方案，可在 iPhone 15 上全程本地运行。该方案将语音转文本（STT）和文本转语音（TTS）交由 FluidAudio 与 Apple Neural Engine 处理，使 llama.cpp 能以最小冲突占用 GPU。GitHub 仓库地址为：https://github.com/fikrikarim/volocal [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3i83m/fully_local_voice_ai_on_iphone/)
- **Level1techs 发布面向 Qwen 的 ARC B70 评测，使用 4 张显卡** — Level1techs 的一篇初步评测文章探讨了使用 Intel Arc B70 GPU 来运行 Qwen LLM 及相关负载的表现。文章给出了一些实际使用观察，并提到测试环境中采用了四张 B70 显卡的组合。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s3ksos/level1techs_initial_review_of_arc_b70_for_qwen/)
- **LLM 个性化难题：记忆反复提起旧问题，Karpathy 如是说** — Karpathy 指出 LLM 个性化中一个长期存在的问题：先前交互中的记忆往往会主导后续回答，使模型动辄回到几个月前的旧话题。这种“记忆蠕变”现象导致模型不断重复，过度提及某个曾被问过的问题，从而影响用户体验。相关观点通过 X（Twitter）分享。 [来源-twitter](https://x.com/karpathy/status/2036836816654147718)
- **AI 并没有让工程更简单，而是暴露工程师短板** — 一篇网络帖子认为，AI 并不会让工程工作变得简单，相反，它会暴露并放大工程师本身的弱点。作者声称，差劲的工程师会变得更加自欺，普通工程师会制造更多噪音，而真正优秀的工程师则变得更难被超越。该观点源自 Yuchenj_UW 在推特上的一条帖子。 [来源-twitter](https://x.com/Yuchenj_UW/status/2036647423595159973)
- **警告：Kryven AI 被指为骗局，其相关声明已遭质疑** — 一款名为 Kryven AI 的新工具被宣传为“私密且无审查”，并向推广者提供基于 token 的奖励，但有测试者发现它看起来更像是一个 Gemini 前端，对其模型来源提出质疑。关于“由 Google 训练”的说法没有任何可验证依据，只见于一篇 Reddit 帖子，这使平台的真实性大打折扣。该报告将 Kryven AI 视为骗局警示，而非可信的 AI 产品。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1s39aec/scam_warning_for_private_uncensored_ai_tool/)

---

*由 AI News Agent 生成 | 2026-03-25*