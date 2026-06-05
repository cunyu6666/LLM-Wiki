---
id: "7429818021205508874"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzk0MzM1MDQ3Ng==&mid=2247492771&idx=1&sn=8577c1729007c18d8aa0b7171534e992&chksm=c29502167494fe086e46b2b8f1a5bb23667f130feb55166b58e1066baf1050a11134693d2560&mpshare=1&scene=1&srcid=0307NcjOeVg0K2akX52KJ0eb&sharer_shareinfo=951d12f04bba4b93905553f3cd5d396d&sharer_shareinfo_first=951d12f04bba4b93905553f3cd5d396d
author: "AI智能体入门 AI智能体入门"
collected: 2026-03-07
tags: []
---

# Agent View 开源工具，一个界面搞定多个 AI 编程助手管理！

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0MzM1MDQ3Ng==&mid=2247492771&idx=1) · AI智能体入门 AI智能体入门


同时开着好几个 AI 编程助手， 一个终端跑 Claude Code，另一个塞了 Gemini CLI，旁边还挂着个 OpenCode...... 结果人变成「调度中心」，窗口切来切去，看谁在跑、谁在等输入，稍微一走神，哪边卡住了都不知道。

这种「人肉 Agent 调度」，说实话，挺折磨人的。 我前段时间也受不了这种混乱状态，开始到处找有没有「统一控制面板」， 结果就翻出来了今天这位主角------Agent View。

它的定位很简单粗暴： 给所有 AI 编程助手搞一个「中央空调面板」， 所有会话、所有任务，全塞到一个界面里统一管。 底层基于 tmux 搭的，轻量但够狠。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F3rHuKstI89WqHTiaW06tr5zGiawRmRY0Tyibqf3UtCtKiaCKVz4mmzfsG1rKzB2I5xAxReiav0p91RY5aj3Cjs5yibSMjDPHoc0z4qfq5JsZbFaJw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

先说玩法。 Agent View 本质是一个会话管理器，专门给这些命令行 AI 工具打工： Claude Code、Gemini CLI、OpenCode、Codex CLI 这些主流选手都支持， 如果你有自己用 node / python 写的小工具，也能接进来。

效果就是： 原来你要开 N 个终端窗口， 现在只需要开一个 Agent View 界面， 每个 AI 助手变成一个「会话格子」， 状态、日志都规整地排在你面前。

它最爽的点，是那个实时状态监控面板。 每个智能体会标明当前状态：运行中、等待输入、还是空闲。 哪怕你在看代码，不盯终端， 任务跑完了、要你输入了，Agent View 也会主动「喊你」。

以前写代码经常出现这种画面： 一边 Debug，一边想「刚才那个命令跑完没」， 切过去一看，要么早就报错停在那，要么早就跑完在等你， 这波时间浪费，真的纯属信息不同步。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F3rHuKstI89U3Q50xkIicTvAS8dDHMU7qdLBCaNYtS67MeHOCWCyXfIHwQloNzph9rjXZhwPrZC3ungkM7ydaleUy0mn0CFgdwptmbDYcEZEI%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

有了 Agent View 之后，心里那条时间线会清晰很多： 哪个任务还在转，哪个已经结束， 哪个在疯狂吐日志，哪个安静地等你下一条指令， 不用满屏 Alt+Tab，眼睛也轻松不少。

更细节一点，它跟 Git 也做了点小勾搭。 Agent View 支持 Git Worktree 集成， 可以给每个会话自动搞一套独立工作树。 你在不同 Agent 会话里折腾不同功能分支，主仓库依然干干净净。

这对经常一边修 bug、一边尝试新特性的人太友好了。 以前同一仓库塞一堆本地分支，切来切去容易搞混， 现在直接「一会话一工作树」，物理隔离，脑子也不容易乱。

操作方式也完全是「重度键盘党友好型」。 创建会话、停止、重启、删除，全部都有快捷键， 用熟了以后，基本不需要碰鼠标。 那种「指尖飞舞，AI 跟着你跑」的感觉，还是挺香的。

而且因为底层是 tmux， 所有会话状态都是持久化的： 终端窗口关了、SSH 断了，甚至电脑重启， 你再连上来，之前那些 AI 会话还乖乖躺在那里。

对于常年在服务器上写后端、训练模型、跑脚本的同学来说， 这一点基本等于「心安」。 再也不用担心一个系统更新，把自己半夜跑的任务直接送走。

安装这块，Agent View 也算比较友好。 官方提供了一键安装脚本， 支持 macOS、Linux 和 WSL， 前提是你机器里先装好 Bun 运行时和 tmux。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F3rHuKstI89WxSL2keA3Jo6eialw4dslJk3BkIl8ct1uhdAERvK1siayq6MqAAeCiaScUYXWtgWP5kD4YI7HhGibSCiajAjqria4Zut73KMCfF8nKE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

整体体验下来，它更像是给一群 AI 编程助手加了一个「调度大脑」。 你原来用什么工具，现在依然用那些， 只是换了一个更体面、更可控的「使用姿势」。

当然，它也不是那种人人必装的软件。 如果你平时就偶尔用用一个 ChatGPT 网页写点小脚本， Agent View 对你来说可能有点「杀鸡用牛刀」。 但只要你每天都在命令行里跟多个 AI 辅助工具打交道， 这个东西，很有机会变成你的主力生产力工具之一。

简单帮你归个类： 如果你 ------ 经常跑长任务、频繁来回切窗口确认结果； 如果你 ------ 同时操作多个项目、多个分支，经常被工作区搞乱； 如果你 ------ 爱用键盘、讨厌鼠标到处点； 那 Agent View 这波操作，我真觉得可以一试。

你现在写代码的时候，都在用哪家 AI 助手？ 有没有那种「窗口开到怀疑人生」的瞬间？ 欢迎在评论区聊聊，顺便分享下你的一套终端工作流， 说不定下一篇就来盘一盘「程序员如何把命令行用出调度中心既视感」\~


GitHub地址：github.com/frayo44/agent-view

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F4CibHF60ZY6t3p4mHiamxXT6oPA0YtOUW7VwOfYfBEibNTXibhSaP5DAmpmSmVp0E3aCRCz6zpvNmmJjyX9ylqm9bw%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**AI智能体入门**

回复：ai，领取AI智能体入门教程。分享AI智能体搭建、智能体工具推荐、智能体应用案例、自动化工作流设计、AI助手开发、AI任务管理、LangChain教程、Agent构建教程、AI+编程教程。

158篇原创内容

<br />

公众号  

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0MzM1MDQ3Ng==&mid=2247492771&idx=1)
