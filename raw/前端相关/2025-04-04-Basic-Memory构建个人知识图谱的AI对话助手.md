---
id: "7307704184596334244"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzUxMzUzNzUzMw==&mid=2247499119&idx=1&sn=627cca378ab1db5ce9ae98688ae40704&chksm=f82682151a25879b73ca2a5bf1d5554103f2edfc52432bd69c918800f22bb6dd22838b1e34f4&mpshare=1&scene=1&srcid=0404WwTj2QuUqba8rmsZVzNE&sharer_shareinfo=02784d17fe15109856f3fddfb8169588&sharer_shareinfo_first=02784d17fe15109856f3fddfb8169588
author: "QOK AI AI Interface"
collected: 2025-04-04
tags: [AI知识管理]
---

# Basic Memory：构建个人知识图谱的AI对话助手

# Basic Memory：构建个人知识图谱的AI对话助手

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzUxMzUzNzUzMw==&mid=2247499119&idx=1&sn=627cca378ab1db5ce9ae98688ae40704&chksm=f82682151a25879b73ca2a5bf1d5554103f2edfc52432bd69c918800f22bb6dd22838b1e34f4&mpshare=1&scene=1&srcid=0404WwTj2QuUqba8rmsZVzNE&sharer_shareinfo=02784d17fe15109856f3fddfb8169588&sharer_shareinfo_first=02784d17fe15109856f3fddfb8169588)QOK AI AI Interface


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGQu9H5a66e5vXc0xXfLS4bzmY4oPFmiaibYCuTKfUJTOy4t3J7V7nPB8jejZBDAgLkW2HhrPmQTzSiaibibNMKl8A2Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Basic Memory 是一个知识管理系统，它能够保存与AI助手（如Claude）对话的上下文，并将这些知识以互联网络的形式存储为本地Markdown文件，从而构建一个随时间成长的个人知识图谱。这款工具让AI能够在新的对话中加载来自本地文件的上下文，实现真正具有连续性的AI辅助体验。

核心功能与解决方案

问题：AI对话的局限性

传统的AI对话存在明显局限：

- 对话结束后上下文消失

- 用户不得不重复已讨论过的信息

- 无法在先前的见解基础上继续构建

- 知识散落在不同的对话中，难以检索和连接

解决方案：知识持久化与智能关联

Basic Memory 提供了创新的解决方案：

1.持久化知识存储：所有对话内容以Markdown文件形式保存在本地，100%由用户控制

2. 知识图谱构建：笔记之间通过语义链接和观察自动连接，形成网状结构

3. 双向流动：可以直接编辑文件或通过AI对话修改内容，始终保持同步

4. 对话连续性：即使几周后，也能从上次中断的地方继续对话

5. 多项目管理：可为不同目的（工作、研究、特定领域）管理单独的知识库

6. 智能检索：AI可以找到并获取仅与当前话题相关的内容，无需上传整个知识库

视频加载失败，请刷新页面再试

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACIAAAAqCAMAAADhynmdAAAAQlBMVEUAAACcnJycnJycnJyoqKicnJycnJycnJycnJycnJyfn5%2BcnJydnZ2enp6kpKSdnZ2cnJyenp6cnJycnJycnJybm5t8KrXMAAAAFXRSTlMAyeb3CNp3tJRvHIEtJhBgqztWRJ%2Bp5TqGAAABCklEQVQ4y5WTi27DIAxFAUMhgTzX8%2F%2B%2FurB2pdKI0x0pSoRuruyLbf7gF3PBaDE6X44LyY0D1SJQsfd9PpMM%2FCJx60v8SmV1HMSi1lKyA1n0jnwWSO08l04uJbxpBmTrpDtbGB6fmxC6Tc4BHv9aZDJdJsHW9w43Jez9x8T5M4l31WZsJn2bsYY%2BnUum2lQkGIVANPZ4FCLWOJImSTgjZE2SkU9crmu57mj9JBc93Qzj9R1d3HSG5bN5MRsnUzcGKK8Ns02z%2BDa7rYQE4bUE2PG1C6kVnkCyf0pwX8%2FjwbyxCLhcHpKTFkvkwK3pRmXtRrVFoTGYLvN%2Bt0EUl0qrRaF1pFBz0anp%2FptvNB4SY1XDAVMAAAAASUVORK5CYII%3D) 刷新

工作原理

Basic Memory 让用户能通过自然交互构建和访问知识库：

1. 基于过往知识构建

AI在未来对话中引用之前的笔记内容。例如，用户可以说："让我们继续讨论咖啡冲泡的话题"，AI会检索相关笔记而非加载所有内容。

2. 自然对话

用户可以与Claude等AI助手进行正常对话。例如："查找关于手冲咖啡方法的信息"，AI会搜索用户的知识库并总结发现。

3. 保存知识

用户可以要求AI创建关于对话的笔记。例如："创建一个关于咖啡冲泡方法的笔记"，AI会创建一个结构化笔记，包含观察和关系。

技术实现

Basic Memory使用Model Context Protocol (MCP)与大型语言模型连接，特别适合与Claude Desktop配合使用。其底层技术实现包括：

- 所有内容以Markdown文件存储

- 使用SQLite数据库进行搜索和索引

- 从简单的Markdown模式中提取语义意义

- 维护从文件派生的本地知识图谱

- 提供文件和知识图谱之间的双向同步

- 实现Model Context Protocol (MCP)以实现AI集成

- 暴露工具让AI助手遍历和操作知识图谱

- 使用memory://URL引用实体

文件格式与结构

每个Markdown文件包含结构化元素，便于AI理解和处理：

前置元数据

    ---title: 咖啡冲泡方法permalink: coffee-brewing-methodstype: notetags:- 咖啡- 冲泡---


观察内容

观察内容是关于主题的事实，可以通过特殊格式的Markdown列表添加：

    观察- [方法] 手冲提供更清晰的口感并突出微妙的风味- [技术] 水温在205°F (96°C)能提取最佳化合物- [原则] 新鲜磨制的豆子保留香气和风味


关系

关系是与其他主题的链接，定义实体在知识图谱中的连接方式：

    关系- relates_to [咖啡豆产地]- requires [正确的研磨技术]- affects [风味提取]


与Obsidian无缝集成

Basic Memory与Obsidian编辑器完美集成，提供强大的视觉化知识导航功能：

知识图谱可视化

Obsidian的图谱视图揭示笔记之间的语义连接，展示整个知识网络结构。用户可以看到主题之间的关联，便于发现知识间的联系。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGQu9H5a66e5vXc0xXfLS4bzmY4oPFmiaib6xiaTbkoLkDo6Atq8lepyMvgL4kbjfiakVWiaMn4XFtxfC3KwLRqam7MQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

画布可视化

Basic Memory可以生成画布文件，将概念之间的关系可视化，创建交互式知识地图。用户可以要求AI创建知识可视化：

"创建一个显示我的咖啡冲泡笔记之间连接的画布。"

AI会生成.canvas文件，提供知识的视觉地图，可在Obsidian中查看。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGQu9H5a66e5vXc0xXfLS4bzmY4oPFmiaibiaRYq4ycywROMjUzpAo9q108ubNMllFALzicPukCuF0xj6Hse4b22I6w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

安装与配置

Basic Memory使用uv工具安装：

    # 使用uv安装（推荐）uv tool install basic-memory# 配置mcpServers配置"mcpServers": {  "basic-memory": {    "command": "uvx",    "args": ["basic-memory", "mcp"]  }}# 运行同步以监视文件变化uv tool run basic-memory sync --watch


与Claude Desktop集成

Basic Memory特别适合与Claude Desktop应用配合使用：

1. 编辑Claude配置文件（通常位于\`\~/Library/Application Support/Claude/claude_desktop_config.json\`）：

    {  "mcpServers": {    "basic-memory": {      "command": "uvx",      "args": [        "basic-memory",        "mcp"      ]    }  }}


2. 同步本地知识：

    # 一次性同步本地知识更新basic-memory sync# 运行实时同步进程（推荐）basic-memory sync --watch


3. 在Claude Desktop中，AI现在可以使用这些工具：

    write_note(title, content, folder, tags) - 创建或更新笔记read_note(identifier, page, page_size) - 通过标题或永久链接读取笔记build_context(url, depth, timeframe) - 通过memory://URL导航知识图谱search_notes(query, page, page_size) - 在知识库中搜索recent_activity(type, depth, timeframe) - 查找最近更新的信息canvas(nodes, edges, title, folder) - 生成知识可视化


即将推出：Basic Memory Pro

一个独立的GUI应用，提供简化的安装体验和便捷功能：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGQu9H5a66e5vXc0xXfLS4bzmY4oPFmiaibqCia03KsnLAuePqFl9OaMJXbvv2tJeiag1nGvwyJSxzib1mq6ib5IYY6KA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

* 一键安装

* 视觉化知识管理界面

* 增强的可视化工具

* 简化的多项目管理

* 优先支持

通过Basic Memory，用户可以构建一个随每次对话成长的知识库，彻底改变与AI助手交流的方式。不再丢失宝贵的对话上下文，所有知识以纯文本文件形式存储在用户的计算机上，提供完全的控制权和所有权。

无论是个人研究、团队协作还是创意项目，Basic Memory都能帮助用户构建更有连贯性、更有价值的AI辅助工作流程。

![](https://image.cubox.pro/cardImg/2anexve2dtaqgiqp65gqrqho9vwtbpv6hz4e6dr7tjl2elz4ti?imageMogr2/quality/90/ignore-error/1)

**MCP Connect**

发现MCP , 每天推荐MCP 工具

4篇原创内容

<br />

公众号  

，

![](https://image.cubox.pro/cardImg/5gx33dcazt5mpqswj8dceujrntwlf03w4qt71k7ofrgq1t6gvd?imageMogr2/quality/90/ignore-error/1)

**每天一款AI产品**

每天体验一款 AI 产品，让你的效率起飞

3篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzUxMzUzNzUzMw==&mid=2247499119&idx=1&sn=627cca378ab1db5ce9ae98688ae40704&chksm=f82682151a25879b73ca2a5bf1d5554103f2edfc52432bd69c918800f22bb6dd22838b1e34f4&mpshare=1&scene=1&srcid=0404WwTj2QuUqba8rmsZVzNE&sharer_shareinfo=02784d17fe15109856f3fddfb8169588&sharer_shareinfo_first=02784d17fe15109856f3fddfb8169588)

