---
id: "7366058951315556619"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247505391&idx=1&sn=c9d397032c88e254bcc294e195db7ba4&chksm=c3fd9712e1d9ee48c5faa4bcee804c59cb109d5a7de2f91ed37d1528082a7bbf60977a4abce6&mpshare=1&scene=1&srcid=0912iE42zDBn9vfBMAtIEG6L&sharer_shareinfo=3399aa6662811aa5732c3fc257ac2aef&sharer_shareinfo_first=3399aa6662811aa5732c3fc257ac2aef
author: "金色传说大聪明 赛博禅心"
collected: 2025-09-12
tags: []
---

# Anthropic 实用发布：《如何为 Agent 构建工具》

# Anthropic 实用发布：《如何为 Agent 构建工具》

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247505391&idx=1&sn=c9d397032c88e254bcc294e195db7ba4&chksm=c3fd9712e1d9ee48c5faa4bcee804c59cb109d5a7de2f91ed37d1528082a7bbf60977a4abce6&mpshare=1&scene=1&srcid=0912iE42zDBn9vfBMAtIEG6L&sharer_shareinfo=3399aa6662811aa5732c3fc257ac2aef&sharer_shareinfo_first=3399aa6662811aa5732c3fc257ac2aef)金色传说大聪明 赛博禅心


⚙️


ANTHROPIC ENGINEERING

如何为 Agent 构建工具


Anthropic 刚刚发布了一篇很值得阅读的文章《如何为 Agent 构建工具》，包括：如何编写高质量的工具和评估，以及如何利用 Claude 来为自己优化工具，从而提升性能。

本文是对内容重点的介绍，更多详细信息，可阅读原文

https://www.anthropic.com/engineering/writing-tools-for-agents


什么是工具?

传统软件是确定性系统，而像 Agent 这样的系统是非确定性的。工具是一种新型软件，它反映了确定性系统与非确定性 Agent 之间的契约。我们编写工具时，需要为 Agent 而不是为其他开发者或系统来设计。我们的目标是通过工具，让 Agent 能够采用多种成功策略，扩大其解决各类任务的有效范围。


如何编写工具

本文描述了一个与 Agent 协作编写和改进工具的迭代流程：首先构建一个快速原型并进行本地测试，然后通过全面的评估来衡量后续的改动，并与 Agent 一起重复评估和改进的过程。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3wzibO5XhRGkz9OX4O2FWNIve2xV6vkGPNLRMhtAI8zxOsP1ib21UHZ2OA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%23imgIndex%3D0)


1构建原型

快速构建工具原型，亲身体验。使用 Claude Code 编写工具时，提供相关软件库、API 的文档会有帮助。将工具包装在本地 MCP 服务器或 DXT 中，以便在 Claude Code 或 Claude 桌面应用中连接和测试。


2运行评估

通过运行评估来衡量 Claude 使用工具的效果。评估任务应基于真实世界用例，并具有足够的复杂性。强大的评估任务可能需要多次（甚至数十次）工具调用。在评估中，我们建议收集准确率、运行时间、工具调用次数、Token 消耗和错误等指标。

我们内部 Slack 工具在留出测试集上的性能表现 ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3wqibFlvrCQ6lObT63RHDoHiayJVkJajhNerKicO8NOd1iasgRVQUBSgm2lA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%23imgIndex%3D1)

我们内部 Asana 工具在留出测试集上的性能表现 ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3wI2YNpO6QAx0JzJp5TUusdcTPJ1nyaNmkKjgs5AQZyFwiaRplib6XnKPA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)


3与 Agent 协作

Agent 是你发现问题和提供反馈的得力伙伴。你可以让 Agent 分析评估结果并为你改进工具。将评估 Agent 的对话记录粘贴到 Claude Code 中，Claude 擅长分析这些记录并一次性重构大量工具。


编写高效工具的原则


原则一: 选择合适的工具

更多的工具并不总是带来更好的结果。Agent 的"上下文"有限，应避免返回大量无关信息。应构建少量、有思想、针对特定高影响力工作流的工具。例如，实现一个 search_contacts 而不是 list_contacts 工具。工具可以整合功能，将多步操作合并为一次调用。


原则二: 为工具命名空间

当工具功能重叠或目的模糊时，Agent 可能会混淆。使用命名空间（例如 asana_search, jira_search）可以帮助在大量工具之间划定界限，帮助 Agent 在正确的时间选择正确的工具。


原则三: 从工具返回有意义的上下文

工具应只返回高信号信息，优先考虑上下文相关性而非灵活性。避免使用 UUID 等底层技术标识符，多使用自然语言名称。可以通过 response_format 枚举参数让 Agent 控制返回"简洁"还是"详细"的响应。


详细响应示例 (206 tokens):

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3w9BKzQHIHsFobrAkPD9rRcnrJ11ROTJichLkCCAWohsYnlFbKTAKKggQ%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%23imgIndex%3D3)


简洁响应示例 (72 tokens):

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3w3icgM7AN5QMOFJobia74HVx1Xl2a2TvMNYzz1YZzHZ1tegMtnOd1Erww%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)


原则四: 优化工具响应的 Token 效率

优化上下文的数量和质量同样重要。为可能消耗大量上下文的工具响应实现分页、过滤和截断等机制。如果截断响应或出现错误，应提供清晰、可操作的改进建议来引导 Agent。


截断响应并提供指导:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3w5ib8CFXAAicAoQ0zHibXmGtJibRicX0ibV97OfopC2frClbpzicuMUgHDXB6A%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%23imgIndex%3D5)


无帮助的错误 vs 有帮助的错误:

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3wGa2ZeQibun0kxKPicAUayZylzuToky5YUfiaHwF6tlO6jwowdicx1tk0Xw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpoBMKgXicict7zjVexdmzI3wPGm4rNX5G0tvDYY6ugrrzEvjZic8RCYUcI64DKBVkpLdcQ6VkQ0PQBw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)


原则五: 对工具描述进行提示工程

这是最有效的方法之一。编写工具描述时，要像向新同事解释一样，将隐含的背景信息明确化。避免模糊性，对预期输入和输出进行清晰描述和严格定义。例如，使用 user_id 而不是 user 作为参数名。对工具描述的微小改进都能带来显著的性能提升。


展望未来

为 Agent 构建有效的工具，需要我们将软件开发实践从确定性模式转向非确定性模式。有效的工具是有意图且清晰定义的，能明智地使用 Agent 上下文，并能直观地帮助 Agent 解决真实世界的任务。通过系统性、评估驱动的方法，我们可以确保随着 Agent 能力的增强，它们使用的工具也能同步发展。


[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247505391&idx=1&sn=c9d397032c88e254bcc294e195db7ba4&chksm=c3fd9712e1d9ee48c5faa4bcee804c59cb109d5a7de2f91ed37d1528082a7bbf60977a4abce6&mpshare=1&scene=1&srcid=0912iE42zDBn9vfBMAtIEG6L&sharer_shareinfo=3399aa6662811aa5732c3fc257ac2aef&sharer_shareinfo_first=3399aa6662811aa5732c3fc257ac2aef)

