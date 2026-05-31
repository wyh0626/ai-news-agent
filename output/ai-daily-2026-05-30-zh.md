---
title: "AI 日报 — 2026-05-30"
description: "前DeepMind团队融资，Hermes超越OpenClaw，托管评估简化模型。"
lang: "zh"
pairSlug: "ai-daily-2026-05-30"
---

# AI 日报 — 2026-05-30

> 覆盖 27 条 AI 新闻

## 🔥 今日焦点

### 1. 前 DeepMind 团队融资 5000 万美元，打造递归 AI 实验室

前 DeepMind 研究人员已完成 5000 万美元融资，计划打造一个聚焦“递归自我改进”的 AI 实验室，改进对象不仅是单个模型，而是整个组织层面。此轮融资由 Index 和 Radical 领投，NVIDIA 风投部门及多位知名天使投资人参投。创始人 Louis Kirsch、Edward Hughes 和 Tantum Collins 拥有自我改进系统、开放式 AI 与 AI 政策背景，目标是构建能在持续实验中与人类协作的 AI，并以公共利益公司（Public Benefit Corporation）的形式运营。 [来源-twitter](https://x.com/kimmonismus/status/2060679313951756554)

### 2. Hermes Agentic AI 赶超 OpenClaw：领导者必须掌握的 10 大转变

《福布斯》文章指出，随着智能体系统加速发展，Hermes Agentic AI 已在竞争中超越 OpenClaw。文中梳理了正在重塑企业战略、速度与执行方式的十个关键“智能体化转变”，并强调领导者今天就应理解和应对这些变化。 [来源-twitter](https://x.com/Teknium/status/2060549920139153511)

### 3. 推出 Hosted Evaluations，简化模型评测流程

该平台宣布推出 Hosted Evaluations，旨在解决模型评测中牵涉大量基础设施的问题，包括评测框架、沙箱环境和大规模算力负载。该功能通过代管复杂基础设施，来简化和扩展评测工作流，大幅减少人工搭建与运维开销。 [来源-twitter](https://x.com/PrimeIntellect/status/2060803767432515872)

## 📰 重点报道

### Open Source

- **Biohub 发布蛋白质生物学世界模型：ESMC、ESMFold2、ESM Atlas** — Biohub 发布了一个面向蛋白质生物学的世界模型，将 ESMC、ESMFold2 和 ESM Atlas 结合，用于多尺度上的蛋白质预测、设计和发现。ESMC 是在数十亿蛋白序列上训练的蛋白语言模型，用来学习蛋白质生物学；ESMFold2 进一步提升结构预测能力，而 ESM Atlas 提供蛋白映射与教程资源。该项目在 GitHub（Biohub/esm）开源，基于 Evolutionary Scale Modeling，在模型扩展时捕捉长程结构信息。 [来源-github](https://github.com/Biohub/esm)
- **开源工具将人声模仿转成音效** — 一个名为 VTS 的新开源项目允许用户用自己的声音去模仿目标声音，然后结合文本输入生成真实的音效。该项目在 GitHub 上以 thxxx/VTS 托管，目标是简化电子游戏和视频制作中的音效设计，并在 Reddit 上征集反馈。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trve9e/open_source_turning_vocal_imitations_into_sound/)
- **Fulloch V2：100% 本地运行的 Home Assistant 语音助手** — Fulloch V2 展示了一个完全本地运行、基于消费级 GPU 的语音助手，使用基于 Qwen 的 ASR/TTS 模型驱动 Home Assistant，支持声学打断（barge-in）和实时响应。它还与本地 Obsidian 笔记库集成，可读取、写入和追加笔记，并通过本地 embedding 模型对 markdown 笔记进行语义搜索。该项目完全开源，提供公开 GitHub 仓库和演示视频。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trw5ym/fulloch_v2_100_local_voice_assistant_for_home/)
- **MOSS TTS v1.5 以出色的音色克隆表现惊艳** — OpenMOSS-Team 的 MOSS TTS v1.5 因其优秀的声音克隆能力而备受好评。帖子作者更偏好该模型而非 Fish Audio S2 Pro，原因在于其商业使用许可更友好，并提到 Long Cat DiT 3.5 也是一个表现很强的备选方案。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trq8kq/this_new_moss_tts_15_is_damn_good_with_voice/)

### AI Research

- **OpenAI：AI 通过扩展“敢想敢做”的边界加速科研** — OpenAI 认为，AI 能让研究人员从重复性工作中解放出来，从而敢于追求更大胆、更高风险的想法。Terence Tao 指出，AI 让许多过去难以尝试的实验和研究路径变得可行，拓展了数学与科学探索的范围。 [来源-twitter](https://x.com/gdb/status/2060611636767998241)

### Multimodal

- **Seedance 2.0 仍然领跑文本转视频，发布于今年 2 月** — 一则推文声称，即便 Seedance 2.0 在今年 2 月就已发布，在文本转视频基准测试中仍然“未逢敌手”。帖子表示，目前尚无实验室在该方向上超越 Seedance 2.0，凸显其在多模态 AI 视频生成上的领先地位。 [来源-twitter](https://x.com/kimmonismus/status/2060715486199845322)

### LLM

- **GPT-5.5 在 DeepSWE 基准上超越 Opus 4.8** — 据报道，GPT-5.5 在 DeepSWE 基准测试中，在分数、运行时间和 Token 效率方面都优于 Opus 4.8。该结果显示出 GPT-5.5 在这一评测中的整体优势，信息来自 Twitter 报道。 [来源-twitter](https://x.com/scaling01/status/2060768119941947699)
- **NVIDIA 为 vLLM 推出量化版 Qwen3.6-35B-A3B-NVFP4** — NVIDIA 发布了阿里巴巴 Qwen3.6-35B-A3B 模型的 NVFP4 后量化版本，用于在 vLLM 框架下进行高速推理。量化将参数精度从 16 bit 降至 4 bit，使磁盘占用和 GPU 显存减少约 3.06 倍，并对 MoE Transformer 模块中的线性算子权重与激活进行量化。基准测试显示，NVFP4 在 MMLU、GPQA、SciCode 等多项测试中的表现接近 BF16 基线。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ts6j6j/nvidiaqwen3635ba3bnvfp4_hugging_face/)
- **Parallax：面向 LLM 的可扩展参数化局部线性注意力** — Parallax 提出一种可扩展的参数化 Local Linear Attention（LLA）机制，用于大语言模型，以解决以往在计算与数值稳定性方面的难题。该方法移除了数值求解器，并加入一个可学习的“查询式”投影器，用于探测 KV 协方差，将 Parallax 置于一类由带宽、探测向量构造和仿射结构定义的注意力机制家族中，从而在预训练中改善偏差-方差权衡。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ts79rg/parallax_parameterized_local_linear_attention_for/)

### Computer Vision

- **SAM 零样本 + YOLO 微调实现快速细胞追踪** — 一则信息讨论了如何用计算机视觉追踪细胞运动。其重点是对免疫细胞应用零样本 SAM，以及在一个小型细菌数据集上微调 YOLO 模型，整体预计实现时间约为 2 小时。 [来源-twitter](https://x.com/mfranz_on/status/2060836382432497679)

### AI Hardware

- **RTX 5090 在 Qwen 3.5-4B 上难以突破 250 TPS** — 一位 Reddit 用户在 Windows Docker 中运行 llama.cpp，使用 Qwen 3.5-4B（并以 Qwen 3.6-27B-mtp 为主模型）时，报告推理吞吐量不佳。其观测到 27B 模型约 100 TPS，而 4B 模型也仅有 200–250 TPS，GPU 利用率约 50%，CPU 几乎空闲，即使预填（prefill）速率可达 2500 TPS。即便测试了多个构建/工具（llama.cpp、havenoammo/llama:cuda13-server、LM Studio），也未获得明显改善，暗示问题更可能出在环境配置而非硬件本身。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ts049w/cant_get_over_250tps_on_rtx5090_with_qwen354b/)

## ⚡ 快讯速览

- **Yoshua Bengio：教皇关于“AI 与共同福祉”的观点是正确的** — Yoshua Bengio 在推文中表示，AI 必须服务于所有人和共同福祉，这与教皇对负责任技术的呼吁一致。他强调，关于 AI 的决策应由良知引导，并呼吁梵蒂冈和全球机构积极参与 AI 治理对话。该帖子突出 AI 治理与伦理在应对未来挑战中的核心地位。 [来源-twitter](https://x.com/Yoshua_Bengio/status/2060760922457539034)
- **Hermes Agent 在读取时可减少 14% 输入 Token** — 一则关于 Hermes Agent 的更新称，其在文件读取操作中平均减少了 14% 的输入 Token 数。该改进已合入主分支，用户可通过运行“hermes update”获得最新版本。 [来源-twitter](https://x.com/Teknium/status/2060839436330655775)
- **爆料称 OpenAI 规划 GPT-5.1 至 GPT-5.5 升级路径** — 一则推文声称，OpenAI 将在 GPT-5 之后继续训练更多模型，从 GPT-5.0 持续迭代到 GPT-5.5。帖子表示每个版本都会在能力与 Token 效率上有所提升，其中 GPT-5.5 被描述为“迄今为止最强模型”，并将这种持续升级视作一种简单而有效的策略。 [来源-twitter](https://x.com/ericmitchellai/status/2060743913892458510)
- **假设情景：押上 90% 净资产赌一家 300 亿美元 AI 独角兽失败** — 一条在线帖子询问，若要押注一家估值 300 亿美元以上的 AI 初创公司会失败，该去哪里、如何下注，且赌注金额相当于个人 90% 的净资产。该讨论凸显 AI 创业公司高风险和高估值的特性，并引发关于下注、对冲与风险评估的争论。 [来源-twitter](https://x.com/joannejang/status/2060548850797236509)
- **即便没有意识，AI 模型也存在“内在性”** — 一则推文认为，即便 AI 模型并不具有人类意义上的意识，它们依然拥有“内在性”（interiority）。帖子强调了关于机器内部状态是否真实且有意义的持续争论，这条推文是对用户 @credenzaclear2 的回复，反映了围绕 AI 意识的哲学讨论。 [来源-twitter](https://x.com/tszzl/status/2060833909177491712)
- **Stable-WorldModel 发布可复现实验的世界模型平台** — Stable-WorldModel 提供一个统一接口，用于在标准化环境中进行世界模型的数据采集、训练和基于模型预测控制（MPC）的评估。它内置常见基线和规划求解器的参考实现，帮助研究者将精力集中在模型与目标设计上。该项目可通过 PyPI（基础版或完整版）安装，并支持可选的 LeRobot 数据集，需要 Python 3.12+，源代码在 GitHub 提供。 [来源-github](https://github.com/galilai-group/stable-worldmodel)
- **6400 美元本地 LLM 服务器的成本分析** — 一位作者分享了自建本地 LLM 服务器与使用 API 的总拥有成本（TCO）对比，强调硬件折旧可能严重影响 TCO 计算。文中逐项列出硬件到手价：AMD Instinct MI100 GPU、华擎 ASRock EPYCD8-2T 主板、1600W 白金电源、DDR4 ECC 内存、AMD EPYC 7k62 CPU、散热器、机箱以及线材和风扇，并讨论硬件在未来可能升值或贬值的情形。文章的目标是展示自建本地 LLM 服务器的成本构成，而非 API 价格。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tsbl9j/cost_analysis_of_my_64k_local_llm_server/)
- **GPU 规格对比：带宽并非 AI 设备性能的唯一关键** — 一则 Reddit 帖子分析了本地 AI 工作流中常见的主要 GPU/整机，认为仅凭带宽并不能决定性能，其他指标同样重要。文中提供一张扩展表格，详细列出多款 GPU 的价格、FP16 TFLOPS、显存容量、带宽以及单位成本，包括 RTX Pro 6000 系列、Arc Pro、Radeon Instinct MI50、Radeon AI PRO R9700，以及 RTX 4060 Ti/5060 Ti/5070 Ti 等消费级显卡。讨论还涉及 Mac 设备的推荐，并指出 Pro 6k 和 M3 Ultra 在定价上的一些调整。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trkze4/i_compared_all_specs_of_the_major_gpusmachines/)
- **所有 DGX Spark 克隆机型并排对比** — 一条 Reddit 帖子整理了一张图片，将多款 DGX Spark 克隆机并排展示，对比其物理尺寸（宽、高、长）和重量。阵容包括 Dell Pro Max、HP ZGX Nano G1n、Lenovo ThinkStation PGX、MSI EdgeXpert、GIGABYTE AI TOP ATOM、Acer Veriton GN100 AI Mini Workstation 和 ASUS Ascent GX10，其中部分尺寸被标记为不确定。帖子注明图片作者为用户 /u/rexyuan，并附上一个 gist 链接。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1trms2k/all_dgx_spark_clones_side_by_side_in_one_image/)
- **STT-LLM-TTS 流水线：如何编排三个模型的协同** — 一位 Reddit 用户介绍了自己在 Ubuntu + 3090 GPU 上搭建的 STT-LLM-TTS 流水线，使用 llama.cpp 运行 Qwen 3.6 27B Q4，并结合 pi-agent 实现工具调用。他正在寻求关于 STT、LLM 与 TTS 之间数据流应如何组织的指导，以及究竟该运行三个独立的 llama.cpp 实例，还是采用统一的框架。目前其全部操作均在终端中完成，没有使用聊天前端。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ts0jjb/stt_llm_tts_pipeline/)
- **高斯 Splats 结合 AI 创造颇具吸引力的视觉场景** — 帖子展示了一种将高斯 Splats 与 AI 相结合的技术，用于生成颇为有趣的视觉场景，并给出一个示例。作者提醒需启用 HLS 播放以查看最终效果。 [来源-twitter](https://x.com/cemdemir/status/2060767843696754938)
- **通过降低温度与 top-p 来稳定低比特量化 LLM** — 一则 Reddit 帖子探讨了如何通过降低 temperature 和 top-p 来稳定低比特量化后的 LLM，以减少“发疯式”输出，尤其是在 80GB 显存上运行大模型时。作者指出，Mixture-of-Experts（MoE）在进行 CPU offload 时速度会很慢，许多大模型不得不进行重度量化，因此计划借助可视化工具测试基于采样参数的稳定性方法，并表示会分享演示链接。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ts94t8/has_anyone_experimented_with_stabilizing_low/)
- **“用 Codex 写代码真爽”，来自 Carol Monroe 的评价** — Carol Monroe 在推文中称赞 Codex 是一个非常好用的编程工具，构建软件的体验令人愉快，体现出开发者对这一 AI 编码工具的积极评价。该帖子并未宣布任何新功能或新产品，而是更多强调 Codex 在开发者群体中的良好口碑。 [来源-twitter](https://x.com/gdb/status/2060581381093388430)

---

*由 AI News Agent 生成 | 2026-05-30*