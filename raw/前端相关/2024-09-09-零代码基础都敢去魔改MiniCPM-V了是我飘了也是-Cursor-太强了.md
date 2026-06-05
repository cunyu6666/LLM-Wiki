---
id: "7232513529822054871"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkyMzU2ODEyMA==&mid=2247525103&idx=1&sn=e0608fe9d778f32f2d6109d43dbb979b&chksm=c056c3e5383894349dc5ba7ba46189d6859f734c88854af6920f8d2a4b28961dcbbdddc3816e&mpshare=1&scene=1&srcid=0909PkHnXQrN1KZxFJ7lQ1lK&sharer_shareinfo=362ecd78cfcddb604859b14d81e25032&sharer_shareinfo_first=362ecd78cfcddb604859b14d81e25032
author: "椰子 硅星GenAI"
collected: 2024-09-09
tags: []
---

# 零代码基础都敢去魔改MiniCPM-V了？是我飘了，也是 Cursor 太强了

# 零代码基础都敢去魔改MiniCPM-V了？是我飘了，也是 Cursor 太强了

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzkyMzU2ODEyMA==&mid=2247525103&idx=1&sn=e0608fe9d778f32f2d6109d43dbb979b&chksm=c056c3e5383894349dc5ba7ba46189d6859f734c88854af6920f8d2a4b28961dcbbdddc3816e&mpshare=1&scene=1&srcid=0909PkHnXQrN1KZxFJ7lQ1lK&sharer_shareinfo=362ecd78cfcddb604859b14d81e25032&sharer_shareinfo_first=362ecd78cfcddb604859b14d81e25032#rd)椰子 硅星GenAI


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2J298hXr635HWdkMsqjlpbYvRWGIaibHUrKKRHsX3EE9vs1ClIyOmqmqg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

不知道有多少人曾经有想过要学一学 Python。

至少我书架上还躺着一本落灰的《Phthon 编程从入门到实践》，B 站的收藏夹里也放着从来没打开过的时长长达近 25 小时的《Python全套课程》视频。

不是真的坚持不下去学习，而是他们教的确实不是我想要的。我也不是要用编程来谋生，就是想解决工作上一些具体到不能再具体的问题。但所有教程都在跟你说，你得先从 Hello World 学起。

Cursor 最近很火，在程序员圈子里讨论的很多，但对于大部分人来说，一款代码编辑器的更新和进展还是离大部分人的日常工作太远了。

如果这么想，那你大概率会错过一次进入新世界的机会。

我现在对于 Cursor 的痴迷程度，已经完全不亚于玩黑神话悟空了。


#01


### **一行代码没敲，先做一款游戏试试水**


在官网（https://www.cursor.com/）下载好程序后，默认是在一个 Cursor 的官方项目中。看不懂没关系，第一步我们先给汉化加上。

选中左上角的扩展，可以搜索**"简体"**，一般第一个就是我们要打的汉化包。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2J6TibrGknuXKPNatGYvUP1PvPUSr6zk1ckGhyRBtpy4jpfrPsZZqa94A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2Je5gQAXs15FI1m3yUicPe1kRymGqvYD9BXNicHrgkgXt1aqcIOVIsggsA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

给界面汉化后，我们还可以通过在设置中，加入一些规则（可以来这里找：https://cursor.directory/），来让回答更加高效和结构化。如果加入"ZH-CN ONLY"，可以让他以中文来回答。在我玩的过程中，中英文回答的能力差距不是特别明显。我这里使用的是一个 Python 相关的规则。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JcNK78pyu2aqO65fTk3Nhko9Wp76qd04aBG8klt1icUstNicdv1KFd6wA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JxBIk85m6TdFDH5OrtiaIdmHN1W4aN9SKjfUMoUUQwVH9OK9peyqm75g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

之后通过文件-关闭文件夹，能关掉这个官方的演示项目，我们可以新建文件夹来做自己的了。  

第一个项目，想先做一款贪吃蛇游戏，通过command+K的快捷键调出"Chat"区域，给他 Prompt："生成一款贪吃蛇游戏"。它会自动生成所有代码和文件，点击Accept All 所有生成效果即会生效。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JBrjgA9ZK663z0a1S4RQwUdQhMoRvhTB6G29R5crfnX9Aj9Vlkm7gHQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

它会自动生成文件，并告诉我们需要什么依赖环境和该怎么运行，最终的结果是这样：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2J3dsMQgUqwy0Re9WhmfGYobic2rLJ1iaRPVSIuXZz8hu1Ty67XeCA46zQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

**一个非常简陋的贪吃蛇游戏就生成了。** 还可以跟它说："以程序方式展现游戏，蛇头应该比身体要大。"于是我们第一款贪吃蛇游戏，就从网页变成了程序，而且也更像蛇了：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2J25uooicvGsf9Klw4nNaMibC5icOSg331MtfcGxH7gMDSiaRP0GwRohNDibw%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

用 Cursor 我能把我所有的想法，都实现，一行代码没敲过，比如我想让他变得更像蛇和苹果，背景也应该是绿色的草地：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JqSl1nhmiboqaIdlA91kTK9jDCoAfG2GDnoN1GmW3YLfEGL2ALvjjA3A%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

如果让它变得更有趣，可以加入关卡机制，随着关卡的升高，速度会越来越快，也会出现炸弹的干扰项，吃到炸弹也会 Game Over，在最后也会引入排行榜机制，整个游戏已经非常完整了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JmD3nrXJHCffw8XTNichars5zOFFdhKBW4IM5y6k0umN6XtfYcZegeicg%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

这里不管是苹果的样式还是炸弹的样式，没有用贴图，而是我是让它通过像素的方式画出来的。主打一个全程只动嘴不动手。


#02


### **开发一个真正有用的程序**


玩到这里，我已经被 Cursor 震撼到了，全程不需要切换任何网页去搜索答案，只要我说出口的要求，他都能解决。我要做的只是说说话，点一点，然后复制粘贴一些命令行就行了。  

我就想能不能做一些真正对我有用的产品出来。

一个非常小的需求：现在下载图片，尤其是在 Google 图片中，很多通过右键下载的都是 .webp 的格式，这种格式的图片微信公众号后台并不支持。那我能不能做一个 Chrome 插件来下载网页中的图片，同时遇到 .webp 的格式就自动转换成 .PNG 的格式。

于是第二个项目就成了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JI5ZuSqyHXoUY5WI1wGUYBjvnb2TFdnuWSYiaLszT9icDXdurLFc1s42Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

比如在 GooglePlay 页面中，想要下载这个 Logo 的图片，右键保存是 .webp 格式的。

但是用我做的这个插件，可以直接下载成.PNG 的格式。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JfRVibJ7yxdb4nPGmXjRYT7ugnby9TCCdUYWNdeAM3q2K74qOCBdviadw%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

当然，每一个项目和程序，都几乎不可能一次成功，中间少不了需要调试的过程。目前为止，我的万能解药就是将报错直接复制，他会给我解释报错的原因和解决方法。点击左上角的按钮可以快速呼出 Chat 和终端。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JRtOKGKqUVVQQcQAuU6dUMCUiasWZO3OvXCrZ0iadQ7tPkETJoLBNmyIg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


#03


### **再做一点更疯狂的事**


## 上面两个项目，总共耗时也就两三个小时，中间的版本功能迭代和调试环境比较费时。模型全程使用的是 Claude 3.5 sonnet，也是默认设置。

我感觉我已经掌握了 Python 的运作和基本语法，是时候挑战一点更高难度的东西了。

**那就魔改一个大模型吧。**

我们都知道现在大部分模型都是靠英伟达的 CUDA 来运用，非英伟达的显卡没办法做加速运算。

从 Github 上转了一圈开源模型，发现趋势月榜上，面壁的 MiniCPM-V 还在前列，这款端侧模型正好合适来测一测能不能原生运行在我这个 M1 Pro 芯片的 Macbook 上。

解压后用 Cursor 打开，试运行了一下自带的 Web-Demo，发现像是gradio、torch、transformers 等一堆环境都没安装。

环境整齐，点击运行很快就会提示系统中没有 CUDA。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JCfQAfIAAL24HTibxf0dfKXzye0HaLv5Hd7OsyZMNBYgZukkxpwGRMTg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Cursor 给出的解决方案是用修改代码的方式来通过 CPU 启动。

经过几次不难的调整之后，让人惊呼的是，我**成功运行了 Web-Demo**。这款模型能通过上传图片或者打开电脑的摄像头，来识别图像内容。

我正兴高采烈的上传一张图片来让他试试。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2Jrdk2YbdyYRExNtJxRYRwCiaCiarHEbIk2iabLs3MokOF0L0JrLibMicibmiaw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

结果打脸来的非常快，不出意外的报错了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JYXqPIXNKSusDsicbEF1Yja7ZJGsUdtXknXd6IhGvxHk5ibS10QcxbIKQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

报错显示了一堆我看不懂的问题，经过几次的调试，最后还是以失败告终，这个demo 是运行成功了，但没能完成一次对话。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JBYqUFVuicYQm2K6l6teGZOyMDRTfSb9mMB3Ke3tvmR1jBdoO03Hn1pA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


#04


### **顶级的 Python 老师**


## Cursor 的门槛很低，但不代表着没有门槛。首先得对编程软件多多少少有点概念，比如通过终端来调用一些命令。也需要能看懂从哪到哪是报错的地方。

人们学习 Python 最大的问题就是不知道怎么上手，前期的部署环境能劝退很多人，而且正向的反馈太慢。

Cursor 非常好的解决了这个问题，下载应用人人都会，用自然语言沟通也人人都会。

当我们只通过直白的语言就能达到预期效果的时候，这种持续的正向反馈会让人上瘾，就像玩游戏一样。

当我们成功的做成一两个项目，如果有心，自然会去了解更多的细节，这时候再拿起书来，用自己的项目对比着来看，就容易多了。

现在 Cursor 是有前两周的免费试用，能调用 GPT-4o、Claude-3-opus、Claude-3.5-sonnet 在内的 6 款模型，收费以后是 20 美元每月，这钱我肯定是掏定了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F5gR6KWHNb7Ro8ZpicSfQuyCGJD4qwyS2JJ2HYOrGz0xT7boTZH7lO5cks7P6XXje1JjzwFDwIZ6A5FQA9dZOFZg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzkyMzU2ODEyMA==&mid=2247525103&idx=1&sn=e0608fe9d778f32f2d6109d43dbb979b&chksm=c056c3e5383894349dc5ba7ba46189d6859f734c88854af6920f8d2a4b28961dcbbdddc3816e&mpshare=1&scene=1&srcid=0909PkHnXQrN1KZxFJ7lQ1lK&sharer_shareinfo=362ecd78cfcddb604859b14d81e25032&sharer_shareinfo_first=362ecd78cfcddb604859b14d81e25032#rd)

