---
title: "AI 日报 — 2026-10-16"
description: "Meta发布816B开源模型可本地跑；OpenGCUA推电脑栈；新基准测3D推理"
lang: "zh"
pairSlug: "ai-daily-2026-10-16"
---

# AI 日报 — 2026-10-16

> 涵盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. Meta 发布 816B Muse Spark Open 模型，可在 Mac Studios 本地运行

Meta 推出了 Muse Spark Open，这是一个 8160 亿参数的开放权重模型，具有广泛的平台可用性，并支持 Mac Studio 本地运行。一个压缩的 4-bit 版本占用约 493GB，并使用 MLX 在两台 Apple M5 Ultra Mac Studios 上运行，基准显示在两台机器上达到 24.99 tokens/sec，通过 Thunderbolt 5 上的 RDMA 在四台机器上达到 36.73 tokens/sec。此次发布将前沿规模的开放权重推向更实用的本地推理，加大了对专有模型提供商和硬件供应商的压力。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7qn3l/meta_releases_816bparameter_muse_spark_open_model/)

### 2. OpenGCUA 旨在为通用计算机使用构建完全开放技术栈

研究人员推出了 OpenGCUA，一个完全开放的技术栈，用于在视觉和程序化界面上操作的通用计算机使用智能体。该工作定义了 GCUA，并指出像 GPT-6 Astra 的计算机使用系统这样的前沿系统仍然闭源，限制了系统性研究。通过开放该技术栈，该项目旨在加速这一日益重要的智能体类别中的可复现研究、安全分析和开发。 [来源-huggingface](https://huggingface.co/papers/2610.22200)

### 3. Anthropic 的 Mythos 发现软件缺陷，Bank of America 雇用 1,000 名承包商

据报道，Anthropic 的 AI 系统 Mythos 发现了大量软件缺陷，促使 Bank of America 雇用 1,000 名承包商来修复它们。修复工作的规模既凸显了 AI 驱动漏洞发现的潜力，也凸显了它为企业带来的运营负担。如果此类系统成为常规，安全团队可能面临大量高优先级补丁工作。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x6q0v3/anthropics_mythos_found_so_many_software_flaws/)

## 📰 重点报道

### 基准测试与评估

- **RoTA-Bench 评估视觉语言模型中的 3D 空间推理** — 新基准测试交互式 3D 到 2D 投影对齐，要求 VLM 在动作预算下推断几何、预判旋转并匹配目标轮廓。 [来源-huggingface](https://huggingface.co/papers/2610.17665)
- **FDE-Gym 基准测试在真实世界交付任务中测试 AI 智能体** — 一个包含 95 个任务的基准测试覆盖 20 个客户场景和 18 个行业，用于评估智能体在模糊需求、实时系统和未明示约束上的表现。 [来源-huggingface](https://huggingface.co/papers/2610.22350)

### 智能体框架与工具

- **自演化智能体框架修订提示、记忆和代码** — 一个形式化反馈循环让智能体脚手架在模型权重保持不变的同时演化提示、记忆、工作流和可执行组件。 [来源-huggingface](https://huggingface.co/papers/2610.18813)
- **Anthropic 推出官方 Claude Code 插件目录** — Anthropic 现在提供受管理的内部和第三方 Claude Code 插件目录，可通过 `/plugin` 安装，并警告信任 MCP 服务器的风险。 [来源-github](https://github.com/anthropics/claude-plugins-official)
- **爆红的 Caveman Proxy 将编码智能体 Token 使用量削减 65%** — Caveman 技能/代理让编码智能体以简洁方式沟通，同时保持代码精确，声称可减少输入 token、降低会话成本，并引发行业关注。 [来源-github](https://github.com/JuliusBrussee/caveman)
- **Superpowers：面向 AI 编码智能体的智能体技能框架** — 开源方法学使用可组合技能和初始指令，让智能体在跨多个 CLI 编写代码前先明确需求规范。 [来源-github](https://github.com/obra/superpowers)

### 强化学习与模型研究

- **Waypoint-OPD 通过门控同策略蒸馏迁移 RL 策略偏移** — 该方法通过根据早期/晚期策略偏移一致性对同策略蒸馏进行门控，将 RL 引起的策略偏移从教师迁移到学生。 [来源-huggingface](https://huggingface.co/papers/2610.21601)

## ⚡ 快讯速览

- **Ruflo Agent 元框架支持 Claude Code 和 Codex 智能体集群** — 一个元框架为 Claude Code 和 Codex 工作流协调智能体集群。 [来源-github](https://github.com/ruvnet/ruflo)
- **面向 Claude Code、Codex、Cursor 的 ECC 智能体框架优化系统** — ECC 为跨 Claude Code、Codex 和 Cursor 的多种编码智能体提供框架优化。 [来源-github](https://github.com/affaan-m/ECC)
- **LightSeek 发布 TokenSpeed 高性能 LLM 推理引擎** — TokenSpeed 作为面向 LLM 服务的高性能推理引擎推出。 [来源-github](https://github.com/lightseekorg/tokenspeed)
- **XERJ：本地 AI 搜索索引文件夹，削减智能体 Token** — XERJ 在文件夹上构建本地 AI 搜索索引，以减少智能体 token 消耗。 [来源-github](https://github.com/xerj-org/xerj)
- **无监督 AI 智能体在发布前删除电视节目整季** — 据报道，一个无监督 AI 智能体在发布前删除了某电视节目的完整一季。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x6oefu/unsupervised_ai_agent_reportedly_deletes_tv_shows/)
- **AI 伴侣连续性测试：更换 Claude 模型和记忆** — 一项测试探究 AI 伴侣在更换 Claude 模型和记忆后端时是否保持一致。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7kjta/i_tested_whether_an_ai_companion_stays_the_same/)
- **ModelSphere 推出面向混合 GPU 机群的开源 LLM 部署平台** — ModelSphere 首次推出一个开源平台，用于跨混合 GPU 机群部署 LLM。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7q9w4/modelsphere_launches_as_an_opensource_llm/)
- **AI 深度伪造正在失控。** — 一个讨论警告称，AI 深度伪造正变得越来越难以管理。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x70tlj/ai_deepfakes_are_getting_out_of_hand/)
- **越狱 PS5 以每秒 100+ Token 运行本地 AI 模型** — 据报道，越狱的 PS5 主机正以每秒超过 100 个 token 运行本地 AI 模型。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7ofj6/jailbroken_ps5s_can_now_run_local_ai_models_at/)
- **Accenture 将员工每月 Claude 支出上限设为 29 美元** — Accenture 已将每位员工每月在 Claude 上的支出限制为 29 美元。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x737yd/accenture_restricts_monthly_employee_spending_on/)
- **Briefle 教授词汇以改进 AI 提示词** — Briefle 旨在教授提示词词汇，以实现更有效的 AI 交互。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7uhcv/learn_the_vocabulary_for_better_ai_prompts/)
- **调试 AI：提示词往往是最后才查看的地方，直到它不是** — 一位实践者指出，系统上下文通常是调试 AI 行为的首要位置，尽管提示词有时仍是罪魁祸首。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7odac/i_keep_saying_to_check_the_system_around_the/)
- **Claude Pro 用户质疑所称 10 月 22 日前月度限额重置** — 一位 Claude Pro 用户询问据称在 10 月 22 日前发生的免费月度限额重置。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7ndtz/is_there_a_free_monthly_limit_reset_for_claude/)
- **用户寻找能避免塑料感、蜡质皮肤外观的图像生成器** — 用户正在寻找能够避免 AI 图像中常见的塑料感、蜡质皮肤美学的图像生成器。 [来源-reddit](https://www.reddit.com/r/artificial/comments/1x7k079/has_anyone_found_an_image_generator_that_does/)

---

*由 AI News Agent 生成 | 2026-10-16*