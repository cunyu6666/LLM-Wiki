---
id: "7387837281173766319"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247483811&idx=1&sn=71e0b51cfd793f84d86c9c5dd561eb0c&chksm=9783cfa97388427f4c9efede1eb39b6051bafb0638d108fc1433ba59bd148b06908e77c821eb&mpshare=1&scene=1&srcid=1111har85R0Vl6ReWlhb6ZKF&sharer_shareinfo=f251323287e4af7b539da763a553333f&sharer_shareinfo_first=f251323287e4af7b539da763a553333f
author: "鲁工 AI编程实验室"
collected: 2025-11-11
tags: []
---

# Claude Code + Slidev：做出开发者风格的PPT

# Claude Code + Slidev：做出开发者风格的PPT

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247483811&idx=1&sn=71e0b51cfd793f84d86c9c5dd561eb0c&chksm=9783cfa97388427f4c9efede1eb39b6051bafb0638d108fc1433ba59bd148b06908e77c821eb&mpshare=1&scene=1&srcid=1111har85R0Vl6ReWlhb6ZKF&sharer_shareinfo=f251323287e4af7b539da763a553333f&sharer_shareinfo_first=f251323287e4af7b539da763a553333f)鲁工 AI编程实验室


大家好，我是鲁工。

昨天逛X，看到一个专为开发者做PPT的项目：

Slidev。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIqOqBH24LqsUYIZwXEprboibPGqmktqM9icR1WFL1bIjVxauQZdqqCmqg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

按照Slidev官方的说法是：Slidev旨在为开发者提供更为灵活和易交互的PPT制作方式，并帮助开发者使用熟悉的技术来使演示更加有趣、有表现力和吸引力。

所以Slidev最大的特色是，基于Markdown进行交互的。

熟悉Markdown的朋友都知道，这是程序员最喜欢的文档写作方式。现在Slidev把它拿来做PPT和视觉效果呈现，也是一件非常有意思的事情。

因为Slidev的PPT是在Web端呈现的，所以只要是在浏览器上能显示的，就能在Slidev的PPT上显示。相较于传统的用Office做PPT的方式，相信Slidev能给大家带来更丝滑的视觉体验。

Slidev如何使用

预先安装18.0以上版本的Node.js，然后找个目录启动创建一个Slidev项目：

    npm init slidev@latest


然后就会自动创建一个Slidev项目，在浏览器中打开：

    http://localhost:3030/


即可进行Markdown文件的编辑来制作PPT。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIZqiaa3Lic79F7qhNn0NxIXXor38tJdmEFcg0Tic7dpLQ8tGunthgUQ8PA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

Slidev项目启动相关页面，可以在右侧直接进行markdown代码编辑，添加各种样式和效果。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdrYoaRGyF2mcO3QDMX1ONM9Zxkoia4mZdCTRKutK0f3bLvGW2XEbPe2PeEibMdicCsRhqe5BwcPZbZhw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdrYoaRGyF2mcO3QDMX1ONM9yibjfUZzjzHzjq5ldWJXIicOvy6ibj3eZqxuWDwEgs17D2Y97M6LuLscQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdrYoaRGyF2mcO3QDMX1ONM9KEOdRP4jfCw7zxiatKbtMKcXliaicDibe1ibvlLXQHrrAxSJyXGmSV3P9xQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

markdown写完之后，也可以通过slidev export导出为PDF或者PPTX文件。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIBWcrF7SsglSGO95Aq7c2rgmOEibEvCMuOUrqetmfSEumXPrWOgnKicnw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

更多命令和用法可参考Slidev官方文档：

https://cn.sli.dev/guide/

如何在Claude Code中使用Slidev

既然Slidev的PPT是基于markdown代码编辑生成的，那么正好可以用Claude Code来帮我们Vibe这些.md文件。

但前提是，需要先安装一下Context7这个MCP，Context7是一个专门为大模型和AI编程工具提供最新代码文档和教程的MCP服务器工具。我在之前的文章中专门写过，安装方法可参考：

[Claude Code，我只用这两个MCP](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247483665&idx=1&sn=e9dc848c277df19fdeff016b6faa487b&scene=21#wechat_redirect)

可以现在Context7中确认一下，确实是有Slidev的文档：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIkkOolwVne7gfXv5Mic47ia2kTVPeZdq41RvntzmZwaeLJ7oZNagD1Xwg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

然后直接在Claude Code会话中，要求帮我们用Slidev做一个任意主题的PPT。比如，我让Claude Code以Vibe Coding为主题，制作一份Slidev PPT，内容和风格不做限制。参考提示词如下：
> 使用Context7工具，查看Slidev相关文档。并以Vibe Coding为主题，查找相关资料，制作一份Slidev PPT，输出为.md文档。

Claude Code一顿操作之后，很快就完成了这个任务。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIGnTgnHtHJIW2HpvicNxM7pA5hlB83xCsBgUJPHltQ2ZPWicL0MwmANibA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)

我们在网页端查看PPT效果，非常nice！满满的程序员风格。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhI81brKe3roOiaSD7dFCBU7wdictiaicQ0HO8VGuR1l2V2ekNKaZhibjf4R1Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D8)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIedY8wgYPts1PIpnibWDp5vXBZs4CMmMjtsyNKQAticJXQpCXPS7esp2Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D9)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIxvk3vTwuo5dr0QPUXkhuYuQsVSYYtHCbU7QDddRb2YcX1iaYHdaicFbA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D10)

如果我们在CLAUDE.md文档对PPT的结构编排、风格做出规则化的限定，这样生成的PPT定制化程度就会更高。进一步地，如果你能把上述流程编排为更加细致和个性化的工作流，从此告别写PPT也不是不可能。

并且，如果你markdown写得非常熟练的话，你也可以直接在网页端修改Claude生成的markdown代码：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoEuVOSAxXOajXsmVOAcYhIaXFzuyicopichMDDxElYs7qlltT2hk4A3k7J2NPia0OezWa8Ribr1Da27w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D11)

以上就是今天的内容。如果对你有帮助，欢迎点赞和留言交流。

感谢您阅读我的文章。我是鲁工，八年AI算法老兵，AI全栈开发者，深耕AI编程赛道。欢迎关注，感兴趣的朋友也可以加我微信（louwill_）交个朋友。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F4lN1XOZshfekhSPOVhKyHjek97r6uIakcYsqZxEMvKBCYqOO6wGleHTNuz4sff6Xns2LDGah9Jb6c39iaOhvfpQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26wxfrom%3D13%26wx_lazy%3D1%26tp%3Dwxpic%23imgIndex%3D4)

\>/ 作者：鲁工

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247483811&idx=1&sn=71e0b51cfd793f84d86c9c5dd561eb0c&chksm=9783cfa97388427f4c9efede1eb39b6051bafb0638d108fc1433ba59bd148b06908e77c821eb&mpshare=1&scene=1&srcid=1111har85R0Vl6ReWlhb6ZKF&sharer_shareinfo=f251323287e4af7b539da763a553333f&sharer_shareinfo_first=f251323287e4af7b539da763a553333f)

