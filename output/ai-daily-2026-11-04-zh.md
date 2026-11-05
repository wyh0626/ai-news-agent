---
title: "AI 日报 — 2026-11-04"
description: "65B稠密模型、Qwen精度提升10–15%、35B智能体基座同日发布。"
lang: "zh"
pairSlug: "ai-daily-2026-11-04"
---

# AI 日报 — 2026-11-04

> 涵盖 19 条 AI 新闻

## 🔥 今日焦点

### 1. Ricursive Intelligence 发布 Ripple-65B-Preview 稠密开放权重模型

Ricursive Intelligence 发布了 Ripple-65B-Preview，这是一款稠密的 65B 开放权重模型，采用 80 层薄而深架构、混合注意力，并进行了轻量后训练，重点面向智能体编程。该实验室声称其能与 Muse Spark Open 和 Reflection 的 Beam 等更大模型互有胜负，这使其成为稠密模型效率对阵更大规模或混合式系统的一项重要测试。如果这些说法成立，它将扩大面向智能体编程和本地部署的竞争性开放权重层级。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xo2arv/ricursive_intelligence_ripple65bpreview_new_dense/)

### 2. Kimi-K3.1-Pro 作为开放权重模型发布

根据 r/LocalLLaMA 的一篇帖子，Kimi-K3.1-Pro 现已作为开放权重模型提供，为本地和自托管部署又增加了一个高关注度选项。该公告提供的技术细节有限，因此实际影响将取决于许可条款、权重可用性和独立基准测试。它也正值社区对开放模型基准声明加强审视之际，这使得可复现性尤为重要。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnrhvb/kimik31pro_is_now_openweights/)

### 3. Axion 1.0：完全开放的 35B 智能体基础模型，训练配方简洁

Axion 1.0 是一个完全开放的 35B 智能体基础模型，采用紧凑的三阶段配方训练：两个监督微调阶段后接强化学习。它避免了专门的中期训练、DPO 和同策略蒸馏，使用模型感知的数据构建和可自动验证任务来构建推理与工具使用能力。该发布为研究简单、面向智能体的后训练流水线的团队提供了可复现基线。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnjiu4/axion10axion1035b_hugging_face/)

## 📰 重点报道

### 模型优化与量化

- **Unsloth 为 Qwen3.8-Flash-Next 发布 Dynamic v3.1 GGUF，准确率提升 10-15%** — 新的量化方案声称在智能体基准上相较 GSQ-RCO 带来 10–15% 的准确率提升，并新增跨 BF16/Q8_0/Q5_1/IQ4_NL 的 engram 切换；该发布对本地部署和可复现的智能体评估意义重大。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnvbxn/new_qwen38flashnext_unsloth_dynamic_v31_ggufs/)

### AI 系统与路由

- **Route Anything：面向通用 AI 系统的模型与策略路由** — 该论文将跨专用模型、工具和策略的动态路由视为通用 AI 的核心机制；它指向编排层，而非单模型扩展。 [来源-huggingface](https://huggingface.co/papers/2611.05275)

### 高效推理

- **LoCo 使用本地偏好学习压缩推理** — LoCo 就何时无需进一步链式思维推敲做出步级决策，目标是在不进行轨迹级压缩的情况下降低推理成本；它可能有助于平衡推理质量与延迟。 [来源-huggingface](https://huggingface.co/papers/2611.04814)

### 多模态与视频

- **MoviEdit 实现可扩展的长篇多镜头视频编辑** — MoviEdit 是一个端到端框架，用于连贯的长篇、多镜头视频编辑，并配有可扩展的跨镜头监督流水线；它解决了复杂视频工作流中的数据、建模和评估缺口。 [来源-huggingface](https://huggingface.co/papers/2611.02737)
- **Kling 报告将视频生成质量与多模态理解联系起来** — Kling 认为视频生成质量取决于跨数据、条件控制、对齐和评估的多模态理解，并在分析中引入了 Kling-MLLM；该报告强调评估是视频模型的瓶颈。 [来源-huggingface](https://huggingface.co/papers/2611.04916)

### 开发者工具与智能体

- **Spotify 为 Claude Code、Codex、Cursor 发布 Portal AI 插件** — Spotify 的 Portal AI 插件将身份验证、目录搜索、简报、诊断和安全的 Portal 操作带入编程智能体，另有一个仅限 Claude Code 的路由插件 shunt；这表明智能体工具正走向打包式企业工作流。 [来源-github](https://github.com/spotify/portal-ai-plugins)

### 端侧与模型压缩

- **裁剪 Gemma 26B-A4B 至 15% 大小，仍保留 92% 任务准确率** — 一位开发者将 MoE Gemma 模型转换为稠密的 15% 大小变体，在狭窄分类任务上保持 92% 一致性，并在 Mac 上以 79 tokens/s 运行；代价是丢失通用知识，因此仅适合有针对性的端侧使用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnoqyy/i_removed_85_of_gemmas_weights_and_it_is_mostly/)

## ⚡ 快讯速览

- **DeepSeek 占 OpenRouter token 的 53%；开放权重实验室超过 75%** — 开放权重模型如今主导 OpenRouter token 份额，仅 DeepSeek 一家就达 53%，开放权重实验室合计超过 75%，表明其生产采用强劲。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnz8ct/deepseek_alone_accounted_for_53_of_all_27/)
- **Revolut 用自托管模型替代 Claude，将 AI 编程成本降低 10 倍** — 据报道，这家金融科技公司通过从 Claude 转向自托管模型，将 AI 编程成本降低 10 倍，凸显本地部署背后的成本压力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xn568h/british_fintech_revolut_slashes_ai_coding_costs/)
- **Pandora 用自不透明表达模拟心理治疗来访者** — Pandora 模拟内部状态并非完全透明的心理治疗来访者，旨在改进临床 AI 智能体的训练与评估。 [来源-huggingface](https://huggingface.co/papers/2611.00617)
- **基于 Playwright 的开源 AI 闲鱼市场监控器发布** — 一个新的基于 Playwright 的开源监控器使用 AI 跟踪闲鱼市场商品列表，显示出细分消费工作流持续被智能体自动化。 [来源-github](https://github.com/Usagi-org/ai-goofish-monitor)
- **Reddit 帖子称 Kimi K3.1 存在基准刷分嫌疑，并引用审计** — 一项社区审计指称 Kimi K3.1 的基准结果可能针对排行榜表现进行了优化，强化了对开放模型评估的审视。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnu6y1/kimi_k31_is_likely_benchmaxxed_with_some_proof/)
- **LFM3-Omni-2B 通过 WebGPU 在 iPhone 上以 80 Tok/s 离线运行** — 据报道，LFM3-Omni-2B 通过 WebGPU 在 iPhone 上以 80 tokens/s 完全离线运行，指向更快的浏览器内和端侧多模态推理。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xntou1/lfm3omni2b_running_fully_offline_on_my_iphone_18/)
- **Hy4 AI 模型公布，开放权重即将发布** — 一个新的 Hy4 AI 模型已公布，并承诺很快开放权重，为即将发布的开放模型阵容再添一员。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnhzbz/introducing_hy4_open_weights_soon/)
- **Reflection 产品团队就开放权重 Beam 501B 模型举行 AMA** — Reflection 的产品团队正在就其开放权重 Beam 501B 模型举行 AMA，为从业者提供直接了解大型开放权重系统的机会。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xmwryg/were_the_product_team_at_reflection_the_lab/)
- **用户在旧笔记本上以低于 1 Token/s 运行 Qwen3 27B Q4** — 一位用户报告在一台低端笔记本上以低于 1 token/s 运行 Qwen3 27B Q4，说明尽管有量化，本地推理仍存在实际限制。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xnzo38/qwen38_27b_q4_on_my_lowend_laptop_and_it_became/)

---

*由 AI 新闻代理生成 | 2026-11-04*