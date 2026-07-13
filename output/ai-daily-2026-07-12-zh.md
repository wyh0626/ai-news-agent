---
title: "AI 日报 — 2026-07-12"
description: "GPT-5.6Sol领跑设计，6M用户Codex/ChatGPT放宽，插件库发布"
lang: "zh"
pairSlug: "ai-daily-2026-07-12"
---

# AI 日报 — 2026-07-12

> 涵盖 13 条 AI 新闻

## 🔥 今日焦点

### 1. GPT-5.6 Sol 登顶 Design Arena；Elo 1353

OpenAI 的 GPT-5.6 Sol 在 Design Arena 综合排名中位列第 1，Elo 评分达到 1353，整体表现优于 AnthropicAI 的 Claude Fable 5，并在前端设计性能上与 GLM 5.2 不相上下。此次更新相比 GPT-5.5 实现了排名提升 18 位、评分提升 60 分，并在偏好与速度之间建立了新的帕累托前沿，在该水平上比任何同级别模型都更快。 [来源-twitter](https://x.com/Designarena/status/2076391367446860249)

## 📰 重点报道

### LLM

- **Codex 和 ChatGPT Work：取消限额；GPT 5.6 Sol 效率提升；600 万用户** — 过去 48 小时内，Codex 和 ChatGPT Work 的更新包括：对 Plus、Business 和 Pro 套餐临时取消 5 小时使用上限。GPT 5.6 Sol 的效率优化将降低整体资源消耗并扩大可服务范围，具体影响还有待进一步量化。该服务的活跃用户数已达到 600 万，并将在一小时内进行一次使用额度重置。 [来源-twitter](https://x.com/thsottiaux/status/2076365965915467978)
- **OpenAI Plugins：Codex 插件示例仓库** — OpenAI 的 Plugins 仓库收录了 Codex 插件示例，每个插件都包含一个 .codex-plugin/plugin.json 清单文件以及可选的支持文件。仓库在 .agents/plugins/marketplace.json 和 .agents/plugins/api_marketplace.json 中定义了面向 API-key 登录的“应用商店”配置。值得关注的示例包括用于 Figma 的插件（use_figma）、Code to Canvas、Code Connect、用于规划与知识记录的 Notion 插件，以及用于 SwiftUI、AppKit/macOS 工作流和 Web 部署的构建工具套件。 [来源-github](https://github.com/openai/plugins)

### LLMs

- **追踪 Codex 在长时任务中的 Steer 行为** — Reddit 用户 foxtrot_north 报告称，Codex 的 steer 在处理长时任务时不会中断当前任务，而是将新输入追加到正在运行的任务中。他通过本地会话日志和一篇链接到 Substack 的分析文章记录了这一行为，并询问其他人是否在类似的智能体系统中也观察到相同现象。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uumoxi/tracing_how_steer_behaves_during_a_longrunning/)

## ⚡ 快讯速览

- **Anthropic 延长 Claude Fable 5 使用；Claude Code 限额 7 月维持上调** — Anthropic 宣布将在所有付费套餐中延长 Claude Fable 5 的可用时间，同时将 Claude Code 的周度调用上限在 7 月 19 日前继续维持在提高后的 150% 水平。官方将此描述为“对用户友好的延期”，但也引发了关于此类调整应通过订阅还是 API 进行的讨论，相关讨论串中对此次更新节奏与沟通方式表达了不满。 [来源-twitter](https://x.com/omarsar0/status/2076381743016276304)
- **OpenAI 发生了什么？Dean Ball 的 AI 政策反思** — Dean W. Ball 质疑 OpenAI 近期的动向，并指出 AI 政策研究往往需要繁重而彻底的调研工作。他表示，本周让他真正体会到这一点，将这一过程比作研读《塔木德》。这篇帖子预示着他将对 OpenAI 的行为展开更深入、以政策为导向的审视。 [来源-twitter](https://x.com/teortaxesTex/status/2076119293566079101)
- **Next AI Draw.io：在 Next.js 中用 AI 生成流程图** — 这个基于 Next.js 的 Web 应用将 AI 与 draw.io 流程图结合，通过自然语言指令与 AI 可视化辅助，实现图表的创建、修改和增强。该项目使用了在字节跳动 Doubao 赞助下提供的 glm-4.7 模型，并已在 GitHub 开源。 [来源-github](https://github.com/DayuanJiang/next-ai-draw-io)
- **Reddit 用户称 ChatGPT 记忆泄露破坏项目隔离** — 一位 Reddit 用户批评 ChatGPT 会将 Praana 项目的上下文泄露到其他无关对话中，而 Claude 则会将上下文严格限定在当前项目。帖子指出 ChatGPT 在用户体验层面存在记忆隔离缺陷，并呼吁改进，同时询问其他用户是否遭遇过类似问题。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uuk6zh/project_isolation_in_chatgpt_needs_serious/)
- **用户抱怨 GPT-5.6 过快速度导致额度飞速消耗** — 一位 X 用户表示，为了节省资源，他已将 GPT-5.6 的速度设置从高调为中，但使用额度仍然在快速消耗。他称 5 小时额度几乎已用尽，三次重置机会也全部耗完，并敦促 OpenAI 提升效率、减少使用瓶颈。 [来源-twitter](https://x.com/kimmonismus/status/2076249579188555907)
- **教授抓到多数学生在居家考试中用 ChatGPT 作弊** — 布朗大学经济学教授 Roberto Serrano 在校园于 12 月发生枪击案后，为缓解学生焦虑，允许他们将考试带回家完成。不久他就怀疑学生大规模使用 AI 作弊，因为期中考试平均分飙升到 96%，远高于往常 65–80 分的区间。此后他将期末考试改为线下举行，以遏制 AI 辅助作弊。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uulyci/this_professor_caught_the_majority_of_his/)
- **Pro 用户如何在日常中使用 ChatGPT** — 这篇 Reddit 帖子向拥有最高使用额度或 Pro 套餐的用户征集真实使用场景。由用户 /u/Savings-Wrongdoer-13 发起，邀请社区分享他们如何从高额度访问中获得价值。讨论旨在收集日常生产力场景及如何最大化利用 ChatGPT 的技巧。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uuop30/for_people_with_maximum_usage_pro_plans_what_do/)
- **“我解决了模型选择器问题”** — 一位 Twitter 作者声称自己已解决“model picker（模型选择器）”问题，并要求读者“不要谢我”。帖子还提到已启用 HLS 回放及可下载视频的选项，并引用了 “Tibo”。 [来源-twitter](https://x.com/maria_rcks/status/2076176709221552447)
- **用户用新语音模型练习英语，自称已是专家** — 一位 Reddit 用户发帖，分享自己使用新发布的语音模型练习英语，并自称已经成为专家。该帖发布在 OpenAI 子版块，并链接到与 AI 语音功能相关的其他讨论。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uujok7/im_practicing_english_with_the_new_voice_model/)

---

*由 AI News Agent 生成 | 2026-07-12*