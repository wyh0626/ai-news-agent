# AI 日报 — 2026-02-20

![封面](https://nitter.net/pic/orig/media%2FHBopKGfXMAA29nQ.jpg)

> 覆盖 39 条 AI 新闻

## 🔥 今日焦点

### 1. Nvidia 与 OpenAI 放弃千亿美元交易，转而推动约 300 亿美元的投资安排

据报道，Nvidia 与 OpenAI 已从未完成的 mega-deal 中撤出，转而追求一项规模较小的投资安排，金额约为 300 亿美元，这一举动在市场动态变化中显示出双方合作策略的再校准。此举可能重塑 AI 生态系统中的资金模式、共同开发时间表以及软硬件集成的投资逻辑。 [来源-rss](https://www.ft.com/content/dea24046-0a73-40b2-8246-5ac7b7a54323)

### 2. Consistency Diffusion LMs: 14x Faster, No Quality Loss

Together AI 公布了面向语言模型的一致性扩散（consistency diffusion），声称通过在各步骤强制扩散约束，生成速度最高可提升至 14 倍，且质量无下降。若在大规模实际应用中可行，该方法可能显著降低企业级 LLM 部署的推理成本与延迟。 [来源-rss](https://www.together.ai/blog/consistency-diffusion-language-models)

### 3. 顶级 OpenRouter 模型：本周中文模型处于领先地位

OpenRouter 的活跃度显示中文开源模型本周吞吐量达到新记录，多款模型在一周内超过万亿标记，且有多款模型达到万亿标记。领导格局的变化凸显开源 AI 能力的全球化进程，以及对开源基准测试和生态系统动态的潜在影响。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9zt8m/the_top_3_models_on_openrouter_this_week_chinese/)

## 📰 重点报道

### LLM

- **Taalas Runs Llama 3 8B at 16k Tokens/s** — 展示了以每个用户 16k tokens/s 的速率运行 Llama 3 8B，声称相比基于 SRAM 的系统快一个数量级；该架构以针对特定模型的硬件芯片为核心，实质上让芯片就是模型。带有 HLS 回放的聊天演示突显了该方法的潜力。 [来源-x](https://x.com/awnihannun/status/2024671348782711153)

- **Anthropic launches official Claude Code Plugins directory** — Anthropic 发布 Claude Code Plugins 的官方目录，展示内部与外部插件，同时提醒关于信任第三方组件的风险；插件可通过 Claude Code 的插件系统安装，由 Anthropic 治理，外部插件由合作伙伴与社区提供。 [来源-github](https://github.com/anthropics/claude-plugins-official)

### AI 安全

- **Frontier Labs: AGI and Superintelligence Near Takeoff** — 前沿实验室的观点认为 AGI 与超智能接近起飞，强调内部加速的快速推进与 ASI 的临近，同时强调对模型增长轨迹的监控。 [来源-x](https://x.com/kimmonismus/status/2024898716365455459)

- **Cord Coordinates Trees of AI Agents** — Cord 提出基于树的框架，用于协调多个 AI 代理以提升可扩展性和协作性，吸引 Hacker News 关注在组织 AI 安全模式方面的讨论。 [来源-rss](https://www.june.kim/cord)

### 行业

- **AI 助手让每位开发者都成为广告公司** — 该文章指出，AI 助手通过广告与数据驱动的收入来变现用户互动，将 AI 助手重新定位为广告平台，并引发隐私与商业模式方面的担忧。 [来源-rss](https://juno-labs.com/blogs/every-company-building-your-ai-assistant-is-an-ad-company)

- **BC 学校枪击案：ChatGPT 消息经 OpenAI 员工审阅** — 华尔街日报报道，被标记的 ChatGPT 消息不仅被自动化筛选器检测到，还被约 12 名 OpenAI 员工审阅与讨论，凸显“人类在环”的安全工作流与相关决策问题。 [来源-x](https://x.com/AricToler/status/2024976260749820067)

- **Stellan Skarsgård 警示 AI 在资本集中背景下对电影行业的增长风险** — 该演员讨论 AI 在电影中的扩展作用，提及采用与抵制并存，并指向资本集中与科技精英控制的更广泛担忧。 [来源-x](https://x.com/Variety/status/2024983345499963815)

- **Anthropic 发布官方 Claude Code 插件目录** —（见 LLM）该目录旨在围绕信任与验证就 Claude Code 扩展的插件进行治理性筛选。 [来源-github](https://github.com/anthropics/claude-plugins-official)

### 开源 / 工具

- **Frontier Labs: AGI and Superintelligence Near Takeoff** —（见 AI 安全）强调在能力加速的背景下，近阶段的治理需求及潜在风险。 [来源-x](https://x.com/kimmonismus/status/2024898716365455459)

- **Cord Coordinates Trees of AI Agents** —（见 AI 安全）提出可扩展的多代理协调模式，以提升安全性与协作性。 [来源-rss](https://www.june.kim/cord)

### AI 研究

- **Consistency Diffusion LMs: 14x Faster, No Quality Loss** —（见 AI 安全）讨论在一致性约束下的扩散推断，以在不牺牲质量的前提下提升生成速度。 [来源-rss](https://www.together.ai/blog/consistency-diffusion-language-models)

## ⚡ 快讯速览

- **Hugging Face 收购 GGML.AI** — HF 在本地模型工具领域扩张，通过收购推动轻量级模型生态的整合。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9vywq/ggmlai_has_got_acquired_by_huggingface/)

- **字节跳动的 Ouro-2.6B-Thinking 实现首次可用推理** — Ouro-2.6B-Thinking 实现初步推理能力，标志着 Ouro 家族的一项里程碑。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ramir9/release_ouro26bthinking_first_working_inference/)

- **Phil Spencer 退出 Microsoft，AI 高管接任 Xbox 职务** — 领导层发生变动，AI 负责人将担任 Xbox 的关键游戏部门角色。 [来源-rss](https://www.neowin.net/news/phil-spencer-is-exiting-microsoft-as-ai-executive-takes-over-xbox/)

- **实现每秒 17k Token 的普及型 AI 路径** — 概述了更快、更易获取的 AI 推理路径，突出效率里程碑。 [来源-rss](https://taalas.com/the-path-to-ubiquitous-ai/)

- **AI 不是同事，而是外骨骼** — 这一观点将 AI 重新定位为工作场所的增强，而非替代。 [来源-rss](https://www.kasava.dev/blog/ai-as-exoskeleton)

- **Google TimesFM 发布 Time-Series Foundation Model 2.5** — Google Research 发布了更新的时序基础模型产品。 [来源-github](https://github.com/google-research/timesfm)

- **roboflow/trackers：即插即用的多对象跟踪库** — 新的跟踪库实现了即插即用的多对象跟踪能力。 [来源-github](https://github.com/roboflow/trackers)

- **OpenAI 报告所有团队普遍取得积极进展** — 内部更新显示跨产品线的跨团队势头。 [来源-x](https://x.com/gdb/status/2024985187579560366)

- **2026年2月最佳音频模型 Megathread** — 社区对 2026 年 2 月领先的音频专注模型进行汇总。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r7bsfd/best_audio_models_feb_2026/)

- **映射澳大利亚最高法院每个案件及引文** — 致力于将澳大利亚判例及引文映射以供参考工具使用。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ram2ov/how_i_mapped_every_high_court_of_australia_case/)

- **Meta 的 AI 部署正在扼杀我们的代理机构** — 对 Meta AI 部署对营销代理机构影响的批评性分析。 [来源-rss](https://mojodojo.io/blog/meta-is-systematically-killing-our-agency/)

- **PentAGI：用于渗透测试的自治 AI 代理** — 开源项目展示了用于安全测试的自治代理。 [来源-github](https://github.com/vxcontrol/pentagi)

- **Hugging Face Skills Define AI Tasks Interoperable with Major Tools** — HF Skills 框架旨在实现跨工具任务互操作性。 [来源-github](https://github.com/huggingface/skills)

- **GLM 5 Appears to Take on Claude Persona** — GLM-5 在演示中展现出类似 Claude 的人格特征。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1raf3dm/glm_5_seems_to_have_a_claude_personality/)

- **Strix Halo Benchmarks: Step 3.5 and MiniMax M2.5** — 社区对 Strix Halo 模型的基准测试。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rabcyp/a_few_strix_halo_benchmarks_minimax_m25_step_35/)

- **Qwen3 Coder Next Outperforms 30B Models with Aggressive Quantization** — Qwen3 Coder 在激进量化下表现出色，超过多款 30B 模型。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rabg6o/qwen3_coder_next_oddly_usable_at_aggressive/)

- **Vellium v0.3.5: Writing Mode Overhaul, Native KoboldCpp, OpenAI TTS** — Vellium 0.3.5 带来写作模式的重大改进、原生 KoboldCpp 支持以及 OpenAI TTS 支持。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rafo5b/update_vellium_v035_massive_writing_mode_upgrade/)

- **Critique: AI Side Projects Spark Backlash** — 讨论公众对 AI 边缘项目的反对情绪及治理方面的担忧。 [来源-rss](https://dylancastillo.co/posts/ai-side-projects.html)

- **AI Uncovers Insiders and Alpha on Polymarket** — 关于 AI 驱动的市场洞察以及 Polymarket 上内部人士活动的信号。 [来源-x](https://twitter.com/peterjliu/status/2024901585806225723)

- **AI Agent Wrote Hit Piece, Operator Came Forward** — 关于由 AI 生成的打击性文章及随后的人工披露的叙事。 [来源-rss](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/)

- **Pi for Excel: AI Sidebar Add-In** — 通过侧边栏插件为 Excel 增添 AI 辅助功能。 [来源-github](https://github.com/tmustier/pi-for-excel)

- **Databricks AI Dev Kit for Coding Agents Released** — Databricks 发布用于构建编码代理的 AI 开发工具包。 [来源-github](https://github.com/databricks-solutions/ai-dev-kit)

- **AI Singularity Takes Off** — 关于 AI 能力快速提升的早期讨论。 [来源-x](https://x.com/scaling01/status/2024925692853395618)

- **StepFun AI to Host AMA on LocalLLaMA** — StepFun AI 宣布将在 LocalLLaMA 上举办 AMA 活动。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r8snay/ama_with_stepfun_ai_ask_us_anything/)

- **TeichAI GLM-4.7, Claude, Opus-4.5 Distill on GGUF** — 将 GLM-4.7、Claude 与 Opus-4.5 提炼为 GGUF 格式。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ranako/teichaiglm47flashclaudeopus45highreasoningdistillg/)

- **New Jersey Residents Defeat AI Data Center** — 新泽西州居民对 AI 数据中心的本地反对行动。 [来源-rss](https://www.commondreams.org/news/new-brunswick-ai-data-center)

- **Gemma to release a new version soon** — 关于 Gemma 即将发布新版本的更新。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ra8omf/gemma_which_we_will_be_releasing_a_new_version_of/)

- **Reddit thread on Deepseek and Gemma** — 关于 Deepseek 与 Gemma 的社区讨论。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1r9uuc6/deepseek_and_gemma/)

- **What are your favorite lesser-known Hugging Face models?** — 关于被低估的 HF 模型的社区投票。 [来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1rajez2/what_are_your_favorite_lesser_known_models_on/)

---

*由 AI 新闻代理生成 | 2026-02-20*