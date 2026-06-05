---
id: "7232513769744632779"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjY2NTcyNg==&mid=2247497704&idx=1&sn=2dbce8103a24f3c2efa5b265ec3a07b4&chksm=cf354a0991a252a512e5341075c90a27add2ca827211ca218d59522c44a25bdd46f3159245a7&mpshare=1&scene=1&srcid=0909LnGfgnXEcYZlq7zjCd3n&sharer_shareinfo=f5c45aa09d2200acf282675f1a38ce21&sharer_shareinfo_first=f5c45aa09d2200acf282675f1a38ce21
author: "林三心不学挖掘机 前端之神"
collected: 2024-09-09
tags: []
---

# 以后用 ElementUI、Ant-Deisgn 的前端只会越来越少

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2NTcyNg==&mid=2247497704&idx=1) · 林三心不学挖掘机 前端之神

## 前言

大家好，我是林三心，用最通俗易懂的话讲最难的知识点是我的座右铭，基础是进阶的前提是我的初心\~

![](https://image.cubox.pro/cardImg/6d1vnm9tjcam0p89cr9azg8otv550me1mhseill00zqdswync4?imageMogr2/quality/90/ignore-error/1)

**前端之神**

一位前端小菜鸡，写过300多篇原创文章，全网有5w+个前端朋友，梦想是成为"前端之神"\~

392篇原创内容

公众号

，

## 老牌的组件库

相信`组件库`这东西大家都不陌生吧？`组件库`其实就是大佬们提前封装好的一些组件的集合体，我们在项目中可以直接拿来使用，无论是`Element-UI`还是`Ant-Design`，想使用无非就是分几步：

- **NPM安装**
- **页面引入**
- **使用组件**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7KOzeichrey5xpbs4SRImEp5DxmodBENkYJeQOZo0NraibJl1oPqXMWMA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

这也是我们现在大部分项目都在使用组件库的方式，但是说实话，大家真的**苦这种方式久矣**

## 苦组件库久矣？

为什么说**苦组件库久矣** 呢？当我们将`Element-UI、Ant-Design`这类组件库后，他们的代码会在`node_modules`中

但是大家都懂，组件库的功能或者样式不一定符合我们项目业务的要求，但是我们又不能直接修改`node_modules`中的源码，那咋办呢？
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7zkjczFYmPHg7KvVnHbIqb5KZOKHw2ZgvD5kLhhc9TdTj6s0XLE0BoQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

其实主要就是两点：

- **组件库的功能不符合业务需要咋办？**
- **组件库的样式不符合UI设计稿咋办？**

其实还是有办法的：

- 样式不满意，我们可以在页面中去使用样式覆盖
- 功能不满意，我们可以给组件库提`issue`，然后等待作者去增加；或者可以通过一些类似`pacth-package`这种工具去给`node_modules`中的源码打补丁，从而达到修改源码的效果

但是始终不是我想要的\~我以前就有一个想法\~

## 为啥不直接把源码复制到项目中？

我以前就有一个想法，我们使用一个组件库或者库的时候，为啥不直接把他们的源码复制到项目中呢？

就拿组件库来说吧，比如我项目只需要使用`Buttom、Input、Select`这些组件，那我可以直接从组件库中把这些组件的源码复制到项目来，那我既可以使用这些组件，我又可以随便改这些组件的源码样式，从而达到我想要的效果
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7354yricZdarZxjwy0VfogSK3TFiaQIRZQ9BfIjZ2h483oUgficnSiaVpwg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

可惜，理想很美好，现实很骨感\~因为这些组件库里的代码互相引用关系很复杂，所以你不可能很轻松把你想要的个别组件源码复制到项目来，所以基本没人这么做\~

既然自己复制不了，那有没有组件库能提供这样的命令呢，比如运行一个`ui add Button`就可以把组件库的`Button`组件源码复制到项目中呢？

还真有，**无头组件库（Headless Component Libraries）**横空出世，它是一种新兴的前端开发模式，其核心在于将组件的逻辑和样式分离。这种开发模式允许开发者在保持组件功能性的同时，完全控制组件的外观和风格，而不受特定UI框架的限制，优点有：

- **高度的灵活性和可定制性**
- **轻量级和性能优化**
- **提高开发效率**
- **高度的可组合性**

总结为一句话就是：**无头组件库为你提供组件的基本架子，你可以随心所欲修改架子，修改样式，修改逻辑，已达到你的要求**

## Shadcn-UI

一个神级的无头组件库，无头组件库中的第一把交椅！！！

它就是**Shadcn-UI** ！！！在去年的最受欢迎的 JavaScript 库中，**Shadcn-UI** 夺下第一名，稳压`Element-UI、Ant-Deisgn`等一众老牌组件库
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7icxX7EDT1SPeYJ2r47qFhdW2Z3N7qMoiab356YU7V3cyI4zbLc0nPErA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

截止目前，github 上已经有`67k stars`
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7ibHAJXBoooE8bj599FaP1H0k5SypXIU80ickh8KZM7dfzDOJX4ZHkrHw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**Shadcn-UI** 使用了`tailwindcss`来当做预设CSS，所以当你自定义样式时会非常方便

目前`React、Vue`版本都有
> React 版本文档：https://ui.shadcn.com
>
> Vue版本文档：https://www.shadcn-vue.com/
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F76jfLU3Pxhe60J2icdzIdj8Ssic1APxOmdfhNrNGhzW0hbrGibSSicjXvjg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

想要使用`Shadcn-UI`你得先初始化一些配置，比如`tailwindcss`
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7jQ6HmtpZH9O7fD9hmT2mYCpD63SsSEzdibiaXcicX0bbJ5UmdqGE6J55Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

接着你只需要使用命令

    npxshadcn-ui@latestinit

比如你想使用`Button`组件，你可以使用命令行

    npxshadcn-ui@latestaddbutton

这样它就会把`Button`这个组件放到你的项目中去
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F74wfycdbhW9OJO6E2eTAFxUV541bFrIibNy3o4QtydhOlrKvSVhichN1A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F7vOaSfopaEKichFHyKTdb2DCOaPhTH8kQSGARXyiapicPU5Lb59AvAB5Nw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

使用的话可以直接引入使用，你如果对他预设的 CSS 和 功能不满意，你也可以直接去到`button.tsx`中去修改
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTZL4BdZpLdhew1ibZqGPU8FA9lAr8h4F78NI6fVRr9YXOU4DibukshsgOgFcktf3AQhorkIkicvCmWTdib8FCeBGDg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

## 结语

我是林三心，感谢您的观看阅读，如果对你有帮助的话，请点点关注呗\~想加学习群的请关注我，回复"加群"

![](https://image.cubox.pro/cardImg/6d1vnm9tjcam0p89cr9azg8otv550me1mhseill00zqdswync4?imageMogr2/quality/90/ignore-error/1)

**前端之神**

一位前端小菜鸡，写过300多篇原创文章，全网有5w+个前端朋友，梦想是成为"前端之神"\~

392篇原创内容

公众号

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2NTcyNg==&mid=2247497704&idx=1)
