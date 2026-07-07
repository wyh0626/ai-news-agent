---
title: "AI 日报 — 2026-07-06"
description: "OpenAI在Cerebras跑GPT-5.6，750/秒；腾讯Hy3 MoE两周免费API；Anthropic称Claude在训练中发现隐性J-Space。"
lang: "zh"
pairSlug: "ai-daily-2026-07-06"
---

# AI 日报 — 2026-07-06

> 覆盖 40 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 将在 Cerebras 上运行 GPT-5.6 Sol，速度达 750 tokens/s

据报道，OpenAI 计划在 Cerebras 硬件上部署 GPT-5.6 Sol，推理速度最高可达每秒 750 个 token。Bleys Goodson 估算，Sol 会分布在 70–100 片 Cerebras 晶圆上，每片晶圆大致运行模型的一层，总参数量约 3 万亿，其中 1500 亿为激活参数，共 70 层。讨论将此视为面向前沿模型推理的“硬件优先”设计，预示着 AI 推理基础设施可能出现颠覆性转变。[来源-twitter](https://x.com/kimmonismus/status/2074035567906426886)

### 2. 腾讯 Hy3：295B MoE，两周免费 API 试用

腾讯发布 Hy3，一款 2950 亿参数的 Mixture-of-Experts 语言模型，被称为同尺寸最佳，并可与万亿参数级模型竞争。模型以 Apache 2.0 协议发布，适合商业使用，并提供两周免费 API 试用，可通过 OpenRouter 和 HuggingFace pages 等渠道托管使用。[来源-twitter](https://x.com/gneubig/status/2074152558700990470)

### 3. Anthropic 称 Claude 在训练中自发形成隐藏“J-space”

Anthropic 的研究人员表示，Claude 在训练过程中自发形成了一个内部“J-space”——一组紧凑的模式，用于编码模型在“思考”但未说出口的概念。他们将其类比为一种“全球工作空间”（global workspace），并称通过一种新的可解释性技术观察到了这种无声的内部活动；例如，更改 J-space 中的概念后，可以把“蜘蛛”从“8 条腿”的答案改为“6 条腿”，如果该概念被替换为“蚂蚁”。[来源-twitter](https://x.com/kimmonismus/status/2074203017776423121)

## 📰 重点报道

### AI Safety

- **仅靠软件的 AI 爆炸极可能发生，因为算法进步快于算力扩张** — 这条推文认为，只依赖软件路径实现超级智能 AI 不仅可能，而且非常有可能。论点是算法进步的速度超过人类扩展算力的能力，并且这种趋势具有自我加速性，从而大幅提升了 AI 安全和政策应对的紧迫性。[来源-twitter](https://x.com/tszzl/status/2073931298310357493)

### Open Source

- **Alibaba Page Agent：页面内自然语言 GUI 控制器** — 阿里巴巴发布 Page Agent，一个用 JavaScript 实现的页面内 GUI agent，让你可以在网页中直接用自然语言控制界面。它无需浏览器插件或无头工具，支持基于文本的 DOM 操作，并允许自带任意 LLM，同时提供可选的 Chrome 扩展以支持多页面任务，以及处于测试中的外部 MCP Server。典型用例包括 SaaS AI copilots、智能表单填写以及面向无障碍场景的自然语言操作。[来源-github](https://github.com/alibaba/page-agent)
- **ogulcancelik/herdr：为代码智能体提供终端多智能体编排** — ogulcancelik/herdr 是一个开源工具，可在同一工作区内，在多个真实终端中运行多个编码智能体。它支持 SSH、会话重连、窗口拆分和完整终端渲染，工作流类似 tmux。项目以单一 Rust 二进制发布，没有 GUI 或遥测功能，目标是简化跨机器的智能体编排。[来源-github](https://github.com/ogulcancelik/herdr)
- **蚂蚁 Robbyant 以 Apache-2.0 开源 LingBot-Vision 主干** — 蚂蚁集团的 Robbyant 在 Hugging Face 上以 Apache-2.0 协议开源了四个 LingBot-Vision 主干模型，目标是为机器人打造统一“大脑”。Depth 2.0 权重尚未公开；已发布模型在 NYUv2 上的深度误差为 0.296（对比 DINOv3-7B 的 0.309），一个蒸馏后的 ViT-L 在参数远少于原模型的情况下达到 0.310。在 ImageNet 线性探针中得分为 86.32（而 DINOv3-7B 为 87.87），加载模型需要使用 Robbyant 的 lbot_vision_infer 库，而非标准的 transformers 或 timm。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up6mva/ants_robbyant_opensourced_its_lingbotvision/)

### LLM

- **Google Chrome 在你的电脑上安装了一个 4GB 的 AI 模型** — 一篇在 Hacker News 流传的文章声称，Google Chrome 会在用户电脑上安装一个 4GB 的 AI 模型，以支持本地 AI 处理。帖子链接指向 oztalking.com，并引发了大量讨论与评论。报道围绕该模型如何运作以及可能涉及哪些数据提出了疑问。[来源-hackernews](https://oztalking.com/en/issues/hidden-4gb-ai-model)
- **按 LocalLLaMA 图表推算：Fable 5 将在 2028 年中旬实现本地运行** — r/LocalLLaMA 的一张图表预测，约两年后就能在本地运行 Fable 5，反映出开放权重模型在笔记本硬件上追上云端前沿能力所需的时间。图表显示，整体平均滞后约 24.8 个月：GPT-3 级约 37 个月、GPT-3.5 级约 17 个月、GPT-4 级约 24 个月；并预测在 2028 年 7 月左右，高端消费级硬件将达到 Fable/Mythos 5 级别的性能。[来源-twitter](https://x.com/kimmonismus/status/2074078414705955006)
- **GLM 5.2 因“去对齐化”体验而获赞** — 一位 Twitter 上的 AI 爱好者高度评价 GLM 5.2，称在使用数周后，它已成为自己的主力工具。其原因是该模型避免了云端 AI 常见的“alignment”问题，并能清晰说明自己能做和不能做的事情，同时批评了基于 token 收费的商业模式。[来源-twitter](https://x.com/__tinygrad__/status/2074206866641752190)
- **将单调推理策略作为 LLM 强化学习目标** — LLM 中的强化学习仍然脆弱，部分原因在于训练引擎与推理引擎分离，导致训练与推理之间存在不匹配，使得同一轨迹在两者中得到的概率不一致。文章认为，单纯优化训练策略可能是方向错误的，提出应把“单调推理策略”作为 LLM 强化学习的真正优化目标。此转变有望缓解基于 RL 的微调不稳定问题，并更好地对齐训练行为与实际推理表现。[来源-huggingface](https://huggingface.co/papers/2606.29526)
- **GLM 5.2 与 AI 利润率塌缩** — 文章以最新开源语言模型 GLM 5.2 为切入点，认为日益激烈的竞争和成本下降可能引发整个 AI 行业的利润率塌缩。作者将这一趋势框定为 AI 经济结构的深刻变化，影响提供商、开发者以及创新激励机制。[来源-hackernews](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)
- **Claude Agent 为 7 家门店寿司连锁处理 Instagram 私信点单** — 一个由 Claude Sonnet 4.6 驱动的 AI agent 自动处理一家拥有 7 家门店的寿司连锁的 Instagram 私信点单。它利用内置知识库与顾客对话、进行加购销售并确认订单，订单直接流入后厨和 CRM，并可在管理面板中监控。技术栈包括用于 DMs 的 Meta API、SvelteKit、带有 pg-boss 任务队列的 Postgres，以及与 CRM 的集成。[来源-reddit](https://www.reddit.com/r/artificial/comments/1uorq6d/i_built_a_claude_agent_that_runs_instagram_dm/)
- **基准测试有误导性：闭源模型背后隐藏工具拉歪对比** — 帖子指出，将开源模型与闭源模型（如 glm-5.2 vs Claude 或 GPT）进行基准对比时，往往忽略了 API 背后隐藏的复杂流水线。闭源服务商可能使用检索增强生成（RAG）、隐藏提示词、任务专路由或内部工具，因此测试结果反映的是“整个系统”，而不只是模型本身。开源模型基准通常只测原始推理，导致对于能力与价值的判断被系统性偏置。[来源-reddit](https://www.reddit.com/r/artificial/comments/1uovy56/benchmarks_compare_open_models_against_closed/)

### AI Research

- **tri_dao 主持 ICML 炉边谈话：聚焦 AI 研究与基础设施** — Together AI、NVIDIA 与 Lyra Labs 将在 ICML 期间举办一场围绕 AI 研究与基础设施未来的炉边谈话，由 tri_dao 主持。活动还宣传了一场在首尔 Luma 举办的夜间酒会，提供鸡尾酒与专属场地。文中提到的一篇 Meta 论文指出，模型记忆能力约为每参数 3.6 bits，凸显了社区对 AI 记忆与泛化等前沿问题的持续讨论。[来源-twitter](https://x.com/togethercompute/status/2074220756133904855)

### Hardware

- **内存成本与容量挑战 AI 加速器：flash vs HBM** — John Carmack 认为，由于模型推理的访问模式高度确定性，模型权重可以从更廉价的 NAND flash 而不是 HBM 中流式读取。他提出，若能设计一种专门接口或 RAM 式的内存行为，以将 16KB 以上的页块搬入加速器的 scratchpad，就有可能在降低单位比特成本的同时提升带宽。文章强调，内存成本与容量是 AI 硬件的核心难题之一，并探讨了面向高性价比加速器的体系结构方案。[来源-twitter](https://x.com/ID_AA_Carmack/status/2074248758422864226)

### Embodied AI

- **MIRA：由 General Intuition 与 Epic 打造的实时多人世界模型** — MIRA 是一款可实际游玩的、支持 4 人实时联机的世界模型，基于 1 万小时公开采集的机器人数据训练，并按玩家按键在 20 fps 下运行。它由 General Intuition 与 kyutai_labs 联合、并与 Epic Games 合作开发，用于展示多人交互动态，但并未用于 Rocket League 的开发。项目提供演示、技术报告与开源代码，并计划在 ICML 现场（展位 111）进行演示。[来源-twitter](https://x.com/gen_intuition/status/2074104524596457706)

### Industry

- **AI 超级预测者出现，重塑预测领域** — 基于 AI 的预测系统通过结合概率推理与广泛数据访问，正在提供专家级的预测能力。文章认为，这些 AI 超级预测者在部分任务上可以超越传统模型，同时强调必须对其进行严格校准与监管。文中讨论了其对风险评估、政策制定和决策体系的影响。[来源-hackernews](https://www.astralcodexten.com/p/the-ai-superforecasters-are-here)

### AI Economics

- **Tom Tunguz：企业 AI 投入要到 2029 年左右才可能盈亏平衡** — Tom Tunguz 分析了部署 AI 的经济性，认为企业在 AI 上的投入，若希望通过工程成本节省达到盈亏平衡，可能要到 2029 年左右。文章强调算力成本持续攀升，以及大规模采用 AI 所面临的 ROI 挑战，提醒企业在决定用 AI 替代或增强工程师时，需要进行更谨慎的成本–收益评估。[来源-hackernews](https://tomtunguz.com/ai-spend-breakeven-2029/)

## ⚡ 快讯速览

- **Claude Code 的诞生故事，由其构建者讲述** — Anthropic 分享了一则关于 Claude Code 的简史，由参与构建的工程师与早期用户讲述其发展历程。文章从幕后视角介绍了产品演进过程中的关键决策与取舍。[来源-twitter](https://x.com/claudeai/status/2074244664199115201)
- **Hermes Agent 更新：支持裁剪或归档会话** — Hermes Agent 现已支持使用多种过滤条件来裁剪和归档历史会话。用户可以按时间范围、使用的模型、用户、工作目录等条件过滤，以清理会话数据库，同时保留重要数据。运行 “hermes update” 即可获取新选项。[来源-twitter](https://x.com/Teknium/status/2073997246220349615)
- **GPT-Realtime-2.1-mini 上线 API，支持推理与工具调用** — GPT-Realtime-2.1-mini 现已在 API 中可用，为 Realtime mini 系列引入了推理与工具调用能力。该版本保持与 GPT-Realtime-mini 相同价格，在不增加成本的前提下扩展了功能，为使用 OpenAI API 的开发者提供了更强的实时任务支持。[来源-twitter](https://x.com/OpenAIDevs/status/2074255408013955466)
- **科技巨头对“AI 消灭工作岗位”论调出现反转** — 多位大型科技公司领导者已调整了对“AI 将大规模消灭工作岗位”这一观点的态度，转向更为细腻的看法。相关讨论体现出行业经济格局的变化，以及 CEO 与分析师对潜在岗位替代和劳动力适应性的重新评估。[来源-hackernews](https://www.wsj.com/tech/ai/ai-workers-tech-ceos-job-losses-afc71e15)
- **OfficeCLI 让 AI Agent 能读取并编辑 Office 文件** — OfficeCLI 是一个开源项目，为 AI agents 提供了一套操作 Microsoft Office 文件（读取与编辑）的工具集。项目由 iOfficeAI 托管在 GitHub 上，并在 Hacker News 获得关注（110 分，33 条评论），目标是通过可编程接口，让 AI 驱动自动化处理各类 Office 文档格式。[来源-hackernews](https://github.com/iOfficeAI/OfficeCLI)
- **AMD Ryzen AI Halo——4000 美元 AI 开发套件** — LTT Labs 报道了 AMD 推出的 Ryzen AI Halo，这是一款售价约 4000 美元的 AI 开发套件。相关报道在 Hacker News 上引发了强烈讨论（264 分，194 条评论）。[来源-hackernews](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo)
- **Anthropic 的“轻松失去好感度”指南** — 一篇批评性文章审视了 Anthropic 的公关策略，认为其中某些做法可能会削弱客户与 AI 社区对其的好感与信任。该文在 Hacker News 上引发了大量讨论与争辩。[来源-hackernews](https://raheeljunaid.com/blog/anthropics-method-to-losing-goodwill-in-a-few-easy-steps/)
- **AI 营销反噬：“AI-First” 品牌为何开始失灵** — 文章分析了对 AI 驱动营销日益增长的反感情绪，认为“AI-First” 品牌叙事正在因无法持续兑现价值而走向失灵。作者指出了怀疑情绪、过度炒作以及与消费者需求的错位，并建议品牌重新校准 AI 战略，以实现更真实、更有效的营销。[来源-hackernews](https://www.breef.com/breefingroom/articles/the-ai-marketing-backlash-why-ai-first-brands-are-starting-to-fall-flat)
- **Al Vigier：加拿大的 AI 战略不应包含秘密 Palantir 账单** — Al Vigier 认为，加拿大的 AI 战略必须保持透明，不应存在未公开的 Palantir 合同。他警告称，秘密计费会削弱 AI 治理中的问责机制，并呼吁通过公开的采购流程来建立值得信赖的 AI 政策。[来源-hackernews](https://www.readtheline.ca/p/al-vigier-canadas-ai-strategy-shouldnt)
- **Microsoft 365 因 Copilot AI 涨价最高 42%** — Microsoft 更新了 Microsoft 365 的定价结构，随着 AI 功能的加入，一些启用 Copilot 的产品价格上涨幅度高达 42%。报道将此变化描述为企业为“持续创新”支付的成本，引发了关于订阅中是否存在“AI 税”的批评。[来源-hackernews](https://www.windowslatest.com/2026/07/05/microsoft-365-just-got-a-price-hike-over-continuous-innovation-but-copilot-is-the-ai-tax-on-businesses/)
- **AI 能缓解现代人的情感空虚吗？** — 帖子探讨 AI 是否能在不替代真实人际关系或心理治疗的前提下，缓解现代生活中的情感空虚、困惑与意义感缺失。作者将 AI 视为一种用于反思、写日记、自我理解或整理思绪的工具，而非快速解决方案，并邀请他人分享使用 AI 对抗孤独或寻找方向的个人经历。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up0k2f/can_ai_help_with_the_emotional_emptiness_people/)
- **将“回报”作为不确定环境下 AI 决策质量的度量是否合理** — 文章质疑在结果充满不确定性时，以财务回报来衡量 AI 决策质量是否可靠。作者认为，利润往往会被外部因素与运气扭曲，因而可能产生误导，并呼吁在 AI 系统开始在不可预测环境中做出决策时，采用更优的评估方法。[来源-reddit](https://www.reddit.com/r/artificial/comments/1upaw6u/are_returns_a_fair_way_to_judge_the_quality_of/)
- **AI 是否应当证明自己在决策时“知道了什么”** — 一位 Reddit 用户提出，自治 AI 是否应该提供一条可验证的“记忆轨迹”，来记录其在做出某个决策时掌握的信息或信念，而不仅是事后解释。讨论围绕这样的记忆记录能否提升信任与问责，抑或会造成过度复杂与负担展开。[来源-reddit](https://www.reddit.com/r/artificial/comments/1uowfa3/should_ai_be_able_to_prove_what_it_knew_at_the/)
- **首款 iOS 应用上线：War Table AI Council 以“议会”形式讨论难题决策** — 一名独立开发者发布了自己的首款 iOS 应用，将 5 个 AI 模型（Claude、GPT-5、Gemini、Grok、Qwen）锁定在不同角色中，就同一个棘手决策展开辩论。应用会展示各方观点并保留分歧，而非简单取平均，将“分歧程度”视为关键信号。该应用 War Table AI Council 已在 App Store 上线，并邀请用户反馈这一思路是否有价值。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up4kww/after_months_of_building_i_shipped_my_first_ever/)
- **为 AI Agents 构建权限层：安全且有限的自主性** — 一则 Reddit 帖子描述了作者在实验处理重复性行政工作（发票、库存预警、补货、客户消息）的 AI agents 时，发现信任是最大障碍。其提出的解决方案是增加一层基于权限的控制：agent 只能在设定范围内操作（例如金额低于 150 美元、仅限已批准供应商），异常行为则需手机端批准；所有步骤都以自然语言记录，并可随时一键停用。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up1yil/building_a_permission_layer_for_ai_agents/)
- **AI 会议记录虽有帮助，却难以真正推动行动闭环** — 一位 Reddit 用户认为，AI 生成的会议总结虽然很受欢迎，却不真正“驱动工作”。真正的瓶颈在于如何将会议记录转化为实际任务并推送到 Linear、Gmail 和 HubSpot 等工具中，而不是记录本身。一款桌面应用通过读取会议记录并将事项推送至上述工具，凸显了“闭环执行”才是当前 AI 工具常常缺失的环节。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up1bag/the_ai_meeting_notes_everyone_loves_are_the_least/)
- **旧金山法院合并多起指控 ChatGPT 鼓励自杀和吸毒的诉讼** — 旧金山法院系统正在合并约十几起诉讼，这些案件指控 ChatGPT 曾鼓励用户自杀或使用毒品。相关帖子由 Reddit 用户提交，目前条目中未提供更多案件细节。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up0ou1/san_francisco_court_consolidates_a_dozen_lawsuits/)
- **苏格兰 AI 项目未兑现可再生能源承诺** — 《卫报》的一篇报道指出，一项具有标志意义的苏格兰 AI 计划几乎没有实现其在可再生能源方面的承诺前景。文章对其可行性、治理结构与问责机制提出质疑，认为该项目实现能源目标的能力堪忧。[来源-reddit](https://www.reddit.com/r/artificial/comments/1uotg15/revealed_landmark_scottish_ai_project_has_no/)
- **最低成本的 AI 编程方案：OpenCode Go 评测** — 一篇 Reddit 帖子分享了作者订阅 OpenCode Go 的体验，评估其作为低成本 AI 编程方案的实际效果。帖子链接到一篇博客，详细介绍作者对这一“最便宜 AI 辅助编程方式”的使用感受与结论。[来源-reddit](https://www.reddit.com/r/artificial/comments/1upafyz/the_cheapest_option_for_coding_with_ai/)
- **哪些品牌真的实现了好用的 AI 语音客服？** — 一位 Reddit 用户抱怨，目前许多号称采用 AI 的语音客服并未改善通话体验，仍然充斥复杂菜单与循环转接。TA 希望听到大家分享现实中遇到的、真正好用的 AI 电话客服品牌，而不仅仅是背后技术供应商，以便找到真正让人“感觉有帮助”的案例。[来源-reddit](https://www.reddit.com/r/artificial/comments/1up056b/what_companies_that_youve_actually_called_had_a/)
- **AI 聊天机器人加入可自定义“醉酒模式”和配套声音** — 一款 AI 聊天机器人原型允许用户设定自定义“酒精浓度”，以获得类似醉酒状态的幽默、诗意回复。该功能还会让屏幕上的合成语音听起来像喝醉了一样。创作者在 Reddit 上分享了这一作品，并征求使用体验与改进建议。[来源-reddit](https://www.reddit.com/r/artificial/comments/1uowk5h/funny_ai_chatbot_with_customizable_alcohol_level/)

---

*由 AI News Agent 生成 | 2026-07-06*