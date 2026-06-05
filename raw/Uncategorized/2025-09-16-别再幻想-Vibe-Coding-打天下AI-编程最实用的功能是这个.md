---
id: "7367492851699025249"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&mid=2650732566&idx=1&sn=3e90133ccd0308fff95e77335af20996&chksm=bfa38640de701e2b760e942f07bb2369bdd1912b9010b0ff81c30cf109ebfd0fbd17433fc1b1&mpshare=1&scene=1&srcid=0916K7m0RHmdEFHDFyGwtMTo&sharer_shareinfo=488a35c508e78220181c7e1499a593b2&sharer_shareinfo_first=488a35c508e78220181c7e1499a593b2
author: "池建强 MacTalk"
collected: 2025-09-16
tags: []
---

# 别再幻想 Vibe Coding 打天下，AI 编程最实用的功能是这个

# 别再幻想 Vibe Coding 打天下，AI 编程最实用的功能是这个

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&mid=2650732566&idx=1&sn=3e90133ccd0308fff95e77335af20996&chksm=bfa38640de701e2b760e942f07bb2369bdd1912b9010b0ff81c30cf109ebfd0fbd17433fc1b1&mpshare=1&scene=1&srcid=0916K7m0RHmdEFHDFyGwtMTo&sharer_shareinfo=488a35c508e78220181c7e1499a593b2&sharer_shareinfo_first=488a35c508e78220181c7e1499a593b2)池建强 MacTalk

如果你是个程序员，肯定注意到了这两年 AI 编程领域发生了翻天覆地的变化：大家先是讨论 Copilot 是不是"AI 编程的终极形态"，后来各个 AI IDE 层出不穷。年初，大家讨论的重点逐渐转向一个词------Vibe Coding。

最早提出这个概念的是 OpenAI 的创始成员 Andrej Karpathy，他曾在 OpenAI 和特斯拉之间来回溜达，并把 AI 编程比作一种有节奏、有氛围的"协作"，程序员只要在编辑器里像指挥家一样挥动手指，AI 就能自动铺陈出一整段代码，宛如魔法。

但魔法并不适合所有场景，8 月底 Andrej 改变了口径，他发文表示，不要幻想有一个万能的 AI 工具能解决所有编程问题，更可行的做法是建立一个结构，让不同的工具在不同场景各司其职，像接力赛一样完成开发任务。

是的，当今世界大部分用户使用的软件，依然是专业软件工程师写出来的，他们不做 demo，也不演示产品，而是在生产线上创造千百万人使用的软件和服务。Andrej 还说了，他使用频率最高的 AI 编程能力是"代码补全"。

对，工程师们写业务逻辑和算法、调试 Bug、改函数签名、重命名变量，在庞大的仓库中做些不起眼的工作------这些事好像一点也不"魔法"，但 AI 真的能帮上忙啊。

在字节跳动出品的 IDE Trae 里，这样的功能叫做 Cue，它在这个看似"基础和简单"的领域下足了功夫。

我之前就给大家介绍过 Trae，那么 Cue 是什么？如果你用过 GitHub Copilot，大概能理解 Cue 的核心功能：代码补全、多行修改、修改点预测、修改点跳转、智能导入和智能重命名功能等等。

不过，在 Trae 这个 IDE 里，Cue 不只是补全和重构代码，它试图重构的是你整个编程动作：从预测你要改哪一行，到给出多行编辑建议，再到智能导入、智能重命名，乃至仓库级别的跳转编辑------把一个个散落在 IDE 里的点串成珍珠项链。

Cue 是今年 6 月发布的，叫做 Context Understanding Engine。这几个月 Trae 团队一直在迭代这个功能，目标很明确：让 AI 成为理解你上下文的伙伴。

这是一个非常低调的工具，它的入口我用了三月才知道：在 IDE 的右下角，点击那个 tab 就可以看到这个窗口：一种更高级的代码辅助体验。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FJuJRyjO2zca6goDopVK8I0ZCbibOozqI0XbftYicI1zvGThcCSiaf7RSEvAaKgFZmqwLLLKUibyCTx8uicAZYb9NgBA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

1

2025 年 AI 编程工具进入"百花齐放"的阶段，工具越做越全能，模型越来越强，体验变得越来越好了吗？未必。

我前几天写过一段话，为什么 Vibe Coding 没有自己写代码快乐？写过程序的人可能会知道，编程写代码是会让我们进入心流状态的：设计系统架构、数据结构、把逻辑画出来、UI 摆上，打开 IDE，摆好机械键盘，把这些东西噼噼啪啪敲进光标闪烁的屏幕里。点个 run，发现有问题，改为 debug，哦，卡住了，看看哪里出了问题，原来出了 Exception，try catch，打断点，单步调试，一点点逼近答案，解了。最后程序跃然屏幕之上。

其实很多工程师喜欢编程，喜欢的是这个透明的心流过程。这段话在社交媒体上超过 10 万阅读，获得几百个点赞和转发，看起来工程师感受有点趋同，哈哈。

很多开发者都试过 Vibe Coding，但最后研发生产系统，用的最多的还是智能代码工具，我们公司就是这样，毕竟生产力场景太复杂了。

一个典型的例子是这样：

你打开一个老项目，准备把业务逻辑里的 UserValidator 改成新的 IdentityChecker。这个操作可能涉及十几个文件，几十处位置，甚至在不同的仓库里。你希望 AI 能帮你找出来并全部替换，但你又担心它错改漏改，Vibe Coding 在这里帮不上忙，但 Cue 能。

Cue 不会用生成的大段代码吓你一跳，而是低调地在你每一次按下回车、每一次光标跳转、每一次变量命名时出现，并提出可行建议。

2

我已经使用了 Trae 一段时间，喜欢它的 SOLO 模式和 Agent 编程，我喜欢它对 MCP 的兼容性，但我觉得对程序员价值最大的是：Cue。

和很多墨问用户聊天，他们已经是忠实的 Trae 用户了，但并不知道 Cue 是怎么回事，或者说，Cue 是那种你一开始感知不到，但用久了却离不开的工具。就像程序员习惯了传统 IDE 自动补全之后，再也回不到手写函数方法一样。

工程师日常使用最多的几个功能都是 Cue 提供的：

代码补全：聪明但不冒进

Cue 的代码补全不会像 Copilot 那样在你打完一行函数名之后就展开整整 20 行实现，而是遵循「先判断意图，再决定补多少」的策略。它更多时候是"灰色提示"的方式，嵌在代码中，一看就知道补的是啥，按 Tab 接收就好。

这背后其实是对上下文理解能力的体现。Cue 的新版本融合了代码续写和已有代码编辑能力，在同一个模型中判断你的意图，然后以最小代价给出最优建议。

多行修改：不是续写，是改写

你改了个函数名，它就会提示你，"是不是要把其他几个地方也一并改了？"然后带你跳过去，一键确认，全部替换。这种操作在维护大型项目时太常见了------以前我们靠搜索，靠计算，现在靠 AI 自动预判位置。

Cue 的编辑能力，不是基于 Token 的逐字符生成，而是采用了 Diff 模型。也就是说，它天生就是为「修改」而生的，而非「续写」。这个重要的差异能力，也解释了为什么在用 Cue 改代码时，整体体验快速而准确。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FJuJRyjO2zca6goDopVK8I0ZCbibOozqI0Ff5GsUP5b6zo0lHl7CgcibpABEadE5zcUu9Y9PFh3fxJtZ42zRic6gCQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D1)

修改点预测与跳转：做手指的延伸

Cue 通过用户最近的编辑行为、光标停留位置、浏览轨迹，判断你下一步可能修改的位置。这种预测能力，让它有能力在你意识到"还需要改哪些地方"之前，就提醒你"这几个地方也要改"。

在大型仓库中，这种基于意图的跳转，明显比全局搜索来得更聪明、更节省心力。

3

我大部分时候都在使用 Trae 国际版，模型更多，还支持 Auto 模式和 Max 模式，产品更新节奏很快，经常一周一更甚至两更。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FJuJRyjO2zca6goDopVK8I0ZCbibOozqI0RFl7SrfsqC4ic5wU5uvzlgIicujlia1bSKib3Eeia8cVYEicPSpFZdpd4otA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

对应的 Cue 更新节奏也很快很快。从 6 月底上线到最近的更新，几乎重写了底层的模型和延迟控制逻辑。Cue 变得更聪明了：

更强的 cue-fusion 模型

这个模型融合了续写和改写能力，从原本两个独立的模块，统一为一个模型处理。它基于真实用户的编码轨迹优化了推荐策略，用的是 SFT 数据集加 MoE 架构，延迟也控制得更好。

在我的实际体验中，Cue 的响应速度明显快于我之前试用过的一些国产 Copilot 替代品。官方说端到端延迟已经降到 700ms 以内，甚至在某些测试中做到 500ms。

智能上下文增强

Cue 不是只看你当前窗口的一两行代码，而是把你的操作轨迹，包括浏览记录、编辑历史、LSP 返回的符号信息全部纳入"理解范围"。

它甚至能知道你在前一个文件里看了哪个类，然后在当前文件提示你"是不是要用那个方法？"这种上下文关联感，是传统补全工具无法做到的。

Auto-Import 与 Smart-Rename

对于 Python、TypeScript、Golang 等语言，Cue 能自动判断你是否使用了未导入的包，并自动补上 import 语句。同时，支持跨文件的智能重命名，准确识别函数、变量、类名修改点，避免你手动全局替换带来的错误。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FJuJRyjO2zca6goDopVK8I0ZCbibOozqI0rniaKZhsMs4x5mtPQTTNQb4ib1ZQficqQJqTASLu3ugcT0NpjYz9GqjXA%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D3)

4

最近国内 AI IDE 赛道真的很卷啊，不过代码补全这件事上，我挺看好 Cue 的。如果给它排个名，从我个人的体验来说，Cue 在国产 IDE 里算是做得最好的。

我们常说做产品要"提升用户体验"，但这种话说多了也会变成空话。我和墨问的研发团队聊天，他们给了 Cue 这个工具一句很朴素的评价：

使用 Cue 之后，我少了很多中断动作，最近一个月我都没有暂停这个服务。

怎么个流畅法呢，我们的 CTO 大师告诉我，使用 Cue，你不再需要：

* 停下来手动加 import

* 在几个文件中跳转查找变量名

* 担心改了函数名后漏掉调用点

* 用肉眼判断"这个修改是不是安全的"

Cue 就像默默为你处理"地板工程"的 AI 工程师，专注于处理代码中那些琐碎却必不可少的基础工作。这也正好呼应了 Trae 的品牌理念：The Real AI Engineer

AI 编程 IDE 发展到现在，一方面是帮助小白用户 Vibe Coiding，实现他们的产品梦和 MVP；另一方面，也是现阶段最有价值的，真正帮开发者提升效率，构建线上的生产系统，按周按月，一次次迭代有成百上千万用户使用的产品。

Cue 是 Trae 的重要组成部分，也是被使用最多的工具套件，它不是用"AI 写整个项目"，而是专注解决那些琐碎但关键的开发场景。

真正写线上代码的工程师都知道，写代码本来就是 95% 的重复劳动 + 5% 的创造力飞跃。

Cue 就是那个把 95% 打理好，让你专注于 5% 创造的工具。可以用起来了，朋友们。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&mid=2650732566&idx=1&sn=3e90133ccd0308fff95e77335af20996&chksm=bfa38640de701e2b760e942f07bb2369bdd1912b9010b0ff81c30cf109ebfd0fbd17433fc1b1&mpshare=1&scene=1&srcid=0916K7m0RHmdEFHDFyGwtMTo&sharer_shareinfo=488a35c508e78220181c7e1499a593b2&sharer_shareinfo_first=488a35c508e78220181c7e1499a593b2)

