---
type: note
description: "L2 模块文档 — GEB 协议要求：模块级世界观，与代码同构"
timestamp: 2026-06-20
---
# yt-talks/CLAUDE.md

> **L2 模块文档** — GEB 协议要求：模块级世界观，与代码同构
> 上游：[/Users/cunyu666/Design/03_材料/LLM-Wiki/catui.md](../../../catui.md)

## 模块定位

YouTube 演讲文字稿的 wiki 入口。所有文件均为软链 → `raw/来自Youtube/` 下原文。

**目的**：让演讲稿在 wiki 知识图谱中可被引用、被检索、与 D20 演讲弹药库打通。

## 文件清单

| 文件 | 演讲者 | 主题 | 软链目标 |
|------|--------|------|----------|
| [软件基础比以往更重要_Software-Fundamentals-Matter-More-Than-Ever-Matt-Pocock_v4F1gFy-hqg.md](软件基础比以往更重要_Software-Fundamentals-Matter-More-Than-Ever-Matt-Pocock_v4F1gFy-hqg.md) | Matt Pocock | 软件工程基本功在 AI 时代更重要 | `raw/来自Youtube/...` |
| [姚顺宇在Anthropic和Gemini训练模型_Yao-Shunyu-Training-Models-at-Anthropic-Gemini_ttkd0t5qTD4.md](姚顺宇在Anthropic和Gemini训练模型_Yao-Shunyu-Training-Models-at-Anthropic-Gemini_ttkd0t5qTD4.md) | 姚顺宇（Yao Shunyu）@ Zhang Xiaojun Podcast | Anthropic/DeepMind 模型训练内幕，"英雄主义已死" | `raw/来自Youtube/...` |
| [设计师如何使用Codex_How-to-Use-Codex-as-a-Designer_GOtHFZnagO0.md](设计师如何使用Codex_How-to-Use-Codex-as-a-Designer_GOtHFZnagO0.md) | Griffin Wooldridge | 设计师用 Codex 实操指南，Codex vs Claude Code 对比 | `raw/来自Youtube/...` |
| [翁家翌谈OpenAI强化学习与后训练基础设施_Weng-Jiayi-OpenAI-RL-Post-Training-Infra_I0DrcsDf3Os.md](翁家翌谈OpenAI强化学习与后训练基础设施_Weng-Jiayi-OpenAI-RL-Post-Training-Infra_I0DrcsDf3Os.md) | 翁家翌 @ WhynotTV Podcast #4 | OpenAI 内部 RL infra 故事，post-training 工程师视角 | `raw/来自Youtube/...` |
| [Uvl-tRga98g_Designing-with-Claude-from-Prompt-to-Production.md](Uvl-tRga98g_Designing-with-Claude-from-Prompt-to-Production.md) | Dan Carey @ Anthropic | Claude Design 官方产品介绍（STT 路线：Groq Whisper）| `raw/来自Youtube/...` |
| [Claude-Architect多智能体编排_Claude-Architect-Multi-Agent-Orchestration_vRYBG_R8JAI.md](Claude-Architect多智能体编排_Claude-Architect-Multi-Agent-Orchestration_vRYBG_R8JAI.md) | — | （linter 自动入库）| `raw/来自Youtube/...` |
| [把Claude-Code变成设计天才_Turn-Claude-Code-into-a-Design-GENIUS_fVPCbCH_c1c.md](把Claude-Code变成设计天才_Turn-Claude-Code-into-a-Design-GENIUS_fVPCbCH_c1c.md) | — | （linter 自动入库）| `raw/来自Youtube/...` |
| [Cursor的Ryo-Lu谈设计活工具与编程未来_8ncYSGbfeyY.md](Cursor的Ryo-Lu谈设计活工具与编程未来_8ncYSGbfeyY.md) | Ryo Lu @ Cursor | 设计师转开发者趋势 | `raw/来自Youtube/...` |
| [Framer发布会介绍Agents与分支_Framer-Event-Introducing-Agents-Branching-and-a-new-Community_j4WW4bwWhPk.md](Framer发布会介绍Agents与分支_Framer-Event-Introducing-Agents-Branching-and-a-new-Community_j4WW4bwWhPk.md) | — | Framer 发布会 | `raw/来自Youtube/...` |
| [Ryo-Lu谈AI将设计师变为开发者_Ryo-Lu-Cursor-AI-Turns-Designers-to-Developers_PQhcHrCyU8M.md](Ryo-Lu谈AI将设计师变为开发者_Ryo-Lu-Cursor-AI-Turns-Designers-to-Developers_PQhcHrCyU8M.md) | Ryo Lu @ Cursor | AI 把设计师变开发者 | `raw/来自Youtube/...` |

## 软链约定

- **绝对路径**，便于跨目录访问
- **写操作统一改 raw 源文件**，wiki 端通过软链自动同步
- 新增文件时同步更新本 CLAUDE.md 的"文件清单"表

## 与其他模块的关系

- **上游被引用**：[speech/sources.md](../sources.md) 收录本目录中的可引用金句
- **关联模块**：[speech/outline-v1.md](../outline-v1.md)、[speech/outline-v2.md](../outline-v2.md) 引用 D20 演讲大纲
- **素材源**：[raw/来自Youtube/](../../../raw/来自Youtube/) 原始 YouTube 文字稿
