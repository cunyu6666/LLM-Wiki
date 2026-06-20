---
type: note
description: "频道：AI Engineer (@aiDotEngineer)"
timestamp: 2026-06-20
---
# "Software Fundamentals Matter More Than Ever" — Matt Pocock

> **频道**：AI Engineer (@aiDotEngineer)  
> **链接**：[https://www.youtube.com/watch?v=v4F1gFy-hqg](https://www.youtube.com/watch?v=v4F1gFy-hqg)  
> **时长**：18 分 26 秒  
> **发布日期**：2026-04-23  
> **观看/点赞**：896,328 / 31,435  
> **字幕抓取日期**：2026-06-20  
> **字幕来源**：YouTube auto-generated (en)  
> **段落数**：120  
> **总字数**：约 3339 词 / 17860 字符

---

## 简介

AI coding tools are overhyped and powerful at the same time. Used well, they're extraordinary. Used badly, they'll bury you in spaghetti code faster than any human team could. The difference isn't the tool. It's the process. After 18 months of teaching developers to build with AI agents, Matt Pocock has watched the same patterns emerge: the devs who succeed aren't the ones who delegate everything or nothing. They're the ones who fall back on engineering fundamentals. In this talk, he shares the iterative process his students use to ship high-quality applications with AI agent swarms, and why the principles that make it work (ubiquitous language, vertical slices, TDD, deep modules) are decades-old ideas that didn't break. They got more important.

Speaker info:
- https://x.com/mattpocockuk
- https://www.linkedin.com/in/mapocock/

**标签**：`ai`, `ai engineer`, `ai engineering`, `software development`, `tech`, `startups`, `software architecture`, `machine learning`

---

## 信达雅中文翻译

> **演讲者**：Matt Pocock（AI Hero 创办人、TypeScript 布道者）  
> **原始语言**：英文 · **翻译**：Claude（手工译校）  
> **风格**：信、达、雅。技术名词保留英文原貌（TDD、DDD、vibe coding、
> ubiquitous language、plan mode、outrunning your headlights、deep module 等），
> 已修复 ASR 误识别（"Clojure Code" → "Claude Code"、"John Osterhout" → "John Ousterhout"、
> "AFK agent" → "AI agent"），补充完整专有名（mattpocock/skills）。
> 本节为人类易读版本，移除时间戳，按演讲逻辑分章整理。
> 完整带时间戳的英中对照见上一节。

### 一、开场：基本功比以往更重要

大家好。大会开得还顺利吧？嗯,诸位都还尽兴吗？嗯,很好。

棒极了。

我今天想对各位说一句话,希望对那些担心自己手艺在这个新时代一文不值的人,是个安慰:我认为,软件工程的基本功,如今比以往任何时候都更重要。

我是一名教师,最近在开一门课,叫《给真工程师的 Claude Code》。

名字够刺激吧。为了把这门课做出来,我得搭一套 AI 编程的教学大纲,简直是噩梦——因为这领域一天一个样,对吧？AI 是一个全新的范式。

按理说,我们得把老规矩全扔了,才能把新东西装进来。

于是圈子里冒出来一派,叫“规格即代码”派。它讲的是:你先写一份规格,描述清楚应用该怎么工作;然后让 AI 把规格变成代码。应用出问题了？回规格。你基本不用看代码,改规格,再跑一遍“编译器”,就又生出一堆代码。听过这套说法的请举手。

亲自试过的请把手留着。

好,我也试过。诸位可以放下了。

我的体验是:我跑一遍,尽量不去看代码——但我还是看了。先是跑出代码来,再跑一遍,代码变烂了;再来一遍,更烂;不停跑、不停跑,最后只剩一坨垃圾。

有同感的请举手。

对吧。这套不行。以为可以不管代码、让代码自己管自己,说白了就是 vibe coding 的另一种说法。

当时我并不信这套。我琢磨:怎么修这个“编译器”？怎么让它别每次都吐烂代码、甚至越吐越烂？于是我想,得用英文跟 LLM 讲清楚好代码长什么样。我翻出一本压箱底的老书——John Ousterhout 的《A Philosophy of Software Design》。

亚马逊上有,去买。

他对“烂代码”有个定义。

他叫它“复杂代码”。复杂,就是软件系统在结构层面任何让人难以理解、难以修改的东西。

所以烂代码库就是改不动的代码库。改一下就出 bug,那它就是烂的。好代码库,是好改的。

我心想:这个定义真漂亮。

再翻一本——The Pragmatic Programmer（《程序员修炼之道》）。亚马逊上有,去买。

里头有一整章讲“软件熵”。这正是我看到的现象。熵的意思是:事物天然会走向混乱,互相离散,直至崩塌。绝大多数软件系统也是这副德性——你每改一处,只想着这一处,不想整个系统的设计,代码库就一遍比一遍烂。我看到的正是这个。

“规格即代码”那一套——“反复跑编译器”——只会让代码越来越烂。

驱动“规格即代码”派的一个核心想法是:代码是廉价的。听过“代码很便宜”这句话的请举手。嗯,听过。

但我觉得这不对。

代码并不廉价。事实上,烂代码是有史以来最贵的。

因为一旦代码库改不动,你就拿不到 AI 带来的红利——AI 在好代码库上表现其实非常、非常好。

所以好代码库比以前更值钱,软件工程的基本功比以前更值钱。

这是今天演讲的论点。

咱们来点实际的。

我会聊几种你可能踩过、或者还没踩过的 AI 失败模式,以及怎么靠翻老书、用老一套好的工程实践去躲过它们。听起来如何？

### 二、失败模式一：AI 做了不是我要的（建议：用 Grill Me 共享设计概念）

第一种:AI 做出的东西不是我要的。

我脑子里明明有个清晰的想法,AI 却做出来一个完全不一样的东西,或者搞出一份我压根不想要的规格。踩过这个坑的请举手。

好,谢谢。

《程序员修炼之道》里讲过一句话:没人真的知道自己要什么。你和 AI 之间存在一道沟通的鸿沟,懂吧？

所以你跟 AI 聊的过程,其实就是 AI 在做需求收集——它在从你嘴里挖出你真正要的东西。

我又想起另一本书——Frederick P. Brooks 的《The Design of Design》,里头讲了一个概念,叫“设计概念”。

说的是:多个人一起设计某个东西时,大家脑子里飘着一个共同的、稍纵即逝的念头——你做的是“那个东西”。这个“那个东西”,或者它背后的想法,就叫“设计概念”。它不是个资产,不能写进 markdown 文件,而是关于你在造什么的一种无形的理论。

我恍然大悟:毛病就在这——我和 AI 共享不到同一个“设计概念”。于是我做了一个 skill。

Skill 极简,叫“Grill Me”（拷问我）,长这样。

“不厌其烦地就方案的方方面面采访我,直到我们达成共识。沿着设计树的每一根枝杈走下去——这又是 Brooks 的另一个概念——把决策之间的依赖一条一条解开。”这个 skill 仓库已经攒到大概 1.3 万星了,完全是爆红。大家都爱用。就这么几行,会让 AI 问你 40 个、60 个问题——我见过它问到 100 个才觉得双方对齐了。它把 AI 变成一个“对手”,不停 ping 你,逼你把想法掏干净,直到共识达成。

一旦聊完,这段对话本身就可以整理成产品需求文档(PRD);改动小的话,直接拆成 issue 也行。

再交给后台的 AI agent 去执行。

别喷我——我个人觉得,这比我用的 Claude Code 的默认 plan mode 还顺手。

默认 plan mode 太急着产出“资产”了,它恨不得立刻写一份计划,然后就开干。

而我觉得,先达成共同的设计概念,再动手,体验好太多。

这是第一条建议。

### 三、失败模式二：AI 太啰嗦（建议：建立通用语言）

第二种失败模式:AI 实在太啰嗦。

你和 AI 几乎在“鸡同鸭讲”。有同感的请举手。嗯,不少。

感觉就是 AI 一直在堆字,想说清它在干嘛——而你们其实没在用同一种语言。

这种体验我太熟了。干开发久了,你会跟领域专家合作,比如对方让你做个芯片相关的东西——你完全不懂芯片。

你得先建立一种共同语言,对吧？不然对方用一堆你不懂的术语,你硬翻译成代码——自己都未必懂,专家肯定也看不懂。

于是就有了你跟领域之间的语言鸿沟——我又去翻了领域驱动设计（DDD）。

这块我还在摸索边缘,但读到的 DDD 内容,句句说到心坎上。我爱死了。

DDD 有一个核心概念:通用语言（ubiquitous language）。

有了通用语言,开发者之间的对话、代码里的命名、跟领域专家的沟通,全都源自同一个领域模型。

落到实操,就是一个 markdown 文件,里面列满你和 AI 共用的术语。你要反复打磨这些词,确保它们的含义和实际所指完全对齐,然后在代码里、聊代码时、跟领域专家沟通时,以及在我们这里——跟 AI 说话时,无时无刻不在用这套词。

我做了一个 skill。

就是“通用语言” skill。它会扫描你的代码库,扒出术语,然后产出一个 markdown 文件——一张张 markdown 表,把术语全列出来。

我把这份文件喂给 AI,我自己也一直开着——在 Grill Me 对话、规划时都开着。翻看 AI 的思考轨迹我发现:这套通用语言不仅让规划更顺,还让 AI 思考时不再啰嗦,产出的实现也更贴近你原本的设计。效果立竿见影,好到难以置信。

这是第二条建议:==跟 AI 建立共同语言==。

### 四、失败模式三：跑不起来（建议：TDD + 反馈回路）

好,假设你已经和 AI 对齐了——你们都知道该造什么。AI 也确实造出了对的东西,但跑不起来。

经历过这事的请举手。

对,就是跑不起来。

改进的方法很直白:加反馈回路。可以用静态类型——你要是还没上 TypeScript,那真说不过去。你要是做前端应用,却没把浏览器权限给 LLM 让它自己看,那也肯定不行。

自动化测试更是少不了。

我观察到一个现象:就算有了这些反馈回路,LLM 也不会用好它。跟老手开发者相比,它根本没把反馈回路的价值榨出来。它的老毛病是一次性做太多——先吐一大坨代码,然后才想起来:“哦,应该跑一下类型检查”;或者“或许该跑下测试”;或者“也许该干点啥”。

《程序员修炼之道》里把这种现象叫“跑出车灯照亮的范围”。说白了就是开得太快——而你车灯能照到多远,就是你的速度上限。

反馈的速度就是你的速度上限。这意味着你要边走边测,小步、刻意地走。而 AI 默认其实并不擅长这个。

所以第三条建议是 TDD（测试驱动开发）。

你必须用 TDD,因为 TDD 会逼着 LLM 真正小步前进——先写一个测试,让测试通过,再回头重构代码,打磨设计。

问题在于,测试本身很难。

测试从来就难。

难在写一个测试要做出一堆决策。

先想清楚要测多“大”的一个单元。

要决定 mock 什么。一开始就要想清楚:你到底要测哪些行为？

这些决策互相牵连。比如你测一个非常大的单元——比如整个庞大的应用——测试就会很 flaky;你也不想测那么多行为。如果只测这一个单元,你又得 mock 它,环环相扣。这些年,整个开发生涯,我都在琢磨这件事。

我们观察到一个规律:好代码库就是好测的代码库。

对吧？绕了一圈,又回到那个命题——代码本身是重要的。代码库越好,反馈回路就越好用——你能给 LLM 更精准的反馈,它就吐出更好的代码。

### 五、深模块 vs 浅模块（建议：深模块 + 灰盒设计）

我就在想:好代码库、好测的代码库,长什么样？又去找 Ousterhout。他提了一个概念:深模块。不是浅模块,不是那种暴露一堆零碎函数的小模块。

应该是“少量、巨大、深度”的模块,接口却很简单。

快速对比一下。

深模块:把大量功能藏在一个简洁的接口后面,把复杂度藏起来。

你愿意的话,可以钻进深模块内部看;但你不必这么做——直接用接口就行。浅模块则相反:功能不多,接口却复杂。

（给大家拍 PPT 的时间。）

浅模块组成的代码库大概长这样:一堆零碎的小块,AI 得一个个爬过去、一点点摸索。说实话,这对 AI 来说极其难导航。

你经常会看到这种情况——AI 特别擅长造出这种代码库——AI 自己也不懂代码在干嘛。它想探索代码,但因为结构混乱,全是浅模块,它要么没及时摸到对的模块,要么理不清依赖,反正就是不懂。

那充满深模块的代码库长什么样？

长这样。

代码量是一样的,只是被组织在边界之内,顶上是一组接口。

这些接口,你得亲自把控、设计好——否则 AI 很可能把设计搞砸。

至于实现,基本可以交给 AI。

那怎么把左边的代码库,改造成右边这种？

我有个 skill 专门做这事——“Improve codebase architecture”。这事做起来并不简单,但套路可以反复套用:去代码库里逛,找出几处明显相关的代码,把整块包进一个深模块里。

这种代码库非常好测,因为边界极其简单。在接口上做测试、靠接口验证,就齐活了。这是会“奖励 TDD”的代码库。

### 六、失败模式六：脑子跟不上（建议：设计接口，委托实现）

那第六种失败模式呢？

假设你的反馈回路都跑顺了,事情开始飞速推进。

你交付的代码量比过去任何时候都多,但你的脑子跟不上。

对吧？开发生涯里,有没有觉得比以往任何时候都更累？请举手。

我也是。真的累垮了。

我觉得,正是这种代码库让大脑更累——你和 AI 都得把这一堆信息塞在脑子里。

而深模块那种代码库,不仅更易读、易懂,你还可以把这些模块当成“灰盒”来对待。

你可以对自己说:“我只设计接口,内部的实现不细抠,也不必逐行 review。”对于应用中不太关键的模块,当然可以这么做——金融之类的核心逻辑可不行——但应用里大多数模块,你不必死磕实现,只要模块外有可测的边界,只要你能从外部讲清它的用途、设计好它的接口,就够了。这套做法真的救了我的脑子——我可以对自己说:“AI,大块内部你随便造。我只从外面测、只从外面验。”这是第五条建议:设计接口,把实现委托出去。

但这意味着,任何时候我们碰代码、做规划,脑子里都要装着应用里有哪些模块。这张模块地图要烂熟于心,也要纳入我们的通用语言。我写 PRD 时,会明确写出:哪些模块要改、这些模块的接口要如何变化。我时时刻刻都在想模块。这套做法来自 Kent Beck。

每天都要投资系统的设计。

### 七、收束：代码是重要的

这是整套心法的核心,懂吧？

因为“规格即代码”那一套,我们根本没有在投资系统的设计。

我们是在撤资——把“系统设计”这块业务砍掉。

而我坚信,这一步才是关键。

所以,代码并不廉价。这是今天我希望大家带走的核心一句话:代码是重要的。

把 AI 想象成一个非常出色的“地面部队”——战术级的程序员,一个在地上敲代码的士官——那你头上还需要有人。

需要有人做战略层面的思考。那个人,是你。

这要求我们掌握软件工程的基本功——这些基本功我们用了 20 年,甚至更久。

刚才提到的这些 skill,都放在 GitHub 仓库 mattpocock/skills 里。

想了解我的课程或免费内容,YouTube 和 Twitter 上都能找到我;另外我也在 aihero.dev 维护一份 newsletter,欢迎订阅。

非常感谢。希望今天的内容能让你在这个 AI 时代更有信心——你完全可以做出真正有价值的贡献。

谢谢。

---

## 完整文字稿（英文原文）

> 字幕来源：YouTube auto-generated English captions
> 段落格式：`[时:分:秒] 文字内容`

*[00:00:07.205] [music]*

**[00:00:14.640]** Hello everyone. Having a good conference so far? Yeah. Are you having a good conference so far? Yeah. Good.

**[00:00:20.480]** Wonderful.

**[00:00:22.160]** I have a message for you that I hope will be um a comforting message for folks who believe that uh their skill set is no longer worth anything in this new age, which is I believe that software fundamentals matter now more than they actually ever have.

**[00:00:39.040]** And I'm a teacher, and I've been recently teaching a course called Clojure Code for Real Engineers.

**[00:00:47.240]** Nice and provocative. And in the process of kind of working on this course, I had to come up with a curriculum about AI coding, which is a bit of a nightmare because things are changing all the time, right? AI is a whole new paradigm.

**[00:01:02.280]** We need to chuck out all of the old rules, surely, so that we can bring in the new stuff.

**[00:01:08.000]** And there's a kind of movement that has come up around this, which is the specs-to-code movement. And the specs-to-code movement says that, "Okay, you can write a specification about how an application is supposed to work. Then you can use AI to turn it into code. If there's a problem with the application, you then go back to the spec. You don't really look at the code. You just change the spec, you run the compiler again, and you end up with more code." Raise your hand if you've heard of that.

**[00:01:37.160]** Keep your hand raised if you've tried it.

**[00:01:39.800]** Okay, I've tried it, too. You can put your hands down.

**[00:01:42.800]** And what I noticed was I would run it, and I would try not to look at the code, but I would look at the code, and I realized I would get code out, first of all, and then I would run it, I would get worse code. And I did it again, I got even worse code. I got it again, I kept running the compiler, kept running the compiler, and I would just end up with garbage.

**[00:02:03.640]** You know, raise your hand if that's happened to you.

**[00:02:06.000]** Yes. I don't think this works. The idea that we can just ignore the code and just have the code let it manage itself is just sort of vibe coding by another name.

**[00:02:16.560]** And I didn't believe that back then. I thought, "Okay, how do I fix the compiler? How do I make it so that it doesn't produce bad code each time, or worse code?" And so I thought, "Okay, I need to explain to the LLM in English what a good code base looks like." Let me dig out one of my old favorite books, which is a Philosophy of Software Design by John Osterhout.

**[00:02:37.760]** Go on Amazon, get it.

**[00:02:39.320]** Um and he has a definition for what bad code looks like.

**[00:02:45.360]** He calls it complex code. Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system, right?

**[00:02:53.480]** So a a bad code base is a code base that's hard to change. If you can't change a code base without causing bugs, then it's a bad code base. Good code bases are easy to change.

**[00:03:04.200]** So I thought, "Ooh, that was good.

**[00:03:05.880]** Let's try another book. Let's try The Pragmatic Programmer." Go on Amazon, get it.

**[00:03:10.680]** They have a whole chapter on something called software entropy. And this is exactly what I was seeing. Entropy is the idea that things tend towards um disaster and uh floating away from each other and collapse. And this is exactly how most software systems behave, too, is that every time you make a change to a code base, if you're only thinking about that change and not thinking about the design of the whole system, your code base is going to get worse and worse and worse. And that's what I was seeing.

**[00:03:36.880]** Everything inside the specs-to-code idea that you just run the compiler again and again was making worse code.

**[00:03:43.200]** Now, there's an idea that sort of drives the specs-to-code movement, which is that code is cheap. Raise your hand if you've heard that phrase before, that code is cheap. Yeah.

**[00:03:55.000]** Well, I don't think this is right.

**[00:03:57.560]** I think code is not cheap. In fact, bad code is the most expensive it's ever been.

**[00:04:03.600]** Because if you have a code base that's hard to change, you're not able to take all of the bounty that AI can offer, cuz AI in a good code base actually does really, really well.

**[00:04:15.120]** And this means good code bases matter more than ever, which means software fundamentals matter more than ever.

**[00:04:20.400]** That's the thesis of this talk.

**[00:04:22.880]** So let's actually get into practical stuff.

**[00:04:25.400]** I'm going to talk about different failure modes that you may have experienced, or you may not have experienced yet with AI, and how you can avoid them by just going back to old books and looking at good software practices. Sound good?

**[00:04:36.640]** So the first one is that the AI didn't do what I wanted.

**[00:04:40.720]** You know, I I thought I had a good idea in my head, and the AI just did something totally different, or it did some uh like specs that I, you know, it just made something I didn't want. Raise your hand if you've hit this mode.

**[00:04:51.720]** Cool. Okay.

**[00:04:53.280]** Well, this is what they say in The Pragmatic Programmer, is that no one knows exactly what they want. It's that you and the AI, there is a communication barrier there, right?

**[00:05:04.000]** And so when you're talking to the AI, that's kind of like the AI doing its requirements gathering. It's basically working out from you what it is that you need.

**[00:05:12.760]** And I realized that there was another book, Frederick P. Brooks' The Design of Design, and it talks about this idea called the design concept.

**[00:05:22.280]** It's that when you have more than one person designing something together, you have this idea sort of floating between you, this ephemeral idea of the thing that you're building. And that thing that you're building, or the idea of it, is called the design concept. It's not an asset, it's not something you can put in a markdown file, it is the invisible sort of theory of what you're building.

**[00:05:44.040]** And so I thought, "Okay, that's what's going on. Me and the AI don't share a design concept." So I came up with a skill.

**[00:05:51.280]** The skill is very, very simple. It's called Grill Me, and it looks like this.

**[00:05:57.080]** "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, which is another thing from Frederick P. Brooks, resolving dependencies between decisions one by one." This skill is like uh the repo containing this skill has like 13,000 stars or something. Like, it just went nuts, went viral. People love this thing. It These couple of lines means the AI asks you like 40 questions, 60 questions. I've had it ask uh people 100 questions before it's satisfied they've reached a shared understanding. And it means it turns the AI into a kind of adversary, where it's just continually pinging you ideas and trying to reach a shared understanding.

**[00:06:38.120]** And that means that the conversation that you then generate, you can take that and turn it into a product requirements document or something. Or if it's a small change, you can just uh do uh turn it directly into issues.

**[00:06:52.000]** And then your AFK agent will then pick it up.

**[00:06:54.640]** And don't at me on this, but I personally believe this is better than the default plan mode in uh the tool that I use, which is Clojure Code.

**[00:07:04.440]** Plan mode is extremely eager to create an asset. It really wants to uh just create a plan and start working.

**[00:07:12.240]** Whereas I think it's a lot nicer to reach a shared design concept first.

**[00:07:18.760]** So that's tip number one.

**[00:07:21.440]** Now, failure mode number two is that the AI is just way too verbose.

**[00:07:25.960]** It's like you're almost talking at cross-purposes with the AI. Raise your hand if you uh feel this. If you've ever experienced that failure mode. Yeah.

**[00:07:33.240]** It's kind of like the AI is like talking just using too many words to try to communicate what it's doing. It's not like you're talking uh using the same language.

**[00:07:41.920]** And this to me felt very, very familiar, right? If you've ever been a developer for a long time, and you've worked with, let's say, domain experts, someone building an application, um let's say the domain expert wants you to build something on uh I don't know, microchips. You have no idea what microchips are.

**[00:07:57.040]** You need to establish some kind of shared language, right? Cuz otherwise, they're going to be using terms you don't understand. You're going to be translating that into code that maybe you don't even understand, and certainly the domain expert won't.

**[00:08:07.760]** And so there's this kind of language gap between you and the domain I went back to domain-driven design, DDD.

**[00:08:17.880]** This is something I'm still kind of on the edge of exploring, but everything I'm reading about DDD is just music to my ears. I freaking love it.

**[00:08:25.600]** And DDD has a concept of a ubiquitous language.

**[00:08:30.880]** With a ubiquitous language, conversations among developers, and expressions of the code, and conversations with domain experts are all derived from the same domain model.

**[00:08:39.120]** It's essentially a markdown file full of a list of terms that you and the AI have in common. And you really focus on those terms, and you really make sure that they're aligned with what it actually means, and you use them all the time in the code, when you're talking about the code, when you're talking to domain experts, or in our case, when you're talking with AI.

**[00:08:57.640]** So I made a skill.

**[00:08:59.760]** This skill is the ubiquitous language skill. Basically just scans your code base, looks for terminology, and then um creates a markdown file. Creates the ubiquitous language markdown file, a bunch of markdown tables with all of the terminology.

**[00:09:14.840]** And this, then I pass it to the AI, and I'm able to read it, too. And I actually have it open all the time when I'm grilling with the AI and planning and that. What I noticed by reading the thinking traces of the AI, it not only improves the planning, but it allows the AI to think in a less verbose way, and actually means that the implementation is more aligned with what you actually planned. So this has absolutely been a powerhouse. It's been unbelievably good.

**[00:09:41.320]** So that's tip number two. Create a shared language with the AI.

**[00:09:45.920]** So okay, let's imagine that you've aligned with the AI. You know what it is you're supposed to be building. The AI has built the right thing, but it doesn't work.

**[00:09:55.440]** Raise your hands if that's happened to you.

**[00:09:57.840]** Yeah, just doesn't work.

**[00:09:59.800]** Well, there's an obvious thing that we can do to make that better, which is we can use feedback loops. We can use um static types, you know, if you're not using TypeScript, uh that's crazy. Uh if you're not using uh if you're building a front-end app and you're not giving it the LLM access to the browser so it can look around, absolutely needs that.

**[00:10:19.040]** And you obviously also need automated tests.

**[00:10:23.240]** And one sort of thing I notice here is that even with these feedback loops, the LLM doesn't use them very well. It doesn't kind of like get the most out of its feedback loops in the way that a veteran developer would. And so it does what it tends to do is just does way too much at once. It will produce like a huge amounts of code and then think, "Oh, I should probably type check that actually." Or I should uh you know, maybe check a test on that or maybe do something like that.

**[00:10:50.560]** And this in the Pragmatic Programmer they describe as outrunning your headlights. It's essentially driving too fast because the rate of feedback is your speed limit.

**[00:11:02.040]** The rate of feedback is your speed limit, which means that you should be testing as you go, taking small deliberate steps. And the AI by default is really not very good at that.

**[00:11:11.920]** So, skill number three is TDD.

**[00:11:14.880]** You should be using test-driven development because TDD forces the LLM to really take small steps. You create a test first, you make that test pass, and then you refactor the code to make it nicer and consider the design.

**[00:11:32.280]** The issue here is that testing is really hard.

**[00:11:36.280]** Testing has always been hard.

**[00:11:38.800]** And the reason for that is there are a ton of different decisions you need to make when you write a test.

**[00:11:46.760]** You need to figure out how big a unit do you want to test?

**[00:11:50.520]** You need to figure out what to mock. You need to figure out what behaviors do you even want to test in the first place?

**[00:11:55.680]** And all of these decisions are dependent. So, if you are testing a really big unit like an entire uh massive application, then it might be quite flaky. You might not want to test that many behaviors. You know, if you only test this unit, you need to mock this unit, you know. It's all interlinked. And I've been thinking about this for years, for my entire development career.

**[00:12:15.160]** And what we notice is that good codebases are easy codebases to test.

**[00:12:20.760]** Right? So, here we're starting to get back to the idea of code being important. It's that the better your codebase is, the better your feedback loops are because you're able to um give better feedback to the LLM, it produces better code.

**[00:12:35.560]** And so I thought, what does a good codebase, what does a testable codebase look like? Again, we go to John Ousterhout. [clears throat] He talks about having deep modules in your codebase. Not shallow modules, not lots of modules that expose type kind of um lots of functions.

**[00:12:52.440]** They should be relatively few large deep modules with simple interfaces.

**[00:12:57.480]** Let's compare them quickly.

**[00:12:59.480]** Deep modules, lots of functionality hidden behind a simple interface. Hiding the complexity.

**[00:13:05.640]** You can look inside the deep module if you want to, but you don't need to. You can just use the interface. Shallow modules, not much functionality, complex interface.

**[00:13:13.880]** And I'll just wait for you to take the photos.

**[00:13:18.360]** Shallow modules in a codebase kind of look like this, where you have a ton of different tiny little blobs that the AI has to walk through and navigate. And this is really hard for the AI to explore actually.

**[00:13:30.960]** And so often what you'll see is if you have a codebase like this, which AI is really good at creating codebases like this, is that you'll have a situation where AI doesn't understand what your code is doing. It will attempt to explore the code, but because it's poorly laid out, filled with shallow modules, it doesn't maybe get to the right module in time or doesn't understand all the dependencies, all that stuff. It doesn't understand your code.

**[00:13:53.720]** And so what does a codebase full of deep modules look like?

**[00:13:57.960]** Well, it looks like this.

**[00:14:00.280]** Where it's the same code, but it's just structured inside boundaries, where you have these interfaces on the top.

**[00:14:08.560]** And these interfaces, you should probably have a lot of control over them and design them really well. Otherwise, you know, AI might mess up the design.

**[00:14:17.120]** But the implementation, you can kind of leave that to the AI bit.

**[00:14:20.920]** So, how do you turn a codebase that looks like this into a codebase that looks like that?

**[00:14:29.120]** Well, I've got a skill for that. Improve codebase architecture. Turns out this is not It's it's quite complicated to do this, but it's a like a set of steps that you can reusably do again and again. You just sort of explore the codebase, look for opportunities where there's code that's kind of look um related, and wrap all of that in a deep module.

**[00:14:50.000]** And this is a testable codebase because the boundaries around this code are so so simple. You test at the interface, you verify using that interface, and you're good to go. And so this is a codebase that rewards TDD.

**[00:15:04.240]** But how about failure mode number six?

**[00:15:06.480]** Which is your Okay, let's say your feedback loops are working. Let's say that things are kicking into gear.

**[00:15:11.120]** You're able to ship more code than you ever have before, but your brain can't keep up.

**[00:15:16.520]** Right? Uh raise your hand if you've felt more tired than you have ever before in your development career.

**[00:15:22.320]** Yeah, me too. It's knackering.

**[00:15:25.160]** And I think that this is a codebase that actually makes it harder for your brain because you, as well as the AI, need to keep all of that information in your head.

**[00:15:34.800]** Whereas this, not only is it simpler for you to read and understand, it also means you can kind of treat these modules, or these deep modules, as gray boxes.

**[00:15:47.360]** You can kind of say, "Okay, I'm going to just design the interface, but I'm not going to worry too much or not review the implementation too much." You can do this obviously with uh things that are less critical in your application. Can't do this with uh you know, various things like finance or whatever, but in many many modules in your app, you don't need to think about the implementation too much as long as you have a testable boundary outside the module, and as long as you understand its purpose and can design it from the outside. I have found this has really saved my brain because I can just go, "Okay, the AI, I'll let you handle what's inside the big blob. I'm just going to test from the outside and verify it." So, that's tip number five. Design the interface, delegate the implementation.

**[00:16:32.000]** But this means that whenever we're touching the code, whenever we're planning stuff, we need to think about and be aware of the modules in our application. We need to know that map really well. It needs to be part of our ubiquitous language. We need to build it into our planning skills as well. So, my write a PRD, inside the PRD I'm specific about the module changes and the interfaces inside those modules, how they're being modified. I'm thinking about them all the time. And this comes from Kent Beck.

**[00:16:58.760]** Invest in the design of the system every day.

**[00:17:02.720]** And this is the core of it, right?

**[00:17:03.920]** Because specs to code, we are not investing in the design of the system.

**[00:17:08.560]** We are divesting from it. We're getting rid of that.

**[00:17:12.240]** Whereas this, I think, is absolutely key.

**[00:17:16.400]** And so code is not cheap. That's the message I want you to take away. Code is important.

**[00:17:23.439]** And if we think about AI as a really great on-the-ground programmer, a kind of tactical programmer, a sergeant on the ground making the code changes, you need someone above that.

**[00:17:35.520]** You need someone thinking on the strategic level. And that's you.

**[00:17:39.600]** And that requires software fundamental skills that we've been using for 20 years, for longer.

**[00:17:46.400]** Now, if you were interested in any of the skills I put up here, it's in the GitHub repo macpocockskills.

**[00:17:52.000]** And if you're interested in the training that I do or any free stuff, I'm on YouTube, I'm on Twitter, but I'm also at aihero.dev, where I have a newsletter you can check out.

**[00:18:01.000]** Thank you so much. I hope that this gives you confidence in this new AI age that you can actually make a good impact.

**[00:18:07.840]** Thank you.

*[00:18:09.277] [music]*

*[00:18:10.587] [applause]*

*[00:18:15.827] [music]*

*[00:18:21.067] [music]*

---

## 关键节点索引

| 时戳 | 内容摘要 |
|------|----------|
| `00:00:14.640` | Hello everyone. Having a good conference so far? Yeah. Are you having a good con... |
| `00:00:20.480` | Wonderful. |
| `00:00:22.160` | I have a message for you that I hope will be um a comforting message for folks w... |
| `00:00:39.040` | And I'm a teacher, and I've been recently teaching a course called Clojure Code ... |
| `00:00:47.240` | Nice and provocative. And in the process of kind of working on this course, I ha... |
| `00:01:02.280` | We need to chuck out all of the old rules, surely, so that we can bring in the n... |
| `00:01:08.000` | And there's a kind of movement that has come up around this, which is the specs-... |
| `00:01:37.160` | Keep your hand raised if you've tried it. |
| `00:01:39.800` | Okay, I've tried it, too. You can put your hands down. |
| `00:01:42.800` | And what I noticed was I would run it, and I would try not to look at the code, ... |
| `00:02:03.640` | You know, raise your hand if that's happened to you. |
| `00:02:06.000` | Yes. I don't think this works. The idea that we can just ignore the code and jus... |
| `00:02:16.560` | And I didn't believe that back then. I thought, "Okay, how do I fix the compiler... |
| `00:02:37.760` | Go on Amazon, get it. |
| `00:02:39.320` | Um and he has a definition for what bad code looks like. |
| `00:02:45.360` | He calls it complex code. Complexity is anything related to the structure of a s... |
| `00:02:53.480` | So a a bad code base is a code base that's hard to change. If you can't change a... |
| `00:03:04.200` | So I thought, "Ooh, that was good. |
| `00:03:05.880` | Let's try another book. Let's try The Pragmatic Programmer." Go on Amazon, get i... |
| `00:03:10.680` | They have a whole chapter on something called software entropy. And this is exac... |
| `00:03:36.880` | Everything inside the specs-to-code idea that you just run the compiler again an... |
| `00:03:43.200` | Now, there's an idea that sort of drives the specs-to-code movement, which is th... |
| `00:03:55.000` | Well, I don't think this is right. |
| `00:03:57.560` | I think code is not cheap. In fact, bad code is the most expensive it's ever bee... |
| `00:04:03.600` | Because if you have a code base that's hard to change, you're not able to take a... |
| `00:04:15.120` | And this means good code bases matter more than ever, which means software funda... |
| `00:04:20.400` | That's the thesis of this talk. |
| `00:04:22.880` | So let's actually get into practical stuff. |
| `00:04:25.400` | I'm going to talk about different failure modes that you may have experienced, o... |
| `00:04:36.640` | So the first one is that the AI didn't do what I wanted. |
| `00:04:40.720` | You know, I I thought I had a good idea in my head, and the AI just did somethin... |
| `00:04:51.720` | Cool. Okay. |
| `00:04:53.280` | Well, this is what they say in The Pragmatic Programmer, is that no one knows ex... |
| `00:05:04.000` | And so when you're talking to the AI, that's kind of like the AI doing its requi... |
| `00:05:12.760` | And I realized that there was another book, Frederick P. Brooks' The Design of D... |
| `00:05:22.280` | It's that when you have more than one person designing something together, you h... |
| `00:05:44.040` | And so I thought, "Okay, that's what's going on. Me and the AI don't share a des... |
| `00:05:51.280` | The skill is very, very simple. It's called Grill Me, and it looks like this. |
| `00:05:57.080` | "Interview me relentlessly about every aspect of this plan until we reach a shar... |
| `00:06:38.120` | And that means that the conversation that you then generate, you can take that a... |
| `00:06:52.000` | And then your AFK agent will then pick it up. |
| `00:06:54.640` | And don't at me on this, but I personally believe this is better than the defaul... |
| `00:07:04.440` | Plan mode is extremely eager to create an asset. It really wants to uh just crea... |
| `00:07:12.240` | Whereas I think it's a lot nicer to reach a shared design concept first. |
| `00:07:18.760` | So that's tip number one. |
| `00:07:21.440` | Now, failure mode number two is that the AI is just way too verbose. |
| `00:07:25.960` | It's like you're almost talking at cross-purposes with the AI. Raise your hand i... |
| `00:07:33.240` | It's kind of like the AI is like talking just using too many words to try to com... |
| `00:07:41.920` | And this to me felt very, very familiar, right? If you've ever been a developer ... |
| `00:07:57.040` | You need to establish some kind of shared language, right? Cuz otherwise, they'r... |
| `00:08:07.760` | And so there's this kind of language gap between you and the domain I went back ... |
| `00:08:17.880` | This is something I'm still kind of on the edge of exploring, but everything I'm... |
| `00:08:25.600` | And DDD has a concept of a ubiquitous language. |
| `00:08:30.880` | With a ubiquitous language, conversations among developers, and expressions of t... |
| `00:08:39.120` | It's essentially a markdown file full of a list of terms that you and the AI hav... |
| `00:08:57.640` | So I made a skill. |
| `00:08:59.760` | This skill is the ubiquitous language skill. Basically just scans your code base... |
| `00:09:14.840` | And this, then I pass it to the AI, and I'm able to read it, too. And I actually... |
| `00:09:41.320` | So that's tip number two. Create a shared language with the AI. |
| `00:09:45.920` | So okay, let's imagine that you've aligned with the AI. You know what it is you'... |
| `00:09:55.440` | Raise your hands if that's happened to you. |
| `00:09:57.840` | Yeah, just doesn't work. |
| `00:09:59.800` | Well, there's an obvious thing that we can do to make that better, which is we c... |
| `00:10:19.040` | And you obviously also need automated tests. |
| `00:10:23.240` | And one sort of thing I notice here is that even with these feedback loops, the ... |
| `00:10:50.560` | And this in the Pragmatic Programmer they describe as outrunning your headlights... |
| `00:11:02.040` | The rate of feedback is your speed limit, which means that you should be testing... |
| `00:11:11.920` | So, skill number three is TDD. |
| `00:11:14.880` | You should be using test-driven development because TDD forces the LLM to really... |
| `00:11:32.280` | The issue here is that testing is really hard. |
| `00:11:36.280` | Testing has always been hard. |
| `00:11:38.800` | And the reason for that is there are a ton of different decisions you need to ma... |
| `00:11:46.760` | You need to figure out how big a unit do you want to test? |
| `00:11:50.520` | You need to figure out what to mock. You need to figure out what behaviors do yo... |
| `00:11:55.680` | And all of these decisions are dependent. So, if you are testing a really big un... |
| `00:12:15.160` | And what we notice is that good codebases are easy codebases to test. |
| `00:12:20.760` | Right? So, here we're starting to get back to the idea of code being important. ... |
| `00:12:35.560` | And so I thought, what does a good codebase, what does a testable codebase look ... |
| `00:12:52.440` | They should be relatively few large deep modules with simple interfaces. |
| `00:12:57.480` | Let's compare them quickly. |
| `00:12:59.480` | Deep modules, lots of functionality hidden behind a simple interface. Hiding the... |
| `00:13:05.640` | You can look inside the deep module if you want to, but you don't need to. You c... |
| `00:13:13.880` | And I'll just wait for you to take the photos. |
| `00:13:18.360` | Shallow modules in a codebase kind of look like this, where you have a ton of di... |
| `00:13:30.960` | And so often what you'll see is if you have a codebase like this, which AI is re... |
| `00:13:53.720` | And so what does a codebase full of deep modules look like? |
| `00:13:57.960` | Well, it looks like this. |
| `00:14:00.280` | Where it's the same code, but it's just structured inside boundaries, where you ... |
| `00:14:08.560` | And these interfaces, you should probably have a lot of control over them and de... |
| `00:14:17.120` | But the implementation, you can kind of leave that to the AI bit. |
| `00:14:20.920` | So, how do you turn a codebase that looks like this into a codebase that looks l... |
| `00:14:29.120` | Well, I've got a skill for that. Improve codebase architecture. Turns out this i... |
| `00:14:50.000` | And this is a testable codebase because the boundaries around this code are so s... |
| `00:15:04.240` | But how about failure mode number six? |
| `00:15:06.480` | Which is your Okay, let's say your feedback loops are working. Let's say that th... |
| `00:15:11.120` | You're able to ship more code than you ever have before, but your brain can't ke... |
| `00:15:16.520` | Right? Uh raise your hand if you've felt more tired than you have ever before in... |
| `00:15:22.320` | Yeah, me too. It's knackering. |
| `00:15:25.160` | And I think that this is a codebase that actually makes it harder for your brain... |
| `00:15:34.800` | Whereas this, not only is it simpler for you to read and understand, it also mea... |
| `00:15:47.360` | You can kind of say, "Okay, I'm going to just design the interface, but I'm not ... |
| `00:16:32.000` | But this means that whenever we're touching the code, whenever we're planning st... |
| `00:16:58.760` | Invest in the design of the system every day. |
| `00:17:02.720` | And this is the core of it, right? |
| `00:17:03.920` | Because specs to code, we are not investing in the design of the system. |
| `00:17:08.560` | We are divesting from it. We're getting rid of that. |
| `00:17:12.240` | Whereas this, I think, is absolutely key. |
| `00:17:16.400` | And so code is not cheap. That's the message I want you to take away. Code is im... |
| `00:17:23.439` | And if we think about AI as a really great on-the-ground programmer, a kind of t... |
| `00:17:35.520` | You need someone thinking on the strategic level. And that's you. |
| `00:17:39.600` | And that requires software fundamental skills that we've been using for 20 years... |
| `00:17:46.400` | Now, if you were interested in any of the skills I put up here, it's in the GitH... |
| `00:17:52.000` | And if you're interested in the training that I do or any free stuff, I'm on You... |
| `00:18:01.000` | Thank you so much. I hope that this gives you confidence in this new AI age that... |
| `00:18:07.840` | Thank you. |

---

