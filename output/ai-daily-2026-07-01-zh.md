---
title: "AI 日报 — 2026-07-01"
description: "Anthropic将ClaudeFable5重启并开放访问发布Sonnet5。"
lang: "zh"
pairSlug: "ai-daily-2026-07-01"
---

# AI 日报 — 2026-07-01

> 涵盖 36 条 AI 新闻

## 🔥 今日焦点

### 1. Claude Fable 5 搭载更新后的安全分类器重新全球上线
Anthropic 宣布 Claude Fable 5 将再次在全球范围内开放使用，并采用全新的分类器组合重新部署，以更好地阻止网络安全相关的滥用行为。日常任务（如编程）将在一段时间内由 Opus 4.8 临时代为处理，同时公司正与主要合作伙伴共同起草一套共识框架，用于评估 AI 越狱行为并指导开发者响应方案，并扩大与美国政府在测试与安全防护方面的协作。 [来源-x](https://x.com/AnthropicAI/status/2072163884430229756)

### 2. Anthropic 开放 Claude Fable 5 促销试用权限
Anthropic 已开始为 Claude Fable 5 提供促销试用访问权限，相关公告已发布在 Claude 支持网站上，并在社区中引发显著讨论与互动（如 Hacker News 讨论）。这表明在更大规模上线前，来自用户与开发者的早期反馈闭环已经开始运转。 [来源-rss](https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access)

### 3. Anthropic 发布 Claude Sonnet 5 AI 模型
Anthropic 正式发布 Claude Sonnet 5，这是 Claude 系列中的最新模型，并在 Hacker News 上引起了大量讨论和关注。此次发布凸显了在大语言模型产品线上，行业在竞争与迭代方面仍在快速推进。 [来源-rss](https://www.anthropic.com/news/claude-sonnet-5)

---

## 📰 重点报道

### Diffusion Models
- **BlockPilot 支持实例自适应的 Diffusion 推测解码** — 提出面向 diffusion 推测解码的“实例自适应策略学习”，可针对每个具体实例动态选择 block 大小与解码策略；通过将 block 级 diffusion 与自适应决策结合，在推理阶段实现当前最先进的并行度表现。 [来源-huggingface](https://huggingface.co/papers/2606.31315)
- **NVIDIA TwoTower 将 30B 模型一分为二以并行生成 token** — 将一个 300 亿参数的 diffusion LLM 拆分为负责保持上下文的部分与负责生成 token 的部分，从而避免重新训练，同时在保持原始质量 98.7% 的前提下，实现约 2.42× 的生成速度提升。 [来源-x](https://x.com/NVIDIAAI/status/2072394812301480067)

### Multimodal & Embodied AI
- **Act2Answer：通过行动式基准测试 VLA 知识** — 提出一种轻量级协议，将 Vision-Language-Action 基准适配为 VLA 评估方式，要求智能体通过“行动”来给出答案，从而更清晰地暴露知识盲区与控制泛化方面的问题。 [来源-huggingface](https://huggingface.co/papers/2606.19297)

### AI Policy
- **美国商务部解除对 Claude Fable 5 与 Mythos 5 的出口管制** — 美国商务部已移除相关出口限制，使这些模型能够在跨境环境中更广泛地访问，也释放出对特定 LLM 更宽松监管态度的信号，对全球 AI 竞争格局可能产生影响。 [来源-x](https://twitter.com/AnthropicAI/status/2072106151890809341)

### AI Safety
- **Anthropic 被指在 Claude Code 中植入隐藏的“间谍软件式”代码** — 有关 Claude Code 中存在类似间谍软件的隐藏代码的说法正在流传；目前从流出的代码片段尚无法证实此事，但这一指控已引发关于代码来源可信度、平台信任以及网络安全与 AI 安全的担忧。 [来源-x](https://twitter.com/IntCyberDigest/status/2071971609183678544)

### Tools
- **ZCode 成为官方 GLM-5.2 IDE 并提供 1.5 倍配额** — ZCode 正式成为 GLM-5.2 的官方开发环境；订阅 GLM Coding Plan 的用户在 ZCode 中可享受 1.5× 使用配额，并支持在 macOS、Windows 与 Linux 上自带密钥（BYOK）的开发体验。 [来源-x](https://x.com/Zai_org/status/2072349453361557898)

### Hardware
- **借助 Ollama MLX，Gemma 4 在 Apple Silicon 上提速约 90%** — 在 Ollama MLX 的支持下，Gemma 4 在 Apple Silicon 上的运行速度显著提升，多 token 预测与动态 token 起草功能的启用，有助于持续维持更高吞吐率。 [来源-x](https://x.com/ollama/status/2072121580201848926)

---

## ⚡ 快讯速览

- Orca: A General World Foundation Model for Next-State-Prediction — 一款面向动态世界“下一状态预测”的通用基础模型。 [来源-huggingface](https://huggingface.co/papers/2606.30534)
- Jelani Nelson joins Anthropic, takes leave from university — 著名研究者 Jelani Nelson 加入 Anthropic，暂时离开其大学岗位，投身于安全与科学相关工作。 [来源-x](https://x.com/dejavucoder/status/2072332366815887769)
- Voice Agent Builder: No-Code Platform for Grok Voice — 用于构建 Grok Voice 智能体的零代码平台。 [来源-x](https://x.com/xai/status/2072342803787702422)
- Dockerless: Environment-Free Program Verifier for Coding Agents — 一种无需运行环境的程序验证器，面向代码智能体的结果校验。 [来源-huggingface](https://huggingface.co/papers/2606.28436)
- ZCode Unveils Claude Code by GLM Makers — ZCode 正式发布由 GLM 团队打造的 Claude Code，对 GLM 生态系统可能产生重要影响。 [来源-rss](https://zcode.z.ai/cn)
- OmniRoute: Free AI Gateway Connects 236 Providers via One Endpoint — 免费 AI 网关 OmniRoute 通过单一接口即可访问 236 家服务提供商。 [来源-github](https://github.com/diegosouzapw/OmniRoute)
- Google Agents CLI Enables Enterprise AI Agents on Gemini Enterprise — Google 推出 Agents CLI，可在 Gemini Enterprise 上部署企业级 AI 智能体。 [来源-github](https://github.com/google/agents-cli)
- Claude Desktop Lands on Linux in Beta — Claude Desktop Linux 版本以测试版形式上线。 [来源-rss](https://code.claude.com/docs/en/desktop-linux)
- NVIDIA ASPIRE Enables Robots to Reuse Skills, Learn Faster — NVIDIA 的机器人平台 ASPIRE 让机器人能够复用技能，并显著加速学习过程。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1uko2de/nvidia_aspire_enables_robots_to_accumulate/)
- AI Might Generate Binary Code, but Tree-Structured Context Helps — 虽然 AI 可以生成二进制代码，但引入树状结构的上下文可以显著改善其表现。 [来源-x](https://x.com/ID_AA_Carmack/status/2072152520374280269)
- Fable 5 usage limited to 50% weekly through July 7, then credits — Fable 5 使用上限政策延长至 7 月 7 日，每周限制在 50%，之后将改为基于点数的计费策略。 [来源-x](https://x.com/theo/status/2072173365318840573)
- DOPD Introduces Dual On-Policy Distillation — DOPD 提出一种“双策略内蒸馏”的新方法。 [来源-huggingface](https://huggingface.co/papers/2606.30626)
- Godot Won't Accept AI-Authored Code Contributions — 开源游戏引擎 Godot 决定不再接受由 AI 生成的代码贡献，认为大量使用 AI 的贡献者难以充分理解代码从而在需要时修复问题。 [来源-rss](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/)
- Employment Shifts as Firms Adopt Generative AI — 随着企业采用生成式 AI，就业结构与趋势正在发生变化。 [来源-rss](https://ramp.com/data/ai-jobs-impact)
- Claude Code Gets 5x More Expensive — Claude Code 的价格大幅上涨，成本接近原先的 5 倍。 [来源-rss](https://www.vincentschmalbach.com/claude-code-quietly-looks-5x-more-expensive/)
- Claude Science: Anthropic's new science-focused AI product — Anthropic 推出面向科学领域的新产品 Claude Science。 [来源-rss](https://claude.com/product/claude-science)
- Anthropic Aims to Assemble an AGI Team — Anthropic 正在组建一个专门面向 AGI 的团队。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ukuahd/anthropic_is_on_a_mission_rn_to_make_agi_team/)
- US Feds Hire Real-Time AI Ban Decision-Maker — 美国联邦机构正在招聘一位负责实时做出 AI 禁令决策的岗位。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ul075e/us_feds_are_actively_hiring_the_person_who_will/)
- Gemini Omni Flash Adds Video Editing Capabilities — Gemini Omni Flash 新增视频编辑相关功能。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ujxrzl/gemini_omni_flash_video_editing_capabilities/)
- Claude Sonnet 5 pricier and less capable than Opus 4.8 — 有反馈称 Claude Sonnet 5 的定价更高，但能力却不如 Opus 4.8。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1uk22hk/claude_sonnet_5_is_both_more_expensive_and_less/)
- Foreign Competitor Offers Cheaper AI Model: What It Means — 更便宜的海外 AI 模型进入市场，引发对竞争格局与意义的讨论。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ujvvu2/so_what_does_it_mean_when_a_foreign_competitor/)
- Personal finance now available for ChatGPT Plus in the U.S. — ChatGPT Plus 在美国地区上线个人理财功能。 [来源-x](https://x.com/gdb/status/2072113363543580690)
- Gemini Flash Next Variant: Launch with 3.5 Pro? — 有传闻称下一代 Gemini Flash 变体可能会与 3.5 Pro 一同发布。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ukn79e/gemini_flash_next_variant_will_it_launch_with_35/)
- Employers regret AI-cited layoffs as backlash grows — 一些以 AI 为理由裁员的公司正面临日益增长的反弹，对此开始感到后悔。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ukqvmu/employers_who_laid_off_workers_citing_ai_are/)
- 150k Tokens: Max 5x Plan Caps Fable Access — Fable 的 Max 5x 方案将访问量封顶在 15 万 tokens。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ul08mc/150k_tokens_thats_all_you_get_on_max_5x_plan_with/)
- Fable 5 diverts coding to Opus 4.8 per Anthropic — 按照 Anthropic 的说法，Fable 5 会将编程类任务转交给 Opus 4.8 处理。 [来源-reddit](https://www.reddit.com/r/singularity/comments/1ukbtjm/fable_5_will_divert_coding_to_opus_48_according/)

---

*由 AI News Agent 生成 | 2026-07-01*