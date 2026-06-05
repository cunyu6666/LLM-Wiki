---
id: "7403887661523404831"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449477473&idx=1&sn=49f3b32af7ce16d19ce66a2db48222e3&chksm=8de384a5a4ff5c14e61fb792b01b4689b519f2efb102ac37461444fefc53b7c91d4fba38852c&mpshare=1&scene=1&srcid=12252hGtmqVrkE57dABxtbNQ&sharer_shareinfo=a8905e8833ea9a3a79bb4f9a6394d7a6&sharer_shareinfo_first=a8905e8833ea9a3a79bb4f9a6394d7a6
author: "风筝 古时的风筝"
collected: 2025-12-25
tags: []
---

# Google 新产品 Code Wiki，什么上古项目、屎山代码统统都不是问题了

# Google 新产品 Code Wiki，什么上古项目、屎山代码统统都不是问题了

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449477473&idx=1&sn=49f3b32af7ce16d19ce66a2db48222e3&chksm=8de384a5a4ff5c14e61fb792b01b4689b519f2efb102ac37461444fefc53b7c91d4fba38852c&mpshare=1&scene=1&srcid=12252hGtmqVrkE57dABxtbNQ&sharer_shareinfo=a8905e8833ea9a3a79bb4f9a6394d7a6&sharer_shareinfo_first=a8905e8833ea9a3a79bb4f9a6394d7a6)风筝 古时的风筝


Google 向来低调，即便是 Gemini 3 这种顶级产品的发布，也不像其他公司一样搞得那么隆重，有一些小产品更是低调到发了很久都没人知道，比如这个面向程序员的产品 **CodeWiki** 。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FiaWSDo4TfyZgnHy0UkxeUASmB1Kq7ZsFzgzkVSyWWbF7XJTRqW8b7LtiaXaQzWU1I17OaDSD6N413ejbfBkHmic0w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

之前介绍过一个叫做 DeepWiki 的产品，和 Code Wiki 属于同一类产品，功能完全一致。

如果说 DeepWiki 是个勤奋的实习生，那 Google 这个 CodeWiki 简直就是坐镇少林寺藏经阁的扫地僧。

DeepWiki 底层可能采用了多家大模型，具体是哪个不太清楚，但是CodeWiki是基于Gemini 模型的，Gemini 具有超长上下文，也就决定了CodeWiki非常适合做大型项目的代码分析。

对于我们这些每天要在代码堆里的程序员来说，CodeWiki 可能才是真正的救命稻草。

简单来说，它的核心逻辑也是**帮你把难啃的 GitHub 仓库嚼碎了喂到嘴里** ，但毕竟是 Google 出品，背靠 Gemini 模型，那个"懂代码"的程度又上了一个台阶。

你只需要把 GitHub 仓库地址扔给它，它自动帮你写好这个项目的详细解析文档，甚至超过绝大多数仓库自带的 README 文档。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FiaWSDo4TfyZgnHy0UkxeUASmB1Kq7ZsFzsuIdiaYNbPnTKEzRsE0Qo1UQX2oeVEdHNicRhg2aiam41XBPPD2aHXr1A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

举个例子，比如大名鼎鼎的 Kubernetes 仓库，地址是 https://github.com/kubernetes/kubernetes。

在 CodeWiki 里，你只需要访问 codewiki.google ，然后把仓库地址放进去，瞬间，一个那种看着就显得"我很贵"的在线文档站就生成了。

不仅是结构像官方文档，关键是它的**内容深度** 。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FiaWSDo4TfyZgnHy0UkxeUASmB1Kq7ZsFzY97GUkgHZtk7UTQ1UosZuicDOibhNgjJK3kibib6MOK1iaLS5pjotn7TDYw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

以前我们看开源项目，最痛苦的是什么？是只有代码没有图！看 AbstractBeanFactory 这种类，光看代码脑子都绕晕了。

**CodeWiki 最强的一点就在于：它是个画图狂魔。**

它生成的文档里，会自动穿插**类图、时序图、架构流转图** 。以前你需要手绘半天才能理清的调用链路，它直接给你画得明明白白。

这就是为什么我说它像个"扫地僧"了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FiaWSDo4TfyZgnHy0UkxeUASmB1Kq7ZsFz3zbhEKFbGDQNzZzcU9E3Ztp01vuG2kkaYiaC46q1zzWqkgZXLCNM4cw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

新手看代码是一行一行看，老师傅看代码是看"脉络"。CodeWiki 就是那个直接带你打通任督二脉的人。它不光告诉你这行代码是干嘛的，还会通过图表告诉你："**这个模块的数据是从 A 传到 B，经过 C 处理，最后存到 D 的** "。

这一套组合拳下来，原本晦涩的逻辑瞬间就通透了。

除了看文档，还可以直接在右侧针对当前代码库向 Gemini 提问。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FiaWSDo4TfyZgnHy0UkxeUASmB1Kq7ZsFzKZrmpxCxwNNBZxeibFIdlsJT7m8Ft0wtmsWGclpgVo1FnBzkBbhn2sw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)目前 Google 已经对海量的热门开源仓库完成了预索引，基本上你听过的、没听过的轮子，在这里都能找到对应的"精读版"。

不久之后，还将支持私有仓库，那时候，什么上古项目、屎山代码统统不是问题了。

说实话，看着现在这些工具，真心羡慕刚入行的兄弟们。

**要是当年我们学代码的时候有 codewiki 这玩意，我头发还能再多留几根！**

赶紧去试试吧，把那些你收藏夹里吃灰的仓库都拿出来"炼"一遍！

**有事儿没事儿都可以加好友，不限于技术交流、AI、独立开发等，备注『公众号』就可以了。**   


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FiaWSDo4TfyZgHJiaAp4jogHHb5OmibicrBib6ZedMP9avevfrrscVDlSkicZibk92OoKkpQ03gDTdjXLaVbbAOxoAVrIA%2F640%3Fwx_fmt%3Djpeg%23imgIndex%3D5)

**往期文章**

[我用 Gemini 3 手搓了一个地球虫洞，这效果太离谱了！](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449476642&idx=1&sn=d23615f03fca792209406a9c2b2369b2&scene=21#wechat_redirect)

[实测 Nano Banana Pro 和 即梦10几种场景，到底差距有多大？](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449476572&idx=1&sn=825c787412d9a00de0d787256590a65d&scene=21#wechat_redirect)

[免费使用 Gemini 3 的几种方法](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449476530&idx=1&sn=cccf31b35f5cd9806817037abb2f2a61&scene=21#wechat_redirect)

[Gemini 3.0 来了，前端不存在了！](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449476511&idx=1&sn=b286cf6591ae573e5c27aebcef0fc25a&scene=21#wechat_redirect)

[Gemini 这个功能才是真的利器，强烈建议豆包、Kimi 跟进一下！](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449476452&idx=1&sn=af65202666a3ba9a9b9cdced8da7d219&scene=21#wechat_redirect)

["黑熊精录音棚唱歌"的视频是怎么做的？](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449476271&idx=1&sn=f402bdd0f1498e7a0c5aff9c931a39bf&scene=21#wechat_redirect)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxMjA0MDk2OA==&mid=2449477473&idx=1&sn=49f3b32af7ce16d19ce66a2db48222e3&chksm=8de384a5a4ff5c14e61fb792b01b4689b519f2efb102ac37461444fefc53b7c91d4fba38852c&mpshare=1&scene=1&srcid=12252hGtmqVrkE57dABxtbNQ&sharer_shareinfo=a8905e8833ea9a3a79bb4f9a6394d7a6&sharer_shareinfo_first=a8905e8833ea9a3a79bb4f9a6394d7a6)

