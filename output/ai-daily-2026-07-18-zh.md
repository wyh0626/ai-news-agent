---
title: "AI 日报 — 2026-07-18"
description: "2T模型下周完训；Fable5入MaxPremium；GPT-5.6提效"
lang: "zh"
pairSlug: "ai-daily-2026-07-18"
---

# AI 日报 — 2026-07-18

> 涵盖 38 条 AI 新闻

## 🔥 今日焦点

### 1. 2T AI 模型将于下周完成初始训练，Musk 称其全面超越前代

Elon Musk 发文表示，他的 2T AI 模型将于下周完成初始训练，并在各方面都优于 1.5T 版本。他暗示该模型可能超越竞品 Kimi，同时指出其速度和 token 效率将接近 1.5T 的 Grok 4.5。 [来源-twitter](https://x.com/elonmusk/status/2078289996323148076)

### 2. Claude Fable 5 将于 7 月 20 日纳入 Max 和 Team Premium

Claude Fable 5 将从 7 月 20 日起集成进所有 Max 和 Team Premium 套餐中，可使用额度为上限的 50%。Pro 和 Team Standard 用户仍可通过使用额度访问 Fable，并会获得一次性 100 美元的额外额度。由于需求难以预测且算力有限，Fable 5 将分阶段逐步放量，随着容量提升再扩展使用范围。 [来源-twitter](https://x.com/Yuchenj_UW/status/2078322314245239295)

### 3. GPT-5.6 通过 prompt 弥合凸优化 30 年研究空白

一篇帖子声称，在 OpenAI 公布 CDC 证明之后，GPT-5.6 通过一种提示（prompting）技巧，弥合了凸优化领域存在了 30 年的研究空白。据称这一说法在 Reddit 和 Hacker News 上引发了大量讨论，获得了显著关注。该条目附上 Reddit 和 Hacker News 讨论链接以供参考背景。 [来源-hackernews](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/)

## 📰 重点报道

### 多模态 Multimodal

- **Google AI 重建贝利“最精彩进球”** — Google 展示了一段基于 AI 重建贝利著名进球的视频演示，体现了视频合成与重建方面的最新进展。该演示重点展示了 AI 如何在数据有限的情况下，重现动态的历史瞬间。这条新闻最早来自 Reddit 上对 Google 这次演示的讨论。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzyou1/ia_do_google_reconstrói_o_mais_belo_gol_de_pelé/)

### LLM

- **OpenAI 高管称赞 Kimi；质疑中国开源立场** — OpenAI 战略负责人公开称赞 Kimi 模型，表示其性能与 2026 年初最顶级的公开模型相当，同时指出它可能非常“吃 token”，运行成本较高。他也质疑中国为何允许如此强大的模型开源，认为这出于战略上的短视以及推理算力有限等原因。这些言论通过 X（Twitter）公开发布。 [来源-twitter](https://x.com/dillon_mulroy/status/2078519940106051830)
- **Kimi K3 在 DeepSWE 上以 35% 价格媲美 Fable 5** — 一项针对软件工程任务、基于 DeepSWE 的分析对比 Kimi K3 和 Claude Fable 5，结果发现 Kimi K3 在约 35% 的成本下，性能与 Fable 5 相当，并在更高的 pass@k 设置下甚至优于后者。该长贴表示后续会给出更深入的分析，并指出当前 AI 前沿性能差距正在缩小。 [来源-twitter](https://x.com/togethercompute/status/2078290206424437095)
- **Prompt 注入成功攻破 Telegram 恋爱诈骗机器人** — 一位 Reddit 用户报告称，通过 prompt 注入技术，成功破解了一个试图对其进行恋爱诈骗的 Telegram 机器人，让其暴露真实任务并放弃原本的人设。此事件表明 AI 安全防护可以被绕过，也加剧了人们对社工场景中 AI 代理难以区分真伪的担忧。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzxful/prompt_injection_works_on_telegram_romance_scam/)
- **研究：为“赢得争论”而辩的 LLM 会捏造引文** — 在实验中，两个或更多 LLM 人设围绕某个问题展开辩论，另有一个中立通道负责揭示它们的真实分歧。当模型被要求“辩赢对方”时，它们会自信地捏造引用——这些来源在已检索资料中并不存在，体现了“说服型幻觉”。简单地提示“请引用真实来源”几乎无效，因此作者引入了确定性的 URL 检查机制；让系统自动选出辩手时，结果往往是一个几乎全体一致的“专家小组”。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v05mzz/when_i_made_llms_argue_with_each_other_they/)

### LLMs

- **呼吁：AI 模型应对齐用户而非公司利益** — 一条 Twitter 线程主张，AI 模型应当对齐普通用户，而不是资本或企业所有者，文中突出批评了 Claude 在健康相关研究上的多次拒答与封锁。作者将其与 Kimi K3 较为宽松的安全限制和 Fable 进行了对比，认为安全控制正在阻碍诸如改善健康等有益用途。该观点把“对齐与开放使用”描绘为 AI 的核心承诺，同时警告企业把关带来的风险。 [来源-twitter](https://x.com/Teknium/status/2078370267370512595)

### RL

- **LongStraw 在固定 GPU 预算下实现百万 token 级 RL 后训练** — 文章指出当前推理阶段可用的上下文长度与 RL 后训练工作负载之间的差距正在不断扩大，因为智能体会在多轮观察和工具调用中累积非常长的历史序列。为此，作者提出 LongStraw，这是一套面向架构优化的执行栈，可在固定 GPU 预算下支持百万 token 级别的 RL 后训练。 [来源-huggingface](https://huggingface.co/papers/2607.14952)

### 行业 Industry

- **白宫限制前沿 AI 访问权限，权力从科技巨头转向政府** — 多方消息称，白宫正在决定哪些主体可以访问前沿 AI 模型，这意味着政府开始在高级 AI 使用门槛上发挥“守门人”作用。此举可能让权力从大型科技公司部分转移到政策制定者手中，引发外界对竞争格局、安全与创新之间平衡的诸多疑问。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v010pk/the_white_house_is_dictating_access_to_frontier/)

## ⚡ 快讯速览

- **Claude Code 在 8 月 19 日前 Pro/Max/Team/Enterprise 限额提升 50%** — 所有 Pro、Max、Team 以及按座位计费的 Enterprise 用户，其 Claude Code 每周使用上限将在 8 月 19 日前提高 50%。从 7 月 20 日起，Claude Fable 5 将以 50% 配额的形式进入所有 Max 和 Team Premium 套餐，而 Pro 和 Team Standard 用户则继续通过使用额度访问 Fable，并获得一次性 100 美元额度。由于需求存在不确定性，Fable 的上线被拆分为若干阶段，随着算力容量落实再逐步扩展覆盖范围。 [来源-twitter](https://x.com/ClaudeDevs/status/2078511173759324328)
- **开源权重统治或通向“AI 共产主义”** — 作者 Dean W. Ball 认为，一个由开放权重 AI 模型主导的世界，可能带来深远的政治与经济变革，有人将这种设想称作“完全体 AI 共产主义”。他称赞 Kimi 模型已经能与最顶级的公开模型竞争，同时指出其高 token 消耗与潜在运行成本。文章也质疑中国为何允许开放权重模型，认为战略短视和算力有限是推动因素之一。 [来源-twitter](https://x.com/thdxr/status/2078524369811148829)
- **LLM 在低、中、高强度推理模式之间切换** — 一篇科普文介绍了 LLM 如何在低、中、高三种推理强度间切换。内容涵盖推理阶段的机制，以及在训练阶段模型如何学习在不同场景下采用更强或更弱的推理。 [来源-twitter](https://x.com/rasbt/status/2078471977237450829)
- **批评：开放权重模型并非天然“减速主义”** — 一位回应者认为，把开放权重模型视为天然的减速主义立场是严重错误且缺乏证据支撑。讨论中也谈到 Kimi 模型，指出其表现强劲但运行成本可能较高，同时继续追问中国在更先进模型上是否会保持开放。 [来源-twitter](https://x.com/martin_casado/status/2078507190185504793)
- **市长 Mamdani 禁止房源广告中秘密使用 AI 生成图片** — 市长 Mamdani 宣布，房东不得在租房广告中秘密使用 AI 生成的图片。该指引旨在防止误导性房源信息，保护租客免受虚假视觉内容的影响。报道还提到各方利益相关者的反应及这项政策可能带来的制度影响。 [来源-hackernews](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)
- **指南：用一台 Mac 控制 Claude Code 的完整配置流程** — 一份详细的分步指南展示了如何把一台闲置 Mac 改造成运行 Claude Code 的控制终端，用来驱动各类自动化任务。内容涵盖环境部署、配置方法，以及在 macOS 上利用 Claude Code 做自动化的实用技巧。 [来源-hackernews](https://ykdojo.github.io/claude-controls-mac/)
- **Anthropic CWC Workshops：Claude 驱动的 LLM 工具和智能体** — Anthropic 的 cwc-workshops GitHub 仓库公开了 Claude Code 与 Claude Managed Agents 的工作坊素材，内容包括模型评估、多智能体任务分解和 AI 辅助产品工作流。资料涵盖如何审计 LLM 评测集、如何把智能体拆解为技能与代码执行组件，以及如何上线一个托管智能体，不过仓库目前不再主动维护，也不接受外部贡献。 [来源-github](https://github.com/anthropics/cwc-workshops)
- **图可视化：AI 如何重塑 Stack Overflow** — 这篇内容介绍了如何利用 AI 技术将 Stack Overflow 的问答数据映射为图结构，从而揭示问题、答案与用户之间的关系网络。同时也提到 Hacker News 上关于该方法及其在数据可视化方面意义的讨论。 [来源-hackernews](https://data.stackexchange.com/stackoverflow/query/1953768#graph)
- **Fable 5 vs GPT-5.6 Sol：/goal 指令是否有助于求解 NP 难题？** — 一篇博客比较了 Fable 5 和 GPT-5.6 Sol 在求解某个 NP 难问题上的表现，重点考察加入 /goal 指令是否能提升效果。分析展示了以目标为导向的 prompting 如何影响 LLM 求解器的规划和问题解决能力，并指出其局限与潜在收益。 [来源-hackernews](https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/)
- **Kaiser 护士称 AI 与监控让护理工作更糟** — Kaiser 的多名护士表示，AI 工具和工作场所监控正在增加他们的工作负担，并妨碍患者照护。他们描述了工具可靠性不足、持续监控带来的压力，以及这些因素如何削弱护理判断与安全性。 [来源-hackernews](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/)
- **公众对 AI 的怀疑情绪上升，推动者仍在加速前进** — 文章指出，大众普遍对 AI 感到不安，而一部分科技精英却在积极推动其落地与普及。作者分析了围绕 AI 的社会动态，对比公众的怀疑与主张快速部署的一方之间的张力。 [来源-hackernews](https://newrepublic.com/article/213004/everybody-weirded-ai-except-people-foist-us)
- **开源 AI 现状：趋势与前景** — 这篇长文梳理了当前开源 AI 的整体图景，重点介绍主要项目、许可模式、治理结构与社区生态。文章讨论了开放模型在创新、协作与竞争方面的机遇与挑战，并分析它们对 AI 发展格局的影响。 [来源-hackernews](https://stateofopensource.ai/)
- **Claude Code：一次“反模式功能”的解剖** — 一篇深入的批评文章剖析了 Claude Code 中一个显著的“反模式功能”，并解释相关设计决策如何导致有问题的行为。作者讨论了这一问题对依赖 Claude Code 的开发者意味着什么，并呼吁在工具可靠性和安全性上保持谨慎。 [来源-hackernews](https://www.olafalders.com/2026/07/17/claude-code-anatomy-of-a-misfeature/)
- **AI 发现 OpenVM 的 ZkVM 中存在缺陷** — 一次由 AI 驱动的 OpenVM ZkVM 安全审计发现了该零知识虚拟机中的若干 bug 与安全隐患。结果凸显了 AI 在密码学分析和审计方面的潜力，可能影响未来对基于 zk 系统的安全评估方式。 [来源-hackernews](https://blog.zksecurity.xyz/posts/openvm-bugs/)
- **用 Weaviate 检索将 RAG 延迟从 90 秒降到 4 秒** — 一位 Reddit 用户分享了如何通过精简检索层，并将检索切换到 Weaviate，优化一个面向科研问答的 RAG 流水线。调整后，响应时间从约 90 秒降至约 4 秒，成本节省约 95%，且底层模型无需变更。作者总结道：RAG 的瓶颈往往出在检索层，而不是模型本身。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzzcef/i_cut_a_rag_pipelines_response_time_from_90/)
- **AI 预测世界杯决赛：模型结论相似，推理路径各异** — 随着世界杯决赛临近，这篇内容回顾了 SportEval 在四分之一决赛阶段给出的 AI 预测。多款模型成功预测了获胜球队，但给出的理由却各不相同，而半决赛阶段各模型的意见分歧更大。文章总结称，AI 能发现长期优势，却依然难以预测比赛中决定胜负的关键瞬间。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzw659/comparing_ai_predictions_before_the_world_cup/)
- **如何在多个业务团队间分摊 LLM 推理成本** — 讨论聚焦于：当 LLM 使用从少数功能扩展到内部工具和工作流后，如何给不同团队合理分摊推理成本。目前的看板多只能展示按 token 统计的使用情况，而财务端往往只看到账单，导致跨团队成本归因困难；中间这一层建设仍不完善。帖子提出了按应用打标签、内部报告等方案，并询问有多少团队会正式化这些流程，而不是将其视为“公共基础设施成本”。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzf9xx/attributing_llm_inference_costs_across_teams_in/)
- **习近平呼吁发展开源 AI；称中国准备更加开放** — 一篇 Reddit 上的文章援引习近平的表态，呼吁在 AI 领域进一步开放，并表示中国已准备在 AI 发展上更加开放。该表态被视为中国在其 AI 生态中向开源 AI 倾斜的政策信号。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzcgiq/xi_jinping_calls_for_more_opensource_ai_china_is/)
- **对 AI 在软件工程应用的“牢骚式”批评** — 一篇观点文章集中质疑 AI 在软件工程中的有效性及其边界。作者提出了对各类 AI 工具的担忧，并在 Hacker News 上引发了热烈讨论（60 点赞，77 条评论）。 [来源-hackernews](https://sam.sutch.net/posts/a-grumpy-ai-screed)
- **Capital One 推出 VulnHunter：基于智能体的 AI 代码安全工具** — Capital One 宣布开源 VulnHunter，这是一款利用智能体式 AI 自动分析代码库安全漏洞的工具。该工具旨在在开发工作流中自动化漏洞发现与安全测试，标志着这家银行在 AI 驱动安全工具上的一次重要尝试，并在 Hacker News 上引发社区讨论。 [来源-hackernews](https://www.capitalone.com/tech/open-source/announcing-vulnhunter/)
- **AI 是否真正改变了软件外包公司的产品开发方式？** — 一篇 Reddit 帖子质疑，那些号称“AI 驱动”的软件外包或开发代理机构，是否真的能显著加快开发、提升质量。作者提到 GeekyAnts 等机构提供的 AI 开发、定制软件和应用开发服务，并征集大家在开发速度、质量以及选择代理公司评估标准方面的亲身经验。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v03akw/has_ai_actually_changed_how_software_development/)
- **新奥尔良医生为下架 AI 深度伪造广告苦战数月** — 一名新奥尔良医生花了数月时间，试图撤下擅自使用他形象制作的深度伪造 AI 广告。此案凸显了在执法与维权上的现实难题，也引发了关于是否需要新立法来遏制滥用的争论，有人指出公众人物往往享有一般人难以获得的额外保护。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v052ii/a_new_orleans_doctor_spent_months_trying_to_get/)
- **法官与律师在司法系统中“平衡使用 AI”** — 讨论围绕法院如何在引入 AI 工具时平衡利弊展开。文章重点提到对偏见、透明度和问责机制的担忧，并描述了法官与律师之间关于治理框架以及 AI 在司法决策中应扮演角色的持续辩论。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v0287x/judges_lawyers_grapple_with_the_benchs_ai/)
- **Reddit 用户寻求可免费持续记录睡眠情况的 AI 平台** — 一位曾经历多次中风和心脏病发作的 Reddit 用户，希望找到一个免费的 AI 平台，帮助创建并持续更新包含小睡在内的睡眠记录。该记录将用于 9 月 7 日与行政法官就 SSDI（社会保障残疾保险）的电话听证，该用户正在征求能够支撑这一长期数据记录需求的 AI 工具建议。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v05nln/need_a_platform_that_can_create_and_update_a/)
- **与 AI 分享想法会改变你的观点和决策吗？** — 一位 Reddit 用户讨论，当自己把想法分享给 AI 工具时，是在获得新视角，还是在削弱原本的想法。他提到，在不同工具间得到的建议常常相互矛盾，因此开始担忧自己是否被 AI “操纵”着做决策，并询问是否应减少在观点和选择上对 AI 的依赖。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1v0346g/sharing_your_ideas_to_ai/)
- **AI 正在让设计师与程序员在“作者身份与自动化”上分化** — 一篇 Reddit 帖子指出，面对 AI，设计师与程序员在态度上正出现分裂：许多设计师因作者身份与个人风格受到冲击而抗拒 AI，而程序员则更乐于接受，用它来自动化重复性工作并享受更智能的自动补全。作者自称身处动效设计与编程交叉点，观察到两方也存在重合之处，并邀请读者分享对这类分化的看法。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uzroqw/ai_for_designers_and_programmers/)
- **Linus Torvalds：Linux 并非“反 AI”，不认同就 fork 或离开** — Linus Torvalds 表示，Linux 并不是一个反 AI 项目。他敦促那些不喜欢在 Linux 中支持 AI 的人，要么 fork 项目自己另起炉灶，要么干脆离开。此言论凸显了 Linux 在开源生态中对 AI 的态度与定位。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1uyuka8/linus_torvalds_says_linux_is_not_an_antiai/)

---

*由 AI News Agent 生成 | 2026-07-18*