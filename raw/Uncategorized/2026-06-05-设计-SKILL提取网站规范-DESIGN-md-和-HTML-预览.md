---
id: "7462244676708337700"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA3MDc2OTQwMw==&mid=2456446410&idx=1&sn=12ab52cdc733326948036ec30c89f0e6&chksm=89a3ba1b27475e6b3ee7d94f78b63b28dfbf48a8c956b5eaa13b73c5e947bf0300b2c1556223&mpshare=1&scene=1&srcid=06058JmqH2bsDdRlKl5bJKL7&sharer_shareinfo=599dc14bc60dcc25cab710030db9ae3d&sharer_shareinfo_first=599dc14bc60dcc25cab710030db9ae3d
author: "ricoui Rico的设计漫想"
collected: 2026-06-05
tags: []
---

# 设计 SKILL：提取网站规范 DESIGN md 和 HTML 预览

# 设计 SKILL：提取网站规范 DESIGN md 和 HTML 预览

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA3MDc2OTQwMw==&mid=2456446410&idx=1&sn=12ab52cdc733326948036ec30c89f0e6&chksm=89a3ba1b27475e6b3ee7d94f78b63b28dfbf48a8c956b5eaa13b73c5e947bf0300b2c1556223&mpshare=1&scene=1&srcid=06058JmqH2bsDdRlKl5bJKL7&sharer_shareinfo=599dc14bc60dcc25cab710030db9ae3d&sharer_shareinfo_first=599dc14bc60dcc25cab710030db9ae3d)ricoui Rico的设计漫想


rico-design-md 是我在 rico-skills 系列中中开发的一个 SKILL，定位是" DESIGN MD 生成器"。

目前 rico-skills 在 GitHub 上已有 183 个 Star。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FCWGgpODLDzeU0yNhkRpqjiaNiclscRliam3kU51rFiaThibL8zibDTfiab7KulpSPl1t15moRD12Cm1gIpziaTum9du0LatyWNulMJxFe1S11vT5qLU%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

地址是：github.com/ricocc/rico-skills

这个 SKILL 面向的场景很明确：当你看到一个优秀网站，希望分析它的颜色、排版、间距、圆角、阴影、组件状态和整体视觉语言时，rico-design-md 可以把这些信息拆解成结构化规范，同时输出 HTML 设计系统预览图以及开发需要的多格式文件，而不是停留在截图、吸色和主观模仿上。

简单的说，你给它一个网站 URL，它会把这个网站转成一套设计系统文档，提取颜色、排版、间距、圆角、阴影、组件状态，再输出成开发和设计都能继续使用的文件，以及 HTML 预览图。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FCWGgpODLDzcLSTjibzdVctxvYYU6Iz9NMAo4J5fcFEk9hib1ric49xtq6BEN5Ieb5OQS49JIo67duLA6Mfs9eahjd5g99pKxf5bZPwb4Vmf2nY%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

我最常用的命令是：

rico DESIGN.md [域名]

执行后会默认生成两个文件，DESIGN.md 和 preview.html。

前者是完整样式参考，写清楚品牌声音、token、组件、Do's 和 Don'ts。后者是一个可以直接打开的可视化预览页，有颜色色板、字体刻度、间距、阴影、组件示例。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FCWGgpODLDzc2kibtGia5SoGzmM2XIA86gmJMvCJ7JfFThb0mpfDtkz4JSBIb75dYX503YbmL6CV7iaibGoETbyBltx4nxTmwndZIKnJIkkQTszM%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

我当时设计成这样，是因为我发现只给 Markdown 还不够。

因为 Markdown 适合给开发看，HTML 适合给设计、产品、客户看。一个讲规则，一个给直觉。

*
  如果你只想提取 token，可以用 \`rico tokens\[url\]
*
  如果你只要 CSS 变量，可以用 rico variables \[url\]
*
  如果你用 Tailwind v4，还可以生成 theme.css。想一次拿全套，就用 rico 全部输出 \[url\]


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FCWGgpODLDzdVgqYAWF9VfDM0CpphLZmp9yaJKtYzO8KJUOazJLZoB4mZwicqcSl66bHlmialickZNiaELwBpfXPG7iaqAky4tZ4feCpUmBbE7MTg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

除了默认输出，rico-design-md 也支持按需生成单一格式。

rico tokens github.com 会生成 tokens.json，遵循 DTCG 设计令牌格式，每个 token 都包含 $description。

rico variables [url] 会生成 variables.css，适合直接导入前端项目。

rico theme.css [url] 会生成 Tailwind v4 的 @theme 格式。

如果需要完整输出，可以使用rico全部输出github，一次生成DESIGN md，preview.html，tokens.json，variables.css 和 theme.css 。

这个 SKILL 的重点不只是"生成文件"，而是把设计信息结构化。

颜色会被整理成语义化 token，例如 canvas、surface-1、ink、accent-blue。这类命名表达的是用途，而不是单纯描述颜色外观。

排版会记录字体族、字号、字重、行高和字间距，避免只提取字号导致还原不完整。

组件会记录可观察到的状态，包括 hover、focus、active、selected。阴影和圆角会保留可执行的 CSS 值，避免使用"轻微阴影""柔和圆角"这类模糊描述。

还有一个容易被低估的能力，是格式转换。

你已经有 DESIGN.md，可以转成 tokens.json。你手里有 variables.css，也能反推成文档。这样一来，它不只是在生成文档，也是在帮不同工具之间搬运设计资产。

你也可以增加一些要求，按照主题的风格来重构 Preview 预览页，比如下图，就是用主题来重新设计 html 图片的视觉和排版

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FCWGgpODLDzcDToYy0TJQRQvicbdL5sIaC3xKXCNeVoHSCdibLYCCxnfFkeexNLQxN9bRzicLKhwoibkkMmX8yibKNUMnl65RTKfmFfnriaXr445nw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

## 最后

对个人开发者来说，它能让你更快学习成熟网站的视觉语言。对团队来说，它能减少很多口头沟通。对 AI 编程用户来说，它尤其有用，因为你可以先把参考网站变成明确规格，再让 Agent 按规则写页面。

这比一句做得像 Linear 一点，要靠谱太多。

我做 rico-design-md 的价值也在这里。

github.com/ricocc/rico-skills

它不是帮你偷一个网站的样子，而是帮你理解，一个好网站到底是怎么被组织起来的。

对于需要整理品牌视觉、提取设计令牌、构建设计系统，或辅助 AI 生成前端页面的用户来说，rico-design-md 是一个实用的设计资产提取工具。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA3MDc2OTQwMw==&mid=2456446410&idx=1&sn=12ab52cdc733326948036ec30c89f0e6&chksm=89a3ba1b27475e6b3ee7d94f78b63b28dfbf48a8c956b5eaa13b73c5e947bf0300b2c1556223&mpshare=1&scene=1&srcid=06058JmqH2bsDdRlKl5bJKL7&sharer_shareinfo=599dc14bc60dcc25cab710030db9ae3d&sharer_shareinfo_first=599dc14bc60dcc25cab710030db9ae3d)

