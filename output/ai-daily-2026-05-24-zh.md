---
title: "AI 日报 — 2026-05-24"
description: "DeepMind用LLM解九题，LongLive2.0推动NVFP4并行视频。"
lang: "zh"
pairSlug: "ai-daily-2026-05-24"
---

# AI 日报 — 2026-05-24

> 共收录 28 条 AI 新闻

## 🔥 今日焦点

### 1. DeepMind 使用 LLM 驱动的智能体解决 9 个 Erdős 问题
据报道，Google DeepMind 使用由大语言模型驱动的自主 Lean 智能体解决了 9 个 Erdős（埃尔德什）问题，先通过形式化验证，再由人类进行复核。该方法显示了 AI 在数学推理方面不断增强的能力，也可能加剧前沿实验室之间的竞争压力，体现了一种由 LLM 赋能的智能体进行自治循环、再经过形式化检查与人类监管的范式。 [来源-x](https://x.com/kimmonismus/status/2058618029781713002)

### 2. LongLive 2.0 基础设施：NVFP4 并行长视频生成
NVlabs 发布 LongLive 2.0，这是一套支持 NVFP4 并行的基础设施，可在训练和推理阶段进行并行化，从而实现长视频生成，速度达到 45.7 FPS。该版本引入基于 TriAttention 的 kv-cache 压缩（约减少 50% KV，质量无损），并对 RoPE 进行适配，实现 KV-cache 相对 RoPE 以支持无限长度视频，同时已被 ICLR-2026 接收，并带来更广泛的生态更新。 [来源-github](https://github.com/NVlabs/LongLive)

### 3. 为 AGI 的预训练：加入 OpenAI、Google、Meta、Anthropic/XAI
这篇帖子指出，日益扩大的算力差距意味着与 AGI 至关重要的问题如今需要海量算力，因而建议在 OpenAI、Google、Meta 或 Anthropic/XAI/Cursor 等一流实验室从事 pretraining-for-AGI（面向 AGI 的预训练）工作。该观点强调，为推动 AGI 进展，整个行业都需要重度算力投入。 [来源-x](https://x.com/_aidan_clark_/status/2058606927811346435)

## 📰 重点报道

### AI 安全
- **DeepMind 使用 LLM 驱动的智能体解决 9 个 Erdős 问题** — 据报道，DeepMind 使用由大语言模型引导的自主 Lean 智能体解决了 9 个 Erdős 问题，先通过形式化验证，再由人类审查，展示了 AI 不断提升的数学推理能力，并可能提升前沿实验室间的竞争压力。 [来源-x](https://x.com/kimmonismus/status/2058618029781713002)

### 开源与工具
- **LongLive 2.0 基础设施：NVFP4 并行长视频生成** — LongLive 2.0 支持 NVFP4 并行长视频生成，推理速度可达 45.7 FPS，并集成 kv-cache 压缩与 RoPE 适配以支持无限长度视频，体现了在多模态 AI 领域软硬件一体的开源创新。 [来源-github](https://github.com/NVlabs/LongLive)
- **LongCat 发布 MIT 许可、开源且达到 SOTA 的 talking-avatar 模型** — MIT 协议开源的、达到当前 SOTA 水平的 talking-avatar 模型，并提供 Hugging Face Space 在线演示，可用于实现 AI 导师、配音、说话人脸代理等各类产品。 [来源-x](https://x.com/victormustar/status/2058492201261244458)
- **社区报告导致 vLLM 中“简历练习式 PR 训练”提交被封禁** — 有社区成员举报后，一项作为“为写简历而练习 PR”的提交在 vLLM 项目中被封禁，这一事件凸显出无效或低价值贡献会给开源维护带来大量工作负担和信任成本。 [来源-x](https://x.com/vllm_project/status/2058358072020779391)

### 行业动态
- **在 GitHub 提交量激增 14 倍的背景下，AI 自动化反而推高软件工程师需求** — 尽管 AI 智能体在自动化编程方面持续进步，对软件工程师的需求仍在增长，因为代码库规模不断扩张；GitHub 提交量同比激增 14 倍，表明为满足定制化需求的软件开发迎来生产力爆发。 [来源-x](https://x.com/DavidSacks/status/2058606722110107970)
- **为 AGI 的预训练：加入 OpenAI、Google、Meta、Anthropic/XAI** — 日益扩大的算力差距意味着与 AGI 相关的关键问题都需要海量算力，帖子呼吁在顶级实验室参与 pretraining-for-AGI 方向的研究。 [来源-x](https://x.com/_aidan_clark_/status/2058606927811346435)
- **生成式 AI 视频借助 Kling 进军工业级电视制作** — Kling 的 AI 视频技术正从演示阶段走向真实的电视/电影制片场景，其中一部作品全球覆盖约 4400 万观众，并在美国 Prime Video 上表现亮眼，标志着 AI 生成视频开始走向主流应用。 [来源-x](https://x.com/kimmonismus/status/2058490137139413436)
- **随着 GPU 大量部署，“算力鸿沟”拉大并加速面向 AGI 的预训练** — 一则讨论认为，随着 GPU 不断落地，通向 AGI 的算力鸿沟正在拉大，预计将加速预训练进展，并使在 pretraining-for-AGI 上投入巨大的头部实验室拥有更大优势与主导权。 [来源-x](https://x.com/willdepue/status/2058631473809293664)

### 硬件与算力
- **BitCPM-CANN 在 Ascend NPU 上训练 1.58 比特 LLM** — BitCPM-CANN 展示了在华为 Ascend NPU 上进行 1.58 比特量化感知训练的 LLM，将原本基于 GPU 的工作流迁移到 CANN，并在多个模型上实现接近全精度的性能，支持端到端的本地设备训练。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmf63y/bitcpmcann_native_158bit_large_language_model/)

### 模型微调与多模态
- **Thinking Machines 数小时内微调 Qwen3.5-397B** — Thinking Machines 展示了在数小时内对 Qwen3.5-397B 进行快速微调，并获得可用的多模态能力，这预示着个人 AI 与实时人机协作的可能性进一步增强。 [来源-x](https://x.com/garrytan/status/2058378310254793013)

### 开源
- **社区报告导致 vLLM 中“简历练习式 PR 训练”提交被封禁** — （见“开源与工具”条目） [来源-x](https://x.com/vllm_project/status/2058358072020779391)

---

*注：部分新闻在主题上存在交叉；此处分组以其在重点报道中的主视角为依据。*

---

- **Kling** 及其他面向娱乐的议题，反映的是 AI 生成内容在更广泛媒体行业中的加速落地。

---

*由 AI News Agent 生成 | 2026-05-24*

━━━━━━ End of Template ━━━━━━

⚡ 快讯速览

- **AI 表情包：Twitter 对爆火 AI 演示的反应** — 一波快速涌现的表情包，折射出公众对 AI 演示的反应。 [来源-x](https://x.com/kimmonismus/status/2058628361589518839)
- **Presenton：开源 AI 演示文稿生成器与 API** — 一款用于生成 AI 演示文稿的开源工具与 API。 [来源-github](https://github.com/presenton/presenton)
- **Qwen3.6-35B Uncensored Genesis 搭配 APEX-MTP 发布** — 未经审查的 Genesis 版本随 APEX-MTP 一同发布，引发更广泛的安全性与能力讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tm3toi/qwen3635ba3buncensoredgenesisapexmtp/)
- **Codex 在多个会话中复用提示模式以实现自动化** — 通过在不同会话间复用模式，Codex 可实现更高效的自动化流程。 [来源-x](https://x.com/gdb/status/2058598608224858442)
- **Ask Codex：复用模式以构建最小化自动化流程** — 关于如何通过模式复用来构建体量最小、却最实用的自动化方案的指导。 [来源-x](https://x.com/reach_vb/status/2058538305872949490)
- **Anthropic 入职梗图包含 Karpathy、Wemby、Michael Scott** — 一则反映入职文化与流行文化梗的 meme，主角包括 Karpathy、Wemby 与 Michael Scott。 [来源-x](https://x.com/theo/status/2058629603091226786)
- **开源项目：将 754 项网络安全技能映射到 AI Agent 框架** — 一个开源项目，将网络安全技能系统化映射到 AI 框架与智能体能力图谱中。 [来源-github](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- **Granite DocLing 2Stage 通过动态布局提示强化 OCR** — 通过针对文档理解的动态布局提示，大幅提升 OCR 效果。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmiz7j/ocr_granitedocling258m_vs/)
- **GPU 显存限制下的小型 LLaMA 模型与 llama.cpp：可行吗？** — 关于在有限显存条件下运行小型 LLaMA 模型的可行性讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmeknt/gpu_vram_only_for_small_models_with_llamacpp_is/)
- **如何选择 Abliterated 版 Gemma 4 的 31B 与 26B-A4B 版本** — 针对本地部署场景，对不同 Gemma 模型变体选型的建议。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tm5c92/choosing_an_abliterated_version_of_gemma_4_31b/)
- **2026 年，本地 LLM 仍然首选 NVIDIA 吗？** — 围绕 NVIDIA 是否仍然是本地 LLM 部署“默认最佳选择”的讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmkaua/is_nvidia_still_the_default_best_choice_for_local/)
- **CEO 容易被 AI 炒作带偏，忽视企业真正要做的事情** — 批评一些高管过度追逐 AI 概念，反而遗漏企业核心建设工作的观点。 [来源-x](https://x.com/levie/status/2058582370253701432)
- **Codex 为开源项目，这令许多人感到意外** — Codex 为开源状态一事让不少社区成员颇感惊讶。 [来源-x](https://x.com/gdb/status/2058381548383096994)
- **未审查 LLM 在角色扮演之外还有价值吗？** — 探讨在角色扮演之外，未审查模型是否仍有实际应用价值的讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tlzvfs/is_there_any_reason_for_an_uncensored_model_if/)
- **LlamaBench 在 MTP 模式下失败，引发对推测式解码的质疑** — LlamaBench 出现的问题让社区开始反思 MTP 以及相关推测式解码策略的可靠性。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmlp1n/magic_incantation_to_get_llamabench_to_work_with/)
- **生成式递归教育：支持即时定制教材生成** — 利用生成式与递归式方法，可在需要时动态创建个性化教材。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmoxio/generative_recursive_education_creating_custom/)
- **有人能解释一下 MCP 及其隐私问题吗？** — 就 MCP 的工作原理及其在隐私方面的影响提出求解。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tmlmmo/can_someone_help_me_understand_mcp/)
- **Geoff Hinton 曾在 Google 的头衔一度被标为“实习生”** — 关于 Geoff Hinton 在 Google 早期被标注为“intern”的趣闻轶事。 [来源-x](https://x.com/karpathy/status/2058584498225467846)

---

*由 AI News Agent 生成 | 2026-05-24*