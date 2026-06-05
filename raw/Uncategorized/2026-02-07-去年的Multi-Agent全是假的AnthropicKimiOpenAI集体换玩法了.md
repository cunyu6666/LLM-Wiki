---
id: "7419717664123129230"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247489989&idx=1&sn=18cc2379373e49a7ff33adcf4d7603c4&chksm=c0a9a8c833aebea0bbb1a310b728cb6764129372e1849147341d96f89e1e4854630b75651408&mpshare=1&scene=1&srcid=0207XRtxGLVyforuNJy6QcO7&sharer_shareinfo=0d8c14392040fb31d8b7f1a2588ca5d2&sharer_shareinfo_first=df40cdcdd7a8e288ec999a25f6bec962
author: "猕猴桃 探索AGI"
collected: 2026-02-07
tags: []
---

# 去年的Multi-Agent全是假的，Anthropic、Kimi、OpenAI集体换玩法了。

# 去年的Multi-Agent全是假的，Anthropic、Kimi、OpenAI集体换玩法了。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247489989&idx=1&sn=18cc2379373e49a7ff33adcf4d7603c4&chksm=c0a9a8c833aebea0bbb1a310b728cb6764129372e1849147341d96f89e1e4854630b75651408&mpshare=1&scene=1&srcid=0207XRtxGLVyforuNJy6QcO7&sharer_shareinfo=0d8c14392040fb31d8b7f1a2588ca5d2&sharer_shareinfo_first=df40cdcdd7a8e288ec999a25f6bec962)猕猴桃 探索AGI


关于Multi-Agent，画风突然变了，Agent进入了下个阶段。

Kimi推出了 K2.5 Agent Swarm。 Claude昨天推出了Agent Teams。 GPT5.3-Codex，昨天的发布博客里边反复强调 "many of them working in parallel"。

可以先来看一下结果：

Claude昨天发了一篇博客，他们使用Agent Teams，从0编写了一个能编译Linux内核的C编译器，有10万行Rust代码。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APpXN878ZQWFIu7OXXLfEO1Y6GQU0iajLg4ZT89F4mO55gueJibLNdNDH97iaxS6Ghd7HTq2CRJyL2VNLemSpkrxdp17UGdAh5TtHA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

Kimi 的Agent集群，可以端到端运行时间降低80%，而且在一些基准上，大幅提升。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APrk4sRthcFwtY4kPOfXziaTBEJM7LXAqEW2rXEicqXPHTVk1AVyNibOcEgw1m3qickIz40nxCCTUvom7b5YQVjBGs2pibdEw3W3Hms0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APpziar4RjEiayv6habwSku13ds5EjVk6RnyY93sic0G5RS3uotfUBbDx6nuutMIDP43vRlxOoejktJZ3NCicjgDDbkC4JOgU3SvZ4Y%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

GPT-5.3-Codex在真实电脑操作测试上，从38.2%跳到64.7%。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APraibrYEe1YreI9srXlPgUoKSeOgYhSawP4cxMA2bXmEoiaLVCTUgyCYhvwJfbWK7LHzCtdgXibdqbVu9MicQgCBrTQJxOibuVXVIZY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

等等，去年Multi-Agent不是已经很热闹了嘛？

满大街都是多智能体协作。

但是，**去年的多智能体其实还是角色扮演。**

给3个大模型分别写一句system prompt------你是产品经理，你是程序员，你是测试。然后让它们轮流说话。

所以去年12月份的时候，Google DeepMind直接发了篇文章打脸：在很多基准上，单Agent的表现，仍然优于Multi-Agent。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APoGZ2eFVGibuyDHoTeTPAr8pBzMVicPyux7pm95HqFQOSspdjAZFDeHqr42XblicrSl4wdyPT0DNOxzriblHSWt8HyvHwZkOYNiaZKw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

那现在，为什么画风突然变了？

从结果来看，这一次，可能真的不一样了。

## 为什么会这样？

我想了想，这事背后，大概有两个关键变量到位了。

一、每个Agent自己得足够强。

要形成一个Agent集群，有一个大前提：

每个Agent都得足够牛。去年的模型尤其国产模型，模型自身能力还不够强。

但今年不一样了。

国内外的模型，在复杂推理上，都大幅提升。

K2.5在Agent基准上比上一代提升了24.3%。GPT-5.3-Codex的Terminal-Bench从64%飙到77.3%。Opus 4.6在网络安全调查中40次里38次被评为最佳。

话说，K2.5现在是真的强。从openrouter上大家的用量就看得出来，已经飙到Top1了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APpibaxmHk92WszYsLm6MRTlZ12VrtQrYeDFa2kQVhkqPdNFTibNJwJYQA3va0v7wjVf8JbDJLKdyzIzbsIIM0yI0ibwhzwN6SPuqE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

同时，metr的统计显示，从25年到26年，大模型可以持续工作的时长在呈指数级增长------25年1小时，26年6小时，甚至这个图表还没算上最新的模型。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APrMSD3UmLianwhEm6bgN4ZkKu6xT5RrNzqibfzmoPeLXdnKscT4D4CccJwkaL9ZK8iauB7CZvibiceRRvWOVEcUMdUSs8U542lpZDF0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

只有模型本身能力到位了，才有资格谈协作。

二、协调能力

这一点应该是最关键的变化。

去年的多Agent，指挥官是你写的Prompt，你告诉他，先让Agent A搜索，再让Agent B总结，最后让Agent C校对。

但今年不一样了。

在K2.5的技术报告里，他们提到了一个叫PARL的编排器。这不是一段Prompt，而是一个专门训练出来的项目经理。

它会根据任务的实际情况，现场决定要派多少个Agent、每个Agent负责什么、什么时候该汇总结果。

所有的角色分配和任务拆解，无需你预设，全由AI自己决策。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APqmCg3rY2PZqXm7IrQIPfHzqNprYF3qytsK0kKEMFJICZkjicEvjZWF8vBCAnUv3otgb91DjjeMdrTAOSFnGZDEePDeCLwiaaoJk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

简单来说，Multi-Agent的底层范式，不再是Prompt约定的规则，而是从模型训练阶段就开始生长出来的协作能力。

再加上MCP这类统一工具协议的出现，让多个Agent可以共享工具和环境。云厂商也都推出了面向多Agent编排的产品架构。

软件硬件，几乎全栈到位了。

## Agent集群到底强在哪？

Claude昨天的博客里，他们用Agent Teams，让16个Claude Agent并行协作，从零开始，写了一个C编译器。

用Rust写了，大概10万行代码。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APrbnIAPdwzNEMx8B5LnMgqicBwwpNstrxKTFZlq8dMFXJ6LIFWF5x5c7ybUahkulnxsbWoRheucVtn4hbU1POxTqID3TaicmkDTE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

这个编译器，能编译Linux 6.9内核。

整个过程大概跑了2000次会话，烧了20亿input token。

但重点不是花了多少钱。

重点是这16个Agent干活，没有人介入。

通过一个共享的任务目录来协调分工，你干这块，我干那块，谁写完了谁去认领下一个。遇到冲突，走Git合并。质量问题，靠测试套件。

这跟一个工程团队已经没有区别了。

再看数据。

Kimi K2.5的技术报告，给出了目前最详细的Agent集群量化数据：

端到端运行时间，缩短了4.5倍。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APpx0VaibicQibsXpQ3Pf4KF1RzqIicicCL6pxPErPlqh3yt1G6MXic9KOrgicxlE1vnDoklM1LWAQEmrPLxeaR7eYwz5NHj9BT9NtHf6Y%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9)

BrowseComp测试上，Agent集群对比单Agent提升明显：78.4% VS 60.6%。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APq7I0xXHsC6swTzrVsVstCLZPFZmNF9hicicw1ddfSPPiaTQpbent8Zq2ic9TK5RQlgrF5ticiaVyOGLcYVpLZyBGNEkVmdYK7vLAkow%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D10)

它的集群最多可以拉起100个分身，并行处理1500个步骤。

至于GPT-5.3-Codex这边，细节就比较少了，就是博客在反复强调。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APqgldKIeArA5yWANO4Sl7Gf4WvFqF7uX6gWmFj6mcKCno52J9y0qnDXktx7loMwclcHShHM23ZFw7AsvyhXFsibn5kIIvUKlEVY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D11)

方向，是一样的。

但Agent集群的优势，不只是快。

还有两个很多人忽略的东西。

第一个，容错。

在Agent集群里，某个子Agent挂了，其他Agent该干嘛干嘛，不受影响。

局部失败，不拖垮全局。

第二个，认知减负。

你想想，让一个人同时记住100件事，然后逐个处理。跟让100个人，各记1件事，各干各的。

谁更容易出错？谁更容易产生幻觉？

答案显而易见。

Agent集群把认知负载打散了。每个子Agent只专注自己那一块，上下文更短，注意力更聚焦，幻觉的概率，大幅降低。

所以你会发现，Agent集群天然适合那些：文件多、步骤多、单Agent跑起来又慢又容易翻车的场景。

批量分析、大规模调研、多文件校对、事实核查、长文撰写。

这些场景有一个共同特征：

一个人干不完，但一群人可以。

## Agent集群到底是什么体验呢？

说了这么多原因，可以来几个案例感受一下。

一、让不同的分身，深度博弈

Claude Code的官方教程里，举了一个特别有意思的场景：

你的应用出了Bug，不确定问题在哪。

有了Agent teams ，你可以建一个调查团队，5个Agent，每Agent带一个假设，互相辩论。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APpKJ7WGQkRc1WB2KbicpONR5DiaalCn5VicAQeBkibPapsJ8WJfiaWWcia298JONTF5eNyCV9xccSzFQeeaFYNaeVu8XSU7Qg6o5wCk0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D12)

然后这5个Agent会，各自去查证据，找到了就拿出来说服对方，被反驳了就换方向。

最后活下来的那个假设，大概率就是真正的答案。

二、千军万马

刚好写这篇文章需要做调研，我就直接拿Agent集群当工具了。

我扔了一段prompt进去：
> 我准备写一篇 Agent的洞察报告。核心内容关于：kimi k2.5发布带上了agent集群，claude code推出了agent teams，GPT-5.3-Codex也暗示了agent集群。这是不是代表一个全新的Agent范式？为什么会出现这种一致性？agent集群跟单一agent优势在哪？现在我需要你帮我找文献，不少于30篇最新的相关文献。

Agent集群的玩法是，先分出几个分身，从不同维度去检索，有的在找高引用经典论文，有的在找最新的行业分析。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APoXa1zHGKSgwR4DBibJxhoYogQjeoU9icUVVe9YEQLyT31F9RAN2BtHu8QvvvEt8vQibKhan1buJyiah6ibJlMwMCERAGHfibpwzL2TM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D13)

然后，更离谱的来了。

当候选列表出来之后，它直接又划出了50个分身，让每个分身单独去下载一个PDF。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APribkmIjVFrskUsVib1G0iam2j9oQeCbZUxkg42aia0sAqjXWeRvia5sxbEbibfSKfrc8XaGD6SSial6MLgw1eJMiacnLPicReom4cEChl0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D14)

50个分身，同时下载50篇论文。

说实话，我看着屏幕上那一排排并行推进的任务条，脑子里只有一个画面，千军万马。

三、现场决策

今天的Agent集群跟去年角色扮演形式的Agent的本质区别在这。

不会有固定的分工模式。几个分身完成了当前任务后，它会自动回收、重新分配，去干下一波任务。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APoEnIwrelALhrY9VvTTVE9cAr0BSSsT1r67G5qtKhGJ7mZYY2DgZG2aIKglIGicjLYtbiayj0ZAwbVNtDpzxyS5N2hEndibLLaEVc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D15)

全程不需要人工介入，你甚至不知道它下一步会怎么分工。

四、合作分工

在前面我拿到下载后的PDF之后。

我转手，又把这些PDF，塞回了Agent集群，让他撰写一篇万字综述。注意：这里可是有50个文件！！！
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APrdEwjQVCmY3WRTQVzt5aV4W5ibicL1WeIF0ibfrkyMmoibiccHA6dU8FSrTxXwEXzB9V3J9eXkI39ABxV8Q6bppEwBpict3ycl6Y7ls%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D16)

还是同样的套路，它又分配了一堆分身：有的负责读文献提取核心观点，有的负责梳理逻辑框架，有的负责撰写具体章节。

最终，我得到了一篇，看起来还真有点对味的综述。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2Fdurt1819APqhqVeFpEQDxCiagxVibXYqZzz6rHhXyJOqZp0TEU1KNuKicEZ6tmRic52tLdtrQjGL4ykSiatOqaA8dIksEjRzRuhiaDCUBwZoibicAGU%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D17)

从找文献、下载PDF、到写万字综述。

我只给了一个目标。

拆活、派人、干活、汇总------全是Agent集群自己搞定的。

我指挥的，已经不再是一个人。而是千军万马。

## 写在最后

当我看到Kimi、Claude、GPT几乎同时推出Agent集群的时候，我的第一反应不是，感觉技术又进步了。

而是一种很微妙的感觉：

AI的进化逻辑，正在变得越来越像人类社会。

你想想看。

人类文明最伟大的跃迁，从来不是因为出现了一个无敌超人。

而是因为我们学会了分工。而是因为我们学会了协作。学会了信任队友。

而今天的AI，似乎正在重新发明一个人类早就知道的道理：一个人可能走的更快，但一群人才会走的更远。

![](https://image.cubox.pro/cardImg/4ucm0lx2a44plmc0loodn47t3vn88lyvdpkv3edybzpdxhnfpg?imageMogr2/quality/90/ignore-error/1)

**探索AGI**

目前专注于大模型agent的产品落地方向，未来不确定\~

261篇原创内容

<br />

公众号  

，

好了，这就是我今天想分享的内容。如果你对构建AI智能体感兴趣，别忘了点赞、关注噢\~

#aiagent #claude #anthropic #multiagent

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247489989&idx=1&sn=18cc2379373e49a7ff33adcf4d7603c4&chksm=c0a9a8c833aebea0bbb1a310b728cb6764129372e1849147341d96f89e1e4854630b75651408&mpshare=1&scene=1&srcid=0207XRtxGLVyforuNJy6QcO7&sharer_shareinfo=0d8c14392040fb31d8b7f1a2588ca5d2&sharer_shareinfo_first=df40cdcdd7a8e288ec999a25f6bec962)

