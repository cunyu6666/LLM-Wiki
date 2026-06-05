---
id: "7409877832769210804"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484318&idx=1&sn=3a3a860448645401b1da2863f40fa69c&chksm=97493d11e907aae1284ba62c6e86658b7801438cb276873f978309e68cf7de05de23059e44a9&mpshare=1&scene=1&srcid=01118SUAM2Jw297f43LAvZA7&sharer_shareinfo=9114096d19b9acc8b4112d571246ff0b&sharer_shareinfo_first=9114096d19b9acc8b4112d571246ff0b
author: "鲁工 AI编程实验室"
collected: 2026-01-11
tags: []
---

# OpenCode + oh-my-opencode的开源组合，用起来比Claude Code还丝滑？

# OpenCode + oh-my-opencode的开源组合，用起来比Claude Code还丝滑？

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484318&idx=1&sn=3a3a860448645401b1da2863f40fa69c&chksm=97493d11e907aae1284ba62c6e86658b7801438cb276873f978309e68cf7de05de23059e44a9&mpshare=1&scene=1&srcid=01118SUAM2Jw297f43LAvZA7&sharer_shareinfo=9114096d19b9acc8b4112d571246ff0b&sharer_shareinfo_first=9114096d19b9acc8b4112d571246ff0b)鲁工 AI编程实验室

大家好，我是鲁工。

我原以为Claude Code不论是在模型上还是Coding Agent上，都已经是当世能给用户带来最好体验的Vibe Coding工具了。

没想到最近X上疯传的OpenCode + oh-my-opencode开源组合，甚至能有比Claude Code更丝滑的Vibe体验。

今天就简单聊一下这套开源方案。

## OpenCode：终端AI编程的开源新星

OpenCode是一个纯开源的终端AI编程助手（TUI），GitHub上已经有50,000+ stars，社区活跃度非常高。当然也提供了GUI安装方式，可以根据需要选择。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4iaUV81ojibEuHicLFINXzjFpMjhib0djADxqBZLvj9TGgFkNVicAnW5AUxsg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

它最大的特点是**Provider无关（说不好听点叫套壳，但对于用户而言，只要好用，并不在乎你是不是套壳），** 你可以接入Claude、GPT、Gemini，甚至本地模型，总共支持75+家供应商。这意味着我们可以用最便宜的模型做日常任务，复杂任务再切换到Claude，灵活控制成本。

并且GLM-4.7、MiniMax M2.1和Grok Code Fast-1等模型都免费用，堪比活菩萨。

核心功能包括：

**双模式切换** 。Tab键一按，在"plan模式"（只规划不动手）和"build模式"（直接改代码）之间切换。这个设计很实用，有时候你只想让AI帮你理清思路，不希望它直接改文件。

**LSP开箱即用** 。语言服务器协议直接集成，代码跳转、类型提示、引用查找这些IDE里的功能，终端里也能用。这点比很多CLI工具做得好。

**MCP协议支持** 。跟Claude Code一样支持MCP扩展，生态兼容性不错。

安装也简单，一行命令搞定：

    npm install -g opencode-ai


    ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4ia2SkvahNQb0GgC4ekrBmyyZWRibsEV5uvlMM4PN9K04SaNsmdTiazXL3w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

    单独用OpenCode已经能覆盖大部分场景了。但如果你想要更丝滑的体验，接下来这个插件值得一试。得一看。

## oh-my-opencode：让OpenCode起飞的增强包

oh-my-opencode是一个社区开发的OpenCode增强插件，作者给它起了个名字叫"Sisyphus"（西西弗斯）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4ia7FcT9boY0FmKd0vNdqgxrSJ4E7v7GHMKBlO3dnfLTzWGz8aR16GGdg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

这个插件的核心理念是Multi-**Agent协作** 。它在主Agent之外，引入了一系列专业代理：

* **Oracle：架构审查，帮你把关代码设计**
* **Librarian：文档检索，快速找到需要的信息**
* **Frontend Engineer：前端专项代理**

这些后台代理可以并行工作，主Agent只需要接收结果通知。用官方的话说就是：Sisyphus不会浪费时间自己翻找文件，它让主Agent的上下文保持精简。oh-my-opencode的作者为了设计Sisyphus的Agent架构，总共烧掉了24000美元的token。

oh-my-opencode的几个核心的功能：

**AST感知的代码操作** 。不是简单的文本替换，而是基于抽象语法树的智能重构。改个变量名不会误伤字符串里的同名文本。

**Comment Checker** 。自动防止AI过度注释，这个真的救命。用过AI编程的都知道，AI特别喜欢加一堆"//这里是xxx"的废话注释。

**ultrawork模式** 。输入这个关键词，直接激活最大性能模式，适合处理复杂任务。有点像Claude Code的Ultrathink关键词触发极限思考模式。

**自动会话恢复** 。断网或者意外退出，重新进来能接着之前的上下文继续。

安装也是一行（需要先安装Bun）：

    bunx oh-my-opencode install


    ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4iahuexAwweOnrxeQib103F15lcOBemhlD9SUjHz6ERgzds6o8icEhLoGEw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

```

```

    安装后终端有引导，按照引导操作即可，配置完成后直接输入opencode即可在oh-my-opencode加持下使用opencode。code加持下使用opencode了。

```

```

    ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4iahoibwYkWNvDscPmiaG98plKJu5wgCdS7wjztnoUw2B0zib1MKGF0GpFWw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

```

```

    切换Agent：

    ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4iaXjHrvpIIMMWZ7bicKPNgVroB8Ckxx6hrety56oH9UHaYngZ57iafNyOA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

```

```

    切换模型：

    ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdoJ0u7iabC1D2icqcPzQmGT4iaDe4Hib3eiahdgqjPeR8gwFXHE7UzWmO2fAP0g8AUAtqiaYT05YDBLu81Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

```

```

    那么，OpenCode + oh-my-opencode的这套开源组合优缺点如何？

    先说说优势。

```

```

首先是灵活性。Claude Code绑定Anthropic的API，OpenCode可以随时切换供应商。我日常用国内开源模型做简单任务，复杂的再切Claude，成本控制在原来的1/3左右。

其次是稳定性。国内网络环境下，OpenCode配合国产模型基本没有断连问题。oh-my-opencode的会话恢复功能也帮了大忙。

最后是社区活力。这个项目更新非常频繁，几乎每天都有新commit。提issue响应也快，有种早期Claude Code社区的感觉。

**不足的话，我觉得其实没有啥真正的不足，硬要说可能就是配置复杂了点（这都不是事），或者套壳是原罪？**

## 这套组合适合谁用？

如果你是以下几类人，建议试试这个组合：

*
  想控制AI编程成本的开发者
*
  需要在国内网络环境稳定使用的用户
*
  喜欢折腾、愿意配置的技术爱好者
*
  对数据隐私有要求，想用本地模型的人

如果你追求开箱即用、不想折腾，Claude Code仍然是体验最好的选择（前提是网络和预算都不是问题）。

Vibe Coding从去年到今年，赛道是越来越热闹了。各种CLI和IDE让人眼花缭乱。

但OpenCode + oh-my-opencode这套组合，代表了开源社区的一种思路：通过模块化和可扩展性，深挖Agent编排架构，能够带来更加极限的Vibe体验。

少说多做，大家可以试一下这套组合。

OpenCode地址：

https://github.com/anomalyco/opencode

OpenCode官方文档：

https://opencode.ai/docs

oh-my-opencode地址：

https://github.com/code-yeongyu/oh-my-opencode

我是鲁工，八年AI算法老兵，AI全栈开发者，深耕AI编程赛道。欢迎关注，感兴趣的朋友也可以加我微信（louwill_）交个朋友。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F4lN1XOZshfekhSPOVhKyHjek97r6uIakcYsqZxEMvKBCYqOO6wGleHTNuz4sff6Xns2LDGah9Jb6c39iaOhvfpQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwxpic%23imgIndex%3D4)

\>/ 作者：鲁工

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484318&idx=1&sn=3a3a860448645401b1da2863f40fa69c&chksm=97493d11e907aae1284ba62c6e86658b7801438cb276873f978309e68cf7de05de23059e44a9&mpshare=1&scene=1&srcid=01118SUAM2Jw297f43LAvZA7&sharer_shareinfo=9114096d19b9acc8b4112d571246ff0b&sharer_shareinfo_first=9114096d19b9acc8b4112d571246ff0b)

