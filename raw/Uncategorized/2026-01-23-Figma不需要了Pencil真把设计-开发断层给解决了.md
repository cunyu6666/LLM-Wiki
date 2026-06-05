---
id: "7414403505437279389"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247486216&idx=1&sn=acb72e6c3c959383d96285a00037aefd&chksm=c1b60590fcee7bba16410e012c852a6477d5ef9c50d43e3388587e0ec76e399c8e54aeaf854d&mpshare=1&scene=1&srcid=0123lujMjZYifNSShaa52OAC&sharer_shareinfo=047153e161fe2390f783bf7cba0c96b2&sharer_shareinfo_first=047153e161fe2390f783bf7cba0c96b2
author: "靈吾靈 AGI智码"
collected: 2026-01-23
tags: []
---

# Figma？不需要了！Pencil真把"设计-开发断层"给解决了

# Figma？不需要了！Pencil真把"设计-开发断层"给解决了

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247486216&idx=1&sn=acb72e6c3c959383d96285a00037aefd&chksm=c1b60590fcee7bba16410e012c852a6477d5ef9c50d43e3388587e0ec76e399c8e54aeaf854d&mpshare=1&scene=1&srcid=0123lujMjZYifNSShaa52OAC&sharer_shareinfo=047153e161fe2390f783bf7cba0c96b2&sharer_shareinfo_first=047153e161fe2390f783bf7cba0c96b2)靈吾靈 AGI智码


> 点击关注上方公众号，发现更多精彩内容等你来发现

大家好，这里是 AGI智码，专注于AI技术前沿分享，用最接地气的话讲最前沿的科技是我的专长，让每个人都能玩转AI是我的初心\~

## 前言

最近，Pencil（官网：www.pencil.dev），突然爆火。

很多人直接叫它「Claude Code 里的 Figma」或者「程序员专属的 AI 设计画布」。

听说是：专为开发者设计，旨在将设计过程无缝嵌入编码环境中。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg61BAicBzMzas9JoGZyCptAYYmazmhfPZLiaCib5ibIPSyK4uGEiaSFKTyTg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

讲真的，我一开始压根没当回事，不就是又多一个打着「AI」噱头的设计工具嘛。

Figma用着不香吗，各大 IDE 都针对它进行一些兼容，例如：Trae、Cursor, 点到哪里，直接让他生成前端代码也贼方便。还搞那么多花里胡哨的设计软件做什么。

带着疑问，我也认真调查一下它的来龙去脉，果然有点心动，大家可以跟着我文章一起来感受一下。

## Pencil.dev简介

> ❓为什么不直接使用Pencil，一定要跟着 .dev?
>
> 因为Pencil 这个单词太常见了，去谷歌一搜，一大堆无关的产品，很容易被误导。

Pencil.dev是一款代理驱动的MCP画布工具，专为开发者设计，旨在将设计过程无缝嵌入编码环境中。

该工具支持与多种IDE集成，如Cursor、VSCode、Trae等，只要是 VS Code fork 出来的 IDE 工具都无缝使用，它本质上就是 VS Code拓展生态。

用户无需离开代码编辑器即可进行像素级精确的设计工作。用最接地气的话给你讲清楚它是干嘛的：想象一下，你平时写代码用VSCode，突然在编辑器里多出一个超级丝滑的无限大画布（就像 Figma 那种随便拖、随便放大缩小的白板），但它比 Figma 更狠：

*
  **无限设计画布** ：提供高性能的WebGL渲染画布，支持无限扩展和像素级精确编辑。用户可以在IDE内直接设计用户界面，无需切换工具。
*
  **AI多人协作** ：AI充当"额外的手"，可并行生成屏幕或用户流程。通过预设动作或自定义提示，用户可以快速迭代设计。例如，使用Claude模型生成复杂界面，并实时调整。
*
  **从向量到代码** ：设计完成后，可一键转换为生产就绪的代码（如HTML、CSS、React），确保设计与实现的无缝衔接，而且像素级尽量对齐，不用再手动调半天。
*
  **开放文件格式** ：所有设计都存成 .pen 文件（其实就是开放的 JSON 格式），跟你的代码放同一个仓库。提交、拉分支、合并、回滚，全跟普通代码一样管理。团队协作再也不用设计扔 Figma、代码扔 GitHub 两头跑了。
*
  **Figma导入与设计套件** ：支持从Figma直接导入设计，保留向量、文本和样式。同时，提供基于组件的预构建设计套件，或集成用户自定义的设计系统。

总体而言，Pencil.dev「又」为未来编程提供了新范式：AI辅助下的无缝设计与编码。

它比较适合以下人群：

*
  不想为Figma AI付费的，又想自由自在通过 AI 做设计的**设计师** ！
*
  一个人既写前端又想快速出漂亮 UI 的**后端开发**
*
  不想在Figma界面和 IDE 工具来回转场，又想疯狂 vibe coding 的 前端开发

不想为

## Pencil.dev怎么用？

> 很多半吊子的自媒体博主会告诉你：下载Pencil以后，要使用官方的CC登陆，必须订阅正版的Claude Code套餐、只能使用Claude Code等等这些话。

我用真实经历告诉你：

1.
   使用Pencil，不需要订阅官方正版Claude Code套餐。
2.
   使用Pencil，并不需要强制使用Claude Code，任何一个AI编程工具都可以。无论是VS Code、Cursor、Google Antigravity、 Trae，全都可以。

因为我上个标题已经说了，Pencil是一个的MCP工具，现如今那个编辑器不支持 MCP 工具？
>
> ⚠️注意一点：
>
> 不要安装Pencil应用（桌面端），它提供了 **VS Code Extension** 版本，如果安装了两者，它两者会同时提供 MCP 服务，避免冲突，发生一些意外情况，尽量避免。

## 安装Pencil Extension

> 下面以 VS Code为例, 在测试阶段还发现一件事，trae 的 vscode 版本太低，没法把 cc 的插件放做侧边栏

### Step 1：打开插件商店搜索Pencil安装

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgf5nbrM9oY3qwgIqpiaTbibxlXyBowWm8EsdDriaEWKfAxhT3nkoTgwKFA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

安装成功后，会出现以下界面，有个✏️的图标。他就是Pencil了
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgjVFOo6PXYCN2bpiatHibUmTUYAR7iaD27560Yicm02OrFkuTgdxictKYPNw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

### Step 2：回到应用商城查看设置

你可以看到：当插件打开的时候，会自动为你所有的编程工具，安装Pencil MCP。

我们上文提到了，Pencil根本就支持全部的AI编程工具，原因就在于此。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg3dufWOwDsb1JjtFp7SNVU8kRC2VkYKWf7nFypFh8VS9wwFTuoBpnxQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg67MzvvWgiaA7YMrKECCZOgXz8Fnib2QvjoE8VMwTicMq5o2q5EEx4U5fg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

### Step 3： 正常登录邮箱并完成注册

回看第一操作它是需要你注册登录邮箱的，你正常使用国内的邮箱登录即可。

它会发邮箱邀请码给到你输入的邮箱
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgFQqYmuFhlveMmPDP7fiboxbIkNQLVnFK01NUQQAz533vzjsZZA8KCTw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

### Step 4： 打开Claude Code IDE Extension

这一步主要检查一下，你本地的 claude code 有没有正常配置了 MCP 工具。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg1QvInI4OLVqficTbuic9N7DODTopExcrxiaRN25hYiaorWeWhlvlzibLqJw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgtMoooS4ice9ZPG8VYDCP5lPvR92GibSPRI9dcZXp8arGAz9yr4RuxywQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

### Step 5： 开始使用 Pencil

1.
   点击左上角的New .pen file
2.
   会新建一个打开的空白画布
3.
   白色的画布跟vscode 的暗黑风格不太搭，我建议可以删除掉

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgEaqkUM12pXIN5ViaME7u4UeK9Fm7D3NOWyDX4nex2TlNhxEYqbWfmGw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

首先选用中间那个白色的矩形，删了它，舒服多了
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgr1FZwBpFcpN7OK7YAfL4wYic16co02YGyUkdETMVyuibcha16MYrxrew%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9)

### Step 6： 开始使用 cc 生成界面

先使用一些简单的提示语，试试成色
>
> 提示词：
>
> 使用 pencil mcp , 在当前活跃的画布上，设计一个运维相关的 app 登录页，要求有指纹登录，账号登录，一键登录，手机验证登录。类似飞书的 b端简洁风格，ios 风格
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgAEcwXB1aZWnvC1dBR8xBhwTFIm3salg4PwsaibZsHCkjE7laNVKqZPw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D10)

不得不说，生成速度是贼快，比 figma 真的快多了，但是效果不是很好，没有完成做出我期待的样子，可能是提示词太过于简单了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXglrtibOBz1n4quIq4iarcGBWJaZfp0BVspBLdwicJocEGd6UnMAC1b6Rvw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D11)

### Step 7： 结合ASCII 草图，看看生成效果。

> ❓ASCII 草图的来源：
>
> 可以看我这篇文章：《[两个 Skills，让前端一天完成产品+设计+开发](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485777&idx=1&sn=076da7b08e6f090137817f2cd1e45287&scene=21#wechat_redirect)》
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgn6LRwWxiaea4Izb7JHt9XRWwFq6feyrxVpjmzfa01WRutWzUmGcC4DQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D12)
>
> 提示词：
>
> 使用pencil MCP 工具,在当前活跃的画布上，重新调整界面，界面大概的风格类似 @ascii-ui-design/login/ios_login_20250112.txt
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg4x1dGQVCSicpcoh2hJiavwQr8Xosm5RFpmXIn9wJwRwUW013oCDSicYZw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D13)

还原度还是很高的，连ASCII 草图的位置偏移了，它没有帮我扶正，得要靠自己扶正一下拖拖拽拽移动，或者再次对话让ai 居中。

下面我让 CC 总结一下它的工作流程如下：

1.
   用户提供了ASCII设计稿文件路径
2.
   我读取了ASCII设计稿了解设计要求
3.
   我获取了当前编辑器状态，了解活跃的画布
4.
   我读取了当前画布的内容，了解现有布局结构
5.
   我获取了设计指南（landing-page）以确保遵循设计规范
6.
   我获取了当前页面的截图，了解现有界面
7.
   我分析了当前界面
8.
   我使用batch_design工具重新设计界面
9.
   遇到语法错误（注释问题），我修正了
10.
    遇到属性问题（textColor vs fill），我修正了
11.
    遇到布局问题（内容被裁剪），我修正了
12.
    最终获取截图并验证设计效果

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgqS4PNDljicf7FkFqs5Sg4XUVibDDM2YVYJYwfHQvs2Bmicx33RNzrkXkg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D14)

通过它的思考过程，我发现，它通过截图验证设计结果，是调用了 GML-4.6v 模型进行验证的，由此可见它其实更适合配合Claude 多模态的系列模型使用，效果会更加好。

**CC + GLM-4.7的组合没有发挥它全部实力** !!!!!

下面图片是相同的提示语，我用Claude 多模态的系列模型生成的，真的有点被惊艳到，太精准了！
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgcOtW5nuAo2FWlGmAJErDbyvDC3BzVuJeZnniaRnVe0D7LnfjMlcVOBA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D15)

看了思考过程的输出内容，我发现了，Pencil [get_screenshot]这个工具是根本就是对接 claude 的模型的（完美适配），不像 glm 还要重新调一次glm-4.6v mcp 工具，通过mcp 的截图工具，丢失了部分信息。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg8JHr14DVxFNrwicS2Jm2js31iaqy9oURx0g1w3p7DdcLVWhc7LlQW91A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D16)

### Step 8： 根据效果图生成可用前端代码

> 提示词：
>
> 生成的效果我十分满意，新开一个子代理智能体，生成登录界面的代码，代码路径在：src/login，记得更改 router，和 tab1.page增加点击入口。不要生成手机的状态栏
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgCWibnIJ03f0xSM0cz0Ofu8nqe9ib6KsWLbK1pEFHWKn5ibR951KW9bxJQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D17)

在过往的文章《[Playwright MCP/Skills/ Dev Browser：AI自动化测试的坑我全踩过](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485674&idx=1&sn=5c0cba3f343cd991f1203ad36ec01ef9&scene=21#wechat_redirect)》中我曾经讲过，MCP 工具由于架构的问题，天生就是会比较吃 token 的，就生成上面一个界面，就消耗了 60% 上下文容量.

为了生成的效果更加好，我们尽量不要早主智能体上再继续生成新的代码，所以上面的提示词我会让他新开一个子代理完成代码的生成任务。

子代理是隔离上下文的，这一点大家应该都能知道。

由于开了子代理，大家可以看到它只增加了8%的上下文容量
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgSW0iaFNkHMPe60icYNpanEh9eDHcwJrM9NhChfXree0ibCGQvypmeZLww%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D18)

生成代码真实效果如下：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgFeC73MHghWibmW3tbxiaROodxleicZ94yPxz4kDM5WsibM5UO5OCaDTARg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D19)

实在还原得太精准了！！！这就是惊喜啊，figma 都做不到这么精准的还原！！！

## Pencil的其他功能

Pencil的功能非常强大，上面只是我一些基础玩法，还有更多玩法需要你去探索，我简单介绍几个

### Figma的设计，可以直接导入Pencil。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgkicUV4oF6ibkSiatcKBb4Dhft3VTAsGts8RgEwUT5hVXgJ5EDtat9jpUw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D20)

### Pencil自带了很多设计规范、示例风格，可以直接用

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgrAjPsTU65TtBA6b4zqYYkU5BzCmWSfah4JUCick4baEYiciaKnudDOmPQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D21)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXg0OiaHk4SsgnJiaibSnRlRzcwUQNg4427ibEP4mpDbf9icTx46wHIfQpjmJg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D22)

### 可以整体设置设计的主题、设置变量

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgjiaawHwccmM1QQsem2KNh5LNQ6ZXkR21U8fgroNoB0vljqgwR8tUrJQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D23)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgkZ44MVV1p8VibkibOE6j64MygRyBY3C5YEYTDNH7wHibXWk4qxFvcCF8g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D24)

### 和Figma有一样的源码图层

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgSITQoB6Nib5IwLhmicPOXkosicmYZ27icaB0FjyCymg7eq7DM8XvFOjiaOg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D25)

### 可以打开一个预设组件版，然后使用这些预设组件进行设计

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgXC0XNypqu7u1eNrODH6ic77Z5ibcualaRSUkD4Knj4zhlNZCJXXMjQsw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D26)
>
> 但是有点遗憾的是，好像只能导入 figma 的源文件，不能导出 figma 的格式，还做不到互联互通的能力

## 总结

结合我们之前两个文章来看，总结一下：

*
  《[轻松拿捏产品设计（附实操 Skills）：SVG 线稿生成全攻略](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485996&idx=1&sn=50c6185912c53d8df39b2ead3dcca753&scene=21#wechat_redirect)》
*
  《[两个 Skills，让前端一天完成产品+设计+开发](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485777&idx=1&sn=076da7b08e6f090137817f2cd1e45287&scene=21#wechat_redirect)》

上面两个文章主要的工作流程是：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgwqeK4QVQEgDlGvZibcsTcepuHqcX0weCw3fbI75nuXlXicCFbLAPpnIQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D27)

因为我们如果没有UI 设计师，是产出不了源文件的，只能通过ASCII草图或者 svg 线图来保证效果，然后再使用有审美能力的 skills 来保证输出，但是这种输出还是有缺陷的，就是元素的定位问题，还有风格问题，都是抽卡式的，不够稳定。

现在又被我发现了Pencil这个工具，彻底补上了整个环节。

现在的工作流程已经变成这样：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgNClCia8wF1s2wZKpMjwickUvEPzgJwWXyeEedXycNzIbTELSTgJ3v1SQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D28)

## 写在最后

开头我说"没当回事"，现在必须承认：**Pencil.dev 确实是个狠角色** 。

它不是又一个打着 AI 噱头的设计工具，而是真正解决了"设计-开发"断层问题的**工程化方案** ：

1.
   **省钱** ：免费替代 Figma AI，一人干完产品+设计+开发
2.
   **省时** ：IDE 内完成设计，无需切换工具，设计即代码
3.
   **省心** ：.pen 文件版本控制，设计与代码同步迭代

**最重要的是** ：配合 Claude 多模态模型，从 ASCII 草图到像素级 UI，再到生产代码，整个流程丝滑得让人惊艳。

如果你是：

*
  想降本增效的**独立开发者**
*
  不想依赖设计师的**全栈工程师**
*
  追求极致效率的**一人公司**
*
  甚至你是一名 UI 设计师

那 Pencil.dev 绝对值得一试。

**毕竟，在 AI 时代，工具链的选择，决定了你的生产力上限。**
>
> **彩蛋提示** ：如果你已经在用我之前分享的 ascii-ui-designer 和 frontend-design 、 ui-ux-pro-maxSkills，现在加上 Pencil，你的开发效率会再上一个台阶。试试看，真香。

*** ** * ** ***

## 📚 推荐阅读

如果你对AI大模型和技术分析感兴趣，推荐阅读以下文章：

*
  《[Claude Code还能这样玩？手机+语音+云端=效率神器！](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485996&idx=1&sn=50c6185912c53d8df39b2ead3dcca753&scene=21#wechat_redirect)》
*
  《[AI ≠ 架构师：一次 Spec Kit 踩坑实录](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485728&idx=1&sn=22506d6c06f1edef8f863e78dd1d4fcb&scene=21#wechat_redirect)》
*
  《[AI编程的残酷真相：为什么说Spec Coding是2026年最大的趋势？](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247485513&idx=1&sn=666618d42b26533d1dc0ba56026d2220&scene=21#wechat_redirect)》

[![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F6Q6lA5HbrOy84rdNicRmEJJDibzf9eQCXgJJMDQxc2OnpDcmC1YeIYic1lnArYeOiahIzm3San245icg2tzWHuM3Jsg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D29)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkwODU5ODE2NQ==&action=getalbum&album_id=4289634444136153092#wechat_redirect)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwODU5ODE2NQ==&mid=2247486216&idx=1&sn=acb72e6c3c959383d96285a00037aefd&chksm=c1b60590fcee7bba16410e012c852a6477d5ef9c50d43e3388587e0ec76e399c8e54aeaf854d&mpshare=1&scene=1&srcid=0123lujMjZYifNSShaa52OAC&sharer_shareinfo=047153e161fe2390f783bf7cba0c96b2&sharer_shareinfo_first=047153e161fe2390f783bf7cba0c96b2)

