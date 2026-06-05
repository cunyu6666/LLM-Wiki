---
id: "7303433732575200901"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483898&idx=1&sn=325483d6c635e779b6cc0f105daaf69e&chksm=918e138366cb401558442b419febe7fb5c2f629ea9b0748ffad78c474646d32923dd5cea11b3&mpshare=1&scene=1&srcid=0323YW44ZpGZ84NvqC7gL0GY&sharer_shareinfo=cca14514ef396c4694ef2160bc255839&sharer_shareinfo_first=cca14514ef396c4694ef2160bc255839
author: "全金属外壳AI 未来的回响"
collected: 2025-03-23
tags: []
---

# 如何在Cursor中使用Magic MCP生成好看的UI

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483898&idx=1) · 全金属外壳AI 未来的回响


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicr2OiaibWxUmKAzKLXkL7TUZtiaDdEBJnKic3ibdFWibqcZZvcuRrNtfxicL2w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

21st.dev发布的Magic Component Platform (MCP) 是一个强大的AI驱动工具，帮助开发者通过自然语言描述即时创建美观、现代的UI组件。它与流行的IDE无缝集成，为UI开发提供流畅的工作流程。

## 一、**功能特点** 🌟

- **AI驱动的UI生成** ：通过自然语言描述创建UI组件

- **多IDE支持** ：

  * Cursor IDE集成

  * Windsurf支持

  * VSCode + Cline集成（测试版）

- **现代组件库** ：访问大量受21st.dev启发的预构建、可定制组件

- **实时预览** ：创建组件时即时查看效果

- **TypeScript支持** ：完全支持TypeScript进行类型安全开发

- **SVGL集成** ：访问大量专业品牌资产和标志

- **组件增强** ：使用高级功能和动画改进现有组件（即将推出）

## 二、工作原理🎯

1. **告诉代理你的需求**

   1. 在你的AI代理聊天中，只需输入/ui并描述你需要的组件

   2. 示例：/ui 创建一个具有响应式设计的现代导航栏

2. **让Magic创建它**

   1. 你的IDE会提示你使用Magic

   2. Magic立即构建一个精美的UI组件

   3. 组件灵感来源于21st.dev的库

3. **无缝集成**

   1. 组件自动添加到你的项目中

   2. 立即开始使用你的新UI组件

   3. 所有组件均可完全定制

## 三、前提条件

- Node.js（推荐最新LTS版本）

- 支持的IDE之一：

  * Cursor

  * Windsurf

  * VSCode（带Cline扩展）

## 四、使用方法

1、进入https://21st.dev/官网点击右上角sign up注册账号，直接使用github账号登陆授权即可。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhico2XtaE3Hdqg4sJUk5oeW76CdVVNcAxfDzTicY7m3icHqw8Bp91fVbN9w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

2、登陆后点击右上角API key。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicW9zbP3y1IDlnP9rX1zUwFXMbQrHagKgssYDEWCiaqneXdXic1TRbnYqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

3、进入页面最下方创建key

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicAQzWyCqFiaIjgTQ0u1Baz90d3wkZ8zaf6jdSWAjnRrlqslVt8XuiabQA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

4、填写项目URL

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicVopZO0XgFYxdLky5hXOziafXsaz7SQDUf4pELZiarW2gtyQZz82aUHpA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

5、创建完成复制key，在smithery.ai生成命令

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhiczd0tvozQhjGFiadibpsibowuu0fABAowQzv7afIpJhpLqnCyn111nFB1Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

6、Cursor 0.47以上版本和0.46及之前版本命令不一样，我现在用的是0.48，需要在终端中运行命令启动Magic MCP服务器。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicNVibZ1LLgMG5HuXgrtichIauOoEvSgz5XHdg7k4QC89ibEibD6uCl9foSQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhic6qsHW3MdXZia1ZAStfHggboOmicYCb0pXnDocoYlNtvESyXW6cGgDNHQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

7、启动完成后在Cursor中就可以看到Magic MCP了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicW1VibcBP0jS1ib4bz5uibj9ZXqq4H2gibYejedsTFX03p90Z03icLeoQJbQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

8、测试一下使用Magic MCP创建企业官网。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicsc2MvCV9OI8AWYZdpw0pPuK9nxgKOWwrTrwQJSIsg1UhZqnqNUrq2g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

9、生成了这些文件，并且提示我启动项目

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicUu0JvjWnt4kpl9sMve5qEM1ulmibMRzib6OGCtCLcJH3JibiapXdgoDiadA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicjGmqzqkdlsCSNIFQamDLSHw8Y6cyiakfo2icpMga6WxbCV79VG7WZamQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

10、有个报错让Cursor处理了一下，测试官网可以正常打开了，效果还不错，该有的都有了，审美非常在线。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicEWRnX6jbfhHMIq35jWpmeibzafzDh8CQEty1BVWZn4xrZP1Lk8TzERQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicpfYVqWs4JesVP7S2Hv4Qwgenh4bNlof7TkckzaKG4uKsPp3HNDKiaMA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhic0uwoyLYr4Jzib6gpfnWo8oqKHJbesuib2icSqNSaf321F6YCWvLconyew%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicBEuRicWEcCiaURLgkHybrzNxw8ibrE2V8TuicumjdnWlBNWNl3qrt5NC0g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicXlrYIl7Fy5ZQ09SQHj3pX6Y6nrAqyYACh4BpHfCfQAgScicRliaqwb2g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**更多关于AI、Cursor、MCP相关的教程和资讯请持续关注我后续的分享！**

本文完整版详见公众号：**未来的回响**


-END-

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBKtiakuToiafwefHHQCgome5pLo7oRwQtx0y1EbibevWTfhjo0o7jLyCdJs2CcFbsvtd2gCFguIPdPSw%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**未来的回响**

未来源自于此，创造在此迸发......

19篇原创内容

<br />

公众号  

，  

欢迎加入**AI工具实战派**交流群一起学习进步～

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FxFbsATlObBLibseVOu6dNmJDZpxUhBy1ZCW4icPZnN7WqIqdOagqjBDjgZ42B9kXSaZXXlgTHXhzzYcFqzK89xRg%2F640%3Fwx_fmt%3Djpeg)

**AI知识学习、工具资料分享**请加入我的知识星球

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FxFbsATlObBKKtKmzU94ezBKA7kn1W8XCs1r6oRibDNG4rVV516OrHNZY8oNFKAbRP3rsicfe2VU0SpCwBznic4sww%2F640%3Fwx_fmt%3Djpeg)

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483898&idx=1)
