---
id: "7461808468844871758"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkxMzUyODQ3OA==&mid=2247494570&idx=1&sn=5fba59ad11268527a063483d0b8f00b4&chksm=c07b276745de547dd013645f73188568ad6b05b57112e1338f2778d0b1819611348e976def3f&mpshare=1&scene=1&srcid=0603UhjQjunu277uCs3t8lh4&sharer_shareinfo=354765191d4eb9ad4aed2f9ec1a60b9b&sharer_shareinfo_first=354765191d4eb9ad4aed2f9ec1a60b9b
author: "银海 AI产品银海"
collected: 2026-06-03
tags: []
---

# MiniMax M3 首发体验：被挤崩、被惊艳，接入 Codex 后也真香。

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxMzUyODQ3OA==&mid=2247494570&idx=1) · 银海 AI产品银海


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FthoHNWXYDzRYoyYw8A4ch0oJO4C01ylISic3JJM1ONArmPibgO8ax7Z5ibVvwSYcTib5FoKseibib39sKpFjVjGKGdlRIMTEEwxrtp49Dz2oJFZKU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

昨天 MiniMax M3 正式发布，我第一时间上手跑了一圈。

国产大模型新版本我基本都第一时间体验，大部分时候的感受是"嗯，又进步了"，很少有让我停下来认真想想"这东西到底能干嘛"的时刻。

M3 毕竟作为主版本，这次不太一样，先说体验结论：整体效果确实更能打了，但首发日服务器也确实拉了。

我自己选了三个真实场景来测：**一个是用 MiniMax Code 中的 M3 模型做了个 Skill 趋势榜单看 Agentic 能力，一个是用多模态复刻动态视频看视觉理解水平，另外顺手把** **API** **接入 Codex 跑日常开发。**

配上 Token Plan 整体用起来还是挺香的，这个就是Codex + MiniMax M3 生成关于自己 MiniMax M3 参数的介绍信息，先来看看，一会儿也有完整配置流程。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

先说做的 Skill 榜单，我给 MiniMax Code下了一句话指令：帮我采集各大 AI Agent 平台上最近一周的热门 Skill 数据，分析趋势，做一个可视化的榜单页面。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FthoHNWXYDzT3BxbCTol5gic2YZ4ib1zhKCDjZicNhWMOTJnXVbwB423KWeE34bPbesocfYAzBIk1X8wZDEudc1kCPm839Cibb3jB2Sgdng0jt5M%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D1)

就这么一句话，它自己拆解任务、抓数据、清洗去重、做趋势分析，最后用前端页面把榜单呈现出来，全程没有干预。

它也直接给我们做了一个数据管理的后台，自己感受MiniMax M3 的 Agentic能力，对于整体复杂项目的规划也有大幅度提升。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

让我觉得有意思的是MiniMax M3 在做Agentic类任务的拆解和规划时，自己对于数据源格式不统一的时候它自己选解析策略。

比如某个平台反爬严格它会换思路绕过去，分析阶段甚至自己加了「本周新上榜 Skill」的维度，不在我的需求里但确实有用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzR4XjBtao10oNInD92zgk71FBicicibBFR80gBh0xAqDsyAV27ic9zA9XlBtmrY3sCdtL2ibbsp2iaNia2J10hrpiaEr5aSFq9fQAjqr1Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

这更像是代码实习生拿到需求后的做了一层思考并且自主推进，只不过速度快 10 倍。

接着测多模态，这次 MiniMax M3 的模型，用一个接口就可以使用图像视频的输入。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FthoHNWXYDzR3FIfiabxJI0yB56zSM4iaDjTdz1ocCtoRJExd0DFsc6ibtonYic28gaANlDOVqEZnZ2kicwrkhsa3UHNonX7vFo5EziaDb9GBfNAOo%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D3)

我把这一张图丢给 M3 复刻还原，并且让它动起来，是真正在动的视频内容。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzSYfYjoplSKM4wEkXPYwlxfDuILUwq3BlfuYzvzOSsR2GibD8wqtKZIuWXribN773G4k11uww7dQPsmBKWCyicq0kUOUOM3kVoKOQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

去年 Gemini 刚发布时很多人第一次看到它理解图片视频内容的可以动态起来那种反应，我觉得可以用一个词概括：意外。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

M3 这次给我的感觉类似。它看懂了视频里的东西，还理解了视觉逻辑：元素之间什么关系、动效节奏怎么变化、布局按什么规律调整，然后用代码还原出来。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzQRWKm3YtBiaBmJbNbgcXyHBtPuiadgjjHOm8fNWSIerOLFCW28af3bujIybUKogJqWJpbDfEbxDfoK599ibR5Gfuiba7PpqGgVtwk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

复刻结果如果要细看虽然不是完美 1:1，但核心的视觉表达和交互逻辑是到位的，比起之前很多模型的多模态勉强能用，M3 这次在视觉理解和动态还原上用起来明显顺畅不少。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FthoHNWXYDzSTVnJ1TFWIdGdI3DcjjSm9AHhUS33Q2VVJYj6ALooYtHpSSnlDOcbxlSzjomepRFVsibuKdwtzuasb3G0aibTK1ibA77XAbicbUrM%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D6)

测完这两个，我又试了一下把 M3 接入 Codex，这个是在Codex 中跑的一个任务，我让他自己介绍一下自己的产品能力特性。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FthoHNWXYDzQMJL72zT4u3T75buCPWeA6lbp3mCI9FR1VjplqTosfRpicNPwkQj245S7td6e0LeGtlewjsJg0em12BPzzATYv8nB3aB4CK1JA%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D7)

M3 的 API 兼容 OpenAI 格式，绑定一个 Token Plan 性价比极高，所以我通过 CC Switch 接到 Codex 里并不复杂，实际跑起来体验也很顺滑。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FthoHNWXYDzSjiapLhPSTiarseuaPz6cS5iauBIEb8bPTeWblibklibyLo26EvRgzCH7EzzTQiceCGYF91N81weu61mU5yyyK08SKfebl0NmnudxZk%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D8)

具体怎么接？借助 CC Switch 就行，流程很简单，下面也直接上流程。

需要三样东西：CC Switch（下载最新版，ccswitch.io/zh）、已安装的 Codex、MiniMax API Key（在 platform.minimaxi.com 注册后创建。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FthoHNWXYDzTet7Gd84UNbfyziaj6BVDvYf2tTUibf2vckwtMFUyUdicvYViciawgdTKjZIeLNI8drdKsmQxvSsic28ESMdpHjWJMzYOibjSn5ZFeKk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D9)

接下来就是配置 CC Switch 中添加 MiniMax 供应商。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FthoHNWXYDzQCTlC7PAmCXtiblqGBejyMJB1obHqMbMkrL9GjDBI1Yu039HIwfLHibjNJIH8yU7iczqGpux99Y2OqPxmnsbh1um1dUXNE4Ambcs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D10)

打开 CC Switch，进入 Codex 配置页面，点击添加供应商，选择 MiniMax。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzQnVyo4VicI5jjQ0uwAWSbt5y1IKwxKdaOdvY6SicGiaxmFib295kHFxSMTRZnmnUCiaFjpV01eGN02RnH55Yl1dIFz0MrcY41WSzJs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D11)

填写 API Key（从 MiniMax 开放平台复制），API 地址保持默认即可。

接下来添加 M3 模型，在供应商配置里添加 M3，我们也可以直接点击一下「获取模型列表」就可以，或者自己手动填写模型名称和模型 ID，只填 Key 不加模型的话，Codex 里看不到可选的 M3。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzRlt1OGGrBGBBY36I1NbKuTFPqALluOHuc9MHDlpHvRl5lRiaRHtnH56Vbcey1XCwGVHHYcww0hUCsMAcicoJBiceMB4jFibq6d2TE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D12)

回到 CC Switch 主界面，进入设置，依次打开：启用路由 → 显示本地路由开关 → Codex 路由开关。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FthoHNWXYDzQFn069LGFuJIlibsXr1GA6n9CKk8RmufjicZD8ibblTy1KjV48yTOjDTX6eEc7qmbTz0QHHBSR8xRvD49OT8JdDjicwCFT77tcyHw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D13)

这一步是关键，CC Switch 本质上是在本地做模型请求转发，路由没开的话 Codex 不会走你配好的 MiniMax M3。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzQWj43oxrGg7XLME3Ah3Ckjvn8nWk2iatGrLs6mUp3mdnXbjImXRXHhv1hKGksiaR9L1Al0s2dlvTqiciaetamibvPskjkWDFdOvqyo%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D14)

重新打开打开 Codex，进入模型选择区域，应该能看到刚添加的 M3。

选中后随便测试一下，能正常回复就说明接入成功。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzTXjvT8c5qkwicdFdOmt0ib0t1ia5ZPUe3ibsds6oBpXXTjVYNiaIIAVFdXHX7ODN3J7TxJrIf8Jv7AwibqXtr5m9UhpEFXID2htnAY4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D15)

接入之后跑了几个日常开发任务，明显感觉任务完成率上来了，尤其是需要多步推理、中间调用好几个工具的场景。

Codex 的工程化体验加上 M3 的能力，非常还顺手。

当然了除了 Codex，M3 的 API Key 也能接到 Claude Code、OpenClaw 这些工具里，对已经有自己工具链的开发者来说迁移成本很低。

上面获取API Key 的时候，有个 Token Plan 也顺便说一下，性价比极高。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FthoHNWXYDzR9iaNkqcib3DPFQech8iagOcnR6VoV8QmeAVzGxnUPJFkbZ16vaLRYibaRBGyrqEcALUWfUPlqDW5kOHGfEhgyyPGuibL5yXElMVlM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D16)

三档：Plus 49 块/月 6 亿 token，Max 119 块/月 18 亿 token，Ultra 469 块/月 55 亿 token。

跟 Claude 订阅比，同价位 token 量大概 5 到 15 倍，日常开发 Max 档位够用，跑长程任务可能需要 Ultra。不过量大不代表能全用完，关键是模型能不能一次做对不浪费 token，M3 的完成率撑得住这个 plan。

不过必须说一下首发日的情况。

昨天刚上线的时候服务器明显扛不住，请求排队、响应变慢、偶尔直接报错，我大概等了两三个小时才正常用上。

可以理解，首发嘛，大家都在涌进来试。但理解归理解，体验确实打了折扣。

如果你也是像我一样那种「上来就要尝鲜」的人，昨天大概率是失望的，不过我自己今天测试完，现在应该已经恢复了，今天再试会好很多。

回到开头的问题：M3 到底能干嘛？

Coding 能跑通从需求到交付的完整链路，1M 上下文让长文档长代码能在窗口里一次性处理完，原生多模态的视觉理解也确实好用了。

这三样单独拿出来之前都有模型做到过，但同时集齐且每一样都到可用水平的开源模型，M3 是第一个。

版本号叫 M3 不是 M2.9，MiniMax 自己也认为这是个大跨越，从我的实测来看这个判断确实不算吹牛。

我不会说 M3 应该是国产模型的希望之类的话，它就是能力到了前沿水平的开源模型，好不好用还是要看大家自己实际生产场景。

至少在我测的这几个方向里，它还是好用令我比较满意的。

可以自己体验下～


© THE END

![](https://image.cubox.pro/cardImg/4p3mlet033q60if93brcy2k6uob241yu7e1ph61vkq91391p5x?imageMogr2/quality/90/ignore-error/1)

**AI产品银海**

银海，专注于AI领域产品应用分享。

222篇原创内容

<br />

公众号  

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxMzUyODQ3OA==&mid=2247494570&idx=1)
