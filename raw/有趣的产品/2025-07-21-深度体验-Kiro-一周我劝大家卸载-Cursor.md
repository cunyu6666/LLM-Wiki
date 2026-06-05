---
id: "7346920223125014947"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MjM5OTkxODM2NA==&mid=2448760754&idx=1&sn=f07a7c7be0a634ed062bf1f312f5254b&chksm=b2436ccf2be5c1d0b6c6e3aea738f07950a8c42463e763fb10e7b23f5429472ce9ee42fad45d&mpshare=1&scene=1&srcid=07219EK6DVC4X0kfWDzcxMdW&sharer_shareinfo=74c4a7d8545d106f11312174f2a44135&sharer_shareinfo_first=74c4a7d8545d106f11312174f2a44135
author: "非遗程序员米粒 全栈"
collected: 2025-07-21
tags: []
---

# 深度体验 Kiro 一周，我劝大家卸载 Cursor

# 深度体验 Kiro 一周，我劝大家卸载 Cursor

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5OTkxODM2NA==&mid=2448760754&idx=1&sn=f07a7c7be0a634ed062bf1f312f5254b&chksm=b2436ccf2be5c1d0b6c6e3aea738f07950a8c42463e763fb10e7b23f5429472ce9ee42fad45d&mpshare=1&scene=1&srcid=07219EK6DVC4X0kfWDzcxMdW&sharer_shareinfo=74c4a7d8545d106f11312174f2a44135&sharer_shareinfo_first=74c4a7d8545d106f11312174f2a44135)非遗程序员米粒 全栈


## 简介

Kiro（音标：英式 \[ˈkaɪroʊ\] 美式 \[ˈkɪərəʊ\]），在 7.14 公布预览版后，由于开发者过于热情，官网已经关闭了下载入口，需要加入候补名单，但其实并没有硬性限制，只要有安装包就能够注册体验。
> 如需获取最新安装包，可向本公众号发送关键词：kiro

预览版期间可以免费体验 Kiro 的全部功能，目前提供 2 款前沿的编程领域模型： Claude Sonnet 4.0 与 Claude Sonnet 3.7。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzZorGq9YoJ4fia3FJZTBaC9OD5LzYOMdRSubia4BiaicKRV75USWtMYrkibQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dio2qvwge)

Kiro 团队貌似怕大家误会，更是把早先预告的订阅价格下架，并且正在重新评估，最终订阅价格应该有所调整，希望官方继续聆听社区意见，做一个双赢的选择。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzlj2tQSwyvUFsgiaAkpxtB1iaRvamicR2cqlcBA3ZzXmfmhxXgHPQicvtBw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D08312tiw)

## 功能

Kiro 与 Windsurf、Trae、通义灵码这些同样基于 VSCode 二开的 AI IDE 不同，并没有完全复刻 Cursor 的功能，而是加入了自己针对 AI 编程的理解，接下来我们将一一讨论。

### Spec 模式

Kiro 同样支持行内会话与侧边会话，侧边会话中的 Vibe 模式与 Cursor Agent 无明显区别，而 Spec 模式比较有特色。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzln8IW2D41bdP2s6h5uyib9SlbAP5Tkkic66eu13AK9t1yKFJgZAWiaCfw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dfhxxqt0u)

有氛围编程经验的开发者应该都深有体会，模型与系统提示词已经强大到我们不太需要关心做提示词优化，但即使这样，AI 的每次回答都很像在抽卡，所以又演化出编写项目级 rules 来约束，这难道不是另一种"提示词"陷阱？

Kiro 摸索出了规范驱动（spec-driven）用来解决当前 AI 编码带来的问题，模拟出原型到生产的开发过程。在 Spec 模式下都会按顺序生成 3 个文档，requirements.d-\>design.md-\>tasks.md，这分别对应软件开发中的三个阶段：需求、设计、开发。

当你进行提问后，Kiro 会先生成一份需求文档，你也可以进行修改补充，确定后再让 Kiro 进入下一个阶段，最终会生成详细的任务列表。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzaxNagVribHnCOibxUcgOibPKicZyYU2CKYQicI0HemJBQB6AYCuFfhSpcMw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D8lx7343u)

我们可以单独执行某个任务，查看任务状态以及任务执行情况等。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGztYbmiciaqBItamLib8vR0uGur8spibT3jyhbau0xkAEv7tYJnSUlDoDQUA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D866vpjny)

通过面板上的任务列表按钮，还能查看当前正在执行的任务，以及队列中的任务。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzWhXH1ib4ia6beFBibUI2DgvffglicmJ7BUAyib4QicQia5Duxt8BxtSyibDZsA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Di0h6lpyg)

这么多任务，你一定想问上下文是否会超出，模型会不会限制等。我在运行这 16 个任务中间，大概用了 2+ 个小时，中间遇到一次模型高锋期，手动切成 3.7 又能继续用，同时勾选了 Autopilot 自动运行也没遇到调用次数限制；Kiro 每个任务都是新建会话去执行可能就是考虑到上下文的问题。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzJ9XROeo5kFjTccHEFLVxK2CJQlt0prxlXRzLdMgvsxUFDVdHbibLxqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dbzkv1eh3)

### Agent Hooks

Agent Hooks 这个功能我觉得非常实用，在 Cursor 1.0.0+ 后回答完问题总要来个总结，帮你更新 README.md 等，这在 Kiro 中就可以设置成一个钩子，你需要的仅仅是点击新建钩子，然后使用自然语言描述，最终 Kiro 会帮你生成好钩子文件（.kiro/hooks/）。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzngFf2bgicK84TicHia3H04EZzbKJWtqhxCRrx3zjGQibOAKuGJ6icXmDFcA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3D6o3kyems)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGz5ibmPLf11NqBkFpRNoxHUhADSk04YiaY3TnlibiaPEwyicOceSzT8BKRIvA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dfvpowcg3)

目前钩子监听 IDE 的三种事件：

*
  文件创建
*
  文件保存
*
  文件删除

### Steering

Steering(音标：英式 \[ˈstɪərɪŋ\] 美式 \[ˈstɪrɪŋ\])这个单词不好直译，等官方中文吧。但与 Cursor 类比就是 .cursorrules，即项目级规则，但不是 Memories，因为 Steering 目前也是主动添加的项目持久知识，存储在 .kiro/steering/ 目录下，初始新建时会有默认的三个文件，也可以自自定义添加其它文件。

*
  产品概述（ product.md ）- 定义你的产品目的、目标用户、关键功能和业务目标。这有助于 Kiro 理解技术决策背后的"为什么"，并建议与你的产品目标一致的解决方案。
*
  项目结构 ( structure.md ) - 概述文件组织、命名规范、导入模式及架构决策。这确保生成的代码能无缝集成到你的现有代码库中。
*
  技术栈 ( tech.md ) - 记录你选择的框架、库、开发工具和技术限制。当 Kiro 提出实现建议时，它会优先考虑你已建立的技术栈而非替代方案。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzl2lzyAgfKk6nibPd24k2vLvXo9uFTtBluBrpARxtezcsN8JhJ7TXIFw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dcd6tjwad)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzgFdEKk8NlnHJKF0YPf9DiapAficCxy6JbVibatmPmjE70icdrk7OuDtydQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dd3kr7n64)

这些 .md 文件支持 YAML 语法用于配置什么时机加载进上下文。

    ---
    inclusion: always
    ---

    ---
    inclusion: manual
    ---

    ---
    inclusion: fileMatch
    fileMatchPattern: "components/**/*.tsx"
    ---

Kiro 还列举了不错的几种文件策略：

*
  API 标准（ api-standards.md ）- 定义 REST 规范、错误响应格式、认证流程和版本控制策略。包括端点命名模式、HTTP 状态码使用以及请求/响应示例。
*
  测试方法（ testing-standards.md ）- 建立单元测试模式、集成测试策略、模拟方法以及覆盖率预期。记录首选的测试库、断言风格和测试文件组织方式。
*
  代码风格 ( code-conventions.md ) - 指定命名规范、文件组织、导入顺序和架构决策。包括首选代码结构、组件模式和应避免的反模式示例。
*
  安全指南（ security-policies.md ）- 文档认证要求、数据验证规则、输入清理标准以及漏洞预防措施。包含针对您应用程序的特定安全编码实践。
*
  部署流程（ deployment-workflow.md ）- 概述构建流程、环境配置、部署步骤和回滚策略。包含 CI/CD 管道细节和环境特定要求。

之前在使用 .cursorrules 也是类似拆分成几个文件，方便在不同项目间复制使用，但维度或者说策略不一样，Kiro 直接约定基础文件，并且能够通过自然语言修改与自动生成，无疑降低了使用门槛。

*
  common.mdc：所有项目能通用的，相当于全局规则，但能跟着项目放 git，比如 node/python 包管理约定等
*
  project.mdc：项目结构、技术栈等
*
  ...

## 其它

Kiro 默认是关闭 Tab 模式的，可以到设置中开启。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzzAuwic9q0I1qzBzOib9RGdmxqDUaOB1y3z8z5pjuMSlmezYZI6ibTt1ZA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dddimpqgy)

# 指令基本把 Cursor 的 @ 指令都带过来了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlotkgsB9Y3HxrJ5ZyfYAp3pYCW7QYvGzOaFKicZbc2y977aQYjR5CB4v0Quia5vGd6yyvs98NX9VL5L6PYHAgjhw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26randomid%3Dgi7h9ho9)

## 总结

Kiro 不管是 Spec、Agent Hooks 还是 Steering 都是使用自然语言，同时提供了一套经过验证的标准，不仅让代码生成更加可靠，同时也降低了使用门槛，对"0 基础"的人非常友好。如果一定要找个缺点，那就是同样一句需求，Kiro 真的太多事...

以上便是我使用一周的体验，Kiro 确实有不小的创新，这才是后起 AI IDE 应该学习的点，而不是单纯靠支持最新 xxx 模型来博眼球。说到这，曾经 T0 级的 Cursor 缺少竞争花样作死，这一个多月来除了调整收费规则就是限制模型，现在作业来了，抄吗？


![](https://image.cubox.pro/cardImg/2zq9e49a3me9qyd3brril7dtdy63qp8d83e3ckcx74bmwrjs3n?imageMogr2/quality/90/ignore-error/1)

**全栈**

分享国内外的前端技术与资讯

11篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5OTkxODM2NA==&mid=2448760754&idx=1&sn=f07a7c7be0a634ed062bf1f312f5254b&chksm=b2436ccf2be5c1d0b6c6e3aea738f07950a8c42463e763fb10e7b23f5429472ce9ee42fad45d&mpshare=1&scene=1&srcid=07219EK6DVC4X0kfWDzcxMdW&sharer_shareinfo=74c4a7d8545d106f11312174f2a44135&sharer_shareinfo_first=74c4a7d8545d106f11312174f2a44135)

