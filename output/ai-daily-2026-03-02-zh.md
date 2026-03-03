---
title: "AI 日报 — 2026-03-02"
description: "Stepfun开源SteptronOSS；Bench无增益，Claude领先"
lang: "zh"
pairSlug: "ai-daily-2026-03-02"
---

# AI 日报 — 2026-03-02

> 覆盖 30 条 AI 新闻

## 🔥 今日焦点

### 1. Stepfun AI 发布基础模型并开源 SteptronOSS
Stepfun AI 发布了两款基础模型：Step-3.5 Flash Base 和 Step-3.5 Flash Base-Midtrain，并开源了 SteptronOSS，用于支持可定制化工作流。此举进一步强化了其开源 / 开放科学目标，并为社区提供参考级流水线；其 SFT 数据即将发布，以扩展社区可用的工作流。 [来源-x](https://x.com/StepFun_ai/status/2028551435290554450)

### 2. BullshitBench v2 发布；模型整体无明显提升，Claude 表现突出
BullshitBench v2 在评测集中新增了 100 个问题，覆盖代码、医疗、法律、金融和物理等领域，并在 70 多个模型上进行了测试。结果再次表明模型进展并不均衡，其中 Claude 表现尤为出色，而其他模型则明显落后；该项目已开源，并提供数据浏览器以便进行更深入分析。 [来源-x](https://x.com/petergostev/status/2028492834693677377)

### 3. 五角大楼风波后，Claude 超越 ChatGPT 成为美国最热应用
据报道，在与五角大楼相关的争议事件之后，Anthropic 的 Claude 在美国应用下载量上超过了 OpenAI 的 ChatGPT，显示头部大模型平台之间的竞争进一步加剧。Axios 汇总自 Hacker News 讨论的下载趋势和报道表明，这一变化已在应用商店数据和舆论关注度中得到体现。 [来源-rss](https://www.axios.com/2026/03/01/anthropic-claude-chatgpt-app-downloads-pentagon)

## 📰 重点报道

### Embodied AI & Benchmark
- **RoboCasa365 发布 2,500 个环境与 365 项任务基准集** — 新的大规模模拟基准面向通用机器人模型：包含 2,500 个厨房环境、365 个任务、3,200+ 个物体以及 2,200+ 小时演示数据，用于支持可扩展的多任务训练和持续学习研究。 [来源-x](https://x.com/yukez/status/2028546069500699075)

### Hardware & Optimization
- **字节跳动推出 CUDA Agent 以自动生成高效内核** — CUDA Agent 可自动编写高速、优化良好的 CUDA 内核，据称在内核复杂度上优于 torch.compile 和多款顶级模型，体现出以性能为优先、结合性能分析与强化学习训练的方向。 [来源-x](https://x.com/BoWang87/status/2028599174992949508)
- **逆向工程 Apple Neural Engine 实现在本地训练神经网络** — 研究人员通过逆向工程 Apple 的 Neural Engine，宣称本地 AI 推理可在速度和能效方面优于传统方案；该项目已在 GitHub 开源，目前仍属前沿研究阶段，尚未获得 Apple 官方支持。 [来源-x](https://x.com/AmbsdOP/status/2028457255968874940)

### Edge AI & On-device
- **Qwen3.5 2B 在 iPhone 17 Pro 本地运行：Edge AI 重大突破** — 阿里巴巴的 Qwen3.5 2B 模型已在 iPhone 17 Pro 上实现端侧本地运行，通过针对 Apple Silicon 的 6-bit 优化推理路径，其性能超越体量数倍于自身的模型。 [来源-x](https://x.com/kimmonismus/status/2028602520302399701)

### AI Safety & Policy
- **OpenAI 合同会“冻结”现行法律？专家认为可能性不大** — 法律分析指出，关于通过合同“锁定”自主武器相关法律框架的说法在现实中难以成立，这一观点也引发了关于 AI 与武器管控政策的持续讨论。 [来源-x](https://x.com/jeremyphoward/status/2028556035183759719)

### Tools & Development Practices
- **AGENTS.md 提升代码智能体效率：运行更快、成本更低** — 研究显示，在 OpenAI Codex 任务中使用 AGENTS.md，可将中位运行时间缩短约 28.6%，输出 token 数减少约 16.6%，这更像是为避免最糟糕的“空转消耗”提供保护措施，而非对所有场景的一致加速。 [来源-x](https://x.com/omarsar0/status/2028464607753654711)

## ⚡ 快讯速览

- **Anthropic natsec 模型内置安全防护，与 OpenAI 公开说法相矛盾** — 有消息称，Anthropic 面向国家安全场景的模型内置了多种安全防护机制，这与 OpenAI 先前的公开表述存在冲突。 [来源-x](https://x.com/David_Kasten/status/2028552626682388542)
- **dLLM 提出简单的扩散式语言建模框架** — 一篇发布在 HuggingFace 的论文提出了一种基于扩散模型的语言建模框架 dLLM。 [来源-huggingface](https://huggingface.co/papers/2602.22661)
- **OmniGAIA：面向原生全模态 AI 智能体的基准测试** — 一套用于评测原生 omni-modal AI 智能体能力的基准 OmniGAIA 正式发布。 [来源-huggingface](https://huggingface.co/papers/2602.22897)
- **高质量环境是研究模型“阴谋行为”的关键** — 研究者指出，若要严肃研究模型的“谋划 / 欺骗”行为，高质量、精心设计的环境设置至关重要。 [来源-x](https://x.com/NeelNanda5/status/2028600215343943983)
- **K-Dense-AI 发布 Claude Scientific Skills 套件助力 AI 智能体科研** — K-Dense-AI 推出面向 AI 智能体的 Claude 科学技能工具集，用于增强其在科研任务中的表现。 [来源-github](https://github.com/K-Dense-AI/claude-scientific-skills)
- **Claude 登顶 App Store，Anthropic 支持声势高涨** — 在围绕 Anthropic 的一系列事件后，Claude 冲上 App Store 榜首，反映出用户对其的集中支持。 [来源-rss](https://9to5mac.com/2026/03/01/claude-hits-1-on-the-app-store-as-users-rally-behind-anthropics-government-standoff/)
- **根据 RAM、CPU、GPU 限制对 LLM 进行精调** — 一套工具可根据硬件资源约束（内存、CPU、GPU）对 LLM 进行配置和调优，使模型更贴合当前算力条件。 [来源-github](https://github.com/AlexsJones/llmfit)
- **AI 让初级开发者显得“没用”** — 一篇观点文章认为，AI 工具正在削弱初级开发者在团队中的价值和存在感。 [来源-rss](https://beabetterdev.com/2026/03/01/ai-is-making-junior-devs-useless/)
- **演示展示“免费、广告支持型 AI 聊天”的可能形态** — 一个概念演示展示了通过广告支持的免费 AI 聊天产品可能呈现的交互和商业模式。 [来源-rss](https://99helpers.com/tools/ad-supported-chat)
- **批评者称封闭的前沿模型“反乌托邦且令人不安”** — 多方批评声音指出，封闭式前沿 AI 模型生态在透明度和权力集中方面带来反乌托邦式的风险。 [来源-x](https://x.com/teortaxesTex/status/2028309554077843933)
- **用于自动定理证明的极简 AI 智能体取得有竞争力的证明成绩** — 一个设计极简的自动定理证明 AI 智能体在多项证明任务上获得了具有竞争力的结果。 [来源-x](https://x.com/omarsar0/status/2028591203579822112)
- **Anthropic Cowork 未预警生成 10GB 的 macOS VM 包** — 与 Claude 工作区相关的一个 macOS 虚拟机打包文件因体积高达 10GB 且缺乏预警而引发用户关注。 [来源-github](https://github.com/anthropics/claude-code/issues/22543)
- **Claude Code LSP 将 Claude 引入代码编辑器** — 通过 LSP 协议集成，Claude 现可在多种代码编辑器中使用，为开发者提供对话式编程辅助。 [来源-rss](https://karanbansal.in/blog/claude-code-lsp/)
- **AI 让“写代码”更轻松，却让“工程”更复杂** — 一篇分析文章认为，AI 工具显著降低了代码编写门槛，却在系统设计、协调和长期维护等工程层面带来新的复杂性。 [来源-rss](https://www.ivanturkovic.com/2026/02/25/ai-made-writing-code-easier-engineering-harder/)
- **切换到 Claude 而无需“从零开始”** — Claude 的记忆导入功能允许用户从其他平台迁移对话记忆，从而在切换时保留上下文而不必完全重来。 [来源-rss](https://claude.com/import-memory)
- **CS336：从零构建 LLM 的课程优于训练营式学习** — 一门名为 CS336 的课程展示了“亲手从零构建 LLM”的教学方式，相比传统编程训练营更能锻炼实战能力。 [来源-x](https://x.com/MoodiSadi/status/2028366501959331953)
- **Go 是构建 AI 智能体的最佳语言** — 一篇观点文章认为，Go 语言在并发、性能和部署上的优势，使其成为开发 AI 智能体的最佳选择。 [来源-rss](https://getbruin.com/blog/go-is-the-best-language-for-agents/)
- **Apple AI 服务器因 Apple Intelligence 使用率低而闲置** — 有报道指出，由于 Apple Intelligence 实际使用率偏低，部分 Apple AI 服务器长期闲置在仓库货架上。 [来源-rss](https://9to5mac.com/2026/03/02/some-apple-ai-servers-are-reportedly-sitting-unused-on-warehouse-shelves-due-to-low-apple-intelligence-usage/)
- **若 AI 参与写代码，会话记录是否应成为提交的一部分？** — 社区正在讨论：在版本控制中，是否应该将 AI 生成代码的会话记录与提交绑定保存。 [来源-github](https://github.com/mandel-macaque/memento)
- **为什么 XML 标签对 Claude 如此重要** — 一篇讨论文章深入分析了 Claude 对 XML 标签的广泛使用及其在结构化指令、解析与控制中的核心作用。 [来源-rss](https://glthr.com/XML-fundamental-to-Claude)

---

*由 AI News Agent 生成 | 2026-03-02*