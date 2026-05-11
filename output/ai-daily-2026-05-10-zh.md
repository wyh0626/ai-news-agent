---
title: "AI 日报 — 2026-05-10"
description: "统一LLM检查点，Cull开源图像工具，Codex靠安全审计月赚506美元。"
lang: "zh"
pairSlug: "ai-daily-2026-05-10"
---

# AI 日报 — 2026-05-10

> 覆盖 25 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA Star Elastic：一个 checkpoint 覆盖 30B/23B/12B LLM

NVIDIA 发布了 Star Elastic，这是一个单一 checkpoint，其中包含 30B、23B 和 12B 的推理模型，并支持 zero-shot 切片，从而实现动态扩缩和跨模型引导。该方法将不同规模的模型视作共享 KV cache 的“嵌套层”，可以在不同大小之间快速切换，并支持本地离线推理。其设计借鉴了稠密模型和 MoE 的理念，实现了可扩展的“套娃式”模型集成，先用快速模型生成推理，再通过在不同模型间循环来精修输出。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t8s83r/nvidia_ai_releases_star_elastic_one_checkpoint/)

### 2. Cull：开源图像数据集爬取与分类工具

一个名为 Cull 的开源工具被推出，作为用于 AI 图像数据集的机器策展引擎。它可以从多种来源（Civitai、X/Twitter、Reddit、Discord 以及各类图像站）爬取图片和提示词，对每个来源进行去重，并用视觉-语言模型依据严格的 17 字段 JSON schema 进行分类。结果会在本地工作流中与提示词和审计记录一同组织起来，支持用于 LoRA 训练和数据集策展，并通过两个质量闸门分别控制整体质量和主题相关性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9jub0/sharing_cull_my_opensource_dataset_tool_for_image/)

## 📰 重点报道

### LLM

- **Codex 通过安全审计自主赚取每月 506 美元** — 一位用户使用 OpenAI 的 Codex 自主寻找并完成一个开源安全/审计悬赏任务。Codex 产出了一个合规的 PR，与维护者进行互动并拿到首笔 16.88 美元的报酬，如果每天复现一次，相当于每月约 506 美元，展示了一个早期的 AI 智能体变现案例。[来源-twitter](https://x.com/sama/status/2053566155571560868)
- **Bubeck 称 GPT-5.5 实现此前“不可能”的能力** — Sebastien Bubeck 回复 @roydanroy 时表示，双方讨论的话题在 GPT-5.5 之前根本不可能发生。该推文暗示新版本模型在能力上有显著跃迁，也折射出关于 AI 进展边界的持续争论。[来源-twitter](https://x.com/SebastienBubeck/status/2053513789010755762)
- **MTP 基准：任务类型主导推理速度（编码 vs 创意写作）** — 一位 AI 研究者对 Qwen 3.6 27B 做了大规模 MTP 基准测试，分析了 300+ 个在任务类型、temperature 与 MTP 量化上的组合。他发现 F16 + MTP 在编码任务中的速度几乎提升三倍，而在 Q4_K_M + MTP 下，创意写作反而变慢；相同特性和模型在不同任务上得到相反结果，表明推测式推理行为是主要性能驱动因素。研究也指出了局限（并未测试所有量化大小），但清楚地展示了任务类型与推理速度在推测式推理设置下的关联。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9gcar/mtp_benchmark_results_the_nature_of_the/)
- **Qwen3.6 35B A3B 在 8GB VRAM 上运行，支持 190k 上下文** — 一篇 Reddit 帖子展示了如何在配备 8GB VRAM RTX 4060 和 32GB 内存的设备上运行 Qwen3.6-35B-A3B，并通过一台 Linux 笔电作为 Tailscale 可访问的服务器，实现约 190k 的上下文长度。实测版本的 token 吞吐率约为 37–43 tok/sec，通过调节 ctx-size、n-gpu-layers 和 n-cpu-moe，并结合 Q5 量化模型，可进一步推到约 51 tok/sec。该配置凸显了在有限 GPU 资源上进行开源 LLM 推理的实用性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9eo83/running_qwen36_35b_a3b_on_8gb_vram_and_32gb_ram/)
- **DeepSeek-V4-Flash MTP 补丁在 RTX Pro 6000 上达 85 tok/s** — 在 DeepSeek-V4-Flash-W4A16-FP8 上加入改造过的 MTP 模块并使用 GPTQ 调优，使其在 524k 上下文（双流）下的解码速度达到 85.52 tok/s，在 128k 上下文（单流）时约为 111 tok/s。该模型（总参数 671B / 激活 32B）运行在两块 RTX PRO 6000 Max-Q GPU（各 96 GB、无 NVLink）上，并通过 vLLM 打补丁；相关工作已在 HuggingFace 与 Reddit 上记录发布。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9em98/deepseekv4flash_w4a16fp8_with_mtp_selfspeculation/)

### 开源

- **字节跳动开源多模态 AI Agent 技术栈** — 字节跳动宣布开源 Multimodal AI Agent Stack，并推出两个项目：Agent TARS 和 UI-TARS-desktop。Agent TARS 提供一个通用多模态 AI Agent，集成 GUI 和视觉能力，可通过 CLI 和 Web UI 访问，目标是实现类人任务完成，并与现实世界的 MCP 工具无缝集成。UI-TARS Desktop 则是一个原生桌面 GUI 应用，可操控本地/远程计算机和浏览器操作器，突出了该项目技术栈在开源领域的可用性。[来源-github](https://github.com/bytedance/UI-TARS-desktop)
- **Rowboat 推出开源个人 AI 知识图谱** — Rowboat Labs 发布了 Rowboat，这是一款开源的 AI 协作助手，会从你的邮件和会议记录中构建一个长期维护的知识图谱，并在本机本地运行。它利用该知识图谱生成演示文稿、准备会议简报、跟踪主题，并通过 Markdown 界面可视化与编辑图谱。该工具已在 GitHub 上提供 Mac、Windows 和 Linux 的下载版本。[来源-github](https://github.com/rowboatlabs/rowboat)
- **面向 Diffusion 微调的开源超参数搜索工具** — 一位开发者发布了 Bracket，这是一款用于自动化 Diffusion 模型微调超参数搜索的开源工具。它会基于 Optuna 的 TPE 框架并行运行多个短训练试验，然后结合训练损失轨迹和本地 VLM 图像质量评估来给结果打分。该工具输出包含 Welch t 检验结果的 Markdown 报告，以判定统计上更优的配置，并通过编排现有训练脚本（musubi-tuner 和 sd-scripts）而非重实现训练本身。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9k8gy/i_built_an_open_source_hyperparameter_search_tool/)

### AI

- **AgentMemory 为 AI 编程 Agent 提供持久记忆** — AgentMemory 为 AI 编程 Agent 提供一个持久化的记忆层，使其能够跨会话记住上下文，避免重复解释。该项目基于 iii 引擎构建，支持 Claude Code、Cursor、Gemini CLI、Codex CLI、pi 和 OpenCode 以及 MCP 客户端，并增加了置信度评分、生命周期管理、知识图谱与混合检索等功能。它可以通过 hooks、MCP 或 REST API 与任何智能体集成，并在多种实现之间共享一个公共内存服务器。[来源-github](https://github.com/rohitg00/agentmemory)
- **Oracle AI Developer Hub 支持在 OCI 上构建 AI 应用** — Oracle AI Developer Hub 为开发者提供技术资源，用于基于 Oracle AI Database 和 OCI 服务构建应用、Agent 和系统。该仓库按应用与参考实现进行组织，附带源码、部署配置和文档，用于展示基于 Oracle 技术的端到端、生产级 AI 解决方案。仓库中包含如 FitTracker 等示例应用，以说明实际的集成模式和最佳实践。[来源-github](https://github.com/oracle-devrel/oracle-ai-developer-hub)

### 硬件

- **llama.cpp b9095 发布：在双 Blackwell PCIe 上实现无 NCCL 的 Tensor 并行** — llama.cpp b9095 版本实现了在双 Blackwell PCIe GPU 上无需 NCCL 的 Tensor 并行（-sm）。这可能会显著提升使用双 Blackwell 硬件用户的性能。讨论中还提到针对 2x5060ti 配置的即将发布的基准测试结果。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t96l6r/ncclfree_tensor_parallelism_on_dual_blackwell/)

## ⚡ 快讯速览

- **全球 AI 模型“地理分布”盘点，硅谷在话题上领先** — Yann LeCun 以轻松的语气盘点了全球范围内 AI 模型和相关技术的“归属地”。该讨论串列出了 AlphaGo、AlphaFold、ESMFold、Llama、DeepSeek、DINO 和 JEPA 等模型和项目在不同城市的分布，并指出硅谷在话题上大约领先其他地区三个月，凸显了全球 AI 研发活动与实验室竞争的格局。[来源-twitter](https://x.com/ylecun/status/2053495035031609808)
- **为何美国仍缺乏有竞争力的开源 AI 实验室** — 一则 Twitter 贴文指出，美国至今仍没有真正有竞争力的开源 AI 模型实验室。作者认为资金和算力并非瓶颈，因为新实验室已经筹集了数十亿美元且美国实验室也能获取硬件资源，于是追问更深层次的问题究竟是什么。[来源-twitter](https://x.com/Yuchenj_UW/status/2053523449956765759)
- **Shopify 的 River Agent 常驻 Slack 以实现公开化学习** — Shopify 的 River AI Agent 运行在 Slack 中，但被限制为公开场景使用，以便同事可以从彼此的工作流程中学习。这一设置被类比为 Midjourney 起初在 Discord 上发布，让用户通过旁观他人来掌握提示工程。该动态提及 Shopify CEO Tobias Lütke，以及围绕内部工具透明化的持续讨论。[来源-twitter](https://x.com/simonw/status/2053529689122328947)
- **Karpathy 的 wikiLLM 让 Obsidian 变成“第二大脑”** — Karpathy 此前发布了 wikiLLM，将 Obsidian 与 Claude 的 code/codex 集成。一位正在恢复中的作者最近完成部署后表示非常兴奋，称这给了他们一个“第二大脑”。该贴强调了 wikiLLM 作为一个值得关注的 AI 知识管理工具的地位。[来源-twitter](https://x.com/kimmonismus/status/2053430289364308112)
- **SFT、RL、OPD 与泛化能力及灾难性遗忘的关系** — 一篇博客文章探讨了有监督微调（SFT）、强化学习（RL）和 OPD 与 AI 模型的泛化能力及灾难性遗忘之间的关系。文章讨论了不同训练范式对模型稳定性和记忆保持的影响。[来源-twitter](https://x.com/nrehiew_/status/2053482603475501361)
- **测算本地 LLM 的真实 tokens/s 体验** — 一篇 Reddit 帖子指出，原始 tokens-per-second 数值往往难以体现真实速度体验。作者推荐了一个脚本，从文本、代码和推理三类任务来测量 tokens/s，以便更直观地感受本地 LLM 的性能，并以 Qwen 3.6-27B 在 21 tokens/s 的表现作为示例。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t99upf/getting_a_feel_for_how_fast_x_tokenssecond_really/)
- **Gemma-4-26b-a4b 在 Three.js 一次性代码生成上表现出色** — 一名 Reddit 用户称赞 Gemma-4-26b-a4b 在生成 Three.js 代码的一次性提示表现方面非常强大。作者介绍了一个 Python 应用，会轮流发送提示、从 CSV 提示列表生成 HTML、检测崩溃并归档完成的 demo，并附上一个静态 demo 和 GitHub 页面链接。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9cle9/anybody_else_noticing_how_good_gemma426ba4b_is/)
- **Hermes Agent 新增 LINE 网关通道** — Hermes Agent 现已正式支持 LINE 作为与你的智能体交互的网关通道。用户可以将 Hermes Agent 配置为一个 LINE Messaging API 机器人，并通过 hermes update 命令开始使用，相关文档位于 hermes-agent.nousresearch.co。[来源-twitter](https://x.com/Teknium/status/2053475951372386656)
- **Aurora Optimizer 博客：重视 Rohan 对 AI 实验室的洞见** — 一则关于 Aurora Optimizer 博客的记录强调应重视 Rohan 的相关洞见。帖中还包含一个技术侧注，谈到“muon” 正尝试在预条件器场景中让由于死神经元导致梯度为零的单元“复活”。同时，讨论也再次提出：尽管拥有资金和硬件访问能力，为何美国仍没有真正有竞争力的开源模型实验室。[来源-twitter](https://x.com/eliebakouch/status/2053607014366945461)
- **Sama 暗示下一代 AI 模型或命名为 “Goblin”** — OpenAI CEO Sam Altman 在一条推文中暗示下一代 AI 模型可能会被命名为 “Goblin”。这更像是一种玩笑而非正式产品公告，但也反映了围绕未来模型品牌命名的持续讨论，尚未体现任何具体计划。[来源-twitter](https://x.com/sama/status/2053572868936761350)
- **删除不必要的 Agent 生成注释与测试代码** — 一则贴文提到正在移除由 AI Agent 自动生成的多余注释和测试代码。作者 isaniss 在 5 月 9 日表示，他们可以“整天都做这件事”，并附带提到关于启用 HLS 播放的说明。[来源-twitter](https://x.com/theo/status/2053548693287211300)
- **玩本地 LLM 过头：线圈啸叫声“跟进梦里”** — Reddit 用户 /u/MrChilliBalls 发帖称自己花太多时间折腾本地大语言模型（Local LLMs）。他以幽默方式表示，甚至在睡梦中都能“听到线圈啸叫声”，并向社区求助建议。该贴发布在 r/LocalLLaMA 子版面，反映了大家对开源本地 LLM 探索的持续热情。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t9jyfu/i_think_i_spent_way_too_much_time_messing_with/)

---

*由 AI News Agent 生成 | 2026-05-10*