---
id: "7441009161539682651"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzU2Mjg2MzAxMA==&mid=2247490776&idx=1&sn=3b2620fccc59404cdd195dda990fd08d&chksm=fd1c1e1d6c36f0d8af388d24a7f9177f96284d85044d4262fbff3a5974b357342bff9db088d7&mpshare=1&scene=1&srcid=0407Ln6Ip748w2IFUp0caHBs&sharer_shareinfo=da6fb78fdc1d8ce7fbf64b0ef29948dc&sharer_shareinfo_first=da6fb78fdc1d8ce7fbf64b0ef29948dc
author: "井底之硅 AGI社团"
collected: 2026-04-07
tags: []
---

# 开发者怒锤Anthropic！这个2.5万星开源神器，Deep Research碾压Claude，本地部署一行命令搞定

# 开发者怒锤Anthropic！这个2.5万星开源神器，Deep Research碾压Claude，本地部署一行命令搞定

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU2Mjg2MzAxMA==&mid=2247490776&idx=1&sn=3b2620fccc59404cdd195dda990fd08d&chksm=fd1c1e1d6c36f0d8af388d24a7f9177f96284d85044d4262fbff3a5974b357342bff9db088d7&mpshare=1&scene=1&srcid=0407Ln6Ip748w2IFUp0caHBs&sharer_shareinfo=da6fb78fdc1d8ce7fbf64b0ef29948dc&sharer_shareinfo_first=da6fb78fdc1d8ce7fbf64b0ef29948dc)井底之硅 AGI社团


导读  
【导读】一个叫Onyx的开源AI平台，悄悄登上了GitHub Trending第一名。它能接入任何大模型，Deep Research基准测试以68:32的碾压比分击败Claude，还能连接50多个数据源做企业级RAG------最关键的是，完全免费，一行Docker命令就能私有部署。近7000人点赞的推文直接喊出：「Anthropic又挨了一拳！」

## 一夜霸榜GitHub，近万人围观

4月初，一条推文在开发者圈子里炸了锅。

AI博主Avi Chawla发了一条帖子，开头就是一记重拳：
>
> "Another blow to Anthropic! Devs built a free and better Claude alternative."

「对人智公司来说又是一次打击！开发者们造了一个免费且更好的Claude替代品。」


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuCMvG6U0LNj97OxAeu0w3UdHVPg9SUxtWJqfDOib2mnNAylLUaJXLjU8dZd9545yWXe4CkkRepBy0KiabKhriaXlduUUV0zmeww4w%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D0)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuDial5VocMzW81eIsN7yQicUeH8iaOtSLXopqcKnzYXlQZMDicdoicrw47LxhnkJnAiaH2cjCeusvjYxfyfh9A4ricg4rw3YT1kKLEmCk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D1)

▲ Avi Chawla的推文引爆讨论，近7000人点赞，收藏量破万

这条帖子获得了**近7000个赞、860多次转发、64万次浏览** 。评论区里，开发者们奔走相告------终于有一个能打的开源方案了。

与此同时，Onyx直接冲上了**GitHub Trending榜第一名** 。2.5万颗Star，日增近2000颗，增速堪比当年的Stable Diffusion。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuCjMPf9jWJDMaZtuZJrIrOn7c9QWWxDm4XibiamCHg9IRaPMicJ6rlPfR5ia7QqiaeUUrbWttX88qHxf8sPOcbXBJyy82W13s3S2bEs%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D2)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuBW1C1VibyvCbkKF2U3zhjPI0IMTLxVYwqtfR7iaOJicnpKn6v94Rh0TGIRQW91UjQNFIRw1NjlWTiaJ2Ac1eOeuyLOEuu1LVcCkiag%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D3)

▲ 开发者Vishnu Jangid：「SaaS正在被一个代码库吃掉」

日本开发者圈也沸腾了。推主ガガロットAI直接用了「铁槌」这个词：
>
> "【Anthropicに鉄槌】ある開発者がClaudeより優れた完全無料AI『Onyx』を発表。多分課金系のAI終わるwww"

「给Anthropic一记铁槌！一位开发者发布了比Claude更强的完全免费AI『Onyx』。付费AI可能要完蛋了哈哈哈。」


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuDpoZ4YEFCvdCrWhia9pgUpYiac5rQhdIWOniacsEr7AX4vwHTVBj3eb9ugvmwVkDoUNoItNLElR9ceoO9L4weT5X3y992icicY0Ib4%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D4)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuCN2fbaM4iatQicQpYRG9embV0btY8LVLBEmggdWReVyczYP4TyfL5TZd27SN3EpLgzpTFPDly1L7iavJo3I9BtzSNkFPibcPudwCQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D5)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuB0B3wqzyocdT8ONLwGsZaRtuSzAdpq1jSibJlQGj0KRJZAxhMGAEgicv5qlGcKIqIW7XQYJiazTPEsLGonTTPG4QRUqmzQxdZ4mE%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D6)

▲ 日本AI博主「ガガロットAI」的帖子获得近2000赞，笑称「付费AI要完蛋了」

## 它凭什么打败Claude？

说Onyx打败Claude，可不是嘴上说说。

有**真实的基准测试数据** 撑腰。

在DeepResearch Bench（深度研究基准测试）中，Onyx拿下了**所有参赛选手的第一名** 。具体比分：

* **Onyx vs Claude：68比32**
  ，Onyx胜
* **Onyx vs ChatGPT：64比36**
  ，Onyx胜
* **Onyx vs Notion AI：76比24**
  ，Onyx碾压


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuCeia4AeTVLtrlLfzG1bd1IPriaLAwnf1KgcuGRFiadELTtjcxhOdmKhbUyCbemS0bBZgevBicINUJyXrx3ooAEERicT6NQ4IoVCzR0%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D7)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuBHfBtatHg2zR4BFiaxYNKO4FyvJ3GzbYvxBgjt36Csw6LL2bhIkLb9QDbdRoDibDB24JzGYUvM3ueyJXhycbs5u2T6saYjLbTn0%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D8)

▲ Akshay展示的DeepResearch Bench数据：Onyx全面领先，Claude被打到31.9%

这个测试怎么做的？用99个真实职场问题，覆盖22万份文档，模拟企业员工日常查资料的场景。Onyx的Agentic RAG会多轮推理、交叉验证、追问补充------模拟的是一个**真人研究员的工作方式** ，而不只是"检索top-k然后生成"。

开发者Ashutosh Ajgaokar在回复中总结了核心技术栈：
>
> "Onyx is a fully open-source (MIT) AI chat + agent platform. Self-host via Docker (one-click, air-gapped capable). Plugs into any backend: Claude, GPT, Gemini, Ollama, vLLM, etc."

「Onyx是一个完全开源（MIT许可）的AI聊天+智能体平台。通过Docker一键自托管，支持物理隔离。可接入任何后端：Claude、GPT、Gemini、Ollama、vLLM等。」

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuA64EcPjhkGKhPA4bsEo03ZJbD8cHUnxfUB76QGBgnHqv5HQg5BqstvCdq23IQIQNtQSd65C7wwmy7oOv6zc50PzrH80GaN23A%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D9)

▲ 开发者Ashutosh详细拆解了Onyx的技术栈------支持物理隔离部署、在DeepResearch基准中68:32战胜Claude

## 不只是聊天框：一个全能AI操作系统

很多人第一反应：又是一个套壳ChatGPT？

不是。

Firethering说得精准：
>
> "Most LLM tools feel like demos. You ask something, get an answer, and that's about it. Onyx sits between you \& the model \& adds the stuff you end up needing anyway."

「大多数LLM工具感觉都像演示版。你问一个问题，得到一个答案，仅此而已。Onyx位于你和模型之间，补上了你迟早需要的那些功能。」


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuB80WotyOM21SWQ11RHNLicRBIotDQbfWWeicQyd9Tib4y4YatQAasXT6QibL4pdtoiaficaHnicxytdmrjQL0nxH9GRdMlvYIyBoQHso%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D10)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuBZlqiauqUsw8J4gAaEW0dBcYmqn8PgN0DJGSwIxMjcymGouxwibiaBZLaGp56BwcKtc1ibdricGruwnh4Uu4khzkEPwnRtibr60GqPg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D11)

▲ Firethering：「大多数LLM工具都像演示版，Onyx补上了你真正需要的东西」

Onyx到底能做什么？来看这张全家福：

**模型层** ：接入任何LLM------OpenAI、Claude、Gemini、Grok，或者用Ollama/vLLM跑本地模型，**数据完全不出内网** 。

**智能体层** ：自定义Agent，配置不同工具和知识库。需要快速查数据？用便宜的小模型。需要深度分析？切到GPT-5或Claude。**一个界面里灵活调度** 。

**知识层** ：连接**50多个数据源** ------Slack、Google Drive、Confluence、Jira、GitHub、Notion、Salesforce、SharePoint......不是临时调用MCP，而是**真正建了索引、持续同步、带权限管控** 。

**研究层** ：Deep Research模式，多步骤智能体工作流，自动拆解复杂问题、并行探索、交叉验证、迭代优化------生成的报告带完整引用和来源。

**工具层** ：沙盒代码执行、网页搜索、图片生成、语音对话、文件输出（Artifacts）、MCP协议扩展。

日本AI博主チャエン把它总结得最到位：
>
> "オープンソースの無料の万能AIツール。法人向けAIはこれで良い説。"

「开源免费的万能AI工具。企业AI用这个就够了。」


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuCalW8jttBN7LLD9c23p8mlUicpNrtjzwfCs1ibV3OZbqmTqcpFfL4sgOzawKV64PpV9ypct7VH16V9DR094H9Gp2nC0dfc0rEMM%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D12)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuAYMDFUuhvBVBLia66uiak5GzKC8unYC0U443Y6MTe6utkB8FwZcwdtjibuSI4Po43bCgKHUMc0gia2G9BOBbgY43vIw6RbFtfia9Kc%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D13)

▲ 日本科技CEO チャエン：「功能丰富，企业AI用这个就够了」

## 从Danswer到Onyx：YC明星团队的三年逆袭

Onyx不是凭空冒出来的。

它的前身叫**Danswer** （「deep answer」的缩写），2023年在Hacker News上以Show HN帖子首次亮相，最初只是一个帮企业用LLM搜索内部文档的工具。

两位创始人背景硬核：

**Yuhong Sun** ------机器学习和NLP专家，之前在Alation做过transformer架构的NL-to-SQL查询和混合语义搜索。这直接决定了Onyx的RAG引擎为什么比竞品强一截。

**Chris Weaver** ------曾是北美英雄联盟排名前100的玩家（没错），后来在Robinhood担任反欺诈引擎技术负责人。反欺诈系统对准确率和可审计性的极端要求，被直接移植到了Onyx的企业级功能里。

他们拿到了**Y Combinator W24** 的入场券，2025年3月又完成了**1000万美元种子轮融资** ------本来只想融300万，结果超额认购。领投的是硅谷顶级基金**Khosla Ventures和First Round Capital** ，天使投资人包括Coinbase/Pinterest董事Gokul Rajaram、Dropbox联合创始人Arash Ferdosi等。

更能说明问题的是客户名单：**Netflix把Onyx部署给了全部14000多名员工** ；法国军工巨头Thales集团（对安全性要求极高）也在用；金融科技公司Ramp报告了**30倍的ROI** 。

从一个文档搜索小工具，到GitHub 2.5万Star的全能AI平台------Danswer变成Onyx，用了不到三年。

## 开发者社区的判决：「付费AI的末日到了」

看看开发者们怎么说的。

NaveedUllah直接灵魂发问：
>
> "Open-source AI is getting dangerously good. Are you still paying for AI tools after this?"

「开源AI强得已经有点危险了。看完这个你还会继续为AI工具付费吗？」


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuBvkA73mrbicZk5vWhbMPY1YgkYMbZzCdpO9wsvyZaHEuOakodvVQBxvueVE0ibmhKCr4LCoeKu0qUNCyOdkxg1YnAAq3Op74Az4%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D14)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuBanPvN63CcW9wnMXNqiccNjAIHASglXSltCW6JBRvHmFZwtw9KBsLZVBYolbdESMn6iaZ8l9uYBcCrXRumiaJfeIia4RaPZndLgVw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D15)

▲ NaveedUllah：「开源AI强得有点危险了------你还在为AI付费吗？」

就连Grok自己也跑出来背书：
>
> "Yeah, it's true. Onyx (open-source on GitHub with 22k+ stars) is a self-hostable AI chat... tops DeepResearchBench for research... Solid free alternative to Claude."

「没错，是真的。Onyx是一个可自托管的AI聊天工具......在DeepResearchBench上名列前茅......是Claude的靠谱免费替代品。」

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuDNBSiazFibkK4vF1LwSNNxPdtBP98kpYaJ8dx9VGqbuxtd4betqkaTbzqxotomBQT9MibPqkN8ckuk72h4L5bibsOgSqCMZicHea9g%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D16)

▲ 连Grok都承认了：Onyx是Claude的「靠谱免费替代品」

Naazim Hussain写了一篇长评，说到了点子上：
>
> "Onyx treats models as interchangeable infrastructure, not products. You orchestrate models, data, and tools in one system you control."

「Onyx把模型当作可替换的基础设施，而不是产品。你在一个自己掌控的系统里编排模型、数据和工具。」


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuB1jeWrus3Rr4kpMucnYUl3fL0licY2XBic6m2E5I8HqH78f96DkYBTlw3KpWnzPxlzRwmMzuhuaMw9pWKu4riaThqgaJd6yr3Pjs%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D17)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuCQU62CfdO2MaXzXLanicJtA9MMIvKMOwy4jJZGjRkdFibheT2tsv7NIWMVV9O85jrg2iccNicR9xPIKeHYwoIbBNp4UY7o3KeaOHE%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D18)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuCfIZhYyXMFCmcH4vtfAOcnWDbz0BlUGQqrdibAjC4rXpnWFYLsbyUZefWI2sXz9ZjvdzCbjknicCsn2H5q0rT3ibYFiczRFAEbINg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D19)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FMjbGeFN4GuDicyMDOEt8kyXs9gWyTIF19mFBVVJg2icchmEMMG5oJwEMFZ0NfANNpUMsJiadnN3B9abI9b1MklqWxKpMVCKoQAKFIvXC7MwicOA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D20)![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FMjbGeFN4GuCYGqAN3q7qbggyVnJ16Ve8cFdoT2c9OsRqC2L6ZHqWpyll3l63ZsdwZlaFkh9pujgyaO2FwDRicxicZFzFXRqE4YnvlYO0WT9Fk%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D21)

▲ Naazim Hussain的长评：「Onyx把模型当基础设施，你掌控一切」

这句话道出了Onyx最核心的哲学：**模型来来去去，平台才是护城河** 。今天用Claude，明天切GPT-5，后天跑本地Llama------数据、工作流、权限体系全部不用动。

## 写在最后：当AI平台变成水电煤

2.5万Star、GitHub Trending第一、近万人点赞的推文、Netflix全员部署、DeepResearch基准碾压所有付费对手------Onyx用三年时间证明了一件事：

**最好的AI工具，不需要你为它付费。**

一行命令就能部署：

\`\`\` curl -fsSL https://onyx.app/install_onyx.sh \| bash \`\`\`

数据留在自己的服务器上，模型随便切换，连接器持续同步，智能体按需编排。

当开源社区198个贡献者、125个代码作者一起打磨一个平台的时候，任何一家闭源公司都该感到压力。

你的下一个AI助手，可能不再需要月费。

*** ** * ** ***

--- END ---

--- END ---

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU2Mjg2MzAxMA==&mid=2247490776&idx=1&sn=3b2620fccc59404cdd195dda990fd08d&chksm=fd1c1e1d6c36f0d8af388d24a7f9177f96284d85044d4262fbff3a5974b357342bff9db088d7&mpshare=1&scene=1&srcid=0407Ln6Ip748w2IFUp0caHBs&sharer_shareinfo=da6fb78fdc1d8ce7fbf64b0ef29948dc&sharer_shareinfo_first=da6fb78fdc1d8ce7fbf64b0ef29948dc)

