---
title: "AI 日报 — 2026-05-20"
description: "通用AI解决重大未解题，Gemini3.5自称更快编码，AI推翻Erdős猜想。"
lang: "zh"
pairSlug: "ai-daily-2026-05-20"
---

# AI 日报 — 2026-05-20

> 涵盖 33 条 AI 新闻

## 🔥 今日焦点

### 1. 通用型 AI reportedly 解决重大数学开放问题

一款通用型 AI 模型据称已经解决了一个数学领域的重大开放问题，被视为 AI 驱动科学发现的里程碑。帖子一方面对 AI 扩展人类认知的能力感到兴奋，另一方面也表达了复杂和矛盾的情绪。Timothy Gowers 提醒数学家在继续往下看之前要先有心理准备。 [来源-twitter](https://x.com/sama/status/2057203171198636251)

### 2. Gemini 3.5 Flash 宣称在编码与速度上全面领先

Google 的 Gemini 3.5 Flash 宣称在代码能力和智能体任务上相比 3.1 Pro 有显著提升。它声称相较前沿模型最多可快 4 倍，在 Antigravity 中可快 12 倍，达到约 800 tokens/秒且成本更低。帖子鼓励用户通过 Antigravity、GeminiApp 等渠道体验该模型。 [来源-twitter](https://x.com/demishassabis/status/2056904067406860545)

### 3. AI reportedly 解决 Erdős 单位距离问题并推翻猜想

据称，一款 OpenAI 模型已经解决了长期悬而未决的单位距离问题，这是 Erdős 在离散几何中最著名的问题之一。该成果被认为推翻了该领域中的一个核心猜想，标志着 AI 辅助数学研究的重要里程碑。该说法在社交媒体上广泛传播，重点强调了 OpenAI 的参与。 [来源-twitter](https://x.com/wtgowers/status/2057175729008153069)

## 📰 重点报道

### AI Tools

- **Google 的 AI Studio Mobile 即将登陆应用商店** — Google 宣布推出 AI Studio Mobile，这是其 AI Studio 平台的移动版本，让用户可以随时随地构建创意应用。该应用即将上线各大应用商店，并支持诸如 HLS 播放等功能。 [来源-twitter](https://x.com/GoogleAIStudio/status/2056904153562264025)

### LLM

- **Anthropic 每月向 SpaceX 支付 12.5 亿美元算力费用** — 据报道，Anthropic 每月向 SpaceX 支付约 12.5 亿美元，以获取计算资源。这样的合作凸显了大规模 AI 模型对硬件与云端算力的极高需求，也说明 SpaceX 在支撑 AI 基础设施方面扮演着重要角色。这笔巨额算力合作也体现了当下前沿 AI 研发背后持续扩大的算力合作趋势。 [来源-twitter](https://x.com/pitdesi/status/2057207627567014014)
- **Qwen3.7 Max 登顶 AI 榜单；27B/35B 模型开放候补** — 在 Artificial Analysis 的基准测试中，Qwen 3.7 Max 排名第 5，大致与 GPT-5.4（xhigh）相当，并略微领先 Gemini 3.5 Flash。DSV4 Flash 与 Qwen3.6 27B 的得分比 Max 版本低大约 6 分。报告还提到 27B/35B 模型目前采用候补队列形式开放。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tie6gy/qwen37_max_scored_by_artificial_analysis_27b35b/)
- **obra/superpowers：开源 agentic 编程框架** — obra/superpowers 是一个面向编码智能体的开源软件开发方法论，基于可组合的技能和起始指令构建。它引导用户先定义目标，再逐步细化成设计规格，并最终给出适合初级工程师执行的实现计划。Quickstart 文档列出了与 Claude Code、Codex CLI、Gemini CLI 等多种 AI 工具的集成，用于支撑完整的开发工作流。 [来源-github](https://github.com/obra/superpowers)
- **免费 Claude Code 代理支持多后端路由** — 这个可直接替换的代理工具，能拦截 Claude Code 对 Anthropic API 的调用，并将其路由到 10 个不同的提供商后端，实现按模型维度的路由以及通过 /v1/models 进行原生模型发现。它可以将流量分发到 NVIDIA NIM、Kimi、Wafer、OpenRouter、DeepSeek、LM Studio、llama.cpp、Ollama、OpenCode Zen、Z.ai 等服务，同时保持 Claude Code 客户端协议不变。该工具面向使用 Claude Code CLI、VS Code、JetBrains ACP 或任何兼容 Anthropic 代理的聊天机器人开发者，支持免费、付费或本地模型。 [来源-github](https://github.com/Alishahryar1/free-claude-code)
- **Cohere 发布开源权重的 Command A+ MoE 模型** — Cohere 宣布推出 Command A+，这是其 Command 系列中首个以 Apache 2.0 协议开放权重的 mixture-of-experts（MoE）模型。该模型强调高效与快速响应，通过量化后仅需 1–2 块 GPU 即可部署，并重点面向小团队与希望构建 Cohere 驱动智能体的开发者的实际应用场景。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tizmar/re_what_ever_happened_to_coheres_commanda_series/)
- **Qwen 3.6 35B GGUF：跨 GPU 和 CPU 的 NTP 与 MTP 量化对比** — ByteShape 发布了 Qwen 3.6 35B GGUF 的两类量化版本：NTP 和 MTP。对 NTP 而言，能装下的最大量化配置表现最好，且更低的 bpw 并不必然更优；MTP 在 GPU 上可带来约 20–40% 的加速，但也显著增加显存占用，从而限制可加载规模，而在 CPU 上使用 MTP 性价比不佳。由于答案格式问题，本次评测没有纳入 MMLU，发布重点在于不同硬件环境下的基准测试，而非简单的模型发布。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tipihx/qwen_36_35b_gguf_ntp_vs_mtp_quantization_results/)
- **HalBench 对 4 个前沿 LLM 的逢迎与幻觉进行评测** — HalBench 被提出作为一个开放基准，用于衡量 LLM 逢迎用户（sycophancy）和产生幻觉的倾向。它针对 3200 条错误前提提示（共 12800 个回答）评估了 4 个前沿模型——Sonnet 4.6、Grok 4.3、GPT-5.4 与 Gemini 3.1 Pro，其中 100 条样本由人工验证。数据集、界面与代码均已开源，作者还征询社区意见，希望知道下一步该测试哪些开源模型，并指出当前 Sonnet 领先，而 Gemini 与 GPT-5.4 表现相对落后。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tizvih/halbench_i_built_a_custom_sycophancy_and/)
- **在受限显存下，启用 MTP 的 ik_llama.cpp 性能优于 llama.cpp** — 一位 Reddit 用户报告称，llama.cpp 在合并某个 PR 后，其 MTP 性能出现了回退，并展示了 ik_llama.cpp 在启用 MTP 时在 RTX 4070 12GB 上显著更高的吞吐量。以 Qwen3.6-35B-A3B-IQ4_XS-4.19bpw.gguf 为基准的测试显示，其在不同任务上可达到约 100–122 tok/s，突出了 ik_llama.cpp 在实际速度上的优势。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tj2gya/try_ik_llamacpp_with_mtp_if_you_have_limited_vram/)
- **LM Studio 新增对 MTP 推测解码的支持** — LM Studio 在 0.4.14 Build 2（Beta）更新中，正式支持兼容模型的 MTP 推测解码。用户需要使用 llama.cpp engine 2.15.0，并在加载模型前手动勾选“Manually choose model load parameters”以启用 MTP，因为默认并未开启。该更新由 Reddit 用户 /u/pigeon57434 在 LocalLLaMA 社区分享。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ti99an/lm_studio_finally_added_support_for_mtp/)
- **LLama.cpp PR 更新：为 MTP 草稿路径引入后端采样** — 在 ggml-org/llama.cpp 仓库中有一个新的 Pull Request，为 MTP 草稿路径引入后端采样机制，以期提升性能。PR #23287 由用户 jacek2023 提交，并由 gaugarg-nv 在 Reddit 上展开讨论。此次更新面向 MTP 工作流内部的性能优化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tis73j/move_to_backend_sampling_for_mtp_draft_path_by/)
- **CohereLabs Command-A+ 05-2026 bf16 模型上线 Hugging Face** — 一则 Reddit 帖子重点介绍了 CohereLabs 的 command-a-plus-05-2026-bf16 模型，已在 Hugging Face 发布。帖子由用户 /u/coder543 提交，附上模型页面与讨论链接，并特别指出这是 bf16 版本。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tiphqe/coherelabscommandaplus052026bf16_hugging_face/)

### AGI

- **Sam Altman：AGI 将加速科研、公司与个人 AI** — Sam Altman 将 AGI 描述为会在三个方面带来加速：科研、公司以及个人 AGI。他提到“unit distance”相关结果，并宣布计划为每一家 YC 公司投资价值 200 万美元的 OpenAI 额度，以强力支持 AI 驱动的创业公司。他同时呼吁业界更加关注“个人 AGI”，帮助个体更好地实现自身目标。 [来源-twitter](https://x.com/sama/status/2057218997503086888)

### AI

- **rtk-ai/rtk CLI 代理可将 LLM token 使用量削减 60–90%** — rtk 是一个基于 Rust 的 CLI 代理，它在命令输出进入 LLM 上下文前对其进行压缩，从而在常见开发命令上将 token 使用量减少 60–90%。该工具以单一二进制形式发布，支持 100+ 常用命令，并提供跨语言文档，旨在加速与 LLM 的交互体验。项目以 rtk-ai/rtk 名义在 GitHub 上开源。 [来源-github](https://github.com/rtk-ai/rtk)

### Google Gemini

- **Google Gemini 工具家族与品牌重塑梳理** — 一篇略带戏谑的长帖将各类 Google Gemini 产品对应到不同的 AI 工具，梳理了被弃用或更名的产品（例如 Gemini Pro/Ultra、AI Studio、Antigravity CLI）以及相关的 IDE、智能体与笔记本环境。它系统地罗列了在 Gemini 生态不断演进下，用户应该用哪些工具来完成编码、视频、图像、搜索与科研等任务。 [来源-twitter](https://x.com/nathanclark_/status/2056947354654355849)

### Industry

- **DeepSeek 将构建 Code Harness，在北京招募新团队** — DeepSeek 宣布组建全新的 Harness 团队，从零开始打造 Code Harness 工具体系，用于支撑 AI 研究和产品集成。公司在北京开放了两个岗位——Harness 产品经理与 Harness 研发工程师。帖子还将这一项目与当前围绕主动学习与交互式提示的更广泛讨论联系在一起。 [来源-twitter](https://x.com/swyx/status/2057064854679331177)

### Multimodal

- **Vision Speaks for Sound：多模态 AI 对音频的“误读”** — 尽管支持视频的多模态 LLM 进展迅速，研究者发现它们在处理视频音频时往往是从视觉线索中“猜测”声音，而不是实际加以验证。这一问题在开源 omni 模型以及 Google、OpenAI 的闭源产品中均有体现，被形容为一种“视听版 Clever Hans 效应”，模型看似在“听”，实则没有真正利用音频信号。这凸显了当前 AI 系统在音频与视觉处理之间存在根本性错位。 [来源-huggingface](https://huggingface.co/papers/2605.16403)

### RL

- **GoLongRL 发布基于 RLVR 的开源长上下文强化学习方案** — GoLongRL 提出了一种完全开源、以能力为导向的长上下文强化学习（long-context RL）方法，并采用可验证奖励（RLVR）。作者认为，此前的长上下文 RL 过度依赖复杂的检索路径，导致任务覆盖不均与奖励错位。论文提出两大贡献，包括以能力为中心的数据构建方法，以及面向可复现性的开放发布。 [来源-huggingface](https://huggingface.co/papers/2605.19577)

### AI Safety

- **OpenComputer 为“电脑操作智能体”构建可验证世界** — OpenComputer 是一个以验证器为基础的框架，用于为电脑操作类智能体构建可验证的软件世界。它整合了四个组件：面向具体应用的状态验证器、自演化验证层、用于生成真实桌面任务的任务生成流水线，以及评测工具链。 [来源-huggingface](https://huggingface.co/papers/2605.19769)

### Open Source

- **ViMax：一体化 AI 视频生成器** — ViMax 是由 HKUDS 发布的开源项目，定位为端到端的 AI 视频解决方案。它旨在自动化完成文案撰写、分镜设计、角色创建以及最终视频生成，解决当前工具普遍存在的片段过短、叙事不连贯和故事深度不足等问题。其 GitHub 页面提供了详细的演示样例和系统架构说明。 [来源-github](https://github.com/HKUDS/ViMax)

## ⚡ 快讯速览

- **前董事会对话：Anthropic 被婉拒；意识形态无法在 AI 现实中存活** — 作者回忆说，Anthropic 曾讨论让他出任董事会席位，但他认为自己不合适而拒绝了这一提议。他提到曾将亚里士多德的《政治学》寄给 Dario Amodei 和 Daniela，但不确定他们是否读过。帖子还引用 Dario Amodei 的观点，认为意识形态无法在 AI 的现实考验下长期存活。 [来源-twitter](https://x.com/eastdakota/status/2057017593991462945)
- **主动学习提升 PRP 重排效率** — Pairwise Ranking Prompting（PRP）通过从 LLM 收集成对偏好来构建排序，但判断常常噪声较大、对顺序敏感且可能不具传递性，因此传统排序在 top-K 场景中容易失效。作者建议将 PRP 重排问题重新表述为“基于噪声成对比较的主动学习”，以在给定预算约束下提高效率和可靠性。 [来源-huggingface](https://huggingface.co/papers/2605.14236)
- **基于 PMI 的“反自蒸馏”推理强化学习** — 文章讨论了一种“on-policy 自蒸馏”方法，即用模型在带有特权上下文的拷贝来指导学生模型，从而在没有更强外部教师的情况下提升推理能力。尽管这一方法在整体推理能力上的前景可观，但在数学推理上的收益并不稳定。通过点互信息（PMI）分析，作者将失败原因归结为特权上下文会抬高教师在已经见过 token 上的置信度，从而削弱教学有效性。 [来源-huggingface](https://huggingface.co/papers/2605.11609)
- **Multica 发布受 Karpathy 启发的 Claude Code 使用指南** — Multica AI 发布了一个 CLAUDE.md 文件，整理了受 Andrej Karpathy 启发的指南，以改进 Claude Code 的行为表现。该指南强调 LLM 编程中的常见问题——代码过度复杂、遗漏澄清步骤以及未暴露不一致之处——并倡导更简洁稳健的代码风格。该项目隶属于 Multica 的开源平台，致力于运行和管理具备可复用技能的编码智能体。 [来源-github](https://github.com/multica-ai/andrej-karpathy-skills)
- **HuggingFace 基准数据集现支持按模型规模过滤** — HuggingFace 的基准数据集现在可以按模型规模过滤，便于对 32B 以下模型在 swebenchverified 等基准上的表现进行更便捷的对比。该功能由一则 Reddit 帖子介绍，并附上按“Trending” 排序的官方数据集页面链接。这一更新有助于研究者更轻松地评估小模型在标准数据集上的表现。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tilvit/huggingface_benchmark_datasets_now_let_you_filter/)
- **Codex 被赞为团队驱动成果；ajambrosino 被称为核心推动力** — 一条推文将 Codex 的成功归功于团队协作，并特别点名 @ajambrosino 是 Codex 应用背后的核心推动力。作者赞扬团队间的密切合作，并表示 Codex 是大家都希望效仿的范例，同时强调他们目前仍然只是在起步阶段。 [来源-twitter](https://x.com/thsottiaux/status/2056931009896317004)
- **Gemma 4 MTP：仍在开发中的预览发布** — Gemma 4 MTP 是一位 Reddit 用户 u/am17an 分享的在研项目。帖子指出，该项目需要由用户自行编译，目前尚不稳定，可能无法可靠运行。它由用户 u/jacek2023 提交至 r/LocalLLaMA 社区。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tijpwl/wip_gemma_4_mtp/)
- **AMD Ryzen AI Halo PC 预计售价 3999 美元，配备 128GB 内存** — 一则 Reddit 帖子称，AMD 的 Ryzen AI Halo PC 预计售价为 3999 美元，并将内置 128GB 内存。该消息由 LocalLLaMA 版块用户 /u/Mochila-Mochila 发布，突出了这款高端、面向 AI 工作负载的 PC 配置。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tinl98/amd_ryzen_ai_halo_pc_will_cost_3999_with_128gb/)
- **批评者：AI 不是通用智能，只是“暴力读书”** — 一位 Twitter 用户认为 AI 并不具备通用智能，声称它只是“把所有书和论文都读一遍，然后在它们之间建立联系”。帖子将 AI 描述为会“思考二十个小时并用蛮力推理”的系统，并以 Erdős 问题为例加以说明。作者最后断言，AI 永远不可能成为一名会计。 [来源-twitter](https://x.com/willdepue/status/2057202320954495282)
- **等待 Qwen 3.7 模型发布：期待 27B/122B 版本** — Reddit 用户 /u/Porespellar 发帖表达对 Qwen 3.7 模型发布的期待，希望能看到新的模型规模。他特别提到期待 27B 和 122B 变体，并用一张 Capybara 表情包来表达这种等待心情。帖子体现了社区对 Qwen 生态的持续关注，以及对来自东方新模型的高度期待。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tiqcwu/waiting_on_qwen_to_drop_those_37_models_be_like/)

---

*由 AI News Agent 生成 | 2026-05-20*