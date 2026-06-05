---
id: "7303658987986095411"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247489814&idx=1&sn=d6e4dd77590a4e26417bec8a56ae36dc&chksm=c06f8eee18114cb7d9b0218aaac24b96e0cb04e02144b712fc76ce255bf6caac213726ef16b3&mpshare=1&scene=1&srcid=0324RMMJnMMhsPUE6Auyqy3k&sharer_shareinfo=3eb28b64d6092f408063a34ded6f8913&sharer_shareinfo_first=3eb28b64d6092f408063a34ded6f8913
author: "老码小张 老码小张"
collected: 2025-03-24
tags: []
---

# 好家伙，MCP 和 Cursor AI 联手，打通了 Figma 的任督二脉！

# 好家伙，MCP 和 Cursor AI 联手，打通了 Figma 的任督二脉！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247489814&idx=1&sn=d6e4dd77590a4e26417bec8a56ae36dc&chksm=c06f8eee18114cb7d9b0218aaac24b96e0cb04e02144b712fc76ce255bf6caac213726ef16b3&mpshare=1&scene=1&srcid=0324RMMJnMMhsPUE6Auyqy3k&sharer_shareinfo=3eb28b64d6092f408063a34ded6f8913&sharer_shareinfo_first=3eb28b64d6092f408063a34ded6f8913)老码小张 老码小张

哈喽大家好，我是老码小张！一个喜欢琢磨技术背后的原理，还老想着怎么用技术搞点事情的家伙。

最近我发现了一个超酷的玩意儿，能让 Cursor AI 直接跟 Figma 沟通！Cursor 你们知道吧？就是那个号称能帮你写代码、改 bug 的 AI 编程助手。Figma 呢，就是设计师们最爱的那个设计神器。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FoXqG8ETvAemMfCoAdQJtAxY3hVSu4DybnbbUGDsKOQnb9ib55Czc3GFb0TuvuF0cK4ux9KxZGW1Vh1rjKxsaEEw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

这俩看似八竿子打不着的工具，居然能通过一个叫 MCP (Model Context Protocol) 的协议给串起来。这就厉害了，这意味着，以后咱们可以用 Cursor AI 来控制 Figma，自动改设计稿、生成设计元素，甚至还能把设计稿里的东西导出来！

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

想想就觉得很爽啊！以前设计师画完图，咱们还得手动去切图、量尺寸、写代码，现在有了这个，直接让 Cursor AI 帮咱们搞定，效率直接起飞！

### 这玩意儿到底是怎么实现的？

我深入研究了一下这个项目:项目地址^\[1\]^，发现它主要由三部分组成：

1.
   1. **MCP Server (TypeScript)** ：这部分是用 TypeScript 写的，它负责跟 Cursor AI 那边对接。你可以把它想象成一个翻译官，把 Cursor AI 的指令翻译成 Figma 能听懂的话。
2.
   2. **Figma Plugin** ：这是个 Figma 插件，负责接收 MCP Server 发过来的指令，然后在 Figma 里执行。
3.
   3. **WebSocket Server** ：这是个中间人，负责 MCP Server 和 Figma Plugin 之间的通信。

整个流程大概是这样的：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FoXqG8ETvAemMfCoAdQJtAxY3hVSu4DybDiaFBUXqCJ6dyATp06hPhhJa93Bwj4Ckd4icCrke8GG7V5iasO5gnfD6Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg "null")

1.
   1. 咱们在 Cursor AI 里输入指令，比如"帮我创建一个红色的矩形"。
2.
   2. Cursor AI 把这个指令发给 MCP Server。
3.
   3. MCP Server 把指令翻译成 Figma Plugin 能听懂的格式，通过 WebSocket Server 发给 Figma Plugin。
4.
   4. Figma Plugin 收到指令后，在 Figma 里创建一个红色的矩形。

### 快速上手，让 Cursor AI 操控你的 Figma！

想要体验这个神奇的功能，其实很简单，跟着我一步步来：

1.
   1. **安装 Bun** ：Bun 是一个 JavaScript 运行时，跟 Node.js 差不多，但是更快。

       curl -fsSL https://bun.sh/install | bash


2.
   2. **运行安装脚本** , 在你项目的根目录下，运行：

       bun setup


3.
   3. **启动 WebSocket Server** ：

       bun start


4.
   4. **安装 Figma 插件** ：
   *
     • 在 Figma 里，依次点击 Plugins \> Development \> New Plugin。
   *
     • 选择 "Link existing plugin"。
   *
     • 找到项目里的 src/cursor_mcp_plugin/manifest.json 文件，选中它。
   *
     • 搞定！现在你的 Figma 开发插件列表里应该能看到这个插件了。
5.
   5. **在 Cursor 里配置 MCP Server** ：
   *
     • 打开 Cursor 的配置文件 ~/.cursor/mcp.json。
   *
     • 在 mcpServers 里添加一个新的配置项，像这样：

         {
           "mcpServers":{
             "TalkToFigma":{
               "command":"bun",
               "args":[
                 "/path/to/cursor-talk-to-figma-mcp/src/talk_to_figma_mcp/server.ts"
               ]
             }
         }
         }

     注意把 /path/to/cursor-talk-to-figma-mcp 换成你项目的实际路径。

### Cursor AI 都能让 Figma 干点啥？

这个项目提供了一堆工具，让 Cursor AI 可以操控 Figma 的方方面面。我挑几个常用的给大家介绍一下：

*
  • **获取信息** ：
  *
    • get_document_info：获取当前 Figma 文档的信息，比如有哪些页面、每个页面里有哪些图层。
  *
    • get_selection：获取当前选中的元素。
  *
    • get_node_info：获取某个元素的详细信息，比如位置、大小、颜色等等。
*
  • **创建元素** ：
  *
    • create_rectangle：创建一个矩形。
  *
    • create_frame：创建一个画框，可以理解为一个容器。
  *
    • create_text：创建一个文本框。
*
  • **修改样式** ：
  *
    • set_fill_color：设置填充颜色。
  *
    • set_stroke_color：设置描边颜色和粗细。
  *
    • set_corner_radius：设置圆角。
  *
    • set_text_content：设置文字内容
*
  • **调整布局** ：
  *
    • move_node：移动元素的位置。
  *
    • resize_node：调整元素的大小。
  *
    • delete_node：删除
*
  • **导出和高级**
  *
    • export_node_as_image: 导出节点为图片
  *
    • execute_figma_code: 直接在 Figma 中执行 js 代码

基本上，有了这些工具，咱们就可以让 Cursor AI 在 Figma 里为所欲为了！

### 一些开发中的最佳实践

在使用这个工具的过程中，我总结了一些经验：

*
  • **先连接通道** ：在发送任何指令之前，一定要先调用 join_channel 来连接到 Figma。
*
  • **先获取文档概览** ：在开始操作之前，最好先用 get_document_info 获取一下整个文档的结构，这样心里有数。
*
  • **先检查当前选中** ：在修改元素之前，最好先用 get_selection 确认一下当前选中的是什么，避免改错东西。
*
  • **根据需求选择合适的创建工具** ：
  *
    • 如果需要创建容器，用 create_frame。
  *
    • 如果只需要创建简单的形状，用 create_rectangle。
  *
    • 如果需要创建文本，用 create_text。
*
  • **用组件实例** ：如果需要创建多个相同的元素，最好用组件实例 (create_component_instance)，这样可以保持一致性。
*
  • **错误处理** ：每个指令都可能会出错，所以一定要做好错误处理。

### 同类工具对比

其实，除了这个项目，还有一些其他的工具也能实现类似的功能。我这里简单对比一下：

|              工具               |                       优点                        |                      缺点                      |
|-------------------------------|-------------------------------------------------|----------------------------------------------|
| Cursor Talk to Figma MCP      | 集成 Cursor AI，可以通过自然语言控制 Figma；功能丰富，支持多种操作；开源免费。 | 需要一定的配置和安装步骤；依赖 Cursor AI 和 Figma 插件。        |
| Figma API                     | Figma 官方提供的 API，功能强大，稳定可靠。                      | 需要编写代码，学习成本较高；不方便直接通过自然语言控制。                 |
| 其他第三方插件 (如 CopyCat, Magician) | 通常有特定的功能，比如自动生成代码、自动布局等；可能有更友好的用户界面。            | 功能可能不如 Cursor Talk to Figma MCP 全面；有些可能是收费的。 |


Cursor Talk to Figma MCP 这个项目还是很有优势的，特别是它跟 Cursor AI 的集成，让我们可以用自然语言来控制 Figma，这简直是懒人福音啊！

### 说了这么多

Cursor Talk to Figma MCP 这个项目，把 Cursor AI 和 Figma 这两个强大的工具连接了起来，让我们有了一种全新的方式来跟设计稿交互。我相信，随着 AI 技术的不断发展，这种跨工具的协作方式会越来越普遍，我们的工作效率也会越来越高！

好了，今天就跟大家分享到这里。如果你觉得这篇文章对你有帮助，别忘了点赞、评论、转发三连哦！

#### 引用链接

[1] 项目地址: *https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp*   

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247489814&idx=1&sn=d6e4dd77590a4e26417bec8a56ae36dc&chksm=c06f8eee18114cb7d9b0218aaac24b96e0cb04e02144b712fc76ce255bf6caac213726ef16b3&mpshare=1&scene=1&srcid=0324RMMJnMMhsPUE6Auyqy3k&sharer_shareinfo=3eb28b64d6092f408063a34ded6f8913&sharer_shareinfo_first=3eb28b64d6092f408063a34ded6f8913)

