---
id: "7427092463136801450"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247490420&idx=1&sn=e8b916bac5117aa5debc128dd69251ee&chksm=c08476a9c902a4f3718ee5dbc02ce6bd34e1c30c4d298b967d082e8dc831c66b88116bacc45c&mpshare=1&scene=1&srcid=0228PV7z221RMLj5W3XAtRbi&sharer_shareinfo=17514d306ab59b174b13858ce4509b47&sharer_shareinfo_first=17514d306ab59b174b13858ce4509b47
author: "猕猴桃 探索AGI"
collected: 2026-02-28
tags: []
---

# 300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。

# 300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247490420&idx=1&sn=e8b916bac5117aa5debc128dd69251ee&chksm=c08476a9c902a4f3718ee5dbc02ce6bd34e1c30c4d298b967d082e8dc831c66b88116bacc45c&mpshare=1&scene=1&srcid=0228PV7z221RMLj5W3XAtRbi&sharer_shareinfo=17514d306ab59b174b13858ce4509b47&sharer_shareinfo_first=17514d306ab59b174b13858ce4509b47)猕猴桃 探索AGI


AI大佬，Karpathy发了一条帖子。 300多万浏览，1000多条回复。

直接把OpenClaw送进了ICU。同时非常赞赏一些更轻量级的Claw项目。表示属于claw的时代来了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APou2EibTfFVpJRRdUnheGjfL0HbaSVxK4dP2h8g767IAD2cHY9Csg5ubWCr54XK6QEQEicpG9auyVu14ibbU4qW89vRFQzGeLYyvs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

他把OpenClaw比作40万行代码的怪物。

52个模块。45个依赖项。15个渠道商的抽象层。

所有东西都挤在一个共享内存的Node进程里。你的私钥、你的数据、你的一切，全部暴露在这头怪物面前。

而像NanoClaw这些轻量级的Claw，反而让他大开眼界。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APqbyq9qD8KWsNNC9Cmkd3B5xBv66zycckzXFnzw1vGfhzyqZu2EfI0Jzh2rgABSJicNtCwqToPnZWvjOia5K5T8eicMBLK6otfNwE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

我也去体验一下NanoClaw，只想说，确实好用。

OpenClaw太重了，这个没得说。各种bug，每天都能刷到一堆。

比如定时任务出问题了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APqic4SI6mmRNrTC77V70fJ20TjapgjwflXmE4Um7UFEeTInDElpfibpDZNFIR0Wr23K1aO9KAwHibjmdeeia1JicjzVRI6Lho5qXuRk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

Bug比features还多的一款软件。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APr2sBuNiapiaGdicDzJibamETXeKox2N2hf0cbGK6ueZbvWL2NdHBY1ar5e2pX6ebCV3SVkSofZbZVmv9LpXJSFZf7AFjicYD5iaBPAo%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

而这，仅仅是因为OpenClaw里边塞了很多很多你可能根本用不到的模块和依赖项。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APqt6FNgkl6iaVJtlb293NQ8fVF2c8Sba9TCDpXXzq3DRGPImldgGkPfxkCHCWB2AjgnpYArU0xgLbNhDwPRSnD9FQF0EWKYLyyg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

反观，NanoClaw确实很不一样。

他的核心代码只有500行不到，总体也就在4000行左右。

这意味着，不管是人，还是国产的各大模型，都可以轻松的改造这个项目。

https://github.com/qwibitai/nanoclaw.git

安装也是极其的简单，3行即可。

    git clone https://github.com/qwibitai/nanoclaw.git
    cd nanoclaw
    claude
    然后运行 /setup。Claude Code 会处理一切：依赖安装、身份验证、容器设置、服务配置。

整个过程不需要一行配置。因为它根本没有配置文件这个概念。

它所有的定制化需求，全部通过Skills来完成。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APogfQzA1WU7icka77atpe5HZDlerYTdticV7R2JlSb5VepYgy1pqb6xbibe2Z0Hnq9N83iaLiavYIkdGe0JbLYKclCJuArJ5hu0WYaw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

提供了各种快捷指令，根本不需要像OpenClaw一样，去研究后台里的各种开启开关，怎么填参数。

只需要/add-telegram，就可以自动读skill，自己安装以来，修改源码加telegram的消息处理逻辑，自己配置bot token。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fdurt1819APpt1CZ58PDHR2MQKQAW7awERUs9EUJUX13wd2svHHgB3SuS0auTx2wBMEGPG6u8vUV7ZHaon16VM3oOyu8dich30gMAIZMj0Bmg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

**AI自己给自己动手术改代码。**

Karpathy也特喜欢这个特性。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APpCbs37aKPzrRV6wwvb1J54h6OHkNVnF7HQzg920KwbqbZQKfibCj2rEzmKog837rfRxzIWSC9QmoWVgcGIlpaicBjRvtzWsbtSc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

NanoClaw创始人Gavriel Cohen顺带抛出了3个观点：

一、DRY原则过时了。

以前我们极度追求代码复用。但在AI时代，AI修改共享函数时不会考虑下游连锁反应。适度的代码重复，反而成了最有效的物理隔离。

二、严格的文件行数限制过时了。

与其让AI在多个文件之间反复横跳，不如让它在一个文件里把整件事干完。

三、代码不需要经得起时间的考验。

不要再为所谓的未来扩展性过度设计了。六个月后，更聪明更强大的下一代模型，会直接帮你把整个系统重写一遍。

## 写在最后

NanoClaw整体上就像他的名字，是一个追求极简、性能的框架。

应该能让我们更轻松构建出更好用的助手。

它还会继续进化吗？还是说，六个月后又会有更极端的东西出现？

没人知道。

但属于claw的时代来了。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fdurt1819APoBV7QRncJerncKzNddcLzFaqSCvAeich72Ml2XKJQ0oTlyAD5KSY3n2dOmpgWl8Gqo9bX6tDpmiaVF3lJuqXX9T2uEP7gGl6Txw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

好了，这就是我今天想分享的内容。如果你对构建AI智能体感兴趣，别忘了点赞、关注噢\~

![](https://image.cubox.pro/cardImg/4ucm0lx2a44plmc0loodn47t3vn88lyvdpkv3edybzpdxhnfpg?imageMogr2/quality/90/ignore-error/1)

**探索AGI**

目前专注于大模型agent的产品落地方向，未来不确定\~

268篇原创内容

<br />

公众号  

，

#aiagent #nanoclaw #openclaw

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247490420&idx=1&sn=e8b916bac5117aa5debc128dd69251ee&chksm=c08476a9c902a4f3718ee5dbc02ce6bd34e1c30c4d298b967d082e8dc831c66b88116bacc45c&mpshare=1&scene=1&srcid=0228PV7z221RMLj5W3XAtRbi&sharer_shareinfo=17514d306ab59b174b13858ce4509b47&sharer_shareinfo_first=17514d306ab59b174b13858ce4509b47)

