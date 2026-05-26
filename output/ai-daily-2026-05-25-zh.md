---
title: "AI 日报 — 2026-05-25"
description: "开放题Gemini解题，Grok将发布，DeepSeek提供FlashFree。"
lang: "zh"
pairSlug: "ai-daily-2026-05-25"
---

# AI 日报 — 2026-05-25

> 涵盖 32 条 AI 新闻

## 🔥 今日焦点

### 1. AlphaProof Nexus 搭配 Gemini 解决多项开放数学难题

基于 Google DeepMind 的 AlphaProof Nexus 构建的 AI 智能体，已自主解决多项正式数学领域的开放问题，其中包括 9 个 Erdős 问题（其中两个已悬而未决 56 年）、44 个 OEIS 挑战、一个拖延了 15 年的代数几何问题，以及一个悬而未决 7 年的极大极小优化问题。该成果展示了由 Gemini 驱动的智能体循环在攻克研究级数学问题上的潜力，并与组合数学、图论和量子光学等领域的数学家展开合作。相关论文可在 arXiv:2605.22763v1 查阅。 [来源-twitter](https://x.com/pushmeet/status/2058936037754224998)

### 2. Grok V9-Medium（1.5T）训练完成；数周内发布

Grok 宣布其拥有 1.5T 参数的 V9-Medium 基础模型已完成训练，初步评估结果积极。补充训练阶段加入了更多 Cursor 数据，且还会继续增加；目前正处于微调阶段，很快将启动强化学习。团队预计在 2 至 3 周内公开发布，该模型在困难编程任务上应该会显著优于当前 0.5T 参数的 v8-small。 [来源-twitter](https://x.com/elonmusk/status/2058787384364265734)

### 3. DeepSeek V4 Flash 在 Nous Portal 免费开放给 Hermes Agent 使用

DeepSeek V4 Flash 重返 Nous Portal，并可通过 Hermes Agent 免费使用。Nous Portal 推动对 DeepSeek V4 Flash 的免费访问，同时将 Nous Research 定位为专注“以人为本”语言模型与模拟器的开发团队。 [来源-twitter](https://x.com/Teknium/status/2058771232217309476)

## 📰 重点报道

### AI Safety

- **Anthropic 联合创始人警告：AI 或将消灭一半初级白领岗位** — Anthropic 联合创始人 Dario Amodei 过去一年多来一直警告，AI 可能引发大规模岗位流失；他在 2025 年 5 月曾表示，未来五年内多达 50% 的初级白领岗位可能被淘汰，失业率或达 10-20%。在 2026 年 1 月，他发表了一篇 2 万字长文，论证 AI 将作为一种“通用劳动力替代品”带来异常剧烈的冲击。文章还提到达沃斯期间关于硅谷“零级世界”（zeroth world）经济的警示，并引用数据：2025 年科技行业初级岗位招聘下滑、华尔街银行削减约 20 万个初级岗位、标普 500 公司整体出现净裁员，以及 Anthropic 自身的劳动力市场研究结果。 [来源-twitter](https://x.com/kimmonismus/status/2058864107432943796)
- **教宗警示：AI 必须服务于人的尊严，警惕国家权力滥用** — 教宗指出，AI 必须服务于人的尊严，而不是被用来实现支配或排斥。他警告说，如果给予政府对 AI 过于宽泛的控制权，可能会催生审查、监控和对公民的操控，并援引奥威尔的《1984》以及“谁来监管监管者”（Quis custodiet ipsos custodes）的古老格言。文章将此视为 AI 治理中真正的“对齐问题”。 [来源-twitter](https://x.com/DavidSacks/status/2058944094035128593)
- **Anthropic 聘用 Karpathy，在武器化争议中打出“伦理牌”的公关胜利** — Anthropic 高调聘用 Andrej Karpathy，被外界视为一场重要的公关胜利，凸显该公司对热门研究者的吸引力以及其强调伦理立场的形象。报道提到过去与“战争部”（Department of War）在 Claude 是否可用于自主武器上的紧张关系，这一争议导致 OpenAI 和 Google 拿下相关合同，而 Anthropic 则被贴上供应链风险标签。同时也提及 Dario Amodei 关于失业的警告，将这次人事动作置于更大的 AI 产业博弈之中。 [来源-twitter](https://x.com/kimmonismus/status/2058942418087481792)

### Multimodal

- **Lens 3.8B 文生图模型以高效率超越更大规模模型** — Lens 是一款拥有 38 亿参数的文生图模型，在多个基准上能与参数量超过 60 亿的最新模型持平甚至超越，同时只使用了约 19.3% 的训练算力。其高效性来源于紧凑的模型规模，以及在每个训练 batch 中最大化数据信息密度的策略。 [来源-huggingface](https://huggingface.co/papers/2605.21573)

### Open Source

- **NuExtract3：面向 Markdown 与 OCR 的 4B 开源权重 VLM** — NuExtract3 是基于 Qwen3.5-4B 构建的 40 亿参数视觉语言模型，采用 Apache-2.0 许可开源权重。它面向复杂文档的实用信息抽取任务——将图像/文本转为 Markdown，并从 PDF、表单、表格、小票和多页版面中提取结构化数据——可自托管，并支持基于目标 JSON 模板输出。该模型延续自 NuMarkdown，并在 HuggingFace 上提供免费体验空间。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tn8utn/nuextract3_released_openweight_4b_vlm_for/)
- **MiMo V2.5-Coder 发布：为本地 128 GB 内存环境优化** — MiMo V2.5-Coder 已发布，并被宣传为在 128 GB 内存本地系统上运行表现最好的模型之一。作者称其速度很快，在实验中性能优于 Qwen 3.6 和 DeepSeek 4-Flash。项目强调开源与开放科学，模型托管在 Hugging Face。 [来源-twitter](https://x.com/jedisct1/status/2058827764237525231)
- **Frigate NVR 为 IP 摄像头提供本地实时目标检测** — Frigate NVR 是一套完整的本地 NVR 方案，为 Home Assistant 设计，利用 OpenCV 和 TensorFlow 对 IP 摄像头进行实时目标检测。它强调本地处理、多进程以实现高 FPS、低开销运动检测，并通过 MQTT 与 Home Assistant 集成。 [来源-github](https://github.com/blakeblackshear/frigate)

### LLM

- **OSCAR RotationZoo：离线 2-bit KV Cache 旋转矩阵** — OSCAR RotationZoo 提供面向 OSCAR INT2 KV-cache 量化的预计算 K/V 旋转矩阵。它打包了一系列工件，支持离线估计“注意力感知”的 K/V 协方差，以及按层构建的正交旋转，使 2-bit 量化方向与注意力方向对齐。据称该方法在致密推理模型上，可带来约 7 倍 KV-cache 内存压缩，在 GPQA 上仅有小幅精度损失，并以可直接使用的 .pt 文件形式发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tn6v0r/oscar_rotationzoo_offline_spectral/)
- **Herm 提升 Python 性能，在多轮基准上击败 Codex** — Herm 的更新公告称，其 Python 性能已有明显提升，与大型 Rust 代码库相比也具竞争力。作者声称 Herm 在多数多轮对话基准上优于 Codex，并附上了指向 NousResearch/herm 的 GitHub PR 链接。 [来源-twitter](https://x.com/Teknium/status/2058885472513065471)
- **Earendil-Works 发布 pi AI Agent 工具包** — pi 项目发布了开源 AI 智能体工具包，包含一个代码智能体 CLI、统一的多提供商 LLM API，以及 UI 库（TUI 和 Web）。该工具包基于 pi agent harness monorepo 构建，内含代码智能体、智能体运行时和 LLM API 等模块。pi.dev 域名由 exe.dev 捐赠；新的 issue 和 PR 默认会被自动关闭，并由维护者每天审阅；参与细节可见 CONTRIBUTING.md。 [来源-github](https://github.com/earendil-works/pi)
- **开源代理实现免费 Claude Code 访问** — 一个名为 free-claude-code 的开源“即插即用”代理项目，可将 Anthropic Claude Code API 调用路由至 17 个后端提供商，从而通过 CLI、VS Code 和类 Discord 界面免费使用 Claude Code。它支持按模型路由，并通过代理的 /v1/models 端点暴露 Claude Code 的模型选择器，同时允许用户在免费、付费或本地模型之间切换。该仓库由 Alishahryar1 创建，列出的提供商包括 NVIDIA NIM、OpenRouter、Gemini、Mistral、llama.cpp、Ollama 等。 [来源-github](https://github.com/Alishahryar1/free-claude-code)
- **CUDA 快速 FWHT 加入 llama.cpp，略微提升速度** — 一则 Reddit 帖子称，am17an 为 llama.cpp 添加了用于 CUDA 的快速 Walsh-Hadamard 变换（FWHT），以加速量化 KV-cache 路径。基准结果显示，在 5090 显卡和多种配置下，pp 测试提升约 1-2%，tg 测试提升约 7-9%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tnfqng/cuda_add_fast_walshhadamard_transform_by_am17an/)
- **Qwen 0.8B 在 Pangram 数据集上微调用于 AI 内容检测** — 一个基于 Qwen 0.8B 的 AI 内容检测器，利用 EditLens 在 Pangram 数据集上完成微调，被打包为名为 Slop Hammer 的 Chrome 扩展。该工具在本地运行，首次使用需从 Hugging Face 下载约 400MB 的模型文件，在 M1 MacBook Pro 上可在约 1 秒内给出文本为 AI 生成的概率分布。作者将 Qwen 0.8B 与其他模型（Llama 3.2 3B、Qwen 2B、Gemma 各版本）比较后认为其表现更好，微调耗时约 20 小时（RTX 3090）。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tngkav/ai_content_detector_based_on_qwen_08b_finetuned/)
- **Qwen3.6 27B 在 V100 GPU 上实现 1000 TPS** — Reddit 用户 Simple_Library_2700 报告称，使用 NVIDIA V100 GPU，在 Qwen3.6 27B 上实现了每秒 1000 token 的生成速度。测试使用了 128 个并发请求（超过实际需求），而对单个用户而言，生成速度约为 80 token/s，处理速度约 3000 token/s，且未使用 MTP（multi-tasking pipeline）。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmyln6/1000_tps_generation_on_qwen36_27b_with_v100s/)
- **关于 Qwen 27B Q8 量化的最佳选择？社区讨论与备选方案** — 一则 Reddit 帖子询问在 Qwen 27B 上使用何种量化配置能获得最佳性能。作者提到社区在 Q4–Q6 之间的讨论，自己目前运行的是 Unsloth 的 Q8，但即便开启 MTP 仍然偏慢，并考虑是否应切换到 Q8 35B A3B 等替代方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tndx54/whats_the_best_qwen_27b_q8_quant/)
- **MiniCPM5-1B 发布：10 亿参数本地 LLaMA 模型** — 一则 Reddit 帖子重点介绍 MiniCPM5-1B，这是一款与 LocalLLaMA 社区相关联的 10 亿参数模型。帖子链接指向关于该模型的更多信息，但条目本身未给出详细规格。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tnafre/minicpm51b/)

### AI

- **Claude 知识工作插件开源** — Anthropics 开源了 11 个插件，用于将 Claude Cowork 打造成针对不同知识工作岗位的专业助手。每个插件都打包了一组技能、连接器、斜杠命令和子智能体，并可根据企业自身的工具、数据和工作流进行定制。这些插件可在 Plugin Marketplace 与 GitHub 获取，且与 Claude Code 有广泛兼容性。 [来源-github](https://github.com/anthropics/knowledge-work-plugins)

## ⚡ 快讯速览

- **教宗良十四发布关于 AI 时代守护人性的通谕** — 梵蒂冈发布通谕《Magnifica Humanitas》，由教宗良十四撰写，探讨 AI 对人类尊严构成的挑战。文件指出，在基督身上彰显的人类尊严不可由机器替代，并呼吁信徒在人工智能时代保持深刻的人性。该通谕将 AI 视为对道德责任的一场考验，强调必须守护人的主体性。 [来源-twitter](https://x.com/Pontifex/status/2058888313029685400)
- **Qwen3.7-Max 上线隐式缓存，更快更省** — 阿里巴巴的 Qwen3.7-Max 现已支持自动启用的隐式缓存，无需额外配置。更新声称可在开箱即用的情况下提供更快、更便宜的推理体验，同时也保留了显式缓存选项，以获得更高且更可控的命中率。 [来源-twitter](https://x.com/Alibaba_Qwen/status/2058932656797368619)
- **Claude Code 通过网络请求实现 API 逆向工程** — 该帖展示如何使用 Claude Code 搭配 browser_harness 或 Playwright 嗅探网络请求，从而推断难以通过 DOM 导航的网站的 API 结构与认证机制。文中示范了如何测试和映射速率限制，以实现自动化数据抓取，并构建诸如旅行 CLI、网站监控等项目。 [来源-twitter](https://x.com/nikunj/status/2058783316753686558)
- **GPT-5.5 Pro 在事实核查方面表现出色（Ethan Mollick 评论）** — Ethan Mollick 称赞 GPT-5.5 Pro 是一款强大的事实核查工具，能够处理整章内容并准确定位关键参考文献。他指出，该模型经常会给出细致的限定和补充说明，既能标记非常细微的错误，又能保持整体观点不失真，这凸显了 GPT-5.5 Pro 作为可靠 AI 辅助事实核查工具的潜力。 [来源-twitter](https://x.com/gdb/status/2058750645394649410)
- **SkillOpt：用于智能体自进化技能的文本空间优化方法** — 论文主张，智能体技能应被视为冻结智能体的“外部状态”，并使用与权重空间优化相同、可复现实验的严谨方法来训练。作者提出 SkillOpt，据其所知，这是首个系统化、可控的文本空间优化方法，用于让智能体技能不断进化。 [来源-huggingface](https://huggingface.co/papers/2605.23904)
- **重新思考扩散 Transformer 中的跨层信息路由** — 该论文对 Diffusion Transformers（DiTs）中的跨层信息流进行了系统实证分析，强调残差流仍延续了原始 Transformer 中的关键角色。文中讨论了这一结构对信息在各层间路由方式的影响，并提出了重新设计 DiTs 跨层通信机制的若干方向。 [来源-huggingface](https://huggingface.co/papers/2605.20708)
- **12×32GB SXM V100 集群：本地法律 AI 框架更新** — 一位律师更新了其本地 AI 集群进展，目前集群包含 12 张 V100-SXM2 32GB GPU，搭载 Threadripper Pro，并对板间 NVLink 布局进行了精细设计。第二个节点（EPYC 7302P、512GB 内存、4×RTX 3090、2×V100-PCIe）也已加入。作者放弃了在本地模型上使用 vLLM，但仍依靠 Claude Code 驱动整个系统，尽管对整体方案仍存不确定感。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tnn29i/update_on_12x32gb_sxm_v100_cluster_local_ai_for/)
- **更小、量化程度更低的模型能否击败更大、更强量化的模型？** — 一名 Reddit 用户询问，更小的模型在使用较“宽松”的量化时，能否超越更大但高强度量化的模型，并举例对比 Gemma 4 31B Q4 K S 与 Gemma 4 26B A4B Q8，以及 Qwen 3.6 27B Q4 K M 与 Qwen 3.6 35B A3B Q6 K。TA 想知道在什么情况下值得切换量化等级，并说明其主要应用场景是创意写作。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tnff26/is_there_any_case_of_a_less_quantised_smaller/)
- **本地 LLM 动态生成个性化交互教材** — 一则 Reddit 帖子探讨使用本地开源 LLM 动态生成个性化交互式教材的方案。该方法旨在按需、递归地构建适配个体需求的学习材料。帖子引用了 Local LLaMA 社区，由用户 Ryoiki-Tokuiten 发布在 r/LocalLLaMA。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tnjxq6/using_local_llms_for_generating_custom/)
- **对署名为人类、实为 AI 代写邮件的担忧** — 一条推文表达了对那些被宣传为“人写”的邮件实则由 AI 生成的现象的不安，认为这种做法具有欺骗性。作者质疑有谁会容忍这种欺骗，并凸显了在 AI 介入的沟通中存在的信任问题。 [来源-twitter](https://x.com/paulg/status/2058855820121498037)
- **呼吁公开 OpenAI Dota 机器人架构；Olah 将谈 AI 通谕** — 一则社交媒体帖子呼吁 OpenAI 公开其 Dota 机器人架构，指责该组织言行不一。该条目还提到，Anthropic 联合创始人 Chris Olah 受邀就教宗良十四关于 AI 的通谕《Magnifica humanitas》发表演讲，并附上他发言的链接。 [来源-twitter](https://x.com/theo/status/2058983530777186559)
- **Building with Codex** — 一条推文提到使用 Codex 构建项目，但未提供更多上下文或细节。 [来源-twitter](https://x.com/mpopv/status/2058743196361117926)

---

*由 AI News Agent 生成 | 2026-05-25*