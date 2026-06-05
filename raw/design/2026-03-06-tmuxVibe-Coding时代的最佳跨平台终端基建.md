---
id: "7429519003204192509"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484912&idx=1&sn=ca66e27f6038a0dcfbd0ad8632b41c57&chksm=97085e2cb538ca390b324dbded2d1c3c2f915b1bec1431e318373717660d2ab175435657f61f&mpshare=1&scene=1&srcid=03065w1TezUtlPdyrqifgw0A&sharer_shareinfo=0d8cf47558ef8a5f2b16bc0eea946d66&sharer_shareinfo_first=0d8cf47558ef8a5f2b16bc0eea946d66
author: "鲁工 AI编程实验室"
collected: 2026-03-06
tags: []
---

# tmux，Vibe Coding时代的最佳跨平台终端基建

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484912&idx=1) · 鲁工 AI编程实验室

大家好，我是鲁工。

前段时间，我写了一篇关于Windows环境下使用Windows Terminal作为最佳Vibe Coding工具的文章，引起了不少读者的讨论：

> 来源: [Windows Terminal，也许是Claude Code用户的最佳终端选择](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484492&idx=1)

但这个只是针对Windows用户，对于跨平台用户，我想推荐一下tmux这款终端工具。

tmux这东西我几年前就接触过，当时觉得学习曲线太陡，没怎么深入。但2025年以来，Claude Code、Codex CLI、Gemini CLI这些AI编程CLI工具全面爆发，tmux突然变成了一个绕不开的基础设施。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FMHVsz9lwuhWUjsG9UQZCZDpOwnhiakXXbbzBk6YmQd1jMRZy7xG1iaYj7XJcw3I0ibPrmF0icE6rCeVnOicteWcUlpGbvMYm4TpyC75mGplwQzUk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

GitHub上42,600+ Stars，最新版本3.6a发布于2025年12月，2026年3月代码仓库还在持续更新。

https://github.com/tmux/tmux

这款2007年诞生的老工具，在Vibe Coding时代反而焕发了新的活力。

今天就简单聊一下tmux，以及它为什么成了AI编程的推荐标配工具。

### tmux简介

对tmux最直白的介绍，我觉得应该是：终端复用器（terminal multiplexer）。它让你在一个终端窗口里同时开多个终端，而且关掉窗口这些终端还在后台跑着。

tmux由Nicholas Marriott在2007年用C语言写的，最初是因为受不了GNU Screen的代码臃肿和配置语法。到现在快19年了，核心代码99%以上由两个人维护，项目代码风格高度一致。

tmux的结构分三层。最上面是Session（会话），一个会话里可以有多个Window（窗口，类似浏览器标签页），每个窗口又可以分成多个Pane（面板）。它采用客户端-服务器架构，tmux server作为独立进程运行，你的终端只是一个客户端。关掉客户端，server里一切正常。

这个架构设计，就是tmux的核心大杀器。

### AI编程为什么需要tmux

关键原因就是：CLI是目前AI编程的主要形式，而CLI工具又天然需要会话管理。

可能你有如下应用场景：用Claude Code做一次大规模代码重构，经常跑20分钟甚至更久。用Codex CLI并行跑多个Agent，每个Agent占一个终端。在服务器上跑Claude Code的headless模式批量处理任务，需要断线保护。这些场景，没有tmux加持的话很不好管理。

先说最刚需的：会话持久化。

在tmux里运行Claude Code，即使SSH断开、终端关闭，Claude Code进程依然在跑。重新attach到tmux会话后，Claude Code还保持在原来的思考状态，不需要用--resume重新加载上下文。有开发者实测过，在Mac上跑Claude Code做重构，然后合盖走人，用手机SSH回来tmux attach一下，Claude Code还在思考中。这种跨设备的无缝体验，只有tmux能给（我没Mac没自己测过，用Mac的读者可以测试下看看）。

再比如多Agent并行。

现在Vibe Coding的效率瓶颈，说白了就是你同时能跑几个Agent，虽然也有Git worktrees等并行方案，但还不够极致。tmux的分屏功能天然适合这个场景：一个面板跑主Agent做架构设计，旁边面板跑子Agent写前端，下面面板跑测试Agent。

更关键的是，Claude Code官方的Agent Teams功能直接用tmux管理多Agent会话。启用方式是设置环境变量：

    CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1


每个teammate就会运行在独立的tmux窗格中。换句话说，Anthropic自己都把tmux当成多Agent编程的标配基础设施来用。

社区也在往这个方向卷。2025到2026年间，围绕tmux + AI编程的专用工具涌现了10+个，dmux、NTM、Agent Deck、CCManager这些。Hacker News上有人分享同时运行30个Claude Code sessions的经验，全靠tmux撑着。

社区最推荐的多Agent方案是Git Worktree + tmux并行化。给每个Agent创建独立的git worktree，再在tmux中为每个worktree创建独立窗格，Agent之间完全隔离，不会互相覆盖代码。

还有一个场景是远程移动编程。tmux + SSH + Tailscale这个组合，让手机上AI编程成为现实。具体方案就是在Mac Mini或云服务器上跑Claude Code，Tailscale建VPN，手机装个Termius，SSH连上去tmux attach，随时随地写代码。

已经有不少开发者在实践这条路，有人写博客说这种体验"像2000年代早期那样编程"，但其实比那时候高效多了。因为你只需要盯着AI干活就行。

对比一下没有tmux的情况：SSH一断，Claude Code进程直接被杀，你得用--resume恢复对话，跑到一半的构建和测试全部丢失。有tmux的情况：SSH断了，一切照旧，重连之后tmux attach，完全恢复。这个差距在实际使用中是非常明显的。

### 快速上手tmux

安装特别简单。

    # macOSbrew install tmux# Ubuntu/Debiansudo apt install tmux


Windows用户走WSL2，先wsl --install装好Linux子系统，再在WSL里apt install tmux。

装好之后，记住这几个核心操作就够日常使用了。

tmux new -s coding，创建一个叫coding的会话。Ctrl+b d，从会话中分离，会话在后台继续跑。tmux attach -t coding，重新连回去（注意是先按Ctrl + b，松开后紧接着按d才有效，不要同时按Ctrl + b + d）。

分屏操作也很直观。Ctrl+b %左右分屏，Ctrl+b "上下分屏，Ctrl+b 方向键在面板间切换。如果想把某个面板临时放大到全屏看看，按Ctrl+b z，再按一次恢复。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FMHVsz9lwuhVYcYPaqg3nk4B4Fictj1apMUiauVicEibbWEs86omcxQiafDKqJxP8MN9slWicIwjLawyYagMvDoJYuzKPEjKibG8QGwkt3wwI9p6gbs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

到这一步，tmux的基本功就够用了。

这里有个点需要注意一下。Claude Code的后台任务快捷键也是Ctrl+B，和tmux的默认前缀键直接冲突了。在tmux里用Claude Code你会发现得按两次Ctrl+B才能触发后台任务。我的建议是改掉tmux的前缀键，在\~/.tmux.conf里加三行：

    unbind C-bset -g prefix C-abind C-a send-prefix


改成Ctrl+a之后就没有冲突了。

另外推荐装3个必备插件。先装TPM（Tmux Plugin Manager，插件管理器），一行命令搞定：

    git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm


    然后装tmux-resurrect（会话保存恢复，GitHub 14,000+ Stars）和tmux-continuum（自动保存）。这两个插件搭配使用，tmux server意外重启也能恢复之前的工作环境。在~/.tmux.conf里加上：


    set -g @plugin 'tmux-plugins/tpm'set -g @plugin 'tmux-plugins/tmux-resurrect'set -g @plugin 'tmux-plugins/tmux-continuum'set -g @continuum-restore 'on'run '~/.tmux/plugins/tpm/tpm'


再加一行set -g mouse on开启鼠标支持，就可以用鼠标点击切换面板、拖拽调整大小了。

主题推荐Catppuccin，目前最火的终端配色方案，颜值相当在线。

### tmux和其他终端工具比较

简单对比一下。Zellij是tmux最有潜力的竞品，Rust写的，开箱即用体验确实比tmux好，底部状态栏实时显示可用快捷键，新手友好很多。但是吧，它的内存占用是tmux的约13倍（80MB vs 6MB），还没到1.0正式版，远程服务器上的覆盖率也远不如tmux。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FMHVsz9lwuhWQxLXnXUt51URiaGz3JfmG4lGjJTaK0MdCLJO1iagumA69iaI6AspxyWqiaKuDj4qFhlHUaAGVybPLCw0IvajzOdbNGPBCl0bmWd4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

WezTerm和Kitty是终端模拟器，内置了分屏功能，本地开发用着挺方便。但它们不支持会话持久化和detach/attach，做不了SSH断线恢复。

个人觉得，如果你的工作流涉及SSH远程开发或者AI编程多Agent场景，tmux目前还是最优选择。纯本地开发的话，WezTerm或Kitty的内置分屏就够用了，看个人偏好。

tmux这款19年历史的老工具，在Vibe Coding时代找到了新的核心价值：会话持久化、多Agent编排、远程移动编程。这三个能力组合下使得tmux焕发新活力。如果你是跨平台CLI用户，那么可以尽快用起来了。

感谢您阅读我的文章。我是鲁工，九年AI算法老兵，AI全栈开发者，深耕AI编程赛道。欢迎关注，感兴趣的朋友也可以加我微信（louwill_）交个朋友。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F4lN1XOZshfekhSPOVhKyHjek97r6uIakcYsqZxEMvKBCYqOO6wGleHTNuz4sff6Xns2LDGah9Jb6c39iaOhvfpQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwxpic%23imgIndex%3D4)

\>/ 作者：鲁工

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484912&idx=1)
