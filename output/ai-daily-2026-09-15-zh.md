---
title: "AI 日报 — 2026-09-15"
description: "ViduS2实时720p视频；Atria科研智能体；ZGCM-1开放数学搜索"
lang: "zh"
pairSlug: "ai-daily-2026-09-15"
---

# AI 日报 — 2026-09-15

> 涵盖 25 条 AI 新闻

## 🔥 今日焦点

### 1. Apple Foundation Models 现已在 macOS 27 上原生运行

据报道，Apple 已让其 Foundation Models 在 macOS 27 上原生可用，使用户能够直接在 Terminal 中运行 `fm chat`。这是 Apple 硬件上本地 AI 的重要一步，使开发者更容易测试和构建不依赖云端的隐私保护应用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wh5fpa/apple_foundation_models_local_ai_natively_on/)

### 2. Alibaba 开源 Open Code Review AI 代码审查工具

Alibaba 发布了 Open Code Review，这是一个 AI 驱动的 CLI，将确定性流水线与 LLM 智能体相结合，读取 Git diff 并生成精确的行级评论。该工具支持多语言安全规则以及 OpenAI/Anthropic 兼容模型，并在发布前于 Alibaba 规模内部经过实战检验。 [来源-github](https://github.com/alibaba/open-code-review)

### 3. Vidu S2 实现实时 720p 交互式与可编辑视频生成

Vidu S2 推出了用于实时交互式数字角色的 Vidu S2-Avatar 和用于实时视频编辑的 Vidu S2-Editing，同时探索实时空间视频生成。它在 Vidu S1 基础上改进了 720p 输出、动态参考和更强的指令遵循能力，指向响应更迅速、更可编辑的生成式媒体流水线。 [来源-huggingface](https://huggingface.co/papers/2609.11638)

## 📰 重点报道

### 开源模型与智能体研究

- **Atria Dawn Preview：面向科学研究的智能体 LLM** — 一个通过可验证经验流水线训练的基础智能体模型，该流水线将工具介导的交互与可执行环境相连接，目标是提升现实世界的科学与工程生产力。 [来源-huggingface](https://huggingface.co/papers/2609.15818)
- **ZGCM-1：面向数学与智能体搜索的完全开放 7B 基础模型** — 一个从零训练的 7B 稠密模型，具有 256K 上下文，将审慎的内部思考与主动的外部工具使用相结合，并附带端到端开放训练方案发布。 [来源-huggingface](https://huggingface.co/papers/2609.13356)
- **Dream-RSI：通过演化世界实现递归自我改进** — 一种新方法，让自主智能体在延迟反馈下改进探索策略，旨在实现跨复杂搜索空间的递归自我改进。 [来源-huggingface](https://huggingface.co/papers/2609.14858)
- **PhysBrain 1.5 将视觉语言模型与物理基础模型相连接** — 一个统一的自回归模型，编码语言响应、末端执行器运动和稠密视觉目标，以理解物理环境并预测未来状态。 [来源-huggingface](https://huggingface.co/papers/2609.14973)

### 语音与多模态系统

- **OpenBMB 发布支持 30 种语言的 VoxCPM2 无分词器 TTS** — 一个基于 MiniCPM-4 构建的 2B 参数无分词器 TTS 系统，在超过 200 万小时的多语言语音上训练，支持语音设计、可控克隆和 48kHz 录音室级音频。 [来源-github](https://github.com/OpenBMB/VoxCPM)

### 智能体工具

- **Agent Reach CLI 让 AI 智能体零成本访问 Twitter、Reddit、YouTube** — 一个开源 CLI，让智能体无需付费 API 费用即可在 Twitter、Reddit、YouTube、GitHub、Bilibili 和 XiaoHongShu 上浏览和搜索。 [来源-github](https://github.com/Panniantong/Agent-Reach)

### 行业与信任

- **CrofAI 被曝为 OpenRouter 包装器，在欺诈指控后关停** — 一家声称提供廉价自定义引擎 token 的推理提供商，据称将请求路由到更便宜的模型并加价高达 20 倍，随后在欺诈指控后抹除了其线上存在。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wgwe4n/crofai_cheapest_inference_provider_in_the_world/)

## ⚡ 快讯速览

- **TradingAgents 发布 v0.4.0 多智能体 LLM 交易框架** — 多智能体 LLM 交易框架的新版本增加了更新的编排和研究能力。 [来源-github](https://github.com/TauricResearch/TradingAgents)
- **UkisAI 的 Swift-Qwen3.8-27B 将推理 token 减少 40%** — 据报道，一个经过调优的 Qwen3.8-27B 变体将推理 token 使用量减少了 40%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wh5elt/cut_qwen3827b_reasoning_tokens_by_40_38/)
- **ByteShape 发布 Qwen 3.8 27B ShapeLearn GGUF 量化版本** — 面向 Qwen 3.8 27B 的新 GGUF 量化版本聚焦于 ShapeLearn 质量权衡。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wh21e9/byteshape_qwen_38_27b_to_kl_diverge_or_not_to_kl/)
- **Voodoo 动态量化方法以 MIT 许可证发布** — 一种面向本地 LLM 的动态量化方法现已在宽松的 MIT 许可证下可用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wgszma/voodoo_dynamic_quant_now_mit_licensed/)
- **IFM/K2-Horizon-7B 在 16GB VRAM 上完成基准测试，落后于 Qwen3.8-27B** — 一项在 16GB VRAM 上进行的 7B 模型基准测试显示出有竞争力的本地性能，但仍落后于 Qwen3.8-27B。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wha6sv/i_benchmarked_ifmk2horizon7b_on_16gb_vram/)
- **MiroFish：面向多智能体预测的通用群体智能引擎** — MiroFish 提供了一个面向多智能体预测任务的群体智能引擎。 [来源-github](https://github.com/666ghj/MiroFish)
- **Qwen3.8-27B-NVFP4 通过 vLLM 以 1M 上下文提供服务** — 一名用户报告使用 vLLM 成功以 1M 上下文服务 Qwen3.8-27B-NVFP4。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wh4gai/qwen3827bnvfp4_1m_context_so_far_so_good/)
- **Accio Lab 发布 Occamy-1.0** — Accio Lab 发布了 Occamy-1.0，一个引起社区关注的新本地模型发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wgz8fo/occamy10_by_accio_lab/)
- **Nvidia RTX 5090 从美国零售渠道消失，黄牛标价 9,500 美元** — RTX 5090 在美国线上零售中的供应已枯竭，黄牛挂牌价达到 9,500 美元。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wgeo55/nvidias_rtx_5090_vanishes_from_online_retail_in/)
- **oh-my-hermes 插件为 Hermes Agent 增加记忆与工作流层** — 一个新插件为 Hermes Agent 提供持久记忆和工作流编排功能。 [来源-github](https://github.com/rlaope/oh-my-hermes)
- **RuView 利用 WiFi 信号进行空间感知与生命体征监测** — RuView 探索基于 WiFi 信号的空间感知和生命体征监测，无需专用传感器。 [来源-github](https://github.com/ruvnet/RuView)
- **用户在 Craigslist 上以 4K 美元买到未拆封的 NVIDIA DGX Spark** — 一名本地 AI 爱好者以 4,000 美元二手购入了一台未拆封的 NVIDIA DGX Spark。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wh2cga/got_it_unopened_off_craigslist_for_4k_excited_to/)
- **Flash Next Q2 在本地网页游戏开发中优于 Gemini Flash 3.8** — 一名开发者报告称，Flash Next Q2 在本地网页游戏开发任务中胜过 Gemini Flash 3.8。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1whbhty/for_web_game_development_i_swear_flash_next_on_q2/)
- **KoboldCpp v1.121 发布，用于本地 LLM 推理** — KoboldCpp v1.121 已发布，为本地 LLM 推理工作流带来更新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wh4cg9/koboldcpp_v1121_released/)
- **r/LocalLLaMA 开设双周项目展示集中帖** — 该 subreddit 开设了一个双周集中帖，用于社区项目展示。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1wgcpww/biweekly_megathread_project_showcase/)

---

*由 AI News Agent 生成 | 2026-09-15*