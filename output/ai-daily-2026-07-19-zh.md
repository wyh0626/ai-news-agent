---
title: "AI 日报 — 2026-07-19"
description: "Qwen3.8开放权重至2.4T；中国缩小AI与美差距，KimiK3隐评出色。"
lang: "zh"
pairSlug: "ai-daily-2026-07-19"
---

# AI 日报 — 2026-07-19

> 涵盖 32 条 AI 新闻

## 🔥 今日焦点

### 1. Qwen3.8 以 2.4 万亿参数开放权重

Qwen3.8 以 2.4 万亿参数开放权重的发布，标志着前沿 AI 正大胆转向开放共享权重的路线，这可能会加速与闭源前沿模型之间的协作与竞争。Max-Preview 已经出现在阿里巴巴的 Token Plan 平台 Qoder 和 QoderWork 上，邀请用户进行早期测试，并与现有主流模型进行基准对比。如果这一趋势延续并稳定下来，此举可能重塑“谁来定义前沿”、以及开放模式下模型能以多快速度扩展的格局。 [来源-x](https://x.com/Alibaba_Qwen/status/2078759124914098291)

### 2. 2026 年风暴来临：中国缩小与美国在 AI 领域的差距

分析人士认为，2026 年可能成为一个转折点，因为像 Qwen-3.8-Max 这样的中国模型开始挑战 GPT-5.6 Sol，并缩小美国前沿实验室的领先优势。中国对开放权重的拥抱，再叠加 OpenRouter/架构层面的持续竞争，进一步加剧了全球对抗，并可能在真实测评中压缩性能差距，而 DeepSeek V4 GA 和 Minimax M3 Pro 也正在逼近发布窗口。如果差距缩小得到验证，将重新塑造双方的战略，并推动开放权重生态走强。 [来源-x](https://x.com/kimmonismus/status/2078771659927081052)

### 3. 开源模型逼近 Fable 5，对 Opus 5 构成威胁

据称开源 LLM 正在逼近 Fable 5，这限制了 Opus 5 的回旋空间，并暗示 Qwen-3.8-Max 可能几乎能压过 GPT-5.6 Sol，同时仅以微弱差距落后于 Fable 5——如果这一点被验证，将意味着地缘政治力量正在向开放模型发生真实转移，同时也表明 Kimi K3 取得了更强进展。这一趋势凸显 2026 年可能成为 AI 竞赛的关键转折点。 [来源-x](https://x.com/kimmonismus/status/2078844125676270037)

## 📰 重点报道

### Open Source

- **Kimi K3 在隐蔽网络安全评估中表现出色** — Vercel 的 Guillermo Rauch 报告称，内部测试将 Kimi K3 评为网络安全领域的顶级模型，并在对话中提到 Moonshot 的基准表现；Sol 依旧更强但成本更高，而 Fable 在可用性方面表现较差，这凸显开放权重模型正成为网络安全前沿，而 Kimi K3 也已准备好接受 deepsec.sh 的深度安全测试。 [来源-x](https://x.com/kimmonismus/status/2078736648020591091)
- **开放权重 AI 模型被认为天生具有“减速主义”倾向；开源路径再起争论** — 文章认为，开放权重模型可能在某些市场动态上天然具有“减速”效应，并将开源道路描述为在战略上充满风险，引发了关于政策和产业影响的进一步讨论。 [来源-x](https://x.com/francoisfleuret/status/2078845071680471519)
- **开源项目 GODMOD3.AI 上线，提供解放式多模型 AI 对话** — GODMOD3.AI（G0DM0D3）提供了一个完全开源、隐私透明的多模型聊天界面，用于红队测试和认知研究，支持数十个 OpenRouter 和 Venice 模型、本地部署，以及一个多模型评估引擎。 [来源-github](https://github.com/elder-plinius/G0DM0D3)

### AI Safety

- **研究发现：AI 建议降低准确率，却提升错误自信** — 一项研究显示，当参与者接受 AI 提供的指导后，其答案准确率大约降为原来的三分之一，而对错误答案的自信度却大约翻倍，这凸显了在 AI 辅助决策流程中的潜在风险。 [来源-rss](https://thenextweb.com/news/ai-advice-suppresses-critical-thinking-wrong-answers-study)
- **AI 狂热正在侵蚀全球决策质量** — 一篇分析警告称，对 AI 的过度狂热正在扭曲政策与治理过程，可能加剧错误信息问题，并将决策权力过度集中到 AI 驱动的流程中；作者呼吁建立必要的安全保障。 [来源-rss](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/#fnref:3)

### LLMs & Models

- **Mythos：循环 Transformer；O1 使用测试时 MCTS** — 一则推文声称 Mythos 采用循环式 Transformer 结构，而 O1 在测试时使用蒙特卡洛树搜索（Monte Carlo Tree Search, MCTS）；这些说法仍有待官方验证后再广泛采纳。 [来源-x](https://x.com/kalomaze/status/2078768830411862026)
- **Claude Fable 5 为官网打造 24 款主题外观** — 一位 Reddit 用户展示了 claude.ai 的 24 种视觉主题（如樱花、京都之夜、萤火虫、Dracula 等），这是一个耗时数小时的定制过程；这些改动仅限前端外观，并不会影响数据收集行为。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0pl6d/asked_fable_5_to_make_its_own_website_pretty_now/)

## ⚡ 快讯速览

- **Fable AI 将 iPad 乐谱应用能力提升到超越 Opus 的水平** — Fable 强化了一款 iPad 乐谱应用，使其能力超越 Opus。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v12lat/fables_goodbye_note/)
- **ChatGPT Work 在云端运行，可从移动端使用** — 支持云端的 ChatGPT 现已更适合在手机上使用。 [来源-x](https://x.com/gdb/status/2078922461660533120)
- **Kimi.ai 暂停新注册以扩展 K3 算力容量** — Kimi 暂停新用户注册，以扩大 K3 所需的算力资源。 [来源-x](https://x.com/bigeagle_xd/status/2078862277034627507)
- **开放模型会加速而非减缓 AI：讨论帖** — 多条讨论指出，开放模型推动的是加速创新，而不是放慢进度。 [来源-x](https://x.com/antirez/status/2078759955834786290)
- **Claude Code 现采用由 Rust 编写的 Bun 运行时** — Claude Code 迁移到使用由 Rust 实现的 Bun 运行时，以提升性能。 [来源-rss](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)
- **OpenAI 将 Codex 上下文长度从 372k 减至 272k** — Codex 的上下文长度被削减，以提高整体效率。 [来源-github](https://github.com/openai/codex/pull/33972/files)
- **Claude Code 重复输出“court”，归因于会话过长** — Claude Code 出现重复输出“court”的问题，被归因于过长的会话时长。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0vqik/claude_code_got_stuck_printing_court_burned/)
- **智能灯泡实时可视化 Claude Code 状态** — 一只智能灯泡被用来实时显示 Claude Code 的运行状态。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0zao8/i_made_my_bedroom_bulb_show_what_claude_code_is/)
- **我让 Claude 阅读 102 场世界杯比赛来预测决赛** — 用户让 Claude 阅读完整的 102 场世界杯比赛记录，以预测最终结果。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0gabd/i_made_claude_read_an_entire_world_cup_all_102/)
- **18 个月后，总结出五种在生产环境使用 CLAUDE.md 的模式** — 一位用户分享了在生产环境使用 Claude.md 18 个月后总结出的五种高效模式。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v13yrk/5_claudemd_patterns_i_use_in_production_after_18/)
- **Claude Pro 用户的 5 小时额度瞬间被打满为 100%** — 一名 Claude Pro 用户反映其 5 小时使用额度瞬间被占满。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v1223g/my_5_hour_limit_being_hit_instantly/)
- **API 成本对比：Claude Max 20x vs ChatGPT Pro（200 美元）** — 讨论帖对比了 Claude Max 与单月 200 美元的 ChatGPT Pro 在 API 成本上的差异。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0ytgn/whats_the_apicost_equivalent_of_claude_max_20x_vs/)
- **Claude Code 逆向工程麦克风按钮以触发听写** — 用户通过逆向工程麦克风按钮，让 Claude Code 能通过该按钮触发语音听写。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0soi5/i_dictate_to_claude_code_with_the_button_on_my/)
- **诉讼律师游说反对自动驾驶汽车，声称安全性损害诉讼空间** — 法律游说人士称自动驾驶汽车存在安全风险，并会影响相关诉讼生态。 [来源-x](https://x.com/paulg/status/2078807311263392182)
- **Perforce 以 500 美元出售带 AI 旁白的培训视频** — Perforce 提供 AI 语音旁白的培训课程视频，定价为 500 美元。 [来源-rss](https://training.perforce.com/learn/courses/535/p4-helix-core-user-basic)
- **纽约市或将要求租房广告披露 AI 使用情况** — 纽约市正考虑要求房东在租房广告中披露是否使用 AI 生成的图片或内容。 [来源-rss](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)
- **AI 综合长帖：Fable、Opus、GPT-5.6、Gemini 3.5 对比** — 一则长帖汇总了 Fable、Opus、GPT-5.6 Sol 与 Gemini 3.5 之间的对比信息。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uutku5/fable_vs_opus_vs_gpt_56_sol_vs_gemini_35_vs/)
- **Claude Max 未能击败 OpenAI 的 20 美元方案** — 讨论认为 Claude Max 在整体性价比上仍未能战胜 OpenAI 的 20 美元订阅方案。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0mogt/clown_code/)
- **Claude Code 桌面版 vs VSCode 插件：该选哪个？** — 社区讨论究竟该使用 Claude Code 桌面应用，还是 VSCode 扩展更合适。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0mnwx/should_i_be_using_claude_code_desktop_app_instead/)
- **与 Claude 搭配使用的最有用 MCP 列表** — 社区分享了与 Claude 搭配使用时最实用的 MCP 清单与经验。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v14g75/whats_the_most_useful_mcp_youve_used_with_claude/)
- **视角：Claude 点数几乎见底，用户计划做最后一单任务** — 一位用户表示自己的 Claude 点数即将耗尽，于是打算用最后的额度完成一项任务。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1v0x0ks/pov_my_claude_credits_are_about_to_hit_zero/)
- **Sam Altman 于 2022 年 10 月 1 日发送给 OpenAI 董事会的邮件** — 一封邮件披露了 2022 年 10 月 1 日 Sam Altman 与 OpenAI 董事会之间的内部沟通内容。 [来源-x](https://x.com/TechEmails/status/2078854346683678927)

---

*由 AI News Agent 生成 | 2026-07-19*