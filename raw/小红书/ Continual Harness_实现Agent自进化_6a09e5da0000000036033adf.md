---
id: "6a09e5da0000000036033adf"
source: 小红书
author_id: "6707bd58000000000d025614"
url: https://www.xiaohongshu.com/explore/6a09e5da0000000036033adf?xsec_token=AB1npgY2-DysYWXG8EQj-jjCNYA622N7vK06XaBh6lKQc=&xsec_source=pc_collect
tags: ["AI Agent 开发", "AI", "批量入库"]
liked: 248
collected: 400
comments: 2
images: 3
ocr_engine: macOS Vision API (VNRecognizeTextRequest, accurate, zh-Hans + en)
captured: 2026-06-20
batch: "xhs mega batch #2 (19 notes, 18 success)"
readability: "english"
---

# 🎮 Continual Harness：实现Agent自进化

> 抓取日期：2026-06-20 > 数据：248 赞 / 400 收藏 / 2 评论 / 3 图 > 作者 ID：`6707bd58000000000d025614`（未登录态无昵称） > OCR：macOS Vision API

---

## 原文摘录

> 🔬 背景痛点 现在的 Agent 框架虽然给大模型配上了工具、记忆、规划能力，但部署后能力就固定了。面对长序列决策和部分可观测环境，Agent 需要不断从交互中学习，而不是靠人类反复迭代 prompt 和工具。现有的 prompt 优化方法还有个致命限制——需要环境重置，每次都得从头开始，这在真实的持续交互场景中根本不现实。
- 💡 核心方案 Continual Harness 的思路是让 Agent 自己改自己。它是一个无重置的自我改进框架，从一个最简环境接口起步——没有预设知识、没有手工工具、没有领域脚手架。Agent 在运行过程中交替执行两件事：在环境中行动，以及根据历史轨迹数据来优化自身的 prompt、子 Agent、技能库和记忆。整个过程发生在一次连续运行中，不需要 episode reset。
这个框架的前身是 Gemini Plays Pokemon（GPP）项目。该项目通...


> ⚠️ **可读性说明**：原图为英文内容（GitHub README / arXiv 论文截图），OCR 保留英文原文。如需中文理解，请结合 desc 摘要。

---

## OCR 全文（3 张图）

### 第 1 张图

![[imgs/6a09e5da0000000036033adf/1.jpg]]

Continual Harness: Online Adaptation for Self-Improving Foundation Agents Seth Karten*！ Joel Zhang*2 Tersoo Upaa Jr! Ruirong Feng' Wenzhe Lil Chengshuai Shi' Chi Jin' Kiran Vodrahalli 1Princeton University2ARISE Foundation 3Google DeepMind *Equal contribution.
Abstract. Coding harnesses such as Claude Code and OpenHands wrap foundation models with tools, memory, and planning, but no equivalent exists for embodied agents’ long-horizon partial-observability decision-making. We first report our Gemini Plays Pokemon （GPP） experiments. With iterative human-in-the-loop harness refinement, GPP became the first AI system to complete Pokemon Blue, Yellow Legacy on hard mode, and Crystal without a lost battle. In the hardest stages, the agent itself began iterating on its strategy through long-context memory, surfacing emergent self-improvement signals alongside human-in-the-loop refinement. Continual Harness removes the human fully from this loop: a reset-free self-improving harness for embodied agents that formalizes and automates what we observed. Starting from only a minimal environment interface， the agent alternates between acting anc refnirr its own prompt, sub-agents, skills, and memory, drawing on any past traject •r laePrompt-optimization methods require episode resets; Continual Harness adapts online within a single run. On Pokemon Red and Emerald across frontier models, Continual Harness starting from scratch substantially reduces button-press cost relative to the minimalist baseline and recovers a majority of the gap to a hand-engineered expert haress, with capability-dependent gains， despite starting from the same raw interface with no curated knowledge, no hand-crafted tools, and no domain scaffolding. We then close the loop with the model itself: an online process-reward co-learning loop, in which an open-source agent's rollouts through the refining harness are relabeled by a frontier teacher and used to update the model, drives Sustained in-game milestone progress on Pokemon Red without resetting the environment between training iterations.
Date: May 12, 2026 arXiv:2605.09998v1 ［cs.LG］ 11 May Correspondence: sethkarten@princeton.edu Website: https://sethkarten.ai/continual-harness 1 Introduction Agentic harnesses, the scaffolding that wraps a foundation model with tools, memory, and planning, are now standard infrastructure for autonomous coding agents. Claude Code ［2J， OpenHands ［21, and OpenClaw ［19］ let models navigate codebases, run commands, and carry state across long interactions. No equivalent exists for embodied agents.
vision-language models make almost no progress on RPG gameplay. Our Gemini Plays PokemonThe PokeAgent Challenge 7 reported that without domain-specific scaffolding, frontier （GPP） project shows that a human-supervised refinement loop can solve this scaffolding problem：

### 第 2 张图

![[imgs/6a09e5da0000000036033adf/2.jpg]]

（1） Human-in-the-loop（2） Self-improving harness（3 Model + harness co-learning HarnessHarnessHarness update updateupdate contextcontextcontext Refiner obseryetrajectoryobseryeobsere trajectog ，.rajectory act20t act EnvironmentHuman refiner EnvironmentRefinerEnvironment AgentAgentAgent weights RL trainer Figure 1. Continual Harness automates the harness refinement performed manually in GPP， and extends to joint training of model weights and harness state. Each panel shares the same topology （environment, agent, harness, refner）； only the identity of the refiner changes. （1） Human-in- the-loop: in our Gemini Plays Pokemon （GPP） experiments, a human reads trajectories and rewrites the harness, producing the frst AI system to complete Pokemon Blue, Yellow Legacy （hard mode）， and Crystal. （2） Self-improving harness: Continual Harness replaces the human with an automated refiner that operates on trajectory data within a single continuous episode; evaluated on Red and Emerald across frontier models. （3） Model + harness co-learning: after warm-up stages, an open-source model's weights and the harness state update jointly during online play.

### 第 3 张图

![[imgs/6a09e5da0000000036033adf/3.jpg]]

a Harness refinement within one episodeb Co-learning across iterations outer loop inner loop reset-free Agent model M reads（st、 、 t）at ENV0000g:0000 at~M（Ist,Htnrt） observation st harness state Ht = （p,9,K, M） iter kiter k-1iter k—2 p promptKskills g sub-agentsMmemory policyrolloutrolloutrollout Goal: 1eaveCombat-move-to-/red/brock：TO OH™Ok+1。H0 +2。H K=256 stepsK=256 steps Pallet,deliverHandLercoords（x,y）'Onix L12；K=256 steps Dak's parcel（A,FIGHT）BFS-path（）use Bulb.
0k+1=0k のVCSFT T，R（stsatsT） Refiner model M, every F steps after warmup Wlow-RShard DkSoft SFT PRM RTeacher Refine:read Tt P t.emi =（Ap、A9,AK,AM）：LoRA on 0 pairwiserelabel Apply:Ht+1 HeO3 ep.5×10-6 Figure 2. Methodology overview. （a）Harness refinement within one episode: the Agent reads （St, H, T）and emits at; every F steps the Refiner reads Tt-F:t,emits per-component edits A=（Ap, A9, AK, AM） via the meta-tool APL, and H HO A. （b） Co-learning across DAgger+PRM iterations: each iteration runs TOw inside a live-refining Ht for K=256 steps. The trajectory is scored by a pairwise PRM, low-R windows are relabeled by Gemini-3.1-pro, and a soft SFT update produces Ok+1.
The loop is reset-free: a persistent state at the end of iter k is loaded as the start of iter k+1.

---

## 抓取与 OCR 说明

- 抓取方式：`curl` + iPhone Safari UA + Referer（无需登录）
- HTML 提取：`__INITIAL_STATE__` 中 `undefined` 替换为 `null`，括号状态机解析
- 图片下载：curl 直连 `sns-webpic-qc.xhscdn.com`
- OCR：macOS Vision API（`VNRecognizeTextRequest`，accurate 级别，zh-Hans + en）
- 阅读顺序：按视觉坐标 `y` 降序 + `x` 升序重建，自适应分位数阈值
- **可读性后处理**：识别 Al→AI / Github→GitHub / scndle→schedule 等字符级误识；多列布局（GitHub README）单独标注

## 元数据

- 抓取日期：2026-06-20
- 点赞/收藏/评论：248 / 400 / 2
- 图片数：3 张（已存档 `imgs/6a09e5da0000000036033adf/1.jpg` ~ `3.jpg`）
- 作者 ID：`6707bd58000000000d025614`（未登录态无法解析昵称）

[[🎮 Continual Harness：实现Agent自进化|wiki 索引版]]
