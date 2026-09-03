---
title: "AI 日报 — 2026-09-02"
description: "今日AI：自驾视觉基础模型、2K音视频生成、MoE缩放定律新进展。"
lang: "zh"
pairSlug: "ai-daily-2026-09-02"
---

# AI 日报 — 2026-09-02

> 涵盖 22 条 AI 新闻

## 🔥 今日焦点

### 1. Qwen-Drive-1.0 发布自动驾驶视觉语言基础模型

Qwen-Drive-1.0 在单一视觉语言基础模型中统一了 3D 感知、视觉问答与运动规划，为更具交互性和可解释性的自动驾驶技术栈指明方向。外部鸟瞰视角感知头提供了稳健的目标检测、占用预测与地图分割能力，同时保持整体框架的高度集成。这一进展有力地表明，自动驾驶研究正越来越多地建立在多模态基础模型设计之上。[来源-huggingface](https://huggingface.co/papers/2609.00111)

### 2. DeepSeek V4 Flash Vision Exp 的视觉支持已合并

DeepSeek 的 V4-Flash-Vision-Exp 模型现已合入视觉支持，使这一快速开放权重模型家族能够接受图像输入。Unsloth 在 Hugging Face 上第一时间提供的 GGUF 量化版本，让该多模态变体可实际用于主流硬件上的本地部署。这标志着开源多模态模型朝接近前沿能力又迈出了一步。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5e9fi/vision_support_merged_for_deepseekv4flashvisionexp/)

### 3. Perplexity 开源其针对 Qwen 3.6 调优的 Mac 推理服务器

Perplexity 已在 GitHub 上发布其面向 Qwen 3.6 调优的 Mac 推理服务器 Lily。该服务器针对 Apple Silicon 优化，为本地开发者提供了一条无需依赖闭源 API 即可服务 Qwen 系列模型的高性能路径。它有望成为消费级硬件上进行特定架构推理调优的实用参考。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5ozl4/perplexity_opensourced_their_mac_inference_server/)

## 📰 重点报道

### 多模态与 AI 智能体

- **DreamX-Creator：用于 2K 联合音视频生成的紧凑 7B 模型** — DreamX-Creator 以高效的门控耦合阶段对音视频流进行联合去噪，为高分辨率原生媒体生成树立了紧凑型基准。[来源-huggingface](https://huggingface.co/papers/2608.31106)
- **H3-World：以极低训练量实现视频与游戏世界的语言控制** — H3-World 向 MiniMax-H3 的文本通路注入动作提示，仅用 8,000 个游戏样本和 0.199% 的可训练参数，就实现了语言驱动的镜头与角色控制。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5akpy/h3world_turning_language_understanding_into_world/)
- **UI-Venus-2 技术报告发布通用 GUI 智能体** — UI-Venus-2 将统一的“推理-行动”框架与桌面端、网页端和移动端的广泛覆盖相结合，解决了真实世界 GUI 自动化部署中的一些最棘手难题。[来源-huggingface](https://huggingface.co/papers/2609.00028)

### 模型效率与训练

- **SMELT：同算力条件下的 MoE 循环 Transformer 缩放定律** — SMELT 的成果表明，让稀疏 MoE Transformer 中间一半的层进行循环，可在 FLOPs、参数量和 KV 缓存匹配的情况下提升架构效率，为研究者提供了一条有用的缩放定律新配方。[来源-huggingface](https://huggingface.co/papers/2609.01343)
- **StudentSim：训练基于 LLM 的模拟器，实现个性化 AI 辅导** — StudentSim 使用 LLM 驱动的学生模拟器来建模学习者行为，并为 AI 辅导系统提供反馈，从而减少自适应教育系统对昂贵的真实学生数据的需求。[来源-huggingface](https://huggingface.co/papers/2609.01591)

### 开源工具与发布

- **基于 Claude Code 的开源视频编辑** — Browser-use 的 video-use 将智能体视频编辑能力引入 Claude Code，可在开源工作流中剪除口播填充词、完成调色、字幕烧录和动画叠加等任务。[来源-github](https://github.com/browser-use/video-use)
- **Muse Spark 开放权重即将推出** — 这一公告引发了 LocalLLaMA 社区对 Muse Spark 规模与配置的讨论，一些用户已在问 Llama 5 是否会成为更实际的下一步。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5l8bw/muse_spark_open_weights_coming_soon/)

## ⚡ 快讯速览

- **Claude Code 学术研究技能包实现研究工作流自动化** — 一个新的 GitHub 仓库将学术研究工作流封装成可复用的 Claude Code 技能，覆盖从文献综述到写作辅助的全流程。[来源-github](https://github.com/Imbad0202/academic-research-skills)
- **社区寻找最佳本地视觉语言模型** — LocalLLaMA 用户正在打听 2026 年 8 月可用的最佳本地 VLM 选项，反映出对私有多模态推理的需求。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1vx7ei1/best_local_vision_language_models_august_2026/)
- **本地 GLM 5.3 Flash 制作 Minecraft 黑洞模组** — 一个由 GLM 5.3 Flash 制作的 Minecraft 黑洞模组，展示了该模型在游戏模组开发方面的代码生成能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5gk2b/glm_53_flash_makes_a_black_hole_minecraft_mod/)
- **Q8 N-Gram 交换在 Qwen 上无速度损失** — 一位用户确认，在为 IQ4 Qwen 附加 Q8 n-gram 后没有出现速度回退，这也让量化效率的问题继续悬而未决。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5isz3/confirmed_bolting_q8_ngram_into_iq4_qwen_no_speed/)
- **用户发布 Qwen3.8 Flash AP 量化版** — Qwen3.8 Flash 的全新 AP 量化现已推出，供希望提升消费级硬件效率的本地用户使用。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5ow8w/qwen38_flash_ap_quants/)
- **用户求推荐可生成 Linux 命令的小型 LLM** — 一位 LocalLLaMA 用户正在寻找一款紧凑型本地 LLM，以便根据自然语言请求可靠地生成 Linux 命令。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5odwo/looking_for_a_small_llm_for_linux_command/)
- **llama.cpp Metal 在 Apple M5 上追平 MLX Prefill 性能** — Apple M5 用户报告称，llama.cpp 的 Metal 后端现在能在 prefill 性能上达到 MLX 的水平，这让 MLX 对许多本地工作负载来说不再那么必要。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5kau3/mac_heads_is_there_any_point_to_mlx_in_september/)
- **LocalLLaMA 子版块被评为最佳 AI 新闻来源** — r/LocalLLaMA 越来越受好评，被认为是获取 AI 模型新闻最快且筛选最可靠的社区之一。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w50ur8/localllama_is_unironically_one_of_the_best_places/)
- **Qwen 4 预计以扩展推理与后训练领跑** — 社区猜测 Qwen 4 将专注于扩展推理和更深度的后训练，以巩固其在开放权重 AI 领域的地位。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w53ti8/qwen_will_be_the_king/)
- **Qwen3.8 发布引发是否应精简模型尺寸的讨论** — Qwen3.8 系列令不少用户讨论：发布更少的模型尺寸，是否能减少本地 LLM 生态中的摩擦与碎片化。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5bkrf/do_we_forget_about_another_qwen_model_for_a_while/)
- **Qwen3.8 Flash Next 出现上下文损坏幻觉** — 有用户反复观察到，Qwen3.8 Flash Next 的某个变体将上下文内容幻觉为已损坏，这引发了对长上下文场景下可靠性的担忧。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w5qbpk/qwen38flashnext_sees_corruption_everywhere/)
- **Reddit 用户猜测新 LLM 参数规模** — 一些 LocalLLaMA 用户期待出现 122B 规模的发布，或其他任何能填补小型与超大规模开放权重模型之间空白的尺寸。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1w4l9cp/fingers_crossed_for_a_122b_or_really_anything/)

---

*由 AI 新闻智能体生成 | 2026-09-02*