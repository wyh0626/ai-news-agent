---
title: "AI 日报 — 2026-09-29"
description: "Qwen3-VL税表胜GPT-5.6但印度日期弱；新视觉骨干与代码智能体RL进展。"
lang: "zh"
pairSlug: "ai-daily-2026-09-29"
---

# AI 日报 — 2026-09-29

> 覆盖 19 条 AI 新闻

## 🔥 今日焦点

### 1. Qwen3-VL 8B 在税表上优于 GPT-5.6，但在印度日期上表现不佳

一项 Reddit 基准测试在 137 份杂乱文档上，将在笔记本电脑上量化的 Qwen3-VL 8B Instruct 与 Claude Opus 5.5、Sonnet 5 和 GPT-5.6 Terra 进行了比较。Qwen 得分 59%，而 GPT-5.6 Terra 为 57%，尤其在 W-2 税表上击败 GPT-5.6，但在印度 dd-mm-yyyy 日期格式上失败。这一结果凸显出小型开放权重 VLM 如何在狭窄的文档任务上变得有竞争力，同时在特定区域格式上仍然脆弱。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wsbqni/qwen3vl_8b_on_a_laptop_vs_opus_55_sonnet_5_gpt56/)

### 2. 无编码器多模态预训练的缩放定律

本文系统比较了无编码器与基于编码器的多模态大语言模型之间的缩放定律。研究发现，移除视觉编码器会改变计算最优分配，为直接从原始像素学习视觉表示的权衡提供了洞见。这项工作有助于刻画无编码器 MLLM 能扩展到何种程度，以及基于编码器的流程在哪些方面仍保有优势。[来源-huggingface](https://huggingface.co/papers/2609.35457)

### 3. 交错 RL 使统一多模态模型具备原生反思能力

本文提出交错强化学习，通过诊断-修正-渲染循环训练统一多模态模型修复自身生成的图像。它认为反思文本与图像生成必须联合学习，因为 SFT 冷启动无法找到高成功率的修复路径，而朴素 RL 也不足够。若得到验证，这指向多模态模型能够原生自校正生成，而无需单独的评判器或修复模块。[来源-huggingface](https://huggingface.co/papers/2609.35767)

## 📰 重点报道

### 计算机视觉与架构

- **VisionHOPE 提出用于自适应学习的自修改视觉骨干网络** — VisionHOPE 将视觉骨干网络视为自修改学习系统，将 CNNs、ViTs、SSMs 和测试时训练扩展到针对每个输入的自适应计算。[来源-huggingface](https://huggingface.co/papers/2609.33325)

### 强化学习、智能体与机器人

- **GAG：用于代码智能体 RL 的分组评分与优势重分配** — GAG 用分组式智能体评分和优势重分配取代二元测试奖励，为 GRPO 提供偏向干净、有针对性的代码修改而非越界编辑的信号。[来源-huggingface](https://huggingface.co/papers/2609.32577)
- **递归 Harness 蒸馏提升跨智能体的机器人操作** — 递归 Harness 蒸馏从强智能体积累经验，帮助视觉-语言-动作模型在操作过程中诊断失败并进行适应。[来源-huggingface](https://huggingface.co/papers/2609.33378)

### 高效机器学习与优化

- **CoWindow 与 MassAlloc Attention：高效长上下文注意力方法** — CoWA 通过互补窗口将远距离上下文分布到 KV 头中，而 MALA 使用 softmax 统计量，在 128K token 时跳过低贡献的评分后计算。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wt1gbk/cowindow_and_massalloc_attention_collective/)
- **具有自适应表示的函数梯度下降被 NeurIPS 接收** — 这篇 NeurIPS 论文形式化了无限维函数梯度的近似方案，据报道可收敛到全局极小值点，并相较神经网络具有最高一个数量级的优势。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wsejb7/functional_gradient_descent_with_adaptive/)

### 开源与教育

- **开源 AI 工程课程以 EPUB/PDF 书籍形式发布 523 节课** — 这个 MIT 许可的 AI Engineering from Scratch 课程新增六卷 EPUB/PDF、八种语言界面、经过 CI 测试的课程，以及一个编码智能体学习技能。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ws6e9p/free_opensource_ai_engineering_course_where_you/)
- **免费开源书籍：让 ML 模型变快，从硅到智能体** — 一本新书涵盖 roofline 分析、内核、编译器、量化、剪枝、端侧 LLM、机器人、性能分析、服务与智能体，强调在优化前识别瓶颈。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wt6ns4/i_wrote_a_free_opensource_book_on_making_ml/)

## ⚡ 快讯速览

- **开源确定性 Clash Royale 模拟器，用于带 PPO 和前瞻的 RL** — 一个确定性、开源的 Clash Royale 环境支持使用 PPO 和前瞻规划进行可复现的 RL 实验。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wrj0t3/clashroyaleai_an_opensource_deterministic_clash/)
- **OpenTrainDNN：基于浏览器的实时神经网络训练可视化工具** — OpenTrainDNN 在浏览器中实时可视化神经网络训练。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ws14qi/opentraindnn_a_browserbased_realtime_neural/)
- **研究者批评 AI 领域对大规模算力的痴迷** — 一位研究者认为，该领域对大规模算力的执迷正在挤占其他有价值的研究方向。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wtmcdo/some_thoughts_about_the_compute_obsession_no_one/)
- **算力有限：重跑 CVPR 实验还是专注写作？** — 一场讨论询问，有限的算力最好用于重跑 CVPR 实验，还是打磨论文写作。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wt9w3s/limited_compute_targeting_cvpr_rerun_experiments/)
- **Reddit 帖子质疑 NAS、对抗 ML 与伦理的相关性** — 一篇社区帖子讨论 NAS、对抗 ML 和伦理是否仍是相关子领域，还是已被过度炒作。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wrqoxp/are_there_machine_learning_subfields_that_are/)
- **为什么不在 Softmax 前去掉一个 Logit？ML 讨论** — 一场讨论探讨在 softmax 前去掉一个 logit 是无害的冗余，还是会影响模型行为。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wt1mk0/why_not_just_have_one_less_feature_before_softmax/)
- **用户寻求使用 LLM 进行文本聚类的研究论文** — 一位用户请求提供关于使用 LLM 进行文本聚类的研究论文。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ws6g1p/are_there_any_good_research_papers_around_text/)
- **数据工程师寻求建议：将工业界 ML 项目转化为论文发表** — 一位数据工程师询问如何将工业界 ML 项目转化为学术发表。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1ws7z0e/how_can_i_turn_an_industry_ml_project_into_a/)
- **BA CS 研究者获得 NeurIPS Poster 接收，询问亚特兰大相关事宜** — 一位 BA 计算机科学研究者庆祝其 NeurIPS Poster 被接收，并询问关于亚特兰大的建议。[来源-reddit](https://www.reddit.com/r/MachineLearning/comments/1wsyu8m/ba_computer_science_but_fell_in_love_with_machine/)

---

*由 AI News Agent 生成 | 2026-09-29*