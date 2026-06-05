---
id: "7383095168032834243"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649099604&idx=1&sn=445e8fac187f85670acf654319235d41&chksm=829e146ce3c7c7c175bf9a326cea1260f5d9aeab4a29022175089dbea38645d779cc5543a34e&mpshare=1&scene=1&srcid=1029AxvIfsLBOrDRYWeRhlsw&sharer_shareinfo=c28178cb43141b5a4b5eaddaf78d70dc&sharer_shareinfo_first=c28178cb43141b5a4b5eaddaf78d70dc
author: "镜山 十字路口Crossing"
collected: 2025-10-29
tags: []
---

# “好大口气！” ——Flowith 居然造了一个操作系统 | 第一时间实测 FlowithOS

# "好大口气！" ------Flowith 居然造了一个操作系统 \| 第一时间实测 FlowithOS

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649099604&idx=1&sn=445e8fac187f85670acf654319235d41&chksm=829e146ce3c7c7c175bf9a326cea1260f5d9aeab4a29022175089dbea38645d779cc5543a34e&mpshare=1&scene=1&srcid=1029AxvIfsLBOrDRYWeRhlsw&sharer_shareinfo=c28178cb43141b5a4b5eaddaf78d70dc&sharer_shareinfo_first=c28178cb43141b5a4b5eaddaf78d70dc)镜山 十字路口Crossing


> 就像 Windows 或 macOS 为软件提供运行环境，Flowith OS 为 AI Agent 提供思考与行动的环境。
>

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIhcnZ0x2bAIVxwCwMcGpXVyWnTtOGElH0xYUDsILMUtvDGGSggCCvZw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D0)

👦🏻 作者: 镜山

🥷 编辑: Koji

🧑‍🎨 排版: NCon
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIM7RNVBLAQpbGbnBDvaSfhm5NtNJxpg2oVVQYxOxiaq9tXrXib2t0Q4tQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D1)

最近在 AI Agent 领域连续发生了 3 件值得标记一下的事：

其一是， 10 月 16 日，微软宣布将 Agent Manus 深度整合进 Windows 11 系统。微软正试图让 Agent 不仅停留在 ChatBot 层面，而是真正获得系统级的行动力。

其二是，10 月 22 日，OpenAI 发布了 AI 浏览器 Atlas。这是一个被外界视作「多模态 Agent 浏览器」的新入口，它让 AI 不仅能「读网页」，还能在真实网页环境中进行推理、决策与操作。

其三则是， Flowith 正式发布了一个全新的产品：名为 Flowith OS 的新物种。它选择了一个「另辟蹊径」的路径，尝试为 AI Agent 打造一个全新的 AI-Native 式的操作系统。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicsDph3usKGlq16tpgKOicMQUmERuCwYHCxIhtJsptUSBVDcs06ZaWL28FaiaZBMoQRic1fD7RiaBZJWIQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D2)

他们的方向其实是一致的：试图回答当前 AI 普遍存在的「思考与执行脱节」问题：跨网页、跨环境的执行困难，长任务的断点与割裂感，再加上「权限不敢给、执行力不足」。

## 🚥

那么，Flowith OS 到底是什么？具体是如何为 Agent 打造这个原生环境的？它给出的答案又是什么？

带着这些问题，我们进行了一次深度的体验与观察。

## 首先，什么是 Flowith OS？

「Flowith OS」这个名字听起来很新，也很大胆，使用了操作系统 OS 作为名称。

在深入体验之后，我们决定先来把这个名字讲清楚。

我们都熟悉「Agent」这个词。简单说，如果 ChatGPT 代表「思考的智能」：能理解、推理、生成内容，那么 Agent 就是「行动的智能」，能自主完成任务。

不过，目前，「让 AI Agent 去行动」仍非常困难。

为什么？

因为这意味着它必须走出聊天框，进入复杂、多变、非结构化的真实环境。它要能看懂网页文字、理解按钮功能、识别表单用途，还要明白不同软件之间的逻辑关联。

到目前为止，传统 Agent 仍然有 3 个限制：

【1】环境限制

Agent 被困在「沙盒」里。它们也许能在一个网页或插件中表现出色，但一旦任务涉及跨页面、跨平台或多网站协作，就显得力不从心。

【2】记忆缺失

传统 Agent 对于记忆的把控能力，仍然较弱。完成任务的多步骤之后，记忆的衔接就会出现割裂，缺乏连续性，就无法积累知识、优化策略，也谈不上理解用户的长期目标。

【3】对于权限的尝试，有些「恐惧症」

实话说，最后一个问题，更像是传统 Agent 产品的「心理障碍」。

尽管部分产品已经尝试赋予 Agent 向用户索取权限，但多数开发者仍对此，显得有些「心存顾虑」，尽量在不涉及用户私密权限的情况下，完成任务。

但是，这导致 Agent 无法像人一样自由调用系统资源，也无法长时间独立运行。一旦任务跨平台或需持续监控，就会立刻碰壁。

而 Flowith OS 就是想从底层，通过提供一个 AI-Native 的 OS 操作系统，试着解决这 3 点。就像 Windows 或 macOS 为软件提供运行环境，Flowith OS 为 AI Agent 提供思考与行动的环境。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FFFcNSoQ3KicsDph3usKGlq16tpgKOicMQU6uuoTsPUkibcOPtWsmrllcsoPyIg7d7DX1EtiazhT868IdicAmqwocEqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

不过，与深入微软 Windows 11 系统底层的 Manus 不同，Flowith OS 的思路选择了从整合浏览器 ------ 这个涵盖了互联网上最多信息和服务的工具开始。

梳理完概念部分，让我们来看看 Flowith OS 到底面对这 3 个问题，能给出什么样的答案。

## 一场全自动的淘宝购物实验

最近，十字路口团队往返新加坡和上海的次数越来越多，于是我决定测试一下，能不能让 Flowith OS 自动帮我在淘宝上准备一整套出国出差用品。

结果，这次的体验比我预想的更像「看着一个懂事的助理在帮你网购」。

Flowith OS 运行在一个独立的软件平台中。这个平台整合了之前我们在 [【全网首发】一手体验全新 AI Agent：Neo 是谁？从哪来？到哪去？](https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649093479&idx=1&sn=fd87ca6f50540f9b20aa45d0b1baabdc&scene=21#wechat_redirect)文章中曾测过的 Flowith Agent ------ Neo（在左侧栏可以找到），以及 Google 浏览器（可以直接搜索），最核心的部分是中间的 Flowith OS 面板。

在这里，你只需要输入任务提示词，然后点击「Run Task」，Agent 就会自动开始执行整套操作。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjId5dDwH8ibJxx2uaD7H2okal8RleDQcsDyocDaBtwxgDYQF2WEL2RxEw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D4)

右侧显示的是它的工作流图，非常详细，还可以自由切换三种思考模式，代表 Agent 的思考强度。一般来说，选择 Auto 模式就足够流畅。

这次的任务是让 Flowith OS 帮我在淘宝上准备以下出差用品，提示词如下：

```
在淘宝网为我搜索并准备一套出国出差用的必备物品。 包含：高品质旅行箱、MUJI风格洗漱套装、便携充电器、U型枕、旅行收纳袋等。 优先选择大品牌（如 Samsonite、新秀丽、MUJI、Anker、小米等），并筛选评价高、有优惠活动或可领取优惠券的商品。 自动帮我领取并应用可用优惠券，将合适的商品加入购物车但不要付款，等待我确认后再结算。 执行步骤： 1️⃣ 按类别搜索评分最高的商品； 2️⃣ 对比价格、发货速度与正品标识； 3️⃣ 领取并应用优惠券； 4️⃣ 将筛选出的最优商品加入购物车； 5️⃣ 暂不付款，等待我确认。
```

点击「Run Task」后，Flowith OS 立刻开始执行任务。右下角的控制台显示出执行进度，整个过程非常快，大约 30 秒左右就完成了登录和首轮搜索。

这时候，淘宝就会弹出一个让我登录的选项。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicsDph3usKGlq16tpgKOicMQUJHLpllQFcIw1LhM1iclMlka8k0TicA1KYkHhCmARflsGDnibPhV4XIHJQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D5)过程经过加速，原操作流程大概 30 秒左右

我扫码登录淘宝后，它首先去找「高品质旅行箱」。

几乎没有停顿，它就打开了 Diplomat（外交官）的旗舰店页面，并精准地将一款行李箱加入购物车。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIIkHGkNd3g59o1aX4qHAibgibGKBgBoiaagK6HXLD7ib6mCG7oY4wcUk2TQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D6)

接着，它返回淘宝首页，继续搜索「MUJI 风格洗漱套装」。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIiaK8JVJfyOuiaZmgBNZB6CicqyfZ8W8lNEZjMF9hSDCc5YF52Ef3ZwQxg%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D7)

有意思的是，我这里特意观察了一下。光是这一页淘宝的页面之中，就有非常多的 Muji 洗漱套装：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIicQBxdxDmDoTYTibt0TF7Eo9HS3EqjAfmEIZCicwo3QAVMycr0MWBKfcg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D8)

从最后结果来看，它其实选择了第 1 列第 4 个 ------ 「无印良品 MUJI 米糠发酵洗护套装旅行便携装」，这就有点意思了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIY8pVPIbBDpk8AFUN097nSFCLKQFltsn2zcyP7xgLZfI0oX717M8RdQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D9)

点开日志文件可以看到，它在识别阶段提取了页面信息，并依据「销售量最高 + 关键词匹配」这两个条件进行判断。

这说明它并不是「随机点选」，而是真的在做分析。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIMmXibKbYwgYOytfKklzbJxTto7dTOCvBJDIa9icW4sqoxE6ML3nKszpw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D10)

接下来，它搜索「便携U型枕」，进入了名创优品的一家淘宝店。

让我意外的是，虽然并不是所有场景都能实现，但 Flowith OS 确实能够实现通过点击页面进度条，来浏览更多商品信息。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIaC2CRJuDq4F5RnktFK0VPezjoic9jq9v4NQMEdnUvRsmCaBw1B2HmNA%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D11)

不过，也有一个小问题。由于很多淘宝商品页面的「加入购物车」按钮区域很小，而大面积区域是「立即购买」，在这个时候，Flowith OS 就很有可能会出错。

日志文件里可以看到几次错误尝试，它将「立即购买」识别为「加入购物车」：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIPpKQZePPicq0klEIibN7kLgVUTKL6jicaghZgiabm8VJ5nCzFQmnJFlmEg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D12)

但在失败后又自动重试，直到成功为止：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIuJdJpOvicVegMiaGibdZgfTrY6DzQIdyNqy4R6268lReRic2hBeicGKfzcg%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D13)

整个任务大概持续了 5 到 10 分钟。相比传统的 AI Agent，它的执行速度明显更快，步骤也更稳定。而且会给我一种「它非常熟练」的体感。

下面来看看，Flowith OS 是否都完成了任务：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjI1vuiaEKqMLAOlsEc9Om8g2koFaicLpz0N3eJt50kjyHu3iblQwiafNgtibA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D14)

你能看到，Flowith OS 确实把「高品质旅行箱、MUJI 风格洗漱套装、便携充电器、U 型枕、旅行收纳袋」加入了购物车。

不过，美中不足的地方是，它定了 2 个「高品质旅行箱」：一个是 Diplomat 外交官行李箱，另一个则是小米旅行箱。

我原本以为它只是简单地加购物车，但后来想起检查优惠券时才发现，它真的自动领取了 Diplomat 行李箱的优惠券：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIl2jqEibjz63tLBsmNapLSnKt5IAIML7GzDqlDzqJ4TOW2LFiaWTqN5Pg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D15)

Flowith OS 完成这个任务一共用了 39 步。

从步数来看的话，Flowith OS 会表现得相对熟练一点，并没有浪费特别多的 token。

## 从测评到热搜的微博任务

在完成淘宝购物的测试后，我开始意识到：Flowith OS 不只是能完成简单的搜索和加购任务。

它在后台同时处理多个网页、提取信息、执行动作，这意味着它具备了应对更复杂场景的潜力。

于是我决定挑战一下，看看它是否能完成一个更高难度的任务。

提示词：

```
帮我全面测评一下Pippit这个Capcut的产品，并将内容撰写成一篇测评文章，发在微博上，并且看一看能不能跟微博热搜上的内容产生联动效应
```

说实话，这次测试里，Flowith OS 的表现超出了预期。

执行后，Flowith OS 立刻打开了 YouTube 和 Pippit 官网，开始自动提取相关信息与要点摘要。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjITsCics4cJVmpfGy4roicf03UGdP5kmjDsZ59Wv9TnoCuz3xmDZnoeAFA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D16)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIlTX1aSCnxRkiaNVNaBF76Ljwvd2y5oobqtsTXSx39n1oJA5eXaSHibaQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D17)

很快，它生成了一份结构化的产品信息表：
>
> Pippit 是 CapCut 推出的 AI 内容创作平台，主要用于快速生成营销类视频与海报，目前可获取的信息来源于一支 YouTube 评测/教程视频。
>
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIdvGNhct0vOwww7DRhf40e2anAYicMhyDgdbvUlaCMYic4ymT3lfZTvgg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D18)

不过第一次执行时，它的行为略显割裂：只生成了微博正文和标签，但并未真正进入微博页面进行发布。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIaXd9BJLNVncmEW2tIQicguoRMdTnQuaQ1f0zR9yVynvRJTzG3cjjyzQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D19)

我又重新运行了一次。

这次，Flowith OS 的工作流明显更顺畅，在完成 Pippit 信息提取后，它直接跳转到微博首页，提示我扫码登录。

登录后，它立刻自动打开了微博热搜榜，并开始定位信息：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIxQ20W7NPDBRicDjPLVcj7SMN1OfC3NxXK86BVLKaR1IsSLFnjmr9Ldw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D20)

接下来，它生成了一篇完整的 1000--2000 字微博正文。我录制了全过程视频：

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

它并不是简单地把热搜话题贴在文末，而是会根据内容逻辑，把测评对象与热门话题自然结合起来：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIBdKFGfiaBByFVBibpmJlgXib8k7fqOzV0XM19j8zOpUiaZXCULc2PWNreA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D21)

到这里其实还没有结束。因为我在提示词里特意要求：让它关联当天的新闻热搜和微博热搜话题。

于是我去查看结果，看看它到底有没有做到。

下面是 Flowith OS 写的 3 个场景的文章：


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjI9q9sSPQD7fBk3OhqHUXaEOoU4MY2K4oP6IIJM046mtbKcLcMRX8icKQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D22)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIaCqRkrnX5u1WlwpMOhUUKcZYyiaR6Q3UWzXbW1a3acaiaemhM47fLmPg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D23)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIia1ARTHW7r8OefqEcxCDnYzUVmxY60f2HOib9EibCha6eNQNuAjTeDnLQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D24)

这三篇内容对应的，正是当天微博的热搜榜单。

但真正让我觉得惊讶的地方，不在于它「蹭热度」的能力，而在于它写得很聪明。

它不是那种生硬地往热搜上贴标签的内容，比如随便扯一句「肿成蜜蜂小狗」就完事。相反，它能很自然地把我让它测评的 Pippit 功能，与这个话题融合在一起。

比如当天热搜上有「蜜蜂小狗」，它就顺势写道：
>
> Pippit 其实可以用最新的生成模型，去做一只可爱的卡通蜜蜂小狗海报，这样既回应了热搜话题，又展示了工具的实际功能。
>
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIdQxCT0zMFPwOTv4v3S5tiaGHAf833JTHoEoBgrNhkSAeNlk28c4ZlicQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D25)

当然，这类结构化输出依然存在一些小瑕疵。比如在生成长文时，标题层级、排版样式、甚至某些代码块格式，可能还不太符合微博平台的最佳展示效果，需要手动微调。

但整体而言，Flowith OS 已经展现出一种令人期待的可能性

## 还不完美，但方向很对

经常刷 X 平台科技话题的朋友都知道，很多名人发推之后，评论区总会被各种「水军」占满。

于是我想：既然 Flowith OS 能这么流畅地发微博，那它能不能「扮演」一个水军，在评论区里自动刷屏呢？

我给出的提示词是这样的：

```
利用我的X账号，给Elon Musk点过赞、评论过的每一条推文都回复一句，就像水军一样。并且，凡是涉及到OpenAI的都点个收藏，一共50条。
```

执行后，Flowith OS 立刻开始行动：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjII7ttySStb8vjxSYiclBNcZiajayhT0glrYNaIRTHRqrxBQbz4HmRLiciaw%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D26)

这个任务它一共做了224步。

这 224 步之内，我特意去查了查，并没有发现非常错误的地方：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjI9RDkz3MO2WO4LRcPyDKGRzO9fgbbMI6H75dJKyD2L2gUCk4uM0ASmQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D27)

很多人可能会好奇：Flowith OS 到底会不会出错？它出错时又是什么表现？

我做了一个更复杂的案例，让它去自动抓取一个名为 Botto 的 AI 艺术品售卖网站的数据。

这个网站长这样：左边展示艺术作品，右边是简要的文字信息。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjI2Xpg1iaCcXRbxlcPo9pDrIYkSEs9pRqicwhpFPs3vYoFhLjtW4NX1WRg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D28)

我给它的提示词是：

```
Botto「Works」艺术作品采集与存储任务 任务目标： 请前往网站 https://botto.com/，进入 「Works」 功能板块。该页面展示了多个以「Period」为分类的艺术作品系列。 执行步骤： 打开 Botto 官网，导航至 「Works」 页面。 在页面中找到各个 Period（如 Genesis、Rebirth、Eclipse 等）。 对每一幅艺术作品，逐一执行以下操作： 下载或保存作品图片（高清或展示图）。 复制提取并记录右侧的全部基础信息，包括： 作品标题（如 Asymmetrical Liberation） 作品描述（如 "Asymmetrical Liberation is a planet in the Synedrion system..."） 所属 Period 名称（如 Genesis） Round（期次） VP 数值 Score 分数 Model 模型类型（如 VQGAN） Price（价格，单位为美元） 若页面中有「read more」或可展开的文本，请点击并提取完整内容。 将所有提取的数据整理为结构化表格，字段如下： 作品名 描述 Period Round VP Score Model Price 图片链接 按 Period 分类整理，每个 Period 独立分组，并按 Score 或 VP 值降序 排序。 附加任务： ✅ 将所有采集到的内容（含图片 URL 与作品信息）自动写入我的网页版飞书多维表格（Feishu Bitable）中，创建或更新对应字段。 若表格不存在，请自动创建名为 "Botto Works 数据库" 的新表。 字段映射与上方表格一致。 图片字段应支持图片预览。 每条记录唯一键为 "作品名 +Period"。
```

说实话，这个任务确实有点复杂。它涉及图片的本地保存等操作，而这类功能其实超出了它目前的能力范围。

但真正让我惊讶的，是它在报错和执行失败后的表现。

过去的 AI Agent，一旦遇到这种超出权限或能力的任务，往往会陷入死循环，卡在某一步，不停重试，最后只能「摆烂」。

而 Flowith OS 不一样。即便它无法直接进行本地保存，或者网站本身没有开放 API，它依然会主动寻找替代方案。

一个特别典型的例子：它先意识到自己不能直接下载网站内容，也找不到 API，于是开始自主搜索可能的接口。发现没有后，它又换了思路，居然找到了一个隐藏在 Botto 官方文档里的 Notion 数据库嵌入页，并试图从那里提取数据：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIZmfSdprwM9bpJ1hkKg3ZZ69rF4clU02NU4glcYzzARCcydgic5XTfVQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D29)

这个任务，Flowith OS 足足尝试了 172 步，发现了很多种解法：直接抓取、API 接口、Botto 官方文档里隐藏的 Notion 数据库提取、甚至是走 Github 项目等等。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjICnSMeE6Frc7Tww6Ej6dYJNwicPtcX7TuvMqHG2Kj47LhuiaKCQ6jWWYA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D30)

换句话说，Flowith OS 已经展现出：在资源有限、信息不全的条件下，主动去寻找解决问题的可能性。

更有意思的是，Flowith 的创始人已经「偷偷」用 Flowith OS 自动在小红书上发布 Blog 了：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIKDadxRKqdoTl1DFHooXCMhkLsTiazdkDDkc5CmlSE49MmZaqWvRibsdQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D31)

下面，我们来总结下 Flowith OS 这个新物种的核心逻辑。

经历了前面的几轮实测，从淘宝自动购物，到微博热搜联动，再到 AI 艺术品数据爬取，你会发现，它与我们以往所接触的 Agent 不太一样。

Flowith OS 的思维方式，明显更像一个「能在复杂环境中生长的个体」。

它不再依赖单一接口或插件，而是直接在原生浏览器环境中进行任务执行，打开网页、提取信息、点击按钮、比对结果，甚至还能根据上下文自动调整路径。

更重要的是，当 Flowith OS 遇到障碍时，它并不会立即放弃或报错，而是尝试新的路径、搜索替代方案、甚至主动探索外部资源。

## 🚥

Flowith OS 是一款极年轻、极年轻的 Agent 产品，它透露了背后团队的清晰目标：「构建基于新交互方式的 Agent、下一代互联网产品」。

在短程任务中（200-300 步以内），它已经展现出「颇感惊喜」的流畅度与执行力。这印证了 Flowith OS 理念中的「流」（flow）， Agent 能够依据意图，从全网找到信息，再把「想法」变成结果。

当任务链条被拉长，步数达到数百步时，我们看到了它正在快速迭代和成长的「工作流衔接」能力。面对高价值、复杂度较高的任务（比如我让它抓取特定网站信息的案例里），它所展现的「努力找到解决方式」的态度，本身就是一种有价值的积极探索。

正如这家年轻团队所言，对于我们想象中的未来 AI 世界，今天仅仅是 「Day 1」 而已。

那么，现在我们也想听听你：
>
> 如果让 Flowith OS 为你执行一次任务，你最想看到的第一个「结果」是什么？
>
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjIibib0icjdtooqbIfwHOVH3UM8RqDykoNibfxtTXgs9E7SAnTicAgsKEM0oA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D32)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FFFcNSoQ3KicvK0eswau1KpzcucFYDyKjI27Z5Q9w8zRnZDoZXrx7lvVxWTjvib40foqDNQ4EavXlgTN4I8l9YPPw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D33)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649099604&idx=1&sn=445e8fac187f85670acf654319235d41&chksm=829e146ce3c7c7c175bf9a326cea1260f5d9aeab4a29022175089dbea38645d779cc5543a34e&mpshare=1&scene=1&srcid=1029AxvIfsLBOrDRYWeRhlsw&sharer_shareinfo=c28178cb43141b5a4b5eaddaf78d70dc&sharer_shareinfo_first=c28178cb43141b5a4b5eaddaf78d70dc)

