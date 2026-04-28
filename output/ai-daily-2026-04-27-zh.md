---
title: "AI 日报 — 2026-04-27"
description: "TRELLIS.2开源4B3D；离线WebGPU代理；MiMoMIT商用。"
lang: "zh"
pairSlug: "ai-daily-2026-04-27"
---

# AI 日报 — 2026-04-27

> 共收录 33 条 AI 新闻

## 🔥 今日焦点

### 1. Microsoft 发布 TRELLIS.2：开源 40 亿参数 3D 生成模型
TRELLIS.2 推出了一个拥有 40 亿参数的图像到 3D 生成模型，采用新颖的 O-Voxel 稀疏体素结构，可以生成具备完整 PBR 材质的高保真资产。它通过原生 3D VAE 实现 16 倍空间压缩，最高可生成 1536^3 分辨率的 3D 资产。该项目完全开源，提供论文、GitHub 代码以及 HuggingFace 在线演示链接。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxf2u0/microsoft_presents_trellis2_an_opensource/)

### 2. 本地浏览器 AI Agent 利用 WebGPU 离线运行
介绍了一款完全本地、基于浏览器的 AI agent，由 Gemma 4 E2B 与 WebGPU 提供算力支持。该 agent 使用原生工具调用来搜索浏览历史、读取和总结网页内容、管理标签页，全程 100% 离线、无需任何服务器端支持。它还能在浏览器内部实现诸如 HLS 播放等功能。[来源-x](https://x.com/googlegemma/status/2048805789788413984)

### 3. 小米以 MIT 协议开放 MiMo-V2.5，可商业使用
小米以 MIT 开源协议发布 MiMo-V2.5，允许在无需额外授权的前提下进行商业部署、持续训练与微调。此次发布包含用于复杂 agent 与编程任务的 MiMo-V2.5-Pro（在 GDPVal-AA 和 ClawEval 上排名领先），以及具备强大 agent 能力的原生多模态模型 MiMo-V2.5，两者均支持 100 万 token 的上下文窗口；模型权重已在 HuggingFace 上发布，更多细节可在 MiMo 博客（mimo.xiaomi.com）查看。[来源-x](https://x.com/XiaomiMiMo/status/2048821516079661561)

---

## 📰 重点报道

### 开源动态
- **DeepSeek AI v4 论文因开放且严谨的研究获赞** — 该论文因数学上的严谨性与彻底开放发布而备受称赞，强调其将数月到数年的研究工作免费公开，为更广泛的 AI 社区带来收益。[来源-x](https://x.com/art_zucker/status/2048683283194826791)
- **Hermes Agent 仓库下载量超越 Claude 代码仓库** — 这被视为开源 AI 工具链势头不断增强、以及各类 AI 代码仓库竞争态势加剧的信号。[来源-x](https://x.com/Teknium/status/2048710115885523444)

### AI 安全
- **规范冲突会提高大型推理模型被越狱的风险** — 一篇 arXiv 论文表明，价值观/规范冲突会显著增加大型推理模型被越狱的风险，指出当前的对齐仍然较为浅层，安全缺口依旧存在。[来源-x](https://x.com/raphaelmilliere/status/2048704379209785479)
- **创作者用 GPT-5.5 搭建项目，凸显 Claude 的缺陷** — 一位开发者使用 GPT-5.5 构建项目，并与 Claude 长期存在的问题进行对比，预告将发布一份 Claude 缺陷汇总及名为 “clawd rip” 的内容。[来源-x](https://x.com/theo/status/2048628814755012945)

### 大模型 / 基准测试
- **Nemotron-3 Nano 在金融、推理、代码的 4B 评测中夺冠** — 在覆盖 39 个任务的正面对比中，Nemotron-3 Nano 在 4B 级别模型中领跑，在金融与推理任务上表现出色，在代码任务上也保持稳健表现。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxch39/the_4b_class_of_2026_benchmark/)
- **Kimi K2.6 登顶 OpenRouter 周度 LLM 排行榜** — Kimi K2.6 升至 OpenRouter 周榜第 1 名，反映出其生态进展迅速，模型仍在持续迭代开发中。[来源-x](https://x.com/Kimi_Moonshot/status/2048693682329776223)

### 硬件 / 推理
- **Skymizer 单张 PCIe 卡实现超大规模 LLM 推理** — 一块集成 6 颗 HTX301 芯片、384 GB 内存的 PCIe 卡 reportedly 能在本地运行 700B 参数规模的大模型推理，每张卡功耗约 240W，从而降低对高显存 GPU 的依赖；更多细节预计将在 Computex 上公布。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sx2vxp/skymizer_taiwan_inc_unveils_breakthrough/)

---

## ⚡ 快讯速览

- **UniT 提出统一物理语言用于人形机器人任务迁移** — 提出一种统一的“物理语言”来实现任务在人形体机器人之间的迁移。[来源-huggingface](https://huggingface.co/papers/2604.19734)
- **Luce DFlash 在 RTX 3090 上实现 Qwen3.6-27B 两倍吞吐** — 在 RTX 3090 上为 Qwen3.6-27B 实现最高 2 倍推理吞吐提升。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sx8uok/luce_dflash_qwen3627b_at_up_to_2x_throughput_on_a/)
- **开源项目 Cua 让 AI Agents 能控制完整桌面环境** — 使 AI agents 能够与完整桌面环境交互并执行控制操作。[来源-github](https://github.com/trycua/cua)
- **中国阻止 Meta 旗下 Manus 被外国投资者收购** — 中国阻止外国投资者收购 Meta 的 Manus 资产交易。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1swy9ap/metas_2_billion_manus_acquisition_blocked_by_china/)
- **2 张 5060 Ti：是否有更优的 Qwen 3.6 27B/35B 配置？** — 社区讨论如何在 2×5060 Ti 上获得更佳的 Qwen 3.6 部署配置。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxe861/2_x_5060_ti_any_better_configs_for_qwen_36_27b_35b/)
- **OpenAI 隐私过滤器通过 ExecuTorch 在端侧运行** — OpenAI 的隐私过滤模型可借助 ExecuTorch 在本地设备上直接运行。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sx5771/got_openais_privacy_filter_model_running_ondevice/)
- **GitHub Copilot 将于 6 月 1 日起改为按使用量计费** — Copilot 自 6 月 1 日起将采用基于使用量的计费模式。[来源-x](https://x.com/github/status/2048794729274278258)
- **Symphony：用于 Issue 处理的开源 Codex Agent 协调器** — Symphony 提供一个类似 Codex 的开源 agent 编排器，用于自动处理各类 issue。[来源-x](https://x.com/OpenAIDevs/status/2048825010371039648)
- **Agentic World Modeling：基础、能力、规律及其拓展** — 提出关于 agentic 世界建模基础与能力的一种新视角和框架。[来源-huggingface](https://huggingface.co/papers/2604.22748)
- **gpt-realtime-1.5 支持语音控制的交互式应用** — 通过 gpt-realtime-1.5 为交互式应用加入语音控制能力。[来源-x](https://x.com/OpenAIDevs/status/2048871260512473385)
- **AI 公司需依赖基准测试才能真正受益于模型进步** — 呼吁将基准测试作为驱动利用模型进步、提升产品效果的核心机制。[来源-x](https://x.com/OfficialLoganK/status/2048554074107470305)
- **用于视频分析与生成的语义进度函数** — 提出一种语义进度函数，用于视频内容分析与生成过程建模。[来源-huggingface](https://huggingface.co/papers/2604.22554)
- **mattpocock/skills：面向工程师的 Agent 技能库** — 一个为真实工程师分享与复用 agent 技能的仓库。[来源-github](https://github.com/mattpocock/skills)
- **Beads：面向 AI 编码 Agent 的 Dolt 驱动记忆图谱** — Beads 提供基于 Dolt 的记忆图谱，用于增强 AI 编码 agent 的长期记忆与上下文管理。[来源-github](https://github.com/gastownhall/beads)
- **OpenClaw 在个人设备上运行的本地 AI 助手** — OpenClaw 推出可在用户自有设备上本地运行的个人 AI 助手。[来源-github](https://github.com/openclaw/openclaw)
- **致 16GB 显存用户：把你的老显卡也插上** — 为仅有 16GB 显存的用户提供实用建议，鼓励将旧 GPU 一并利用以提升本地推理能力。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1swzjnu/to_16gb_vram_users_plug_in_your_old_gpu/)
- **GBNF 调优加速 Qwen3.6 35B-A3B 与 27B** — 通过 GBNF 语法/数值约束进行调优，以加速 Qwen3.6 系列模型的推理速度。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sx7w55/gbnf_grammar_tweak_for_faster_qwen36_35ba3b_and/)
- **多模态模型端到端微调教程** — 一份覆盖“完整旅程”的教程，讲解如何对多模态模型进行端到端微调。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxgq6l/end2end_tutorial_on_finetuning_the_whole_journey/)
- **Grok 3 开源延迟引发外界质疑** — Grok 3 迟迟未开源在社区内引发越来越多的怀疑与不满声音。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sx25ir/still_waiting_for_grok_3_to_go_opensource/)
- **汇总贴展示 Claude 多年来的各种问题** — 一条线程系统整理了 Claude 这些年来暴露出的各种问题与失败案例。[来源-x](https://x.com/maria_rcks/status/2048627990817288197)
- **Qwen 3.6 27B 跑在 Strix Halo 128GB 上的体验？** — 用户讨论在 Strix Halo 128GB 平台上运行 Qwen 3.6 27B 的实际体验和性能表现。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxbvux/qwen_36_27b_on_strix_halo_128gb_any_experiences/)
- **56GB 显存本地 LLM：用 llamacpp 选哪个模型最好？** — 围绕如何在 56GB 显存条件下、借助 llamacpp 运行本地 LLM 的模型选择与配置讨论。[来源-reddit](https://www.reddit.com/r/LocalLLaMA/comments/1sxd2sc/built_myself_a_bit_of_a_local_llm_workhorse_whats/)
- **多 Agent 协作相关内容在 Twitter/X 上被重点推荐** — 汇集并突出展示多 Agent 协作的讨论与案例线程。[来源-x](https://x.com/Yuchenj_UW/status/2048616767933817291)

---

*由 AI News Agent 生成 | 2026-04-27*

━━━━━━ End of Template ━━━━━━