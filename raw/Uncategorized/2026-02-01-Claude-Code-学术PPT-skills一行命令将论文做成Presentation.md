---
id: "7417613572999481023"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484509&idx=1&sn=1cc0e5842e9f7342ad94e476e01f57e3&chksm=970b94924cca466ab9d37f95176c7b1ca15be3d7156fbb1382df9384e3186d51b0f537cdb8cb&mpshare=1&scene=1&srcid=02018FHCmeHJPKeOJUPFQKwv&sharer_shareinfo=c7dd77900cef9508d43092b301d6f3ae&sharer_shareinfo_first=c7dd77900cef9508d43092b301d6f3ae
author: "鲁工 AI编程实验室"
collected: 2026-02-01
tags: []
---

# Claude Code + 学术PPT skills：一行命令将论文做成Presentation

# Claude Code + 学术PPT skills：一行命令将论文做成Presentation

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484509&idx=1&sn=1cc0e5842e9f7342ad94e476e01f57e3&chksm=970b94924cca466ab9d37f95176c7b1ca15be3d7156fbb1382df9384e3186d51b0f537cdb8cb&mpshare=1&scene=1&srcid=02018FHCmeHJPKeOJUPFQKwv&sharer_shareinfo=c7dd77900cef9508d43092b301d6f3ae&sharer_shareinfo_first=c7dd77900cef9508d43092b301d6f3ae)鲁工 AI编程实验室


大家好，我是鲁工。

最近Skills实在太火了，已经从单纯的AI编程领域火到了其他AI领域，国内外都在持续跟进。

受到上次用Claude Code写综述论文的思路启发，我最近也在打造一个系统的用于学术科研的skills集合。

今天我想要分享的是如何在Claude Code中实现一个用于生成学术论文PPT的skill。

很多朋友读研读博时，经常要开组会。开组会的重点内容，就是汇报PPT。把最近一段时间读了哪些paper、做了哪些实验、有哪些阶段性结果，都通过PPT呈现出来。

在算法岗位，即使是工作后，也免不了时不时要做paper review和presentation。之前这个过程从搜集文献、研读再到做PPT，起码耗费一周的时间。

后来，有了基于Nano Banana Pro模型的NotebookLM，就省事很多了。NotebookLM的slide deck一键直出PPT的功能，我相信是很多人都刚需。那么如何将NotebookLM的这种生成PPT的功能变成Claude Code中的skills，方便我们随时调用呢？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoOxpGJXJxgqyqia6vHcMmZTyMYlfw9Eoibak9ibcPr1ypzduKcglsRkicdHw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

我先是自己尝试写了一个，但是编排效果不理想。直到我在X上发现宝玉老师（@dotey）开源的一个slide-deck skill，尝试了一下效果非常稳定。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoOp9tOYyiaPPMA1LjDqxiala9jpvEww8WhehbrfjGLkWp5ibBHBibMibGQlPg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

但这个skill是面向通用场景的PPT生成，对于学术论文的PPT适配性可能没有那么高，所以我在宝玉老师的slide-deck skill基础上，专门做学术论文PPT的风格和内容适配修改。

slide-deck skill的PPT生成逻辑是这样：

对于指定的md或pdf文章，先对其进行内容分析和拆解，然后生成一份内容编排大纲（outline）并由用户确定风格和语言。之后再依据这份outline生成每一张slide的Nano Banana Pro模型生图提示词。最后调用模型以图片形式生成每一张slide并合成PPT和PDF。

上述流程对于通用场景下的PPT生成无论完成度还是质量上都非常高，但对于学术论文的PPT制作，并不适合每一页的slide都用模型生成的方式来完成，PDF原文中的overall framework、实验结果等图表，更适合直接截图放到PPT中。

所以，我需要一种能综合模型生成和直接截图来获取PPT slide的方法。在对论文进行分析时，直接在outline.md中就确定好哪些slide是模型生成，哪些slide是原文自动截图，并且自动截图效果不好的时候也可以人工干预手动截图（实际测试发现截图存在一定的失败率，所以这块可能人工截图效果更好，需要后续优化）。

outline.md文档：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoObiazGOdyMzumZiaicXicpDbUjH4twGCOSo5MXibY0UQNbQMkfVHUUX0nZ7Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)


Nano Banana Pro图像生成有两种方式，一种是你直接提供Gemini API，这种的话最方便，当然也得承担API费用。另一种是宝玉老师给slide-deck配套的gemini-web skill，可以逆向到Gemini官网登录后进行生图，免费但是有账号风险，所以谨慎使用。

框架确定后由AI确定哪些slide截图提取，哪些slide模型生成：


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoOTzDrQjSzwGoXnakZR1K8DytTdogGboF0wIU1BzUl4Nicj5jCKtHy6QQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

完整的PPT效果：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoOC7wGeevX7sGk5cAuvpYG2WZFIKoLC6bdwzjjNUNCP8ln6ib75AXJZQQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoORDaRqRbmMibdib3uzjErASlTjt7curJ7ic5ia5nsnC1HXNgcoAAdgriaHcg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F29gExhZKtdovstYAzlrKeENVzOjkVtoO7GN9mDKRj3LCPk6ibEXf4p1X27CdzfrZQEribH1YiaHw9bVT6jDa5UWZQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D6)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoOIXlKnD2nQHNeJqbBevUHYfTYmnbcebIc6cibLZywXtl06vO8XDhnD1Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)

这样，通过这个skill我们就可以将一篇专业的学术论文转换成PPT了。

宝玉老师原slide-deck skills开源地址：

https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-slide-deck

我针对学术论文适应性修改后的paper-slide-deck skills地址：  


https://github.com/luwill/research-skills/tree/main/paper-slide-deck

安装方式：

    # clone项目到本地git clone https://github.com/luwill/research-skills.git# 复制到skills目录cp -r research-skills/paper-slide-deck ~/.claude/skills/


调用方式：

    /paper-slide-deck example-paper.pdf --style academic-paper


paper-slide-deck目前还是初版，实际使用过程中可能还有许多不足，后续会根据反馈持续优化。

另外，上次用Claude Code写综述的推文火了之后，后台很多读者问我在国内怎么才能稳定使用Claude Code和Opus 4.5模型。其实我之前也推过，就是使用七牛云平台的模型API，可以在Claude Code中没有网络限制的条件下无障碍使用Claude Opus 4.5和Sonnet 4.5等模型。

之前用七牛云api使用Claude模型搭建的Nano Banana Pro图像生成案例：

[Claude Code + 七牛云：快速Vibe一个基于Nano Banana Pro的图像生成项目](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484015&idx=1&sn=204cc44996b3ed7845895889db7abda2&scene=21#wechat_redirect)

在Claude Code中配置七牛云API非常简单：

    {  "env": {    "ANTHROPIC_API_KEY": "你的七牛云API Key",    "ANTHROPIC_BASE_URL": "https://api.qnaigc.com",    "ANTHROPIC_MODEL": "claude-4.5-opus",       }}


七牛云支持国内外大多数主流大模型，所以选择非常灵活，比如国内的kimi-k2-thinking、GLM-4.7、MiniMax-M2.1等模型，同样可以通过七牛云平台使用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F29gExhZKtdovstYAzlrKeENVzOjkVtoOXv0qfcs9b4bMkXy5LaTbMwqXmlAeo6BxEAKUeQziajXfEvNubMnSiceA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D8)

七牛云Claude Code接入配置文档：

https://developer.qiniu.com/aitokenapi/13085/claude-code-configuration-instructions

七牛云API获取地址：

https://portal.qiniu.com/ai-inference/api-key

七牛云支持的模型列表查询地址：

https://www.qiniu.com/ai/models

我这里放一下我的七牛云账号的邀请链接，可以直接通过这个链接注册获取token，注册就送1000w token，并且我也能拿到500w的token。无法在国内顺畅使用Claude Code的朋友值得一试：

https://s.qiniu.com/rEBnM3

我是鲁工，八年AI算法老兵，AI全栈开发者，深耕AI编程赛道。欢迎关注，感兴趣的朋友也可以加我微信（louwill_）交个朋友。

点击阅读原文立即拿1000w token⬇️

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzE5ODY5MDU4Mw==&mid=2247484509&idx=1&sn=1cc0e5842e9f7342ad94e476e01f57e3&chksm=970b94924cca466ab9d37f95176c7b1ca15be3d7156fbb1382df9384e3186d51b0f537cdb8cb&mpshare=1&scene=1&srcid=02018FHCmeHJPKeOJUPFQKwv&sharer_shareinfo=c7dd77900cef9508d43092b301d6f3ae&sharer_shareinfo_first=c7dd77900cef9508d43092b301d6f3ae)

