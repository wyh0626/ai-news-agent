# AI 日报 — 2026-03-01

> 覆盖 26 条 AI 新闻

## 🔥 今日焦点

### 1. 华尔街日报：美国在对伊朗空袭行动中使用 Claude AI

《华尔街日报》报道，美中央司令部（CENTCOM）一直在使用 Anthropic 的 Claude AI 进行情报评估、目标识别以及在对伊朗行动中模拟战斗情景。该用法覆盖全球指挥行动，显示出人工智能工具在军事规划中的深度嵌入，CENTCOM 拒绝就具体系统发表评论。 [来源-twitter](https://x.com/nitashatiku/status/2027981676593484164)

### 2. GUI-Owl 1.5 发布原生 GUI Agent 家族

X-PLUG 的 Mobile-Agent 宣告 GUI-Owl 1.5，这是一个原生 GUI Agent 家族，覆盖 2B/4B/8B/32B/235B，具备 Instruct & Thinking，基于 Qwen3-VL 构建。它支持桌面、移动与浏览器自动化，声称在 20 多项 GUI 基准测试中处于行业前列，且端到端性能强劲。权重文件托管在 HuggingFace，并附有技术报告和 README；演示包括通过 Modelscope 和 Bailian 的 Mobile-Agent-v3.5 演示，提供有限的免费 API。 [来源-github](https://github.com/X-PLUG/MobileAgent)

---

## 📰 重点报道

### 大型语言模型（LLM）

- **Perplexity 能在数秒内实现AI驱动的投资组合管理** — Perplexity 能从一个提示生成一个极简风格的投资组合管理工具，能够为 100 多名客户提供仪表板与客户视图。过去需要数月时间和六位数预算的工作，如今可在数秒内完成，实质上实现了 AI 原生的金融基础设施的实时构建。这一开发预示着对传统财富科技应用模型的更大范围颠覆。 [来源-twitter](https://x.com/IndianTechGuide/status/2027987479752806499)
- **Qwen3.5-35B-A3B 能在 M4 笔记本上实现实时推理** — 据称，35B 参数模型 Qwen3.5-35B-A3B 能在 M4 芯片上本地运行，速度约为每秒 49.5 token，从而在笔记本上实现实时推理。该演示凸显了消费级硬件上本地 AI 能力的迅速提升，并暗示在边缘部署方面的更广阔潜力。 [来源-twitter](https://x.com/RoundtableSpace/status/2028141965355975139)
- **Perplexity Computer 使单人创业接近 10 亿美元估值** — Patrick Moorhead 称赞 Perplexity Computer，是他使用过的第一个平台，几乎实现端到端地让一个人创业接近 10 亿美元估值，关键在于匹配合适的模型与工具。他称赞其能够将模型与工具对齐以完成工作，称之为“令人印象深刻”。该贴来自 X（前身为 Twitter）。 [来源-twitter](https://x.com/PatrickMoorhead/status/2028089608559378846)
- **公开警告：在指责 30k 上下文模型前先检查 KV 缓存量化** — 长上下文本地代理（约 30k token）可能会产生幻觉或错误处理工具调用。作者认为，过度的 KV 缓存量化（在 llama.cpp 的 Q4/Q8 或 ExLlamaV3）往往才是真正原因，尽管对短上下文困惑度的影响不大。该贴引用 OpenClaw 测试中在 30k token 附近出现的 JSON 输出格式错误，并敦促在调整提示或精度前先检查 KV 缓存量化。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rhvi09/psa_if_your_local_coding_agent_feels_dumb_at_30k/)

### AI 代理

- **agent-browser 为桌面应用增加 Electron 控制** — 针对 agent-browser 的 Electron 技能使代理能够控制用 Electron 构建的桌面应用，包含 Discord、Figma、Notion、Spotify 和 VS Code。它还可用于调试 Electron 应用，并通过 npx skills add vercel-labs/agent-browser --skill electron（或 --skill slack 用于 Slack）来扩展编码代理。 [来源-twitter](https://x.com/ctatedev/status/2028128730132922760)

### AI 政策

- **DoW 对 Anthropic 的 SCR 指定的批评** — 一位 AI 政策倡议者认为，对 Anthropic 强制执行 SCR 指定将损害 AI 行业、国家及 Anthropic 本身。他强调降级、优先实现安全的超级智能与广泛受益分享，而非企业竞争，并敦促 DoW 尽管可能遭遇批评，仍应撤销这一决定。 [来源-twitter](https://x.com/sama/status/2027917750858092921)

### 开源

- **Nous Research 发布开源 Hermes Agent 供个人 AI 使用** — Hermes Agent 是一个完全开源的 AI agent，您可以将其安装在自己的机器上，连接您的消息账户，成为一个持续存在的个人助手，能够学习、构建技能并按计划执行任务。它通过 Nous Portal、OpenRouter，或您自己的 VLLM/SGLang 端点来支持多模型，提供基于终端的 UI（TUI），而非网页界面。由 Nous Research 开发，该项目支撑工具调用模型的数据生成与 RL 训练。 [来源-github](https://github.com/NousResearch/hermes-agent)
- **PaddlePaddle：来自中国的开源深度学习平台** — PaddlePaddle（飞桨）是最早的独立研发深度学习平台之一，自 2016 年起开源。它提供高性能的单机与分布式训练、跨平台部署，以及丰富的核心框架、库、工具与服务生态，服务于 2333 万开发者、76 万家公司和 110 万个模型。 [来源-github](https://github.com/PaddlePaddle/Paddle)

### AI 工具

- **Data.gouv MCP 服务器使 AI 聊天机器人能够访问数据集** — data.gouv.fr 的官方 MCP 服务器让 Claude、ChatGPT、Gemini 等 AI 聊天机器人能够通过对话搜索、浏览和分析法国家开放数据平台的数据集。公开实例 https://mcp.data.gouv.fr/mcp 提供无访问限制端点，便于自然语言查询数据集。 [来源-github](https://github.com/datagouv/datagouv-mcp)

### 硬件

- **逆向工程 Apple Neural Engine 训练 110M MicroGPT** — 一位作者声称通过使用 Claude 逆向工程 Apple Neural Engine 的私有 API，以绕过 Core ML，构建了一个定制的训练流水线，训练一个 110M 的 MicroGPT。他们认为 Apple Neural Engine 提供极高的功耗效率，并建议对 3B/7B 模型进行 LoRA 训练，且在集群上可进行更大规模的训练。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rhx5pc/reverse_engineered_apple_neural_engineane_to/)
- **AMD GPU 固件更新提升 Vulkan 性能，搭配 ROCm 与 llama.cpp** — 一则 AMD GPU 固件更新，结合新的 llama.cpp Vulkan 构建，据称在 Qwen3.5-35B-A3B-Q8_0 上实现了 Vulkan 性能的显著提升。测试在 Debian GNU/Linux 环境下进行，使用 ROCm 7.12 nightly 与支持 Vulkan 的 llama.cpp 构建，并显示出较此前 Vulkan 结果的改进。该帖还提及能效对比及旧版 Qwen3.5 配置下的较弱 Vulkan 性能。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ri6yhb/the_last_amd_gpu_firmware_update_together_with/)

---

## ⚡ 快讯速览

- **AGI 的涌现需要工程实现，而非纯理论** — Francois Chollet 指出，通过扩展算法得到的涌现性属性本质上不可预测，使得 AGI 更像是工程挑战而非纯理论挑战。他强调，AGI 的进展来自构建与发现，而非纯粹的形式化分析。 [来源-twitter](https://x.com/fchollet/status/2027950829525954935)
- **AI 在战争中的应用：高风险决策模型是否存在缺陷？** — 推文级批评认为，领导者可能将关键战争决策交由一个基础的 AI 来处理，类似于 Microsoft Clippy。主张寻求真相的 AI，并援引 Katie Miller 的 2 月 28 日发帖与 grok 账号，强调高风险军事决策中的安全问题。 [来源-twitter](https://x.com/NateSilver538/status/2028101089053008262)
- **Honor 将手机打造为集成 AI 机器人伴侣** — Honor 正在开发一款可作为 AI 机器人伴侣的智能手机，弹出式摄像头充当 AI 的“眼睛”。设想为一个持续运行的 AI 伴侣，能够担任助手。文章认为该想法有趣，但可能只是花哨的噱头，同时指出个人 AI 伴侣将逐步落地。 [来源-twitter](https://x.com/kimmonismus/status/2028158574900261177)
- **前 OpenAI 地缘政治团队负责人就 frontier AI 军事政策发表观察** — 一位前 OpenAI 地缘政治团队负责人就前沿 AI 公司及其军用政策发表了观察，基于其曾任职经验与国际安全研究者身份。相关笔记以 Twitter 帖子形式分享，并附有链接。 [来源-twitter](https://x.com/SarahShoker/status/2027975822704054544)
- **Anthropic 推出 Claude 内存导入，方便切换** — Twitter 一则预告贴强调通过内存导入功能实现切换到 Claude 的简易路径。该贴引导用户访问 claude.com/import-memory，暗示更易切换至 Claude 的内存能力。 [来源-twitter](https://x.com/i/status/2027904566696788225)
- **精选优秀 LLM 应用，结合 AI 代理与 RAG** — 汇集了基于 RAG、AI Agent 与多代理系统的 LLM 驱动应用，涵盖 OpenAI、Anthropic、Gemini、Google 与开源模型。展示了从代码助手到电子邮件工作流等实际演示，包含完善文档的项目与本地运行选项。仓库鼓励社区贡献，并重点说明赞助。 [来源-github](https://github.com/Shubhamsaboo/awesome-llm-apps)
- **Superset：面向 macOS 的 AI 代理时代的 IDE** — Superset 提供一个功能强大的终端，让开发者在本地运行 10+ 个编码代理（如 Claude Code、Codex），支持按任务的工作树隔离、并行代理执行、集中监控以及内置差异查看器以审阅变更，旨在提升开发吞吐量。该开源项目在 GitHub 上定位自己为管理单机 AI 代理的核心枢纽。 [来源-github](https://github.com/superset-sh/superset)
- **Sub2API 提供面向订阅的开源 AI API 网关** — Sub2API 是一个开源 AI API 网关，用于分发和管理 AI 产品订阅的 API 配额（如 Claude、OpenAI、Gemini、Antigravity）。它向用户签发 API Key，并处理认证、计费、负载均衡与请求转发。平台提供多账户管理、按 API Key 分发、按令牌级别的精确计费、智能调度及按用户并发控制；提供演示与 GitHub 源码。 [来源-github](https://github.com/Wei-Shaw/sub2api)
- **美军更偏好 Claude 而非 GPT，用户切换意愿强烈** — 文章认为美军对 Claude 的依赖程度高于 GPT，意味着实际用户将抗拒切换。警告称强制切换的领导者将遭遇反对，将此类情形比作 Copilot 在许多组织中被厌恶的情形。 [来源-twitter](https://x.com/signulll/status/2027972865576837240)
- **OpenAI 合同冲突：所有合法用途 vs 安全栈的争论** — 一条 Twitter 讨论指出 OpenAI 声称合同允许“所有合法用途”，但部署中的安全栈提供保护。作者警告若安全栈阻止了合法用途，合同可能被视为违约，涉及执行问题。讨论还推测未来可能与五角大楼就安全条款产生的合同纠纷。 [来源-twitter](https://x.com/peterwildeford/status/2027915494926225706)
- **Honor 将采用 Deepseek** — 一篇 Reddit 帖子称 Honor 将在设备中使用 Deepseek。该说法引用了 X 的状态，但未提供官方确认或详细信息。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ri0puh/honor_would_use_deepseek/)
- **批评者认为 AI 的表现令人失望** — X 上的一条推文对 AI 表现表达强烈负面情绪，称其表现让人失望。帖文未提供关于 AI 模型或情境的具体信息，反映公众对 AI 质量的挫败感。 [来源-twitter](https://x.com/i/status/2027906747290239201)
- **OpenAI 员工被分配到兼职公关岗位** — 一条 X 帖子指控 OpenAI 员工被分配到兼职公关岗位，并被要求公开为公司的决定辩护。发帖者表示遗憾，并希望公司尽快聘请全职公关人员。该项关注的是人事与沟通实践，而非 AI 研究或产品开发。 [来源-twitter](https://x.com/typedfemale/status/2028199628643176450)

---

*Generated by AI News Agent | 2026-03-01*