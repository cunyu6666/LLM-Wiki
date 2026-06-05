---
id: "7452001990797692412"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODkyOTkwOQ==&mid=2247498528&idx=1&sn=60f24a895aa044616bdaf01bcc884b70&chksm=c1087e79f0afe0b89aea056dd1ad2b47bbeeb287d84912be4bef9e0c16c2a2c6e08dec150580&mpshare=1&scene=1&srcid=0507ZKdSqRDiMPY94zefIw9s&sharer_shareinfo=eda48bf6319bed4cf86d35f5fcd24754&sharer_shareinfo_first=eda48bf6319bed4cf86d35f5fcd24754
author: "鳗鱼 AIGitHub"
collected: 2026-05-07
tags: []
---

# 斩获4.6Kstar的开源AI排版项目！Kami：让AI生成的文档也能精致又好看！

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg5ODkyOTkwOQ==&mid=2247498528&idx=1) · 鳗鱼 AIGitHub


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZdrSHaq5Gr1uXuaAG1Jgibd5DC6ibtVhrX4ff5eQib3ZApns6BEqpPxkBUXQ2PHQMsO6E9djzk54CbcU4MPx8Zibicg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26randomid%3Du1uwjimf%23imgIndex%3D0)

很多人用 Claude 等 AI 写研究报告或文档，但默认输出往往是纯白背景、默认黑字、排版随意且每次风格都不一致，内容再好也让人不想读。

于是开源作者 tw93就开源了Kami，这是一套专为 AI Agent 设计的文档设计系统与排版约束语言，在GitHub上已经斩获了4.6Kstar！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9Q9Z2icqic4kGibRsgKmHiaibv3TK6OLsyKBCWAk4evqTD4FsMts6mJe26yYzqgG6eAcdA4YVpf7RyUIFIqDubJLqoR2P3vuE6icg1DkE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D61)

Kami 把这些经验抽象成一套严格的视觉与排版规则，让 AI 生成的内容能稳定输出成像印刷品一样的专业文档。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9QibWJhpncI4prPZ4nXkgNTIIOn4iak1QoCS3GOxIV2o8gicScAmFlz8lyDdHBXFGliaV8ksp4T7tdvibZar51IdzvicBGEDicY3BAJ4mw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D62)

它并非UI框架，而是面向静态文档/印刷品的约束系统：文档应当像精心编排的页面，而不是仪表盘。

Kami 以 Claude Code Skill 等形式分发，安装后通过自然语言描述需求即可自动套用视觉语言并生成 PDF，无需斜杠命令或额外提示词。同时，它也是作者"工作方法论三部曲"的最后一环：Kaku（写代码）、Waza（练习惯）、Kami（交付文档）。

##### 功能特点


**多类型文档模板**

内置多种常用文档形态，包括 One-Pager（一页纸报告/介绍）、Long Doc（白皮书/长文研究）、Letter（正式信函/推荐信）、Portfolio（作品集）、Resume（简历）、Slides（演讲幻灯片）等，并逐步扩展至更多类型（如 Equity Report、Changelog 等），多数模板提供中英（及部分日文）支持。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTJPc1U4E9Qic7ic0lQq7B8GUjaJBnPCOGBCJ26gEz8t7b6zI5YfCCtibTq1j3gZFNbIJkT2116tMTgxtibJasWcapfXRaBwn4iaia8l7fialybImpA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D63)

**内嵌图表能力**

内置多种内联 SVG 图表（如架构图、流程图、柱状图、折线图、时间线等），AI 可直接注入文档，减少对外部图片或 JS 库的依赖，保证文档自包含与一致性。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9Q99wwb6SoHM5Dhq4y1iaB9MR16ibxh9RRJveRAVywiatKiboFmTumLXD5iaZh4vVRQDIFmzTCnGfHvCsuLZVxHN8J4KFU0UXuURy36c%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D64)

**多语言与字体体系**

中文、英文为一等公民，日文通过 CJK 路径支持（交付前建议视觉 QA）。字体选择强调"每语言单一衬线体"的克制：中文用仓耳今楷 02、英文用 Charter、日文用 YuMinchi，整体偏向印刷质感的 serif 风格。

**易集成与低门槛触发**

支持 Claude Code、Codex、Claude Desktop 等环境，通常通过一条 npx skills add ...命令或上传 ZIP 即可完成安装；安装后直接用自然语言描述需求即可触发对应排版与生成流程。

**品牌/个人信息固化**   

可通过配置文件（如 brand.md）固化姓名、职位、品牌色等信息，减少重复描述，提高多轮产出的一致性。

##### **核心创新**


Kami 的关键不在"模板多漂亮"，而在**用一套跨文档的硬约束替代随意的样式漂移** ，让 AI 输出从"每次像不同人排的"变成"每次像同一套设计系统排的"。其设计规则大致可概括为几类（每一条都指向可读性、一致性与印刷感）：

**底色与情绪** ：页面背景使用暖米色，避免纯白刺眼与"廉价感"，建立温暖、专业的视觉基调。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTJPc1U4E9Q9mpdUWiaBwcjaUqpgPPcoyHYDq8txCDYufTrdnGCPGiazkDvhAiaH2DgbnfwcVD1czMseJZxmH8qjPkX9WUK7gb03GHNcRHA44qg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D65)

**字体与字重约束** ：各语言尽量使用单一 serif 字体；字重趋向固定，避免随意加粗，需要通过层级时用字号、间距或竖线等方式表达强调，从而保持格调统一。

**面向 Agent 的稳定性** ：规则简单到 AI 能稳定执行，又严格到输出可直接交付；图表与样式尽量自包含，减少外部依赖导致的渲染不确定性。

##### **应用场景**


Kami 适合"经常用 AI 生成文档，但受够了默认排版"的人群与场景，例如：

**职场与商务输出** ：一页纸方案/公司介绍、正式信函、推荐信、项目提案等，提升专业度与信任感。

**研究与分析材料** ：研报、行业/技术白皮书、长篇分析与研究报告，兼顾结构、可读性与视觉统一。

**个人展示与求职** ：作品集、简历等，强调清晰结构与克制美观，减少"排版分心"。

**演讲与汇报** ：幻灯片/演讲材料，配合内嵌图表快速形成可交付的演示文档。


    GitHub：https://github.com/tw93/Kami


**【招募兼职 AI 文案作者】**

招募熟悉 AI 领域、有写作经验的兼职作者，负责AI相关文章创作。

按篇结算，稿费从优，要求对 AI 工具、AI 应用、行业动态有一定了解，文笔通顺、逻辑清晰。

有意者可添加VX：wenhuaijun94

**欢迎扫码加入社群**

**一起交流AI前沿技术！**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FTJPc1U4E9QicZDQAGDnx4P2f6TZQXGtNkBA9nichMYTYhC1hia6G4m0IQmFwVgMQicOwtnMuGzf6cLNycugKbWQ5mXW3mHGaj9ickR7ctP1ZQhYk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D66)

**小编免费共享AI开源项目知识库，**

****实现大家的AI资讯自由！****

****直接扫码或点击链接即可查看！****

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FZdrSHaq5Gr2icoAqL9FLIibAkebXyIt25G4z0EOJ8nVNrIQA45Bpnbotv000NOyLBQW92us6z977xIo5Qs1zsCTg%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%26randomid%3Dhvcwn0ta%23imgIndex%3D12)

AI开源项目知识库：https://qyxznlkmwx.feishu.cn/wiki/BwWIwsCOuiMWGmkUzNHcKLvPnPh

点击下方名片「**关注我们**」第一时间收到推送

![](https://image.cubox.pro/cardImg/2kd0hamq06wa0f9wise0vv84nwn30e119ohhfwoiz5w5cjx42x?imageMogr2/quality/90/ignore-error/1)

**AIGitHub**

专注GitHub开源AI项目、AI前沿资讯、最新AI工具分享推荐

490篇原创内容

<br />

公众号  

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzg5ODkyOTkwOQ==&mid=2247498528&idx=1)
