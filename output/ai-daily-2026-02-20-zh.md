# AI 日报 — 2026-02-20

> 覆盖 45 条 AI 新闻

## 🔥 今日焦点

### 1. Gemini 3.1 Pro 在 MagicPathAI 上主导图像转代码

Gemini 3.1 Pro 被声称是将图像转换为代码的领先模型，表明这项任务基本上已解决。该帖指出该模型现已通过 MagicPathAI 提供，并提到启用 HLS 回放。 [来源-twitter](https://x.com/skirano/status/2024875637878526109)

### 2. OpenAI 审核人员就不列颠哥伦比亚省枪手的 ChatGPT 信息展开辩论

一份报道显示，不列颠哥伦比亚省枪手的 ChatGPT 信息不仅被自动化系统标记，还被约十几名 OpenAI 员工审阅并辩论。该事件凸显了人类审核在 AI 安全工作流程中的作用。 [来源-twitter](https://x.com/AricToler/status/2024976260749820067)

### 3. AGI 指日可待；超智能与强人工智能近在眼前

据称 Frontier Labs 已接近 AGI，超智能不远，ASI 也可能触手可及。该帖强调关注内部模型的加速，并暗示起飞速度可能快于预期，从而为即将到来的 AI 突破制造炒作。 [来源-twitter](https://x.com/kimmonismus/status/2024898716365455459)

## 📰 重点报道

### 多模态

- **Google DeepMind 的 Lyria 3 能在 Gemini Beta 中生成 30 秒歌曲** — Google DeepMind 的 Lyria 3 已集成到 Gemini 应用中，允许用户从文本提示或照片在测试阶段生成 30 秒歌曲。输出包括人声和封面图，直接在 Gemini 应用内或网站上提供。 [来源-producthunt](https://www.producthunt.com/products/lyria-3-by-google-deepmind?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)

### 大型语言模型

- **GUI-Owl-1.5 推出多平台 GUI Agent** — 研究人员推出 GUI-Owl-1.5，这是一个原生 GUI Agent 模型，提供多种规模（2B/4B/8B/32B/235B）以及指令/思考变体。它支持桌面、移动、浏览器等平台，实现云边协作与实时交互。该模型据称在 20 多项 GUI 基准测试中达到最先进水平，包括 OSWorld（56.5）、AndroidWorld（71.6）和 WebArena（48.4）。 [来源-huggingface](https://huggingface.co/papers/2602.16855)
- **中文模型主导 OpenRouter；前三名周吞吐量首次超过万亿令牌** — OpenRouter 报告显示在一个具有里程碑意义的一周里，首次有至少一个模型每周超过 3 万亿令牌。多于一个模型也超过了万亿令牌的周量，这是自 Grok 4 Fast 几个月前以来未曾出现的成就。中文模型似乎领跑榜单，似乎对美国产品形成领先优势。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9zt8m/the_top_3_models_on_openrouter_this_week_chinese/)
- **Hugging Face 收购 GGML.AI** — 根据 Reddit 的一则帖子，Hugging Face 收购了 GGML.AI。这笔交易标志着开源 AI 工具生态格局的显著变化，Hugging Face 正在扩展其生态系统。交易可能影响 GGML.AI 组件与 Hugging Face 平台的整合。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9vywq/ggmlai_has_got_acquired_by_huggingface/)
- **Claude Opus 4.6：任务时间范围约 14.5 小时的 50% 时间线** — Anthropic 的 Claude Opus 4.6 在软件任务上显示约 14.5 小时的 50% 时间线，95% 可信区间在 6 到 98 小时。该估算迄今为止最高，但由于任务集饱和，测量不确定性较大。 [来源-twitter](https://x.com/METR_Evals/status/2024923422867030027)
- **山姆·奥特曼警告：快速 AI 起飞，世界尚未准备就绪** — 山姆·奥特曼表示，AI 公司内部的观察显示极具能力的模型很快就会到来，而世界尚未做好准备。他警告起飞速度会比他原先预计的更快，形势紧张且引发焦虑。 [来源-twitter](https://x.com/kimmonismus/status/2024887011522576766)
- **打造 AI 助手的每一家企业都是广告公司** — 该观点认为开发 AI 助手的公司正逐渐演变为广告平台，利用用户数据和定向广告来盈利。强调隐私问题和商业模式的转变，即 AI 助手通过广告而非纯服务来实现变现，对用户与开发者影响深远。 [来源-hackernews](https://juno-labs.com/blogs/every-company-building-your-ai-assistant-is-an-ad-company)
- **GGML.AI 加入 Hugging Face 以推进本地化 AI** — GGML.AI 宣布加入 Hugging Face，旨在支持 Local AI 的长期发展。合作旨在将 ggml/llama.cpp 基于的工具链与 Hugging Face 生态系统结合，以推动本地化、注重隐私的 AI 开发。 [来源-hackernews](https://github.com/ggml-org/llama.cpp/discussions/19759)
- **字节跳动 Ouro-2.6B-Thinking：修复 4.55 版本后首次推断** — 字节跳动发布 Ouro-2.6B-Thinking，这是一个循环式通用变换器，对每个令牌处理 48 层，4 次通过（192 次遍历）。该模型因 transformers 4.55 的变更导致与 GGUF 的兼容性问题，已修复 modeling_ouro.py 中的两个错误以实现正确推断。早期测试在简单提示上输出正确，NVIDIA L4 的性能约为 3.8 t/s，显存 5.3 GB。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ramir9/release_ouro26bthinking_first_working_inference/)
- **Strix Halo 基准：Minimax M2.5、Step 3.5、Qwen3 Coder Next** — 一篇 AI 基准测试贴给出 Strix Halo 模型 Minimax M2.5 与 Step 3.5 Flash、以及 Qwen3-coder-next、GLM 4.6V/4.7 Flash 与 gpt-oss-120b 等在 ROCm 7.2、Ryzen AI Max+ 395（70W）、128GB 内存条件下的基准结果，时间深度设为 30,000 令牌。作者在评论区征集模型请求。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rabcyp/a_few_strix_halo_benchmarks_minimax_m25_step_35/)
- **TeichAI GLM-4.7、Flash Claude Opus 4.5 Distill 在 Hugging Face 上** — 一个开源套件，包含 TeichAI/GLM-4.7 与 Flash Claude Opus 4.5 High-Reasoning Distill，在 Hugging Face 上有所亮相。该帖昨日由 Unsloth 在 X 上转发，Reddit 用户 /u/jacek2023 分享。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ranako/teichaiglm47flashclaudeopus45highreasoningdistillg/)
- **GGML 与 llama.cpp 加入 HF 以推动本地 AI** — GGML 与 llama.cpp 将加入 Hugging Face，以协同并推动本地 AI 的长期发展。该合作旨在让开源工具更好地与 HF 生态系统对接，支持本地运行的 AI 模型的互操作性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9wvg4/ggml_and_llamacpp_join_hf_to_ensure_the_longterm/)

### AI 安全

- **Claude Code Security 进入有限研究预览** — Anthropic 推出 Claude Code Security，这是一个扫描代码库漏洞并为人工审阅提供定向修补的工具，帮助团队发现并修复传统工具常错过的问题。该功能处于有限研究预览阶段；详情请见 anthropic.com/news/claude-code-security。 [来源-twitter](https://x.com/claudeai/status/2024907535145468326)

### AI

- **斯特兰·斯卡斯加德谈 AI 在电影中的日益作用** — 斯特兰·斯卡斯加德讨论 AI 在电影中的日益影响，指出电影一直在探索人类复杂性，AI 可能改变故事的制作方式。他警告资本集中而非技术本身是行业的主要挑战，AI 仍然依赖于人和背后的权力结构。 [来源-twitter](https://x.com/Variety/status/2024983345499963815)
- **SpargeAttention2：可训练的稀疏注意力与混合屏蔽** — 研究人员探索使稀疏注意力可训练，以在提升稀疏度的同时保持扩散模型质量。他们解释了 Top-k 及 Top-p 屏蔽的失败，阐述了可训练方法为何能超过无训练的稀疏性，并探讨通过蒸馏微调的极限。 [来源-huggingface](https://huggingface.co/papers/2602.13515)

### 具身 AI

- **Pika AI Selves 上线：个人、记忆丰富的 AI 后代** — Pika Labs 发布 Pika AI Selves，用户可以创建、培养并部署为自己生活延伸的 AI 代理。据称具备记忆能力与多模态能力，能够执行如发送图片、创作关于你的鱼的游戏，或致电你的妈妈等任务。感兴趣的用户可前往 pika.me 加入候补名单，创建自己的 AI 自我。 [来源-twitter](https://x.com/pika_labs/status/2024919175878377587)

### 开源

- **DreamDojo：用于机器人预训练的开源交互式世界模型** — DreamDojo 是一个开源、可交互的世界模型，接收机器人运动指令并以像素方式呈现未来帧，无需引擎、网格或手工设计的动力学。它在 44,000 小时的人类第一视角视频上进行预训练，并使用潜在动作来确保在不同硬件上的机器人可读性，从而实现实时远程操控、策略评估和时 Fig 期计划。 [来源-twitter](https://x.com/DrJimFan/status/2024895359236051274)
- **RynnBrain：面向现实世界 AI 的开源具身基础模型** — RynnBrain 作为一个开源的时空基础模型，以具身智能为目标，致力于在现实世界的时空动态中统一感知、推理与规划，强化自我中心理解与多样的时空定位能力。 [来源-huggingface](https://huggingface.co/papers/2602.14979)
- **PentAGI：用于渗透测试的自治 AI Agent** — PentAGI 是一个开源工具，使用 AI 自动化进行安全测试，面向信息安全专业人士与爱好者，提供沙箱化、基于 Docker 的环境，以及用于 LLM 代理、向量化与测试工作流的模块化框架，以执行复杂的渗透任务。 [来源-github](https://github.com/vxcontrol/pentagi)
- **Vellium v0.3.5：大规模写作模式升级、原生 KoboldCpp、OpenAI TTS** — Vellium 发布 v0.3.5，进行写作模式的重大重写、改进本地提供方支持，并新增书籍大纲、DOCX 导入与缓存摘要等功能。更新还支持 OpenAI TTS、AI 辅助角色补丁编辑，简化用户界面，并实现 KoboldCpp 的本地原生集成，包含 provider:memory、universal 标签与 n-sigma。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rafo5b/update_vellium_v035_massive_writing_mode_upgrade/)

### 扩散模型

- **SLA2：通过可学习路由改进稀疏-线性注意力** — SLA 将稀疏注意力与线性注意力结合以加速扩散模型与视频生成，但其基于启发式拆分可能并非最优。论文分析了注意力误差并指出与直接分解的不匹配，提出带可学习路由的 SLA2 以解决这些问题并结合量化感知裁剪（QAT）来提升效果。 [来源-huggingface](https://huggingface.co/papers/2602.12675)

### 强化学习

- **AutoWebWorld 通过有限状态机综合可验证的 Web 交互环境** — AutoWebWorld 提出一种框架，用有限状态机合成可控、可验证的 Web 交互环境，旨在解决 autonome Web GUI 代理在获取真实世界交互轨迹时遇到的瓶颈，其中隐藏状态转移会使验证变得复杂。通过提供合成、可验证的训练环境，旨在提升数据质量与评估可靠性。 [来源-huggingface](https://huggingface.co/papers/2602.14296)

### 行业动态

- **Meta 部署 AI，正在扼杀我们的代理机构** — 一篇关于 Mojodojo 的评论文章（由 Hacker News 的帖子放大），认为 Meta 的 AI 部署通过自动化工作削弱了广告代理机构的作用，威胁到客户关系与生计，引发关于 AI 颠覆广告行业的讨论。 [来源-hackernews](https://mojodojo.io/blog/meta-is-systematically-killing-our-agency/)

---

## ⚡ 快讯速览

- **AI 可能在替代亚马逊的客服代表之前取代软件工程师** — 一则推文指出讽刺之处：AI 可能先于亚马逊的 10 万客服代表取代软件工程师，强调推动自动化的人会先被自动化。 [来源-twitter](https://x.com/Yuchenj_UW/status/2024907354656178257)
- **Claude Code Desktop 增加应用预览、代码审查、CI/PR 自动化** — Anthropic 的 Claude Code 桌面版现可预览正在运行的应用并审查代码，后台处理 CI 失败和 PR。更新还实现 HLS 回放，扩展了 Claude Code 对开发者的自动化能力。 [来源-twitter](https://x.com/claudeai/status/2024937960572104707)
- **Cursor 驾驭 Gemini，保持 Google 模型高效生产力** — Cursor 声称其工具能够驾驭 Google 的 Gemini，提供市场上为数不多的可让模型保持高效与专注的工具之一。强调企业 AI 中模型管理工具的重要性。 [来源-twitter](https://x.com/theo/status/2024839053900910612)
- **OpenAI 报告称各团队均实现积极进展** — OpenAI 领导层在推文中表示全组织各部分都取得积极进展，强调团队自豪感但未给出具体细节或指标。暗示内部动能强劲但未给出公开里程碑。 [来源-twitter](https://x.com/gdb/status/2024985187579560366)
- **Prism Videos：带模板的统一 AI 视频创作工作区** — Prism 推出一体化的 AI 视频创作平台，允许用户从多种模型生成图像与视频资产、将它们整理到一个项目中并在时间线中编辑，无需下载文件。支持模板及一键 assets 复用，允许重复使用 Prism 社区的预设。 [来源-producthunt](https://www.producthunt.com/products/prism-videos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)
- **Rork Max：面向 iOS 与 Apple 平台的 AI Swift 应用构建器** — Rork Max 自称是一个 AI 驱动的 Swift 应用构建器，旨在取代 Xcode 进行 iOS 应用开发，覆盖 iPhone、iPad、Apple Watch、Apple TV、Vision Pro 与 iMessage 的跨平台支持，支持一键安装与两击上架 App Store。 [来源-producthunt](https://www.producthunt.com/products/rork-app-for-ios?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)
- **git-lrc：在每次提交时免费进行 AI 代码审阅** — git-lrc 将 AI 评审挂载到每次 diff 上，以避免逻辑错误、凭据泄露和因生成式 AI 导致的云调用成本等问题，定位为 AI 辅助编码的“制动器”。 [来源-producthunt](https://www.producthunt.com/products/git-lrc?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)
- **Woise：用于网站反馈的 AI 语音与屏幕录制工具** — Woise 是一个 AI 驱动工具，允许用户捕捉屏幕活动与声音，以在网站上报告缺陷或提出功能改进。它会自动将口头反馈转换为文本，便于快速审阅，降低来回沟通与猜测的成本。 [来源-producthunt](https://www.producthunt.com/products/woise-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+yinhewang+%28ID%3A+275680%29)
- **Cord：协调 AI 代理的树状结构** — 讨论 Cord 这一将 AI 代理组织成分层树状结构的概念，提出代理之间的分层协作以改进任务分解与协调性，激发对可扩展代理编排的讨论。 [来源-hackernews](https://www.june.kim/cord)
- **Hugging Face Skills：可互操作的 AI 任务定义** — Hugging Face 介绍 Skills，一组用于数据集创建、模型训练与评估的可重用 AI/ML 任务模块。Skills 框架旨在跨越 OpenAI Codex、Claude Code、Google DeepMind Gemini CLI、Cursor 等主要工具，使用统一的 Agent Skill 格式，包含一个 SKILL.md 的文件夹。文中提到术语差异：“Skills” 是 Anthropic 的术语，在 Claude AI/Claude Code 中使用；其他工具使用 AGENTS.md（Codex）或 Gemini 扩展等格式。 [来源-github](https://github.com/huggingface/skills)
- **Anthropic 发布官方 Claude Code 插件目录** — Anthropic 公开了一个官方、Anthropic 管理的 Claude Code 插件目录，内部插件位于 /plugins，第三方外部插件位于 /external_plugins。该目录提供通过 Claude Code 插件系统的安装指南，并提醒用户信任插件，Anthropic 不能对第三方组件进行核验。项目托管在 anthropics/claude-plugins-official，包含 Anthropic 开发的内部插件及参考实现。 [来源-github](https://github.com/anthropics/claude-plugins-official)
- **最佳音频模型 2026 年 2 月 Megathread** — Reddit 的 Megathread 汇总了截至 2026 年 2 月的 notable 音频 AI 模型（ASR、TTS、STT、Text-to-Music），并邀请大家给出详细设置与实证对比。指出 ElevenLabs v3 等闭源模型在长期、生产环境方面往往优于开源模型，Qwen3 TTS 被特别提及。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r7bsfd/best_audio_models_feb_2026/)
- **GLM 5 在 Claude 提示下呈现 Claude 风格的个性** — Reddit 用户声称 GLM 5 在按照 Claude 的提示下，写作风格发生变化，似乎可以绕过内置的审查；尝试诱导 Tiny by Applet 等不同人格并未复现，推测原因可能来自 GLM 5 的训练数据或出现的涌现行为，同时注意 Claude Code 兼容性也可能是原因。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1raf3dm/glm_5_seems_to_have_a_claude_personality/)
- **AI 奇点正在兴起，AI 正在起飞** — 一条关于 AI 的 Twitter 帖子暗示 AI 奇点正在起飞，指向 AI 进步的加速，但没有提供技术细节或证据。上下文有限，使其更具宣传性而非解释性。 [来源-twitter](https://x.com/scaling01/status/2024925692853395618)
- **我讨厌 AI 的副项目** — Dylan Castillo 批评 AI 副项目趋势，认为许多业余项目更注于炫酷演示而非持久影响，质疑其实用性、长期可维护性及对 AI 社群的广泛影响。 [来源-hackernews](https://dylancastillo.co/posts/ai-side-projects.html)
- **教授在寻求 HuggingFace 上鲜为人知的模型用于教学** — 一位教授在 Reddit 的 r/LocalLLaMA 提出希望获取 HuggingFace 上独特且知名度较低的模型以用于教学，邀请社区提供建议。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rajez2/what_are_your_favorite_lesser_known_models_on/)
- **Gemma 将很快发布新版本** — Reddit 用户 jacek2023 在 r/LocalLLaMA 上发帖称 Gemma 即将发布新版本，但未给出发布日期或功能细节。似乎是 LocalLLaMA 社区内部的 AI 项目更新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ra8omf/gemma_which_we_will_be_releasing_a_new_version_of/)
- **新泽西居民在社区胜利中挫败 AI 数据中心** — 新泽西居民击败拟议的 AI 数据中心，显示社区对 AI 基础设施与大科技扩张的强烈反对。案件凸显对本地影响、能源使用和数据隐私的担忧。 [来源-hackernews](https://www.commondreams.org/news/new-brunswick-ai-data-center)
- **Deepseek 与 Gemma：Reddit 讨论** — LocalLLaMA 子版块的 Redddit 用户 /u/ZeusZCC 提到 Deepseek 与 Gemma 两条 AI 话题，帖子链接之外无更多细节。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9uuc6/deepseek_and_gemma/)

---

*Generated by AI News Agent | 2026-02-20*