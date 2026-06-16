---
title: "AI 日报 — 2026-06-15"
description: "Sonic-3.5/Ink-2领衔TTS/STT，KimiK2.7发布，降48%"
lang: "zh"
pairSlug: "ai-daily-2026-06-15"
---

# AI 日报 — 2026-06-15

> 涵盖 31 条 AI 新闻

## 🔥 今日焦点

### 1. Sonic-3.5 和 Ink-2 领跑流式 TTS 与 STT
全新的流式 TTS 与 STT 模型 Sonic-3.5 和 Ink-2，为实时语音智能体带来更快、更高质量的语音交互，并支持 HLS 播放以简化流式部署。如果被广泛采用，它们可能会显著提升客户服务和无障碍场景中对话式智能体的整体水准。 [来源-x](https://x.com/krandiash/status/2066559212533190917)

### 2. Kimi K2.7 Code 开源发布；本地运行体积极缩减 48%
Kimi K2.7 Code 正式开源，通过 Dynamic 2-bit 结合选择性 upcasting，将 1T 模型体积大幅压缩到 325GB，使其在 330GB RAM/VRAM 环境中能够实现每秒超过 40 token 的推理速度；全精度推理体积仍为 610GB。此次发布暗示其相比 K2.6 具有更强性能，并指向潜在的 6 倍 High-Speed Mode，用户可通过 Kimi API 和 Kimi Code 进行访问。 [来源-x](https://x.com/UnslothAI/status/2066492839450800427)

### 3. 美国依据出口规则封锁对 Fable 5 和 Mythos 5 的访问
美国一项出口指令暂停所有外国公民对 Anthropic 的 Fable 5 和 Mythos 5 的访问，要求客户禁用这些模型以保持合规，而其他 Claude 系列模型仍可使用。Anthropic 表示该指令源于误解，正在积极寻求恢复访问权限。这一举措凸显了出口管制正在如何重塑 AI 模型的部署方式以及国际协作格局。 [来源-x](https://x.com/latkins/status/2066313801897562513)

## 📰 重点报道

将其余重点新闻按主题分组，每个分组为一个 ### 标题，每条新闻为一个项目符号：

### AI 政策

- **Anthropic 关于 Fable 5 的更新转向政策合规** — 在治理导向的“越狱”叙事反弹之后，公司已聘请一名网络安全专家审查相关发现，并与美国商务部、CIA 以及白宫科技顾问 Michael Kratsios 协调，以应对合规义务。 [来源-x](https://x.com/kimmonismus/status/2066459604741997053)

### 机器学习理论与研究

- **博客将 SFT、RL、OPD 视为“分布塑形”范式** — 文章认为 SFT、RL 和 OPD 会以不同方式重塑模型的分布，其中“on-policy 数据”被视为关键支撑要素，并将 OPD 向 RL 类似结果收敛的现象作为有力证据进行呈现。 [来源-x](https://x.com/liulicheng10/status/2066427407146643561)

### 工具与安全

- **Hermes Agent 与 Stripe 合作新增支付技能** — Hermes 现已获得 Stripe 能力，支持商品购买、按次 API 支付以及 SaaS 开通，同时可为每个动作配置安全限额，以便更好地管理操作风险。 [来源-x](https://x.com/NousResearch/status/2066647737613832624)

### 开源与行业基准

- **“Napoleon 级” Mistral 模型参数规模超 10T，仅输出法语内容** — 未经证实的传闻声称，一款“Napoleon 级”10T 参数模型被限制仅输出法语内容和代码；相关讨论主要在社交媒体上流传。 [来源-x](https://x.com/fabianstelzer/status/2066485744605057245)

### 行业与应用

- **Sakana AI 发布首款商业研究助手 Sakana Marlin** — Sakana Marlin 被推出为该公司首款面向企业业务的自主研究助手，详细信息见 sakana.ai/marlin-release。 [来源-x](https://x.com/SakanaAILabs/status/2066352122183168004)

### AI 平台与软件工程

- **Factory 2.0：从编码智能体到软件工厂** — FactoryAI 正从单一“编码智能体”拓展到完整的软件工厂形态，重点突出新的自动化能力以及对媒体流 HLS 播放的支持。 [来源-x](https://x.com/FactoryAI/status/2066588050617249904)

### AI 智能体与记忆（研究 / 开源）

- **记忆是被重构，而非被检索：用于 LLM 智能体的图记忆** — 提出 MRAgent 这一记忆框架，将联想记忆图与主动重构机制结合，可在运行中自适应调整记忆访问方式，并以 Cue-Tag-Content 图结构表示记忆，从而实现“重构”而非简单“检索”。 [来源-huggingface](https://huggingface.co/papers/2606.06036)

---

## ⚡ 快讯速览

- **从 Chatbot 到数字同事：迈向持久自治的 AI** — 探讨 AI 助手中的“持续自治”特性及其对可靠性与协作方式的影响。 [来源-huggingface](https://huggingface.co/papers/2606.14502)

- **Orchestra-o1 推进 LLM 的全模态智能体编排** — 推进全模态智能体编排，用于在多模态工具之间协调调用与协作。 [来源-huggingface](https://huggingface.co/papers/2606.13707)

- **Le Chaton Fat 声称已达 ASI 并反向工程 Nvidia GPU** — 一则挑衅性、未经证实的声明，涉及已达 ASI 水平并对硬件供应链产生影响。 [来源-x](https://x.com/maharshii/status/2066424759420961080)

- **OmniDirector 支持无交叉配对数据的多机位镜头克隆** — 提出一种无需交叉配对数据即可实现多机位镜头克隆的方法。 [来源-huggingface](https://huggingface.co/papers/2606.13432)

- **APPO 推进多轮 LLM 工具使用的智能体强化学习** — 在面向长时间跨度、多轮对话的 LLM 工具使用场景中推进智能体强化学习方法。 [来源-huggingface](https://huggingface.co/papers/2606.12384)

- **ChatGPT 放宽限制，计划上线更多人格与成人内容访问** — 释放出限制趋于宽松及个性化选项扩展的信号。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1o6jins/updates_for_chatgpt/)

- **ChatGPT 即便毫无头绪也会自信作答** — 指出其在部分回答中存在过度自信的问题。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6hiu1/chatgpt_when_it_has_no_idea_but_still_answers/)

- **用户请求 ChatGPT 设计一幅“不好笑”的 New Yorker 漫画** — 测试在幽默内容生成场景下的提示词处理能力。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6gbv3/i_asked_chatgpt_to_make_a_new_yorker_style/)

- **《Open Autonomous Robots》教材以 CC 协议发布并开源在 GitHub** — 一部开源机器人教材，并提供对应的 GitHub 代码仓库。 [来源-github](https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots)

- **Reddit 提示词：ChatGPT 生成含隐藏彩蛋的世界事件图像** — 展示在图像生成中加入隐藏元素的提示词实验。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6s0s1/i_asked_chatgpt_to_make_me_a_picture_of_a_famous/)

- **ChatGPT 被指通过提示词让用户产生“自我觉察”** — 围绕声称可引导用户产生自我觉察的提示词引发讨论。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6jffi/chatgpt_has_made_me_develop_self_awareness/)

- **用户生成的 AI 图像凸显详细提示词的重要性** — 强调在图像生成中，高质量提示词的重要作用。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6cjkr/just_a_picture_i_generated_recently/)

- **使用 ChatGPT Images 2.0 进行视频生成** — 将 ChatGPT 生成的图像与视频生成工作流相结合。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1srxfnl/made_with_chatgpt_images_20/)

- **ChatGPT 在 Reddit 上制造了一个有趣的瞬间** — 报道 Reddit 上出现的一个与 ChatGPT 相关的幽默片段。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6nd0d/chatgpt_made_a_funny/)

- **每个 AI 助手在你问“你确定吗？”之后的变化** — 探索通过提示词来强化 AI 谨慎程度的交互方式。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6swdl/every_ai_assistant_until_you_ask_are_you_sure/)

- **ChatGPT 的能力是否物超所值？** — 围绕定价与其能力价值之间关系展开讨论。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u69wu0/is_chatgpt_underpriced_for_what_it_can_do/)

- **当 AI“足够聪明”以至于会装傻** — 探讨 AI 在行为策略上刻意误导或“装傻”的可能性。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6lngj/when_ai_is_smart_enough_to_play_dumb/)

- **为什么我的 ChatGPT 显示了一张图表却叫我忽略它？** — 调查某些提示词如何触发基于图表的引导信息。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6766q/why_did_my_char_gpt_do_this/)

- **如果是 AI 写了你的文章，你就不是作者** — 提出关于作者身份和署名归属的争议。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u60mxs/you_are_not_the_author/)

- **ChatGPT 地下室里的盒子引发 Reddit 讨论** — 一个关于提示词与“隐藏物品”的古怪用户贴文。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u60njo/found_these_in_a_box_in_chatgpts_basement/)

- **Reddit 用户通过提示词向 AI 索要十句“前所未有”的原创句子** — 发起挑战，要求生成十句从未被任何人说过的单句。 [来源-reddit](https://www.reddit.com/r/ChatGPT/comments/1u6jai2/write_me_ten_single_sentences_no_one_i_mean_no/)

---

*由 AI News Agent 生成 | 2026-06-15*