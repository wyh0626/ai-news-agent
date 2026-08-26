---
title: "AI 日报 — 2026-08-25"
description: "英国NCSC促AI代理设急停，Apodex与EchoWM推动智能演进。"
lang: "zh"
pairSlug: "ai-daily-2026-08-25"
---

# AI 日报 — 2026-08-25

> 覆盖 25 条 AI 新闻资讯

## 🔥 今日焦点

### 1. 英国国家网络安全中心敦促为 AI 智能体配置紧急关闭开关，警告安全训练可被绕过

英国国家网络安全中心发布了首份关于保护智能体 AI 安全的指南，建议为具备工具访问权限的 AI 智能体配置紧急关闭开关、监督模式和沙箱隔离。该机构明确警告，模型的安全训练是可以被绕过的，这意味着随着智能体获得凭证和企业访问权限，必须通过外部控制来强制执行安全措施。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vxznqe/uks_cyber_agency_just_told_every_company_running/)

### 2. Uber 因算法驱动的司机封禁违反 GDPR 被罚近 10 亿美元

Uber 因算法在未经人工审核的情况下封禁司机，违反了欧盟数据保护规则，被处以近 10 亿美元的 GDPR 罚款。这一处罚凸显了监管机构对自动化决策日益严格的审查，并明确表明对高风险 AI 系统实施有效的人工监督现在已成为法律要求。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vxv8pl/uber_hit_with_a_near1b_gdpr_fine_after_algorithms/)

### 3. EchoWM：全模态世界模型生成 720p 视频与音频

研究人员推出了 EchoWM，一个开放的全模态世界模型，能够从第一人称和第三人称场景的连续导航输入中生成 720p 视频、环境音、音乐和语音。通过将离散命令和连续姿态映射到共享的公制尺度 6 自由度轨迹，该模型指向了新一代可进入的生成式媒体。[来源-huggingface](https://huggingface.co/papers/2608.23189)

## 📰 重点报道

### 智能体 AI 与框架

- **Apodex 1.1 扩展智能体智能以应对复杂工作** — 引入了一个支持模型与文件、代码和数据持续交互的框架，强调通过环境扩展来提高真实世界任务中的可验证性和可靠性。[来源-huggingface](https://huggingface.co/papers/2608.23283)
- **OpenClaw 发布跨平台个人 AI 助手** — 这款开源助手可在 macOS、Linux 和 Windows 上运行，通过单一网关连接模型、工具和消息渠道，支持通过脚本或 npm 轻松安装。[来源-github](https://github.com/openclaw/openclaw)
- **FreeLLMAPI 将 34 个免费 LLM 提供商统一为一个 API** — 将 34 个提供商的免费套餐聚合为 635+ 个模型端点，封装在兼容 OpenAI 的 API 之后，支持智能路由、自动故障转移和加密密钥存储。[来源-github](https://github.com/tashfeenahmed/freellmapi)

### 多模态 AI 与视觉

- **TLive-Omni：面向电商直播的全模态 AI 模型** — 将图像、视频、音频和文本整合到统一的表示空间中，并引入带时间戳的 Per-vGrid 标记，提升了对嘈杂且商品密集的直播电商内容的分析能力。[来源-huggingface](https://huggingface.co/papers/2608.20958)
- **新图像编辑框架以 1200 万数据集攻克概念粒度问题** — 建立了包含 1000+ 细粒度编辑概念的分层分类体系，并发布了 ConceptEdit-12M 数据集，以提高基于扩散模型的编辑器的训练效率和概念处理能力。[来源-huggingface](https://huggingface.co/papers/2608.16812)

### 效率与扩展

- **大规模 MoE 的计算高效超参数迁移** — 一个两步迁移框架可在不同模型规模和 token 预算下估算混合专家模型的最优学习率，大幅降低了极端规模下超参数扫描的成本。[来源-huggingface](https://huggingface.co/papers/2608.20061)

### 开源与教育

- **从零开始学 AI 工程：全面免费的开源课程** — 这门 MIT 许可的课程涵盖 20 个阶段共 511 节课，通过实际的智能体和 MCP 服务器项目，教授使用 Python、TypeScript、Rust 和 Julia 进行 AI 工程开发。[来源-github](https://github.com/rohitg00/ai-engineering-from-scratch)

## ⚡ 快讯速览

- **OpenAI 为 ChatGPT Work 和 Codex 推出管理员插件** — OpenAI 发布了面向 ChatGPT Work 和 Codex 的管理员插件，为组织提供对 AI 使用的更多管理控制权。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vyab8z/openai_adds_an_admin_plugin_for_chatgpt_work_and/)
- **基准测试揭示 LLM 作为评判者在 AI 智能体框架评估中失效** — 一项对 AutoGen、CrewAI、LangGraph 等框架进行测试的新基准发现，LLM 作为评判者的评估方式在比较智能体性能时并不可靠。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vya5ko/i_benchmarked_autogen_crewai_langgraph_and/)
- **ChatGPT、Claude、Gemini 群聊中互相发现对方的幻觉** — 在一项群聊实验中，ChatGPT、Claude 和 Gemini 通过跨模型对话成功发现了彼此的幻觉。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vx1jrm/i_brought_chatgpt_claude_and_gemini_into_a_group/)
- **基于 Claude Code 构建的开源 AI 求职框架** — 一个新的开源框架利用 Claude Code 自动化 AI 辅助的求职工作流程。[来源-github](https://github.com/MadsLorentzen/ai-job-search)
- **Claude-Obsidian：开源 AI 第二大脑知识管理工具** — 一个开源集成将 Claude 变成连接 Obsidian 的 AI 驱动第二大脑，用于知识管理。[来源-github](https://github.com/AgriciDaniel/claude-obsidian)
- **被 AI 取代的开发者打造开源 AI CEO** — 在一名 CEO 解雇开发者以便为 AI 腾出位置之后，这些开发者构建了一个开源的 AI CEO 替代方案。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vyegah/ceo_fired_developers_to_make_room_for_ai/)
- **卡车司机用 Claude Code 构建 AI 新闻聚合器** — 一名卡车司机使用 Claude Code 构建了一个 AI 新闻聚合器，展示了低代码 AI 工具正在降低开发门槛。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vycupz/truck_driver_builds_ai_news_aggregator/)
- **利用伪随机生成器绕过 AI 水印** — 研究人员证明，基于伪随机生成器的提示词操纵可以规避 AI 水印检测。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vybcrs/dribbling_the_ai_watermark_directly_inprompt/)
- **共享记忆的公共 AI 从对话中进化** — 一项新实验让所有人都可以与共享记忆的同一 AI 实例对话，使其能够基于集体对话不断进化。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vxxeef/i_built_an_ai_where_everyone_talks_to_the_same/)
- **GenOS 基因组驱动智能体环境修复提示词膨胀问题** — GenOS 为 LLM 智能体采用基因组驱动环境，据称可以修复多智能体工作流中的提示词膨胀问题。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vy43mo/i_tested_my_genos_for_llm_agents_it_fixed_prompt/)
- **UNDP 与 DFINITY 合作推进主权云和去中心化 AI** — 联合国开发计划署与 DFINITY 基金会正在就主权云基础设施和去中心化 AI 解决方案展开合作。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vy06hp/undp_and_dfinity_foundation_collaborate_on/)
- **Claude AI 个性化记忆丢失** — 用户报告称 Claude 的定制化记忆被清空，引发了对个性化 AI 记忆功能持久性和可靠性的担忧。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vy55oi/my_claude_got_its_memory_wiped/)
- **开发者在 .NET 中使用 ONNX 进行语音转文本遭遇挑战** — 一位开发者指出了在 .NET 中使用 ONNX 进行语音转文本的实际困难，包括兼容性和性能问题。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vxqw62/onnx_for_speech_to_text/)
- **6000 欧元预算：AI 开发选 MacBook Pro 还是 NVIDIA 笔记本** — 社区就 6000 欧元的便携 AI 开发设备应优先选择 MacBook Pro 还是 NVIDIA 笔记本展开讨论，聚焦 GPU 性能与统一内存之间的权衡。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vxxrqj/for_a_6k_portable_aidevelopment_setup_prioritize/)
- **AI 视频生成模型仍有很长的路要走** — 新测试显示，当前的 AI 视频生成模型在处理复杂场景时仍远未达到可投入生产的水平。[来源-reddit](https://www.reddit.com/r/artificial/comments/1vxle74/ai_video_generation_models_still_have_a_long_way/)

---

*由 AI 新闻智能体生成 | 2026-08-25*