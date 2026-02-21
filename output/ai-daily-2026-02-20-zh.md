# AI 日报 — 2026-02-20

> 涵盖 45 条 AI 新闻

## 🔥 今日焦点

### 1. **AGI 与 ASI 接近：前沿实验室加速迈向起飞**

一条推文质疑前沿 AI 实验室内部在发生什么，因为信号指向通用人工智能（AGI）非常接近，以及超级智能也不远。该帖子指出观察模型内部加速的速度，并暗示 AI 起飞可能比预期更快。它反映出关于近在眼前的通用人工智能与超智能能力的炒作。 [来源-twitter](https://x.com/kimmonismus/status/2024898716365455459)

### 2. **Taalas 展示 Llama 3 8B：每位用户 16k 令牌/秒**

Taalas 展示了一种模型特定的加速器，在此处每块芯片即为一个模型，目标模型为 Llama 3 8B，达到每位用户 16k 令牌/秒。该设置据称比基于 SRAM 的系统如 Cerebras 快约一个数量级。配套的对话演示被描述为相当疯狂。 [来源-twitter](https://x.com/awnihannun/status/2024671348782711153)

### 3. **GUI-Owl-1.5 公布多平台 GUI 代理**

开源论文引介 GUI-Owl-1.5，是一个原生 GUI 代理模型，具备指令/思考变体，提供 2B/4B/8B/32B/235B 等多种尺寸，并支持桌面、移动与浏览器平台，以实现云端-边缘协作与实时互动。其在超过 20 个 GUI 基准测试中达到最先进的水平，在 GUI 自动化和定位任务上取得如 OSWorld 56.5、AndroidWorld 71.6、WebArena 48.4 等分数。 [来源-huggingface](https://huggingface.co/papers/2602.16855)

## 📰 重点报道

### 多模态

- **MAEB 基准在音频任务上未出现主导模型** — Massive Audio Embedding Benchmark (MAEB) 评估覆盖 30 项任务，涵盖语音、音乐、环境声音以及跨模态音频文本推理，涉及超过 100 种语言、50 多个模型的比较。研究发现不存在单一模型在所有任务上都表现出色；对比式音频-文本模型在环境声音分类（如 ESC50）上表现最佳，但在多语言语音任务（如 SIB-FLEURS）上表现欠佳；而带有语音预训练的模型呈现相反的模式。 [来源-huggingface](https://huggingface.co/papers/2602.16008)

### AI 在广告领域

- **Meta 的 AI 部署正在扼杀我们的代理机构** — 一篇帖子主张 Meta 的 AI 推广正在通过自动化核心职能并侵蚀价值来削弱传统广告代理机构。帖子警示这种机制性危害会冲击代理机构的商业模型，并呼吁重新评估在广告生态系统中对 Meta AI 的依赖。 [来源-hackernews](https://mojodojo.io/blog/meta-is-systematically-killing-our-agency/)

### 大语言模型

- **Strix Halo 基准：Minimax M2.5、Step 3.5、Qwen3-Coder Next** — 一项实验性基准测试在 llama.cpp 上比较 Strix Halo 模型（Minimax M2.5 与 Step 3.5 Flash），并对 Qwen3-Coder-Next、GLM 4.6V/4.7 Flash、gpt-oss-120b 进行额外测试。基准测试在 ROCm 7.2、 Ryzen AI Max+ 395 @70W、128GB 内存，以及 30,000 token 的上下文深度条件下进行。作者在评论区邀请对更多模型或分量的请求。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rabcyp/a_few_strix_halo_benchmarks_minimax_m25_step_35/)
- **Hugging Face 收购 GGML.AI** — Reddit 发帖报道 GGML.AI 已被 Hugging Face 收购。这一举动表明开源 AI 工具的整合将进一步推进，或扩展 Hugging Face 平台对 GGML 技术的能力。帖文给出来源但未提供官方确认。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9vywq/ggmlai_has_got_acquired_by_huggingface/)
- **SpargeAttention2：可训练的稀疏注意力，结合混合掩蔽** — 研究者提出 SpargeAttention2，一种可训练的稀疏注意力方法，使用 Top-k 与 Top-p 掩蔽的混合以及蒸馏微调，以在不牺牲扩散模型质量的前提下提高稀疏性。他们探讨 Top-k 与 Top-p 掩蔽失效的情形、如何避免这些失败，以及为何可训练的稀疏注意力可超越“无训练”的方法，同时概述微调的局限性。 [来源-huggingface](https://huggingface.co/papers/2602.13515)
- **Frontier AI 更新风险管理框架 v1.5** — Frontier AI 发布的《实践中的风险管理框架》（v1.5）更新，提供在前沿 AI 模型能力加速与代理式 AI 增生的背景下的细粒度风险分析。报告强调五个关键维度，包括网络攻击与劝说/操控，用以评估快速发展的 AI 所带来的前所未有的风险。 [来源-huggingface](https://huggingface.co/papers/2602.14457)
- **面向代理式大语言模型车载助手的反馈时机研究** — 一项控制性混合方法研究（N=45）考察代理式 LLM 驾车助手在多步任务中应如何传达进度与推理过程，与计划步骤和中间结果反馈对比静默的仅最终反应，结果对用户体验和在注意力关键的驾驶场景下的安全性具有影响。 [来源-huggingface](https://huggingface.co/papers/2602.15569)
- **Arcee Trinity Large 技术报告发布；Nano 与 Mini 细节** — Arcee Trinity Large 的技术报告介绍一种稀疏专家网络模型，总参数量 400B，每个 token 激活 13B。报告还覆盖 Trinity Nano（总量 6B，激活 1B）与 Trinity Mini（总量 26B，激活 3B），描述使用互插的局部/全局注意力、门控注意力、深度尺度化三明治范式以及 ME 的 Sigmoid 路由等架构特性。 [来源-huggingface](https://huggingface.co/papers/2602.17004)
- **本周顶级 OpenRouter 模型：华人主导地位空前** — OpenRouter 展示前所未有的标记使用量，一模型周授超过 3 万亿令牌，且不止一个模型跨越 1 万亿令牌。这标志着规模与性能的里程碑，凸显中国模型在该领域对美系同行的超越。趋势提示开源大语言模型领域的领导权正在发生转移。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9zt8m/the_top_3_models_on_openrouter_this_week_chinese/)
- **ByteDance Ouro-2.6B-Thinking 实现首个工作推断** — 字节跳动发布 Ouro-2.6B-Thinking，是一种循环式通用 Transformer，按每个 token 进行 192 次有效经过，与传统的一次通过模型不同。作者说明为兼容 transformers 4.55 做出修正——解决 UniversalTransformerCache 属性以及缺失的 get_mask_sizes() 方法，使得首次实现可工作推断。在一个测试提示中，该模型对 2+2 输出 4，NVIDIA L4 的性能约为 3.8 t/s，显存 5.3 GB。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ramir9/release_ouro26bthinking_first_working_inference/)
- **Qwen3 Coder Next 以激进量化超越 30B 模型** — Reddit 发帖称 Qwen Next Coder 在 Q2 量化下避免了无意义输出，甚至能在提示时自行纠错，能够胜过若干 30B 量级模型。作者对其在激进量化下的表现感到惊讶，并征求他人经验与解释其有效性的原因。讨论聚焦于模型量化及轻量级 LLM 的比较性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rabg6o/qwen3_coder_next_oddly_usable_at_aggressive/)
- **Vellium 0.3.5：写作模式大改造、KoboldCpp 原生化、TTS** — Vellium 从 v0.2.8 更新至 v0.3.5，重构写作模式，新增书籍大纲、直接 DOCX 导入、缓存的书籍摘要，并提升 UI/UX 与项目导出/导入的稳定性。还实现了 KoboldCpp 的本地原生集成，与官方 API 的字段保持一致，并修复了模型加载问题。此外，新增与 OpenAI 兼容的文本转语音（TTS）以及分离翻译模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rafo5b/update_vellium_v035_massive_writing_mode_upgrade/)
- **TeichAI GLM-4.7、Flash-Claude、Opus-4.5 高推理蒸馏在 GGUF 上** — TeichAI 发布了一组开源大型语言模型，包括 GLM-4.7、Flash-Claude 与 Opus-4.5，被描述为 GGUF 格式的高推理蒸馏，面向 Hugging Face。昨日由 Unsloth 在 X 上展示，并由 Reddit 用户 /u/jacek2023 于 r/LocalLLaMA 分享。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ranako/teichaiglm47flashclaudeopus45highreasoningdistillg/)

### AI 安全

- **不列颠哥伦比亚省校枪手的 ChatGPT 对话由 OpenAI 员工审阅** — 新报道显示，校枪手的 ChatGPT 消息不仅被自动化系统标记，还有多达 12 名 OpenAI 员工进行了审阅与讨论。这一披露凸显在高风险事件中的人工参与度以及 AI 安全内容审核的水平。 [来源-twitter](https://x.com/AricToler/status/2024976260749820067)
- **基于轨迹的安全审计评估 Clawdbot（OpenClaw）** — 研究人员呈现对 Clawdbot 的轨迹为中心的安全评估，在六个风险维度上进行测试。测试套件从 ATBench 与 LPS-Bench 仿真情境入手，并添加手工设计的案例以在模糊性与对抗性引导下进行安全压力测试。 [来源-huggingface](https://huggingface.co/papers/2602.14364)

### AI 在媒体

- **Stellen Skarsgård 谈 AI 在电影行业中的日益增长作用** — Stellen Skarsgård 讨论 AI 在电影行业中的影响力扩大，强调电影仍然关乎描述人际关系和未言明之处。他警示 AI 的影响取决于谁来掌控它，指出资本集中与科技巨头的所有权是行业面临的关键挑战。 [来源-twitter](https://x.com/Variety/status/2024983345499963815)

### 开源

- **ggml.ai 加入 Hugging Face，推动 llama.cpp 与开源化进程** — ggml.ai 加入 Hugging Face，继续打造 ggml、提升 llama.cpp 的易用性与可访问性，助力开源社区在本地硬件上高效运行 AI。 [来源-twitter](https://x.com/ggerganov/status/2024839991482777976)

### 强化学习

- **AutoWebWorld 使用有限状态机合成可验证的网页环境** — AutoWebWorld 提出一种框架，用有限状态机来合成可控且可验证的网页环境。该方法旨在降低为训练自主网页 GUI 代理而采集真实交互数据的高成本与验证难题，通过生成具可验证逐步正确性的轨迹并减少对外部验证者的依赖，提供可扩展、可验证的训练环境。 [来源-huggingface](https://huggingface.co/papers/2602.14296)

### 具身 AI

- **RynnBrain 发布开源具身基础模型** — RynnBrain 推出一个面向具身智能的开源时空基础模型，整合感知、推理与规划以适应真实世界的动态。强调自我中心理解、时空定位与物理着陆在同一框架中的重要性。 [来源-huggingface](https://huggingface.co/papers/2602.14979)
- **HERO 实现开放词汇的人形机器人运动与操作** — 这项工作解决了利用 RGB-D 输入进行视觉定位与操控的人形机器人运动与操作的开集问题，指出当前的模仿学习方法在面对大规模训练数据时的泛化能力不足。论文提出 HERO，为对象运动与操作提供开放词汇感知与控制的新范式，以提升泛化能力。 [来源-huggingface](https://huggingface.co/papers/2602.16705)

### 扩散模型

- **UL：联合正则化扩散先验来训练潜在变量** — UL 引入一个框架，联合正则化的扩散先验通过解码的扩散模型来学习潜在表示。通过将编码器输出的噪声与先验的最小噪声水平绑定，UL 产生一个上界潜在比特率的训练目标。在 ImageNet-512 上，UL 取得了 1.4 的竞争性 FID 与高 PSNR 的重建，同时使用的训练 FLOPs 低于同类基线。 [来源-huggingface](https://huggingface.co/papers/2602.17270)

## ⚡ 快讯速览

- **Claude Code 为 CLI 增添内置的 git worktree 支持** — Claude Code 现在在 CLI 中也提供内置的 git worktree 支持，允许多代理并行运行且互不干扰。每个代理获得自己的 worktree，可以独立运行。这将此前仅在桌面端的功能扩展到 CLI；更多信息请参见 git-scm.com/docs/git-worktree。 [来源-twitter](https://x.com/bcherny/status/2025007393290272904)
- **OpenAI 各部分进展积极，团队感到自豪** — 一条推文强调 OpenAI 各团队与组件的广泛积极进展。作者表达对团队努力与动量的自豪。 [来源-twitter](https://x.com/gdb/status/2024985187579560366)
- **SLA2 引入可学习路由以提升注意力效率** — 提出一种改进的 Sparse-Linear Attention (SLA2) 架构，具备在稀疏分支与线性分支之间的可学习路由，以及对量化感知的训练（QAT），以加速扩散模型的注意力运算。作者认为 SLA 在注意力权重的大小上进行的启发式分割可能并非最优，并指出直接将稀疏注意力与线性注意力解耦的方式更合适。该工作作为 HuggingFace 的研究笔记，旨在提升扩散模型视频生成的效率。 [来源-huggingface](https://huggingface.co/papers/2602.12675)
- **CADEvolve 通过程序进化实现更真实的 CAD** — CADEvolve 提出使用程序进化来生成更真实的 CAD 任务，目标实现工程建模的全自动化。报告指出进展受限于数据质量，公开语料库多聚焦于简单的草图-挤出工作流，缺乏复杂操作与设计意图。尝试用冻结的视觉-语言模型来弥补数据缺口往往会产生简单或无效的 CAD 程序，因为对 3D 着陆的 grounding 不充分。 [来源-huggingface](https://huggingface.co/papers/2602.16317)
- **Recall Bottleneck Shapes Parametric Factuality in LLMs** — 标准的大语言模型事实性测试对错误统一处理，掩盖了错误来源于知识缺失还是访问受限。文章提出一种行为框架，通过将事实编码为状态与可及性来对事实进行分组：无法回忆、直接回忆、仅在推理时可回忆。聚焦事实而非问题，旨在更好地诊断并改善 LLM 的参数化事实性。 [来源-huggingface](https://huggingface.co/papers/2602.14080)
- **通过上下文共同玩家推理实现多智能体协作** — 本研究探讨自利代理在多智能体强化学习中如何实现协作，提出考虑并塑造共同玩家的学习动态的学习型代理，以推动互惠协作，避免对共同学习规则的硬编码假设。 [来源-huggingface](https://huggingface.co/papers/2602.16301)
- **Cord 协调 AI Agent 树** — Cord 提出一个用于协调多 AI 代理以树状排列的框架，探讨分层协调、通信策略和模块化组件，以提升 AI 系统的可扩展性。 [来源-hackernews](https://www.june.kim/cord)
- **PentAGI：用于渗透测试的自治 AI 代理** — PentAGI 是一个开源工具，使用自治 AI 代理执行复杂的渗透测试任务。它在沙箱 Docker 环境中运行以实现隔离，目标用户为信息安全专业人员与研究人员，文档覆盖概览、功能、设置、开发/测试等。 [来源-github](https://github.com/vxcontrol/pentagi)
- **obra 的 Superpowers：用于编码代理的自主技能** — Superpowers 是一个开源的软件开发工作流，基于可组合的“技能”和起始指令来构建编码代理；它引导代理先澄清用户目标，交付经过签署的、分块的规格，以及强调红/绿 TDD、YAGNI 与 DRY 的可执行计划，然后由子代理驱动执行。该项目在 GitHub 的 obra/superpowers 仓库中。 [来源-github](https://github.com/obra/superpowers)
- **Hugging Face Skills 使 AI 任务实现互操作性** — Hugging Face 推出 Skills，这是一个用于数据集创建、模型训练与评估等 AI/ML 任务的自包含框架。Skills 的包、指令、脚本和资源位于包含 YAML 前言的 SKILL.md 文件夹中，设计用于与 OpenAI Codex、Claude Code、Gemini CLI、Cursor 等主流编码代理实现互操作。尽管“Skills”在 Claude AI 中属于 Anthropic 的术语，但该仓库强调通过 Agent Skill 格式实现工具间的标准化。 [来源-github](https://github.com/huggingface/skills)
- **新泽西州居民击败 AI 数据中心** — 新布朗斯维克 (New Brunswick) 所在的新泽西州居民组织起来反对拟建 AI 数据中心。通过抗议与社区行动，他们使该项目遭遇挫败，标志着对 AI 基础设施的草根层面抵抗。 [来源-hackernews](https://www.commondreams.org/news/new-brunswick-ai-data-center)
- **AI 助手成为所有开发者的广告平台** — Hacker News 讨论聚焦 Juno Labs 博客的观点，认为每一家在构建 AI 助手的公司都通过广告与数据来实现盈利，将用户交互转化为广告定向数据。这一观点引发隐私与商业模式的讨论，因为 AI 助手日渐成为广告平台。 [来源-hackernews](https://juno-labs.com/blogs/every-company-building-your-ai-assistant-is-an-ad-company)
- **StepFun AI 宣布 LocalLLaMA 社区问答会 AMA** — StepFun AI 宣布在 LocalLLaMA 社区的首次 AMA，邀请高层与研究人员参与。活动将于 2 月 19 日太平洋标准时间 8–11 点举办，随后有 24 小时的跟进问答，涵盖 StepFun 的 Step 家族模型，包括 Step 3.5 Flash 与 Step-3-VL-10B。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r8snay/ama_with_stepfun_ai_ask_us_anything/)
- **GLM 5 展现出 Claude 风格的个性** — Reddit 帖子称 GLM 5 在按 Claude 提示指令时会呈现出 Claude 式的人格特征，包括写作风格的改变以及看似绕过安全过滤的现象。作者指出其他提示并未产生同样效果，暗示训练数据、隐藏提示或新兴行为的潜在影响。讨论还提及与 Claude Code 的潜在关联，但尚未得到证实。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1raf3dm/glm_5_seems_to_have_a_claude_personality/)
- **你最喜欢的较少为人知的 Hugging Face 模型有哪些？** — 一位教授在 Reddit 社区征集对 Hugging Face 上较少知名但有用的模型的推荐，旨在帮助学生拓宽对 AI 模型的认知，并邀请熟练的回应者分享有趣的选项。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rajez2/what_are_your_favorite_lesser_known_models_on/)
- **Kimi 拟扩大上下文窗口的野心** — Reddit 帖子讨论 LocalLLaMA 的 Kimi 模型在追求更大上下文窗口的情况，指出对更长输入序列的潜在收益，并强调内存用量与效率等挑战。讨论聚焦于扩大模型令牌上下文的可行性与影响。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9qa7l/kimi_has_context_window_expansion_ambitions/)
- **最佳音频模型 2026 年 2 月 Megathread** — Reddit 的最佳音频模型主题聚焦 AI 在音频领域的最新进展，特别是 Qwen3 TTS。邀请对 ASR、TTS、STT 与文本音乐的设置、用法与工具进行详细对比，偏好开源权重模型。帖文指出 ElevenLabs v3 等封闭模型在生产环境中往往优于开源模型，并鼓励基于社区的实证评估。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r7bsfd/best_audio_models_feb_2026/)
- **AI 奇点起飞：欢迎进入新纪元** — X/Twitter 发布贴文宣称 AI 奇点已经到来，AI 正在起飞。信息传达出对 AI 快速进步的乐观态度，但未提供具体细节，标志着围绕 AI 进展的热度持续上升，而非可核实的主张。 [来源-twitter](https://x.com/scaling01/status/2024925692853395618)
- **对 AI 副项目的批评引发辩论** — Dylan Castillo 的文章批评 AI 的副项目，认为它们分散了对更有意义的 AI 发展的关注。这篇文章在 Hacker News 上引发大量互动（67 点与 91 条评论），并链接至 dylancastillo.co。 [来源-hackernews](https://dylancastillo.co/posts/ai-side-projects.html)
- **Phil Spencer 离开微软，AI 高管接任 Xbox 主管** — Phil Spencer 将离开微软，AI 高管接任 Xbox 领导职务。此举显示将 AI 领导力嵌入微软的游戏策略之中，同时也将 Xbox 的责任从 Spencer 转移，体现公司在 AI 驱动的优先级上的更广泛取向。 [来源-hackernews](https://www.neowin.net/news/phil-spencer-is-exiting-microsoft-as-ai-executive-takes-over-xbox/)
- **关于 LocalLLaMA 的 Deepseek 与 Gemma 的提问** — Reddit 用户 /u/ZeusZCC 提出对 Deepseek 与 Gemma 两个 AI 相关项目的疑问，未提供额外上下文。帖子链接至 LocalLLaMA 讨论区，未给出进一步细节。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9uuc6/deepseek_and_gemma/)

---

*Generated by AI News Agent | 2026-02-20*