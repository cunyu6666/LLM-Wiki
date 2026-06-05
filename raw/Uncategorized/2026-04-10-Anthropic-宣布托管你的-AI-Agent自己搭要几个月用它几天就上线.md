---
id: "7442271741793011509"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzYzNTY5Mjc2Ng==&mid=2247486412&idx=1&sn=4c7d5620186373eb9642d85d16928c09&chksm=f1a74165f3355a62427ebda4854c36a3117f1c604332af55198662e9a5581d219877fb769968&mpshare=1&scene=1&srcid=0410kSZhk7JStlyevY1agpRL&sharer_shareinfo=8362f2622ae072a48178827f4267d397&sharer_shareinfo_first=8362f2622ae072a48178827f4267d397
author: "AI新知前线Now AI新知前线Now"
collected: 2026-04-10
tags: []
---

# Anthropic 宣布托管你的 AI Agent：自己搭要几个月，用它几天就上线

# Anthropic 宣布托管你的 AI Agent：自己搭要几个月，用它几天就上线

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYzNTY5Mjc2Ng==&mid=2247486412&idx=1&sn=4c7d5620186373eb9642d85d16928c09&chksm=f1a74165f3355a62427ebda4854c36a3117f1c604332af55198662e9a5581d219877fb769968&mpshare=1&scene=1&srcid=0410kSZhk7JStlyevY1agpRL&sharer_shareinfo=8362f2622ae072a48178827f4267d397&sharer_shareinfo_first=8362f2622ae072a48178827f4267d397)AI新知前线Now AI新知前线Now


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FGAOdibiana5jHIExAOpq7nmpBibgV9ibfXtoicFKKAAiaZrjm4PxLibtgLLPndrett2qzP5BWpb9355N8dx2tvSN6fwKqTVdlRl1YTLs8wqcJdS4uY%2F640%3Fwx_fmt%3Djpeg%26watermark%3D1%23imgIndex%3D0)

你有没有想过，让 AI 自己去查资料、整理数据、写报告、改代码------全程不用你盯着，做完了直接给你结果？

这种能持续干活、自己拆解任务的 AI，叫做 **AI Agent（AI 代理）** 。

每家公司都想要它。但现实是------**想把它真正跑起来，要先花几个月时间自己搭一套复杂的底层系统。** 大多数公司，就卡在这里，Demo 看了一堆，迟迟没法落地。

4月8日，Anthropic 宣布：**这套底层系统不用你搭了，交给我，你直接来建 Agent。** Notion、Rakuten、Asana 已经用它把原本要几个月的事，压缩到了几天。

这到底是怎么做到的？

*** ** * ** ***

## 搭 Agent 到底难在哪里


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FGAOdibiana5jEaaibTdoXg6pJg2FJJATHaHCs48tzngF42LlUkMnB7EibOrOafHP0ibOsgcGC1JESqYjPs62Gv3loKM6N39aas75oVk9I2adADJM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

要回答这个问题，得先搞清楚，为什么企业自己搭 Agent 这么难。

很多人以为，有了 Claude 或者 GPT 这样的聪明 AI，搭个 Agent 不就是写几行代码的事？

实际上，差得远。

AI 本身只是"大脑"------它会思考、会回答。但要让它持续干活，你还得给它搭一整套"身体"，这套身体至少要解决六个问题：

**第一，它在哪里干活？** Agent 干活需要跑代码、读写文件，但又不能乱动你系统里其他的东西。你得搭一个隔离的运行环境，让它在里面安全操作。

**第二，它怎么记住做了什么？** 一个任务要跑半小时，上下文和历史记录必须有地方存着。一旦断连，如果什么都没记录，就得从头再来。

**第三，它怎么知道下一步做什么？** 需要一套"控制逻辑"，负责决定 AI 什么时候继续推理、什么时候调用外部工具、什么时候停下来交结果。这套逻辑，得你自己一行一行写出来。

**第四，出错了怎么办？** 网络断了、某个工具没响应、AI 跑偏了------这些意外情况随时都会发生。怎么自动重试、怎么从断点恢复，都要有人处理。

**第五，怎么让你看到 Agent 在做什么？** 如果 Agent 是个黑盒，你根本不知道它做到哪一步了、有没有出问题。没有可视化的过程，没有任何企业敢把正式任务交给它。

**第六，怎么规模化？** 一个 Agent 跑起来还好说，几十个 Agent 同时运行，并发调度、权限管理、稳定性------复杂程度又是另一个量级。

把这六件事都做好，搭出一套能用于正式生产环境的 Agent 系统，行业普遍的经验是：**少则两三个月，多则半年** 。而且做完了还容易出各种奇怪的问题。

这就是为什么你经常看到 AI Agent 的演示视频，却鲜少看到真正在企业里跑起来的案例。卡住大家的，不是 AI 不够聪明，而是这六件苦活。

*** ** * ** ***

## Anthropic 的答案：这六件事，我全包了


视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

正是为了解决这个问题，4月8日，Anthropic 推出了 **Claude Managed Agents** 。

它的逻辑很直接：既然搭 Agent 最难的是"跑起来所需要的那套底层系统"，那就由 Anthropic 来提供这套系统，企业不用再从零开始造轮子。

官方的定义是："**预构建、可配置的 Agent 运行框架，跑在 Anthropic 托管的基础设施上，专为长时间运行和异步任务设计。** "

用一句话说清楚就是：**你来定义"这个 Agent 是谁、能干什么"，它怎么跑起来、怎么存历史、出错了怎么恢复，Anthropic 全包了。**

具体来说，它帮你搞定的事情有这些：

**安全的"工作间"（沙箱环境）：** Agent 在一个完全隔离的容器里干活------可以跑代码、读写文件、访问外部服务，但出不了这个范围，不会碰到你系统里其他的东西。多个任务可以共用同一套环境模板，但每个任务都有自己独立的容器，互不干扰。

**不会失忆的记录系统：** 整个任务过程中发生的每一件事------AI 想了什么、调用了哪个工具、得到了什么结果------都被完整记录下来，存在服务器上，随时可以查看和恢复。就算中途断连，接上之后还能从断点继续，不用从头再跑。

**可以随时看到进展：** 任务不是黑盒。你可以实时看到 Agent 每一步在做什么。觉得它跑偏了，随时可以介入叫停或者纠正方向。这一点对企业来说非常关键------**没有可观测性，就没有信任，就不敢大规模用。**

**Agent 可以版本化管理：** 你定义的这个 Agent 有版本号，改动了可以更新，出了问题可以回滚，历史记录可以审计。企业需要能说清楚"这个 Agent 在某个时间点是什么配置、干了什么"，这套机制直接支持。

**和外部系统连接：** Agent 可以调用各种工具------搜索网页、读写文件、运行代码、连接外部服务（比如公司内部的系统、第三方 API）。Anthropic 还支持 MCP 协议，让 Agent 能对接更多标准化的外部工具。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FGAOdibiana5jGHiaWaUj3YSLvcEWiadNphAibpeYBO7ThrsrcSZMk0T4mqzVpeAfPhF4rvztC1WeVDY9iaCiaF7eWEIL3vGib1jS6iclIS8WFUbAuJu4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

*** ** * ** ***

## 真实案例：从几个月压缩到几天

理解了它能做什么，再来看几个已经在用的公司，会更有感觉。

**Rakuten（日本最大电商平台之一）** 他们用 Claude Managed Agents，给产品、销售、市场、财务、HR 等不同部门分别搭建了专属 AI Agent，各自负责不同类型的任务。每一个 Agent 从零到正式上线：**不到一周** 。如果自己搭同样的东西，要几个月。

**Sentry（代码错误监控工具）** 这个案例最直接。Sentry 的产品本来是帮工程师发现代码 Bug 的。现在他们用 Claude Managed Agents 搭了一个 Agent，流程变成了：代码出现 Bug → Agent 自动分析原因 → Agent 自己写修复代码 → 直接提交一个可以合并的代码改动。**全程不需要任何人工介入。**

**Asana（知名项目管理软件）** 他们在产品里加入了"AI 队友"功能------在 Asana 的项目里，你可以把一个任务直接指派给 AI，它像真正的团队成员一样接手去做。他们的 CTO 说，用了这套系统之后，复杂功能的开发速度大幅提升。

**Notion（知名笔记和协作工具）** 用户在 Notion 里对 AI 说"帮我把这份资料做成 PPT"或者"帮我整理这堆数据做个表格"，AI 直接去做，用户等结果就行，**全程不用离开 Notion 界面** 。而且可以同时跑几十个任务并行------一个人把任务丢给十几个 Agent 同时处理，完全可以实现。

这些公司有一个共同点：它们都是真实企业，在真实产品里，把 Claude Managed Agents 用在了生产环境中，不是演示。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

*** ** * ** ***

## 一个小故事，说明它为什么这样设计

光看功能列表，可能还不太能感受到 Anthropic 做这件事的底层思考。工程博客里有一个真实的故事，我觉得很能说明问题。

他们发现，早期版本的 Claude 在跑长时间任务时，有一个奇怪的毛病：**快撑到"记忆上限"的时候，它会主动提前结束任务，交一份残缺的结果出来。**

Anthropic 把这个行为叫做 **"context anxiety"（上下文焦虑）** ------就像一个实习生，快下班了，任务还没做完，开始慌，然后草草交差跑路。

工程师当时给这个问题打了补丁，在控制系统里做了专门的修复。

后来他们用更强的新模型跑同样的任务，发现：**那个焦虑的行为消失了。** 模型变强了，根本不需要那个补丁了。

这件事让 Anthropic 意识到一个根本性的问题：**AI 模型会不断进化，以前需要靠工程手段打补丁解决的问题，随着模型变强会自动消失。如果底层运行系统是针对某一版 AI 定制死的，每次 AI 升级，企业都得重新搭一遍。**

所以他们把 Managed Agents 设计成了一套"通用底座"：三个部分相互独立------**大脑（AI 推理）、双手（工具执行）、记忆（任务历史）** ，三者解耦，可以分别升级、分别替换，不会互相拖累。

AI 模型升级了，换新模型就行，底层不用动。某个工具出问题了，换工具就行，任务历史还在。用 Anthropic 自己的话说：\*\*"我们要设计一套能容纳未来所有 Agent 形态的基础设施，包括那些我们现在还想不到的。"\*\*

*** ** * ** ***

## 它怎么收费

收费分两部分，逻辑很清晰：

**第一部分，按 AI 用量收费。** 和普通调用 Claude API 一样，AI 输入输出了多少内容，按量计费。这部分没有变化。

**第二部分，按 Agent 运行时长收费。** 每小时 **0.08 美元** ，只在 Agent 真正工作的时候计费，等待或者空闲的时候不收。

第二部分是这个产品最值得关注的收费逻辑。

以前企业自己搭 Agent，运行环境的成本是隐性的------服务器要钱、搭建这套系统的工程师工资要钱、出了问题修复要时间和人力。这些加起来，是一笔不小的数字，但很少有人把它单独列出来算清楚。

现在 Anthropic 把这些成本折算成 0.08 美元/小时，明码标价。对很多中小团队来说，把这笔账认真算一遍，付给 Anthropic 可能比自己搭反而更划算------更不用说省下来的几个月时间。

*** ** * ** ***

## 它现在还有哪些不足

说了这么多优点，也必须说清楚它现在的局限。

**第一，还在 Beta 测试阶段。** 官方文档明确提示：Beta 阶段的功能接口可能随时改动，价格可能调整，稳定性还在持续验证中。用来做试点、小范围验证是合适的，但把最核心的业务全量押上去，现阶段风险不小。

**第二，三个最重要的能力还没完全开放。** 多个 Agent 之间互相协作（让一个 Agent 指挥其他 Agent 分工合作）、Agent 跨任务的长期记忆（今天的 Agent 能记得上周做了什么）、以及任务结果的结构化管理------这三块目前仍是"研究预览"阶段，需要单独申请才能用。而这三块，恰恰是让 Agent 真正像一个"长期在职员工"的关键能力。没有它们，Agent 每次任务结束都像是"失忆"重来。

**第三，目前只在 Anthropic 自己的平台上使用。** 如果你的公司已经深度部署在 AWS 或谷歌云上，Claude Managed Agents 暂时还不能无缝接入那些平台。一旦用进去，切换到其他供应商的成本也会比较高------这是所有云托管服务都有的问题，不是 Anthropic 独有的，但值得提前想清楚。

*** ** * ** ***

## 最后：这件事意味着什么

退一步看，Anthropic 做这件事的意义，比单纯"推出一个新产品"要大得多。

过去三年，AI 公司之间的竞争主要是在"模型层"------谁的 AI 更聪明、跑分更高、代码写得更好。这场比赛还在继续。

但 Anthropic 已经悄悄开辟了另一条战线：**不只是卖"聪明的 AI"，而是把"让 AI 真正跑起来干活"这件事，做成一套可以直接用的云服务。**

你现在用的很多软件------Notion、Asana，或者你们公司的 HR 系统、财务工具------接下来两年里，很可能都会陆续加入"能真正替你干复杂活"的 AI 功能。这些功能背后，很可能就是跑在 Claude Managed Agents 这样的基础设施上的。

搭 Agent 的"地基"问题解决了，那些真正有价值的 AI 应用，才能一个接一个建起来。

这才是 Claude Managed Agents 值得关注的地方。

*** ** * ** ***

*本文基于 Anthropic 官方文档、工程博客及 SiliconANGLE、The New Stack、WIRED 报道综合整理。*

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYzNTY5Mjc2Ng==&mid=2247486412&idx=1&sn=4c7d5620186373eb9642d85d16928c09&chksm=f1a74165f3355a62427ebda4854c36a3117f1c604332af55198662e9a5581d219877fb769968&mpshare=1&scene=1&srcid=0410kSZhk7JStlyevY1agpRL&sharer_shareinfo=8362f2622ae072a48178827f4267d397&sharer_shareinfo_first=8362f2622ae072a48178827f4267d397)

