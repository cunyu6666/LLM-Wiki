---
type: index
description: "小红书笔记 · 2026-06-20 抓取"
timestamp: 2026-06-20
---
# 一文读懂 Agent、harness、Loop 等概念：AI 的边界在哪？

> 小红书笔记 · 2026-06-20 抓取
> Raw：[raw/小红书/一文读懂 Agent、harness、Loop 等概念_6a2bf71e000000002100a7d2.md](../../raw/小红书/一文读懂Agent与Harness与Loop等概念_6a2bf71e000000002100a7d2.md)
> 作者 ID：`60f18e070000000001000784`（未登录态无昵称）
> 数据：719 赞 / 717 收藏 / 10 评论 / 9 图
> OCR：macOS Vision API（zh-Hans + en, accurate）

---

## 摘要

把当下 AI 圈的所有热词（Prompt Engineering、Context Engineering、Agent、Skill、Harness、Agent Loop）拆到地基层——**和 AI 互动的本质，就是用确定的代码和提示词，去约束 AI 概率的不确定性**。

## 三段大纲

### 一、AI 在思考吗？
**概率模拟，不是逻辑推导**。界面上的"思考/Deep Think"全是 token 概率分布模拟。人类理解 1+1=2 因为我们有三维物理世界的具身认知，AI 没有。

> 0.9²⁰ ≈ 0.1215 — 20 步推理的整体走通率仅 12%。这就是为什么 AI 写短文惊艳、写长文空洞。

### 二、Agent / Harness / Skill / 上下文工程
- **Agent 上限 = 软件工程水平**，不是模型本身
- **Harness** = 套在 AI 这匹野马身上的缰绳；Agent = Harness + AI
- **Skill** 和 Harness 概念重叠、没官方标准
- **上下文工程** = 给 AI 喂干净资料，让短任务可被框定

### 三、Agent Loop 是什么？
不是新概念，本质是**用验证代码循环试错**。Boris Cherny（Claude Code 负责人）说"我不再写提示词，我写 Loop"。

> 但 Agent Loop 有明确边界：**只在有自动化验证环境的封闭任务里有效**（编程、科研数据处理）。开放性任务里，人类的经验、直觉、责任担当不可替代。

## 核心金句

> 不管包装成什么概念，核心就是：想办法用确定的代码和提示词，去约束 AI 概率的不确定性。
>
> 好用的 Agent = Harness + AI（大模型），Harness 是方向盘，AI 是发动机。
>
> 起点依然是人类。

## 与本 Wiki 的关联

- [[Catui 提示词]] — Catui 系统提示词本身就是 Harness 的具体实例
- [[Claude Code 系统提示词]] — Boris Cherny 主导的产品，Agent Loop 的实践场
- [[Codex 系统提示词]] — 另一类 Harness 实现
- [[Open Design 系统提示词]] — 设计领域的 Harness 范式

## 9 张原图（OCR 重建顺序）

1. 封面：行业造词史 + "底层逻辑非常简单"
2. 一、AI 在思考吗？— 概率接龙游戏
3. 世界模型 / 90% 准确率 / 围棋封闭系统
4. 0.9²⁰ ≈ 12% / AI 长文空洞 / 引出 Agent
5. Agent = 严密的流程图，不是 AI 全局规划
6. Harness Engineering / Skill 重叠 / 三件套
7. 上下文工程 / 引出 Agent Loop + Boris Cherny
8. 开放 vs 封闭任务 / Loop 验证机制 / Token 商业逻辑
9. Loop 边界 / 人类不可替代 / 起点是人类

---

*版本：v1.0 · 抓取日期 2026-06-20 · 标签 `#Agent` `#Harness` `#上下文工程` `#Agent Loop`*