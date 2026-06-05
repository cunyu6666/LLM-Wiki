---
id: "7447529834156132173"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ==&mid=2247484650&idx=1&sn=9319ac01be87985654732b7f5c5135dd&chksm=f55edb0052c49f7d324d1f58b53b68e0fdd17725daf90829a78c40968c81ab46efd08ebc648e&mpshare=1&scene=1&srcid=0425nPMIO8FmM4NEJi6EEJXx&sharer_shareinfo=2b5636a0dce6bee0c590467ca1f1153a&sharer_shareinfo_first=2b5636a0dce6bee0c590467ca1f1153a
author: "AI开源提效指南 AI开源提效指南"
collected: 2026-04-25
tags: []
---

# open-codesign：开源版 Claude Design , 本地优先的 AI 设计神器!

# open-codesign：开源版 Claude Design , 本地优先的 AI 设计神器!

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ==&mid=2247484650&idx=1&sn=9319ac01be87985654732b7f5c5135dd&chksm=f55edb0052c49f7d324d1f58b53b68e0fdd17725daf90829a78c40968c81ab46efd08ebc648e&mpshare=1&scene=1&srcid=0425nPMIO8FmM4NEJi6EEJXx&sharer_shareinfo=2b5636a0dce6bee0c590467ca1f1153a&sharer_shareinfo_first=2b5636a0dce6bee0c590467ca1f1153a)AI开源提效指南 AI开源提效指南


## 大家好！这里是AI开源提效指南！

Open Codesign 是一个由开源的桌面端 AI 设计工具。它被定位为 Claude Design 的开源替代品，不仅能通过 Prompt（提示词）快速生成原型、幻灯片、PDF 和各种 UI 设计，更重要的是------它把选择权还给了你。

它的核心理念是：本地优先 (Local-first) + 随心所欲 (Bring Your Own Key)。

如果你在使用 Claude Design 、v0 by Vercel 、Lovable 、Bolt.new 、Figma 等产品，建议大家可以耐心读完这篇文章！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FF1MjIPU9X0NSWcLN8icEBkvEia2nSsbKMnTLZPTyHicYyYYlwkc5BMNkd8mOxBhWgsoNct2Ueje9apsEvQZD3x51yG2xzcjN8cUrvbYa4OUj74%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)
> Your prompts. Your model. Your laptop. --- 将提示词转化为精美原型，本地运行，支持你自己的模型!

下面，我会安装测试，大家看看效果！

## 🚀 快速开始

大家去官方仓库的 releases 下载安装包，然后执行安装就行了！

这里我遇到了一个问题，我的Windows环境（Windows 11 专业版 x64）下载 x64 版本安装包出现了闪退问题，安装通用版本(open-codesign-0.1.4-setup.exe) 没问题，如果大家有 x64 版本问题，可以试试通用版本！

如果是 MacOS Sequoia 15+ 系统用户，可以参考执行 xattr -cr "/Applications/Open CoDesign.app" ，更多细节查看文末的**参考资源** ！

后面双击安装，选择安装目录就行了！

*
  1.我们先来配置我们的模型信息！ 这里它自动识别并帮我导入了！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FF1MjIPU9X0PTrWEVHtL0qtMocWUfnMGQhknhwRoUicDpB8ick8btHiaxTmiaDvhQC6aapXbrkAicyDJZ8YDalDG4KicMiajHHPicFSRrhVbWic6NH6Nc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

*
  2.这里我选择了一个默认的模板，来看看效果！


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FF1MjIPU9X0MYe22F5d1zDm8W9UYJMdv3wvpb0DibcaExEyAicUrJXIPmNedpJZLNRbJIfB5ibp2icj6KKsiaezxvRM2ibB4JqK5L9yRf4lNKMq0LA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

一会儿的时间，右侧就渲染出来落地页了！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FF1MjIPU9X0NgxlwoWAGVxzTMcwJGRib9WVLiaDic97GLOjqbTsOIBVnaCgGqlVfJTdxWxMkL82WC5EicTwQnltsDIcS1rBGVE17p48BJ71GMWmk%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

*
  3.丰富一下默认模板的信息！ 我让它补全，index 页面的超链接及页面信息！

  这里我输入：落地页中每个超链接帮我生成对应的页面！


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FF1MjIPU9X0OGCgnkD9niccWibZflmQfZaBHQGlCZua7EAgJGLqomDGNMVLyib5uC4gyxIOh5vamRl1cfvibUVr9V4yicKWYbNBGeex9VFo98soTU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

*
  4.看看效果！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FF1MjIPU9X0PgHtRP0I6secI7tsZxQSCNM7U2ofeYbSRomfdBQlZicq105lpIWBzRQQVnk6RX2qQuHJL9dicsDgp7ibiavy62kGhvhYIYYkFZcDY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FF1MjIPU9X0OOosJxV4wbW7NAW6P1gloUy0q9DsKwWOLiae2Q6hjcEdbic3JK4tiaz9t6bom0VudZhNzCHCiajWFfibpokAtA9yIeGAaCmTHpAXpw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

*
  5.大家可以按需导出自己想要的文件格式！


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FF1MjIPU9X0Pr6tdVTNKibIdClgdfDfPL9TYyh9rj4kCzcO51BHmMSBfiagpIOFmKptatE6M2q25JOxUtYVic47ayQvssEVnP4et8siann3H5Jyw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

## 💡 15 个内置示例 + 12 个设计技能模块

从 **15 个内置示例** 中选择一个。几秒钟内就会出现一个沙盒原型。

|  设计技能  |     说明     |
|--------|------------|
| 幻灯片演示  | 专业的路演幻灯片布局 |
| 仪表板    | 数据可视化和管理界面 |
| 落地页    | 营销和产品介绍页   |
| SVG 图表 | 动态数据图表组件   |
| 玻璃拟态   | 现代玻璃态设计风格  |
| 编辑排版   | 精致的文字排版设计  |
| 英雄区    | 引人注目的页面头部  |
| 定价页    | 产品定价和对比表格  |
| 页脚     | 完整的网站页脚设计  |
| 聊天 UI  | 即时通讯界面     |
| 数据表格   | 复杂数据展示表格   |
| 日历     | 活动和日程日历    |


每个技能在每次生成中都可用。在模型编写 CSS 之前，它会选择适合需求的技能，并通过布局意图、设计系统一致性和对比度进行推理。

## 🎯 核心亮点

Open CoDesign 是一个开源的 Claude Design 替代品 --- 为那些想要 AI 原生设计工具的速度，但不想被订阅锁定、仅限云端工作流或单一提供商的用户打造。

它不仅仅是一个对话框，而是一个生产力工具。

系统包含**15 个内置示例 + 12 个设计技能模块！** 基本上就是开箱即用！

输入提示词描述你的想法，它能直接生成网页原型、数据看板、幻灯片 (PPTX)、PDF 等。

他还能实时调试，提供直观的滑块调节工具（颜色、间距、字体等），无需反复重写 Prompt 即可精细调整设计细节。

Open CoDesign 支持 从 Claude Code 或 Codex 一键导入 API 配置，打开设置就会识别并导入了我的Claude Code 配置！

**响应式预览** ： 内置手机、平板、桌面三种视图，设计效果一眼就能看见！

**支持任意模型** ：只要模型支持 OpenAI Chat、OpenAI Responses、Anthropic Messages 协议就可以使用！当然也支持 Ollama，关于Ollama，如果大家想了解，可以在评论区留言，我可以出一期部署使用教程！

**支持多种文件格式导出** --- HTML、PDF、PPTX、ZIP、Markdown 五种格式！

**透明可见** : 实时代理活动、可见的工具调用、可中断的生成过程，你也可以在设置中查看执行日志。设置中有日志文件地址，直接打开就行了！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FF1MjIPU9X0OPjDhnSW8iaIyQardfODIFDKufUr6SRepf5ichYD3WYc9oiamzHaTibHDzYE13oiccr5q9GExIJh5XpPcTn6ia6FffzwcNr7Rj6uCJc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)


## 📚 参考资源

    项目地址: https://github.com/OpenCoworkAI/open-codesign
    官方网站: https://opencoworkai.github.io/open-codesign/


免责声明：本文内容仅供学习交流，所述工具/方法请遵守相关平台服务条款及法律法规。如涉及第三方服务，请以官方最新政策为准。

*** ** * ** ***

**🎯****觉得这份工具干货有用？希望收到您的支持：**

*
  ⭐ 星标 / 置顶公众号，**第一时间解锁最新工具分享！**
*
  ✅ **点赞** 「**推荐**」，让更多技术伙伴发现优质干货！
*
  🔗 **转发** 给团队小伙伴，一起高效提效！
*
  💬 **底部留言区** ，告诉我您想找的工具/项目方向！

**📬 长期追踪优质开源工具**

*
  关注「**AI 开源提效指南** 」｜日更开源神器，玩转技术提效！
*
  回复 **【容器加速器】** ，即刻开启你的高效探索之旅～


![](https://image.cubox.pro/cardImg/3npzozequ7qvgscmc6ms9r228jk9kczqxd8o2zj2mgtx4fpfvr?imageMogr2/quality/90/ignore-error/1)

**AI开源提效指南**

深耕云计算、devops 领域多年，每日推荐优质开源项目，用工具提升编程效率，用 AI 重构你的编程工作！

44篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ==&mid=2247484650&idx=1&sn=9319ac01be87985654732b7f5c5135dd&chksm=f55edb0052c49f7d324d1f58b53b68e0fdd17725daf90829a78c40968c81ab46efd08ebc648e&mpshare=1&scene=1&srcid=0425nPMIO8FmM4NEJi6EEJXx&sharer_shareinfo=2b5636a0dce6bee0c590467ca1f1153a&sharer_shareinfo_first=2b5636a0dce6bee0c590467ca1f1153a)

