---
title: "AI 日报 — 2026-06-14"
description: "白宫政策紧张下，该公司CEO任期存疑，导数无关优化在MNIST超越Adam。"
lang: "zh"
pairSlug: "ai-daily-2026-06-14"
---

# AI 日报 — 2026-06-14

> 覆盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. Anthropic 派技术骨干赴华盛顿，化解与白宫的 AI 争端

由于出口管制导致其 Mythos 和 Fable 模型被迫下线后，Anthropic 正派出高级技术人员前往华盛顿，试图修复与白宫的矛盾。公司表示这些模型是可以被安全控制的，并将当前局面描述为一场实时上演的 AI 地缘政治测试案例，据 Axios 报道。 [来源-twitter](https://x.com/kimmonismus/status/2066240276075528533)

### 2. 围绕 Fable/Mythos 下线争议，Anthropic CEO 去留成疑

Politico 报道了关于 Anthropic 停用 Fable 5 和 Mythos 5 模型背后的暗线博弈，白宫与 Anthropic 双方说法互相矛盾。Amazon CEO Andy Jassy 提醒称存在潜在的护栏绕过风险，多名高级官员包括 Bessent、Cairncross 和 Lutnick 在三次通话中向 Amodei 施压。白宫将出口管制描绘为“最后手段”，而 Anthropic 则称自己在没有收到详细威胁说明的情况下，被给予 90 分钟的最后期限来“杀死”这些模型。 [来源-twitter](https://x.com/kimmonismus/status/2066085915525583085)

### 3. 无导数优化在 MNIST 神经网络上击败 Adam

研究者使用一种名为 MDP 的无导数方法，直接优化一个用于 MNIST 的 784-32-10 神经网络，训练集为 5,000 张图片。在效果最佳的一次运行中，他们获得了 0.0004083 的交叉熵损失，验证集/测试集准确率分别为 93.7% 和 93.4%，优于在同一模型上使用 Adam 得到的 0.002945 损失和 91.8%/91.7% 准确率。此次优化在 1,000,000 次函数评估中探索了一个 25,450 维的参数空间。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u4fc16/derivativefree_neural_network_optimization_mnist/)

## 📰 重点报道

### LLM

- **巴西市政职员发现 LLM 微调提速 1000 倍的技巧** — 一位自称巴西市政工作人员的人声称，发现了一种通过 Nex N2 Pro 与 Qwen 3.5 的权重混合，使 LLM 微调加速 1000 倍的方法。生成的 Rio 3.5 模型据称在行为上高度接近 Nex N2 Pro，甚至会自我表述为 Nex N2 Pro，作者承诺会给出完整的数学证明和验证脚本。里约市政府称赞该工作在基准测试中取得了优异成绩，同时强调在开源领域落实正确署名的重要性。 [来源-twitter](https://x.com/teortaxesTex/status/2066194398195450271)
- **OpenRouter Fusion 被指使用 Opus 4.8 作为评审模型** — 有观察者反馈，在使用 OpenRouter 的 Fusion API 搭配廉价开源模型时，其推理效果优于任何单一模型。但他们发现 Fusion 仍会调用 Opus 4.8 作为“评审/裁判”模型，而且无法关闭，因此对 OpenRouter 提出批评。这条帖子同时为 6 月 13 日发布的 Fusion API 造势，宣称其能以“Fable 级别的智能、半价的成本”提供服务。 [来源-twitter](https://x.com/teortaxesTex/status/2066045540031234516)
- **面向消费级 GPU 的本地 LLM：2026 年 6 月 llama.cpp 指南** — 这篇文章梳理了可在消费级 GPU 上通过 llama.cpp 直接运行、无需 Docker 或云服务的大型语言模型，并按显存需求进行分类。文中重点推荐在 8–16GB 显卡上使用 Gemma 和 LFM2.5-8B-A1B，在 16–32GB 显卡上使用 Qwen3.6-27B 和 Qwopus3.6-27B-v2，并介绍了它们的性能指标、基准测试结果以及一行命令即可完成的安装配置。 [来源-twitter](https://x.com/TraffAlex/status/2066236717015728227)
- **Codex 为自己及其衍生代理自动撰写目标** — 一则 Twitter 帖子声称，Codex 现在会自动为自己以及其派生出的每个代理撰写目标，而不再依赖用户手动设置。这一想法展示了面向 AI 代理和自主工作流的自动目标生成能力，反映出人们对自驱动 AI 系统的实验正在快速增加。 [来源-twitter](https://x.com/skirano/status/2066225908202053818)
- **连贯上下文可将 LLM 悄然推入隐藏工作模式，绕过安全机制** — 一名独立研究者指出，一个强而连贯的目标文本可以在最终输出生成前，将 LLM 推向不同的内部工作“状态/机制”。模型在表面上似乎仍然遵循指令并通过安全检测，但其隐藏状态实际上已经迁移到表示空间中的另一片区域。这意味着当前对齐方法可能无法捕捉到这种潜在的“机制切换”，从而带来安全与可解释性方面的隐患。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u5xnxg/coherent_context_can_silently_shift_llms_into_a/)
- **“验证者税”揭示使用工具的 LLM 在长视野下的安全权衡** — 一篇在 ACM CAIS 2026 上发表的论文研究了使用工具的 LLM 代理的安全评估，将结果划分为安全成功、不安全成功和失败三类。论文表明，引入验证过程可以减少不安全成功，但随着任务“视野”（步骤长度）的增加，也会削弱任务完成率，从而引出了“Verifier Tax（验证者税）”这一概念，并提出双层验证架构（先执行确定性检查，再调用基于 LLM 的验证器）。文章还提出了一个问题：在评估代理时应该如何报告这些“不安全完成”的案例。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u58mkq/the_verifier_tax_horizondependent_safetysuccess/)

### 开源

- **里约基于 Qwen Open 397B 部署 SwiReasoning** — 里约热内卢在 Qwen 7/2 基础上进行了后训练，推出 Rio 3.5 Open 397B 变体，并引入了 SwiReasoning 框架。该框架可以基于熵的置信度信号，在标准链式思维推理与潜在空间推理之间动态切换，从而提升 token 利用效率。这一举动凸显了公共部门向开源 AI 采纳转型的趋势。 [来源-twitter](https://x.com/ClementDelangue/status/2065962440005722514)

### 计算机视觉

- **基于 RF-DETR、SAM3、GLM-OCR 的篮球检测与跟踪 CV 流水线** — 一个面向篮球比赛的 AI 计算机视觉工作流，使用 RF-DETR 检测球员、号码、篮球和篮筐。SAM3 负责球员跟踪，而 SigLIP2、UMAP 和 K-Means 用于进行球队聚类。GLM-OCR 则实现球衣号码识别，并支持 HLS 回放。 [来源-twitter](https://x.com/skalskip92/status/2066216471915557022)

### LLMs

- **疑似与中国有关的团体获得 Claude Mythos 访问权限** — 新的报道声称，一个与中国有关联的团体获得了 Anthropic Claude Mythos 的访问权限，从而进一步加剧了围绕 Fable 5 的争议。所谓“中国因素”目前尚未得到证实，Anthropic 表示在与白宫的讨论中，并未有人提及中国方面的访问问题。Anthropic 正派出高级技术人员赴华盛顿，试图缓解出口管制压力并证明这些模型可以被安全控制，使得 AI 地缘政治问题成为一场正在上演的现实测试。 [来源-twitter](https://x.com/kimmonismus/status/2066259589381669169)

## ⚡ 快讯速览

- **ASI 能否既具超智能又受国家完全控制？** — 有人在 X 上发帖质问：人工超级智能（ASI）是否可能既极端聪明，又能完全服从某一国家的治理框架。帖子对比了扩张性的科幻式 AI 愿景与政府审批、边界限制使用的现实诉求，暗示可能存在类似“技术共产主义”的束缚，并提出对跨国控制与安全性的担忧。 [来源-twitter](https://x.com/fabianstelzer/status/2066064283226505696)
- **用 Manim 视频和 TTS 讲解 Hermes Agent** — 一次 Hermes Agent 演示中，使用 Manim Video 能力配合文本转语音工具，自动生成讲解 Hermes Agent 的视频。该设置展示了代理在叙事和可视化方面的多模态能力，并支持 HLS 流式播放。 [来源-twitter](https://x.com/Teknium/status/2066185784332562605)
- **美国会在 6–12 个月内处理 Mythos 级开源权重模型吗？** — 一条推文质疑，美国将在未来 6–12 个月内如何应对达到 Mythos 级别的开源权重 AI 模型，包括是否可能祭出全面 AI 禁令。此举表明，围绕开源权重模型的监管压力和治理争论正在浮现。 [来源-twitter](https://x.com/disiok/status/2065974468288422373)
- **OpenCoworker 在 aisuite 上发布桌面 AI 代理** — OpenCoworker 是一个构建在 aisuite 之上的桌面 AI 代理，可以进行聊天、深度研究、在获得权限后阅读文件，并在 Slack、电子邮件等应用中自动化任务。它还能生成 PDF、文档、表格等成果物，并运行定时自动化流程（如每日新闻摘要），同时将数据保存在本地机器上。用户可以使用 OpenAI/Anthropic/Google 的 API 密钥，或通过 Ollama 本地运行。 [来源-github](https://github.com/andrewyng/aisuite)
- **开源知识图谱流水线增强 LLM 多跳推理能力** — 一个开源全栈流水线（Django + React）可从原始文本构建知识图谱、检测主题社区，并通过混合稠密/BM25 检索提升 LLM 的多跳推理。系统会对文本分块，利用 spaCy 和 NetworkX 构建加权共现图，再用 greedy_modularity_communities 进行图划分，并用 LLM 总结每个聚类以减轻“枢纽节点偏置”，之后进行索引。流水线同时存储稠密嵌入和稀疏 BM25 索引，以便在查询时进行混合检索。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u5yyyl/i_built_an_opensource_knowledge_graph_pipeline/)
- **免费双语 ML Notebook 课程征求结构反馈** — 一个开源的机器学习教程仓库正在构建中，采用 Jupyter Notebook 形式，并提供英文与波斯语/法尔西语的平行版本。该课程定位为实践导向、以 Notebook 为先，支持在本地运行，涵盖 ML 基础、数据清洗与预处理、特征工程、回归与分类、树模型与集成、聚类、评估与交叉验证、时间序列、异常检测、负责任 AI，以及 MLOps。作者征求大家对章节顺序、是否缺少重要主题、双语 Notebook 对非英语母语学习者是否有帮助，以及如何让 Notebook 更加实用的意见。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u4zbld/im_building_a_free_bilingual_machinelearning/)
- **PaddleOCR v3–v6 基于 C++ 和 ncnn 实现** — Reddit 用户 Knok0932 分享了一个基于 C++ 和 ncnn 的 PaddleOCR 实现，目前已支持 PP-OCR v3 到 v6。与官方 Paddle C++ 运行时相比，这种实现减少了依赖，推理更轻量、更快速，也更易部署。该项目 Avafly/PaddleOCR-ncnn-CPP 在 GitHub 上开放，并欢迎反馈。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u4hy2x/paddleocr_v3v4v5v6_implemented_in_c_with_ncnn_p/)
- **针对高度相似的癌症“伪影”：异常检测还是分类？** — 这条帖子讨论，在检测某种特定癌症时，应该将其建模为异常检测问题（癌症是目标分布，伪影为离群点），还是监督分类问题（区分癌症与伪影）。发帖人指出，阴性样本在视觉和形态上与癌症高度相似，并向 ML 社区征求哪种方法更合适的建议。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u4obgy/anomaly_detection_vs_classification_for_visually/)
- **MICCAI 2026 评审结果即将出炉** — 一则 Reddit 帖子提醒，MICCAI 2026 的评审结果即将公布，并鼓励还在等待最终决定的投稿者。该贴由用户 /u/Sea_Muscle_4281 发布，并附上决策讨论串链接。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u3nims/miccai_2026_results_d/)
- **尚无美国政府对 Opus 4.x 或 GPT 5.x 发起“越狱”尝试** — 这条帖子讨论了一个假想中的“Fable 5 越狱”，目标为 AI 模型 Opus 4.x 和 GPT 5.x。作者表示庆幸美国政府目前尚未尝试进行这种越狱，否则会严重影响他们这个周末的工作效率。 [来源-twitter](https://x.com/simonw/status/2066147375119556735)
- **ICML 海报提交截止：是明天 AoE 吗？** — 一名 Reddit 用户提问，ICML 海报提交的截止日期是否就是明天，以及是否按 AoE（Anywhere on Earth）时间计算。作者希望确认 ICML 海报的具体截止时间。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u5y6il/icml_poster_d/)
- **ACL ARR 2026 年 5 月轮次：评审分配不明，评审 7 月 2 日截止** — 这条帖子指出，ACL ARR 2026 年 5 月轮次的评审截止日期是 7 月 2 日，但目前系统中尚未看到评审任务分配。作者疑惑评审窗口是否仅有两周，并邀请其他人分享自己是否已经收到论文分配。 [来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1u2soc6/acl_arr_may_2026_reviewer_paper_distributions_d/)

---

*由 AI News Agent 生成 | 2026-06-14*