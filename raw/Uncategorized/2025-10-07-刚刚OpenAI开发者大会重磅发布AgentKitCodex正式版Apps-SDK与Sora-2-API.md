---
id: "7375174274769749180"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650994027&idx=1&sn=bb0eadc486c25ffbf203c93286492d98&chksm=8570f1aa75c6333bddde959c6b07ba727435791b35bf593d06c618ec67a213ab82dd8f98a079&mpshare=1&scene=1&srcid=1007C3NG4lT7xQIEDWaInHUY&sharer_shareinfo=614581857f48284ff2a1589cd5afd552&sharer_shareinfo_first=614581857f48284ff2a1589cd5afd552
author: "机器之心 机器之心"
collected: 2025-10-07
tags: []
---

# 刚刚，OpenAI开发者大会重磅发布：AgentKit、Codex正式版、Apps SDK与Sora 2 API

# 刚刚，OpenAI开发者大会重磅发布：AgentKit、Codex正式版、Apps SDK与Sora 2 API

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650994027&idx=1&sn=bb0eadc486c25ffbf203c93286492d98&chksm=8570f1aa75c6333bddde959c6b07ba727435791b35bf593d06c618ec67a213ab82dd8f98a079&mpshare=1&scene=1&srcid=1007C3NG4lT7xQIEDWaInHUY&sharer_shareinfo=614581857f48284ff2a1589cd5afd552&sharer_shareinfo_first=614581857f48284ff2a1589cd5afd552)机器之心 机器之心


机器之心报道

**编辑：Panda**

OpenAI 今年的开发者大会（OpenAI DevDay 2025）正在进行中。

Keynote 一开场，山姆・奥特曼便分享了 OpenAI 这两年取得的成绩：400 万开发者、8 亿周活 ChatGPT 用户、API 每分钟 60 亿 token 消耗量。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudgB6A6GLndJemyib5aT9yMDx3qDlpNibL1WS4CoXeZUia7CYFhWYiapNxfw%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D0)

更重要的是，OpenAI 在今年的开发者大会上可真是发布了不少东西，简单总结起来包括：AgentKit、Codex 正式版、ChatGPT 内置应用与 Apps SDK、gpt-realtime-mini、gpt-image-1-mini、Sora 2 API、GPT-5 pro API。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudKLoRMCkdlryibiaHECIYCkD1y6eZrsUWU8dr5njfmPyStia9VkeKRsznw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

下面具体来看看这些新模型和新工具。

AgentKit

首先，最引人瞩目的便是：AgentKit。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudVCSZb1fjJcl59ccLkxIq4yDaprhQcFdZwoZumwAleUYoibT5dicAcGKA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

AgentKit 是一套面向开发者和企业的完整工具集，可用于构建、部署和优化智能体（agent）。

这让不少人惊呼：OpenAI 「杀死」了大量创业公司。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQud1g9vlQ3nDYryiaqr9KXicGVuITUBsY3vyPWpWhB2eJfhjMmf1JdWPlJQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

OpenAI 为 AgentKit 设计了一些全新的模块化组件，可助力用户更快地开发智能体，包括 Agent Builder、Connector Registry 和 ChatKit。

Agent Builder

乍一看，Agent Builder 的界面与扣子等工作流编排工具非常相似，可让用户可视化地设计工作流。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudmpAdHNrGe1rwCIc3ibBxr0UAInQ1sTOdBrbIpc9ClSfSy0FKt63Cqug%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

具体来说，可视化画布 Agent Builder 可用于创建、管理和版本化多智能体工作流；其提供了一个拖拽式的可视化画布，用于组合逻辑节点、连接工具、配置自定义安全护栏。它支持预览运行、内嵌评估配置和完整版本控制，非常适合快速迭代。

Guardrails（护栏）是 Agent Builder 中一个开源、模块化的安全层，用于防止智能体出现意外或恶意行为。它可用于屏蔽或标记个人信息（PII）、检测越狱尝试、应用其他安全机制。Guardrails 可以单独部署，也可通过 Python 或 JavaScript 库集成。用户可以选择是否启用它。

Connector Registry

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudcIMWITarI20vJpdVgXMy6Vkas0X9HJwWqe9ARHYWPFNc3IiaSaVD8kg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

用于集中管理数据与工具在 OpenAI 产品中的连接方式；其在一个管理面板中整合了 ChatGPT 和 API 的所有数据源，包括预置连接器（如 Dropbox、Google Drive、SharePoint、Microsoft Teams）及第三方 MCP。

ChatKit

一个工具套件，可以将基于聊天的智能体直接嵌入用户的应用或网站，并自定义外观与品牌风格。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudmxI0ia5Ceyxb3uk8RTa7Mw6Jpt7PRggz3jRrGaRRxWiaWbAhTDo87jaQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

目前，ChatKit 已广泛应用于内部知识助手、新员工入职引导、客服支持、研究助手等场景。OpenAI 表示 HubSpot、LegalOn、Evernote、Taboola 等公司都已使用 ChatKit 来增强产品交互体验。

评估

此外，OpenAI 还扩展了评估功能，引入了数据集、trace 评分、自动提示词优化、第三方模型支持等新特性。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudm9XSGkaAYDNGibFSkwsd6DibkxeqXKzkgKBYUChNNkYtRtmdZtJya48Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)

OpenAI 表示：「自从 3 月推出 Responses API 和 Agents SDK 以来，我们看到开发者和企业已经在使用它们构建端到端的智能体工作流，例如用于深度研究、客户支持等。Klarna 构建的客服智能体现已处理了全部工单的三分之二，而 Clay 则通过销售智能体实现了 10 倍增长。而 AgentKit 正是在 Responses API 的基础上构建的，可以帮助开发者更高效、更可靠地构建智能体。」

强化微调

强化微调（RFT）让开发者能够定制 OpenAI 的推理模型。目前它已在 o4-mini 模型上全面开放，并在 GPT-5 上进入私测阶段。OpenAI 表示正与数十家客户合作，持续完善 GPT-5 的 RFT 体验。

OpenAI 介绍了此次在 RFT 私测中新增的两项关键功能：

* Custom tool calls：可让模型学会在合适时机调用正确工具，提高推理效率；

* Custom graders：可让用户自定义评估标准，从而聚焦最关注的性能指标。

价格与可用性

从今天起：

* ChatKit 与全新的评估功能已对所有开发者全面开放

* Agent Builder 进入公开测试（Beta）

* Connector Registry 正在逐步向部分 API、ChatGPT Enterprise 和 Edu 客户开放测试，Connector Registry 需要通过 Global Admin Console 启用（供全局管理员管理域名、SSO、多组织 API 等）。

* 以上所有工具均包含在标准 API 模型定价中。

OpenAI 表示，计划在不久的将来为 ChatGPT 增加独立的 Workflows API 与智能体部署选项。

Codex 正式版

今天，CodeX 正式版（General Availability）上线，并带来了三项全新功能：

* 全新的 Slack 集成：用户现在可以像与同事交流一样，在团队频道或线程中直接向 Codex 分配任务或提问。

* Codex SDK：可将驱动 Codex CLI 的同款智能体嵌入用户自己的工作流、工具或应用中，在 GPT-5-Codex 上实现最先进性能，无需额外微调。

* 全新的管理员工具：通过环境控制、监控与分析面板，ChatGPT 工作区管理员可以更好地掌控 Codex 的使用和运行。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudDxgS8Nh0V5orU32ByTy02Krib3rSYGo7oa3nkKfaRzic5BPEgnKoibmLw%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D8)

自从今年 5 月 Codex 云端智能体（Codex cloud agent）以研究预览版推出以来，Codex 已稳步演进为一个更可靠、更强大的编码协作伙伴。

现在，用户可以在所有编码场景中使用 Codex（编辑器、终端、云端）都通过 ChatGPT 账号互联。

OpenAI 还介绍了 Codex 的用户增长情况：自 8 月初以来，Codex 的日活跃使用量增长了 10 倍以上，而 GPT-5-Codex 也成为增长最快的模型之一，在上线后短短三周内就处理了超过 40 万亿 token。

如今，Codex 已被全球不少开发者广泛采用 ------ 从 Duolingo、Vanta 这样的初创公司，到思科、乐天这样的企业巨头。OpenAI 表示：「在 OpenAI 内部，Codex 也已成为我们研发流程中不可或缺的一部分：从 7 月时的一半工程师使用，到现在几乎所有工程师都在用。他们每周合并的 PR 数量增加了 70%，而 Codex 会自动审查几乎所有 PR，在问题进入生产环境前就能发现关键缺陷。」

ChatGPT 内置应用与 Apps SDK

OpenAI 还正式发布 ChatGPT 新一代可对话应用（Apps）。用户现在可以直接在 ChatGPT 聊天界面中与这些应用交互。

这些应用可与 ChatGPT 的对话体验无缝融合。用户可以在对话中被智能推荐到合适的应用，也可以直接「呼叫」它们的名字。这些应用支持自然语言交互，并在聊天窗口中内嵌交互式界面，让体验更直观。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudny3SIFODibbzhJWMFf3nwNzaAlqVKMcJ6gCL5HI4Gf1dKMXG5LXuZRA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D9)

对用户而言，ChatGPT 中的应用会根据用户上下文动态适应，提供创作、学习、任务执行等方面的帮助。

从今天起，除欧盟地区外，所有登录的 ChatGPT 用户（Free、Go、Plus、Pro 版本）均可使用这些应用。首批上线的应用包括：Booking.com、Canva、Coursera、Figma、Expedia、Spotify、Zillow。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudicBtBujiaAzGrswAxIZgWicdzk0tMjoDRRibpaCHRwfSGIRkWsVAAwiaAicw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D10)

开发者也可从今天起，使用全新的 Apps SDK（预览版） 开始构建属于自己的 ChatGPT 应用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQud0l3rAPMibXSVhvBBicWaIJQSHmOveAlURhibA5lwlVpMUthibMXNodNxtg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D11)

该 SDK 基于 Model Context Protocol (MCP) ------ 一种开放标准，使 ChatGPT 能连接外部工具与数据。Apps SDK 在此基础上进一步扩展，让开发者能够同时设计应用的逻辑与界面。

Apps SDK 已经开源。

此外，通过 Apps SDK 构建的应用还可以在恰当的时机触达超过 8 亿 ChatGPT 用户。

OpenAI 计划今年晚些时候把应用功能扩展到 ChatGPT Business、Enterprise 和 Edu 版本。届时也会开放应用提交流程，让开发者能正式在 ChatGPT 上架应用。

他们还将推出一个专属的应用目录（App Directory），用户可在其中浏览、搜索、发现应用。

gpt-realtime-mini

OpenAI 还发布了一个 GPT Realtime 的 mini 版本，可通过 WebRTC、WebSocket 或 SIP 连接实时响应音频和文本输入。以下截图展示了其一些参数和定价信息：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudrByclpR2KtuJicllfomGRnHkaktGrAFXFOgaibKcAYXdGRRq7icbt3DMw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D12)

gpt-image-1-mini

另外，OpenAI 也为 GPT Image 1 模型打造了一个 mini 版本。它是一种原生多模态语言模型，可同时接受文本和图像输入和生成图像输出。以下截图展示了其一些参数和定价信息：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudSj4ibCtONnqCkBHQFSC1ObnicXkvuFXiapSldGj3Eic056fFgnC0H2Hkxw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D13)

Sora 2 API

Sora 是 OpenAI 在生成式媒体领域的最新前沿成果。这是一款最先进的视频生成模型，能够根据自然语言或图像生成具有丰富细节、动态画面与音频的视频片段。

Sora 基于多模态扩散模型（multimodal diffusion）多年研究成果构建，并在多样化的视觉数据上训练，使其在三维空间理解、运动建模和场景连贯性方面具备深厚能力，将文本到视频的生成质量推向新高度。

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

今天，OpenAI 也首次通过 Video API 首次向开发者开放 Sora 的能力，支持通过编程方式创建、扩展或混合（remix）视频内容。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudfAtpu3kiaMrCPQBjuGLwR2r0oTKgZkSMkPXLZnVAickyS4hKMTTKSjzQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D14)

它包含五个端点（endpoints），每个端点都有不同的功能：

* Create video（创建视频）：从提示词开始一个新的渲染任务，可选择性添加参考输入或 remix ID。

* Get video status（获取视频状态）：查询渲染任务的当前状态，监控其进度。

* Download video（下载视频）：任务完成后，下载生成好的 MP4 文件。

* List videos（列出视频）：分页查看你的历史视频记录，用于展示、管理或清理。

* Delete videos（删除视频）：从 OpenAI 存储中移除指定视频 ID。

Sora 2 系列目前提供两个变体，针对不同使用场景优化。

* Sora 2：注重速度与灵活性，适用于创意探索阶段，注重快速反馈而非极致画质。特点是生成速度快、质量佳，适合快速迭代、概念验证或粗剪阶段。推荐用途：社交媒体内容、产品原型、需要快速产出的项目。

* Sora 2 Pro：支持专业级画质，适用于需要高质量视频的场景、可直接用于生产的内容。其渲染时间更长、成本更高，但输出更加稳定、细腻、逼真。推荐用途：高分辨率电影镜头、营销视频、以及对视觉精度要求极高的项目。

GPT-5 pro API

强大推理模型 GPT-5 pro 的 API 也已经上线：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FKmXPKA19gWibmcicic9rKXFgic4uTu8XDQudFzxduVoGIpx1hLr20vg1bKoLZdGNrZdoEtcwibc8kyCQvPksibghbCaA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D15)

对于 OpenAI 这场正在进行中的开发者大会，你有什么期待？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FKmXPKA19gW9Bp2wicyhZaMEwwc2j43whc8nicGBovZKFKcYIC63iblWMeTmeRicmtKutf2uevdGXMrc8uEZzlPWYVA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D16)


© THE END

转载请联系本公众号获得授权

投稿或寻求报道：liyazhou@jiqizhixin.com

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650994027&idx=1&sn=bb0eadc486c25ffbf203c93286492d98&chksm=8570f1aa75c6333bddde959c6b07ba727435791b35bf593d06c618ec67a213ab82dd8f98a079&mpshare=1&scene=1&srcid=1007C3NG4lT7xQIEDWaInHUY&sharer_shareinfo=614581857f48284ff2a1589cd5afd552&sharer_shareinfo_first=614581857f48284ff2a1589cd5afd552)

