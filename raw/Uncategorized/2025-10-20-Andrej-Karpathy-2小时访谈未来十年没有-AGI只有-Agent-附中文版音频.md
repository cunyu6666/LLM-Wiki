---
id: "7379766374861637471"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247507121&idx=1&sn=24fa549e79321c46fc1db45a73613f22&chksm=c32cd265a9cda41507bed895eb89d32515308f3d01cc0342ee2e158cc81d683c860c6f692523&mpshare=1&scene=1&srcid=1019ZX0FYSATWLvZv9mTI59A&sharer_shareinfo=c5c3f6de771bba09c561282888dfeed4&sharer_shareinfo_first=c5c3f6de771bba09c561282888dfeed4
author: "金色传说大聪明 赛博禅心"
collected: 2025-10-20
tags: []
---

# Andrej Karpathy 2小时访谈：未来十年，没有 AGI，只有 Agent ｜附：中文版音频

# Andrej Karpathy 2小时访谈：未来十年，没有 AGI，只有 Agent ｜附：中文版音频

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247507121&idx=1&sn=24fa549e79321c46fc1db45a73613f22&chksm=c32cd265a9cda41507bed895eb89d32515308f3d01cc0342ee2e158cc81d683c860c6f692523&mpshare=1&scene=1&srcid=1019ZX0FYSATWLvZv9mTI59A&sharer_shareinfo=c5c3f6de771bba09c561282888dfeed4&sharer_shareinfo_first=c5c3f6de771bba09c561282888dfeed4)金色传说大聪明 赛博禅心


看了 Andrej Karpathy 的播客，信息量巨大

开篇泼冷水：  
**未来十年没有 AGI，只有 Agent**

这里说一下，Karpathy 是 OpenAI 早期成员，参与过 GPT 背后的技术路线，在一线干了 15 年  
同时，Karpathy 也是前特斯拉 AI 总监

原始视频在这里

<br />

赛博禅心  

，赞   
18  


同时，我制作了一份中文版音频  
使用的工具，是[大橘子的 ListenHub 的 API](https://mp.weixin.qq.com/s?__biz=MzkwMzY5NzU2Nw==&mid=2247486898&idx=1&sn=5e4bfa9568f79de98b746a606a94e4fa&scene=21#wechat_redirect)  
（我弄了一整个周日，非常良心）

**【中文复刻】Andrej Karpathy 2小时访谈** ,赛博禅心 ,1小时42分钟 进度条

这里，我还准备了一份文字实录，中英双语
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB69V4xqpPC0mXcWAiaEeqGV7vkUGQUP0OrZzk3qRajhoYEwN9JTr8f5pA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)中英双语，非常贴心

公众号回复 **ak1019** ，即可获取

在 Andrej Karpathy 眼中，当前的 AI Agent，核心问题有三个：

*
  • **continual learning** ：你告诉它一个事，它记不住
*
  • **multimodal** ：真正的多模态还没做到
*
  • **computer use** ：不能像人一样操作电脑

这三个问题，每一个都得花好几年解决

*** ** * ** ***

## AGI 还要十年

有人说今年是 Agent 之年  
Karpathy 表示：应该叫「agents 的十年」

在他的观点里  
我们未来十年没有 AGI，只有 Agent  
业界有很多 over-prediction  
对于 AGI 大家都太乐观了
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6kFIWnD4RZ93RkLOQ22Phc1f7BsuqA7z4ibbWtWeXlqQ7MsIzXoGnia1g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)Andrej Karpathy：AGI 需要十年

他举了个例子  
你现在有 Claude、有 Codex，对吧，很厉害  
但你会让它们替你干活吗？不会

为什么？  
因为它们就是不行

智能不够、多模态不够、记不住东西、不能操作电脑  
这些问题，每一个都是硬骨头  
要花时间一个个啃

continual learning 这个事，很多人可能没意识到有多重要

现在的 LLM，你跟它聊天  
**它看起来「记住」了你说的话**   
但那只是因为对话历史还在 context window 里  
你关掉窗口，重新开一个对话，它什么都不记得

这不是 bug，这是设计就这样  
要让它真的「学习」新知识  
不只是记住，而是真正理解并融入已有知识体系

目前没有好办法  
你可能会想，那就扩大 context window 不就行了

问题是这治标不治本，学习不能只是把内容简单地塞进上下文  
**真正的学习，是要把新知识整合到模型的参数里**   
这需要重新训练，或者找到新的架构，成本高得吓人
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB63BG67CO35ybfqCAkglaBmpP1yUn0gc7NqHS649VOicrfF5snEib2KN6Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)当前的AI， 无法真正学习新知识

*** ** * ** ***

## 强化学习：terrible, but everything else is worse

播客里有个特别有意思的部分

Karpathy 说：  
**强化学习是个糟糕的选择**

但紧接着他又说：  
**但其他方法更糟糕**

这话听着矛盾，但其实是对现状最准确的描述  
RL 的问题主要是数据效率太低  
你想让模型学会一个东西，得让它试错无数次

AlphaGo 下围棋，self-play 了几百万局  
才达到世界冠军水平

这种训练方式，放在真实世界根本不现实  
你不可能让自动驾驶撞车几百万次来学习  
你也不可能让医疗 AI 误诊几百万次来进步  
所以：**RL 在真实世界的应用，始终受限于数据效率**
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6MddibPlibDS7bX3JISD6V4gKZu7Sp8IB5VfYmxj2hN7DVUXKVWnsfL3w%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D3)强化学习，需要海量试错

但为什么还要用 RL？

因为 **supervised learning** 也有问题：  
**需要大量标注数据**   
而真正难的任务，根本标注不出来

比如「写一个好的代码」、「做一个好的决策」  
什么叫「好」  
人类自己都说不清楚

你让标注员去标注什么是「好代码」  
每个人的标准都不一样  
有人觉得简洁就是好，有人觉得性能高就是好  
这种**主观性太强的任务，标注成本高得离谱**   
而且质量还没保证  
所以最后还是得回到 RL，让模型自己在反馈中学  
**通过奖励信号，而不是人工标注，是目前唯一可行的路**

Karpathy 的判断是：  
**未来会是 SL + RL 的混合**   
先用 supervised learning 学个大概，建立基础能力  
再用 RL 精调，在具体任务上优化

但这条路，还有很长的路要走  
需要解决的技术问题一堆  
比如怎么设计好的奖励函数，怎么平衡探索和利用  
每一个都不容易
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6iagMSUcZWPlicW6JibL5ZFDDegvpAD1yFGWAicQrgC6hS4PX3491GaPJpg%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D4)未来的训练方式：监督学习 + 强化学习

*** ** * ** ***

## 人类怎么学习，AI 为什么学不会

播客里有一段特别精彩

主持人问：  
**人类是怎么学习的，为什么 AI 学不会**

Karpathy 给了个很有意思的观点  
**人类的学习，是多模态 + embodied + continual 的**

什么意思？  
对于一个苹果，在人类的认识中：

*
  • 视觉上看到红色、圆形
*
  • 触觉上感受到光滑、硬度
*
  • 味觉上尝到甜味
*
  • 听觉上听到咬下去声音

这些信息是同时发生的，互相强化的  
而且你一辈子都在学，不断更新认知

你小时候对「苹果」的理解  
和你现在对「苹果」的理解  
肯定不一样

正如...  
小时候对「络腮胡」的理解  
和你现在对「络腮胡」的理解  
也不一样（雾

这种持续的、多模态的学习方式，是人类智能的基础
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB624VUcDu7DA2I2cNt0TgWpFufpJtSl5wbxBSG54wdxoUQKp8nyDFYOQ%2F640%3Fwx_fmt%3Dwebp%26from%3Dappmsg%23imgIndex%3D5)人的学习能力，很牛逼

**但 LLM 呢？它只有文本**   
虽然现在有了 vision model，但那还不是真正的 multimodal  
真正的 multimodal，是所有模态在同一个 latent space 里  
信息是融合的，不是翻译的

现在的做法，更像是把图片翻译成文本描述，再喂给 LLM  
这不是真正的融合  
就像你把一个视频的每一帧都写成文字描述  
这个描述再详细，也不等于你真的看了视频  
丢失的信息太多了

而且，**LLM 不能 continual learning**   
你今天告诉它一个新知识，明天它就忘了  
除非你重新训练整个模型，但那成本太高

一个模型训练一次，可能要花几百万美元  
你不可能每次有新知识就重新训练一遍

Karpathy 说：  
**这是个根本性的架构问题**   
当前的 transformer 架构，就不是为 continual learning 设计的

它的参数是固定的，训练完就冻结了  
要解决这个问题，可能需要新的架构  
能够动态更新参数，而不影响已有知识  
这是一个很难的问题

学术界在研究，但还没有成熟的方案
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6pr3n9Uicc3gtxYkPWTkbibzMAWyicBYJeU8ktHKcR6a9ETzdibia6AYlUFw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D6)Transformer 架构不支持持续学习

*** ** * ** ***

## model collapse：AI 不能吃自己

播客里还提到一个很有意思的概念：  
**model collapse**

什么意思？  
就是 AI 生成的数据，不能用来训练 AI  
为什么？  
因为会越来越糟

人类可以从人类写的东西里学习，对吧  
你读别人写的书，你变聪明了  
代际之间互相学习，知识不断积累

但 AI 不行  
如果你用 AI 生成的文本，再去训练下一代 AI，模型就会越来越偏  
最后输出变得越来越单调、越来越重复
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6QVFhiayxZkH4ydZr4S1Z9gqctmy2dQfRvD9QibaRp7AZic5DA1g91O17Q%2F640%3Fwx_fmt%3Dwebp%26from%3Dappmsg%23imgIndex%3D7)打个比喻...算了，不解释了...

这个问题其实挺严重的  
现在网上越来越多 AI 生成的内容  
文章、代码、图片、视频  
如果下一代 AI 训练的时候，把这些内容也当成「**真实数据** 」  
那就完了

模型会学到 AI 的偏见和错误  
然后放大这些偏见和错误  
循环往复，越来越糟

这就是为什么 AI 不能像人类那样自我学习  
人类可以互相学习、代际传承  
但 AI 必须依赖人类产生的真实数据  
这是个很大的瓶颈

而且随着 AI 生成内容越来越多  
「干净」的人类数据会越来越少  
将来怎么办？值得思考

有人提出：  
可以标注 AI 生成的内容，训练时过滤掉

但这也不容易  
AI 生成的内容越来越逼真，很难区分  
而且标注成本也很高

这个问题，目前还没有好的解决方案
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB609SqvRkenXjFWPrtHXWCrIic9SZu8GuGJ1ZMiaAFDUAQT2pvRicodDCWA%2F640%3Fwx_fmt%3Djpeg%23imgIndex%3D8)AI 生成内容，正在污染整个互联网

*** ** * ** ***

## AGI 会是什么样：融入 2% 的 GDP 增长

很多人对 AGI 有个幻想  
觉得会有个奇点，突然爆炸  
某一天，AGI 出现了，然后世界完全变了

Karpathy 说：不会的  

他的判断是：  
**AGI 会融入过去 2.5 个世纪的 2% GDP 增长**

什么意思？  
过去 250 年，人类社会一直在以每年 2% 的速度增长  
蒸汽机来了，2%  
电力来了，2%  
互联网来了，2%

为什么？  
**因为技术革命不是一瞬间的**   
它需要时间扩散、需要基础设施、需要人适应

蒸汽机发明了，不是第二天所有工厂都换成蒸汽动力  
需要几十年时间，建铁路、建工厂、培训工人

互联网也一样  
1990 年代就有了，但真正普及到每个人手机上，用了 20 多年
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6whDJ09DVOhbG2ls81Oac3vPEwxy2CxPjFM4vHu0Fuua3utLicAxZTnA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D9)windows xp，发布于 2001 年

AGI 也一样  
它会逐渐渗透到各行各业  
但不会在某一天突然改变一切  
先是一些简单的任务被自动化  
然后是复杂的任务  
一步步来

期间会有阵痛，会有失业，会有适应期  
但不会是突然的、剧烈的

Karpathy 说  
他不相信「hard takeoff」

他相信的是：  
AGI 会像之前所有技术革命一样，缓慢、渐进地改变世界

这个判断，其实挺重要的  
如果 AGI 真的是这样，那我们有时间准备  
不用担心明天醒来世界就变了  
可以慢慢调整教育体系、社会保障、法律法规

这是一个好消息  
当然，2% 的增长也不是绝对的  
可能某些年份会高一些，某些年份低一些  
但长期来看，会是一个相对稳定的、可预测的过程  
而不是指数爆炸式的奇点

*** ** * ** ***

## 自动驾驶：为什么花了这么久

播客里还聊了自动驾驶  
Karpathy 在特斯拉干了 5 年 Autopilot，他太清楚这里面的坑了

主持人问：  
为什么自动驾驶这么难，为什么花了这么久

Karpathy 给了几个理由

第一个，是 long tail problem

你以为自动驾驶就是识别车道线、识别红绿灯  
太天真了，真实世界有无数种情况  
施工路段、临时路牌、突然窜出的小孩、逆行的疯子、路上的大坑、掉落的货物

这些「长尾情况」，占比很小，但每一个都可能致命  
你必须把它们全部解决  
不能说「我 99% 的情况都能处理」，剩下的 1% 就会是事故

而且这个长尾，真的很长  
你以为处理完 100 种情况就够了  
结果发现还有 1000 种  
处理完 1000 种，还有 10000 种  
永远有新的边缘情况  
这就是为什么自动驾驶这么难

第二个，是 safety bar

自动驾驶不是「比人类平均水平好」就行  
它必须远好于人类

为什么？  
**人们对机器的容忍度，远低于对人的容忍度**

人类司机每天撞车，大家习惯了  
美国每年 4 万人死于车祸，大家也接受了  
但如果是自动驾驶撞了一次  
新闻头条、国会听证、股价暴跌  
所以 safety bar 特别高  
（所以... AGI Bar 呢？）

不是做到人类水平就行，要做到远超人类水平  
这个标准，其实挺不公平的  
但现实就是这样  
**技术要被接受，必须远好于现状**   
不能只是「稍微好一点」

第三个，是 data problem

自动驾驶，需要海量的真实驾驶数据  
再次划重点：**真实世界的**

这需要时间积累  
特斯拉为什么现在做得好  
因为它有几百万辆车在路上跑，每天收集数据  
这是花钱买不来的

你可以造一个很贵的实验室，雇一堆博士  
但你造不出几百万辆车在路上跑的数据  
这个优势，其他公司很难追上

Karpathy 说：  
**自动驾驶花了这么久，其实是给 AGI 的一个预警**   
AGI 会遇到同样的问题

long tail、safety、data  
每一个都需要时间  
不是说模型做出来就完事了  
还要在真实世界里打磨，处理各种边缘情况  
这个过程，可能比模型训练本身还要长

*** ** * ** ***

## 教育的未来：untangling knowledge

播客最后聊了教育

Karpathy 现在在做 Eureka Labs，一个 AI 教育公司  
他对教育有个很有意思的理解  
**好的教育，是 untangling knowledge**

什么意思？  
知识本身是一团乱麻  
所有概念互相缠绕、互相依赖  
但学习需要一个线性的路径  
你得先学 A，才能学 B

**好的老师，就是把这团乱麻理清楚**   
让学生按照一个清晰的顺序，一步步往上爬  
每一步都只依赖前面学过的东西  
不会突然冒出一个新概念，让你措手不及

Karpathy 举了个例子  
他的 transformer 教程，为什么大家觉得好  
因为他从 bigram 开始

bigram 是什么？  
就是个 lookup table：上一个词是 A，下一个词是 B  
就这么简单  
一个 2 维表格，谁都能看懂  
然后一步步加东西  
加 embedding、加 attention、加 layer norm  

好的教育，每一步都会解释：为什么要加东西，这是在解决什么问题这就是 untangling  
比如，把复杂的 transformer 拆成一步步的演进，每一步都有章可循
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F2icSMc1VBIYpLM0KLq36TIOSFVvwRLkB6aukpmEmIMDMbYECvcfBlZabY60Y1iaPIEC4FWWmjVyZxYFV71iaCtuag%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D10)emmmmm...

他还说了个特别重要的教育原则：  
**present the pain before you present the solution**   
别上来就告诉学生答案，先让他们感受到问题，然后再给解决方案，这样学得才深

为什么？  
因为如果你直接给答案，学生不知道这个答案解决了什么问题

就像你告诉学生「attention 机制是这样的」  
学生学会了公式，但不知道为什么需要 attention

如果你先展示问题：  
之前的模型处理长序列有这个问题

先让学生自己思考怎么解决  
然后你再给出 attention 这个方案  
学生会恍然大悟：原来是这样解决的  
这种学习，才是深刻的，才能记得住

这个原则，其实不只适用于技术教育  
任何教育都一样  
**先让学生感受到问题的存在，再给解决方案，这样学习效果最好**

*** ** * ** ***

## 最后说两句

这个播客值得一看  
Karpathy 是一个在一线干了 15 年的人  
很诚实地说出他看到的东西

在 Karpaty 眼中，AGI 还需要十年  
不是因为技术不行，而是因为问题太多、太难

continual learning、multimodal、safety、long tail、data  
每一个都是硬骨头，需要时间一个个啃，但也不是遥不可及

十年，听起来很长  
**但 iPhone 发布到现在，也就 17 年**

不用焦虑，也不用盲目乐观  
**踏踏实实做事就好**

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247507121&idx=1&sn=24fa549e79321c46fc1db45a73613f22&chksm=c32cd265a9cda41507bed895eb89d32515308f3d01cc0342ee2e158cc81d683c860c6f692523&mpshare=1&scene=1&srcid=1019ZX0FYSATWLvZv9mTI59A&sharer_shareinfo=c5c3f6de771bba09c561282888dfeed4&sharer_shareinfo_first=c5c3f6de771bba09c561282888dfeed4)

