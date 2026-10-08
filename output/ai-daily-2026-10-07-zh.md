---
title: "AI 日报 — 2026-10-07"
description: "自补偿VLA纠错、DeepSeek GPU内核支持昇腾、SWE-Race并发测试"
lang: "zh"
pairSlug: "ai-daily-2026-10-07"
---

# AI 日报 — 2026-10-07

> 覆盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. DeepSeek 的 DeepGEMM 发布高性能 GPU 内核并支持昇腾

DeepSeek 发布了 DeepGEMM，这是一个统一的张量核心内核库，打包了 FP8/FP4/BF16 GEMM、带重叠通信的融合 MoE、MQA 打分以及 HyperConnection，并采用运行时 DeepJIT 编译，安装时无需 CUDA 构建步骤。据称其性能可匹配甚至超越专家手工调优的库，而昇腾版本的推出则将部署范围拓展到 NVIDIA 之外。对 AI 基础设施团队而言，这有望降低内核工程的投入开销，并让低精度、MoE 密集型训练与推理更具可移植性。[来源-github](https://github.com/deepseek-ai/DeepGEMM)

### 2. ARC-AGI-3 在 Kaggle 上的得分从 7% 跃升至 56%

Kaggle 上的小型本地模型在 30 天内将其 ARC-AGI-3 得分从 7% 提升至 56%，如今在这一抽象基准上已超过人类平均表现。这一跃升表明推理与测试时自适应方面取得了快速进展，不过 ARC 得分对评测框架设计和算力仍然敏感。对从业者而言，这释放出一个信号：紧凑的开源模型已能在曾被视为遥不可及的任务上参与竞争。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

### 3. SWE-Race 基准用 188 个真实并发缺陷考验编码智能体

SWE-Race 引入了来自约 100 个 Python 项目已合并 PR 的 188 个真实并发缺陷，并在隔离容器中由各项目自身的测试进行评分。GLM-5.3 Flash 一次尝试即取得 85% 的得分，GPT-5.6 Luna 取得 81%，但在更困难的那一半任务上表现急剧下滑。该基准揭示出编码智能体在处理非确定性的多线程故障时仍显吃力——而这恰恰是真实世界可靠性至关重要的领域。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wyw0my/swerace_a_codingagent_benchmark_of_188_real/)

## 📰 重点报道

### 机器人与具身智能

- **自补偿 VLA 可适应机器人执行误差** — 一种部署期自适应方法让视觉-语言-动作策略利用指令动作与实际执行动作之间的残差，预先补偿执行误差，无需任务奖励或标签；压力测试覆盖了机械磨损与负载变化。[来源-huggingface](https://huggingface.co/papers/2609.37334)

### 高效 LLM 训练

- **TRACE 为 MoE 语言模型实现 FP4 强化学习训练** —  rollout 引导的量化感知训练缩小了量化训练与 rollout 执行路径之间的差距，目标是为 MoE 模型提供更廉价的 FP4 强化学习后训练。[来源-huggingface](https://huggingface.co/papers/2610.07767)

### 推荐系统

- **Yandex Music 的 Sona Transformer 取代 15 个以上推荐组件** — 在 A/B 测试中，单个 transformer 推荐器取代了 15 个以上的候选生成器、预排序器和排序器组件，可处理 8,192 个事件，并利用 History Compression 将推理成本大致减半。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/)

### 智能体评估与安全

- **CheckerBench 以静态分析检查器合成任务评测长时程智能体** — 一个包含 300 项任务的可执行基准，评估编码智能体能否端到端构建静态分析检查器，涵盖缺陷规范解读、代码仓库检查、分析器逻辑以及反馈驱动的迭代改进。[来源-huggingface](https://huggingface.co/papers/2610.07557)
- **使用工具的 AI 智能体无法将行动建立在证据之上** — 一项新研究发现，证据到行动的链条在执行之前或执行过程中就已断裂：在十种模型-框架配置中，强大的静态行动评估往往与薄弱的交互式执行并存。[来源-huggingface](https://huggingface.co/papers/2610.07753)

### 研究与数据集

- **模型从合成非语言先验中进行上下文内语言学习** — 一个 300M 参数的字节级 transformer 在随机采样的递归因果模型上训练后，完全依靠上下文就提升了六种语言的下一个字节预测能力：在权重冻结的情况下，处理一百万个字节后，每字节比特数从 8 降至 0.9–2.4。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)
- **Stockfish 在 10 亿局面上蒸馏为 ResNet/ViT；39 亿规模数据集已发布** — 一个项目利用 10 亿个 Gigafish 局面将 Stockfish 的价值函数蒸馏进 ResNet/ViT 模型，并发布了源自 Lichess 的 39 亿局面数据集；CNN+ViT 组合表现最佳。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/)

## ⚡ 快讯速览

- **跨分词器在线策略蒸馏：对齐覆盖率与监督可靠性** — 新研究考察了跨分词器蒸馏时对齐覆盖率与监督可靠性之间的权衡。[来源-huggingface](https://huggingface.co/papers/2610.08448)
- **GitHub 技能让 AI 编码智能体给出对 ADHD 友好的回答** — 一个 GitHub 技能指示编码智能体为开发者生成更简短、对 ADHD 友好的回复。[来源-github](https://github.com/ayghri/i-have-adhd)
- **REA：MCP 工具让 AI 智能体能够逆向工程软件** — 一个 MCP 工具赋予 AI 智能体用于软件分析的逆向工程能力。[来源-github](https://github.com/morluto/rea)
- **图表设计工具为 AI 编码智能体新增编辑风格图表** — 一款图表设计工具现在可生成专为 AI 编码智能体定制的编辑风格图表。[来源-github](https://github.com/cathrynlavery/diagram-design)
- **56 亿条 TikTok 视频元数据集在 Hugging Face 上发布** — 一个涵盖 56 亿条 TikTok 视频的元数据集已在 Hugging Face 上发布。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x04235/uploaded_56_billion_tiktok_videos_metadata_on/)
- **质疑 AutoResearch：智能体搜索真的算研究吗？** — 一场讨论质疑自主智能体搜索究竟算真正的科研，还是多半只是自动化探索。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wzxqze/how_much_of_autoresearch_is_research_and_how_much/)
- **RNN、Transformer 与 SSM 之间的记忆权衡** — 一项对比研究考察了 RNN、Transformer 与状态空间模型之间记忆权衡出现的不同位置。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wz71g3/transformers_vs_rnns_vs_ssms_where_does_memory/)
- **AFP-GIC：可控生成式图像压缩框架发布** — AFP-GIC 提供可控的生成式图像压缩，其率失真行为可调。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wzbe6r/afpgic_controllable_generative_image_compression_r/)
- **神经网络字体嵌入揭示视觉结构** — 用神经网络为每一种字体生成嵌入，可揭示字体之间潜在的视觉结构。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wypbnf/embedding_every_font_with_neural_networks_makes/)
- **微型 Transformer 凭合成数据零样本预测血糖** — 根据一项个人实验，一个小型 transformer 在合成数据上训练后即可零样本预测血糖。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wy99gd/i_have_trained_a_model_to_predict_my_blood_sugar/)
- **DynaBase：面向零样本动力系统的极简单参数架构** — DynaBase 提出了一种极简、可解释的单参数架构，用于零样本动力系统。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wxex8n/a_minimal_interpretable_architecture_for_zeroshot/)
- **MA-BC 汇聚多目标示范并给出样本复杂度界** — MA-BC 汇聚多目标示范，并为行为克隆给出样本复杂度界。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x0854j/split_the_differences_pool_the_rest_provably/)
- **Reddit 用户寻求从无标注网络流量中检测应用的方法** — 一位从业者询问从无标注网络流量中检测应用程序的方法。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1x08xbn/stuck_on_finding_a_approach_for_app_detection/)
- **独立开发者在遭遇 Together AI 速率限制后寻找对开发者友好的推理服务商** — 一位独立开发者在本周触及 Together AI 速率限制后，正在寻找对开发者友好的推理服务商。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wzqmka/looking_for_developerfriendly_inference_providers/)

---

*由 AI News Agent 生成 | 2026-10-07*