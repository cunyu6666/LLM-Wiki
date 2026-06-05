---
id: "7267485024465716497"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247766868&idx=1&sn=56a2da0966ea947e03542aa3eba73c45&chksm=e927bd22c7268bacd81d87a42b97629092de0e21e8b78630cb8f268129568ac6292a7a37aa76&mpshare=1&scene=1&srcid=1214sx76nFCIA72EB2YBLoai&sharer_shareinfo=3818a1e604c281f2ba6628766dc3f3de&sharer_shareinfo_first=3818a1e604c281f2ba6628766dc3f3de
author: "关注前沿科技 量子位"
collected: 2024-12-14
tags: []
---

# Ilya宣判：预训练即将终结！NeurIPS现场沸腾

# Ilya宣判：预训练即将终结！NeurIPS现场沸腾

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247766868&idx=1&sn=56a2da0966ea947e03542aa3eba73c45&chksm=e927bd22c7268bacd81d87a42b97629092de0e21e8b78630cb8f268129568ac6292a7a37aa76&mpshare=1&scene=1&srcid=1214sx76nFCIA72EB2YBLoai&sharer_shareinfo=3818a1e604c281f2ba6628766dc3f3de&sharer_shareinfo_first=3818a1e604c281f2ba6628766dc3f3de)关注前沿科技 量子位

##### 金磊 发自 凹非寺
量子位 \| 公众号 QbitAI

继李飞飞、Bengio、何恺明之后，在刚刚的**NeurIPS 2024** 中，**Ilya Sutskever**最新演讲也来了。

虽然时长仅有15分钟左右，但内容依旧看头十足。

例如这一句：
> Pre-training as we know it will end.  
> **我们所熟知的预训练即将终结。**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oDp5cb8CNWpmYyXKNTLHLmlc4zmDtcGgpL5VzM5wMoOkAljLTQOs20A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

而之于未来，Ilya还预测道：
> what comes next is superintelligence: agentic, reasons, understands and is self aware.  
> **接下来将是超级智能：代理、推理、理解和自我意识。**

那么为何会有如此？我们一起来看看完整演讲。

## 回顾十年技术发展

Ilya先是用一张十年前的PPT截图开启了这次演讲，那时候深度学习还处于探索阶段。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oyrfDjvjzxsdia7TuWAbkO6qMyuFJoQmfpBWAyvXmbUK5XK1A2T9XlHA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在2014年的蒙特利尔，他和团队（还有Oriol Vinyals和Quoc Le）首次提出了如今成为AI领域基石的深度学习理念。

Ilya展示了当时的一张PPT，揭示了他和团队的核心工作：**自回归模型** 、**大型神经网络** 和**大数据集**的结合。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9ozEWHaicDqSKg4vY81jE53kk1QK38futYoFXgPbvkTbQHqs5qBicqSJiaQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在十年前，这些元素并不被广泛看作成功的保证，而今天，它们已经成为人工智能领域最重要的基础。

例如在谈到**深度学习假设**时，Ilya强调了一个重要观点：
> 如果有一个10层的大型神经网络，它就能在一秒钟内完成人类能做的任何事情。

他解释说，深度学习的核心假设是人工神经元与生物神经元的相似性。

基于这一假设，如果人类能够在0.1秒钟内完成某项任务，那么同样的任务，一个训练良好的10层神经网络也能完成。

这一假设推动了深度学习的研究，并最终实现了当时看似大胆的目标。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oqhOiaPxfLWB0F8ia498ic2LaJYWEHagREricey485aWqeyrDDlYyxmIneQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Ilya还介绍了自回归模型的核心思想：**通过训练模型预测序列中的下一个token，当模型预测得足够准确时，它就能捕捉到整个序列的正确分布。**

这一思想为后来的语言模型奠定了基础，特别是在自然语言处理领域的应用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9owHmAZSyhuwW7gwunRVq8c77VDfoTWmsbhawp89jfeCKRZgaibQpAvPQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

当然除了"押对宝"的技术之外，也有"押错"的。

LSTM（长短期记忆网络）就是其中之一。

Ilya提到LSTM是深度学习研究者在Transformer之前的主要技术之一。

尽管LSTM在当时为神经网络提供了强大的能力，但它的复杂性和局限性也显而易见。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9ozAf8uJN75LqvIpicmbDks968c7fRBFvdwNWDTyLGNd2qytN8bSYXwjQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

另一个便是并行化（parallelization）。

尽管现在我们知道pipeline并不是一个好主意，但当时他们通过在每个GPU上运行一层网络，实现了3.5倍的速度提升。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oFW5QXIWavh6qYnuV0M9wxpEYsr0rSAlboibgicPTqIQDqzWYQ7v3JZbw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Ilya认为，**规模假设**（scaling hypothesis）是深度学习成功的关键。

这一假设表明，**如果你有一个非常大的数据集，并训练一个足够大的神经网络，那么成功几乎是可以预见的。**

这个观点已经成为今天深度学习领域的核心法则。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oQnfWYyGI5cdic7f6EdDiaG7g9LmdpmzaT9sTMiceq9BWzIZkbSe5e9gWQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Ilya进一步阐述了连接主义的思想，认为人工神经元与生物神经元之间的相似性给了我们信心，认为即使不完全模仿人脑的结构，巨大的神经网络也能完成与人类相似的任务。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oiaT1Hiandib2PibbFsJA9T8Mq2v9tjUz5GIhjuibORQj8cZDADGGcssdz0g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

## 预训练时代即将结束

基于上述技术的发展，也让我们迎来了预训练的时代。

预训练是推动所有进步的动力，包括大型神经网络和大规模数据集。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oYBwUqmM2st3bib4GEaE7xwfewiblQkRmibyibrWO8exRQ2PEvzkRWlTumQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

但Ilya接下来预测说：
> 虽然计算能力在不断增长，硬件和算法的进步使得神经网络的训练效率得到了提升，但数据的增长却已接近瓶颈。

他认为，数据是AI的化石燃料，随着全球数据的限制，未来人工智能将面临数据瓶颈。

虽然当前我们仍然可以使用现有数据进行有效训练，但Ilya认为这一增长趋势终将放缓，**预训练的时代也会逐步结束**。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oFnULNcbErd4KxZxSxQ5WUl9wgl69O595o3F8IUXJa5Ry4H7wWmkXCQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

## 超级智能将是未来

在谈到未来的发展方向时，Ilya提到了**"Agent"和"合成数据"**的概念。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9oYXaARk3xVj3WBQhbicEvZUpzR7oXbtZoYk7A4KXKw2ZubtlY2FXGe4g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

许多专家都在讨论这些话题，认为Agent系统和合成数据将是突破预训练瓶颈的关键。

Agent系统指的是能够自主推理和决策的人工智能，而合成数据则可以通过模拟环境创造新的数据，弥补现实世界数据的不足。

Ilya还引用了一个生物学上的例子，展示了哺乳动物身体与大脑大小的关系，暗示不同生物可能通过不同的"规模法则"进化出不同的智能表现。

这一思想为深度学习领域的进一步扩展提供了启示，表明人工智能也许可以通过不同的方式突破目前的规模限制。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYicUhk5aAGtDYeFHH0Eo3ubYicRPMwPo9or0aOibpYO2BEkYIleSAxqSW0O7HWFQnupvy3XlMIozSrfjACLSgVfYg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Ilya最后谈到了**超级智能**的前景。

他指出，虽然当前的语言模型和AI系统在某些任务上表现出超人类的能力，但它们在推理时仍显得不稳定和不可预测。

**推理越多，系统变得越不可预测**，这一点在一些复杂任务中表现得尤为突出。

他还提到：
> 目前的AI系统还不能真正理解和推理，虽然它们能模拟人类的直觉，但未来的AI将会在推理和决策方面展现出更加不可预测的能力。

Ilya进一步推测，未来的AI将不仅仅是执行任务的工具，而会发展成"Agent"，能够自主进行推理和决策，甚至可能具备某种形式的**自我意识**。

这将是一个质的飞跃，AI将不再是人类的延伸，而是一个具有独立智能的存在。

参考链接：  
https://x.com/vincentweisser/status/1867719020444889118

--- **完** ---

**点这里👇关注我，记得标星哦～**

![](https://image.cubox.pro/cardImg/14z8gf5kbumqt19jevpu5db2zudnou01s2jjqjv5of2bi3c0k8?imageMogr2/quality/90/ignore-error/1)

**量子位**

追踪人工智能新趋势，关注科技行业新突破

3184篇原创内容

<br />

公众号  

，


**一键三连「分享」、「点赞」和「在看」**

**科技前沿进展日日相见 \~**


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_svg%2Fg9RQicMD01M0tYoRQT2cMQRmPS5ZDyrrfzeksiay90KaDzlGBH61icqHxmgFKfvfXtVuwTHV740CDLAaXU1LIfZyoJEpYKcRIiaE%2F640%3Fwx_fmt%3Dsvg)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247766868&idx=1&sn=56a2da0966ea947e03542aa3eba73c45&chksm=e927bd22c7268bacd81d87a42b97629092de0e21e8b78630cb8f268129568ac6292a7a37aa76&mpshare=1&scene=1&srcid=1214sx76nFCIA72EB2YBLoai&sharer_shareinfo=3818a1e604c281f2ba6628766dc3f3de&sharer_shareinfo_first=3818a1e604c281f2ba6628766dc3f3de)

