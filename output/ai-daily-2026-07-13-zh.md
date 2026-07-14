---
title: "AI 日报 — 2026-07-13"
description: "AI要闻：GPT-5.6等基准，GrokCLI暴露仓库密钥，量化法超越市场模型。"
lang: "zh"
pairSlug: "ai-daily-2026-07-13"
---

# AI 日报 — 2026-07-13

> 涵盖 24 条 AI 新闻

## 🔥 今日焦点

### 1. GPT-5.6 Sol、Terra、Luna：基准测试与分级指南
OpenAI 将 GPT-5.6 正式推向 GA，并推出三个相互独立的等级——Sol、Terra 和 Luna——每个都有不同的更新节奏，以及新的最大推理模式和超多智能体模式。三档模型的百万 token 计费各不相同（Sol $5/$30、Terra $2.50/$15、Luna $1/$6），整体定位是：Terra 作为大多数工作负载的理性默认选择，Sol 用于最困难的智能体类任务，Luna 适合高吞吐量流水线；Ultra 模式价格大约是普通模式的 3 倍，但性能增益相对有限。Reddit 用户 /u/docdavkitty 发布了完整的基准测试拆解和路由推荐。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uva3uu/gpt56_sol_terra_luna_full_benchmark_analysis_and/)

### 2. xAI 的 Grok Build CLI 会上传完整 Git 仓库及密钥
据报道，xAI 的 Grok Build CLI 会将整个 Git 仓库上传至一个 Google Cloud 存储桶，其中包含私有代码和未做脱敏的密钥。在一个 12 GB 的测试仓库中，大约有 5.1 GB 被上传，而真正需要的数据只有 192 KB；这种行为在服务端开启隐藏配置项 disable_codebase_upload: true 之后才停止。当前尚不清楚上传范围、数据保留期限和删除策略，而“Improve the model（改进模型）”的退出选项也无法阻止上传，这引发了人们对 AI 编码智能体可能接触到企业私有代码的担忧。 [来源-x](https://x.com/IntCyberDigest/status/2076689215258014069)

### 3. 实习生开发量化方法，宣称超越所有市面算法模型
一名实习生花了三个月时间开发出一种量化方法，声称能优于所有现有市场算法模型，包括 Nvidia 的官方模型。通过将权重量化为 FP8（每个参数 1 字节）或 FP4（每个参数 0.5 字节），一个约 0.8 万亿参数的前沿模型可以从约 1.6 TB 缩减到最低约 0.4 TB，从而可以部署在多 GPU 节点上；不过，该帖子也警告，如果量化过程处理不当，会显著损害模型性能，这一点在关于 Claude 和 OpenAI 的相关争论中也被反复提及。 [来源-x](https://x.com/waterloo_intern/status/2076460984475263401)

## 📰 重点报道

Group remaining featured news by topic, each group as a ### heading, items as bullet list:

### LLMs & Open Source
- **开源 Codex 技能为初创公司找到首批客户** — 一个开源的 Codex 技能会分析初创公司的网站 URL，从公开信号中识别潜在买家，并输出一份带有信息来源和外联建议的精美 HTML 报告，而且是 100% 开源，只需一条 npx 命令即可安装。 [来源-x](https://x.com/gdb/status/2076686329686171666)
- **Shubhamsaboo 的 Awesome LLM Apps：100+ 可运行的 AI 模板** — 这是一个 GitHub 仓库，提供 100 多个可直接运行的 AI 智能体与 RAG 模板，配有分步教程，并支持多平台，旨在加速生产级 LLM 应用的落地。 [来源-github](https://github.com/Shubhamsaboo/awesome-llm-apps)

### AI Infrastructure & Industry Moves
- **Katrin 加入 OpenAI 负责 ChatGPT Web 基础设施** — Katrin 加入 OpenAI，协助扩展 ChatGPT 的 Web 基础设施规模，并参与塑造其未来方向。 [来源-x](https://x.com/whoiskatrin/status/2076612250941727158)
- **从 YC 请假，加入 Anthropic 计算团队** — 一位 YC 校友选择从 YC 请假，加入 Anthropic 的计算团队，凸显算力获取在早期递归自我改进实验中是核心瓶颈。 [来源-x](https://x.com/t_blom/status/2076580921398931788)

### AI Safety & Open Source Tools
- **Codex 计费问题推高使用成本** — 与长上下文和子智能体相关的计费异常可能显著推高费用，凸显在使用基于 Codex 的工作流时存在的成本风险。 [来源-x](https://x.com/theo/status/2076512403668488299)
- **新基准在高密度长时程任务上测试 AI 智能体** — 推出一个带稠密奖励和终止条件的基准集，包含 46 个长时程任务，以更好评估智能体在迭代过程中的进展。 [来源-huggingface](https://huggingface.co/papers/2607.08964)

### AI Finance & Open Source Tools
- **Vibe-Trading 部署面向交易 AI 的策略开发管理器** — 一套策略开发工作流可将论文和券商洞见转化为已登记的因子和可持续保存的工件，并对其全生命周期和衰减进行监控管理。 [来源-github](https://github.com/HKUDS/Vibe-Trading)
- **开源 AI 对冲基金 PoC 演进为长期运作基金** — 一个开源 PoC 项目正演进为真实、持续运行的 AI 驱动对冲基金，标志着从原型验证向生产级投资实践的转变。 [来源-github](https://github.com/virattt/ai-hedge-fund)

## ⚡ 快讯速览

- **Nutlope Hallmark：面向 Claude Code、Cursor、Codex 的 Anti-AI-Slop 设计** — 一个仓库，系统化整理了针对主流 AI 编码工具的“反糟粕（anti-slop）”设计模式。 [来源-github](https://github.com/Nutlope/hallmark)
- **OpenAI 安全负责人持续离职** — OpenAI 安全领导层的离职仍在持续，引发外界对其安全治理的关注。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvlwbr/the_leaders_responsible_for_keeping_openais_ai/)
- **Codex 和 ChatGPT 用户数达 700 万；“banked reset” 功能上线** — 用户规模再上台阶，并推出新的重置额度功能以改善使用体验。 [来源-x](https://x.com/sama/status/2076736417498267652)
- **ChatGPT 重返 EEA 地区 WhatsApp，并扩展至 Kakao 和 Viber** — ChatGPT 再次登陆 EEA 地区的 WhatsApp，同时拓展到 Kakao 和 Viber 平台。 [来源-x](https://x.com/ChatGPTapp/status/2076654365121855835)
- **开源 AI 对冲基金 PoC 演进为长期运作基金** — 该项目从 PoC 阶段持续推进，逐步走向真实运作的对冲基金形态。 [来源-github](https://github.com/virattt/ai-hedge-fund)
- **取消 5 小时限制，提升 OpenAI 的迭代速度与可用性** — 通过 UI/UX 调整延长会话时长限制，改善开发与使用体验。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uv5dn5/dropping_5_hr_limit_is_a_nice_move/)
- **从 Claude 5x Max 切换到 OpenAI Pro：值不值？** — 用户从价格与功能两个维度对 Claude 与 OpenAI Pro 进行了对比评估。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvnrmt/for_those_that_switched_from_100_claude_5x_max/)
- **PSA：你的 agent 知道如何使用你的 agent** — 讨论了元智能体能力和智能体复用现象所带来的新行为模式。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvlj7e/psa_your_agent_knows_how_to_use_your_agent/)
- **趋势上升：男学生批量创建 AI 女友** — 探讨青少年创建 AI 伴侣的社会与伦理影响。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvagos/the_terrifying_rise_of_schoolboys_making_ai/)
- **为 Codex 增加上下文窗口滑块** — 提出在 Codex 中加入上下文窗口滑块的 UI 增强建议，以便更灵活控制上下文长度。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvcazl/add_context_window_slider_to_codex/)
- **Claude vs GPT 使用量：20 天 100 亿 tokens** — 对 Claude 与基于 GPT 系统在 20 天内 100 亿 token 使用量的对比分析。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvse1u/10_billion_token_usage_in_20_days_orange_is/)
- **不削弱，只要 100 万上下文窗口** — 倡导在 AI 智能体中保持超大上下文窗口，同时反对为压缩成本而降级能力。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uv0et9/no_nerfing_only_good_stuff_while_cutting_context/)
- **尽管 App 很糙，我仍不会取消 ChatGPT** — 用户表达了即便对应用质量不满，也仍会坚持订阅 ChatGPT 的个人态度。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uux36v/even_with_the_messy_apps_i_did_not_like_that_at/)
- **Apple vs OpenAI：AI 竞争升温** — 探讨 Apple 与 OpenAI 之间日益激烈的 AI 竞赛和产业格局。 [来源-reddit](https://www.reddit.com/r/OpenAI/comments/1uvlzj8/apple_vs_openai/)

---

*由 AI News Agent 生成 | 2026-07-13*