---
title: "AI 日报 — 2026-06-03"
description: "微软披露MAI报告透明后训练模型，发布Scout与Gemma 4 12B。"
lang: "zh"
pairSlug: "ai-daily-2026-06-03"
---

# AI 日报 — 2026-06-03

> 收录 31 条 AI 新闻

## 🔥 今日焦点

### 1. Microsoft MAI 报告披露透明的后训练模型

Microsoft 发布的 MAI 技术报告因高度透明而备受赞誉，详尽描述了在无需任何合成数据或蒸馏的情况下进行后训练学习的过程。报告给出了各迭代阶段精确的 MFU（机器浮点利用率）数据，并分享了一整套可复现的 scaling ladder（规模扩展）配方，显示出其在前沿研究上的严肃投入以及对整个模型系列的完全掌控。Mustafa Suleyman 预告了 7 个全新的 MAI 模型，意味着一次大胆且可能重塑行业格局的发布节奏。[来源-twitter](https://x.com/eliebakouch/status/2061965825037254947)

### 2. Microsoft 发布 Scout：基于 OpenClaw 的自主 AI Agent

Microsoft 宣布推出 Scout，这是一款基于 OpenClaw 框架构建的自主 AI agent。此举凸显了其向能够在有限人工干预下独立完成任务的智能体方向推进，表明公司在各类产品和服务中部署自主 AI 工具的更宏大野心。[来源-hackernews](https://www.computerworld.com/article/4180103/microsoft-unveils-scout-an-autonomous-ai-agent-built-on-openclaw.html)

### 3. Gemma 4 12B：为笔记本打造的无编码器多模态 AI

Gemma 4 12B 推出了一种统一的、无编码器（encoder-free）多模态模型，旨在直接在笔记本电脑上运行高性能智能推理。该模型以 Apache 2.0 许可证发布，强调端侧高效与高级推理能力。公告特别指出，Gemma 4 12B 能够为边缘设备带来强大的多模态能力，打通本地运行与高阶多模态理解之间的连接。[来源-twitter](https://x.com/googlegemma/status/2062202706882883696)

## 📰 重点报道

### 开源

- **Ideogram 4.0 开源图像模型连同权重一同发布** — Ideogram 宣布发布 Ideogram 4.0，并将其称为目前最好的开源图像模型。本次发布允许用户下载模型权重、在自有数据上进行微调，并在本地硬件上运行。该模型已在所有 Ideogram 订阅计划和 Ideogram API 上线，并支持 HLS 播放功能。[来源-twitter](https://x.com/ideogram_ai/status/2062202208700313872)

### LLM

- **OpenAI 将 ChatGPT、Codex 和 Atlas 合并进桌面应用** — OpenAI 计划把 ChatGPT、Codex 以及 Atlas 浏览器整合到一个统一的桌面应用中，并将 Codex 从“编程工具”重新定位为“生产力平台”。公司提到 Codex 每周有 500 万用户、企业营收同比增长 50%、日活使用增长 5%，以此作为增长动能的指标，并暗示 GPT-5.6 即将到来。[来源-twitter](https://x.com/kimmonismus/status/2061961710823686489)
- **AI 在 Stanford 法学院研究中表现优于法律教授** — Stanford 法学院发布的一项研究显示，在一组法律推理任务上，一个 AI 系统的表现超过了法律教授。研究结果表明，在某些法律评估场景中，AI 已能达到甚至超越人类专家的水平，对法律教育与法律实务均具有潜在影响。[来源-hackernews](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/)
- **Google Gemma 4 12B 接近 26B 级别性能** — 一篇 Reddit 帖子在本地 RTX 4090 上，通过自包含的 HTML5 canvas 物理测试对比了 Google Gemma 4 12B 与 Gemma 4 26B-A4B。26B-A4B 模型占用 15GB 显存，生成 6.9k token，速度为 138 tok/s，相比之下 12B 使用 9GB 显存，生成 8.9k token，速度为 80 tok/s；在每个场景中 26B 都胜出，大约快 1.7 倍，并有 4B 激活参数。12B 仍保持更高的显存效率，使其对 16GB 显存的笔记本用户颇具吸引力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tw4tmf/new_google_gemma_4_12b_claims_near26b_performance/)
- **Gemma 4：被预告的 120B 模型即将登场** — 一则 Reddit 帖子暗示更多 Gemma 4 模型即将推出，其中包括一款由用户 /u/Deep-Vermicelli-4591 提交的可能拥有 120B 参数的模型。相关信息引用了一条 X 平台状态链接，显示社区在跨平台热议即将发布的 Gemma 4 变体。如果消息属实，这将凸显社区对 Gemma 4 系列的持续贡献，以及其在开源路线上的进一步扩展。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tvzzml/more_gemma_4_models_incoming/)
- **OCC-RAG 提出用于可靠问答的 Optimal Cognitive Core** — 新研究指出，仅仅扩大全语言模型规模不足以实现真正可靠的问答和稳健推理。论文提出 Optimal Cognitive Core（OCC），这是一组针对任务专门设计的小型语言模型家族，并给出 OCC-RAG 这一专用于忠实问答的变体。[来源-huggingface](https://huggingface.co/papers/2606.00683)
- **Humanoid-GPT 通过扩充数据与结构实现零样本动作追踪** — Humanoid-GPT 是一种具有因果注意力的 GPT 风格 Transformer，被训练在十亿规模的动作数据集上，用于全身控制。它将多个主流动作捕捉（mocap）数据集统一成一个包含 20 亿帧的重定向语料，并加入自采数据，从而实现零样本动作追踪。通过同时扩展数据规模与模型容量，目标是在单一生成式 Transformer 中跟踪高度动态的行为，超越传统浅层追踪器。[来源-huggingface](https://huggingface.co/papers/2606.03985)
- **Headroom 将 AI token 用量削减最高可达 95%** — Headroom 作为 AI agent 的上下文压缩层，在工具输出、日志、RAG 片段、文件以及对话历史传入 LLM 之前进行预处理。项目宣称在保持答案一致的前提下可减少 60–95% 的 token 消耗，并以库、代理和 MCP 服务器三种形式提供。其强调“本地优先”的运行方式以及可逆的工作流，并支持多种算法。[来源-github](https://github.com/chopratejas/headroom)
- **Microsoft 打算让用户“上瘾”于 Scout AI 助手** — 内部文件显示，Microsoft 计划通过养成机制和参与度设计，让用户对其新 AI 助手 Scout 形成“上瘾”式使用习惯。基于内部材料的报道在 Hacker News 上引发讨论，暴露出 AI 产品设计与用户自主性之间的紧张关系。[来源-hackernews](https://www.404media.co/microsoft-wants-to-make-people-addicted-to-scout-its-new-ai-assistant-internal-documents-reveal/)
- **Qwen 在 8 项基准中的 5 项击败 Gemma，且体积更小** — Qwen3.5-9B 在与 gemma-4-12b-it 共享的基准测试中，在 8 项中有 5 项表现更优，尽管其模型规模更小。Gemma 在编码能力上可能略有优势，但也存在 Omnicoder-9B 等替代模型。相关基准结果引用自 Hugging Face 官方模型卡，并在 Reddit 上展开讨论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tw0lua/gemma412bit_vs_qwen359b_on_shared_benchmarks_qwen/)
- **安卓手机变身 Vulkan 加速的本地 LLM 网格节点** — 一位开发者展示了如何将 Android 设备变成便携式、由 Vulkan 加速的 GGUF 推理服务器，并接入自建 AI mesh。手机可在本地运行 GGUF 模型，暴露一个兼容 OpenAI 的接口，并通过 LiteLLM 和 Tailscale mesh 进行路由，在 mesh 离线时也可单机独立运行，并在需要时回退到更大的本地节点。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tw63jz/i_turned_an_android_phone_into_a/)

### AI 工具

- **Hermes Desktop 将 Hermes Agent 原生带到你的电脑上** — Hermes Desktop 作为 Hermes Agent 的下一代形态目前已开放公测，可在用户的本机原生运行。它通过 Ollama 支持本地或云端模型，并提供 HLS 播放功能；这一特性曾在 Nvidia GTC 主题演讲中由黄仁勋首次演示。[来源-twitter](https://x.com/ollama/status/2062011585355551231)

### AI

- **AI 赋能的网络攻击正在检验现有安全技术** — Anthropic 分析了 832 个恶意账号，并将其活动映射到一个长期维护的威胁技术数据库，以测试安全框架在 AI 驱动攻击下的韧性。研究结果评估了传统防御方法能否跟上 AI 驱动对手的演化步伐，反映出网络威胁升级后的新形势。[来源-twitter](https://x.com/AnthropicAI/status/2062243425580367905)
- **为什么 AI 数据中心要秘密建设？** — 文章质疑围绕 AI 数据中心建设所存在的高度保密，以及这对 AI 行业透明度意味着什么。它梳理了 Hacker News 上的相关讨论，并指出人们对 AI 基础设施建设与监管缺位的更广泛担忧。[来源-hackernews](https://www.thebrockovichreport.com/p/if-data-centers-are-so-great-why)

### AI 安全

- **美国要以安全模型和防御工具引领 AI** — Sam Altman 表示，美国应通过持续打造顶级模型、确保其安全性，并向可信赖的防御方提供网络安全工具，从而在 AI 领域保持领导地位。他称赞最新行政命令在创新与安全之间取得平衡，并将政策定位为负责任 AI 领导力的关键支点。[来源-twitter](https://x.com/sama/status/2061973280655904815)
- **多伦多大学 AI 蠕虫可攻击任意联网设备** — 多伦多大学的研究人员展示了一种 AI 驱动的蠕虫，可潜在针对任何联网设备发动攻击，凸显网络安全风险。演示表明 AI 如何在恶意软件创建上实现自动化和规模化，强调需要更强的防御措施与安全机制。[来源-hackernews](https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device)

### AI 政策

- **特朗普在多次反复后签署缩水版 AI 行政令** — 特朗普在数周的反复与修订后，签署了一份“缩水版” AI 行政命令。此举凸显美国在 AI 政策与安全标准上的持续政治争论，并已被《纽约时报》和 Politico 等主流媒体广泛报道。[来源-hackernews](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389)

## ⚡ 快讯速览

- **Anthropic 发布基于 Claude 的数据分析最佳实践** — Anthropic 在博客中分享了如何用 Claude 自动化商业分析的最佳实践，包括所需核心技能、数据基础建设以及面向分析 agent 的评估标准。文章提供了实用建议，帮助企业最大化 Claude 在自助式数据洞察和数据分析流程优化方面的能力。[来源-twitter](https://x.com/ClaudeDevs/status/2062274312363770064)
- **Grok Imagine 1.5 预览版通过 API 开放** — Grok 发布了 Imagine 1.5 的预览版本，并宣布新版本现已可用。用户可以通过 x.ai/api/imagine 的 API 进行试用，更新说明中提到支持 HLS 播放功能。这标志着 Grok 在多模态图像生成能力上的又一次迭代。[来源-twitter](https://x.com/grok/status/2062225080843747351)
- **Thinking Levels 登陆 Gemini Web、iOS 与 Android** — Google Gemini 现已在 Web、iOS 和 Android 平台支持 Thinking Levels 功能。此次更新为所有平台的该功能开启了 HLS 播放支持。[来源-twitter](https://x.com/joshwoodward/status/2062025667852812583)
- **Trust Region 提升 LLM 的 On-Policy 蒸馏稳定性** — On-Policy Distillation（OPD）可以高效完成大型语言模型的后训练，但当教师模型与学生模型的分布出现偏离时，训练会变得不稳定。论文提出了一种基于 trust region 的可靠 on-policy token 级监督方法，用于稳定策略梯度并防止优化失败，旨在让 OPD 在 agent 学习、多任务训练和模型压缩等 LLM 后训练场景中更加鲁棒。[来源-huggingface](https://huggingface.co/papers/2606.01249)
- **Uber 每月 1500 美元的 AI 使用上限为工具定价提供参考** — Uber 为团队使用 AI 工具设定了每月 1500 美元的费用上限，被视为企业级 AI 工具定价的一种信号。该上限被描述为在 AI 大规模落地过程中，在可用性和成本控制之间寻求平衡的举措，分析人士认为这凸显了 AI 工具预算与治理的重要性。[来源-hackernews](https://simonwillison.net/2026/Jun/3/uber-caps-usage/)
- **Open-LLM-VTuber v2.0 进入早期规划阶段** — Open-LLM-VTuber 宣布将进行完全重写，v2.0 目前处于早期规划中。维护者呼吁不要再提交针对 v1 的 issue 或 PR，并建议有兴趣的贡献者加入 Zulip 参与 v2 讨论，周会信息也会在那公布；v1 的 bug 修复仍会继续，多语言 README/文档保持可用，且本地跨平台支持基于 Live2D 的免手持语音+人脸追踪。[来源-github](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)
- **数学家警示 AI 正在快速推进** — Science.org 的文章报道，多位数学家警告 AI 正在以极快的速度发展，并伴随潜在的安全与伦理问题。文章强调技术进展可能快于我们对风险建模与理解的能力，呼吁在 AI 安全与治理方面建立更扎实的理论基础并保持审慎态度。[来源-hackernews](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground)
- **RSS 回潮：AI Agents 开始“阅读”它** — 文章认为，随着 AI agents 对最新信息的需求上升，RSS 再度成为一种有价值的数据源。它探讨了 AI 系统如何利用类似 RSS 的数据管线实现轻量、可扩展的数据摄取，并讨论了这一趋势对工具生态、标准制定和隐私保护的影响。[来源-hackernews](https://julienreszka.com/blog/rss-is-back-ai-agents-are-reading-it/)
- **AI 短缺推高 DDR5 32GB 内存至 375 美元** — 由于 AI 驱动的持续需求与供应紧张，32GB DDR5 内存价格已飙升至约 375 美元。报道指出，AI 相关短缺正在挤压 PC 装机玩家和专业用户，使大容量内存升级成本显著提高，也从硬件层面反映出 AI 负载对主流 PC 升级路径的影响。[来源-hackernews](https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-now-costs-usd375-minimum-ai-shortage-continues-to-squeeze-pc-building)
- **多数人开始依赖 AI 进行心理支持** — AXA 发布的 2026 年心智健康报告显示，超过 60% 的人会求助于人工智能来获得心理支持。报告强调，AI 在心理健康领域的使用快速增长，引发对其有效性、可获得性以及安全性的质疑，并凸显了人们寻求心理帮助方式的转变，对医疗服务提供方与科技平台都有深远影响。[来源-hackernews](https://www.axa.com/en/press/press-releases/2026-mind-health-report)
- **Qwen-Coder 再被关注：总参 80B，激活 8–12B** — 一篇 Reddit 帖子讨论了重新启用 Qwen-Coder，并表达了对大规模模型的兴趣。作者希望模型总参数达到 800 亿，同时保持 80–120 亿激活参数，并询问这样的架构是否仍可行；该帖由用户 FaustAg 发布在 r/LocalLLaMA 社区。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1tvzpk1/been_a_while_since_we_had_a_qwencoder_could_use_a/)

---

*由 AI News Agent 生成 | 2026-06-03*