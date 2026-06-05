---
id: "7419793771451121945"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA==&mid=2247495787&idx=1&sn=6d2ed6a6a695c79178ad68cd70a5798c&chksm=fab04aa7c0c49f1020edddaaf1b741f4f4308a4b6475c97fe45256ad2c49ceee218e9ca14f2e&mpshare=1&scene=1&srcid=02078GE49qHtcnJmrgVAZWmk&sharer_shareinfo=2ae7a0dc553a9db4b5f9129b525918bc&sharer_shareinfo_first=2ae7a0dc553a9db4b5f9129b525918bc
author: "歸藏的 AI 工具箱 歸藏的AI工具箱"
collected: 2026-02-07
tags: []
---

# 只用一天Opus4.6+Agent Teams做了个ClaudeCode桌面端：已开源

# 只用一天Opus4.6+Agent Teams做了个ClaudeCode桌面端：已开源

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA==&mid=2247495787&idx=1&sn=6d2ed6a6a695c79178ad68cd70a5798c&chksm=fab04aa7c0c49f1020edddaaf1b741f4f4308a4b6475c97fe45256ad2c49ceee218e9ca14f2e&mpshare=1&scene=1&srcid=02078GE49qHtcnJmrgVAZWmk&sharer_shareinfo=2ae7a0dc553a9db4b5f9129b525918bc&sharer_shareinfo_first=2ae7a0dc553a9db4b5f9129b525918bc)歸藏的 AI 工具箱 歸藏的AI工具箱


<br />

歸藏2079  

，赞   
32  


CodePilot 客户端：https://github.com/op7418/CodePilot/releases/tag/v0.2.1

昨天用 Opus 4.6 + Agent Teams 上线。

我用一天时间做了个 Claude Code 桌面端 CodePilot，功能全齐、颜值在线、已经开源。

很难想象，即使我了解 AI，我也不敢想这个事情。

你可以用一下这个软件，看一下它的完成度。

我发现真的只要你现在敢给 AI 花钱和放权，它就是一个许愿机、阿拉丁神灯。

把开发过程和 Agent Teams 的使用经验总结一下。

CodePilot：一个真正能用的 Claude Code 客户端

核心功能全部支持：选择文件夹、切换模型、斜杠命令、Skills 调用、MCP 服务器，跟 Claude Code 命令行版能做的事情一模一样。但体验好了不止一个档次。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FofWbZTuv4DXfLlsibic2nF5yc6Y0EYQoPfT3EBstcb8GfHiaqAU8j4mYtKqeNDibhoFEtkibKkxEW5PPXDZjuZBcb1wvricNJ7gv4AhoZobZbqMyk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D0)

最有价值的三个功能

第一是聊天记录管理：

Claude Code 最让小白头疼的问题就是找不到聊天记录。你明明知道之前聊的内容很有价值，但就是翻不出来。

现在所有聊天记录都保存在侧边栏，跟文件夹绑定，随时能翻回去看。每条消息还会显示花了多少钱，这个透明度很重要。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FofWbZTuv4DUGFPrXy85GnBaxaYnseTKwR50okzDyzupVE695J0FAFAMmMxAzmCnUmibEbkOPxadISwLiaH1PUVpWoeuGUicPOoHoxoHWbicniayE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

第二是可视化配置管理：

Claude Code 的配置文件、Skills、MCP、插件，以前都得去命令行里折腾。现在有个可视化界面，直接在这里改、预览、保存，跟用普通应用一样。

第三是文件夹内容预览。右边栏能看到当前文件夹里所有东西，文本文件可以直接预览。这个功能看起来简单，但实际用起来真的方便。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FofWbZTuv4DVcLS8UJIVIXKNsZ923ugkZL3CYsa6Nwdo8nTec4Qpicy5bfaoVfibYiasKksVUtAQ5rhsic7MYqGtxwXaqa6vZHN0yrPG1icVywI1k%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D2)

第三方 API 配置也支持：

如果你用的是官方授权登录或者已经配好环境变量，直接就能用，不需要额外设置。

但如果你想用第三方的 Claude API（比如一些国内转发的服务），也可以在设置里配置。这个灵活性很重要，毕竟不是每个人都能直接访问官方 API。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FofWbZTuv4DXenZREbVAnz5cekRn6Bwg7r7vw6ic85jtb3ZVNZMOouwAfx81AdZESgiamib3sRzglriaVK96HsDZJTB8y6GK7GBJY26VibzaFrZPQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

连接状态一目了然

状态栏会显示 Claude Code 的连接状态。如果没连上，会告诉你怎么安装和启动 Claude Code。

这个细节很贴心，新手不用懵逼半天不知道为什么用不了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FofWbZTuv4DUTIGaA61KYrJGogTvj8GFdTG2L8t46gqUzxZPECNCG3bFYg1M2qMjfpnlX38cMtpyRILlIjCx3bEF6kkY2AglNyNHiaZ9I9xHk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D4)

最后说一下这个图标设计。为了避免侵权问题（哪怕开源也可能被 Anthropic 说侵权），我没直接用 Claude Code 的官方图标。

做了个体素风格的放射性形状，保留了原图标的菊花辐射感，但变成立体的。猛一看有点像，但又是全新的设计。放在一堆知名工具旁边，一点也不违和。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FofWbZTuv4DWe6kKCiacxnhDbC01eLwXOibE9KKRzy7AALD17rUYiceV2cca7NhaIqCwsAw7d8AUmjFg7UDZiaicfkhM4IaVd6ia5w4DsD8yFnnHZ8%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D5)

如果对 Codepilot 感兴趣可以下下来用一下，目前只支持 M 芯片的 macOS 系统。

因为没有证书，所以需要你去设置安全那边，点击"仍要打开"按钮。

Windows 的话，我回头打个包，我得测试一下。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FofWbZTuv4DXVQJLL33CQgURfUcUicbVtkkWTyQqA9bOt5U3hPCHA5Hb6rUnneibOHhN5kEO3Z8UKhK5FmW0UL6fxETbiaEDjlZ9AxRgAKejT2A%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D7)

Agent Teams：真正的多智能体协作

这次开发用的 Agent Teams 模式，跟以前单个 AI 来回对话完全不是一个概念。

简单说就是有个主智能体，它可以把任务委派给多个子智能体，让他们各司其职、并行工作。而且这些智能体之间能互相通信，主智能体能实时知道子智能体的进度，子智能体也能主动汇报。

这种协作是真的顺畅，不是那种伪多智能体（其实就是一个 AI 来回切换角色）。

怎么启用 Agent Teams

非常简单。更新到最新版 Claude Code，确保能用 Opus 4.6，然后把官方文档扔给 Claude Code，让它帮你开启就行。其实就是改个参数，它直接就能搞定。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FofWbZTuv4DUFAoty08m0WyMJw3tXYDZefiaYaet8aiaDyXbJVyIFFhltf6xLswgGQazxYibB3F8XlDAPzj0POPB8xwsaJgDpRPoflpXB6rQx54%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D8)

技巧 1：让 Claude 帮你写规划提示词

官方文档里有建议的提示词格式，要给每个 agent 设置角色、任务、能力要求。你可能会觉得头疼：我就一个需求，还得想这么多？

不用。把官方文档和你的需求一起扔给 Claude，让它帮你构建 Agent Teams 的规划提示词。

你可以让它先写提示词给你审核，也可以直接让它帮你构建一个 teams 开始执行。反正它比你更清楚怎么拆分任务和分配角色。

技巧 2：前期调研非常重要

我昨天开发的时候发现，前期调研角色能直接决定后面的开发效率。

技术选型、架构设计、组件库选择，你选错一步，后面就会非常难受。所以无论什么需求，我建议都加一个调研角色。

让它去查市面上最好的解决方案、最合适的技术栈、最新的组件库。哪怕你只是要优化 UI，也得让它先找找现在最流行的图标库和设计系统是什么。

技巧 3：角色设计不要用传统软件工程思路

传统团队里，人是固定的，你很难随时调整角色和能力。但 Agent Teams 不一样，你可以针对每个任务定制角色。

比如同样是 QA 角色，在测评功能逻辑的时候，它就专注 code review 和功能实现验证。但在体验优化阶段，同一个 QA 可以变成体验走查专家，专门找视觉和交互问题。

不要让传统的工程思路限制你。每个任务都可以有定制化的角色配置，甚至可以给 agent 设置特长。这种灵活性是人类团队做不到的。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FofWbZTuv4DVIVHYU5Ogp8CvNbsL6OVUgiaINibLpEds4MoBB4dsjdqrNyQYr3u97efK55p7oNKeeVmKDsKdfoaMd352jFwR6Q7Bkzzicbl8Zsk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D9)

这个时代真的不太一样

写 iOS 客户端、macOS 桌面端，功能全齐、没有 bug、一天就能产出。这事儿我以前根本不敢想。

关键是你得敢花钱、敢给权限。很多人舍不得用 Opus，觉得贵。但实际上 Opus 4.6 因为理解能力强、不需要反复纠正，最后反而比用小模型省钱省时间。

Agent Teams 更是这样。多个智能体并行工作，看起来好像花钱更多，但因为效率高、出错少，整体成本反而更低。

好了这就是今天的内容。

如果你觉得内容对你有帮助的话，可以帮我点个赞👍，或者是转发给你需要的朋友。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA==&mid=2247495787&idx=1&sn=6d2ed6a6a695c79178ad68cd70a5798c&chksm=fab04aa7c0c49f1020edddaaf1b741f4f4308a4b6475c97fe45256ad2c49ceee218e9ca14f2e&mpshare=1&scene=1&srcid=02078GE49qHtcnJmrgVAZWmk&sharer_shareinfo=2ae7a0dc553a9db4b5f9129b525918bc&sharer_shareinfo_first=2ae7a0dc553a9db4b5f9129b525918bc)

