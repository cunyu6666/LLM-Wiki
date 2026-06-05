---
id: "7289988556955583837"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247777378&idx=1&sn=607ad9a38ea24ac57470ef8f7d37f9b9&chksm=e95001aaceae7caa6838a8e8e23f8f8600ec3988c5b2ed2a45e5699587c776263c63e0188970&mpshare=1&scene=1&srcid=0214RsyOqc1jSJtHtTww2lIs&sharer_shareinfo=83923479b5148cfa2d3dc7c9e0167e65&sharer_shareinfo_first=83923479b5148cfa2d3dc7c9e0167e65
author: "关注前沿科技 量子位"
collected: 2025-02-14
tags: []
---

# DeepSeek缝合Claude，比单用R1/o1效果都好！GitHub揽星3k

# DeepSeek缝合Claude，比单用R1/o1效果都好！GitHub揽星3k

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247777378&idx=1&sn=607ad9a38ea24ac57470ef8f7d37f9b9&chksm=e95001aaceae7caa6838a8e8e23f8f8600ec3988c5b2ed2a45e5699587c776263c63e0188970&mpshare=1&scene=1&srcid=0214RsyOqc1jSJtHtTww2lIs&sharer_shareinfo=83923479b5148cfa2d3dc7c9e0167e65&sharer_shareinfo_first=83923479b5148cfa2d3dc7c9e0167e65)关注前沿科技 量子位

##### 梦晨 西风 发自 凹非寺
量子位 \| 公众号 QbitAI

让**DeepSeek代替Claude思考**，缝合怪玩法火了。

原因无它：比单独使用DeepSeek R1、Claude Sonnet 3.5、OpenAI o1模型的**效果更好**。

先来看一段VCR：

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

再来看一个测评结果：

在**代** **码编辑基准**Polyglot Benchmark上，缝合模型效果小超o1-high和R1一头。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajR6SwRdWoVShNGynFro9JoYA2uhoUVzOFTIKNgv17FQwqtX7UFaLUgMw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在这个测试中，**R1扮演架构师**，描述如何解决代码问题。

而**Claude扮演程序员**，按要求生成特定的代码编辑指令，以便把改动应用到源文件中。

除此之外，实验过程中还得出还有几个有意思的结论：

* **o1与Claude Sonnet搭配**效果并不如单独使用o1。

* 使用R1或o1当架构师，**Claude之外的其他模型当程序员**，效果都不如单独使用R1或o1。

* 但**o1-preview和o1-mini当架构师** ，使用很多不同的模型当程序员都能提高组合的成绩。

* 使用R1的推理过程token效果**不如使用R1的最终输出token。**

这样看来，R1和Claude Sonnet还真是一对绝配啊～  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRA9LG3fpq3b2FFOS6qyfhRB3ia3fj6leq25BeRYUMbzddWqcLgUj7V1g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

DeepClaude应用本身100%免费且开源，在GitHub上已揽获3k星星（当然API要用自己的）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRuhpia2OGNwjAd58I1HqlMZQWIA9N4oCGKRBblPZrY0rISCMx0cwZlJg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

网友测试后总结到：Claude擅长撰写清晰、结构良好的文本和代码，因此它能将DeepSeek-R1的想法转化为精炼的回复。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRd9ZSTR32ibhkAicSue5DcCVhIv9Q6MIkBnVq1HY16SYx8rvUdCMhCHtA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

DeepClaude作者之一对此有感而发：
> AI智能体和智能体应用正在展示出一种"数字世界优先"的范式转变，智能系统正在成为主动的合作者，而不仅仅是被动的工具。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajR2x2gEJYlAhr0pUhqWgnibtaDx5liaD8gxPRGSIa6Zt6AocLx8zW26hPQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

## DeepSeek和Claude的混血儿

具体来说，DeepClaude是一个LLM推理API，通过Rust编写。

它提供了一个统一的接口，将DeepSeek R1的CoT逻辑推理能力和Claude的回复**在单一流中无缝衔接**。

开发者可以通过这个API同时调用两种模型的功能，还能完全掌控自己的API密钥和数据。

打造它的团队名为**Asterisk** ，团队成员具有安全研究\&CTF（Capture The Flag）背景，致力于利用AI让检查代码安全这事儿变得更加高效。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajR09eVDUs1RefibpiaWUMKjg0micpnnk2e5hlnbPxvtQicl4o1rS9wzLAfTQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

团队认为，DeepSeek R1的CoT深度推理甚至达到了LLM具有反省认知（metacognition）的程度，它能够自我纠正、思考不常见/极端/特殊的情况，并在自然语言中进行类似蒙特卡洛树搜索（MCTS）的推理。

不过R1在代码生成、创造力和对话技巧方面有所欠缺，Claude 3.5 Sonnet在这些方面表现出色，刚好可以作补充。
> 何不将两者结合起来？取两者之长，打造出DeepClaude～

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRzUSNdHDcoJp5zIFwNZ7z7hhfiaUr20Ds7FsIl1S93YymQHbibibxtb3qg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

对话中，Claude回应之前，系统会显示"\<thinging\>"这样的预填充文本。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRKMuibz3OjfibQXLoTicEichkvdYO6152jhiaiaHJbDoLIAjUxPjNOK1Y7yxQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

DeepClaude结合了这两种模型，具有以下特性：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRFOWXLvYYfbDgfeM1t206ibIhZ7bG2IT1xZfVatJn6RdKbWM13d9Hic8Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

托管API完全免费，允许用户使用自己的密钥，并将DeepSeek和Claude的流式API整合在一起，提供计算组合使用量和价格等便利功能。

代码是开源的，用户可以自由托管、修改和重新分发。团队表示它已经在Asterisk的生产环境中大规模使用，每天处理数百万token，至今尚未出现故障，只要不滥用就行。

## One More Thing

你以为两个模型缝合就是极限了吗？

No no no

还有网友开发出了**三缝合玩法**，将DeepSeek-R1和Gemini 2.0 Flash的思考结果组合起来，在让Claude Sonnet去回答问题。

在GPQA测试（谷歌搜不到的理化生博士级选择题）中也取得了好成绩。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtBlCRkldhsLxicicTpbVibaajRiaAxgicMkYtfic0B1M1BicezgQjiacRgK35gVO4BfKQK73LlK1QzeIWJetA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Github地址：https://github.com/getasterisk/deepclaude

参考链接：  
\[1\]https://aider.chat/2025/01/24/r1-sonnet.html  
\[2\]https://x.com/deepclaude_/status/1886911416478642279  
\[3\]https://x.com/omercelik/status/1883510797193937278  
\[4\]https://x.com/mufeedvh/status/1883620781583901011


--- **完** ---


**评选报名** ｜**2025年值得关注的** **AIGC企业\&产品**

下一个AI"国产之光"将会是谁？

本次评选结果将于4月中国AIGC产业峰会上公布，欢迎参与！


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDllXZe5ic5ib8mZ2TdBHbfWiaTd0hVeY2Yvno55e5cxNU2nLBWNLrZSVowHAewCyv6kyXhDx6VnicNMQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

**一键关注 👇 点亮星标**

**科技前沿进展每日见**


![](https://image.cubox.pro/cardImg/14z8gf5kbumqt19jevpu5db2zudnou01s2jjqjv5of2bi3c0k8?imageMogr2/quality/90/ignore-error/1)

**量子位**

追踪人工智能新趋势，关注科技行业新突破

3249篇原创内容

<br />

公众号  

，


**一键三连** **「点赞」「转发」「小心心」**

**欢迎在评论区留下你的想法！**


[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247777378&idx=1&sn=607ad9a38ea24ac57470ef8f7d37f9b9&chksm=e95001aaceae7caa6838a8e8e23f8f8600ec3988c5b2ed2a45e5699587c776263c63e0188970&mpshare=1&scene=1&srcid=0214RsyOqc1jSJtHtTww2lIs&sharer_shareinfo=83923479b5148cfa2d3dc7c9e0167e65&sharer_shareinfo_first=83923479b5148cfa2d3dc7c9e0167e65)

