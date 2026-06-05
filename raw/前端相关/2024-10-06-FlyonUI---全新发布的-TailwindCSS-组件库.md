---
id: "7242562994910004440"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkxNjUxMDg4Ng==&mid=2247496418&idx=1&sn=916c2aa32e8feb1115ec0f7a91598371&chksm=c0689a95170fc4fb63abedeb26f510bcbc589a61fe2ea6c68191d566134a375667e6e207baf6&mpshare=1&scene=1&srcid=1006YTpMUYFi9r5tOrtUY4IK&sharer_shareinfo=a846a48eb4220250672e1e7b057ec198&sharer_shareinfo_first=a846a48eb4220250672e1e7b057ec198
author: "程序员Sunday 程序员Sunday"
collected: 2024-10-06
tags: []
---

# FlyonUI - 全新发布的 TailwindCSS 组件库

# FlyonUI - 全新发布的 TailwindCSS 组件库

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzkxNjUxMDg4Ng==&mid=2247496418&idx=1&sn=916c2aa32e8feb1115ec0f7a91598371&chksm=c0689a95170fc4fb63abedeb26f510bcbc589a61fe2ea6c68191d566134a375667e6e207baf6&mpshare=1&scene=1&srcid=1006YTpMUYFi9r5tOrtUY4IK&sharer_shareinfo=a846a48eb4220250672e1e7b057ec198&sharer_shareinfo_first=a846a48eb4220250672e1e7b057ec198#rd)程序员Sunday 程序员Sunday


> **[前端训练营：1v1私教，终身辅导计划，帮你拿到满意的 `offer`。](https://mp.weixin.qq.com/s?__biz=MzkxNjUxMDg4Ng==&mid=2247496306&idx=1&sn=750851b805bcaf4d8876076d3ed9f8ec&chksm=c14c73bbf63bfaad215823d5ad9d63d290edf4bb7936a8fbc9f58d3efde04caa88c11e6b4bef&token=557474678&lang=zh_CN&scene=21#wechat_redirect)** 已帮助数百位同学拿到了中大厂 `offer`

Hello，大家好，我是 Sunday。

说起组件库，我们首先想到的就是 `Element、Ant Desgin、Arco Design` 这些。但是我们需要知道的是，除了这些国内开源的组件库之外，还有很多其他的组件库。

所以，今天我们就为大家介绍一个最新开源的组件库 `FlyonUI`，它是基于 `tailwindcss` 进行构建的
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7TYk3Nkicfc6KoWobPPg0lVT7QiaQYd67R8IXfvdvMia9kovYKNzWwwGyEA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)

根据他的发布记录，该组件库是 `2024 年 10 月 1 日` 发布的，目前最新的版本是 `V1.0.2`。发布 4 天时间，拥有 `300+` 的 `star`，还是非常不错的
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7TTjssCCxiayqH5NsuZXkBrS2zZ5rGz9XlqTaLiaCP8AYbPia5ybtDL4sdg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

## 使用方式

1.
   `FlyonUI` 是不支持 `CDN` 引入的，这意味着我们必需要通过 `npm` 进行安装 `npm install flyonui`。同时还需要注意 **必须安装 `tailwidncss`**

2.
   安装好之后，需要在 `tailwind.config.js` 文件并添加 FlyonUI 作为插件

    module.exports = { 
      content: ["./node_modules/flyonui/dist/js/*.js"], 
      plugins: [
        require("flyonui"),
        require("flyonui/plugin") 
      ]
    }

3.
   开始 JS 交互

    <script src="../node_modules/flyonui/flyonui.js"></script>

## 组件特性

`FlyonUI` 的组件风格与大家所熟悉的组件风格差距较大，它是基于自己独特 设计风格（Desgin）的一种模式，并且沿用了 `Tailwindcss` 的 "原子级 css" 风格
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7THTGibYMQqEsZo3FX4ibKTIFicUnYDMVP874dIjkQ1HQaicQ541kTicbck7Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

我们以常用的 `button` 组件为例，先来看下对应的样式：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7TZtzMCwP9KeibyiaOOjzdca1Ct4vticL8DKdfpfnR6daTAKl9Qib7bficZtA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

点击 `HTML` 部分既可看到对应的 `使用方案`
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7ToBRqOibOBOyx2MxRhPicAEU6p1yLhFfY9poaOLY0ibWEb74tI8kYjiaqbw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

没错，`FlyonUI` 的使用与传统组件库完全不同，它是通过 `class` 类名的方式制定对应样式的。如果不熟悉 `tailwindcss` 的同学，可以类比最早的 `bootstrap` 使用方式。

那么看到这里有同学就可以会疑惑了：\*\*既然是组件，那么就要提供 `功能`，而不能 `仅仅是样式`\*\*。如果它通过 `class` 来进行使用，那么如何提供组件的功能呢？

我们以 `loading` 功能为例：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7TURLqib2DiaianeAB4XrYiaiaUQQCVMGibnu8pYvdSp0sJSfIl97JQIBMQdoQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

如果想要使用 `loading` 那么需要采用 **组合的 html 结构进行**
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxy7dia8mbicHK90Qtkslaiah7Tt12UH5p9VPWiaV22aoxJ2CyYrTWiblibv6WgG0jLESiaPW5R3qshr1jrvg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

如果要在框架中进行使用的话，那么需要这样做：

    // vue
    <button class="btn btn-square btn-primary" aria-label="Loading Button">
      <span v-if="isLoading" class="loading loading-spinner"></span>
    </button>

    // react
    <button className="btn btn-square btn-primary" aria-label="Loading Button">
      {isLoading && <span className="loading loading-spinner"></span>}
    </button>


## 1v1私教，帮大家拿到满意的 offer

我目前在做一个 **前端训练营** ，主打的就是：**1v1 私教，帮大家拿到满意的 offer** 。

[可以点击这里查看详情](http://mp.weixin.qq.com/s?__biz=MzkxNjUxMDg4Ng==&mid=2247496306&idx=1&sn=750851b805bcaf4d8876076d3ed9f8ec&chksm=c14c73bbf63bfaad215823d5ad9d63d290edf4bb7936a8fbc9f58d3efde04caa88c11e6b4bef&scene=21#wechat_redirect)

也可以直接加我微信沟通，备注【训练营】：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FPtef09iaEWxyQaReU5SpIyjlxuaM5tF5yqMLD6iaRLK8cCrALyq89zQCgBoJ5uibx7P6IicyScPMevDwnZwSiclNJdQ%2F640%3Fwx_fmt%3Dother%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26tp%3Dwebp)

[mp.weixin.qq.com](http://mp.weixin.qq.com/s?__biz=MzkxNjUxMDg4Ng==&mid=2247496418&idx=1&sn=916c2aa32e8feb1115ec0f7a91598371&chksm=c0689a95170fc4fb63abedeb26f510bcbc589a61fe2ea6c68191d566134a375667e6e207baf6&mpshare=1&scene=1&srcid=1006YTpMUYFi9r5tOrtUY4IK&sharer_shareinfo=a846a48eb4220250672e1e7b057ec198&sharer_shareinfo_first=a846a48eb4220250672e1e7b057ec198#rd)

