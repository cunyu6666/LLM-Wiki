---
id: "7420846861856016761"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484707&idx=1&sn=716598aa8840ae0ec8174230f9c0aef1&chksm=97a8adae395ff7ec6237f58158b2678f7067c3fada2e730ca6792902afef882df58f32e6a131&mpshare=1&scene=1&srcid=0210E7VOBHnWBgjAgT5i745D&sharer_shareinfo=c88107291dc2dd5fd67205aecb30ca9a&sharer_shareinfo_first=c88107291dc2dd5fd67205aecb30ca9a
author: "鲁工 AI编程实验室"
collected: 2026-02-10
tags: []
---

# 终极效率方案：使用Claude Code + Opus 4.6与Codex + GPT-5.3-Codex组合开发

# 终极效率方案：使用Claude Code + Opus 4.6与Codex + GPT-5.3-Codex组合开发

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484707&idx=1&sn=716598aa8840ae0ec8174230f9c0aef1&chksm=97a8adae395ff7ec6237f58158b2678f7067c3fada2e730ca6792902afef882df58f32e6a131&mpshare=1&scene=1&srcid=0210E7VOBHnWBgjAgT5i745D&sharer_shareinfo=c88107291dc2dd5fd67205aecb30ca9a&sharer_shareinfo_first=c88107291dc2dd5fd67205aecb30ca9a)鲁工 AI编程实验室


大家好，我是鲁工。

去年11月底Gemini 3.0和Antigravity发布的那段时间，我写过一篇关于如何在Antigravity中综合使用Gemini 3.0、Claude Code + Opus 4.5、Codex + GPT-5.1-Codex来构建最强AI开发组合的文章。

[用Antigravity组建最强开发团队：Opus 4.5 + GPT-5.1-Codex-Max + Gemini 3 Pro](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484044&idx=1&sn=717e2a0a2919c1541228c00b09d6c8fe&scene=21#wechat_redirect)

其中Gemini 3.0和Opus 4.5在Antigravity里面可以免费使用，只需要安装Codex插件后使用GPT-5.1-Codex模型即可。这个方案得益于Antigravity的Agent整合优势和谷歌做慈善的行事风格。

虽然Antigravity现在来看，仍然称不上是一款好用的AI IDE，但上述组合方案确实也还能算是顶级阵容设计。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FMHVsz9lwuhXoPeRVxJ5qks4iaRSYxzbVbykZQn2NmgfY7XKicqx8gOlBOd46wgL9sBtib898QgMxluznfsGFFh1zEnicNGphcyFRIdIDAtW5I3U%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

现在时间到2026年2月，你只需要把Opus 4.5换成4.6，GPT-5.1-Codex换成GPT-5.3-Codex，继续沿用该框架维持顶配阵容。

这个方案在实际使用时，如果想要不同模型之间有交互，可以对每个Agent在在执行任务后给出相应的交付物（artifacts）、切换到另外一个模型时，让其对其他模型的交付物进行review即可。比如，我让Claude Code对代码进行review，并输出review-report.md文件，然后让Codex直接对这份md报告进行check即可。

但是我今天还想分享另外两个组合开发方案。

众所周知的是，Claude Code和Codex CLI是两家独立的AI CLI工具，要想两个工具之间能够状态共享和相互调用，本质上缺少一个共用的工具总线和会话编排设计。

这在去年看起来还比较困难，现在来看已有更多的方案可以选择。

MCP方案

第一种要分享的交互方法是MCP方案。这种方案最简单直接。就是通过Codex的MCP工具，将Codex CLI接入到Claude Code，然后在Claude Code中就可以调用Codex来完成任务。

直接安装codex-mcp-server这个MCP即可：

    claude mcp add codex-cli -- npx -y codex-mcp-server


安装完成后，在Claude Code中确认一下codex-cli MCP状态：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FMHVsz9lwuhXWyEB3arEurM0XM9VsqvH8dibZrgoeOY56xz0Iml03iaJNC0Bzqp630FDnKLL1AFy8DPZCqWwOx0srVuCSWSvxOtJAzj0gfSOvU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

没有问题的话，就可以直接在Claude Code中调用Codex来执行任务了。这个时候，Claude Code是主阵地，Codex只是变成了一个工具调用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FMHVsz9lwuhVArF0YJuzvcXBq8xZZxQLlJb4ylDzEYJ9diaqicSVU4J7LnJTJSaE0xm1El9tufCnrw8X0jnKhnac5eCTgbEGUibBg3blyBrS9Sg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

实际开发时，建议用Claude Code + Opus 4.6来制定计划、拆解任务、设计验收标准和做最终review，具体的代码执行交给Codex + GPT-5.3-Codex来实现。

无头模式 + Skills方案

大家日常都是通过交互模式来使用Claude Code和Codex的，其实我们还可以通过无头模式（Headless mode）来使用这些工具。

无头模式，简单而言就是把Claude Code/Codex从交互式终端应用变成一个可脚本化的命令行工具：不进入TUI和对话界面，而是一次性接收输入 、在指定工作目录里完成任务，然后把结果直接输出到 stdout，方便你塞进CI、脚本、IDE 任务、Makefile、pre-commit hook等自动化流程里。

说白了，就是直接在命令行里面执行任务。

Claude Code和Codex的无头模式执行示例：

    # claude code headless mode example claude -p "Explain what this project does"# codex cli headless mode examplecodex "review一下这份代码"


这样，我们就可以用一个skills结合无头模式，来把Codex的代码执行能力变成一个调用Codex的skills。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FMHVsz9lwuhUGCNIpzWia8hmjNRLcXdwaxTPzURA0EehbDokyr4fy0zofbhjibhb3nTjibYVTzrwicZpWiaXyGjK3mg6zXwIH7mLhJufcKeCDYib28%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

使用GPT-5.3-Codex模型并开启最大权限来执行：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FMHVsz9lwuhWiaHnAuNoicQL54Fh6096a9Txv6AUygNEZyas4ASWbZPH1c5e8uwPySXsyMatzWJiayzIP2kmhTC2SNbbBfWY3Ovl7erM0GF5cSo%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

在Claude Code做完规划后，使用/codex-execute来执行开发计划：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FMHVsz9lwuhWma4IUyEEB3fsFYMRpOIoPRRsp3wulmJ15e3NERsyvATGJsRPFZpPRaA7iaicwtSLbYE7JGsibnxWJhA6tRsibh9AeoCod8WsRneA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

除此之外，还有一种VSCode Multi-Agents方案，也能同时实现对Claude Code与Codex的任务指派。这个功能我们将在下一期文章中给出详细教程。

感谢您阅读我的文章。我是鲁工，九年AI算法老兵，AI全栈开发者，深耕AI编程赛道。感兴趣的朋友也可以加我微信（louwill_）交个朋友。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F4lN1XOZshfekhSPOVhKyHjek97r6uIakcYsqZxEMvKBCYqOO6wGleHTNuz4sff6Xns2LDGah9Jb6c39iaOhvfpQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26wxfrom%3D13%26wx_lazy%3D1%26tp%3Dwxpic%23imgIndex%3D4)

\>/ 作者：鲁工

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484707&idx=1&sn=716598aa8840ae0ec8174230f9c0aef1&chksm=97a8adae395ff7ec6237f58158b2678f7067c3fada2e730ca6792902afef882df58f32e6a131&mpshare=1&scene=1&srcid=0210E7VOBHnWBgjAgT5i745D&sharer_shareinfo=c88107291dc2dd5fd67205aecb30ca9a&sharer_shareinfo_first=c88107291dc2dd5fd67205aecb30ca9a)

