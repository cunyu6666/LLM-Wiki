---
id: "7447681337382669917"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484100&idx=1&sn=34fccbbde0e6b5e77bb4fbdb6eb3b5f1&chksm=f51d9ebcf4f62e5ae8bce7d3df964a58af655d54796564769bc26a2d98c67b2fda3cefc3a139&mpshare=1&scene=1&srcid=0425YCvpNCqv2dwtYXY6H6QH&sharer_shareinfo=6bb2cc7aa25e6f06f9aea89fe998a8b7&sharer_shareinfo_first=6bb2cc7aa25e6f06f9aea89fe998a8b7
author: "Github AI 精选 GitHub AI 精选"
collected: 2026-04-25
tags: []
---

# 视频界的“码农”革命！HeyGen 刚开源的 HyperFrames，让写 HTML 也能出大片

# 视频界的"码农"革命！HeyGen 刚开源的 HyperFrames，让写 HTML 也能出大片

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484100&idx=1&sn=34fccbbde0e6b5e77bb4fbdb6eb3b5f1&chksm=f51d9ebcf4f62e5ae8bce7d3df964a58af655d54796564769bc26a2d98c67b2fda3cefc3a139&mpshare=1&scene=1&srcid=0425YCvpNCqv2dwtYXY6H6QH&sharer_shareinfo=6bb2cc7aa25e6f06f9aea89fe998a8b7&sharer_shareinfo_first=6bb2cc7aa25e6f06f9aea89fe998a8b7)Github AI 精选 GitHub AI 精选


还在用剪辑软件一帧帧拖进度条？HeyGen 开源的 HyperFrames 告诉我们：视频不再是"剪"出来的，而是"写"出来的。支持 HTML 渲染、AI Agent 原生驱动，视频生产力即将迎来降维打击。


PART 01


视频创作的"工业化"拐点


如果你关注 AI 视频领域，一定听过 HeyGen 。这个让全球政要"开口说外语"的公司，最近又在开源社区扔下了一枚重磅炸弹： HyperFrames 。

简单来说，HyperFrames 是一个 视频渲染框架 。但它最性感的点在于： 它让你像写网页一样写视频。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FuMTXOl2H5hlvCXRJOjXXE62bzp9clWrX5Fsia7shbQeT4z6rZT58uticCIic2dAPcxascpvkA4oWodcOthmNWMpBeiaZFr49ZUIibWpXkHQssfqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)


PART 02


什么是 HyperFrames？


在传统的视频制作流程中，我们依赖于 Premiere、After Effects 等 GUI 工具。而 HyperFrames 彻底颠覆了这个逻辑，它提出了： Write HTML, Render Video.

它本质上是一个基于 Node.js、Puppeteer 和 FFmpeg 的渲染引擎。它将 HTML 页面中的元素、动画（GSAP/Lottie）和多媒体素材，通过"帧适配器"模式精确捕获，最终导出为高品质的 MP4 视频。

核心特性：

*
  HTML 原生： 不需要学习复杂的视频编辑协议，只要你会写 HTML/CSS，你就能做视频。

<!-- -->

*
  AI Agent 友好： 这大概是 HyperFrames 最核心的野心。它内置了专门针对 AI 代理（如 Claude, Cursor）的技能包，让 AI 能直接"看懂"并编写视频脚本。

<!-- -->

*
  确定性渲染： 同样的输入永远得到同样的输出。对于需要批量化、自动化生产视频的团队来说，这是梦寐以求的稳定性。


PART 03


它是如何工作的？


想象一下，你只需要定义一段简单的 HTML 代码：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FuMTXOl2H5hmXxZu5ric1b5874P2tIkG4dY9BqNhdvRwG3tOrqm4u1mzicZYzT1Xl2kHwhYTBZEczePdzJcLvnXzfZf7O6EFiawpXvK7XE5orZU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

再配合几行 GSAP 动画代码，HyperFrames 就能在后台像浏览器渲染网页一样，逐帧捕捉这些画面。

它支持的"黑科技"包括：

*
  Shader 转换： 甚至支持 WebGL 着色器，做出电影级的转场效果。

<!-- -->

*
  数据驱动： 输入一个 CSV 文件，自动生成动态柱状图视频。

<!-- -->

*
  网站一键转视频： 直接输入一个 URL，它能把网页内容抓取并转化为视频演示。


PART 04


为什么说它是 AI 时代的"基础设施"？


过去，我们让 AI 做视频，通常是"提示词 -\> 视频"。但这种方式不可控，且难以微调。

HyperFrames 走的是另一条路： AI 控制代码，代码控制视频。

因为 HyperFrames 使用的是 HTML 这种结构化语言，AI 对它的理解远超复杂的视频工程文件。现在，你可以对你的 AI 助手说：

"帮我把这个 GitHub 仓库的介绍做成一段 45 秒的短视频，背景要深蓝色，标题带渐变，加上活泼的入场动画。"

AI 瞬间就能生成对应的 HyperFrames 项目并直接渲染出片。


PART 05


如何快速上手？


HyperFrames 的安装和使用非常开发者友好，只需几个命令：

1.
   初始化项目
2.
   实时预览（在浏览器里实时看到视频效果）
3.
   正式渲染（导出 MP4）


对于专业开发者，它甚至提供了 Docker 支持 ，意味着你可以轻松地在服务器端部署一套"视频生产工厂"。


PART 06


结语：剪辑师会被取代吗？


HyperFrames 的出现，并不是要消灭剪辑师，而是要消灭 重复性的体力活 。

它将视频制作从"手工艺活"变成了"软件工程"。如果你是一个开发者，或者正在寻找自动化内容生产方案，HyperFrames 绝对是目前最值得关注的开源项目之一。

项目地址： https://github.com/heygen-com/hyperframes

互动话题： 你觉得"代码写视频"会成为未来的主流吗？欢迎在评论区分享你的看法！

![](https://image.cubox.pro/cardImg/4r1vfr6povf3fwwm2kjgbcprat69ntmx3agle8qx5rzw0bukqv?imageMogr2/quality/90/ignore-error/1)

**GitHub AI 精选**

专注分享 GitHub 上免费、开源、可商用的 AI 工具，更新保姆级部署教程，帮你零代码上手 AI 办公、AI 写作、AI 绘图、AI 编程，让普通人也能用 AI 提升效率。关注我，带你玩转 GitHub 开源 AI，少走弯路、不花冤枉钱

35篇原创内容

<br />

公众号  

，


PART 07


往期推荐


[上交大出手！免费大模型教程爆火 GitHub，星标 30800+](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484075&idx=1&sn=1bb3285ea9790a2c54cb3c2bb6ca3d17&scene=21#wechat_redirect)

[40K星封神！Claude总失忆？这款开源神器让AI拥有永久记忆](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484066&idx=1&sn=ed82233ab52f26bf9c60e44d7583c335&scene=21#wechat_redirect)

[11K星爆火！AI写代码总翻车？Karpathy大神4条准则，让Claude秒变靠谱队友](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484061&idx=1&sn=4a559efc5619e517e5e7e49fc97fbd6e&scene=21#wechat_redirect)

[微软杀疯了！这款开源神器，一行命令搞定所有文档，AI 直接起飞！](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484055&idx=1&sn=920bae6532e2e87d566625cba4634612&scene=21#wechat_redirect)

[AI太啰嗦还烧钱？这个"山顶洞人"插件火了！一句话省75%成本，普通人也能用](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484050&idx=1&sn=04185adea4fd0f1c1f1201786423617a&scene=21#wechat_redirect)

[星标 35.7k+！Hermes Agent：自我进化的 AI Agent 框架](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484045&idx=1&sn=bfc6651f02124ccdc22cdbd3fa4bc59e&scene=21#wechat_redirect)

[爆火 GitHub！《生化危机》女主打造免费 "AI 记忆系统](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484035&idx=1&sn=6d225f516dcadabcb979e685d78ba1b3&scene=21#wechat_redirect)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY5NzE0Mjc5OQ==&mid=2247484100&idx=1&sn=34fccbbde0e6b5e77bb4fbdb6eb3b5f1&chksm=f51d9ebcf4f62e5ae8bce7d3df964a58af655d54796564769bc26a2d98c67b2fda3cefc3a139&mpshare=1&scene=1&srcid=0425YCvpNCqv2dwtYXY6H6QH&sharer_shareinfo=6bb2cc7aa25e6f06f9aea89fe998a8b7&sharer_shareinfo_first=6bb2cc7aa25e6f06f9aea89fe998a8b7)

