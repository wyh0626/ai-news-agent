---
title: "AI 日报 — 2026-06-13"
description: "美方暂停Fable5/Mythos5访问；Adaline2.0促自改循环。"
lang: "zh"
pairSlug: "ai-daily-2026-06-13"
---

# AI 日报 — 2026-06-13

> 共收录 30 条 AI 新闻

## 🔥 今日焦点

### 1. 美国指令暂停 Claude Fable 5 和 Mythos 5 的使用权限
一项来自美国政府的指令已经暂停所有用户对 Claude Fable 5 的访问，同时出口管制禁止向外国公民提供 Fable 5 和 Mythos 5，这迫使用户迁移到其他 Claude 模型。现有的 Fable 5 会话将报错，Claude Platform 对 Fable 5 的请求也会失败，加速了相关集成迁移的紧迫性。这一举措凸显了高调大模型所面临的监管风险，可能重塑厂商的产品和合规策略。[来源-x](https://x.com/ClaudeDevs/status/2065597942602531163)

### 2. Adaline 2.0 实现智能体自我改进闭环
Adaline 2.0 增加了一个自我改进层，可将运行轨迹转化为可执行行为，并自动暴露问题，进而生成自动化评估和数据。由此形成持续产生新智能体候选、再进行测试和优化的流水线。这一变化强调了在自治系统中，让观察、评估与部署之间形成更紧密的反馈闭环。[来源-x](https://x.com/arshdilbagi/status/2065826083224834345)

### 3. MiniMaxAI 发布 M3 权重；Anthropic 暂停 Fable 5/Mythos 5 访问
MiniMaxAI 在 Hugging Face 上发布了 M3 模型权重，延续其在开源方向上的推进。与此同时，Anthropic 宣布因出口管制而暂停向外国公民提供 Fable 5 和 Mythos 5 访问，其他 Claude 模型不受影响，并表示正努力恢复相关访问权限。这两件事并行发生，凸显了当下生态中开放性与监管约束之间的紧张关系。[来源-x](https://x.com/MiniMax_AI/status/2065645689582006333)

---

## 📰 重点报道

### AI 政策与监管
- **美国指令暂停 Claude Fable 5 和 Mythos 5 的使用权限** — 这项指令暂停了 Fable 5 的使用，并通过出口管制施压，释放出监管收紧的信号，也迫使各方制定新的迁移方案。[来源-x](https://x.com/ClaudeDevs/status/2065597942602531163)
- **Amazon CEO 与美国官员的会谈引发对 Anthropic 模型的严查** — 有报道指出，监管部门正对 Anthropic 模型展开协同行动式的审查，反映出政府对 AI 模型的监管关注正在升温。[来源-rss](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578?st=Yct6gx&reflink=desktopwebshare_permalink)
- **Amazon 研究人员被指与触发 Anthropic 严查的越狱报告有关** — 一则未经证实的说法称，一份关于模型越狱的报告与监管行动相关联，说明安全问题如何与政策决策交织在一起。[来源-x](https://x.com/skirano/status/2065808962176295178)

### 开源与工具
- **LMCache 扩展多节点共享，集成 NVIDIA Dynamo** — 这一快速 KV 缓存层新增多节点 CPU 内存共享能力，并与 Dynamo 集成，以进一步加速大模型推理。[来源-github](https://github.com/LMCache/LMCache)
- **GLM 5.2 上线；100 万上下文、MIT 协议权重下周发布** — GLM 5.2 提供了 100 万长度的上下文窗口和 MIT 协议的模型权重，预计很快将开放 API 访问以及更长上下文能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4nmpl/glm_52_is_deployed_in_glm_coding_plan_api_and_mit/)
- **AI 开源工具仓库在获得 730 万美元种子轮后被归档** — 仓库突然被归档，引发外界对 AI 开源项目在融资之后仍如何保持可持续性的疑问。[来源-github](https://github.com/tensorzero/tensorzero)

### 测评基准与数据集
- **WeaveBench：面向电脑操作智能体的长程混合基准** — 引入一个包含 114 个任务的基准，覆盖可视化桌面、CLI、编辑器、浏览器和各类工具，用于评估跨界面编排能力，并以真实用户请求和可验证产出为基础。[来源-huggingface](https://huggingface.co/papers/2606.09426)

### 行业与市场
- **有传闻称 Andrej Karpathy 或加入 Anthropic 获取 Mythos 做机器学习研究** — 这一猜测性报道讨论了访问控制如何可能影响机器学习实验环境与公司内部的人才流动与战略布局。[来源-x](https://x.com/theo/status/2065729219850842224)

---

## ⚡ 快讯速览

- **DeepSeek v4 Pro 拥有 1.6T 参数，却被质疑名不副实？** — 社区争论 1.6 万亿参数的 DeepSeek v4 Pro 是否真的能匹配其性能与成本投入。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4yvqy/deepseek_v4_pro_is_too_big_for_such_a_midrange/)
- **Diffusion Gemma 速度快 4 倍但错误多 6 倍** — 性能加速以显著牺牲准确率为代价，给在关键任务中的可靠性带来挑战。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4bne8/diffusion_gemma_is_4x_faster_but_makes_6x_more/)
- **德比郡一名警官因使用 AI 伪造证据被调查** — 该调查凸显了在法律程序中使用 AI 生成内容所带来的风险。[来源-rss](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)
- **PwC 报告：AI 正在推高医疗账单** — PwC 发现 AI 采用与更高医疗费用相关，引发关于政策与定价机制的新一轮讨论。[来源-rss](https://fortune.com/2026/06/12/ai-making-medical-bills-higher/)
- **如何在家用 AI 写代码又不被费用“掏空”** — 一篇关于低成本 AI 工具组合的实用讨论，聚焦在家编程的经济型方案。[来源-rss](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)
- **Paca：面向人机协作的轻量 Jira 替代品** — Paca 提供了一款强调人类与 AI 协作的轻量级项目管理工具。[来源-github](https://github.com/Paca-AI/paca)
- **开源 AI 必须获胜** — 一篇观点文章，主张开源应在 AI 发展中占据主导地位，以保障开放性与韧性。[来源-rss](https://opensourceaimustwin.com/?share=v2)
- **AI 核模拟游戏登上 arXiv 论文讨论** — 论文探索了由 AI 驱动的核模拟机制及其潜在影响。[来源-rss](https://www.kennethpayne.uk/p/shall-we-play-a-game)
- **Pi + Qwen3.6-27B 组合取代了我对 Claude Code 的需求** — 一套用 Pi 搭配 Qwen3.6-27B 的方案，展示了成本更友好的替代组合。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4ow2h/pi_setup_that_pretty_much_replaced_claude_code/)
- **提案：用 Torrent 网络镜像开源 AI 模型** — 有人倡议利用种子网络分发开源 AI 模型，以提升可获得性与抗审查能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4gto1/we_should_set_up_a_torrent_network_for_open/)
- **128GB BD-R XL M-Disc 成为顶级消费级档案存储介质** — 文章介绍了适用于长期 AI 数据归档的存储介质选择。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4rarz/i_dont_know_who_needs_to_hear_this_but_128gb_bdr/)
- **WIP：EAGLE3 与 Qwens 的集成** — 正在推进 EAGLE3 与 Qwens 的集成工作，以扩展其能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u5278u/wip_eagle3_for_qwens/)
- **兽人圈用户对 GPT-4o 下线的反应** — 这一社区对 GPT-4o 被移除的反应，引发关于访问权与替代方案的讨论。[来源-x](https://x.com/udiWertheimer/status/2065644382548574386)
- **对搭建 LLM 种子站点的兴趣引发协作讨论** — 有关建立一个基于 Torrent 的大模型共享站点的呼吁正在促成社区协作。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4xiw8/interest_in_an_llm_torrent_site/)
- **中国开源大模型即将迎来重要更新** — 社区预期中国开源 LLM 即将推出新版本，带来性能提升。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4wy3p/this_is_coming_to_chinese_open_source_models/)
- **Fable 被禁后，社区开始讨论下载 Qwen3.7 AGI 模型** — 对 Fable 的封禁引发了关于 Qwen3.7 AGI 模型可用性的热议。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u4l98a/when_fable_gets_banned_but_its_ok_because_youve/)
- **第二块 P40 让 Goblin Box 拥有 48GB 显存** — 硬件升级使本地可运行更大规模的 AI 任务成为可能。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1u533by/me_after_installing_my_second_p40_into_my_goblin/)
- **美国不再是建设 AI 实验室的最佳地点？** — 围绕美国在 AI 实验室基础设施方面吸引力的争论正在加剧。[来源-x](https://x.com/theo/status/2065622694113235359)
- **新版测试中的 Claude Code 模型切换器** — 新的测试版工具让在不同 Claude Code 模型间切换更加便捷。[来源-x](https://x.com/southpolesteve/status/2065773518025793761)
- **最新 Fable 评测得分公布** — 更新后的 Fable 评测成绩为其性能表现提供了新的参考视角。[来源-x](https://x.com/banteg/status/2065741346095165555)

---

*由 AI News Agent 生成 | 2026-06-13*