---
title: "AI 日报 — 2026-05-05"
description: "GPT-5.5提升回复，Grok4.3加速，Heretic1.3发布基准。"
lang: "zh"
pairSlug: "ai-daily-2026-05-05"
---

# AI 日报 — 2026-05-05

> 覆盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. GPT-5.5 Instant 登陆 ChatGPT，回复更聪明、更温暖

OpenAI 开始在 ChatGPT 中逐步上线 GPT-5.5 Instant，带来更智能、更清晰、更个性化的回答，同时语气更加自然、温暖。此次更新还根据用户反馈，特别强调在保证信息量的前提下控制回复长度，更加简洁凝练。[来源-twitter](https://x.com/OpenAI/status/2051709028250915275)

### 2. Grok 4.3 登陆 xAI API，号称迄今最快模型

Grok 4.3 现已在 xAI API 上线，被宣传为目前速度最快、能力最强的模型。它在 ArtificialAnlys 榜单中，工具调用与指令跟随的智能体能力位居前列，并在 ValsAI 的企业领域（如判例法和公司金融）中排名第 1。该模型支持 100 万 token 的上下文窗口，定价为输入每百万 token 1.25 美元、输出每百万 token 2.50 美元。[来源-twitter](https://x.com/xai/status/2051703217697010103)

### 3. Heretic 1.3 发布，引入可复现模型与集成评测系统

Heretic 1.3 现已发布，带来可复现的模型、内置基准测试系统、更低的峰值显存占用以及更广泛的模型支持。此次版本在分叉项目众多的生态中强调透明性，提到项目已获得约 2 万 GitHub star 和 1300 万次总下载量，并点名某竞争者疑似使用抄袭的 Heretic 分叉版本。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4hwup/heretic_13_released_reproducible_models/)

## 📰 重点报道

### LLMs

- **DeepSeek V4 Pro 在 FoodTruck Benchmark 上追平 GPT-5.2** — DeepSeek V4 Pro 参与了为期 30 天的 FoodTruck Bench 测试，这是一个包含 34 个工具、支持记忆的智能体任务集，在表现上与 Grok 4.3 打平，并且与 GPT-5.2 的中位数成绩仅差 3%。在 GPT-5.2 发布十周后，这标志着中美前沿模型差距进一步缩小，同时 DeepSeek 相比 GPT-5.2 提供约 17 倍的成本优势（单元价 0.435/0.87 对 GPT-5.2）。这是首个进入“前沿梯队”的中国模型，凸显了智能体型 AI 在性能与成本效率上的快速进步。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t47qbw/deepseek_v4_pro_matches_gpt52_on_foodtruck_bench/)
- **llama.cpp 在 Strix Halo 上支持 MTP（PR 22673）** — Reddit 用户 Edenar 报告在 AMD Strix Halo 环境下测试 llama.cpp 的 MTP 支持。他们重构了 amd-strix-halo-toolboxes，并结合 PR 22673，搭配 GGUF 版本的 Qwen3.6-35BA3B-MTP-GGUF，启用了 --spec-type mtp 和 --spec-draft-n-max 3，使用 MTP 时可达到约 60–80 tokens/s，而未启用时约为 40 tokens/s。帖子指出相关 GGUF 文件体积相近（各约 36 GB），作者计划继续尝试 Qwen 3.5 122B，并称测试结果相当惊艳。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4uj9h/mtp_on_strix_halo_with_llamacpp_pr_22673/)

### LLM

- **Claude 推出金融服务领域的即用型智能体模板** — Claude 发布了面向金融行业的即用型智能体模板，支持路演撰写、估值复核、月末关账等任务。这些模板可以作为插件安装到 Cowork 和 Claude Code 中，或通过 cookbook 以 Managed Agents 方式直接用于生产环境。本次更新体现了 Claude 在企业级金融工作流工具集方面的持续扩张。[来源-twitter](https://x.com/claudeai/status/2051679629488865498)
- **Gemma 4 借助多 token 草稿推理实现 3 倍加速** — Google 的 Gemma 4 模型通过引入 Multi-Token Prediction Drafters（MTP drafters），最高可实现约 3 倍推理加速。该方法允许 Gemma 4 一次性预测多个 token，在不明显牺牲生成质量的前提下显著提升输出速度。该消息由 Google 面向开发者的 X（Twitter）频道发布。[来源-twitter](https://x.com/googledevs/status/2051700498328346945)
- **OpenAI 将 Codex 速率限制提高 10 倍，社区用户欢呼** — 用户 Arav Jain 在推文中称赞 OpenAI 开发者，将 Codex 的速率限制提升了 10 倍，引发了开发者群体的强烈兴奋。帖子将这一调整视为对编码类任务的重大利好，反映了社区对 AI 开发工具升级的积极反应。[来源-twitter](https://x.com/sama/status/2051464155094507902)
- **正确打开方式：把 Qwen3.6 接到 Pi coding agent 上** — 一位 Reddit 用户分享称，将 Qwen3.6 35B 与 Pi coding agent、exa 网络搜索以及 agent-browser 扩展组合使用，大幅改善了写代码、维护代码和网页调研的体验。作者声称这一组合覆盖了自己约 80% 的使用场景，在网络检索方面甚至可以超越 Perplexity，而更复杂的规划则交由 Kimi2.6 处理。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4ji36/use_qwen36_right_way_send_it_to_pi_coding_agent/)
- **在 Google TPU 上用扩散风格推测解码，实现 3 倍 LLM 推理加速** — Google Developers Blog 介绍了一种在 Google TPU 上加速 LLM 推理的技术，利用类似扩散模型的推测式解码，整体性能可提升约 3 倍。该方法通过扩散启发式方式预测 token，减少计算量与延迟，使基于 TPU 的生成式工作负载能显著提速。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4jehc/supercharging_llm_inference_on_google_tpus/)

### Multimodal

- **Hermes Agent 借助 HeyGen HyperFrames 生成完整视频** — Hermes Agent 现在可以利用 HeyGen 官方的 HyperFrames 技能生成完整视频。HyperFrames 视频原生基于 HTML，使智能体可以对最终输出进行全流程控制，并支持 HLS 流式播放。[来源-twitter](https://x.com/NousResearch/status/2051697780985368921)
- **Map2World 支持按分割图约束的 3D 世界生成** — Map2World 提出一种 3D 世界生成框架，可依据用户自定义的分割图进行条件控制，这些分割图可具有任意形状和尺度。该方法旨在克服以往方法中网格布局约束及尺度不一致的问题，从而生成在全球一致性上更好的三维场景。这一工作推动了 AI 驱动的 3D 内容生成，在沉浸式内容创作与自动驾驶仿真等方面具有潜在价值。[来源-huggingface](https://huggingface.co/papers/2605.00781)

### Open Source

- **MolmoAct2：面向真实部署的开放动作推理模型** — MolmoAct2 被提出为一个完全开源、针对实际部署优化的动作推理模型，面向 Vision-Language-Action（VLA）机器人系统。作者指出，当前前沿模型大多封闭或成本高昂，而加入复杂推理的策略在延迟上难以接受，MolmoAct2 旨在提供一个可用性强、易部署的替代方案。此项工作希望推动开源具身智能在真实世界场景中的落地应用。[来源-huggingface](https://huggingface.co/papers/2605.02881)

### AI Benchmarking

- **ProgramBench：用 AI 智能体从零重建大型二进制程序** — ProgramBench 构建了一个包含 200 个任务的基准集，要求 AI 智能体仅凭目标可执行文件和使用示例文件，从零构建完整程序，且禁止访问互联网和使用反编译。该基准测试语言选择、架构设计以及软件工程决策，并配备了 600 万行自动生成的行为测试代码，经过质量过滤。项目已开源其 GitHub 仓库、Hugging Face 资源及 Docker 镜像，所有结果发布在 programbench.com。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4j4s9/programbench_can_we_really_rebuild_huge_binaries/)

### Voice Cloning

- **OmniVoice 实现一键式一段样本声音克隆，用户直呼震撼** — 一篇 Reddit 帖子称赞 OmniVoice 实现了一次录音（one-shot）即可完成声音克隆，而且使用过程极其简单。作者表示效果“简直就是我梦寐以求的一切”，尽管强调这并不是一个 LLM，但仍对其语音克隆性能印象深刻。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4rst5/i_know_this_isnt_technically_an_llm_but_omnivoice/)

### AI Safety

- **美国与科技企业达成协议：新 AI 模型发布前先进行国家安全审查** — 美国政府与多家科技公司达成协议，将在 AI 模型向公众发布之前，对其可能引发的国家安全影响进行审查。该安排旨在在新系统部署之前，确保安全性并满足相关监管要求。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4tj11/us_and_tech_firms_strike_deal_to_review_ai_models/)

## ⚡ 快讯速览

- **高效 AI 模型引发对 Codex–Claude 迁移的担忧** — 帖子指出相较其能力，这些 AI 模型的效率极高，并对 Codex 的调用上限表示担心。作者认为 Claude 迁移到 Codex 的阶段是刻意营造的“蜜月期”，警告未来可能出现“地毯式撤走”（rugpull）的风险。[来源-twitter](https://x.com/sama/status/2051670144842395990)
- **Sama 寻找基于 5.5 模型和超大 token 预算的 AI 壮举案例** — Sam Altman 使用 @sama 账号发帖，征集在假想的 5.5 模型上构建的、在旧版本上无法实现的令人印象深刻的应用案例。帖子特别强调那些依赖“极大 token 预算”的用例，希望听到通过扩展上下文长度而解锁的新能力故事。[来源-twitter](https://x.com/sama/status/2051724685231214650)
- **Web2BigTable：面向互联网规模检索的双层多智能体 LLM 框架** — Web2BigTable 提出一种双层、多智能体的 LLM 框架，用于可扩展的“Web 到表格”检索。它面向长搜索链路中的深度推理，并在跨异构数据源时进行结构化、与模式对齐的聚合，力图同时解决智能体式网页检索中的广度与深度挑战，用于信息抽取。[来源-huggingface](https://huggingface.co/papers/2604.27221)
- **CocoIndex：面向长程智能体的增量式上下文引擎** — CocoIndex 提供一个增量式引擎，将多种数据源（代码库、笔记、收件箱、Slack、PDF 和视频等）转化为 AI 智能体与 LLM 应用的实时、最新上下文，仅对增量部分重新计算。其目标是通过并行处理与 Python 工具链，快速交付可用于生产环境的 AI 智能体。项目已在 cocoindex-io/cocoindex 开源，并每周更新示例。[来源-github](https://github.com/cocoindex-io/cocoindex)
- **本地跑 LLM：5 天 2 亿 tokens，算一算 ROI** — 一篇 Reddit 帖子介绍在本地使用 Qwen-397b，部署在 2-Spark 集群上，并用 Hermes 统计 token，在五天内跑到了 2 亿个 token。作者以每百万 token 1.25 美元的价格估算，认为每月可产生约 1250 美元“价值”，硬件回本周期大致在六个月左右，同时也提醒需要考虑成本与替代方案等前提条件。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4qwzf/why_run_local_count_the_money/)
- **26B 本地大模型在 CPU 上也能跑得飞快，无需 GPU** — 一位 Reddit 用户报告在一台仅配备 CPU 的本地机器（i5-8500 + 32GB 内存）上运行 Gemma4 26B，推理速度表现令人惊讶，无需 GPU 即可流畅使用。帖子还提到 12B 级别模型在同一配置上表现同样出色，凸显了在无 GPU 环境下进行大模型本地推理的可行性。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1t4e046/running_a_26b_llm_locally_with_no_gpu/)
- **语言模型能从上下文中习得技能吗？** — 文章指出，语言模型往往需要在超出其参数记忆范围的上下文中进行推理。作者提出“上下文学习”和“推理阶段技能增强”两种思路，用以将上下文中的规则转化为自然语言形式的技能，并提到至少两个主要挑战，其中之一是对上下文学习而言，手工标注技能成本过高。[来源-huggingface](https://huggingface.co/papers/2604.27660)
- **对语音模型重塑人机交互方式感到兴奋** — 帖子表达了对语音模型逐渐成熟的兴奋之情，指出人们已经在改变与 AI 交互的方式。这预示着语音将成为与 AI 互动的一种主要形态，语音驱动的 AI 使用场景将得到更广泛的普及。[来源-twitter](https://x.com/sama/status/2051464865634742334)

---

*由 AI News Agent 生成 | 2026-05-05*