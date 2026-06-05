---
id: "7305295416830984746"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483920&idx=1&sn=29ae0739dff846d72c9792291aedc23d&chksm=91d8436110436f0b9ac3f4c8e750129aa34d9097dbc2fcd942c0f00ce9cbb9759c073082f4b2&mpshare=1&scene=1&srcid=032899WZgs0YyhTkyZpR7aQl&sharer_shareinfo=1fd888c628d6b885a28e77757c26b647&sharer_shareinfo_first=1fd888c628d6b885a28e77757c26b647
author: "全金属外壳AI 未来的回响"
collected: 2025-03-28
tags: []
---

# 如何在Cursor中使用Magic MCP生成好看的UI（第二期）

# 如何在Cursor中使用Magic MCP生成好看的UI（第二期）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483920&idx=1&sn=29ae0739dff846d72c9792291aedc23d&chksm=91d8436110436f0b9ac3f4c8e750129aa34d9097dbc2fcd942c0f00ce9cbb9759c073082f4b2&mpshare=1&scene=1&srcid=032899WZgs0YyhTkyZpR7aQl&sharer_shareinfo=1fd888c628d6b885a28e77757c26b647&sharer_shareinfo_first=1fd888c628d6b885a28e77757c26b647)全金属外壳AI 未来的回响


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBIeMyPOnfMy7HX0zdvHhnhicr2OiaibWxUmKAzKLXkL7TUZtiaDdEBJnKic3ibdFWibqcZZvcuRrNtfxicL2w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

大家好，上一期关于Magic MCP的教程大家反响十分强烈，这一期分享一下我在使用Magic MCP的小技巧。

### 一、针对上一期《如何在Cursor中使用Magic MCP生成好看的UI》中部分内容的勘误

1、首先，先对上一期文章做个勘误，在测试在Cursor中调用Magic MCP时提示调用出错了，打开里面的调用结果提示502的服务器错误。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBL8SpvAlHLrfRgP6VBiblXAiaqrxNPiaBSJHOhDYtDDt6LxWMICjYW9y8ISYkrNC0icwhpPkrYeIAwRicA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

2、但是这时在21st.dev的官网API页面查看调用居然是成功的！消耗了2个request，就挺无语。怀疑是输出太长导致的超时，但是目前还没有找到具体配置调用MCP server超时时间的方法。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBL8SpvAlHLrfRgP6VBiblXAiaLdibMKALMaBHQd29VU7DiaChQGcZTJDQFCPWAGrBAGia9aUvViatIrlP2Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

3、因此上一期的网站实际上是使用了Claude 3.7 thinking原生的设计能力完成的UI设计，在此对上一期中出现的纰漏和大家道个歉。

4、实际上Claude 3.7 thinking设计能力非常强悍，审美也是相当之高，单纯使用Claude3.7去做产品原型设计或者网站UI设计也是几乎可以满足需求的，这里再给大家分享一下做的另外一个测试网站。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FxFbsATlObBL8SpvAlHLrfRgP6VBiblXAiaoa6IHfib4eARor2iaLHJolWicnrzlmkTG0lBSGx5ANvOFe4JHNWtTk53g%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

### 二、在Cursor中使用Magic MCP的一些小技巧

1、使用 /ui 快速调用Magic MCP。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBL8SpvAlHLrfRgP6VBiblXAiauicsgQnBEJc9JyCPjZXxJoicPjsvDp3kaf3oW5YucERBPiaKBPvUDbueg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


2、多次测试发现使用smithery.ai生成的命令在Cursor中调用Magic MCP不稳定，换成官方的mcp.json就正常了。cursor setting的MCP页面中才能看到Magic MCP服务器显示绿色可用状态，可以看到可以使用的tools。



        "magic-mcp": {         "command": "npx",        "args": [        "-y",        "@21st-dev/magic@latest",        "--config",        "API_KEY=\"YOUR-KEY\""      ]    }




![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBL8SpvAlHLrfRgP6VBiblXAiawBNynrgwHK6TAIS2v4W0FXHkbKbr9uWgWWt2UQjwVnzLYUOXz5YUsw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

3、因此目前我会在使用前先问一下当前这个Magic MCP是否可以正常调用。如果result中可以正常返回代码说明可以调用成功。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FxFbsATlObBL8SpvAlHLrfRgP6VBiblXAia8ADLlF8UI21tNhqpqfTaObEfNCYaKKTvIORjYwrS6icVBVWiaEaArRpA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

4、目前在Cursor中使用Magic MCP问题还比较多，有条件也可以在Claude客户端中使用。

**更多关于AI工具、Cursor、MCP相关的教程和资讯请持续关注我后续的分享！**

**-END-**

![](https://image.cubox.pro/cardImg/4i3gfcfjrb36iw20gbn17gozx2egzgty4kmrty82269ynn0ipr?imageMogr2/quality/90/ignore-error/1)

**未来的回响**

未来源自于此，创造在此迸发......

21篇原创内容

<br />

公众号  

，  

**【限时开放】** 欢迎加入**AI工具实战派**交流群一起学习进步～

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FxFbsATlObBLRUXn23rarIHOrgzm4x7icgDfRBice1xP99ibWSpLibazfJKzgct7eUHU5DxaKgHEP4E2RlT6icpJ0ttw%2F640%3Fwx_fmt%3Djpeg)

**AI知识学习、工具资料分享**请加入我的知识星球

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FxFbsATlObBKKtKmzU94ezBKA7kn1W8XCs1r6oRibDNG4rVV516OrHNZY8oNFKAbRP3rsicfe2VU0SpCwBznic4sww%2F640%3Fwx_fmt%3Djpeg)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA4Nzc3NzkzNQ==&mid=2247483920&idx=1&sn=29ae0739dff846d72c9792291aedc23d&chksm=91d8436110436f0b9ac3f4c8e750129aa34d9097dbc2fcd942c0f00ce9cbb9759c073082f4b2&mpshare=1&scene=1&srcid=032899WZgs0YyhTkyZpR7aQl&sharer_shareinfo=1fd888c628d6b885a28e77757c26b647&sharer_shareinfo_first=1fd888c628d6b885a28e77757c26b647)

