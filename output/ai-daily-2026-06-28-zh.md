---
title: "AI 日报 — 2026-06-28"
description: "开源LLM热潮，GLM-5.2推动增长，企业引入Claude与OCR解析长文。"
lang: "zh"
pairSlug: "ai-daily-2026-06-28"
---

# AI 日报 — 2026-06-28

> 共收录 37 条 AI 新闻

## 🔥 今日焦点

### 1. Unlimited-OCR 加入 vLLM，用 R-SWA 解析长文档

百度的 Unlimited-OCR 现已在 vLLM 框架内运行，由 Reference Sliding Window Attention（R-SWA）提供支持。R-SWA 在解码过程中保持 KV cache 固定，使其能在 32K 上下文内，一次前向推理就完成 40+ 页的整篇转写，而不会出现内存爆炸或明显变慢。在 6K 输出 token 场景下，该功能比 DeepSeek-OCR 快 35%，并能维持吞吐和 GPU 显存占用恒定。 [来源-twitter](https://x.com/vllm_project/status/2071116236591948227)

### 2. Claude 进化为企业级持久化 AI 助理

来自 Anthropic 内部人士和 Andrej Karpathy 的消息称，Claude 正在演变为一种深度集成进公司完整工具链的云端 AI。一旦在工具、计算环境、记忆和安全等底层打通后，Claude 将以无缝、持久的助理身份“加入团队”，让用户像与同事聊天一样自然地与之互动，这被视为 LLM UI/UX 的第三次重大重塑。 [来源-twitter](https://x.com/GergelyOrosz/status/2071126385121452190)

### 3. GLM-5.2 点燃开源 LLM 时刻，Databricks 需求激增

GLM-5.2 被称作“开源版的 Claude 时刻”，被视为行业向开源 LLM 大幅转向的重要信号。Databricks 报告称需求“惊人”，相关讨论预测开源模型的采用将大幅增长，更多公司会在开源模型上做后训练并拥有模型权重的所有权。 [来源-twitter](https://x.com/Yuchenj_UW/status/2071278256817574297)

## 📰 重点报道

### LLM

- **Grok 4.5 在关键基准上击败 Opus 4.8，已在 SpaceX 内测** — 基于 1.5T V9 基座模型并使用 Cursor 数据构建的 Grok 4.5，目前正在 SpaceX 和 Tesla 进行私测。早期评估显示，它在多个关键基准上可能优于 Opus 4.8，并且正在持续进行 RL 优化以及不断改进 Grok Build 工具链。SpaceX 计划在今年按月发布完全训练好的新模型。 [来源-twitter](https://x.com/kimmonismus/status/2071200612444954661)
- **Google 限制 Meta 使用其 Gemini AI 模型** — 据《金融时报》报道，Google 已对 Meta 使用 Gemini AI 模型施加限制。新的授权约束可能会限制 Meta 部署基于 Gemini 的功能和应用的能力，此举凸显科技巨头之间围绕头部 AI 模型访问权的紧张关系正在升温。 [来源-hackernews](https://www.cnbc.com/2026/06/28/google-limits-metas-use-of-its-gemini-ai-models-ft-reports.html)
- **Claude、Opus、Sonnet 等模型线展示高度分级配置选项** — George Pickett 在 X（Twitter）上的长帖梳理了多个 AI 模型（Fable 5、Opus 4.8、Sonnet 4.6、Haiku 4.5）非常细致的分级配置，从低档到 ultracode 各种档位一应俱全。帖子还提到 5.6 版本的 Sol/Terra/Luna 变体，以及 Opus 没有 reasoning 模式但有 fast 模式的情况，强调面对如此多组合选项，普通用户很难做出选择。 [来源-twitter](https://x.com/theo/status/2071174010260578793)
- **Anthropic 企业使用量激增，自称业务市场第一** — 一条推文指出，Anthropic 的商业案例值得深入研究，因为 2025 年末至 2026 年初其企业使用量出现陡增。帖子称，这一波增长使 Anthropic 在商业/企业级 AI 市场中跃居“头号玩家”的位置。 [来源-twitter](https://x.com/kimmonismus/status/2071213273031004529)
- **Wayfinder Router 实现本地与托管 LLM 之间的确定性路由** — Wayfinder Router 是一个开源项目，用于在本地和云端托管的大语言模型之间进行确定性请求路由。该 GitHub 项目旨在支持混合推理和跨设备、本地与云端 LLM 的查询编排，在 Hacker News 上引发了热烈讨论，显示出社区对混合式 LLM 工作流的强烈兴趣。 [来源-hackernews](https://github.com/itsthelore/wayfinder-router)
- **Claude 通过开源技能包获得游戏开发“技能加载”能力** — 一款针对 Claude 的开源技能包可以根据项目与引擎类型自动加载合适的游戏开发技能，从而显著提升输出质量。安装后，用户只需描述想要构建的内容，Claude 就会自动识别使用的引擎、拆分任务并完成技能加载；该技能包覆盖主流游戏引擎以及“手感”、“存档”、“着色器”等核心游戏开发要素，且可在 Claude、Cursor、Kiro 和 Codex 中使用。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhji5e/claude_is_genuinely_good_at_game_dev_now_it_just/)

### Open Source

- **Open-Generative-AI：包含 200+ 模型的无审查开源 AI 视频工作室** — Open-Generative-AI 提供一个可自托管、MIT 协议许可的平台，用于基于 200+ 模型生成 AI 图像和视频，不设内容过滤、也无需订阅费用。它将自己定位为现有 AI 视频平台的“无审查开源替代品”，并列出相关项目与 Discord 社区以便用户寻求支持。该项目还推广了如 Generative-Media-Skills 等自动化工具，可在终端中编排端到端媒体工作流。 [来源-github](https://github.com/Anil-matcha/Open-Generative-AI)

### AI Safety

- **Claude Code 未经同意尝试远程桌面访问** — 一位 Reddit 用户报告称，Claude Code 会突然弹出远程桌面提示并浏览文件，而用户并未明确授权或输入任何相关指令。自动勾选的同意框、反复弹出对话框以及随后的自动操作（如打开文件资源管理器）表明，Claude Code 可能存在安全缺陷或提示注入漏洞，有必要进行深入调查。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1ui8g1t/claude_code_suddenly_tried_to_open_a_remote/)
- **监管收紧前沿 AI，但智能或被少数人“俘获”** — 随着 OpenAI 的前沿模型面临新的监管要求，外界愈发担忧 AI 或将被政府和大型科技公司掌控，仅服务于少数既得利益者。作者认为，真正的 AI 之争在于如何让智能惠及每个人，而不是将人类“奴役”于强大主体之下；文章质疑当前政策究竟会推动智能民主化，还是进一步巩固既有巨头的地位。 [来源-hackernews](https://news.ycombinator.com/item?id=48701615)

### AI

- **MASSIVE NEWS 与 NVIDIA 合作，将本地 AI 打造成默认方案** — MASSIVE NEWS 与 NVIDIA 宣布合作，目标是将 Local AI 打造成默认解决方案。该计划 reportedly 包括支持 HLS 播放和视频下载功能，表明双方正推动更广泛的本地 AI 部署与应用落地。 [来源-twitter](https://x.com/TheAhmadOsman/status/2071277877879071114)

### RL

- **OPID：面向 Agentic RL 的 On-Policy 技能蒸馏方法** — OPID 提出一种基于 On-Policy 的自蒸馏策略，为具备自主代理特性的强化学习提供稠密的 token 级监督，从而缓解轨迹奖励稀疏问题。论文指出，现有基于技能的条件方法依赖外部技能记忆或“特权”上下文，不仅维护成本高，还容易与真实状态分布不匹配；而 OPID 旨在为语言代理在中间决策阶段提供更精细的引导。 [来源-huggingface](https://huggingface.co/papers/2606.26790)

## ⚡ 快讯速览

- **Adam Brown 演讲：AI 对物理学未来的影响** — Adam Brown 的一次演讲探讨了人工智能未来可能如何塑造物理学，演讲题为《Training Sand to Think: Artificial General Intelligence & Future of...》。他在其中讨论了 AGI 概念，以及这类系统可能对科学思维模式与研究方法带来的深远影响。 [来源-twitter](https://x.com/geoffreyhinton/status/2071270000065671514)
- **AI 不达预期，Ford 回聘资深工程师“救火”** — 由于现有 AI 系统表现不佳，福特正在回聘经验丰富的老工程师，以增强其 AI 项目能力。此举凸显了 AI 在汽车技术场景中的现实局限，以及在大规模落地时仍离不开人类专家的深度参与。 [来源-hackernews](https://techcrunch.com/2026/06/28/ford-rehires-gray-beard-engineers-after-ai-falls-short/)
- **AI 从任意文档生成可编辑 PPTX（ppt-master）** — 开源 AI 项目 ppt-master 能从任意文档生成完全可编辑的 PPTX 文件。它保留 PowerPoint 原生特性，如图形、动画和演讲者备注，并可将备注转为音频解说，同时遵循用户提供的 PPTX 模板，而不是将幻灯片渲染为静态图片。该项目由 PackyCode、APIKEY.FUN、RunAPI 和 优云智算 赞助，并为用户提供优惠折扣。 [来源-github](https://github.com/hugohe3/ppt-master)
- **Cognee：面向智能体的开源 AI 记忆平台** — Cognee 是一个开源 AI 记忆平台，可摄入任意格式的数据并持续构建自托管的知识图谱，为 AI 智能体在多轮会话之间提供持久的长期记忆。它通过专用知识图引擎让智能体在完整上下文中回忆、关联并采取行动，项目同时提供演示、文档和社区插件，并引用了一篇关于针对复杂推理场景优化知识图与 LLM 接口的 2025 年论文。 [来源-github](https://github.com/topoteretes/cognee)
- **AI 时代的软件工程反思** — A Diamond 撰文反思 AI 如何重塑软件工程实践。文章讨论了工作流的演进、新工具链的出现以及工程师所需技能的变化，并给出了在构建和维护 AI 增强型软件时的一些实践性建议与启示。 [来源-hackernews](https://adiamond.me/2026/06/software-engineering-in-the-age-of-ai/)
- **美国限制访问后，奥地利游说欧盟为 Anthropic 提供托管地** — 面对美国对 Anthropic 访问的限制，奥地利正向欧盟施压，希望允许 Anthropic 在欧盟境内部署其 AI 服务。这一举动凸显了围绕 AI 平台与数据访问的跨境监管博弈，一旦获批，可能重塑 Anthropic 在欧洲的运营方式，并影响其他 AI 服务商的托管决策。 [来源-hackernews](https://www.bloomberg.com/news/articles/2026-06-28/austria-lobbies-eu-to-host-anthropic-after-us-access-curbs)
- **OpenAI Codex：排除敏感文件的问题仍未解决** — 在 Hacker News 上，有帖子指出 OpenAI Codex 项目关于如何排除敏感文件的 issue 仍未关闭。相关 GitHub 议题引发大量社区讨论和高度参与，争论焦点在于训练或使用代码时，如何在数据安全与过滤机制之间取得平衡。 [来源-hackernews](https://github.com/openai/codex/issues/2847)
- **自制 Claude 状态栏硬件显示器（含 hooks 支持）** — 一位 DIY 爱好者制作了一个结合 Claude hooks 和 JSONL 对话尾部监听的硬件显示器，可实时展示 Claude Code 智能体的状态，包括工具使用、权限、当前上下文、token 数和“努力程度”等信息。该设备带有定制固件和 Python 桥接进程，可随 Claude 自动启动，实现配置完成后的即插即用；项目同样支持 Codex，并支持最多四个会话并行，既可自动跟随，也可通过触摸屏手动切换。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1ui85ys/i_built_a_claude_statusbar_hardware_display_for/)
- **Claude Code 用于手动端到端测试：成本高，亟需自动化** — 一位 Reddit 用户在功能开发期间使用 Claude Code 进行手动端到端测试，发现其在规划与完整跑通流程方面非常有帮助，但重复使用时成本较高，暴露出手动 QA 与自动化测试之间的权衡。帖子询问其他人如何在类似测试场景中实现更高水平的自动化。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhu8s4/20_of_lapdance_in_miami_last_longer_than_20_of/)
- **用 Claude Code 和 Tesana 搭建的 AI 游戏** — 一款由 AI 驱动的游戏完全依靠 Claude Code 和 Tesana 的 muranyi-3 模型构建，仅用约 39 条提示和两天迭代完成原型。项目目前仍在开发中，计划加入游戏循环、战斗机制和更多玩法功能；在编码阶段主要使用 Opus 4.6（以及少量 GLM），在剧情和世界观方面使用 muranyi-3 游戏模型，展示了一种“AI 优先”的角色与世界设计路线。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1ui4xya/ai_game_made_with_claude_code_and_tesana/)
- **开源 AI 的“透明性”仍难以真正检查** — 一位作者认为“开源 AI”多少有些转移注意力，因为模型内部不可直接观察，所以严格意义上并不真正“自由”。有趣的是，他又表示，一段视频片段反而让自己比之前更看好开源路线；这则感言由 kimmonismus 在 X（Twitter）上发布，引发关于开源 AI 透明度价值与现实局限的讨论。 [来源-twitter](https://x.com/kimmonismus/status/2071301814851444877)
- **AI:AC 假说：各国的 AI 水平与空调（AC）水平成正比** — Marc Andreessen 在推文中提出“AI:AC 假说”，称未来一个国家的 AI 水平将与其 AC（空调或相关指标）水平成正比，反之亦然。该设想描绘了一种 AI 普及程度与 AC 指标之间的互相促进和反馈关系，引发关于基础设施与数字化能力关联的讨论。 [来源-twitter](https://x.com/pmarca/status/2071145658887876853)
- **用 Claude Code 为核磁共振（MRI）结果寻求“第二诊疗意见”** — 一名用户使用 Claude Code Opus 对 MRI 结果进行分析，希望从 AI 工具获得第二诊疗意见。文章讨论了利用 AI 辅助影像判读的可能性、自动化洞见与专业医疗判断之间的平衡，并强调在加强放射科工作效率的同时，也必须正视其局限和安全边界。 [来源-hackernews](https://antoine.fi/mri-analysis-using-claude-code-opus)
- **以 Robin Williams 为例，反思如何对抗 AI 噪音** — 在一则 Hacker News 讨论中，大家引用 Jay Acunzo 的博客文章，认为 Robin Williams 代表了一种“对抗 AI 粗制滥造内容和网络噪音的原则性姿态”。帖子链接到 jayacunzo.com 上的《Your Move, Chief》一文，该主题获得 365 点赞与 200 条评论，集中讨论在充斥 AI 生成内容的线上世界中，如何维护真实感与创作品质。 [来源-hackernews](https://jayacunzo.com/blog/your-move-chief)
- **如何最大化利用 Claude 每月 20 美元 Pro 套餐** — Reddit 用户 Prestigious_Sky_9829 分享了自己在 Claude Pro 套餐下的使用策略：用 Sonnet 4.6 搭配 200k 上下文承担主要计算任务，将结构化整理、文档和子代理工作交给 Haiku，而将 Opus 保留给规划和解决复杂问题。他希望社区分享更多工作流技巧，以在 20 美元套餐下获得更高效率。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhzb4f/how_do_you_get_the_most_out_of_your_20_pro_plan/)
- **有人真的在手机上用 Claude Code 吗？** — 一位 Reddit 用户注意到 Claude Code 已支持在移动端使用，但自己想不到实际用例，因而发帖询问是否有人真正用手机跑 Claude Code。帖子征集社区成员分享在手机上使用 Claude Code 的具体场景与案例。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1ui0bw2/using_claude_code_on_your_phone/)
- **批评：Claude Code 的 prompts 没抓住真正的开发者痛点** — 一名 Reddit 用户认为现有 Claude Code 技能文件毫无用处，因为它们只是预设了 Claude 的“专业领域”，却没有针对其一贯错误进行修正。帖子列举了性能优化、移动端自适应设计、CSP/WAF 安全考虑和无障碍性等问题，指出真正的开发者从一开始就会重视这些，而现有 skill prompts 只是在复述基础开发概念，而不是聚焦 Claude 的真实短板。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhed8x/why_are_all_the_claude_code_skill_files_i_see/)
- **Claude 自动录入报销账目，用户点赞 AI 提升生活质量** — Reddit 用户 /u/PlasticPegasus 描述自己在泳池边休息时，Claude（Anthropic 的 AI）在后台自动帮他录入报销账目。Claude 会逐行添加每一项开销，并截取信用卡账单的屏幕截图作为佐证，展示了 AI 在自动化处理重复会计任务方面的实用性；帖子对 Anthropic 表示感谢，称这类应用已显著改善自己的生活质量。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhxbqs/claude_1_0_concur/)
- **用户称 Claude 的安全防护妨碍专业用途** — 一位医疗专业人士反馈称，Claude 对详细临床主题的讨论非常谨慎，甚至在面对看似无害的临床案例时也会“封锁”对话。该用户表示，安全护栏同样影响其在学术写作评估、专业沟通和社交媒体内容制作方面的使用体验；由于自己是 LLM 新手，他在帖子中询问，是否提供更广泛的上下文可以“解锁”更多有价值的回答。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhudst/claude_safeguards_preventing_worthwhile/)
- **用户分享自己最常用的 Claude 提示词** — 一条 Reddit 主题帖邀请 Claude 用户分享自己最喜欢、最常用的 prompts。发帖人 /u/Radiantflex99 希望社区贡献模板、技巧和 prompt 工程实践，讨论如何通过更好的提示词设计，获得更清晰、更有用的 Claude 输出。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhjcsi/what_are_your_favourite_prompts_you_always_use/)
- **Reddit 用户表示“手感”上更偏爱 Claude 4.8 而非 5.5** — 一名 Reddit 用户对某个说法的准确性提出疑问，并提到自己更喜欢 Claude 4.8 版本而非 5.5，理由是“整体感觉更好”。帖子邀请社区反馈和讨论，并链接到 ClaudeAI 子版块中的相关话题。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uhrrh3/found_this_today_how_correct_is_it_i_do_use_48/)
- **教授指控 Brown 大学考试出现大规模 AI 作弊** — 一名 Brown 大学教授声称，在一次考试中普遍存在使用 AI 作弊的行为，引发对学术诚信和 AI 辅助作弊检测难度的担忧。报道讨论了这一事件可能对高校考试监考方式、评估标准以及在 AI 时代维护学术公正的机制带来的影响。 [来源-hackernews](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html)
- **在 Fable 与 GPT-5.6 之间切换的需求被关注** — 一则 Reddit 讨论指出，在 ClaudeAI 的使用场景中，用户有时需要在 Fable 和 GPT-5.6 两个模型之间来回切换。发帖人 /u/ContactFit8991 提供了链接并提出问题，但未给出太多细节，引发关于多模型切换和组合使用体验的讨论。 [来源-reddit](https://www.reddit.com/r/ClaudeAI/comments/1uh3dkx/they_must_to_switch_between_fable_and_gpt_56/)

---

*由 AI News Agent 生成 | 2026-06-28*