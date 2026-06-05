---
id: "7441913256760839039"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzE5MTM0NTQ1MA==&mid=2247483822&idx=1&sn=1ea4a578c7c0992970ff932d51b7975c&chksm=97f69fec1e6c4340f1f85416c36e2fc4f080978d14830f2e465e05760e33ed50b215685389fc&mpshare=1&scene=1&srcid=0409ZBut4vFpytM0gRdxlpFd&sharer_shareinfo=105dcca215968f2be8739c3611692321&sharer_shareinfo_first=105dcca215968f2be8739c3611692321
author: "是小邓同学 小邓同学的研习社"
collected: 2026-04-09
tags: []
---

# GitHub 热点周报：172k Stars 达成！史上最快破纪录的 AI 项目现身

# GitHub 热点周报：172k Stars 达成！史上最快破纪录的 AI 项目现身

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5MTM0NTQ1MA==&mid=2247483822&idx=1&sn=1ea4a578c7c0992970ff932d51b7975c&chksm=97f69fec1e6c4340f1f85416c36e2fc4f080978d14830f2e465e05760e33ed50b215685389fc&mpshare=1&scene=1&srcid=0409ZBut4vFpytM0gRdxlpFd&sharer_shareinfo=105dcca215968f2be8739c3611692321&sharer_shareinfo_first=105dcca215968f2be8739c3611692321)是小邓同学 小邓同学的研习社


> 字数 1727，阅读大约需 9 分钟

最近开源社区的节奏快得离谱，尤其是 AI 编程工具领域，几乎每天都在诞生"新王"。为了帮大家节省筛选时间，我决定开启一个新坑：每周固定更新一期，深度复盘 GitHub Trending 榜单前三（或最值得关注）的热门项目。

本周项目预览：

1.**claw-code** - Claude Code CLI 的 Rust 版，史上最快破 10 万 stars  
2. **oh-my-codex** - 给 Codex 用的增强工具，工作流、agent teams、HUD 全配齐  
3. **claude-howto** - 最实用的 Claude Code 入门指南，11-13 小时从入门到熟练  
4. **VibeVoice** - 微软开源的语音 AI，支持 50+ 语言，长音频处理是亮点

## 1. claw-code：史上最快破 10 万 stars 的项目

*
  • **GitHub** : ultraworkers/claw-code
*
  • **Stars** : 172k
*
  • **语言** : Rust

### 这是什么

claw-code 是 Claude Code CLI 的 Rust 开源实现。Anthropic 官方只有 TypeScript 版，这是社区用 Rust 重写的版本。有意思的是，这个项目本身就是用 oh-my-codex 构建的------算是"自己构建自己"。

### 核心内容

*
  • **Rust 实现** ：用 Rust 重写了 Claude Code CLI
*
  • **工作空间** ：完整的 Rust workspace
*
  • **CLI** ：和 Claude Code 类似的命令行接口
*
  • **测试** ：配套的 Python 参考工作空间和审计工具

### 快速开始

    cd rust
    cargo build --workspace
    ./target/debug/claw --help
    ./target/debug/claw prompt "summarize this repository"

认证方式：

    export ANTHROPIC_API_KEY="sk-ant-..."
    # 或者
    cd rust
    ./target/debug/claw login

### 我的感受

10 万 stars 什么概念？几天时间就达成了，史上最快。这个项目火的原因很简单：这周 Claude Code 源码刚通过 source maps 泄露了 50万行 TypeScript，本项目是 Claude Code 的 Rust 版，性能更好、部署更方便。对于喜欢 Claude Code 但想要 Rust 性能的人来说，这个版本值得关注。

## 2. oh-my-codex：让你的 Codex 变成"工作站"

**GitHub** : Yeachan-Heo/oh-my-codex  
**Stars** : 16,941  
**语言** : TypeScript

### 这是什么

oh-my-codex（简称 OMX）是给 OpenAI Codex CLI 用的增强工具。官方说法是"workflow layer"------在 Codex 外面包了一层更好的工作流。简单说，它让原本只能单兵作战的 Codex 变得更强：加了 hook、加了 agent teams、加了 HUD 界面，还能自定义各种工作流。

### 核心功能

1.
   1. **标准工作流** ：用 $deep-interview 澄清需求 → $ralplan 制定计划 → $ralph 持续执行 → $team 并行协作
2.
   2. **Agent 团队** ：支持多 agent 协同工作，用 tmux 做持久化运行
3.
   3. **持久状态** ：在 .omx/ 目录下存计划、日志、记忆、运行时状态
4.
   4. **HUD 界面** ：实时监控 agent 工作状态
5.
   5. **Skills 扩展** ：自带一系列常用技能

### 适合谁

*
  • 已经会用 Claude Code，想进一步提升效率的人
*
  • 需要处理复杂任务，想用多 agent 协作的人
*
  • 想把 Codex 变成完整工作台的人

### 快速开始

    npm install -g @openai/codex oh-my-codex
    omx setup
    omx --madmax --high

然后正常使用 Codex，但多了几个命令：

*
  • $deep-interview "..." - 澄清需求边界
*
  • $ralplan "..." - 制定并批准计划
*
  • $ralph "..." - 持续执行直到完成
*
  • $team 3:executor "..." - 并行执行

### 我的感受

这个项目火是有道理的。Codex 本身很强，但缺一个标准化的"怎么用才最好"的框架。OMX 补上了这个缺口，而且跟 OpenClaw 的思路其实有点像------都是给 Agent 加工作流、加状态管理、加多 agent 协作。如果你在用 Codex，值得试试。

## 3. claude-howto：最实用的 Claude Code 入门指南

**GitHub** : luongnv89/claude-howto  
**Stars** : 20,707  
**语言** : Python

### 这是什么

这是一个视觉化的 Claude Code 入门指南，从基础概念到高级 agent 都有覆盖。最重要的是，有大量 copy-paste 模板，拿来就能用。

### 解决的问题

很多人装了 Claude Code，会用但不知道还能怎么用：

*
  • 官方文档只讲功能，不教怎么组合
*
  • 没有清晰的学习路径
*
  • 示例太基础，"hello world"级别的演示没法用到生产环境

这个项目就是来解决这些问题的。

### 内容结构

10 个教程模块，覆盖 Claude Code 所有功能：

*
  • Slash Commands（基础）
*
  • Memory（记忆）
*
  • Checkpoints（检查点）
*
  • CLI Basics
*
  • Skills（技能）
*
  • Hooks（钩子）
*
  • MCP（模型上下文协议）
*
  • Subagents（子代理）
*
  • Advanced Features

每个模块都有：视觉化的 Mermaid 图示、可直接复制的配置模板、预计学习时间。

### 学习路径


|      级别      |        你能做什么        |       从这里开始       |   时间   |
|--------------|---------------------|-------------------|--------|
| Beginner     | 启动 Claude Code 并聊天  | Slash Commands    | \~2.5h |
| Intermediate | 使用 CLAUDE.md 和自定义命令 | Skills            | \~3.5h |
| Advanced     | 配置 MCP 服务器和 hooks   | Advanced Features | \~5h   |


完整的 10 个模块学完大概 11-13 小时。

### 特色功能

*
  • **自测quiz** ：运行 /lesson-quiz 或 /self-assessment，帮你定位知识盲区
*
  • **个性化路径** ：根据你目前会的程度，推荐下一步该学什么
*
  • **生产级模板** ：不是简单 demo，是真的能用到项目里的配置

### 我的感受

这个项目特别适合刚接触 Claude Code 的人。官方文档是好的，但太散了，没有一条清晰的路。这个 guide 把散的知识串起来了，而且模板真的能直接用。20k+ stars 说明大家都觉得有用。

## 4. VibeVoice：微软开源的语音 AI

**GitHub** : microsoft/VibeVoice  
**Stars** : 36,564  
**语言** : Python

### 这是什么

VibeVoice 是微软开源的语音 AI 家族，包括语音识别（ASR）和语音合成（TTS）两部分。核心创新点是用了一个超低帧率（7.5 Hz）的连续语音 tokenizer，能在保持音质的同时大幅提升计算效率。支持长达 60 分钟的长音频单次处理。

### 主要模型


|           模型            |   用途   |    快速体验    |
|-------------------------|--------|------------|
| VibeVoice-ASR-7B        | 语音识别   | Playground |
| VibeVoice-TTS-1.5B      | 语音合成   | Colab      |
| VibeVoice-Realtime-0.5B | 实时语音合成 | Colab      |


### 支持的特性

*
  • **多语言** ：支持 50+ 语言
*
  • **长音频** ：ASR 支持 60 分钟单次处理，TTS 支持 90 分钟合成
*
  • **多speaker** ：TTS 支持最多 4 个不同 speaker
*
  • **微调** ：提供 finetuning 代码，可以自己训练
*
  • **vLLM 推理** ：支持快速推理部署
*
  • **HuggingFace Transformers** ：已集成到 Transformers v5.3.0

### 实际应用

这个项目已经被开源社区采用了。Vibing，一个语音驱动的输入法，基于 VibeVoice-ASR 构建，已支持 macOS 和 Windows。

### 我的感受

微软这次挺有诚意的。虽然之前因为一些原因下掉了 TTS 代码，但重新开源的 ASR 和 Realtime TTS 都很能打。36k stars 在语音领域算是很高的了。如果你想做语音相关的应用，值得关注。

## 总结

纵观本周榜单，工具链整合是绝对的关键词。  
我们正在从"调教单个 AI"转向"管理 AI 团队"。无论是 OMX 的工作流，还是 claw-code 的高性能底座，都在告诉我们：2026 年的编程，拼的不再是手速，而是你构建和驾驭 Agent 工作流的能力。

以上就是本期 GitHub 热点观察。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5MTM0NTQ1MA==&mid=2247483822&idx=1&sn=1ea4a578c7c0992970ff932d51b7975c&chksm=97f69fec1e6c4340f1f85416c36e2fc4f080978d14830f2e465e05760e33ed50b215685389fc&mpshare=1&scene=1&srcid=0409ZBut4vFpytM0gRdxlpFd&sharer_shareinfo=105dcca215968f2be8739c3611692321&sharer_shareinfo_first=105dcca215968f2be8739c3611692321)

