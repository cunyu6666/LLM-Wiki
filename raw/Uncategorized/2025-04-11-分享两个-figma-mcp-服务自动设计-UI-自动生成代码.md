---
id: "7310177628814574213"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzk0NDY4Mzk3Ng==&mid=2247485592&idx=1&sn=bacaadd6e44fc2d203810b2fd925aa5a&chksm=c275d61db0d4bfaaef887612a07292a28b867060a3a1031c7ab7c2bf7e5b9fe81141e6fa9adc&mpshare=1&scene=1&srcid=041197BUcWTA5E2a23PpWe9O&sharer_shareinfo=55e6dc5f4b551c3f3c300c7b80833339&sharer_shareinfo_first=55e6dc5f4b551c3f3c300c7b80833339
author: "极客枫哥 极客枫哥"
collected: 2025-04-11
tags: []
---

# 分享两个 figma mcp 服务，自动设计 UI + 自动生成代码

# 分享两个 figma mcp 服务，自动设计 UI + 自动生成代码

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NDY4Mzk3Ng==&mid=2247485592&idx=1&sn=bacaadd6e44fc2d203810b2fd925aa5a&chksm=c275d61db0d4bfaaef887612a07292a28b867060a3a1031c7ab7c2bf7e5b9fe81141e6fa9adc&mpshare=1&scene=1&srcid=041197BUcWTA5E2a23PpWe9O&sharer_shareinfo=55e6dc5f4b551c3f3c300c7b80833339&sharer_shareinfo_first=55e6dc5f4b551c3f3c300c7b80833339)极客枫哥 极客枫哥


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FbAz5IvF9nicic4odDFUECRT00unQ79au9TT8EtpSiaYY8Q8xDicoxkLCHyf2mfrlWgmcxjNktAxhia207oic9hzsJplw%2F640%3Fwx_fmt%3Dpng)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FLibHyzFUiaj5icqcX4QlHE66jjicPP9JvUgrzlmgPwDOwD6YPx0lat6IUicHAYGGffdVPxXuk2iaVa9kovj1Gmj0kV0w%2F640%3Fwx_fmt%3Dpng)

hi，我是枫哥～十年互联网程序员，擅长 js 逆向，python 爬虫，各种前后端技术。热衷于分享各种好玩、实用的技术和软件工具。


今天给大家介绍两个 figma mcp插件

*
  • cursor-talk-to-figma-mcp，直接写提示词就可以在 figma上生成设计稿
*
  • Figma-Context-MCP, 可以根据设计稿生成前端代码

## cursor-talk-to-figma-mcp 使用教程

#### 安装 bun

    curl -fsSL https://bun.sh/install | bash

#### 安装 talk-to-figma-mcp 服务

打开 vscode中的 cline，点击 mcp -\> Configure MCP Servers，增加如下 mcp配置内容

    "TalkToFigma": {
        "command": "bunx",
        "args": ["cursor-talk-to-figma-mcp@latest"]
    }

将项目 clone到本地，github地址：https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp

执行启动命令

    bun socket    

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icU8vbU9AEfMJ9ztFUhhnGvToRvECibFSvZ9vUMCZmNCMp8SicXhwaZMjw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

看到 TalkToFigma显示绿灯就表示配置成功了

#### 下载 figma 应用程序

因为网页版不支持 mcp，所以要使用桌面版，下载地址：https://www.figma.com/downloads/

#### 配置 figma

按照下图所示进行操作
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icCy6vicHH37glmQID9icqz5oz6JrWJibUKMdqib9cGaOuBQlRkmeA3Jxr6w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

选择 cursor-talk-to-figma-mcp/src/cursor_mcp_plugin/manifest.json文件
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icmSDwhg4ZDnsLg5VkLK4mgU5jac7LeNAVe0PlHibpQkU28ozpc2ibVicibg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

然后选择第一个 Cursor MCP Plugin，配置成功后可以看到如下结果
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icOTW4tdyQG1ZtCE1PuEAZrVeiaYtw3ugT7BpOZlPsDdJj7VEzb3NibNGg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

#### 开始使用

在 cline中尝试与 figma进行连接
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icibhGFloIbGicJiaWgUMVFbuL14Kbu8iaDScnVg4QNRfD1elvStSm89gDOQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

如果操作都没有问题的话，就可以成功连接到 figma了
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icSKYk7Vy0kTOhd893telj9eN7eUqRpjoV578OE4dFyV6YJQYBV3ico4Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

接下来我们尝试来设计一个移动端的登录页面，让 chatgpt给出一段提示词
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1ic4OvbktrfBSWwlFOQG3rSibrNqrjjpkQCUmHudoBcNKWrEa40BaChibfA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

复制提示词到 cline中，运行，等待操作完成后，就可以得到一个登录页面了

但是这个效果说实话很一般，我使用的是 deepseek-0324模型
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icWZHydprBp1dDK1r43EX71cDOlqppU74rAxVlwa53vLYg6oRxiaNogvA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

然后同样的步骤使用 cursor 再试试看，生成的设计稿如下
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icE6HngYbTTwTL5WhNpUUgUykEXqQ8icibNjwmUsBH3WH3pGPXKJghF3icg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

这个效果比 deepseek-0324稍好一些，但是也是达不到设计师的水准，但是用来出原型图目前应该还是一个比较不错的选择。

## Figma-Context-MCP 使用教程

仓库地址：https://github.com/GLips/Figma-Context-MCP

还是以 cline为例，在 mcp服务中添加如下配置

    {
      "mcpServers":{
        "Framelink Figma MCP":{
          "command":"npx",
          "args":["-y","figma-developer-mcp","--figma-api-key=YOUR-KEY","--stdio"]
        }
    }
    }

然后到 figma网站中点击个人头像 -\> Settings -\> Security -\> Generate new token，复制 token设置好 mcp服务中的 api-key就行了
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icTaaODb2VUFghia1xkXoaCKOqm9LpjXvnwTgaE9yNEx8IxFjrsrvwxdA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")看到绿灯就表示配置成功了![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1ic8tne3MpKFFk05wUubZc9PhTdB73P4gBDt7OaYO6wyoN2GZogkWich1g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

这里我们直接使用上一步生成出来的设计稿，选中页面，按照上图进行操作，然后扔到 cline中，提示词

    https://www.figma.com/design/UzioBfkovMOtuNapyJ2Ubx/Untitled?node-id=2002-2&t=Jytp2VedmvusMQjS-4 
    按照这个设计稿实现 login.html

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbibBe4w1d5FnGaHHiciaDqe1icvgsjm021eyWSv4HHECJY6scia9AXGJ8EbHmgbjNatCVBIDI7Uia1np4Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

不得不说，这种简单的页面，实现的效果还是很好的。

我也使用过真实的项目设计稿来通过 mcp实现代码，但是效果上就没有这么理想了。

所以短期内，AI还是只能辅助做一些复杂度、还原度要求不高的设计，但是相信随着技术发展，未来的能力会越来越强大。


![](https://image.cubox.pro/cardImg/2fvg50xuc5iuuv2obz0e1wuqtbumii19a3pbnk3qr0rn3jh928?imageMogr2/quality/90/ignore-error/1)

**极客枫哥**

懒癌患者，擅于利用技术解决实际问题，分享 js 逆向，python 爬虫，前后端技术，实用软件，开源工具等

67篇原创内容

<br />

公众号  

，

### 作者介绍

*
  枫哥，90 后奶爸，10 年程序员，正在尝试打造第二曲线。
*
  专注分享：折腾副业的成长故事，各种好玩的技术。
*
  如果你想与我交流，欢迎加我微信～备注：公众号

  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FmSLdmLCicHlbMohibcuvKDms3RqtCDWwyQUO5yKTBbzCADuLWpSKsVgMqLeB2Ysyk70VPG8SpbPfHOnVM8jTSNcw%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26tp%3Dwebp)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NDY4Mzk3Ng==&mid=2247485592&idx=1&sn=bacaadd6e44fc2d203810b2fd925aa5a&chksm=c275d61db0d4bfaaef887612a07292a28b867060a3a1031c7ab7c2bf7e5b9fe81141e6fa9adc&mpshare=1&scene=1&srcid=041197BUcWTA5E2a23PpWe9O&sharer_shareinfo=55e6dc5f4b551c3f3c300c7b80833339&sharer_shareinfo_first=55e6dc5f4b551c3f3c300c7b80833339)

