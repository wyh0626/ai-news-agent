---
title: "AI 日报 — 2026-10-08"
description: "Cua开源计算机代理工具，Swift模型下载破220万，一人用AI入侵韩国银行。"
lang: "zh"
pairSlug: "ai-daily-2026-10-08"
---

# AI 日报 — 2026-10-08

> 覆盖 22 条 AI 新闻

## 🔥 今日焦点

### 1. Cua 以开源驱动和基准测试开放计算机使用智能体

Cua 发布了一个开源技术栈，使 AI 智能体能够在 Mac 和其他自有机器上获得完整桌面，包括用于桌面自动化的 Cua Driver、用于本地虚拟机的 Lume、CUA-S1 决策模型以及 Cua Bench。通过将驱动、虚拟机、模型和评估打包到一个平台中，它降低了跨操作系统构建和基准测试计算机使用智能体的门槛。 [来源-github](https://github.com/trycua/cua)

### 2. Swift 开源推理 LLM 下载量突破 220 万次

UkisAI 的 Swift 模型下载量已突破 220 万次；它们将 token 使用量减少 58.3%，速度提升 1.95 倍且不损失准确率，主要方式是对病态过度思考进行惩罚。该团队还宣布新模型开放早期访问，并向研究人员提供免费算力，进一步证明高效推理模型在本地和生产部署中的价值。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0ui6f/thank_you_swift_models_hit_22_million_downloads/)

### 3. 单一攻击者利用开源 AI 技术栈入侵韩国银行

据 CrowdStrike 称，韩国最大的几家银行据报遭到网络攻击，攻击由一个人使用开源 AI 渗透工具 ARTEX 以及 DeepSeek v4.1-Flash、GLM-5.3、Grok 4.6 和 Claude Code 实施。该事件凸显了易于获取的 AI 工具如何降低高影响力网络攻击所需的技术和资源门槛，从而加大防御方采用 AI 辅助安全工作流的压力。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0n4pt/last_week_some_of_south_koreas_biggest_banks_were/)

## 📰 重点报道

### 高效推理与硬件

- **STEPQuant：线性注意力中循环状态的误差感知量化** — STEPQuant 按循环状态中的时间和空间维度区分量化误差，从而在不过度降低准确率的情况下实现更低精度的线性注意力服务。 [来源-huggingface](https://huggingface.co/papers/2609.38169)
- **2,800 美元的 8x Radeon Pro V620 主机构建通过自定义 vLLM 分支运行 LLM** — 一个使用八块 Radeon Pro V620 显卡、配备 256 GB VRAM 的装机方案，在自定义 vLLM 分支解决 RDNA2 内核限制后，达到 60–100 tokens/s 解码和 3000+ tokens/s 预填充。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0wnz1/2800_rig_with_8x_radeon_pro_v620_256_gb_vram/)

### 多模态与生成研究

- **GRACE：面向高效视频生成的生成感知潜在压缩** — GRACE 通过生成感知潜在压缩减少视频扩散 Transformer 处理的 token 数，针对重建质量、通道增长、收敛变慢和预训练潜在不匹配问题。 [来源-huggingface](https://huggingface.co/papers/2610.10524)
- **UltraText Bench：图像生成中视觉文本渲染的双语基准** — UltraText Bench 提供 432 个人工审查提示词，覆盖 24 个真实场景类别和三个难度级别，英文和中文各占一半。 [来源-huggingface](https://huggingface.co/papers/2610.09823)
- **VepAgent 使用工具增强 RL 进行视频事件预测** — VepAgent 将因果转换推理与工具增强强化学习相结合，帮助多模态 LLM 预测视频中未观察到的因果转换。 [来源-huggingface](https://huggingface.co/papers/2610.06293)
- **UniWAM 集成物理推理器、世界生成器和动作预测器** — UniWAM 通过物理推理器、世界生成器和动作预测器，将语义 VLA 推理与时空世界模型先验统一起来。 [来源-huggingface](https://huggingface.co/papers/2610.02054)

### AI 安全与智能体工具

- **Cloudflare 为编码智能体发布安全审计技能** — Cloudflare 的 security-audit-skill 使用隔离智能体、验证和独立核实的发现，运行结构化六阶段审计，用于全机群漏洞发现。 [来源-github](https://github.com/cloudflare/security-audit-skill)

## ⚡ 快讯速览

- **六个 AI 决策模型玩 Pac-Man，开源排行榜发布** — 六个 AI 决策模型在 Pac-Man 中竞争，并配有开源排行榜，用于可复现的智能体评估。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0sm1b/jevman_ai_decision_models_play_pacman/)
- **RTX 4090 对四个开放决策模型进行基准测试** — 一项本地 RTX 4090 测试对四个开放决策模型的性能和决策质量进行了基准测试。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0wg85/running_decision_model_locally_on_an_rtx_4090_to/)
- **audio.cpp 更新：Higgs TTS 的 VRAM 减少 48%，模型更快** — audio.cpp 更新将 Higgs TTS 的 VRAM 使用量降低 48%，同时加速多个受支持模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0q91x/audiocpp_recent_updates_you_might_have_missed/)
- **JetBrains 发布 Mellum2.1 小型 MoE 思考 GGUF 模型** — JetBrains 在其 Mellum2.1 集合中新增一个小型 MoE 思考 GGUF 模型，用于本地推理工作负载。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0u6l7/mellum21_a_jetbrains_collection/)
- **Saluki 27B 声称以 1/7 的规模达到 Qwen 3.8 约 96% 的性能** — Saluki 27B 声称在模型规模仅为七分之一的情况下，达到 Qwen 3.8 约 96% 的性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0mn7x/saluki_27b_96_of_qwen_38s_performance_at_17_the/)
- **LittleBit 通过潜在因子分解实现超低位量化** — LittleBit 为超低位 LLM 部署引入潜在因子分解量化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0sa6g/250613771_littlebit_ultra_lowbit_quantization_via/)
- **土耳其语 TTS 在 RTX 5090 上使用 Drifting 方法从零训练** — 一个土耳其语 TTS 模型使用 Drifting 方法在单张 RTX 5090 上从零训练。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0oaum/i_trained_turkish_tts_from_scratch_using_the/)
- **Strata 重写 GitHub 历史以抹去 Claude 共同作者证据** — 据报道，Strata 重写了其 GitHub 历史，以删除 Claude 共同撰写更改的证据。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x15a8w/strata_rewrote_their_github_history_to_wipe/)
- **Nvidia CMP 170HX 显卡据报可将 VRAM 从 40GB 解锁至 48GB** — 用户报告称，可将 Nvidia CMP 170HX 显卡的 VRAM 从 40 GB 解锁至 48 GB，用于 AI 任务。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x0rjzb/attn_cmp170hx_10gb_card_owners_unlock_from_40gb/)
- **小众 Hugging Face 微调模型 VeriLoop-E2 在代码库中表现成功** — 据报道，小众 Hugging Face 微调模型 VeriLoop-E2 在代码库任务中表现出很高的成功率。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x10r5t/currently_having_high_success_with_this_little/)
- **AMD R9700 水冷头发布，实现安静 4x/6x AI 构建** — 一款新的 AMD R9700 水冷头可实现更安静的 4x/6x GPU AI 构建。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x135oh/bois_theres_now_a_waterblock_for_the_r9700_quiet/)
- **llama.cpp 创作者 ggerganov 在活动舞台上演讲** — llama.cpp 创作者 ggerganov 登台演讲，凸显本地推理的持续发展势头。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x079wc/llamacpp_on_the_stage/)

---

*由 AI News Agent 生成 | 2026-10-08*