---
id: "6a2bdb14000000001503dc0e"
source: 小红书
author_id: "5652a49e62a60c290444c4ba"
url: https://www.xiaohongshu.com/explore/6a2bdb14000000001503dc0e?xsec_token=AB5tR21seiJs92_Qsp_-GDG67wicEGFUdAHUWfOYujpQw=&xsec_source=pc_collect
tags: ["AI Agent 开发", "AI", "批量入库"]
liked: 197
collected: 311
comments: 
images: 8
ocr_engine: macOS Vision API (VNRecognizeTextRequest, accurate, zh-Hans + en)
captured: 2026-06-20
batch: "xhs mega batch #1 (10 notes)"
---

# Loop Engineering 是什么｜8 张图讲透

> 抓取日期：2026-06-20 > 数据：197 赞 / 311 收藏 /  评论 / 8 图 > 作者 ID：`5652a49e62a60c290444c4ba`（未登录态无昵称） > OCR：macOS Vision API

---

## 原文摘录

> 这两周 timeline 全在聊 Loop Engineering，我把它整明白了，顺手做成了 8 张图。
说白了就一句话：别再一句句手写 prompt，改成设计一个会自己派活、检查、记录、再接着干的闭环，让这套系统去 prompt agent，而不是你盯着键盘一轮一轮敲。Claude Code 负责人 Boris Cherny 原话——"写 loop 才是现在的工作"。
为什么是现在不是去年？不是模型突然变强，是搭这种闭环要的零件——定时触发、隔离分支、skills、连接器、子代理，再加一个外部记忆——现在全内建进 Codex 和 Claude Code 了；去年你还得自己写一堆 bash 自己维护。
但别上头。它有三件事解决不了，而且 loop 越顺反而越要命：验证还是你的责任、你对代码的理解会越欠越多、最舒服的那个"啥都不想直接收货"最危险。所以我最喜欢它的收尾——build the...

---

## OCR 全文（8 张图）

### 第 1 张图

![[imgs/6a2bdb14000000001503dc0e/1.jpg]]

• AI编程•2026 范式拐点DEEP DIVE 什么是Loop Engineering 循环工程 别再一句句手写 prompt—而是设计一个会自己派活、检查、记录、再继续的闭环，然后让这个系统去 prompt agent。工作从”操作 agent”升到“设计驱动 agent 的闭环"。
— 2026.6•两个产品的核心人物，同一个判断 别再给编程 agent 写 prompt 了— 要去设计 prompt 它们的 loop。
Peter Steinberger PSPDFKit C有人现 OpenAI Codex 团队 不再亲自 prompt，让 loop 决定下一步—写 loop，才是现在的工作。
Boris Cherny Anthropic• Claude Code 负责人 PROMPTCONTEXTHARNESSLOOP 杠杆点一路外移：一句话一喂对上下文 一单个 agent 的环境一自动驱动的闭环 8 图拆透左滑 是什么为什么是现在5 个零件+1 记忆还解决不了什么

### 第 2 张图

![[imgs/6a2bdb14000000001503dc0e/2.jpg]]

• EVOLUTION• 四次焦点迁移Loop 是这条线的最新一层 不是模型突然变强，是杠杆点一路外移：你做的事，从”写好一句话“变成“设计整个闭环"。
PROMPT工程河象一段输入文本 ENGLNEERING关键词怎么跟模型说好这一句 提示词工程典型system prompt•few-shot•ReAct 2022 - 2024 02 CONTEXT工程对象模型当前看到什么 ENGINEERING关键词把对的信息喂进有限的窗口 上下文工程典型RAG•长期记忆•上下文压缩 2024 - 2025 03 HARNESS工程对象单个 agent运行的整个环境 ENGINEERING关键词工具 •沙箱•验证 •恢复 执行外壳工程典型sandbox• hooks• 子代理•trace 2025 - 2026 04工程对象驱动多次运行的闭环系统 LOOP关键词谁发起•多久一次 •何时停•谁来 ENGINEERING检查 循环工程典型/Loop•/goal• 调度• 编排• 状态文 2026现在件 每往外一层，越少"操作"一越多"设计"；LOOP 是目前的最外层。

### 第 3 张图

![[imgs/6a2bdb14000000001503dc0e/3.jpg]]

• THE SHIFT• 交互模式翻面 从操作 agent，到设计闭环 过去两年的交互是一条直线；loop engineering 把它折成了自己转的闭环。
旧法•OLD新法•NEW 线性对话自动闭环 怎么做怎么做 写 prompt 读结果 再写下一个，一轮接一轮设计闭环 - 它自己派活•检查•记录•接续 你的角色尔的角色 操作员：全程握着工具、在键盘前设计者：定规则、边界、验收标准 上限在哪今天写多少 prompt，就产出上限在哪 多少不在场也产出，上限是你的审查与判断 被绑在每一轮 prompt 上设计一次，持续运转 同一个 agent--区别只在：你在循环里一轮轮 prompt，还是在循环外设计它自己跑。

### 第 4 张图

![[imgs/6a2bdb14000000001503dc0e/4.jpg]]

• WHY NOW• 为什么是现在为什么是现在，不是去年 不是模型突然变强——是搭一个 loop 需要的零件，终于内建进了产品。
一年前ITHEN • 想要 loop？只能自己写一堆 bash 脚本 •自己永远维护下去，没人帮你 •只有你一个人看得懂，难复用 现在 Now 搭1oop的零件，全部变成产品自带的原生能力： AutomationsWorktreesSkiLLsConnectors Sub-agents OpenAl Codex 有，Claude Code 也有—同一套形状。
基础设施到位，行为模式才会变。形状一样—别纠结用哪个工具，设计一个两边都能跑的 loop。

### 第 5 张图

![[imgs/6a2bdb14000000001503dc0e/5.jpg]]

• THE LOOP•5 个零件 +1 处记忆搭一个 loop， 5 个零件让它转起来，1处记忆让它记得住。就这6块 Automations定时发现+分诊，是 loop 的心跳 自动触发在产品里：/Loop•/goal:cron ②Worktrees隔离工作区每个 agent 独立 checkout，并行不打架 在产品里：git worktreeisolation: worktree 3Skills技能项目知识写成文件，不必每次重讲 在产品里：- e（Codex / Claude Code 同款） Connectors接 issue / Slack / 数据库，是loop 的手脚 连接器在产品里：基于 MCP，两边通用 5Sub-agents子代理写代码的和检查的分开，别自己批作业在产品里：.claude/agents•.codex/agents Memory活在对话之外的 markdown / Linear-"agent会忘，repo不会" 记忆 脊柱在产品里：AGENTS.md• 进度文件，Linear board

### 第 6 张图

![[imgs/6a2bdb14000000001503dc0e/6.jpg]]

• ONE LOOP•一个真实的 loop每天早上，自己跑一遍 下面这套，你只设计一次——之后没再亲手写过一条 prompt。
①AUTOMATION自动启动每天早上在 repo上自己启动，不用你动手 2TRIAGE读＋分诊一个 skill 读昨天CI 失败、open issue、最近 commit，写进状态文件 3WORKTREE隔离分支每个值得诚的友现，开一个独立 worktree ④DRAFT +REVIEW一个 sub-agent 写修复，另一个对照 skills 和测 起草＋审试审 5SHIP交付connector 开 PR、更新 ticket；搞不定的丟回inbox 给人 状态文件记住进度，明早从这里接着跑——全程你没写一条 prompt，只设计了一次。

### 第 7 张图

![[imgs/6a2bdb14000000001503dc0e/7.jpg]]

• THE LIMITS• Loop 解决不了的 3件事loop 越好，这3件越尖锐 它们不会随 loop 变好而消失—一反而会被一个顺畅的 loop 放大。
VERIFICATIONloop 在你不在场时跑，也在你不在场时犯 验证仍是你的错。“完成"只是声明，不是证明。
• 你的活：交付你确认能跑的代码 ②COMPREHENSION交付越快你读得越少，代码和你的理解差距越 理解债务•顺畅的 Loop，让这笔债积得更快大。
3SURRENDER认知投降loop跑顺了，容易不再有判断—一它给啥你收啥。
•最舒服的姿势，最危险 带判断地设计loop，它是加速器；用它逃避思考，它是投降。同一个动作，相反结果。

### 第 8 张图

![[imgs/6a2bdb14000000001503dc0e/8.jpg]]

• CLOSING• 写在最后 Build the Loop.Stay the engineer.
搭你的 loop—一但像一个打算继续做工程师的人那样搭， 而不是只负责按 Go 的人。
杠杆点移动了，不是工作变轻松了。你的价值，从"写好 prompt"，变成"设计可靠的loop" +判断它的产出。
你分得出。同样一个 loop：有人用它跑得更快，有人用它逃避理解。loop 分不出区别一 NEXT• 下一篇从O，搭你的第一个 loop觉得有用 先收藏

---

## 抓取与 OCR 说明

- 抓取方式：`curl` + iPhone Safari UA + Referer（无需登录）
- HTML 提取：`__INITIAL_STATE__` 中 `undefined` 替换为 `null`，括号状态机解析
- 图片下载：curl 直连 `sns-webpic-qc.xhscdn.com`
- OCR：macOS Vision API（`VNRecognizeTextRequest`，accurate 级别，zh-Hans + en）
- 阅读顺序：按视觉坐标 `y` 降序 + `x` 升序重建

## 元数据

- 抓取日期：2026-06-20
- 点赞/收藏/评论：197 / 311 / 
- 图片数：8 张（已存档 `imgs/6a2bdb14000000001503dc0e/1.jpg` ~ `8.jpg`）
- 作者 ID：`5652a49e62a60c290444c4ba`（未登录态无法解析昵称）

[[Loop Engineering 是什么｜8 张图讲透|wiki 索引版]]
