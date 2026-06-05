---
id: "7402623169711834245"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247504527&idx=1&sn=3ab2139a944707e4de260372430a2eac&chksm=c1340a4b83b11b493cb937e70cc3e53124df10e7366f53a31296782a9db92dad17c46c4a6052&mpshare=1&scene=1&srcid=1222EgQpLT4kkEb7aEdp8wU2&sharer_shareinfo=85bb5d13c9103d074ec3f992cdbf51a7&sharer_shareinfo_first=85bb5d13c9103d074ec3f992cdbf51a7
author: "痕小子 开源星探"
collected: 2025-12-22
tags: []
---

# 3.5K Star！GitHub 高赞 Vibe Coding 神级指南！

# 3.5K Star！GitHub 高赞 Vibe Coding 神级指南！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247504527&idx=1&sn=3ab2139a944707e4de260372430a2eac&chksm=c1340a4b83b11b493cb937e70cc3e53124df10e7366f53a31296782a9db92dad17c46c4a6052&mpshare=1&scene=1&srcid=1222EgQpLT4kkEb7aEdp8wU2&sharer_shareinfo=85bb5d13c9103d074ec3f992cdbf51a7&sharer_shareinfo_first=85bb5d13c9103d074ec3f992cdbf51a7)痕小子 开源星探


这两年，Cursor、Windsurf、Copilot、Claude Code 把「写代码」的门槛拉得越来越低。

但很多人很快就会遇到同一个问题：
> 项目一大，AI 就开始乱写。

*
  • 文件结构不统一
*
  • 新代码和旧逻辑打架
*
  • 重复实现、风格混乱

最近在 GitHub 上看到了一份 Vibe Coding 神级指南：**vibe-coding-cn** 。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeIAE556qI0Yy2IicdwLONnXFNpEvjhvBmgicbnewrOxWkic36Tj6vwzRJCf7lEdibqCgjnEhfuO2mbaTg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

它不仅仅是一些提示词的堆砌，而是一套完整的 AI 辅助编程方法论。它的核心理念只有四个字："规划先行"。

它并不是教你怎么写 Prompt，而是在系统性回答一个问题：如何让 AI 参与编程，但不把项目控制权交出去？

#### 项目简介

Vibe Coding 作为当下最为火热的 AI 编程术语，直译过来是"氛围编码"，听起来有点玄学，但其实是使用自然语言需求来驱动AI编程。

它是一个与 AI 结对编程的终极工作流程，旨在帮助开发者丝滑地将想法变为现实。

而该开源指南详细介绍了从项目构思、技术选型、实施规划到具体开发、调试和扩展的全过程，强调以规划驱动和模块化为核心，避免让 AI 失控导致项目混乱。

它的核心逻辑是：不要直接让 AI 写代码，而是先让 AI 写文档。

在传统的 AI 编程中，我们的操作路径通常是：
> 提需求 -\> AI 生成代码 -\> 报错 -\> 把报错丢给 AI -\> AI 瞎改

而在 Vibe Coding 的体系下，路径变成了：
> 提需求 -\> 生成设计文档 -\> 确认技术栈 -\> 生成实施计划 -\> AI 按计划写代码

通过一系列标准化的 Markdown 文件，我们将项目的"上下文"固化下来，让 AI 无论进行到哪一步，都有据可查，不会"胡言乱语"。

#### 快速开始（基础）

第 1 步：复制下面的提示词，粘贴到 Claude 或 GPT 中。

    你是一个专业的 AI 编程助手。我想用 Vibe Coding 的方式开发一个项目。

    请先问我：
    1. 你想做什么项目？（一句话描述）
    2. 你熟悉什么编程语言？（不熟悉也没关系）
    3. 你的操作系统是什么？

    然后帮我：
    1. 推荐最简单的技术栈
    2. 生成项目结构
    3. 一步步指导我完成开发

    要求：每完成一步问我是否成功，再继续下一步。

第 2 步：跟着 AI 的指导，把想法变成现实

就这么简单！

(更多进阶内容可打开项目主页阅览）

#### 核心思想

该指南提出了一个核心思想：**元方法论** ，核心是构建一个能够自我优化的 AI 系统。

其递归本质可分解为以下步骤：

① 定义核心角色：

*
  • **α-提示词 (生成器)** : 一个"母体"提示词，其唯一职责是生成其他提示词或技能。
*
  • **Ω-提示词 (优化器)** : 另一个"母体"提示词，其唯一职责是优化其他提示词或技能。

② 描述递归的生命周期：

*
  • **创生 (Bootstrap)** :使用 AI 生成 α-提示词 和 Ω-提示词 的初始版本 (v1)。
*
  • **自省与进化 (Self-Correction \& Evolution)** :使用 Ω-提示词 (v1) 优化 α-提示词 (v1)，从而得到一个更强大的 α-提示词 (v2)。
*
  • **创造 (Generation)** :：使用进化后的 α-提示词 (v2) 生成所有需要的目标提示词和技能。
*
  • **循环与飞跃 (Recursive Loop)** :将新生成的、更强大的产物（甚至包括新版本的 Ω-提示词）反馈给系统，再次用于优化 α-提示词，从而启动持续进化。

③ 终极目标：

通过此持续的递归优化循环，系统在每次迭代中实现自我超越，无限逼近预设的预期状态。

同时还给出了一套方法论精要，又将其分为：道·法·术。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeIAE556qI0Yy2IicdwLONnXFVwHuzNxicDGia1p7MApibrqtT8wDdP04yLAHymzanquG8CLDRobKiaiaUYQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeIAE556qI0Yy2IicdwLONnXFiahTZd8P4icfKfxxudIT0EDGkKiaDdGqgnkgib2YemWbG6iagJQmzf1mRtg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeIAE556qI0Yy2IicdwLONnXF4MSgLmSiapricnoiaEeH3yspdWR2aVFumVTefUUuianaibquic5lrBkWJbDw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

#### 工具资源

同时整理了终端\&IDE、AI模型\&服务、开发辅助工具、资源模板、项目内部文档、外部交流资源等众多工具资源在内。

*
  • 几百个覆盖不同场景的提示词
*
  • 元提示词生成器（Prompt for Prompt）
*
  • Skills 技能库
*
  • ......


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeIAE556qI0Yy2IicdwLONnXFml4mickokk8mGBFwoW0VYXwnibg8Vr73UBxyZt1WkSFSDlwOFrpdpWwg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

你可以把它理解为：
> **一套面向 AI 编程的"操作手册 + 工具箱"。**

当做大量可复用的 Prompt 资产。

#### 项目目录结构


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FNjA8gwicXyeIAE556qI0Yy2IicdwLONnXF4icHG4hNiaevibIU2F9gd6Uz7oVGQzFnsUwiaE1sNUpjAZFLjOjKzgD8Kg%2F640%3Fwx_fmt%3Djpeg%23imgIndex%3D5)

#### 写在最后

未来，用 AI 写代码可能会变成一件"默认动作"。

真正拉开差距的，不是你用不用 AI，而是：
> **你有没有一套方法，能让 AI 在复杂项目中保持理性和一致性。**

如果你已经开始做真正的项目，而不是 Demo，那 **Vibe Coding** 这套实践，非常值得你认真看一遍。

详细使用方式，包括完整的设置流程及技巧都在项目中说明了。

GitHub：https://github.com/tukuaiai/vibe-coding-cn


![](https://image.cubox.pro/cardImg/4b5uzdwlzim32fi21mqn4gb4p09jfaphbqk26wxxock1xs0pv7?imageMogr2/quality/90/ignore-error/1)

**开源星探**

专注于分享GitHub上优质、有趣、实用的开源项目、工具及学习资源，为互联网行业爱好者提供优质的科技技术资讯。

740篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNjA8gwicXyeKqAjyn8A3ob9xT4DDY8DB3JCvIaM6JKWXFsgCxznXicJhpRYJ5MIPb9xvgGA4WYhPagIKorlScib0Q%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D6)

如果本文对您有帮助，也请帮忙点个 赞👍 + 在看 哈！❤️


**在看你就赞赞我！**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNjA8gwicXyeLZdEkueqhds4y07sImrPvibkDIsnVCibl5ibS6jSiccRh6RtH8ZqBPBWSib0kn7Ep6mP5YPJCJkraJ3kw%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D7)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247504527&idx=1&sn=3ab2139a944707e4de260372430a2eac&chksm=c1340a4b83b11b493cb937e70cc3e53124df10e7366f53a31296782a9db92dad17c46c4a6052&mpshare=1&scene=1&srcid=1222EgQpLT4kkEb7aEdp8wU2&sharer_shareinfo=85bb5d13c9103d074ec3f992cdbf51a7&sharer_shareinfo_first=85bb5d13c9103d074ec3f992cdbf51a7)

