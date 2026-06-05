---
id: "7410407184401435116"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzYyMTMzMjUwNg==&mid=2247484405&idx=1&sn=91a0ce83308fa6a54eb41dac6a18c906&chksm=fea0e2b26b852d42855f4a3df0034dcbc2d6a36d92e9d9bf89d8aa4e88cb913211dfdcf8fbe2&mpshare=1&scene=1&srcid=0112pq4P21oHXer7NuKdm5kh&sharer_shareinfo=3f879418b37c1b1a4a987b29ab04d638&sharer_shareinfo_first=3f879418b37c1b1a4a987b29ab04d638
author: "第九比特 第九比特"
collected: 2026-01-12
tags: []
---

# Conductor：可能改变 AI 编程范式的 Mac 神器

# Conductor：可能改变 AI 编程范式的 Mac 神器

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYyMTMzMjUwNg==&mid=2247484405&idx=1&sn=91a0ce83308fa6a54eb41dac6a18c906&chksm=fea0e2b26b852d42855f4a3df0034dcbc2d6a36d92e9d9bf89d8aa4e88cb913211dfdcf8fbe2&mpshare=1&scene=1&srcid=0112pq4P21oHXer7NuKdm5kh&sharer_shareinfo=3f879418b37c1b1a4a987b29ab04d638&sharer_shareinfo_first=3f879418b37c1b1a4a987b29ab04d638)第九比特 第九比特


**Conductor：你的AI开发团队指挥官** ,第九比特 ,3分钟 进度条

三个 Bug 等着修，产品经理又来了个紧急需求。

切分支，改代码，提交。

再切分支，再改代码，再提交......

一个人，四条线，脑子快炸了。

如果有四个"自己"同时干活呢？

**Conductor，就是让你拥有一支 AI 编程团队的工具。**

## 从"副驾驶"到"项目经理"

我们已经习惯了 Copilot 的模式。

它像一个聪明的家教，坐在你旁边。

你写一行，它补一行。

很贴心，但本质上还是**一对一** 。

Conductor 彻底颠覆了这个逻辑。

它不是家教。

它是让你当上了**项目经理** 。

你不再是亲自写每一行代码的人。

你是分配任务、审查成果、拍板合并的人。

这种感觉，怎么说呢------

**爽。**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaErCOxDibY82ptt1fLsBh2CK5jN4Q7u9DlZiaZznt5gDMiaO3GhFMnBKlPIuom9rE6ZEgovKl3u6RKC6AUKTNBSEg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

## 核心黑科技：Git Worktrees

Conductor 能让多个 AI 并行工作，靠的不是魔法。

是 Git 的一个冷门功能：git worktrees。

简单说，它能让你同一个仓库，同时检出多个分支。

每个 AI Agent 在自己的"沙箱"里干活。

互不干扰。

不会打架。

主分支始终干干净净。

以前你得自己折腾这些。

现在，**Conductor 帮你搞定一切** 。

一位用户说得好："它把所有 git worktree 的脏活累活全包了！"

**但说实话，worktree 也有个小麻烦。**

每个新的工作区，理论上都要重新安装依赖。

npm install 跑一遍，pnpm install 跑一遍......

这很烦。

好消息是，**Conductor 用内置的 scripts 功能解决了这个问题** 。

你可以配置自动化脚本，让依赖安装、环境准备这些事自动完成。

AI Agent 一创建，环境就绪，立刻开工。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaErCOxDibY82ptt1fLsBh2CK5jN4Q7u9D8Sk97t6n2u5Itta3Mic3niabYriawovreOpPqt0U5rcJzxxJ9qCkpoyaw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

## 它到底怎么用？

流程简单到令人发指：

**第一步** ，把你的项目导入 Conductor。

**第二步** ，Command+N，新建一个任务。

用大白话描述："帮我修复登录页的 Bug。"

回车。

一个 AI Agent 就开始干活了。

**第三步** ，再来一个任务。

"给设置页面加个深色模式。"

又一个 Agent 上线。

**第四步** ，你喝咖啡。

侧边栏实时显示每个 Agent 的进度。

谁在工作，谁完成了，一目了然。

**第五步** ，Agent 交作业了。

Conductor 内置了 Diff Viewer.

你直接审查代码，不用切到别的工具。

满意？一键提 PR 合并。

不满意？给它反馈，让它重来。

整个流程，**闭环** 。

**说句实在话。**

这套流程，程序员其实很熟悉。

本质上就是：本地开多个分支，并行写代码，提 PR，合并。

没什么新鲜的。

**该遇到的问题，还是会遇到。**

比如合并冲突。

两个 Agent 改了同一个文件，照样要你手动解决。

但关键是------

**并行效率真的提升了。**

以前你得串行干活，现在可以并行。

以前你得自己管理多个分支，现在有可视化仪表盘。

以前你得记住每个分支干了啥，现在一目了然。

这就是 Conductor 的价值。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaErCOxDibY82ptt1fLsBh2CK5jN4Q7u9DPkJ6txFHAtBwWsBJn2UwTpibyzgrzyLfdXX1Pib0MGicZJS46omxsHCSA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

## 原生 Mac 应用的体验

说实话，网页工具用多了，再用原生应用会有一种被宠爱的感觉。

Conductor 就是这种感觉。

**丝滑。**

用户管它叫"beautiful Mac app"。

这不是客套话。

动画流畅，响应即时，UI 克制又精致。

有人甚至问："Conductor 是新的 Cursor 吗？"

这评价，懂的都懂。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaErCOxDibY82ptt1fLsBh2CK5jN4Q7u9DRvCNIempypl7Qw46lUiaF3OGgCtKe81bqI0JRYwq6iciaZibowiaKqSWljg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

## 它和 Cursor、Copilot 有什么不同？

**Copilot** ：一对一家教，实时补全代码。

**Cursor** ：AI 原生编辑器，想取代 VSCode。

**Conductor** ：不取代你的编辑器，只负责**编排和管理 AI 团队** 。

它们不是竞争关系。

Conductor 是**更上一层** 的工具。

你可以继续用 VSCode、用 Cursor。

但 Conductor 帮你把多个 AI 的产出**统一调度** 。

就像一个乐团：

Copilot 是首席小提琴手。

Cursor 是整个弦乐组。

而 Conductor，是那个站在最前面的**指挥家** 。

目前支持 Claude Code 和 Codex 这两个最强大的编码 CLI 工具。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaErCOxDibY82ptt1fLsBh2CK5jN4Q7u9Dw212FMUtjkIaCiasteZ8BDtEGfkOSP9U2YVffJzic5QOvEB7I0uIzic3g%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

## 真实用户怎么说？

Stripe 的工程师说：

"这就是未来。我上一次对开发工具有这么强烈的感觉，还是 Vercel 和 Supabase。"

Notion 的设计工程师说：

"我已经无法想象没有它的开发工作了。"

"疯狂"、"新的生产力解锁"、"游戏规则改变者"......

这些词反复出现。

我理解他们的激动。

因为 Conductor 解决的，是一个**真实的痛点** 。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaErCOxDibY82ptt1fLsBh2CK5jN4Q7u9DBQ9MHokG7ibs26qQjpDgQdkzRa6hGhsiaTXkgrHaY2esg8Gfc0kUHWsQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

## 它让我想到了什么

用 Conductor 的时候，我脑子里一直在想一个问题：

**开发者的角色，正在被重新定义。**

以前，程序员是"写代码的人"。

现在，可能要变成"管理 AI 写代码的人"。

你的核心竞争力，不再是敲键盘的速度。

而是**拆解任务的能力** 。

是**审查代码的眼光** 。

是**架构设计的判断** 。

Conductor 这类工具，正在把我们从"执行者"推向"决策者"。

这是好事吗？

我觉得是。

但它也意味着：

**躺平等着被 AI 取代，是最危险的策略。**

主动学习如何"指挥"AI，才是正道。

## 最后

Mark Weiser 说过一句话：

"最伟大的技术，是那些最终会变得隐形的技术。"

Conductor 让我看到了这种"隐形"的可能。

当你不再纠结于每一行代码的实现。

当 AI 团队在后台默默干活。

当你只需要关注"做什么"而不是"怎么做"。

那一刻，技术真的隐形了。

而你，终于可以专注于**真正重要的事** 。

**如果内容对你有启发，欢迎点赞、在看或转发支持。如果想不错过后续内容，记得设为星标 🌟 ～感谢你陪跑到最后，下回见。**

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYyMTMzMjUwNg==&mid=2247484405&idx=1&sn=91a0ce83308fa6a54eb41dac6a18c906&chksm=fea0e2b26b852d42855f4a3df0034dcbc2d6a36d92e9d9bf89d8aa4e88cb913211dfdcf8fbe2&mpshare=1&scene=1&srcid=0112pq4P21oHXer7NuKdm5kh&sharer_shareinfo=3f879418b37c1b1a4a987b29ab04d638&sharer_shareinfo_first=3f879418b37c1b1a4a987b29ab04d638)

