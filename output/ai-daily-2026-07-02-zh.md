---
title: "AI 日报 — 2026-07-02"
description: "AI时代漏洞检测；评估框架将多模态对齐人类感知；局部解码路由提升分布式模型服务。"
lang: "zh"
pairSlug: "ai-daily-2026-07-02"
---

# AI 日报 — 2026-07-02

> 涵盖 38 条 AI 新闻

## 🔥 今日焦点

### 1. Mythos AI 时代显示 AI 可大规模发现安全漏洞

Epoch AI 指出，基于 Mythos 的系统（包括 Fable）正在大规模发现软件安全漏洞。2026 年 6 月，有 21 家知名组织披露了约 1500 个高危至严重级别的 CVE，是 Claude Mythos Preview 发布前单月纪录的 3.5 倍以上。[来源-twitter](https://x.com/emollick/status/2072778376494895139)

### 2. PerceptionRubrics 将多模态评测校准到人类感知

PerceptionRubrics 提出了一套基于评估量表（rubric）的评价框架，旨在缩小基准分数与多模态模型真实脆弱性之间的差距。它将 1,038 张信息密集型图片与超过 12,000 条针对具体样本的 rubric 配对，这些 rubric 从黄金标准描述（golden captions）中，通过循环式同行评审（Circular Peer-Review）共识流程提炼而来，并蒸馏为一个双流式评估系统。[来源-huggingface](https://huggingface.co/papers/2606.28322)

### 3. ELDR：面向 PD-Disaggregated MoE 服务的专家局部感知解码路由

新型解码路由器 ELDR 针对 PD-disaggregated MoE 服务，重点考虑专家局部性而不仅仅是负载。它利用 prefill 阶段的专家激活信息，将请求路由到其已加载专家与该 batch 匹配的解码工作节点，目标是降低 MoE 模型推理延迟的波动。该方法解决了现有 MoE 部署路由器中的一个关键低效问题。[来源-huggingface](https://huggingface.co/papers/2607.00466)

## 📰 重点报道

### LLM

- **MOTHRAG：无图多跳检索框架开源** — MOTHRAG 是一个无图多跳 RAG 框架，现已开源，旨在避免离线构建知识图谱以及昂贵的重新索引。它采用稠密索引并在查询时进行编排（无图、无 GPU），支持通过“嵌入 + 追加”的方式更新，而无需完全重建。针对 HotpotQA、2WikiMultiHopQA 和 MuSiQue 的基准测试显示，其准确率和 F1 与 GraphRAG、HippoRAG、RAPTOR 等图检索系统具有相当竞争力。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ukotww/p_mothretrieval_graphfree_multihop_retrieval_via/)
- **GPT-5.6 Sol Ultra 为 Codex 推出预热** — 一则社交媒体帖子为 GPT-5.6 Sol Ultra 造势，暗示将把“太阳之力”带到 Codex。发帖人 Tibo 表示非常期待人们如何使用它，并建议大家提前保存复杂提示词，表明围绕这一新 AI 模型已开始积聚关注和热度。[来源-twitter](https://x.com/DeryaTR_/status/2072720987510931895)
- **Anthropic 的安全护栏驱动 Fable 5 大量重路由到 Opus** — 一场基准讨论显示，许多触发条件会导致 Fable 5 被重路由到 Opus，而这一行为由 Anthropic 设定的安全护栏驱动。结果是 Fable 5 的性能保持不变，但被重路由的概率明显提高。一些用户对此提出质疑，认为问题不在模型本身，而在于过于刚性的安全护栏。[来源-twitter](https://x.com/theo/status/2072777929180987485)
- **SkillHone 通过持续历史实现智能体技能持续演化** — SkillHone 提出了一种为智能体提供持续技能演化能力的“挂架”，其核心是持久化的决策历史，使后续智能体能够解读先前的修改记录、评估以及被拒绝的备选方案。它针对现有方法的局限——只保留有限运行中的最终产物而丢弃整个决策过程。通过保留这些历史，SkillHone 旨在在任务和环境不断变化的情况下，改进任务相关的操作流程、脚本和参考资料。[来源-huggingface](https://huggingface.co/papers/2606.08671)
- **AllenAI olmocr v0.4.0 为 LLM 提供 PDF 转文本 OCR 能力** — olmocr 是一个开源工具包，用于将 PDF 和基于图像的文档转换为适合 LLM 数据集的干净纯文本，并提供在线演示。它可将 PDF、PNG、JPEG 转为 Markdown，保留公式、表格、手写内容和复杂排版，同时去除页眉页脚，并保持自然的阅读顺序。该流程使用 GPU 加速，官方宣称成本低于每百万页 200 美元；v0.4.0 引入了 RL 训练，并在 olmOCR-bench 上带来约 4 分的性能提升。[来源-github](https://github.com/allenai/olmocr)

### AI 工具

- **Claude Code Artifacts 扩展至 Pro 和 Max 方案** — Claude Code 的 Artifacts 现已在 Pro 和 Max 套餐中开放，使用户可以基于会话生成实时交互页面。Claude 负责编写代码、将页面实时发布到 claude.ai，并在持续工作时进行即时更新。页面对账户私有、完全自包含，可作为私有看板或类似 PR 的演示分享；Team 和 Enterprise 套餐也可申请测试版访问。[来源-twitter](https://x.com/ClaudeDevs/status/2072770790114914317)
- **Fable xhigh 搭配 GPT-5.5 xhigh 作为规划、编码与评审组合** — 一位用户分享使用组合方案取得成功：以 Fable xhigh 作为规划/架构师，订阅版 GPT-5.5 xhigh 负责编码，再由 Fable xhigh 进行评审。他们指出，规划和评审阶段仅花费几美元，而完整端到端流程通常要 50 美元以上，并称赞 GPT-5.5 便宜且快速。不过，由于该版本刚重新发布，这种策略是否具有长期可行性仍不确定。[来源-twitter](https://x.com/mitchellh/status/2072715852944957531)

### RL

- **EBR-bench：用桌游 Earthborne Rangers 衡量即时学习能力** — Epoch AI Research 推出 EBR-bench，一个通过让 AI 反复玩 Earthborne Rangers 来衡量“即时学习”（on-the-fly learning）的基准。早期结果显示没有明显进步迹象，凸显快速适应能力的难度。该基准旨在量化模型在动态博弈环境中从错误中学习的能力。[来源-twitter](https://x.com/EpochAIResearch/status/2072714372175237255)

### LLMs

- **Anthropic 推出 Claude Design 引发与 Figma 的信任争议** — 据 The Information 报道，Anthropic 在发布 Claude Design 时，并未事先告知其当时的商业合作伙伴 Figma，Figma 创始人表示 Anthropic 并非始终坦诚；Anthropic 的首席产品官在发布前三天仍是 Figma 董事会成员。这一举动伴随 Figma 股价下跌与 Anthropic 估值飙升，引发关于竞争、数据控制与合作伙伴关系的讨论。Dario Amodei 认为，与 Anthropic 旗鼓相当的开源模型可能是危险的，这进一步放大了围绕“道德品牌”、合作伙伴访问权限以及快速纵向扩张的紧张关系。[来源-twitter](https://x.com/DeryaTR_/status/2072689189443801089)

### 开源

- **Karukan：开源神经假名—汉字输入法 IME** — Karukan 是一款面向 Linux 和 macOS 的开源日文输入法，内置神经假名-汉字转换引擎。它通过 llama.cpp 使用基于 GPT-2 的模型进行推理，实现实时、上下文感知的转换与端侧学习，并内置基于 SudachiDict 派生的系统词典、从 Mozc 移植的候选重写器、表情输入与 Slack 风格触发器。该项目模块化设计，提供 Linux 前端（fcitx5）、macOS 前端、共享引擎以及 CLI/服务端工具；首次启动会从 Hugging Face 下载模型，因此初次运行会有延迟。[来源-github](https://github.com/togatoga/karukan)
- **SentryCode：面向本地 AI 编码智能体的实时审计与蜜罐令牌** — 开源项目 SentryCode 是一款内核级审计工具，用于监控本地 AI 编码智能体。它记录文件、网络和提示（cue）活动，利用蜜罐令牌在数据泄露检测中实现零误报，能够识别隐藏通道，并提供防篡改审计日志与策略执行，全部在本地运行且无外发连接。GitHub 上提供演示二进制文件，并欢迎本地 AI 智能体用户反馈。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ul7ap2/sentrycode_realtime_auditor_honeytokens_for_ai/)

### AI 基础设施

- **CubeSandbox 为智能体提供快速安全的 AI 沙箱** — CubeSandbox 是一款为 AI 智能体构建的高性能沙箱服务，基于 RustVMM 和 KVM。它支持单节点与多节点部署，提供硬件隔离沙箱，启动时间低于 60ms，内存开销低于 5MB，同时兼容 E2B SDK。v0.4 版本新增更安全的外联、凭据保管库、带健康检查的控制面板，并沿用 v0.3.0 引入的 CubeCoW 写时复制快照引擎，以实现事件级快照和高速快照操作。[来源-github](https://github.com/TencentCloud/CubeSandbox)

### AI 安全

- **Gnosys 使用稀疏标注改进安全分类器** — Gnosys Labs 展示了一种自治模型工程方法，在真实标签稀缺的情况下改进提示词与分类器。在 ToxicChat 安全基准上，在固定 5% 误报率下，该方法在两个留出测试轮次中都优于初始分类器和 GEPA。说明中也对结果与局限进行了讨论。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ul3ohk/making_optimization_work_when_labels_are_scarce_r/)

### 多模态

- **ECCV 2026 的 MARS2 研讨会：多模态视频推理** — ECCV 2026 上的 MARS2 研讨会（多模态推理竞赛）聚焦多模态与测试时（慢速）推理，强调视频与广告理解等真实世界任务。它汇集了来自 MIT、剑桥、牛津、CMU、南洋理工的研究者，并列出 Tec-Do 与 Minimax 为组织方/赞助方。帖子对其实验评估设置的实际性以及该基准对日常开发的帮助价值提出质疑。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1uka1r6/anyone_looking_into_the_new_mars2/)

## ⚡ 快讯速览

- **更新版 AI 术语词典用讽刺方式解构行话** — 一条聚焦 AI 的 Twitter 长帖发布了更新版 AI 词典，以幽默方式重新定义大家熟悉的术语。列表涵盖 The bitter lesson、AGI、RL、持续学习以及与 transformer 相关的概念，并配以讽刺式解释，通过调侃术语用法来影射 AI 研究文化。[来源-twitter](https://x.com/ziv_ravid/status/2072535130908897778)
- **TurboServe 支持高效可扩展的流式视频生成** — 流式视频生成被描述为一种新型推理工作负载，其特点是会话时间长，按片段持续生成视频。它需要在活跃与空闲阶段都保持会话状态，并在严格延迟目标下交付视频片段。在多用户、多 GPU 环境中，两个关键挑战是会话时长差异巨大以及必须反复为正在进行的会话进行调度。[来源-huggingface](https://huggingface.co/papers/2606.19271)
- **GitHub 数据集：多语言健身动作元数据与后端脚手架** — 仓库 hasaneyldrm/exercises-dataset 提供了结构化的健身动作数据集，包含名称、类别、目标肌群、器械、指导说明以及媒体引用等元数据。它还提供开发者配置向导，为 1,324 个动作在六种语言（英语、西班牙语、意大利语、土耳其语、俄语、中文）生成后端脚手架，并说明由于版权原因不包含动作媒体文件本身。[来源-github](https://github.com/hasaneyldrm/exercises-dataset)
- **ML/CV 顶会中 Best Paper 与 Oral/Highlight 是如何评选的？** — 帖子询问在顶级 ML/CV 会议上，论文如何被选为 Best Paper、Oral 或 Highlight。问题包括：由谁来挑选候选（AC、SAC、程序主席、奖项委员会或独立小组）、是否使用 camera-ready 版本，以及决策是否依赖审稿分数，还是更强调新颖性和讨论情况。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ulnstb/how_papers_are_selected_for_best_paper_oral_or/)
- **基于语义相似与时间片的 1100 万论文地图** — 研究者构建了一个免费的可视化地图 The Global Research Space，聚合了 OpenAlex 与 arXiv 上最新的 1100 万篇论文。论文通过 SPECTER 2 对标题与摘要进行编码，再用 UMAP 降至二维，并在高密度峰值周围的 Voronoi 区域内进行标签标注。该工具支持关键词与语义搜索，提供机构、作者与主题的分析功能，并配有时间滑块与每日自动抓取，以保持最新覆盖。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ujn3u5/a_map_of_the_latest_11_million_papers_split_by/)
- **系统级提示注入防护：区分指令与数据通道** — 文章提出一种面向使用工具的 LLM 的中间件式提示注入缓解方案，引入 Sentinel Gateway 严格区分指令（可信）和数据（不可信）通道。系统为所有智能体动作强制使用签名化、作用域限定的运行时授权 token，将“观察”与“执行”解耦。实现上采用 FastAPI 中间件与基于 token 的执行机制，并提供 Streamlit 界面用于检查与审计日志。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ukgwk1/a_systemlevel_approach_to_prompt_injection/)
- **改进基于 APTOS 2019 的 5 类糖网病模型** — 一名毕业年学生基于 APTOS 2019 训练了一个 5 类分类器，并用 Flask 搭建糖尿病视网膜病变检测应用。该模型在各类别上的预测不稳定，一些样本被误分类，有时对错误结果仍给出高置信度，尤其是在使用非 APTOS 图像时。为改进模型，他们尝试了 ResNet50（在 APTOS 上训练）和 ResNet152 等预训练模型。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ujztdd/how_to_improve_a_5class_diabetic_retinopathy/)
- **明日将采访 Hermes 联合创始人 karan4d** — 一场与 NousResearch 的 Hermes 联合创始人 karan4d 的访谈已经安排。主持人邀请观众提议话题，提到此前已经讨论过环境搭建、集成与基础定时任务，并询问还有哪些内容值得深入。帖子中还轻松调侃了一张“图表其实就是一条竖直线”。[来源-twitter](https://x.com/petergyang/status/2072737599362621866)
- **急聘：AI 推理方向的强力产品经理** — 一则 Twitter 帖子宣布紧急招聘一位高能力、专注 AI 推理的产品经理。帖子强调招聘此类 AI 推理领导角色的紧迫性，反映了业界对 AI 推理产品领导力的持续需求。[来源-twitter](https://x.com/romanchernin/status/2072571100517519612)
- **开源驱动“无限主权智能”** — 推文宣称开源等同于“无限主权智能”。其观点是开源 AI 能让用户或国家拥有主权级能力，体现了对开源 AI 在民主化能力方面潜力的乐观态度。[来源-twitter](https://x.com/Jason/status/2072778368530198973)
- **强化 ML 数学基础的书单与资源** — 一位 ML 博士生征求资源推荐，希望巩固线性代数、概率论与泛函分析基础。他提到《Linear Algebra Done Right》、A Primer on RKHS，并考虑重读 PRML，同时计划进一步学习 Pat Kidger 的相关工作。目标是在毕业前对基础知识进行系统复盘。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ulmy9g/booksresources_to_improve_mathematical/)
- **从微分几何视角审视 Hamiltonian Neural Networks** — 一篇文章从微分几何而非传统“损失函数中心”视角探讨 Hamiltonian Neural Networks（HNN）。作者强调其与 Noether 定理之间的联系，突出物理引导神经网络中的对称性与守恒定律，并通过大量数学推导与可视化说明提供更深入的见解。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ukzdnj/hamiltonian_neural_networks_from_a_differential/)
- **用风格迁移改进机翻网文：忠实度 vs 流畅度** — 研究者讨论使用风格迁移清理机器翻译的网络小说，目标是生成既像专业写作、又忠实原文的文本。由于缺乏干净的平行语料，他们考虑基于 STRAP 的无监督方法，包括将任务视作释义、构造伪平行数据以及训练特定风格的逆向模型。主要难点在于保持跨数千页文本的长程上下文一致性。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ulrdw9/improving_machinetranslated_novels_via_style/)
- **有人尝试把 Fast Byte Latent Transformers 与 Mamba 结合吗？** — 一位 Reddit 用户提到论文 arXiv:2412.09871v1，询问是否可以用 Mamba 模型替换其中的熵模型 transformer，以降低计算复杂度至 O(n)。帖子邀请社区讨论该方案的可行性以及在方法上可能需要做出的调整。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ulngy8/has_anyone_tried_this_approach_with_fast_byte/)
- **BMVC 2026 评审讨论串明日开启** — 帖子宣布 BMVC 2026 评审结果将于明日发布，并创建了一个专门的主贴供社区讨论。帖子提到作者身份，并附上相关 Reddit 讨论链接。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ulnp4d/bmvc_2026_review_discussion_thread_d/)
- **如何描述“更准且更小”的高效模型** — 一位在线发帖者询问：如何描述一个在参数量与 FLOPs 更少的情况下反而获得更高准确率的模型。讨论涉及基准测试、模型压缩，以及在交流效率提升时应使用的表述方式。这是来自一位 AI 社区新人的澄清请求。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ukv9x5/how_to_describe_a_model_that_has_higher_accuracy/)
- **在围绕 Fable 的批评声中，Anthropic 模型被点赞** — 一名 X 用户自称是 Anthropic 的“头号黑粉”，却表示该模型确实很好用。他批评针对“Fable”的一些观点很愚蠢，认为这些批评转移了 Anthropic 应该真正解决的问题。该帖在为 Anthropic 工作点赞的同时，也将矛头指向其反对者。[来源-twitter](https://x.com/theo/status/2072777433997316436)
- **政府持股 AI 公司应基于自愿而非税收** — 帖子讨论政府可能入股 AI 公司的传闻，并坚持两个条件：一是出资必须是自愿而非强制税收；二是资金应进入公民所有的账户，而不是政府的“黑箱基金”。作者强调政府应只负责协调，而不应直接拥有这部分资产。[来源-twitter](https://x.com/altcap/status/2072784499943895477)
- **T3 社区今日在 OpenAI 展台举办线下见面会** — T3 社区宣布将在今天下午 2 点于 AI Engineer 会场进行见面会，计划在 OpenAI 展台集合。参会者被邀请前往 OpenAI 展台进行交流与社交。[来源-twitter](https://x.com/theo/status/2072751781952762139)
- **粉丝表白 Fable 5 与 Anthropic** — 在 Twitter 上，一位用户表达了对 Fable 5 和 Anthropic 的喜爱。帖子将对一款电子游戏的热情与对一家 AI 安全公司的欣赏糅合在一起，体现了跨领域兴趣在单条社交动态中的交织。[来源-twitter](https://x.com/dylan522p/status/2072741962214707311)
- **ACL ARR 2026 年 5 月轮评审结果何时公布？** — 一位 Reddit 用户询问 ACL ARR 2026 年 5 月轮的评审结果究竟会在 7 月 2 日还是 7 月 7 日发布，以及 Main 和 Findings 两个 track 的录用门槛如何。帖子表明作者对 ACL 投稿结果机制还不熟悉，需要社区指点。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ukud96/acl_arr_may_2026d/)

---

*由 AI News Agent 生成 | 2026-07-02*