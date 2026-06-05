---
id: "7424766550952906166"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503771&idx=1&sn=c0ae78600263d4f0b2049739dc8d0737&chksm=ebbdd408df9180d72b70319d6170ec86625f69a9a9f5637bdb1024af1df00e2edc1091e71c88&mpshare=1&scene=1&srcid=0220E1O69p96Loco04judwl2&sharer_shareinfo=d335c9495cd17985442a5e60246081aa&sharer_shareinfo_first=d335c9495cd17985442a5e60246081aa
author: "三丰 soft张三丰"
collected: 2026-02-21
tags: []
---

# 【开源】Vibe Coding已过时？35.9K Star！一个人顶一个团队：这个AI开发框架把PRD、架构、代码全包了

# 【开源】Vibe Coding已过时？35.9K Star！一个人顶一个团队：这个AI开发框架把PRD、架构、代码全包了

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503771&idx=1&sn=c0ae78600263d4f0b2049739dc8d0737&chksm=ebbdd408df9180d72b70319d6170ec86625f69a9a9f5637bdb1024af1df00e2edc1091e71c88&mpshare=1&scene=1&srcid=0220E1O69p96Loco04judwl2&sharer_shareinfo=d335c9495cd17985442a5e60246081aa&sharer_shareinfo_first=d335c9495cd17985442a5e60246081aa)三丰 soft张三丰


最近在 GitHub 上看到一个非常有意思的开源项目------BMAD-METHOD。

目前 Star 数已经冲到35.9K，在 AI 编程圈里热度很高。

它的全称是Breakthrough Method for Agile AI-Driven Development，你可以把它理解成一套"AI 敏捷开发框架"：
> 它用一整套多智能体（Multi-Agent）来模拟一个完整的软件团队（产品经理、架构师、开发、测试......），帮你把从想法到代码的全过程"流程化、文档化、可控化"。

注意，它不是要取代你，而是让你一个人就能拥有一个专业团队的生产力。

*** ** * ** ***

## 🤔 为什么会有 BMAD-METHOD？


一句话总结：因为"让 AI 写代码"这件事，已经进入了"深水区"。

过去一年，我们经历了从"ChatGPT 写脚本"到"IDE 里各种 Copilot/Cursor"的进化，很多人惊呼"一个人顶一个团队"。

但问题也随之而来：

*
  上下文丢失：项目一大，AI 就忘了之前的需求和架构，开始乱写。
*
  计划混乱：今天加个登录，明天改个支付，需求像打补丁，代码越来越难维护。
*
  文档缺失：很多项目做完，PRD、架构图、测试用例散落各处，甚至根本没有。


这些问题，本质上是：我们只是把 AI 当成了一个更聪明的"代码打字员"，却没有给它一个"团队"和"流程"的框架。

于是，BMAD-METHOD 诞生了。

它的目标很明确：
> 把 AI 从"写代码的工具"，升级为"遵循敏捷流程的虚拟开发团队"，让 AI 编程从"好玩"变成"可靠、可维护的生产力工具"。

*** ** * ** ***

## 💡 核心思路：AI 即团队 + 先规划后编码


BMAD-METHOD 的核心理念，可以浓缩成两句话：

*
  AI 即团队：内置一整套专业 AI 代理（Analyst、PM、Architect、Scrum Master、Dev、QA 等），模拟真实团队角色。
*
  先规划后编码：严格遵循"先规划，后编码"的敏捷思想，用 AI 把需求、架构、任务都梳理清楚，再进入实现阶段。


它有两个关键创新点：

## 1. 代理规划（Agentic Planning）


在动手写代码前，先让 AI 团队帮你把"要做什么、怎么做"想清楚。

Analyst / 产品经理代理：将你的模糊想法，转化为结构化的项目简报和详细的 PRD（产品需求文档）。

架构师代理：基于 PRD，设计技术栈、系统架构、目录结构等，并输出 architecture.md等文档。

这个过程就像你在和一支专业团队开需求评审会，最终产出的是一套完整、一致的规划文档，而不是零散的聊天记录。

## 2. 上下文工程化开发（Context-Engineered Development）


这是 BMAD 非常"工程化"的一点：它把"上下文"当成一等公民来管理。

Scrum Master 代理：将 PRD 和架构文档，拆解成一系列详细的"用户故事"（User Story），每个故事都包含实现细节、验收标准和相关上下文。

开发代理：只加载当前任务的"故事文件"进行开发，避免了被整个项目的海量信息淹没。

简单说，就是"一个故事，一份上下文，一次开发"，极大降低了 AI 的"幻觉"和"跑偏"概率。

*** ** * ** ***

## ⚙️ 工作流程：四阶段闭环


BMAD-METHOD 的工作流程非常清晰，主要分为四个阶段：

分析阶段（可选）

由 Analyst 代理进行市场调研、竞品分析，输出项目简报（Project Brief）。

规划阶段

方案设计阶段

进一步细化架构，明确技术选型、API 契约、数据库设计等，确保方案的可落地性。

实施阶段

这个流程在 BMAD 中被称为"四阶段开发生命周期"，并且支持 Quick / Standard / Enterprise 等不同复杂度的"轨道"，非常灵活。

*** ** * ** ***

## 🚀 如何使用 BMAD-METHOD？


上手非常简单，官方提供了成熟的脚手架和 CLI 工具。

    npx bmad-method install


执行完之后，BMad会在你的项目根目录下创建一个.bmad文件夹，里面包含了所有的工作流配置和Agent定义。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F6wEpbjZhHQzwKTXB5PYdm4riafnP1NZN6vKRXPvuEgwCicNQUuX0YrWRD1DkFMuNrSmpXBCvdk4Bf0lPAYEgwhErBOWsOThdxGZicGPicCEN6p0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

然后在Claude Code、Cursor、Windsurf这些AI IDE里打开项目，直接输入：

    /bmad-help


就能看到BMad的智能助手界面。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6wEpbjZhHQxAHKJAYbgXduoSu9sqsxLo8iamsjdd6fJiaQJg0oGmoAhqyXTllvW7eOUoG9aEricCPqVkk8ufCrQHt3X6VONdXibFFj9EAIjPicVQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

举个例子，你可以这样问：

"我有一个T恤生意，想做一个能撑住百万用户的Web应用，该怎么规划？"

BMad不会直接甩给你一堆代码，而是先派业务分析师Mary上场，帮你梳理需求、定义用户画像、明确MVP范围。

这就是BMad和其他AI工具最大的不同------它不是"替你思考"，而是"引导你思考"。

*** ** * ** ***

## 👍 核心优势


真正的"AI 团队"体验

内置 20+ 专业角色，覆盖从需求到测试的全流程，让你一个人就能体验团队开发模式。

高度结构化与可扩展

采用"Agent-as-Code"理念，智能体以 Markdown/YAML 文件形式定义，与代码一同版本管理。支持通过 BMad Builder (BMB) 创建领域特定的智能体。

上下文工程化，告别"失忆"

通过信息分片（Sharding）和"故事文件"机制，确保每个开发任务都有完整、纯净的上下文，有效减少 AI 的"幻觉"。

与现有工具无缝集成

它是一个"框架层"，可以与 Cursor、Claude Code 等 AI IDE 完美配合，不改变你的开发习惯。

强调人机协作（Human-in-the-loop）

在关键节点（如 PRD 确认、架构评审）强制人工决策，确保项目方向不偏离。

实战效果显著

已有开发者使用 BMAD 完整开发了一个 CLI 工具，从需求到测试全流程 AI 参与，效率提升 10 倍以上，并产出了高质量的可维护代码。

*** ** * ** ***

## 🆚 同类工具对比

|              工具/方法论              |         核心定位         |             与 BMAD 的主要区别              |
|----------------------------------|----------------------|---------------------------------------|
| **传统 AI 编程助手** (Copilot, Cursor) | 代码补全、片段生成            | 无流程、无角色分工，易出现上下文丢失和架构混乱。              |
| **LangChain / AutoGPT**          | 通用大模型应用开发框架          | 偏向底层，需自行设计流程和角色，对敏捷开发实践支持不足。          |
| **Spec 方法论 / Kiro Spec**         | 规范驱动开发 (Spec-Driven) | 更轻量，侧重于"文档即规范"，AI 角色分工和流程化不如 BMAD 完整。 |
| **PRP / 6A 工作流**                 | 结构化 AI 协作流程          | 多为方法论或实践总结，缺少像 BMAD 这样成熟的开源框架和工具链支持。  |


一句话总结：

传统助手：帮你写代码。

LangChain/AutoGPT：帮你搭"AI应用"的骨架。

Spec 系列：帮你写好"规范文档"。

BMAD-METHOD：直接给你一整套"AI 敏捷团队 + 流程 + 工具"，让你专注决策和审核。

## 和Cursor、Claude Code怎么选？

很多人会问，BMad和Cursor、Claude Code是什么关系？

直接说结论：**BMad是"框架层"，Cursor和Claude Code是"工具层"。**

你可以这样理解：

*
  \*\*Cursor：\*\*给你一个会写代码的编辑器，适合快速原型、单兵作战
*
  \*\*Claude Code：\*\*给你一个自主的编码助手，适合复杂文件操作、长任务规划
*
  \*\*BMad：\*\*给你一套结构化开发流程，21个Agent带着你走完敏捷开发全流程

更重要的是，**BMad可以在Cursor或者Claude Code之上使用** 。

你用Claude Code写代码，用BMad管理流程，两者是互补关系。

从社区反馈来看，Claude Code的代码重做率比Cursor低30%，文件操作更快。

BMad v6版本的改进后，Token消耗节省了90%，减少了"瞎猜"带来的无效生成。

我自己的体验是：

*
  如果你只是想快速写个脚本、改个小功能，Cursor足够了
*
  如果你要做一个完整的模块，涉及前后端联调，Claude Code更省心
*
  如果你要从零做一个产品，或者重构一个大项目，BMad能帮你少走很多弯路

三者不是互斥，而是叠加。

## 🎯 适用场景

*
  个人开发者：想从 0 到 1 开发完整项目，并希望过程规范、文档齐全。
*
  小型团队/初创公司：人手不足，但希望项目有清晰的流程和文档，便于后期维护和交接。
*
  技术负责人：希望为团队引入一套标准的 AI 辅助开发流程，提升整体效率和质量。
*
  学习者：想系统学习现代软件工程（需求、架构、敏捷）的实践方法。


如果你最近正被"AI 写代码一时爽，项目大了火葬场"所困扰，不妨试试 BMAD-METHOD，或许它能给你带来全新的开发体验。

开源地址

    关注公众号 回复 20260220 获得


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F6wEpbjZhHQzicZ3q5yibyQZxz3wJAflIAvPNQbYLR5PmZzpAAb1Ogy1yRcUEHkiceQPTMCYTRXfu7UbJqEnz8dNlgMkibBJnkpJf06LJqDoiaVpU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

猜您喜欢：

[【开源】133K star，爆火AI智能体 Clawdbot 数小时内两度更名，开源、本地运行、主动帮你干活：重新定义数字员工](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503661&idx=1&sn=d143ce19feb68644021b97db1b807e1c&scene=21#wechat_redirect)

[【开源】93.6K Star！告别厂商锁定，完全开源、隐私优先的 AI 编程助手 ，支持 75+ 模型，用 AI 帮你读懂、重构、修复整个项目](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503651&idx=1&sn=82ffbcfac217ce7d75e59321807273b9&scene=21#wechat_redirect)

[【开源】28.4K star，一键解锁全网舆情！完全开源，不用写代码！这个AI工具让品牌/科研/公关的"读心术"更简单](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503197&idx=1&sn=f3006cec1541a240fd9181fbf7844c70&scene=21#wechat_redirect)

[【开源】3.1K Star ，一张照片 + 一段语音，打造会听会说的数字分身](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503431&idx=1&sn=5a1f4fef6f56e92e424d5e05f616db1b&scene=21#wechat_redirect)

[6元解锁640+优质开源项目！技术会员群上线，包括70+低开平台，50+AI平台](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503690&idx=1&sn=a8153eda2be8ed9169ec0306dcf5588e&scene=21#wechat_redirect)

添加微信进相关交流群，

备注"微服务"进群交流

备注"低开"进低开群交流

备注"AI"进AI大数据，数据治理群交流

备注"数字"进物联网和数字孪生群交流

备注"安全"进安全相关群交流

备注"自动"进自动化运维群交流

备注"试用"可以申请产品试用

备注"助手"进代码助手和插件交流群

备注"定制"可以定制项目，全源码交付

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FKmEUbWy7RO9icbfoYK0eiakZOquUgsBqvQf0q6NBoGO8YARSPwcHLGibnl35GU9jgE992B5NMDNcuhyqoSwreQ2cA%2F640%3Fwx_fmt%3Dother%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26randomid%3Dttwn2tyf%26tp%3Dwebp%23imgIndex%3D6)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI3MTQyNDc5MA==&mid=2247503771&idx=1&sn=c0ae78600263d4f0b2049739dc8d0737&chksm=ebbdd408df9180d72b70319d6170ec86625f69a9a9f5637bdb1024af1df00e2edc1091e71c88&mpshare=1&scene=1&srcid=0220E1O69p96Loco04judwl2&sharer_shareinfo=d335c9495cd17985442a5e60246081aa&sharer_shareinfo_first=d335c9495cd17985442a5e60246081aa)

