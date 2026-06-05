---
id: "7409690738046272620"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484944&idx=1&sn=15d64102c5c70b1929834c92f75de7ac&chksm=ebb3853030e4ffa180f025528cc2cd78cc5b4501a6480311b3519289536bdf04647ff2bf16ce&mpshare=1&scene=1&srcid=0110Yb9kUQawTHPKko79eXcg&sharer_shareinfo=c00b4d4b91c66426e2582cc26971d628&sharer_shareinfo_first=c00b4d4b91c66426e2582cc26971d628
author: "范凌的泛谈 范凌的泛谈"
collected: 2026-01-10
tags: []
---

# 别开发智能体，开发Skills！介绍 Skill0.IO

# 别开发智能体，开发Skills！介绍 Skill0.IO

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484944&idx=1&sn=15d64102c5c70b1929834c92f75de7ac&chksm=ebb3853030e4ffa180f025528cc2cd78cc5b4501a6480311b3519289536bdf04647ff2bf16ce&mpshare=1&scene=1&srcid=0110Yb9kUQawTHPKko79eXcg&sharer_shareinfo=c00b4d4b91c66426e2582cc26971d628&sharer_shareinfo_first=c00b4d4b91c66426e2582cc26971d628)范凌的泛谈 范凌的泛谈

有两位 **Anthropic** 的研究员的分享**《别开发智能体，而是开发技能（Don't build agents, build skills instead）》** 讲述了AI开发的新阶段。他们提出的核心观点是：在构建智能体的时候，其实并不需要反复重构一个"看起来像通用智能体"的复杂结构。真正重要的是基于已有的上下文和模型推理能力，**不断为智能体构建、叠加可复用的 Skills（Agent Skills）。**   

这对我们很有启发，我们也在做一件类似的事情------[如何把](https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484824&idx=1&sn=4f39536c2083d7b4ac2d89a59789c975&scene=21#wechat_redirect)**[Atypica](https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484824&idx=1&sn=4f39536c2083d7b4ac2d89a59789c975&scene=21#wechat_redirect)** [可以从用户研究拓展为更通用的企业级智能体结构（我们称它为](https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484824&idx=1&sn=4f39536c2083d7b4ac2d89a59789c975&scene=21#wechat_redirect)**[GEA = Generative Enterprise Agent）。](https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484824&idx=1&sn=4f39536c2083d7b4ac2d89a59789c975&scene=21#wechat_redirect)**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F9oWYoLCZTYWCibtbmvEeC89BmHRuLO65ibicOmRzmmhputyZOZXicdatBm7cRxG3fHcWc4vzKqD4cl3jZVdgNAENjA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

在多智能体系统里，我们慢慢形成了一个越来越清晰的判断：

**Lead Agent，更像「大脑」；**

**Sub Agent，更像「手」。**   

大脑负责理解问题、做判断、规划路径；手负责执行，把事情真正完成。但关键在于------**"手"本身是通用的。** 真正让手变得强大的，是它能不能调用合适的 **skills** 。

Agent 也一样。当它能够根据场景，自由调用不同的 skills，它才会从一个"会说话的模型"，变成一个**真正"会做事"的伙伴** 。

继续往下走，我们遇到了一个更具体、也更工程化的问题：

**如何让 AI 在"需要的时候"，加载"需要的能力"？**   

而不是把所有东西一股脑塞进 context？

我们逐渐收敛出了一个核心思路：

**Universal Agent + Skills Library**

不是构建越来越多的专用 agent，而是：

* 一个通用的执行 agent

* 一组可以被动态加载的 skills

* 由推理层来决定：

* 什么时候加载、加载哪些

也就是说------不是让 agent "记住一切"，而是让它**学会判断：此刻需要什么能力。** 当 skills 只有几个的时候，这不是问题。但当它们从十几个，变成几十个、上百个。你一定会遇到新的挑战：

* skills 如何被管理？

* 如何被发现？

* 如何被复用？

* 如何被共享？

你需要一个地方，来承载这些能力单元。基于这些真实的实践和困惑，我们把在 **Atypica** 里反复打磨的一部分 skills，先开放了出来：

👉 **skill0.io**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F9oWYoLCZTYWCibtbmvEeC89BmHRuLO65ibL0VtjaoAxzbje1jdM34fAj9Yrib8w4KvLQtiaicYhjNElfl3YeERcj5nw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F9oWYoLCZTYWCibtbmvEeC89BmHRuLO65iblFBJxs9519uWyW3zunj2ichApY4CViazpv2ZjGQQYLhVCUicAMXlTjSOA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

十年前创业的时候，我很喜欢一家公司，叫 **Skillshare** 。他们当时有一个让我印象很深的理念："不论是谁，每个人都有一些技能，可以教给别人；也可以从别人那里学到新的技能。" 我一直觉得这是一个平权、乐观、自驱的世界观。  

而到了今天，在 AI 时代，**Skillshare 这个概念有了新的含义。** 它不再只是"人和人之间的技能分享"，而是变成了------**智能体之间的 skill 分享。** 你可以把一个人的经验、方法论、判断路径，封装成一个 skill，让不同的 agent，在不同场景下直接复用。

虽然这个尝试最早来自**消费者研究场景** ，但我们相信------**这套以判断为核心、以Agent Skills 为能力单元的架构，理论上适用于任何复杂的知识型工作。**   

欢迎交流、指正。

**这件事，才刚刚开始。**

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1ODM1MjA3NQ==&mid=2247484944&idx=1&sn=15d64102c5c70b1929834c92f75de7ac&chksm=ebb3853030e4ffa180f025528cc2cd78cc5b4501a6480311b3519289536bdf04647ff2bf16ce&mpshare=1&scene=1&srcid=0110Yb9kUQawTHPKko79eXcg&sharer_shareinfo=c00b4d4b91c66426e2582cc26971d628&sharer_shareinfo_first=c00b4d4b91c66426e2582cc26971d628)

