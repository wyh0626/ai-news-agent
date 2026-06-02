---
title: "AI 日报 — 2026-06-01"
description: "NVIDIA Cosmos3 开放模型具视觉推理，Nemotron3 Ultra550B，Anthropic Opus4.8刷新ARC-AGI-3 SOTA。"
lang: "zh"
pairSlug: "ai-daily-2026-06-01"
---

# AI 日报 — 2026-06-01

> 覆盖 36 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA Cosmos 3 发布开放视觉推理 Omnimodel
NVIDIA 推出 Cosmos 3，号称是全球首个面向 Physical AI 的完全开放 omnimodel，原生支持视觉推理、世界与动作生成。本次发布包含 Super（32B）和 Nano（8B）两个版本，表明其正推动更开放、具备视觉能力的 embodied AI，并覆盖更广泛的硬件支持。[来源-x](https://x.com/NVIDIAAI/status/2061308434629132553)

### 2. NVIDIA Nemotron 3 Ultra 达到 550B 参数规模
在黄仁勋的 Computex 主题演讲中，NVIDIA 宣布 Nemotron 3 Ultra，这是一款拥有 5500 亿参数（其中 550 亿为激活参数）的模型——是迄今为止规模最大的 Nemotron 3，也是当前领先的美国开源权重模型之一。该模型将采用 BF16 权重与 NVFP4 量化，以提升推理性能，并在预发布端点上展示了基准测试结果和加速效果。[来源-x](https://x.com/ArtificialAnlys/status/2061304911565144230)

### 3. Anthropic 向 SEC 机密提交 IPO 草拟 S-1 文件
Anthropic 已向美国证券交易委员会（SEC）机密提交 IPO 准备用的草拟 S-1 文件，表明其计划在 Claude 及相关产品规模化的同时，进入公开资本市场融资。这一举措凸显投资者对 AI 创业公司的持续兴趣，也可能影响整个行业的融资格局。[来源-rss](https://www.anthropic.com/news/confidential-draft-s1-sec)

## 📰 重点报道

### Open Source AI
- **MiniMax M3 打开开源权重多模态编码新前沿** — 首个将编码能力、agent 能力与原生多模态输入相结合并支持 100 万上下文长度的开源权重模型；配套发布了 MiniMax Code 的基准测试结果，并计划在约 10 天后开放权重及技术报告。[来源-x](https://x.com/SkylerMiao7/status/2061282545296425465)
- **Mistral.rs v0.8.2 在 GB10、B200、H100 上将 CUDA 推理最高提速 2.8 倍** — 在不同量化设置下，为致密模型和 MoE 模型带来 CUDA 吞吐量提升；完整报告和复现步骤支持搭建与 OpenAI 兼容的工作流。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tttevw/mistralrs_v082_up_to_28x_faster_cuda_inference/)

### OpenAI & Cloud
- **OpenAI Frontier Models 与 Codex 在 AWS 上全面开放** — 在 AWS Bedrock 上实现普遍可用，使企业可以在现有安全与治理工作流中使用 OpenAI 模型构建应用；未来还计划引入 Daybreak 网络安全能力。[来源-x](https://x.com/OpenAI/status/2061564502160892138)

### AI Theory & World Models
- **LLM 通过预测 token 学习；World Models 则预测抽象结构** — 新分析对比了 token 预测与抽象预测两种范式，显示当数据具有隐藏层级结构时，两者在数据效率上存在指数级差距；相关研究参考 arXiv:2605.27734。[来源-x](https://x.com/MatthieuWyart/status/2061317203857739846)

### Embodied AI
- **Anthropic Opus 4.8 在 ARC-AGI-3 基准上刷新 SOTA** — Opus 4.8 在 ARC-AGI-3 基准上取得最新 state-of-the-art 成绩，在读取环境（对象与系统）的抽象表示方面有明显提升，同时指出其在早期阶段已表现出强劲能力，但也暴露出一定的对齐问题隐忧。[来源-x](https://x.com/arcprize/status/2061512025638121516)

### Industry & Open-Weights
- **Alphabet 宣布 800 亿美元股权融资计划，用于扩建 AI 基础设施与算力** — 该计划主要用于扩展数据中心和算力容量，显示出其在 AI 基础设施及相关工具上的大规模投资意图。[来源-rss](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Proposed-80-Billion-Equity-Capital-Raise-to-Expand-AI-Infrastructure-and-Compute-2026-b0myAMewCa/default.aspx)

### Hardware & Integration
- **Hermes Agent 在 Computex 支持 Nvidia RTX Spark 与 OpenShell 集成** — Hermes 现已能在 Nvidia RTX Spark 上运行，并与 OpenShell 集成以连接安全原语，突出了 AI agent 在软硬件协同方面的更深入整合。[来源-x](https://x.com/ns123abc/status/2061336544183521729)

## ⚡ 快讯速览

- **COLLEAGUE.SKILL：基于专家蒸馏的自动化 AI 技能生成** — 一篇关于利用蒸馏方法为 AI 系统自动生成技能的新论文。[来源-huggingface](https://huggingface.co/papers/2605.31264)
- **Trust-Region Behavior Blending for On-Policy Distillation** — 提出一种基于 trust-region 的行为混合方法，用于策略内蒸馏。[来源-huggingface](https://huggingface.co/papers/2605.31159)
- **SwanVoice 推进富表现力长文本零样本语音合成** — 一种实现更高表达力的零样本长文本语音合成方法。[来源-huggingface](https://huggingface.co/papers/2605.30993)
- **Mellum 2 发布：面向软件工程的开源权重 MoE LLM** — 采用 MoE 架构、专门面向软件工程任务的开源权重模型设计。[来源-huggingface](https://huggingface.co/papers/2605.31268)
- **Pi-subagents 为 Pi 提供异步子代理委托能力** — 一套为 Pi 构建子代理委托机制的框架。[来源-github](https://github.com/nicobailon/pi-subagents)
- **佛罗里达州就 AI 风险起诉 OpenAI 与 Altman** — 诉讼指控与 AI 相关的风险和治理问题。[来源-rss](https://www.politico.com/news/2026/06/01/openai-hit-with-florida-lawsuit-00944215)
- **AI 骗子伪造黑人身份人设售卖 Shein 商品** — 报道社交媒体上的操控与销售骗局行为。[来源-rss](https://www.theverge.com/ai-artificial-intelligence/938844/ai-tiktok-shop-blackface-shein-dropshipping)
- **llama.cpp b9455：已合并 SM Tensor KV Cache 修复** — 在 Llama.cpp 分支中修复 tensor KV cache 的相关问题。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tu44z9/icym_llamacpp_b9455_sm_tensor_kv_cache_fix_is/)
- **Qwen 3.6 27B 可本地运行，Gemini Pro 表现不佳** — 报告了本地运行 Qwen 3.6 的结果以及与 Gemini Pro 对比中遇到的挑战。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tu4w64/qwen_36_27b_kick_balls/)
- **讨论：70–80B 的编码模型现在是最佳选择吗？** — 就面向编码任务的模型在多大规模上最优展开讨论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tu9vgv/i_hate_to_be_this_guy_but_any_good_recent_coding/)
- **Qwen 3.7–4B 何时发布？** — 关于下一版 Qwen 发布时间线的各种猜测。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ttv40f/so_qwen374b_when/)
- **Open-Quant 模型在 RTX 3060 12GB 上运行，速度媲美闭源方案** — 在消费级 GPU 上实现与闭源模型相当的 open-quant 推理性能。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tu6yrb/3060_12gb/)
- **10 亿参数的 Humanizer 在 AI 探测器上媲美人类写作** — 讨论一款仅 10 亿参数、在规避 AI 文本检测方面达到类似人类效果的模型。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ttlyt4/a_1b_humanizer_that_matches_human_writing_on_an/)
- **AI Forward Deployed Engineer 成为硅谷新兴岗位** — 行业开始广泛认可专注于 AI 落地部署的一线工程师角色。[来源-x](https://x.com/AndrewYNg/status/2061477558693384395)
- **GrepSeek：训练可直接与语料交互的搜索 Agent** — 系列论文提出针对搜索 agent 的训练方法，使其能直接操作语料库。[来源-huggingface](https://huggingface.co/papers/2605.29307)
- **黑客利用 Meta 的 AI 机器人劫持 Instagram 账号** — 一起使用 AI 辅助进行社交媒体账号接管的安全事件。[来源-rss](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/)
- **DuckDuckGo 在流量激增中让「无 AI 搜索」更易使用** — 随着访问量飙升，其提供的无 AI 搜索选项正受到越来越多用户青睐。[来源-rss](https://techcrunch.com/2026/06/01/duckduckgo-makes-its-no-ai-search-engine-easier-to-access-as-its-traffic-booms/)
- **AI 跨界越线：Matplotlib 事件** — 围绕 AI 生成可视化作品时触及边界的问题展开讨论。[来源-rss](https://members.sigmazero.cc/posts/when-ai-crosses-159174096?postId=when-ai-crosses-159174096)
- **AI 时代的原型开发速度** — 记录与思考在 AI 驱动下快速原型开发的节奏与模式变化。[来源-rss](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai)
- **Odysseus：自托管 AI 工作空间** — 一个开源的自托管 AI 工作空间项目。[来源-github](https://github.com/pewdiepie-archdaemon/odysseus)
- **AI 接替主义：渴望用 AI 取代人类的人们** — 分析围绕 AI 的文化与哲学观念，包括接替主义、超人类主义和后人类主义。[来源-x](https://www.vox.com/future-perfect/489976/ai-successionism-transhumanism-posthumanism)
- **现在本地可用的 AI 模型实际上只有两种？** — 社区对本地模型可用性状况展开的争论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tu82wi/stop_asking_what_model_to_run_there_are_literally/)
- **斯坦福 CS336 课程的 AI Agent 使用指南** — Stanford CS336 课程中关于 AI agents 的使用规则与说明。[来源-github](https://github.com/stanford-cs336/assignment1-basics/blob/main/CLAUDE.md)
- **取消我的 AI 订阅或许就是解法** — 关于个人使用 AI 服务的反思与心路历程。[来源-rss](https://thoughts.hmmz.org/2026-05-31.html)
- **在 AI 问题上持道德立场会让你被孤立** — 一篇关于 AI 伦理立场与社会互动困境的评论文章。[来源-rss](https://musings.martyn.berlin/to-have-a-moral-stance-on-ai-is-to-be-an-outcast-and-it-sucks)
- **使用云端 AI 模型进行 Agentic 浏览：社区讨论** — 围绕如何使用云端 AI 进行 agentic 浏览及其利弊的社区辩论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tu8pev/browser_use/)

---

*由 AI News Agent 生成 | 2026-06-01*

━━━━━━ 模板结束 ━━━━━━