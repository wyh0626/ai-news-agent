---
title: "AI 日报 — 2026-11-05"
description: "开源300B智能体RL配方、物理基准及Qwen更快投机解码，推进AI训练与推理。"
lang: "zh"
pairSlug: "ai-daily-2026-11-05"
---

# AI 日报 — 2026-11-05

> 涵盖 26 条 AI 新闻

## 🔥 今日焦点

### 1. FireFlash：面向 Pareto 前沿的 300B 智能体强化学习开放配方

FireFlash 是一个 300B 规模的智能体强化学习配方，在 Terminal-Bench 4.0 上达到 46.2%，同时每任务成本比前沿智能体低 30 倍以上。该配方在 64 块 NVIDIA B300 GPU 上训练不到五天，并结合精选的 RL 环境、稳健的 rollout 配方和优化的编码工具链，且收益可迁移到 SWE 基准。其主要影响在于可复现性：团队获得一条有文档记录的路径，无需前沿级投入即可构建接近前沿的长时程智能体。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xomst7/paper_fireflash_an_open_recipe_for_longhorizon/)

### 2. FrontierPhysics 基准测试在真实物理研究中评估 AI 智能体

FrontierPhysics 推出 56 个端到端任务，由 42 位物理学家编写，覆盖九个领域，涵盖理论、计算和实验研究。与固定问题或论文复现类基准不同，它在智能体执行完整研究工作流时同时评估研究质量和正确性。该基准将智能体评估推向真正的科学实用性，并揭示当前系统仍需人类级判断的地方。 [来源-huggingface](https://huggingface.co/papers/2611.06910)

### 3. Qwen 推出 SpecOPD 以加速投机解码

Qwen 研究人员提出 SpecOPD，一种用于投机解码的分支并行同策略蒸馏框架，在独立分支上采样草稿 token 和目标监督。通过将这些分支打包成提案树以共享计算，该方法旨在获得更长的接受长度和更快的 LLM 推理。如果能在生产环境中成立，SpecOPD 可能在不改变模型架构的情况下改善推理经济性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xoo0pp/paper_specopd_branchparallel_onpolicy/)

## 📰 重点报道

### 开源模型与开发者工具

- **CCORE 发布 GLB-3D-Coder 4B 模型及完整权重** — 对 Qwen3.5-4B 的完整微调可生成完整的 Three.js HTML 场景，并导出 GLB 供 Godot、Blender 和 Unity 使用，提供 GGUF 和 Safetensors 权重。其对可复用 3D 资产的关注使其成为游戏和设计流水线中实用的开放模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xobe4h/ccore_glb3dcoder_4b_final_model_and_full_weights/)
- **Garry Tan 发布面向 Claude Code 智能体团队的开源 gstack** — 这个 MIT 许可的工具包提供 23 个 Markdown 斜杠命令，为编码智能体模拟从 CEO 到 QA 和发布工程师的角色。它反映了将智能体工作流打包为轻量、可 fork 的操作流程这一日益增长的模式。 [来源-github](https://github.com/garrytan/gstack)

### 智能体强化学习与具身 AI

- **TurnWise 推出用于流式视频 RL 的轮次级 GRPO** — TurnWise 用逐轮信用取代轨迹级优势，用于流式视频理解，旨在避免强化冗余回复，或避免在失败后惩罚有用的后续追问。该方法解决了多轮视频智能体中一个关键的信用分配缺口。 [来源-huggingface](https://huggingface.co/papers/2611.06728)
- **NEO-VLA 提出超越固定视觉编码器的原生视觉-语言-动作策略** — NEO-VLA 让动作策略访问不断演化的视觉计算，而不是依赖固定的编码器端点，主张操作需要局部几何、边界、深度和细微状态变化。该设计指向机器人中更紧密的视觉-动作耦合。 [来源-huggingface](https://huggingface.co/papers/2611.06918)

### 世界模型与生成式视频

- **GameVerse 数据集支持分钟级长时程交互式世界建模** — GameVerse 提供分钟级游戏玩法数据和更精细的说明文字，用于训练交互式世界模型，使其超越约一分钟的连贯性。更好的长时程数据可减少动作条件环境生成中的漂移。 [来源-huggingface](https://huggingface.co/papers/2610.37257)
- **MoneyPrinterTurbo 根据主题生成高清短视频** — 这个开源工具可从一个关键词自动完成脚本、素材匹配、字幕、音乐和最终合成，并提供 WebUI 和 API。它降低了自动化短视频制作的门槛，同时引发人们对合成媒体数量的常见担忧。 [来源-github](https://github.com/harry0703/MoneyPrinterTurbo)

### 极低资源推理

- **Kimi K3 2.78T 模型在 8GB RAM 的单 CPU 上运行** — 一个便携式 C99 实现通过磁盘流式传输和 8.24 GB 峰值 RAM，在单 CPU 上运行 2.78 万亿参数模型，以极慢速度产生字节完全一致的输出。该项目与其说是实用的服务路径，不如说是对内存层次工程的一次引人注目的演示。 [来源-github](https://github.com/FareedKhan-dev/kimi-k3-in-c)

## ⚡ 快讯速览

- **MoE 训练手册发布，附带 Megatron-LM 运行手册** — 一本新手册将 MoE 训练指导与 Megatron-LM 运行手册配对，为从业者提供大规模混合专家训练的结构化参考。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xor5nr/the_ultimate_moe_training_handbook_training/)
- **DeepSeek-V4.1-Flash 在八块 2018 年 V100 上达到 200+ tok/s** — 一位实践者报告称，DeepSeek-V4.1-Flash 在八块 2018 年时代的 V100 GPU 上超过每秒 200 个 token，凸显旧加速器经过优化推理后仍具可行性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xoubyo/lawyer_with_too_many_gpus_part_4_deepseekv41flash/)
- **Z.ai 披露 GLM-5.5 训练流水线及 32B/122B/256B 模型** — Z.ai 首席科学家详细介绍了 GLM-5.5 的训练流水线，以及涵盖 32B、122B 和 256B 参数在内的模型规模。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xossr5/zai_chief_scientist_jie_tang_just_revealed_the/)
- **Delta Inference Engine v0.93 在 RTX 3090 上提升 DeepSeek-V4.1-Flash** — 根据一项社区发布，Delta Inference Engine v0.93 提升了 DeepSeek-V4.1-Flash 在单块 RTX 3090 上的性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xoq4vq/deepseekv41flash1017_on_one_rtx_3090_big_updates/)
- **因子化 MLLM 嵌入改进组合图像检索** — 一篇新论文使用因子化多模态 LLM 嵌入来改进组合图像检索，其中查询结合参考图像和文本编辑。 [来源-huggingface](https://huggingface.co/papers/2611.05193)
- **PR-Agent：开源 AI 代码审查智能体，社区维护的遗留项目** — PR-Agent 被定位为一个社区维护的开源 AI 代码审查智能体，用于自动化拉取请求反馈。 [来源-github](https://github.com/The-PR-Agent/pr-agent)
- **Horizon 推出 AI 驱动的新闻雷达，用于每日双语简报** — Horizon 是一个 AI 驱动的新闻雷达，可生成每日双语简报。 [来源-github](https://github.com/Thysrael/Horizon)
- **Scenario Labs 发布面向 AI 内容创作和 DCC 工具的智能体技能** — Scenario Labs 发布了面向 AI 内容创作和数字内容创作工具的智能体技能，将可复用能力打包用于创意工作流。 [来源-github](https://github.com/scenario-labs/skills)
- **RustingStrata 与 llama.cpp 在 Qwen GGUF 模型上的基准测试对比** — 一项社区基准在 Qwen GGUF 模型上比较 RustingStrata 和 llama.cpp，为运行时性能权衡增加了证据。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xottw2/strata_for_all_qwen_models_from_little_to_big/)
- **Kokon 在 Qwen-Image 2.1 编辑器周围增加可编辑图层** — Kokon 在 Qwen-Image 2.1 编辑器周围增加可编辑图层，改善图像生成工作流中的图层级控制。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xoji3b/getting_editable_layers_out_of_qwenimage_21_a/)
- **Qwen3.8 Flash-Next 借助 Basalt 在单块 RTX 5080 上达到 250 tok/s** — 一份指南报告称，Qwen3.8 Flash-Next 借助 Basalt 在单块 RTX 5080 上达到每秒 250 个 token。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xomy0i/guide_qwen38_flashnext_on_a_single_rtx_5080_64gb/)
- **Qwen LLM 在工具使用和视觉方面的有趣内心独白** — 一篇社区帖子展示了 Qwen 模型围绕工具使用和视觉的一段有趣内心独白，凸显推理轨迹如何暴露古怪但有启发性的行为。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xobzg3/qwen_be_like/)
- **Reddit 用户称赞 OrcaCyber-Nano-1.0 微调模型在编码和规划方面的表现** — 一位 Reddit 用户称赞 OrcaCyber-Nano-1.0 微调模型在编码和规划任务上的表现，为小型专用模型增添了轶事证据。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xosw1w/appreciation_post_for_orcacybernano10/)
- **DeepSeek 在本地 LLM 测试中 Qwen 失败后修复 HDMI 显示** — 一则本地 LLM 测试轶事声称，在 Qwen 失败后 DeepSeek 修复了 HDMI 显示问题，这是模型被用于实际故障排查的一个例子。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xoql51/deepseek_fixed_my_hdmi_display_show_case/)
- **NVIDIA RTX PRO 5500 Blackwell 标价 17,999 美元，高于 RTX PRO 6000** — NVIDIA 的 RTX PRO 5500 Blackwell 已以 17,999 美元出现，定价高于 RTX PRO 6000，引发关于工作站 GPU 定位的疑问。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xojryw/nvidia_rtx_pro_5500_blackwell_appears_at_17999/)
- **Reddit 用户称 Qwen3.8-27B 质量在初次发布后下降** — 一位 Reddit 用户称 Qwen3.8-27B 的质量在初次发布后下降，凸显社区对托管模型更新的持续审视。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1xoeeyf/qwen3827b_has_become_unuseable_recently/)

---

*由 AI News Agent 生成 | 2026-11-05*