---
id: "7419427343690631972"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247505227&idx=1&sn=3caf9e292abe8eaf966e7d3f50e800ba&chksm=c1030e46030e2f1b23684a1e7b69263602f403b7307aed5d6991eb0aa3a5ad3f614ac7252297&mpshare=1&scene=1&srcid=0206bukENQUPzG06tvqujK24&sharer_shareinfo=cc1855a31efa6ba4308c345128a3140f&sharer_shareinfo_first=cc1855a31efa6ba4308c345128a3140f
author: "开源星探 开源星探"
collected: 2026-02-06
tags: []
---

# 6.3K Star！全球首款开源 Agent Skills 构建神器，Agent 的御用“兵工厂”！

# 6.3K Star！全球首款开源 Agent Skills 构建神器，Agent 的御用"兵工厂"！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247505227&idx=1&sn=3caf9e292abe8eaf966e7d3f50e800ba&chksm=c1030e46030e2f1b23684a1e7b69263602f403b7307aed5d6991eb0aa3a5ad3f614ac7252297&mpshare=1&scene=1&srcid=0206bukENQUPzG06tvqujK24&sharer_shareinfo=cc1855a31efa6ba4308c345128a3140f&sharer_shareinfo_first=cc1855a31efa6ba4308c345128a3140f)开源星探 开源星探


如果说 2025 年我们还在为"哪个大模型更聪明"争得面红耳赤，那么 2026 年的风向标已经彻底变了。

现在大家只关心一件事：**谁能让 AI 真正把活干了？**

大家都在用 Cursor 和 Claude Code 写代码，但这类 AI 编程工具最缺的是什么？是现成的、可靠的、可复用的业务逻辑（Skills）。

直到我发现了这个全球首款开源 Agent Skills Builder 神器：**Refly** ，它的出现几乎是冲着这些痛点正面开火：
> **一句话 → 生产级 Agent Workflow**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FrfBHhQhezUia0ymVCKekuNk0oPXX1jrnXwJSzkx51Y8M3hs5lr2ibvNyIq3v0zRzwrI2GQmSkaibzfTC1dpWSQJd38tFP8gicKLAKk1iaOgRNaJI%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

更狠的是，它不是 Demo，不是玩具，而是：

*
  • 全球首个 **开源 Agent Skills Builder**
*
  • 面向非技术用户的「工作流版 Canva」
*
  • 面向 Agent 时代的 **确定性执行引擎**

Refly 它不是一个刚开源的工具，但它却看到了在 Skills 时代的可能性。

#### Refly 是什么？

Refly = 面向 Agent 时代的「氛围式（Vibe）」工作流平台

你可以把它理解为：

*
  • 非技术用户的 n8n
*
  • 工作流版的 Canva
*
  • Agent 世界的 Skills 工厂

但更准确地说，它在做一件以前没人真正做好的事：
> **把「意图」直接变成「可控、可复用、可上线」的 Agent 能力。**

Refly 的核心不是"画流程图"，而是 **Skill（技能）** 。

#### 最炸裂的能力

Refly 的核心构建方式叫：Vibe 构建（Copilot 主导）

你不需要：

*
  • 设计节点
*
  • 思考状态机
*
  • 写 YAML/JSON

你只需要说一句话，比如：
> "每天抓取 X 上的 AI 开源项目，筛选 500 Star 以上的，生成中文摘要并推送到飞书。"

Refly 会做三件事：

1.
   1. **理解你的业务意图**
2.
   2. 将意图编译为 **Model-Native DSL**
3.
   3. 生成 **确定性、可复用、可组合** 的 Agent Skill

这不是 Prompt 拼装，而是 **意图 → 确定性程序** 。

*为什么这一步很重要？*

因为它解决了 Agent 最大的三个痛点：

*
  • ❌ Prompt 不稳定
*
  • ❌ Token 成本失控
*
  • ❌ 逻辑不可复用

Refly 的 DSL 是 **为 LLM 执行而生的** ，不是给人看的。

结果是：

*
  • 执行更快
*
  • Token 更省
*
  • 行为可预测

官方给出的数据是：
> **3 分钟，把企业 SOP 变成可上线的 Agent Skill**

这对内容创作者、运营、分析师、产品经理来说，杀伤力极大。

#### 以可控方式执行

Refly 的运行时是：

*
  • **有状态的**
*
  • **可暂停的**
*
  • **可人工介入的**

你可以：

*
  • 在关键步骤暂停
*
  • 审核中间结果
*
  • 手动修正后继续执行

这使它第一次满足了 **企业级合规和可审计** 的要求。

#### 统一 Agent 堆栈

Refly 并不把自己限制在"一个平台"。

你构建的 Skill，可以被导出为：

*
  • Claude Code/Cursor 的原生工具
*
  • API（供前端或系统调用）
*
  • Slack/Lark/飞书/Teams 的 Webhook
*
  • Agent 框架（AutoGen/LangChain/Manus）

一次构建，任意 Agent 环境复用，可直接上线生产环境。

#### Skills = 资产，而不是脚本

Refly 另一个非常"工程化"的设计是：Skill 注册体系。

在 Refly 里：

*
  • Skill 是一等公民
*
  • 有版本
*
  • 有权限
*
  • 有审计日志

你可以：

*
  • 在组织内共享 Skill
*
  • 把成熟能力沉淀为基础设施
*
  • 复用到不同 Agent / 应用 / 团队

这一步，直接把 Agent 从「个人玩具」推进到了「组织能力」。

*** ** * ** ***

#### 生态：不是封闭平台，而是桥梁

输入侧（工具 \& 协议）：

*
  • **3000+ 原生工具** ：Stripe/Slack/Salesforce/GitHub...
*
  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FrfBHhQhezUgLUxgg49cNSUabEG9Zu5XoOib8kCjm1GWsTLX3Gua3NvdALHDnOw0Dx3voboXcpGg3s0Gt6gIYU7lb0urwUCcjuqe4DrNVK3nU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

<!-- -->

*
  • **完整 MCP 支持**
*
  • **私有技能连接器** ：数据库/内部系统/私有脚本

输出侧（运行环境）：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FrfBHhQhezUiaZGjxQufnfkMvgEtzkXShqpxzSjTtMWL6IlEiaticfqXa145iaAt5TAdUUia263pUqYASZglsnq4vFibjTTDyib5ACIgibluGoteiaGuM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

*
  • AI 编程工具（Claude Code/Cursor）
*
  • 应用前端（有状态 API）
*
  • 自动化中心（企业 IM）
*
  • Agent 框架 \& Python 技术栈

Refly 的定位非常清晰：Refly 是 Agent 世界的"通用技能中枢"。

#### 写在最后

Refly 是 AI Native Workflow 的典型代表。

它把"自动化"的门槛降到了地板上。

过去，如果你想做一个自动化工作流，你得是"半个程序员"。 现在，只要你逻辑清晰，懂业务，会说话，你就是最好的 Agent 架构师。

它把复杂的代码逻辑封装成了可视化的画布，把晦涩的 API 封装成了自然语言的指令。它让 Claude Code、Cursor、Manus 这些超级大脑，终于有了趁手的兵器。

在这个 AI 一天一个样的时代，掌握"制造工具"的能力，永远比只通过聊天框"使用工具"要高一个维度。

Refly 已经把锤子递到了你手里，接下来，看你想造什么了。

如果你一直眼馋 n8n 的强大但被它的复杂度劝退，或者你需要快速构建大量的 Agent Skills 给团队使用，Refly 绝对是目前最好的选择之一。

官网：https://refly.ai/

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FrfBHhQhezUiaK3FJsahm0gd9FXykNTibSwXmQUPVTvXxRCP8x1EoxyiaOPGjzhgkxHbhEWGVPFZDpoibfoTKTY4nHlNOOXoqlHq4sPzVlaxJKgs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

GitHub：
> https://github.com/refly-ai/refly


![](https://image.cubox.pro/cardImg/4b5uzdwlzim32fi21mqn4gb4p09jfaphbqk26wxxock1xs0pv7?imageMogr2/quality/90/ignore-error/1)

**开源星探**

专注于分享GitHub上优质、有趣、实用的开源项目、工具及学习资源，为互联网行业爱好者提供优质的科技技术资讯。

613篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNjA8gwicXyeKqAjyn8A3ob9xT4DDY8DB3JCvIaM6JKWXFsgCxznXicJhpRYJ5MIPb9xvgGA4WYhPagIKorlScib0Q%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D4)

如果本文对您有帮助，也请帮忙点个 赞👍 + 在看 哈！❤️


**在看你就赞赞我！**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNjA8gwicXyeLZdEkueqhds4y07sImrPvibkDIsnVCibl5ibS6jSiccRh6RtH8ZqBPBWSib0kn7Ep6mP5YPJCJkraJ3kw%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D5)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247505227&idx=1&sn=3caf9e292abe8eaf966e7d3f50e800ba&chksm=c1030e46030e2f1b23684a1e7b69263602f403b7307aed5d6991eb0aa3a5ad3f614ac7252297&mpshare=1&scene=1&srcid=0206bukENQUPzG06tvqujK24&sharer_shareinfo=cc1855a31efa6ba4308c345128a3140f&sharer_shareinfo_first=cc1855a31efa6ba4308c345128a3140f)

