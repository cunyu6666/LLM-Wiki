---
id: "7298633688269459273"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzOTkwMjM0OQ==&mid=2247540494&idx=1&sn=79bcfc8c2eafe4a51f3ace5fad8d7f5b&chksm=e8760ae05986c4350b87a8a32d4b66c93953dd32afcd7e2301aa65f3cadd5dd65d4d0d1d213b&mpshare=1&scene=1&srcid=0310H94mzeUig5WmxjpQNMC5&sharer_shareinfo=3a82b49850ce4345380a72c02adc1ac7&sharer_shareinfo_first=3a82b49850ce4345380a72c02adc1ac7
author: "印记中文团队 印记中文"
collected: 2025-03-10
tags: []
---

# React 中文周刊 #221 - Lynx：抖音团队推出的 React Native 替代方案

# React 中文周刊 #221 - Lynx：抖音团队推出的 React Native 替代方案

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzOTkwMjM0OQ==&mid=2247540494&idx=1&sn=79bcfc8c2eafe4a51f3ace5fad8d7f5b&chksm=e8760ae05986c4350b87a8a32d4b66c93953dd32afcd7e2301aa65f3cadd5dd65d4d0d1d213b&mpshare=1&scene=1&srcid=0310H94mzeUig5WmxjpQNMC5&sharer_shareinfo=3a82b49850ce4345380a72c02adc1ac7&sharer_shareinfo_first=3a82b49850ce4345380a72c02adc1ac7)印记中文团队 印记中文

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2c0JIbGtkx2xViaMY3meBIrtw5YLtKPicE1XWK0QeT2Y1N0NmC6TYbIUQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)
> 本期看点：抖音团队发布基于 QuickJS 的原生应用开发框架 Lynx，TanStack Form v1.0 正式发布提供类型安全的表单状态管理，Next.js 15.2 推出全新调试体验并支持流式元数据，React Scan 工具助力优化 React 应用性能，TypeScript 5.8 发布并增强 Node.js 支持。
> 编辑：TimLi

🔥 本周热门

**Lynx：React Native 的新选择？** ------ 这个标题可能有点夸张，但 Lynx 确实是一个全新的框架，用于构建基于 JavaScript 的原生应用程序。它借鉴了 React Native 的思路，但目标是提供更模块化和灵活的解决方案（最终将支持多个框架）。这个项目来自抖音团队，并已在其内部使用，还配备了自己的基于 QuickJS 的 JavaScript 引擎。


**长按识别二维码查看原文**

https://lynxjs.org/blog/lynx-unlock-native-for-more


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2VntoS3tqciad75SK3lG3P2ibyLbW9eAEtEuBX2Hd78XWSR534TUj3FbQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Xuan Huang 和 Lynx 团队

**TanStack Form v1.0：Headless、类型安全的表单状态管理** ------ 这是一个筹备了两年多终于发布 v1.0 的项目。它提供了类型安全、框架无关（但与 React 关系密切）、headless 且同构的表单处理方案。如果你已经在使用 Formik 或 React Hook Form，想了解它们之间的区别，可以看看这个对比表格。


**长按识别二维码查看原文**

https://tanstack.com/blog/announcing-tanstack-form-v1


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2wI3CicvrrDx5kzEWnKOqdXFVKgwWeocuIzI7ibTTwyafCiaQXDzlqmFiaA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Tanner Linsley

**▶ 如何用 React Scan 优化你的慢速 React 应用程序** ------ React Scan 是一个很实用的工具，可以轻松检测和发现 React 应用程序中的性能问题。如果你还没被说服要尝试它，不妨看看 Jack Herrington 这个 8 分钟的演示视频。


**长按识别二维码查看原文**

https://www.youtube.com/watch?v=3EnathFYgz8


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2zqM9o0ibUrB3EtNR24eaOJbia9USYhGESM04vtP2RwQ9djevOPeDuYmA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Jack Herrington

**React Server Actions 实现 Toast 反馈** ------ Robin 详细介绍了如何一步步实现 toast 通知，为用户提供实时反馈。


**长按识别二维码查看原文**

https://www.robinwieruch.de/react-server-actions-toast/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2hzWia9zns8Sdtx5atzqIeBOdJjE0FVLibg2qpTU7H4OoRfBynbHjPyOg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Robin Wieruch

**📄 使用 React 19 的 cache() 避免服务器组件的瀑布式获取** Aurora Scharff


**长按识别二维码查看原文**

https://aurorascharff.no/posts/avoiding-server-component-waterfall-fetching-with-react-19-cache/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq20eRApkvFgTtUC94053Lf1eckPjcYhvygvS7z7ia3s7iaQkJicVhCA4oLw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**📄 使用 React Three Fiber 创建风格化的水效果** ------ 效果非常漂亮！Thalles Lopes


**长按识别二维码查看原文**

https://tympanus.net/codrops/2025/03/04/creating-stylized-water-effects-with-react-three-fiber/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2gKoUBBbHIW1rT8NzNKOgae0icG39oQD5faKlrLKvF5RmyNgegktxjLQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**📄 不存在真正的同构 Layout Effect** Shane Friedman


**长按识别二维码查看原文**

https://smoores.dev/post/no_such_thing_isomorphic_layout_effect/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2WtDnouuzkWjSHEia16J93r66m1thSFCqHWXiaQlMxEpkETjKQCnnia7DQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**📄 为什么我们放弃了 Next.js** Stewart 和 Snelling


**长按识别二维码查看原文**

https://northflank.com/blog/why-we-ditched-next-js-and-never-looked-back


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2DG4ssrLWTPNcg7syFKZBDWSdpsMknC0T4RAUWpS4FxIrAibltLkxpbg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**📄 如何为表单编写 Zod Schema 类型** Philip Jones


**长按识别二维码查看原文**

https://pgjones.dev/blog/how-to-type-zod-form-schemas-2025/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2v9WPrFZQysHLCvf72Wj8Po8iaRMQDBJe3xnrzjwFtYQkpf5EAOFAvAQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


🛠 代码与工具

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2nvw0RibE1LWNHqHA9SXxuA6QQJ3Q6H6MSfjoZEgKVbJmOzaGh3U7ibag%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg)

**React Data Table：响应式动态表格组件** ------ 简洁但功能丰富。内置列排序和分页等功能。提供了大量演示和代码示例。GitHub 仓库。


**长按识别二维码查看原文**

https://reactdatatable.com/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq24FaKvqrialiaOsdhcKk4icYicDdytGxp74HALiaYRAGoibChxRUw1nU2BBUg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

John Betancur

**使用现代依赖的 Electron 应用程序模板** ------ 一个基础模板，集成了 React 19、Tailwind CSS 4、shadcn/ui、Electron Vite、Biome，并包含 GitHub Actions 发布工作流。


**长按识别二维码查看原文**

https://github.com/daltonmenezes/electron-app


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2LK2EeRLM0MJEY7EllulrNobrupryVJRwycxibSbNTicmIxTOl78DqOvA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Dalton Menezes

**🕒 react-timer-hook：用于处理计时器、秒表和时间状态的 Hook** ------ 提供 useTimer、useStopwatch 和 useTime 三个 Hook，用于在组件中实现各种时间相关的逻辑和状态。


**长按识别二维码查看原文**

https://github.com/amrlabib/react-timer-hook


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2NMhHSRUJj3vNrepthte8eJV8vSQVjg9jrhygicFgRq1eDBymFfxXGSg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Amr Labib

**PDFSlick v2.2：查看和交互 PDF 文档** ------ 一个功能完整的 PDF 查看器，支持 React、Solid、Svelte 等 JS 框架。基于 PDF.js 构建，使用 Zustand 为文档提供响应式存储。查看演示。


**长按识别二维码查看原文**

https://pdfslick.dev/


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2JJAJGlUQVjicN9lfhCZnUD85AEhfRbkzN6Bhh3QNgt4xQ1fOLwk5JHw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Vancho Stojkov

📢 其他

以下是 JavaScript 生态圈中一些你可能错过的有趣故事：

*
  TypeScript v5.8 已发布，这次更新主要关注 Node.js 相关特性，包括新增的 --erasableSyntaxOnly 标志，用于防止使用那些无法在 Node 中直接运行的 TypeScript 特有功能。


  **长按识别二维码查看原文**

  https://devblogs.microsoft.com/typescript/announcing-typescript-5-8/


  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq25I0tjSYGYtjyBMLibeDicGNsPnSC2jJeeZPgiajiaUZmsAPzdk2qn9ibJLQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


*
  如果你是一个对 TypeScript 工具链和开发体验感到困惑的 JavaScript 开发者，Dr. Axel Rauschmayer 写了一篇《什么是 TypeScript？》的概述。


  **长按识别二维码查看原文**

  https://2ality.com/2025/02/what-is-typescript.html


  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq20zJ7s6BEB4C7YZDuYRVMrico6vj0QWtr0k1ib7JkUibsFAg09m1XUGjkg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


*
  QuickJS Sandbox 提供了一种在 QuickJS 驱动的沙箱环境中安全运行 JavaScript 代码的方式 ------ 这里有在线演示。


  **长按识别二维码查看原文**

  https://sebastianwessel.github.io/quickjs/


  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2pJ2JhpLe0yhUdr0q6jHmwSxZiarEMGFWb71VS0LdRGENbDvYdibKBLaA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


*
  free-for.dev 是一个非常实用的大型列表（超过 1000 项），收录了具有免费开发者层级的托管工具和在线服务。


  **长按识别二维码查看原文**

  https://free-for.dev/#/


  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FINNfEriciaG5eCibd9FFNFiaVKJricWlEYAq2M3zJe8lKy0j3ZEFO3fON8gia2QpNgwb2jdZ3hNib1bJhnwCjTFonLvCw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


**版本发布：**

*
  **⭐ Next.js 15.2** ------ 重新设计了调试体验，增加了流式元数据，以及对 React View Transitions 的实验性支持。

*
  **react-responsive v10.0.1** ------ 在 React 中使用 CSS 媒体查询。

*
  **React Native Windows v0.78.0** ------ 用于构建原生 Windows 应用程序的框架。

*
  **React Native Testing Library v13.1** ------ React Native 组件测试工具。

*
  **react-movable v3.4.1** ------ React 中列表和表格的垂直拖放功能。

*
  **React hCaptcha Component v1.12.0** ------ 如果你想要一个 reCAPTCHA 的替代品。

🙋‍♀️ 关注我们

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FINNfEriciaG5fkFtYT6Vj5FicQKu49mRHXDUMUYITOhlZ3ufQ0mez8MenpWd4dtrATsThrTMSjaCHmMuc4a6ic3VSA%2F640%3Fwx_fmt%3Dpng)

![](https://image.cubox.pro/cardImg/2m5zp94iivyaxc6s3fc83fwxsjqy2vfsxfxh1r784f13hzad6u?imageMogr2/quality/90/ignore-error/1)

**印记中文**

深入挖掘国外前端新领域，为中国 Web 前端开发人员提供优质文档！

700篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzOTkwMjM0OQ==&mid=2247540494&idx=1&sn=79bcfc8c2eafe4a51f3ace5fad8d7f5b&chksm=e8760ae05986c4350b87a8a32d4b66c93953dd32afcd7e2301aa65f3cadd5dd65d4d0d1d213b&mpshare=1&scene=1&srcid=0310H94mzeUig5WmxjpQNMC5&sharer_shareinfo=3a82b49850ce4345380a72c02adc1ac7&sharer_shareinfo_first=3a82b49850ce4345380a72c02adc1ac7)

