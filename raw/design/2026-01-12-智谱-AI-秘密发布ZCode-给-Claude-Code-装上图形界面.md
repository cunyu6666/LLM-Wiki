---
id: "7410406928238510508"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI1ODkyMTE1Mw==&mid=2247484237&idx=1&sn=ead3408a57c2bafc872257b460c676d4&chksm=ebb3f361cbd4c63e08a5317bccc4d6f8bf29285a26afb395ed60e0cd2918ca8fc584e4a9afd9&mpshare=1&scene=1&srcid=0112u0cSx4X6iu7mSKugTpgQ&sharer_shareinfo=34e6b9c9d3cfd1b497a714b9953b5728&sharer_shareinfo_first=34e6b9c9d3cfd1b497a714b9953b5728
author: "AI探路者 AIGC胶囊"
collected: 2026-01-12
tags: []
---

# 智谱 AI 秘密发布ZCode ：给 Claude Code 装上图形界面

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1ODkyMTE1Mw==&mid=2247484237&idx=1) · AI探路者 AIGC胶囊


智谱昨天推出了ZCode 这个轻量级的编程工具，它的核心优势，它不仅集成了 Claude Code CLI、OpenAI Codex CLI、Google Gemini CLI 三大主流编程 Agent 工具，而且原生、完整地保留了它们的超强 Agent 能力。 感兴趣的可以直接去官网下载体验，官网地址：https://zcode-ai.com

现在开发圈最火的 AI 编程工具是Claude Code CLI，他的Agent能力很强，但是它的这个配置很复杂，很多人想尝试使用Claude Code CLI，但是都卡在这个第一步的配置上。

使用 ZCode，不会损失任何「直接用原生 CLI」时的编程品质，却能获得远超命令行时代的编程体验：统一可视化界面、多模型调度、自动版本管理，带来体验与效率的双重飞跃。

## 界面介绍

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmILnokMic56XYGfuBoPZex4XGXIrcC5TlD3SAZVEUic9bPb6DfxUjNgvQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0 "null")  

Z Code 应用界面主要可分为4个区域：

1.
   1. 顶部导航栏：主要是管理窗口和文件夹
2.
   2. 工具选择栏：功能是切换内置的CLI编程工具
3.
   3. 会话面板：核心功能是展示用户和Agent的对话和Agent执行过程；以及model、mcp 等的配置
4.
   4. 预览面板：主要作用是展开/隐藏右侧预览面板（代码审核、浏览器预览）

### 顶部导航栏

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmSqArjY8FzPIpdDABKCicXeCHZCtd7McOgO8F71mYHrtPONSCNiaAicDbg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1 "null")顶部导航栏

通过顶部工具栏的按钮可以打开和关闭预览区的panel以及终端的显示和关闭。

### 工具选择栏

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmLYN6egp1Ll9jnoavhLSZYekxepoe8j5o43gFQJYsibMvdCTwsP1aeCg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2 "null")工具栏切换CLI

工具栏主要提供的功能是切换不同的 CLI 工具，目前ZCode 默认集成的有Claude Code CLI、Codex CLI、Gemini CLI，当然通过点击"+"可以增加这三个CLI 的实例，相当于实现了某个CLI 的多开，可以在一个项目上同时使用这三个CLI + git worktree，实现三个CLI agent 同时开工服务一个项目的场景；也可以多开某一个CLI的实例实现同样的效果。

### 会话面板

#### 1 模式切换

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xma5XTozNERn2KCfVaibcq77zsdPWgU778zLDbprrqp9uUzCSPJRbW6Dg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3 "null")会话区切换模式

目前默认的模式有:

- • Always Ask: 每次阅读或修改文件或执行命令时都需要你的授权大模型才能继续执行，这是权限最小的模式，默认是这种模式
- • Accept Edits: 在以上权限的基础上放开了文件编辑的权限，模型直接编辑不在需要你的授权
- • Plan Mode: 这与权限无关，是Agent ，是任务执行的模式，在这种模式下执行任务先要规划，想好和输出规划并得到你的认可后，才动手执行
- • Bypass Permissions: 一次授权所有的权限，大模型能做任何事情都不需要你的授权了，这种模式比较危险，最好是在sanbox 中使用。

#### 2 模型切换

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmcUXmic7ZxAvWTTB4wm8l8icvQticFdsVLNFI75S8Hn7IV8kfF4ZhoIlCQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4 "null")会话区模型切换

实现不同模型的切换

#### 3 模型配置

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmMC82ywibM5PWdAdqZOtYdgk2S8lPQjrVD2YW7e4Yibx1mstYJVobJoRg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5 "null")配置模型

先选定模型供应商，内置的几个模型供应商的URL 已经内置不用单独输入，只需要输入模型API Key就可以了。前提是需要提前充值或者购买 GLM 的 Coding 套餐 ：  
https://www.bigmodel.cn/glm-coding?ic=F0LYA0JJUP ，当然购买海外版也是一样的 ：  
https://z.ai/subscribe?ic=RP34Q6GQVY

#### 4 MCP服务器配置

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmk2Njeh7ApxqsAhibcUBq4JHK3I12yeXBzRCMuWTiay1ibvMwVpYSPlMxg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6 "null")配置 MCP

如图所示，Zcode 内置了不少的MCP，也可以通过点击"Add MCP Server"来配置其他的 MCP Server。

#### 5 命令配置

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmEDJkPpSlOrHaAwoXzeKcs19Mfzp0WmcTBYrAH7vEic5AAyiaiakTzgVAA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7 "null")配置Command

这个有点像Claude Code CLI 里面的 斜杠命令，在Claude Code CLI 中可以通过/plugin 命令进行添加。ZCode 可以填写命令名称、描述以及 prompt内容完成对一个Command 的定义。Command 的质量与prompt 紧密相关。

### 预览面板

#### 文件预览区

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmp6tg4SVr3xwUZr3ODdzrF9a2lAQwtLh7eRAoGjrxVsK5PtS4EWovug%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8 "null")文件预览区

可以看到整个工程的目录结构，点击任意的文件，可以直接看到这个文件的内容，ZCode 应该是集成的文本编辑器对大部分的开发文件类型支持都挺好的，基本上点击了很多文件都支持预览。

#### 终端预览区

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xmrK9GW2W4SFXUoSDZghM5hJKoAeV7Nz6l3d2okzib889vYSZpCMUUmoA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9 "null")终端预览区

可以一边看大模型的输出，一边通过这个终端确认一些与大模型执行相关的工作，不用在不同的工具之间来回切换。其实这点与字节TRAE 比较类似。

#### git commit 预览区

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6cP0ZeOWMJkXe9ZUQ2s6xm7SBp5JDcp6sNmXF1he8Qgplp8gbWJcMVNibyVSHcJiaSn5Yt7WF70Mzg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D10 "null")git commit 预览区

这个区域是管理、审查和回顾修改状态以及提交状态相关的信息。

## ZCode有何不同

### 1. 是个技术人都能上手，不再只限"硬核玩家"

那几个 CLI 工具强是强，但前提是你得爱折腾终端，环境配置就能劝退一波人。

ZCode 换了个思路：大脑还是那个强力的大脑，但入口变成了傻瓜式。只要你有 API Key，哪怕你是前端、设计转行或者产品经理，也能无痛参与 AI 编程。它把"写代码"这件事的入场券，发给了更多人。

### 2. 告别"盲打"，给你真正的可视化工作台

用命令行最痛苦的是什么？是一行行滚动的文本。你得在脑子里硬构建项目结构。

ZCode 直接把这一套拆开了：左边跟 AI 聊天，右边就是文件树和编辑器。AI 改了哪行代码，Diff 视图里标得清清楚楚。你能看见代码是怎么"长"出来的，而不是对着黑框瞎猜。

### 3. 自带"后悔药"，想怎么试错都行

在命令行里用 AI，忘了 git commit 就是灾难，改崩了很难救。

ZCode 给每一轮对话都加了自动快照。聊错了？改偏了？一键回滚到上一轮。这种"随时能撤回"的安全感，才让你真正敢放手让 AI 去写核心逻辑。

### 4. 从"个人黑科技"变成"团队资产"

命令行里的操作是碎片的，只有你自己知道发生了什么。

ZCode 把整个对话、修改记录和项目结构绑在一起。这代码是怎么一步步迭代出来的，全都有迹可循。以后做复盘、搞交接，这就是现成的文档，而不是一堆只有天知道怎么跑起来的烂代码。

### 5. 真正的模型调度中枢

不用再为了切模型去换工具、改配置。

在 ZCode 里，模型随便切，API Key 随便配。今天用 Claude 写逻辑，明天用 GPT 润色，还能挂上 MCP 插件去联网、去识图。它不只是个壳，它是一个能统筹所有 AI 能力的超级中枢。

## 最后

在三大 CLI 已经证明 Agent 能力足够强大的前提下，ZCode 提供的，不是「再造一个新轮子」，而是一款轻量级 AI IDE 编辑器，它通过「将 Claude Code 等主流命令行工具可视化」，从而让这些能力真正落地到更多开发者和团队的统一工作台。既保留原生 CLI 的编程品质，又显著提升体验与工程可控性，这是它相对传统命令行工具最核心的差异点。

另外，官方还提供一份非常完整的使用指南： https://zhipu-ai.feishu.cn/wiki/VpgrwtBcyiU59zk9fMEcm2sFnee

**如果觉得这篇文章对你有启发，关注、点赞、分享三连就是对我最大的支持，谢谢～**

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1ODkyMTE1Mw==&mid=2247484237&idx=1)
