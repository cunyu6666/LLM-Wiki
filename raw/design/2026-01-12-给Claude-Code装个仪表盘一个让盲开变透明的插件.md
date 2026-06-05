---
id: "7410321638408847670"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI1ODkyMTE1Mw==&mid=2247484441&idx=1&sn=28cf99b7d6a05836eb77d6bb8cca3080&chksm=ebca29446b0fb3730cc405aeccc49625a1b21a3d334aa3630ea825917f82e84dffe6ae582c35&mpshare=1&scene=1&srcid=0112nyDYxw2UyWWolnoVwcKT&sharer_shareinfo=a3197cffd213d17c6977d69f7c4fecb5&sharer_shareinfo_first=a3197cffd213d17c6977d69f7c4fecb5
author: "AI探路者 AIGC胶囊"
collected: 2026-01-12
tags: []
---

# 给Claude Code装个仪表盘：一个让"盲开"变透明的插件

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1ODkyMTE1Mw==&mid=2247484441&idx=1) · AI探路者 AIGC胶囊


用Claude Code有段时间了，不得不吐槽一个问题：它的交互体验真的很盲盒。

上周让它重构一个模块，我就盯着终端看了20分钟，黑底白字，代码刷屏，然后就是等。

等什么？不知道。

它在干什么？不知道。

Context用了多少？不知道。

哪个Agent在工作？也不知道。

就像开一辆没仪表盘的车，你知道它在跑，但不知道速度、油量、转速，甚至不知道它是不是已经抛锚了。

这种"盲开"的感觉，挺让人焦虑。

特别是处理复杂任务的时候。你让Claude Code起几个子Agent并行重构，它确实在干活，但你只能猜：它卡了吗？Context快炸了吗？那个Agent读文件怎么读了10分钟？

这种不可控感，确实消耗耐心。

直到发现了一个插件。

### 一个务实的解决方案

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F5EZ1TshXkh6XhjZVNwibPAIRqlndwDeA147ic9kmnkBcsaVqfRvGzia0s920RH5bEnFLfG56NHeibqrjcNunRDZ0ibw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0 "null")  

claude-hud，就是给Claude Code装个抬头显示器（Head-Up Display）。

开发者jarrodwatts在GitHub上维护，1k+ stars。核心思路很简单：在终端底部加一行状态栏，把关键信息实时展示出来。

这个设计没改变Claude Code的工作方式，也没搞复杂的GUI，就是用一行状态栏，把你原本"盲猜"的信息直接show出来。

它很轻量，通过Claude Code的statusline API工作，不需要额外的tmux或者独立窗口。

更重要的是不干扰工作流。该敲命令敲命令，该看代码看代码，状态栏就在那里，需要的时候瞥一眼就行。

那它到底能看什么？

### 四个核心功能

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F5EZ1TshXkh6XhjZVNwibPAIRqlndwDeA1ibXicjicrwq6RibpnXNPic1JBXQiamvuUfcpkX22RHgyh5QURN7CTIK9SXEQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1 "null")  

### 1. Context健康度

这个我觉得最实用。

用可视化进度条实时显示当前会话占用了多少Context Window，从绿到黄到红，颜色编码很直观。

它的原理是通过statusline API获取当前token使用量，然后按模型的上下文窗口（比如Claude 3.5 Sonnet是200K tokens）计算占用率：

- • 绿色：0-60%，随便用
- • 黄色：60-85%，注意一下
- • 红色：85%+，该清理了

以前你得靠经验猜Claude是不是快忘事了，现在看一眼进度条就知道。红了就该介入，输入/clear或者/compact。

**关于清理命令** ：

- • /clear：彻底清空会话，适合换话题或者开新任务
- • /compact：压缩保留关键信息，适合继续当前项目

我个人更喜欢/clear，因为/compact有时候会保留一些不太重要的东西，但如果你在做长期项目需要保持连贯性，/compact能派上用场。看具体场景。

### 2. 工具活动监控

Claude到底在干什么，以前你只能看结果，现在HUD能告诉你过程。

状态栏会显示：

- • 正在读哪个文件（Read工具）
- • 正在搜索什么关键词（Glob工具）
- • 正在执行什么命令（Bash工具）
- • 已完成的操作统计（✓ Read ×3 \| ✓ Edit ×1）

这个监控的作用是防止你傻等，结果Claude Code自己卡半路了。

举个例子：上周我调试一个CI/CD问题，让Claude Code跑测试套件。大概要20多分钟。没HUD的话，我就只能干等，心里嘀咕"它是不是卡了"。

有了HUD，能实时看到它在执行哪个测试文件，跑到第几个用例。虽然还是要等，但至少知道进度，焦虑感会少很多。

### 3. Agent状态追踪

任务复杂时，Claude会分派多个子Agent并行工作，HUD会显示：

- • Agent类型（Explore、Research、Code等）
- • 当前任务描述
- • 已运行时间

比如：

    ✓ Explore: Explore home directory structure (5s)
    ✓ open-source-librarian: Research React hooks patterns (2s)

这个监控挺有用的。我遇到过某个Agent一直在"Read files"，读个不停。这时候你就知道，可能是Context太大了，或者文件结构太复杂，需要介入调整。

### 4. Todo进度条

Claude规划的Todo List会变成实时进度条：

    ✓ All todos complete (5/5)

说实话，这个功能确实有点爽。每次看到所有Todo打勾，多少会有点成就感。

但它不只是让你爽，还有实战价值。比如看到某个Todo一直卡着不动，你就知道可能需要手动介入了。

### 安装步骤

官方文档给的步骤很清楚\[\^4\]：

1. 官方README: https://github.com/jarrodwatts/claude-hud ↩︎

在Claude Code终端里依次输入：

**第一步：添加marketplace**

    /plugin marketplace add jarrodwatts/claude-hud

**第二步：安装插件**

    /plugin install claude-hud

**第三步：初始化配置**

    /claude-hud:setup

终端底部马上就会出现状态栏，不需要重启。

第一次用的时候，感觉还行。状态栏信息密度控制得不错：

- • 左边：模型型号、订阅类型（Pro/Max/Team）、使用率
- • 中间：Context进度条、项目路径、Git分支、配置数量
- • 右边：运行时长、工具活动、Agent状态、Todo进度

你最关心的信息，基本都在了。

### 踩过的坑

用了一段时间，说几个坑：

### 坑1：终端兼容性

HUD依赖statusline API，某些终端可能显示有问题。

我在macOS的iTerm2和VS Code内置终端上用得挺好，但在Windows的CMD里试了一下，状态栏有点乱码。

如果你遇到显示问题，可以：

1.
   1. 换个终端试试（推荐iTerm2、Warp、VS Code Terminal）
2.
   2. 调整配置文件~/.claude/plugins/claude-hud/config.json里的layout选项

### 坑2：小屏幕问题

状态栏会占用一行高度（如果有tool/agent/todo活动，可能占2-3行）。

13寸笔记本用起来有点挤。如果你屏幕小，可以在配置里关掉一些不太需要的显示项：

    {
      "display":{
        "showModel":true,
        "showContextBar":true,
        "showDuration":false,// 关掉运行时长
        "showUsage":false,     // 关掉使用率
        "showTools":true,
        "showAgents":true,
        "showTodos":true
    }
    }

### 坑3：使用率显示限制

使用率功能（5h: 25% \| 7d: 85%）只对Pro/Max/Team订阅有效。

如果你用API Key模式（按token付费），这个功能不会显示，因为API用户没有rate limit，是pay-per-token的计费方式。

如果你是订阅用户但看不到使用率，检查：

- • 确认已登录（不是用API Key）
- • 确认配置里display.showUsage不是false

### 坑4：刷新频率

官方文档没明说刷新频率，我估计是几百毫秒一次（应该在300-500ms左右）。

大部分情况下不会有性能问题，但如果你在处理超大型项目（几千个文件），频繁刷新可能会有点卡。

暂时没找到调整刷新频率的配置项，如果遇到性能问题，可能需要去GitHub提issue。

### 说说实际感受

用了一段时间，总结一下：

**简单任务不需要装**

如果你只是偶尔让Claude Code写个小函数、改个bug，HUD没什么必要。任务短，反馈快，有没有可视化差别不大。

**复杂任务建议装**

但如果你经常干这些事：

- • 重构模块
- • 调试CI/CD
- • 多文件并行操作
- • 长时间会话（30分钟+）

HUD能帮上忙。至少你知道它在干什么，不用瞎猜。

**Context管理更直观了**

HUD的Context进度条挺有用，但说到底，工具是辅助，关键还是你的习惯：

- • 看到红色就清理
- • 别无限制往context里塞东西
- • 该compact就compact，该clear就clear

我之前遇到过好几次，让Claude Code处理复杂任务，它突然就开始答非所问，一看Context进度条都快满了。清一下，马上就好。

HUD的价值就在这：让你知道发生了什么。不然你只能猜，猜错了就浪费时间。

### 值不值得装

claude-hud不是什么革命性工具，它没给Claude Code增加新功能，只是把那些本来就有、但你看不见的信息，用很轻量的方式展示出来。

但就是这个简单的展示，让体验从"盲盒"变成了"透明"。

感觉是：重度用户值得装。效率不会翻倍，但体验确实舒服不少。

毕竟，开车还是要看仪表盘的。

你用Claude Code遇到过什么坑？评论区聊聊👇

谢谢你读我的文章。  
能看到这里的都是凤毛麟角的存在！  
如果觉得不错，随手点个赞、在看、转发三连吧\~  
如果想第一时间收到推送，也可以给我个星标⭐


![](https://image.cubox.pro/cardImg/2jjatm9zc1s6qww37nf4bwd5hu7azc5jzzbzbn2alvwwhp8szc?imageMogr2/quality/90/ignore-error/1)

**AIGC胶囊**

探索AI前沿，分享实用工具与应用经验！AIGC 胶囊为您带来最新AI技术动态、开发技巧及日常生活中的智能应用，助力您轻松驾驭智能时代。关注我们，捕捉AI的每一次脉动！

80篇原创内容

<br />

公众号  

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1ODkyMTE1Mw==&mid=2247484441&idx=1)
