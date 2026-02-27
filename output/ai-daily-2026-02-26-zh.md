# AI 日报 — 2026-02-26

> 覆盖 29 条 AI 新闻

## 🔥 今日焦点

### 1. Google 的 Nano Banana 2 首次亮相，成为实时多模态图像模型

Google 公布 Nano Banana 2，这是其基于 Gemini 的世界理解能力并由实时网络数据驱动的最新图像模型。它可以以高保真度反映实时条件，Window Seat 演示展示了在实时天气下以 2K/4K 分辨率呈现更准确的视图。Nano Banana 2 将作为 Geminiapp 与 Search 在全球 141 个国家的默认版本推出，并在 Flow 中提供预览，且在 Google AI Studio 与 Vertex AI 中有预览，并在 Antigravity 上可用。[来源-twitter](https://x.com/sundarpichai/status/2027057726170509724)

### 2. 五角大楼对 Anthropic 的无限制 AI 使用提出最终报价

据称美国五角大楼已提出最终报价，敦促 Anthropic 允许其 AI 能力用于无限制的军事用途，截止日期在逼近。据称 Anthropic 拒绝将其 AI 用于美国监控以及致命军事任务，尽管其最近赢得了一份价值 2 亿美元的政府合同。这一局势凸显了 AI 战争与治理领域的高风险辩论。[来源-twitter](https://x.com/KobeissiLetter/status/2027031529042411581)

### 3. Apple 推出用于在 Mac 上本地化语言模型的 Python SDK

Apple 发布了一个 Python SDK，使得通过 Foundation Models 框架在 Mac 上访问本地语言模型成为可能。该仓库 apple/python-apple-fm-sdk 提供用于与本地模型交互的 Python 绑定。这使本地 AI 推理不再依赖云端，并扩展了开发者在 Apple 硬件上的工具链。[来源-twitter](https://x.com/rxwei/status/2026838142557499756)

## 📰 重点报道

### 大语言模型

- **LFM2-24B-A2B 在 Strix Halo 上运行速度提升约 2 倍** — 一篇 Reddit 帖子声称在 Strix Halo 上配合 ROCm 与 Lemonade v9.4.0 时，LFM2-24B-A2B 的速度大约是 gpt-oss-20b 的两倍。作者对潜在应用表示乐观，并邀请他人分享其用例。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfid0q/lfm224ba2b_is_crazy_fast_on_strix_halo/)

- **带 KV 绑定的测试时训练其实是线性注意力** — 最新分析认为带有 key-value 绑定的测试时训练并非单纯记忆。研究显示，许多 TTT 架构可以重新表述为学习到的线性注意力，将在线元学习重新框定为线性注意力过程。该工作重访了 TTT 的表述，帮助解释此前令人困惑的模型行为。 [来源-huggingface](https://huggingface.co/papers/2602.21204)

- **学习 Claude Code：从零到一的 Nano Claude Code‑like Agent** — 来自 shareAI-lab 的开源项目，概述了一个基于最小循环结构的 Claude Code‑like Agent。它介绍了 AGENT PATTERN 与 12 个递进会话，每个会话增加一个机制，使代理从简单循环逐步演化为独立自治执行。代码仓库托管在 GitHub 上。 [来源-github](https://github.com/shareAI-lab/learn-claude-code)

- **Plano：面向代理应用的 AI 原生代理与数据平面** — Plano 是一个 AI 原生代理与数据平面，负责将路由、编排、信号、安全过滤与 LLM 路由从代理应用中解耦。它旨在让开发者摆脱脆弱的框架抽象，跨语言和 AI 框架加速生产交付，同时为代理工作流提供集中治理与可观测性。 [来源-github](https://github.com/katanemo/plano)

- **NVIDIA 推出 Megatron-LM Core，用于大规模 Transformer 训练** — NVIDIA 的 Megatron-LM 项目推出两大组件：Megatron-LM，面向研究的参考实现，配有预配置训练脚本；Megatron Core，是一个针对 GPU 的 Transformer 架构基础组件库，具备高级并行性与混合精度支持。Megatron Core 支持 TP、PP、DP、EP 与 CP，以及 FP16、BF16、FP8、FP4，便于构建自定义训练流程；Megatron-LM 提供现成可运行的配置以便快速试验。套件还包括 Megatron Bridge，用于 Hugging Face ↔ Megatron 检查点的双向转换，快速上手可通过 pip 安装。 [来源-github](https://github.com/NVIDIA/Megatron-LM)

- **Qwen3.5-35B-A3B 的 Q4 量化对比** — 对 Qwen3.5-35B-A3B 进行了一系列 Q4 量化评测，评估对 BF16 基线的保真度，使用多种量化器与配方。研究报告给出 KL 散度与困惑度，用以衡量信息损失与模型置信度，旨在指导数据驱动的文件选择，而非凭直觉。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfds1h/qwen3535ba3b_q4_quantization_comparison/)

- **从零开始训练一个 144M 参数的脉冲神经网络用于文本生成** — 在 FineWeb-Edu 上，用约 10 美元的成本、租用 NVIDIA RTX A5000 的条件，从零开始训练了一个 144M 参数的脉冲神经网络语言模型，未使用变换器教师或蒸馏。该模型天然实现 97-98% 的推理稀疏度，在相同提示下展现出比 GPT-2 Small 更强的主题连贯性。脉冲速率分析显示可解释的处理，Block 4 活跃度最高（9.8%），Block 0 负责过滤噪声（0.6%），并具备在线学习能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfddpi/training_a_144m_spiking_neural_network_for_text/)

- **DualPath 打破了代理型 LLM 推理中的存储带宽瓶颈** — 来自北京大学、清华大学与 DeepSeek-AI 的联合团队发表论文，提出 DualPath 推理系统，旨在解决代理型 LLM 工作负载中的 KV-Cache 存储 I/O 带宽瓶颈，通过优化存储访问模式与数据流来提升推理吞吐量。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rf740o/deepseek_released_new_paper_dualpath_breaking_the/)

### 硬件

- **Prime Intellect 推出搭载 H100 GPU 的 AI 计算基础设施** — Prime Intellect 发布了采用 H100 GPU、InfiniBand、7×24 小时支持的前沿 AI 计算基础设施，并推广将 15+ 云提供商进行对比以选择最佳 GPU。此外，推文作者 Johannes Hagemann、以及 Hieu Pham 因工作压力离开 OpenAI 的消息也被提及。 [来源-twitter](https://x.com/johannes_hage/status/2026900883896938978)

### 金融科技中的 AI

- **Perplexity AI 演示在一个盒子里完成完整基金工作流** — 来自 Perplexity AI 的一个 AI 驱动系统声称在仅 1-2 名人员协助的情况下，可信地运行一个小型基金的核心工作流，而非整桌 10 名分析师。该项目 reportedly 涉及超过 4500 行代码与一个完整工作的 Web 应用。创作者将其定位为 Bloomberg 终端的更经济替代方案，并预告将发布详细实现的串文。 [来源-twitter](https://x.com/morganlinton/status/2026865776100258261)

### 人工智能

- **HyTRec 提出用于长行为推荐的混合注意力结构** — HyTRec 引入一种混合注意力架构，将长期稳定的用户偏好与短期信号解耦，从而提升对长序列的检索精度，同时降低软最大注意力的计算成本，成为大规模实现长期用户建模的可扩展解法。 [来源-huggingface](https://huggingface.co/papers/2602.18283)

- **MolHIT 通过分层离散扩散提升分子图生成能力** — MolHIT 引入了用于分子图生成的分层离散扩散框架，旨在克服以往图扩散方法的局限性，提升化学有效性与目标属性的一致性，解决相对于一维建模的挑战，推动 AI 驱动的药物发现与材料科学的发展。 [来源-huggingface](https://huggingface.co/papers/2602.17602)

### AI 安全

- **如何修复 OpenClaw 的内部推理泄漏** — 一条推文探讨如何减轻 OpenClaw 的内部推理泄漏，强调在 AI 代理中暴露思维过程所带来的安全性担忧，并寻求实际可行的修复办法。该帖凸显了在开源 AI 系统中保护内部推理的持续讨论。 [来源-twitter](https://x.com/babykeem/status/2026836033757934056)

### 多模态

- **DreamID-Omni：统一、可控的音频-视频生成** — 论文认为当前的方法将基于参考的音频-视频生成（R2AV）、视频编辑（RV2AV）与音频驱动的视频动画（RA2V）视为独立任务。它提出 DreamID-Omni，一种统一框架，旨在在单一系统中实现对多个角色身份与声线的精准、解缠控控制。 [来源-huggingface](https://huggingface.co/papers/2602.12160)

### 开源

- **开源 AI 指南：AI 知识库与 Vibe Coding 教程** — 由程序员 liyupi 创建的开源 AI 资源中心 ai-guide 汇聚了免费 AI 知识库、教程、提示词与变现指南。它覆盖模型选项（DeepSeek、GPT、Gemini、Claude）、工具（Cursor、Claude Code、OpenClaw、TRAE、Lovable、Agent Skills）、开发框架（Spring AI、LangChain）及行业新闻。该项目对外免费开放，旨在缩小信息差，现已演变为 Fish AI Navigation 网站。 [来源-github](https://github.com/liyupi/ai-guide)

- **Hello-Agents：Datawhale 的 AI 原生代理教程** — Datawhale 推出 Hello-Agents，这是一个全面的开源教程，指导学习者从基础到实践开发 AI 原生代理。该项目将 AI 原生代理与基于工作流的方法进行对比，提供使用 OpenAI API 构建多代理应用的实操示例，包括上下文、记忆、协议与评估。还包含旅行助手、 cyber town 等现实项目，以及 AI 代理的面试准备。 [来源-github](https://github.com/datawhalechina/hello-agents)

### AI 硬件

- **Ubuntu 26.04 LTS 通过自动驱动优化本地 AI** — Ubuntu 26.04 LTS 预计将内置自动硬件感知 AI 驱动程序，支持出厂即用的 NVIDIA CUDA 与 AMD ROCm，并引入 Inference Snaps（沙盒化 AI 推理容器）以及针对沙盒化 AI 代理的功能。更新旨在提升在 Ubuntu 上开发者与研究人员的本地 AI 能力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfmzfp/new_upcoming_ubuntu_2604_lts_will_be_optimized/)

### 行业

- **DeepSeek 向华为提供 V4 的早期访问；Nvidia/AMD 等待** — DeepSeek 已向国内供应商如华为提供其 V4_AI 模型更新的早期访问，旨在优化软件并确保在其硬件上的高效表现。与此同时，Nvidia 与 AMD 尚未获得访问权限，凸显 AI 硬件生态系统中的持续门槛与地缘政治摩擦。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rf7m85/deepseek_allows_huawei_early_access_to_v4_update/)

## ⚡ 快讯速览

- **Anthropic CEO Dario Amodei 就战争部讨论发表声明** — Anthropic 的首席执行官 Dario Amodei 发布声明，回应与战争部的讨论，强调在政府场景下对 AI 的国家安全用途需负责任、安全地部署。更多细节见 anthropic.com/news/statement。 [来源-twitter](https://x.com/AnthropicAI/status/2027150818575528261)

- **招募非传统背景人才以参与 AGI 研究** — AGI 研究人员在推动通过招聘的方式让非技术背景人员参与该领域。Tifa (@tifafafafa) 正在寻求具有非传统背景的杰出招聘人员，偏好前创始人。目标是组建具有情境感知与前瞻性品味的团队，以推动前沿进展，而非仅仅填补职位。 [来源-twitter](https://x.com/sama/status/2027087700214591913)

- **ByteDance 发布 DeerFlow 2.0 开源超代理框架 Harness** — DeerFlow 2.0 是 ByteDance 面向子代理、记忆与沙盒协同的开源超代理框架的全面重写。1.x 分支仍用于原始 Deep Research 框架，2.0 版本正在积极开发中。该项目托管在 GitHub，演示与文档见 deerflow.tech。 [来源-github](https://github.com/bytedance/deer-flow)

- **美国闭源 AI 模型 vs 开放中文模型引发行业紧张局势** — 讨论在离线环境下需要闭源美国模型的客户与开放中文模型的可获取性之间的冲突。文章认为旧的、能力较低的模型会让局势落后于现代的大型语言模型，并探讨切换到中文模型或游说 OpenAI 提供更多开放权重的选项，同时关注国家安全与数据泄漏的担忧。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfg3kx/american_closed_models_vs_chinese_open_models_is/)

- **Dual AMD Instinct MI50 AI 机架，64GB VRAM 与定制罩壳** — 一位爱好者构建本地 AI 服务器，配备两张 AMD Instinct MI50 GPUs（总计 64GB VRAM），主板为 Gigabyte X399 DESIGNARE，处理器为 Threadripper 2990WX。系统运行 Ubuntu 24.04 LTS + ROCm 6.3 与 llama.cpp，在 GLM 4.7 Q8_0 的吞吐率约为 50 t/s，负载下性能下降。为降低噪音，设计了一个 3D 打印的 MIT 许可罩壳（三部分），用于单一 92mm 风扇，作为开源模块化降温方案进行了文档化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfi53f/completed_my_64gb_vram_rig_dual_mi50_build_custom/)

- **AI 在小型 TAM 的定制软件市场中脱颖而出** — Balaji Srinivasan 认为 AI 在面向非常小的市场的定制软件中尤为强大，因为这类市场通常无法承担传统软件开发的成本。他建议小型市场通过降低开发成本来实现更高的 AI 驱动价值。该帖子将 AI 描绘为面向小众软件项目的降本驱动者。 [来源-twitter](https://x.com/balajis/status/2027099587937460375)

- **Top 10 Trending Hugging Face 模型** — Reddit 用户 jacek2023 询问 Hugging Face 上热度最高的前十模型的结论。该帖表现出对 HF 模型热度的兴趣，但未给出具体模型名称或细节。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rfjp6v/top_10_trending_models_on_hf/)

- **OpenAI 员工因 Burnout 离职，计划前往越南休整** — 一名 AI 专业人士宣布离开 OpenAI，此前曾在 xai 工作。他对团队与前沿 AI 研究表示肯定，但因疲惫与心理健康恶化，计划短暂休整并带家人赴越南寻求新机会与治疗。 [来源-twitter](https://x.com/hyhieu226/status/2026841633342501150)

---

*Generated by AI News Agent | 2026-02-26*