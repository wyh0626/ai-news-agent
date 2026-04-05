---
title: "AI 日报 — 2026-04-04"
description: "GPT-Image-2泄露显强世界知识；Qwen3.6Plus压路由，令牌万亿。"
lang: "zh"
pairSlug: "ai-daily-2026-04-04"
---

# AI 日报 — 2026-04-04

> 涵盖 18 条 AI 新闻

## 🔥 今日焦点

### 1. OpenAI 的 GPT-Image-2 泄露，号称具备强大世界知识

OpenAI 的 GPT-Image-2 泄露，声称具备极其强大的世界知识和出色的文本渲染能力。帖子列出了代号 maskingtape-alpha、gaffertape-alpha 和 packingtape-alpha，并暗示其可能优于 Nano Banana Pro；该模型与 Arena 关联。[来源-twitter](https://x.com/kimmonismus/status/2040338389526822933)

### 2. Qwen 3.6 Plus 在 OpenRouter 上单日处理 1 万亿 Token，位列榜首

阿里巴巴的 Qwen 3.6 Plus 成为 OpenRouter 上首个在单日内处理超过 1 万亿 token 的模型，峰值约达 1.4 万亿。此成绩标志着今年已发布模型中单日表现最强的一次，OpenRouter 也向 Qwen 团队表示祝贺。[来源-twitter](https://x.com/OpenRouter/status/2040239467865489874)

### 3. T3 Code 确认对 Claude 订阅安全；本地封装使用被允许

一则 X/Twitter 帖子称，T3 Code 已被确认对 Claude 订阅用户是安全的，并且已经获得明确确认：将 Claude Code 封装成本地工具的做法是被允许的。发帖者将此视为在围绕 Anthropic 传播策略讨论之中的一项积极进展。[来源-twitter](https://x.com/theo/status/2040221237503561780)

## 📰 重点报道

### LLM

- **GLM-5 以 1/11 成本接近 Claude Opus 表现** — YC-Bench 进行了一项为期一年的试验，让 12 个 LLM 在数百轮交互中管理一个模拟创业公司。GLM-5 在表现上几乎追平 Claude Opus 4.6，而单次运行成本却低约 11 倍；最顶尖的模型平均最终资金约为 120 万美元，而许多其他模型则“创业失败”。该研究强调了在延迟反馈条件下长周期推理连贯性的重要性，并指出 Kimi-K2.5 在“每 API 美元收入”指标上表现最佳。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sbyte4/we_gave_12_llms_a_startup_to_run_for_a_year_glm5/)
- **扩展版 NYT Connections 基准：MiniMax-M2.7 以 34.4 分领跑** — 一项扩展版 NYT Connections 基准报告了开源模型得分：MiniMax-M2.7 获得 34.4 分，Gemma 4（31B）得分 30.1，Arcee Trinity Large Thinking 为 29.5。结果通过 GitHub 仓库（lechmazur/nyt-connections）和 Reddit 帖子分享，凸显了开源模型在 AI 基准测试上的持续进步。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1scl7pl/extended_nyt_connections_benchmark_scores/)
- **Ollama Cloud 让 OpenClaw 可在 20 美元方案上运行** — Ollama 宣传其云服务是运行 OpenClaw 的最佳选择之一，指出仅需 20 美元的套餐就足以满足日常使用 kimi-k2.5:cloud、glm-5:cloud 和 minimax-m2.7:cloud 等开源模型。帖子包含一个号召行动：通过终端命令 `ollama launch openclaw` 切换到该方案，并提到 The Verge 关于 Anthropic 限制 OpenClaw 访问 Claude、并需额外付费的报道。[来源-twitter](https://x.com/ollama/status/2040261847597867159)
- **Llama-server 在 OpenAI 兼容模式下接入 Gemma-4-26B GGUF** — 该帖子介绍了如何为 llama-server 实例接入 Gemma-4-26B GGUF 模型（ggml-org/gemma-4-26b-a4b-it-GGUF），并以非交互模式运行。配置使用本地 OpenAI 兼容 API `http://127.0.0.1:8080/v1`，自定义 model-id 和 API key，以及明文方式输入密钥，并设置接受风险的选项。[来源-twitter](https://x.com/huggingface/status/2040223333921259699)
- **Onyx 开源 AI 平台主打 RAG 与深度研究** — Onyx 是一个开源 AI 平台，为 LLM 提供应用层和功能丰富的自部署界面。它支持 Agentic RAG、深度研究工作流、自定义 AI agent 和网页搜索，并内置 50+ 即开即用的连接器。项目强调可通过一行 curl 命令轻松部署，并声称截至 2026 年 2 月在深度研究相关排行榜上名列前茅。[来源-github](https://github.com/onyx-dot-app/onyx)
- **Hermes Agent 成为本地模型中最强开源 Agent 候选** — Nous Research 的 Hermes agent 因其对本地模型的优异支持而获赞，包括在 30B 级别模型上仍然有效的按模型划分工具调用解析能力。它原生支持 Ollama、vLLM 和 SGLang，提供包括 Modal 和 Daytona 在内的六种终端后端以便无服务器使用，并为多种消息平台提供单进程网关。自我改进的 Honcho 特性默认关闭，但在通过 config.yaml 启用后会有明显表现；该项目还内置了 OpenClaw 迁移能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1scnevd/hermes_agent_might_be_the_best_open_source_agent/)

### 行业

- **MiniMax 方案支持跨三方 AI Harness 使用** — MiniMax Token 方案被设计为可在第三方 harness 中通用，认为外部生态的 AI 点子将超越实验室内孵化的创意。帖子警告，如果将 AI 订阅限制在自家一方产品，会在创新尚未出现前就将其扼杀。发帖呼吁对外部 AI 使用场景和创意保持开放态度。[来源-twitter](https://x.com/MiniMax_AI/status/2040431340961542460)

## ⚡ 快讯速览

- **Stanford CS153：AI 扩展与算力瓶颈** — 该课程讲解了可扩展 AI 系统的“四大瓶颈”框架，并强调经验验证的重要性。内容讨论了云成本结构的变化、可验证进展与模糊进展的区别，以及芯片短缺和资本开支增长为何阻止算力成为真正的“商品化资源”。[来源-twitter](https://x.com/AnjneyMidha/status/2040294388098814412)
- **AI 赋能公众，提升政府的可见性与问责性** — 有推文认为，在 AI 赋能下，公众可以增强对政府的可见性、可理解性和问责性，从而逆转历史上“治理塑造社会”的单向格局。其指出，虽然政府发布了海量数据，但瓶颈在于处理和洞察，而非获取本身；帖子以大部头法案和 FOIA（信息自由法）回复为例，认为 AI 可以帮助非专业人士理解这些信息。[来源-twitter](https://x.com/karpathy/status/2040549459193704852)
- **中国超大规模 AI 训练中心预示下一场革命** — 一些帖子展示了中国超大规模 AI 训练设施，并指出随着自动化推进，工作岗位安全不再可靠。作者声称“下一场革命”已经在这些训练场中酝酿，预示 AI 能力和劳动力市场将快速变革。[来源-twitter](https://x.com/kimmonismus/status/2040417921378418867)
- **可控视觉表征：用提示引导 ViT 特征** — 像 DINOv2 和 MAE 这样的预训练 Vision Transformer 通常会生成抓取最显著线索的通用图像特征。文章讨论了如何将表征“引导”到较不显眼的概念上，并将其与可通过提示引导的多模态 LLM 做对比：后者虽然可被文本提示控制，但可能会过度偏向语言而丢失纯视觉信息。[来源-huggingface](https://huggingface.co/papers/2604.02327)
- **NVFP4 在 DGX Spark 上六个月仍未交付** — 一位拥有两台 DGX Spark 的 Reddit 用户表示，NVFP4 在购买后六个月仍未得到妥善交付。他指出，原本 Blackwell + NVFP4 配合 NVIDIA 软件栈的本地 AI 方案极具吸引力，但现在 Spark 需要各种变通方式和后端折腾才能正常使用。该产品当初的定位是“完备的高端系统”，而非实验性开发套件，而这次延迟则削弱了这一定位。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1scf1x8/dont_buy_the_dgx_spark_nvfp4_still_missing_after/)
- **Qwen 3.5 vs Gemma 4：谁更胜一筹？** — 一则 Reddit 帖子询问 Qwen 3.5 与 Gemma 4 两个模型谁更强，希望得到明确结论。讨论围绕开源 LLM 展开，邀请社区就性能、基准测试与实际体验给出见解。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1scbpmo/so_qwen35_or_gemma_4/)
- **Apple：极其简单的 Self-Distillation 提升代码生成表现** — 题为“Apple: Embarrassingly Simple Self-Distillation Improves Code Generation”的 Reddit 帖子讨论了一种据称可显著提升代码生成能力的极度简单自蒸馏方法。讨论提及 Apple，并链接至 LocalLLaMA 子版块，将其定位为一项 AI 技术话题。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sc7uwa/apple_embarrassingly_simple_selfdistillation/)
- **传闻 OpenAI 研究员每天跑步路过 Anthropic 办公室；周六出勤成为调侃话题** — 一条 Twitter 帖子声称，一位 OpenAI 研究员每天跑步时都会朝 Anthropic 办公室方向前进，并提到了名为 Gabriel 的人。作者还对 Anthropic 员工周六是否到办公室上班进行揣测。整体内容更像是圈内八卦，而非严肃的 AI 进展更新。[来源-twitter](https://x.com/tenderizzation/status/2040480436665925846)

---

*由 AI News Agent 生成 | 2026-04-04*