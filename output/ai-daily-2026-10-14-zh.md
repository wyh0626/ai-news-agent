---
title: "AI 日报 — 2026-10-14"
description: "GreenWAM机器人世界模型Tev密集奖励长程智能体英伟达Nemotron将发"
lang: "zh"
pairSlug: "ai-daily-2026-10-14"
---

# AI 日报 — 2026-10-14

> 覆盖 21 条 AI 新闻

## 🔥 今日焦点

### 1. NVIDIA Nemotron Bolt 3.5 74B A9B 将于 10 月 15 日发布

NVIDIA 即将推出的 74B 参数 MoE 模型仅使用 9B 激活参数和 2-bit 量化，以装入 24GB 内存，并通过量化感知训练来保持质量。此次发布让高能力本地推理更接近消费级硬件，而 10 月 23 日推出的更小 E4B 4GB 变体则标志着向边缘部署的更广泛推进。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5t1tm/nvidia_nemotron_bolt_35_74b_a9b_releases_oct_15th/)

### 2. 中国的开放权重 AI 模型落后美国闭源模型 7 个月

一个汇总了 22,113 项基准测试结果的开放排行榜发现，中国的开放权重模型大约落后美国闭源前沿系统七个月。独立评分与实验室自报评分之间的分歧既凸显了进展，也揭示了测量风险，为企业提供了一张更清晰——尽管仍有争议——的开放权重前沿地图。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5pjv7/the_ai_race_chinas_openweight_models_trail_us/)

### 3. inclusionAI 发布 Ling-3.1-flash 560B MoE，支持 1M 上下文

inclusionAI 的 Ling-3.1-flash 扩展至 560B 总参数，每个 token 激活 25B 参数，并具备 1M token 上下文窗口，较 Ling 3.0 的 127B 大幅提升。此次发布面向长文档、检索密集型以及智能体工作负载，不过服务如此大型的 MoE 将需要大量内存和高效路由。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5tsni/inclusionailing31flash_hugging_face/)

## 📰 重点报道

### 机器人与具身 AI

- **GreenWAM：面向机器人的世界基础模型** — GreenWAM 提出共享的解剖式动作空间和训练配方，以在多种机器人本体上同时充当世界模型和策略，解决机器人领域中动作格式碎片化的问题。 [来源-huggingface](https://huggingface.co/papers/2610.18774)
- **Urbex：面向城市级 3D 定位的智能体视觉-语言框架** — Urbex 将城市级 3D 定位重新表述为主动空间搜索，让 VLM 智能体查询地标、缩放、渲染斜视图并提交边界框，以更高效地理解大型场景。 [来源-huggingface](https://huggingface.co/papers/2610.18356)

### 智能体 AI 与训练

- **Tev 通过密集进度奖励扩展长时程智能体环境** — Tev 引入密集进度奖励，以训练智能体完成持续数小时到数天的任务，解决限制开源智能体模型的稀疏奖励和数据瓶颈问题。 [来源-huggingface](https://huggingface.co/papers/2610.18868)
- **Agent-Reflex：训练语言智能体主动反思** — Agent-Reflex 使用三阶段训练框架，通过主动反思帮助语言智能体从嘈杂的 MCP 工具反馈和用户干预中恢复。 [来源-huggingface](https://huggingface.co/papers/2610.17953)

### 高效开放权重模型

- **MiniCPM-V 4.7 在手机上运行 35B 多模态 MoE** — OpenBMB 展示了 35B-A3B 视觉-语言 MoE 在移动端本地运行，内存占用约 3GB，这得益于 LES 专家调度，以及面向端侧多模态任务的更小 1B 变体。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5uwnd/a_35b_multimodal_model_running_on_a_phone_with/)
- **Telperion 发布 Qwen3.8-27B MLA/GLA 变体，实现 4 倍 KV 缓存压缩** — Telperion 的潜在注意力变体将 KV 缓存压缩至四分之一，其中 MLA 模型将 SWE-bench Verified 提升到 42.1%，同时使用的推理 token 减少约 20%。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5wcnz/new_model_from_telperion_qwen3827bmla/)
- **Sabi-Noema：Qwen 3.8 27B 微调提升能力与效率** — Sabi-Noema 和 Sabi-Noema-MLA 提升了编码、智能体和工具调用性能，同时将冗长程度减半并减少幻觉，据称在 DeepSWE 上击败 GPT 6 Luna-medium。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x62zrz/sabinoema_a_capability_and_efficiency_focused/)

## ⚡ 快讯速览

- **开源 VoiceStudio 为 646 种语言提供本地 ElevenLabs 替代方案** — VoiceStudio 为隐私敏感的音频工作流提供覆盖 646 种语言的本地开源语音合成选项。 [来源-github](https://github.com/debpalash/VoiceStudio)
- **Vercel Labs 推出面向编码智能体的开放 Agent Skills CLI** — Vercel Labs 发布了一个 CLI，用于向编码智能体添加可复用的智能体技能。 [来源-github](https://github.com/vercel-labs/skills)
- **Mr.Chatterbox-2.7B-Chat：基于维多利亚时代文本训练的语言模型发布** — 一个完全基于维多利亚时代文本从零训练的 2.7B 聊天模型已发布，用于风格化和历史语言实验。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5y904/mrchatterbox27bchat_a_model_trained_from_scratch/)
- **Zellige AI 发布 Tessera-27B-B-CJK Qwen 微调模型，实现更 token 高效的思考** — Zellige AI 基于 Qwen 的微调模型面向 CJK 用例，提供更 token 高效的推理。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5xm28/tessera27bbcjk_zellige_ais_new_finetune_of_qwen/)
- **Anthropic 高管称开源 AI 模型风险更高** — 一位 Anthropic 高管主张开源 AI 模型风险更高，重新点燃了关于开放与安全的争论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5nyd3/anthropic_executive_says_opensource_ai_models_are/)
- **零设置本地照片编辑器在 12GB+ GPU 上运行 Qwen-Image 2.1** — 一个零设置本地照片编辑器可在显存 12GB 或以上的 GPU 上运行 Qwen-Image 2.1。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5wyii/gptimagestyle_photo_editing_on_your_own_gpu_12_gb/)
- **ComfyUI v0.40.0 发布** — ComfyUI v0.40.0 为这款流行的基于节点的图像生成工作流工具带来更新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5nu99/comfyui_v0400_released/)
- **Jeva：从第一性原理出发的 System One 模型** — Jeva 提出一种从第一性原理出发的“System One”模型方法，用于快速、直觉式推理。 [来源-huggingface](https://huggingface.co/papers/2610.18773)
- **BreezeBlue-TTS-2 被称为最佳本地 TTS 模型，采用非商业许可证** — BreezeBlue-TTS-2 被宣传为最佳本地 TTS 模型，但其非商业许可证限制了部署。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x5qr7b/breezebluetts2_is_currently_the_best_tts_model/)
- **越狱 PS5 以每秒 20 token 本地运行 Qwen 3.8 27B** — 一台越狱 PS5 以约每秒 20 token 在本地运行 Qwen 3.8 27B，展示了非常规消费级硬件推理。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x62uhc/someone_jailbroke_a_ps5_and_got_qwen_38_27b/)
- **用户比较 Qwen 3.8 Flash Next 与 DeepSeekV4 Flash 的速度** — 一项用户基准测试比较了 Qwen 3.8 Flash Next 和 DeepSeekV4 Flash 的速度与延迟。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1x61xas/qwen_38_flash_next_deepseekv4_flash_and_time/)

---

*由 AI News Agent 生成 | 2026-10-14*