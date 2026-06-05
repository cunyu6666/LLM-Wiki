---
id: "7311097502181100835"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIwMjkwMDAwMg==&mid=2247485774&idx=1&sn=8ae26b58c222b22a658325119a351616&chksm=97a692e72dea40f4a6ee4f7f1884a7a5e855661d9ba4c5fca60b0febb04adf8d5337c6b72801&mpshare=1&scene=1&srcid=0413r4bTuM7JD9Dp6wATiWad&sharer_shareinfo=4c5d6d71ad52e188397b8c4d9ca21ba8&sharer_shareinfo_first=4c5d6d71ad52e188397b8c4d9ca21ba8
author: "安阳i 安阳im"
collected: 2025-04-13
tags: []
---

# Cline x MCP x MasterGo | 设计稿转代码

# Cline x MCP x MasterGo \| 设计稿转代码

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIwMjkwMDAwMg==&mid=2247485774&idx=1&sn=8ae26b58c222b22a658325119a351616&chksm=97a692e72dea40f4a6ee4f7f1884a7a5e855661d9ba4c5fca60b0febb04adf8d5337c6b72801&mpshare=1&scene=1&srcid=0413r4bTuM7JD9Dp6wATiWad&sharer_shareinfo=4c5d6d71ad52e188397b8c4d9ca21ba8&sharer_shareinfo_first=4c5d6d71ad52e188397b8c4d9ca21ba8)安阳i 安阳im


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F6aVaON9Kibf7U8kyccAm9c63gM1MwibJqsoiaDzHicA9VFaQN95UIFPewWV4vMIvxpll56HDh5uE9ictyzbeTU2JtKg%2F640%3Fwx_fmt%3Dgif)  


正文：1155字 5图

预计阅读时间：8分钟


写在前面

MCP（Model Context Protocol，模型上下文协议） ，由 Anthropic 在2024年11月底推出的一种开放标准，旨在统一大型语言模型（LLM）与外部数据源和工具之间的通信协议。与Function Calling不同的是，MCP不依赖特定模型实现，开发复杂度低且复用度高。

在Manus火的时候，MCP也出现在大众视野且逐渐被接受。大家可以自己实现MCP Server，也可以使用公开发布的MCP Server来扩展Agent的能力。

- Github：https://github.com/modelcontextprotocol/servers

- smithery仓库：https://smithery.ai/

MasterGo今天推出了自己的MCP Server，通过该Server可以实现将设计稿中的容器转为HTML代码，测试效果之余记录下来。  

本文将利用VS Code、Cline来实现这个过程（Cursor也一样但我的到期了，先用免费的Cline）：

- VS Code：进入官网下载即可，https://code.visualstudio.com/

- Cline：VS Code插件，在VS Code安装Cline以及初始化MCP后续有需要再出教程

测试步骤

生成MasterGo令牌

在MasterGo个人设置里进入安全设置，点击生成令牌

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjUVHUdkYfcYBBvAPAPBQx4SbeIW2iccwDSJD8PBEibEcicGpldxHOXGU6bSc1Q0Ie8BNPf7N06DKYroGxkgYbiaMwg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

在Cline中配置MasterGo MCP Server

进入VS Code，点击Cline，并查看MCP Server，在Installed里点击Configure MCP Servers，会打开cline_mcp_settings.json文件，在文件添加MasterGo MCP Server的配置。具体代码如下，其中\<MG_MCP_TOKEN\>换成从MasterGo生成的令牌。

    {  "mcpServers": {    "mastergo-magic-mcp": {      "command": "npx",      "args": [        "-y",        "@mastergo/magic-mcp",        "--token=<MG_MCP_TOKEN>",        "--url=https://mastergo.com"      ],      "env": {        "NPM_CONFIG_REGISTRY": "https://registry.npmjs.org/"      }    }  }}


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjUVHUdkYfcYBBvAPAPBQx4SbeIW2iccwDFWUNwTdm8crdXQ90jur7wuxJShhx3Pdb2VCNdqWChsfcGaiaWUqMjOA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)


配置后会自动更新，在Installed里边里如果mastergo-magic-mcp是绿灯并且是打开状态，则表示配置成功。现在可以进行测试了。

使用MasterGo设计稿转HTML代码

这里我们使用MasterGo官方提供的DEMO进行测试，容器地址如下：  

    https://mastergo.com/file/155675508499265?page_id=1%3A0&layer_id=24%3A1312


官方DEMO图：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjUVHUdkYfcYBBvAPAPBQx4SbeIW2iccwDbjfeqDTOy0gKzrYmnibKEicic2ggPlpMJwzqlCtXPAKicCcFYq21R1dZ6Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

如果要使用自己的设计稿进行测试，请先选中容器后再复制浏览器中的URL地址，确保URL中包含page_id以及layer_id参数。

进入Cline对话框，输入容器链接以及你希望Cline为你做的事，比如"生成html代码"。  

无剪辑的生成过程如下，速度不算快，可以倍速观看：

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

最终生成的HTML

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjUVHUdkYfcYBBvAPAPBQx4SbeIW2iccwDF8P9SlCIcdc1lkibgnLKhBBO438LwD1Yqetuoc59k7mXSoQfPnRM1Bg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

几乎是完全还原。

测试结论

本次使用的大模型是deepseek-v3免费版，Cline做MCP客户端（Cursor与Cline都支持MCP），输入指令后模型会自动识别可用的MCP工具，进行HTML生成。

在写这篇文章时，整体表现可圈可点，一次性生成的HTML与官方提供的DEMO几乎一比一还原，但实际多次的测试结果发现生成也不稳定，具体表现为调用超时、生成的HTML与官方DEMO差异较大，需要多次交互才能够到想要的结果。

对于复杂页面的实现几乎无法还原设计稿，通过MCP确实能够扩展模型的能力，且随着MCP Server越来越多，可玩的方法还有很多，但还需要让子弹飞一会。

写在后面


MasterGo MCP提供了设计稿转代码能力，但本质是一个编码诉求。在之前使用Cursor+Claude3.7通过设计图片+自然语言修正，效果似乎更好，但调试的过程是漫长的。对于PD来说，使用详细的PRD作为Prompt利用这类工具是可以实现完整的产品落地，当然具备一定的编码能力会让这件事变得更简单。

祝工作顺利。

*** ** * ** ***

**关于我**

一个数据产品经理  

个人微信：[Johnney_Ann]()

(点击可复制，注明来意)

公众号，在下方点击查看

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FjUVHUdkYfcZbYa4mzDiaz3QPicaEMxtkDK7ge0uLWQD3uj7GODib329KhnnsTCJ2dbAHXJoibTueO2Wm4MXxQfzYiaA%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**安阳im**

没事写点东西。

38篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIwMjkwMDAwMg==&mid=2247485774&idx=1&sn=8ae26b58c222b22a658325119a351616&chksm=97a692e72dea40f4a6ee4f7f1884a7a5e855661d9ba4c5fca60b0febb04adf8d5337c6b72801&mpshare=1&scene=1&srcid=0413r4bTuM7JD9Dp6wATiWad&sharer_shareinfo=4c5d6d71ad52e188397b8c4d9ca21ba8&sharer_shareinfo_first=4c5d6d71ad52e188397b8c4d9ca21ba8)

