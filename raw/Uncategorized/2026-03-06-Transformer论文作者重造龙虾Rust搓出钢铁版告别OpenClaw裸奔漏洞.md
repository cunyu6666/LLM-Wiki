---
id: "7429510332248228882"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247872761&idx=1&sn=56933c472e903cb30cc4cefcbdf3b2fb&chksm=e9121281ed6ee07ab9b23a664fc565552c7d0705cc9fa9b1f03c2a6b9c1764f923c066a8ae7a&mpshare=1&scene=1&srcid=0306Wtw44Lu47FMMmlFp3q2B&sharer_shareinfo=b137ea0158d8cb6d8ba972c5cd75030f&sharer_shareinfo_first=b137ea0158d8cb6d8ba972c5cd75030f
author: "关注前沿科技 量子位"
collected: 2026-03-06
tags: []
---

# Transformer论文作者重造龙虾，Rust搓出钢铁版，告别OpenClaw裸奔漏洞

# Transformer论文作者重造龙虾，Rust搓出钢铁版，告别OpenClaw裸奔漏洞

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247872761&idx=1&sn=56933c472e903cb30cc4cefcbdf3b2fb&chksm=e9121281ed6ee07ab9b23a664fc565552c7d0705cc9fa9b1f03c2a6b9c1764f923c066a8ae7a&mpshare=1&scene=1&srcid=0306Wtw44Lu47FMMmlFp3q2B&sharer_shareinfo=b137ea0158d8cb6d8ba972c5cd75030f&sharer_shareinfo_first=b137ea0158d8cb6d8ba972c5cd75030f)关注前沿科技 量子位

##### 梦晨 发自 凹非寺
量子位 \| 公众号 QbitAI

有多少龙虾在互联网上裸奔？

AI智能体带着你的密码和API密钥暴露给全网。

Transformer作者Illia Polosukhin看不下去了。出手从零重构了安全版龙虾：IronClaw。

|------|------------|--------------|
| 功能   | OpenClaw   | IronClaw     |
| 核心语言 | TypeScript | Rust         |
| 凭证处理 | 直接暴露给AI智能体 | 加密存储，LLM无法访问 |
| 工具执行 | 在主环境中运行    | WASM沙箱隔离运行   |
| 部署环境 | 标准服务器      | 可信执行环境（TEE）  |
| 数据隐私 | 存在泄露风险     | 本地加密，无遥测数据   |

IronClaw目前已在GitHub上开源，提供macOS、Linux和Windows的安装包，支持本地部署，也支持通过云端托管。项目仍处于快速迭代阶段，v0.15.0版本的二进制文件已可下载。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FA6fTew8FFGHxE3VHGUs1SY0cicwYyY4ODk8x46gLSy7FOVWOav3xo5EoFAQpsaibvhSGjeuQFRXY0oaJuycY1UU1v4HSWdceSEOuYdazyfrBM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

Polosukhin（以下简称菠萝哥）还在Reddit论坛开贴回应一切，关注度颇高。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGHBwUseeTmBUfGMVZz5zcQBHQlGqkCqwaCOq0aKItRKRA2E3gmBL6czQBdMWiaicPppnpegnvtDKJOic0dSRdVySRtoOIVc14sicFE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

## OpenClaw火了，但也"着火"了

菠萝哥本人也是OpenClaw的早期使用者，并称这是他等了20年的技术。
> 它已经改变了我与计算交互的方式。

然而OpenClaw的安全状况堪称灾难，一键式远程代码执行、提示注入攻击、恶意技能窃取密码，这些漏洞在OpenClaw的生态系统中被逐一曝光。

超过25000个公开实例在没有充分安全控制的情况下暴露在互联网上，被安全专家直接称为「安全垃圾火灾（security dumpster fire）」。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FA6fTew8FFGGcncJnqTce59pASI83miaxgy2pdxMYbZ0HtcBVb9UJ7DbEaEKmr5ZzH58hAVRlKStLK2g8z0MSSsrvEbqodEWnoX6uhQXz5k94%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

问题的根源在于架构本身。

当用户将自己的邮箱Bearer Token交给OpenClaw时，会被直接送入LLM提供商的服务器。

菠萝哥在Reddit上指出这意味着什么：
> 你所有的信息，甚至包括你没有明确授权的数据，都可能被该公司的任何员工访问到。这同样适用于你雇主的数据。不是说这些公司有恶意，但现实就是用户没有真正的隐私。

他表示，再多的便利也不值得拿自己和家人的安全与隐私去冒险。

## 用Rust从零重建一切

IronClaw是用Rust语言对OpenClaw的完全重写。

Rust的内存安全特性能从根本上消除缓冲区溢出等传统漏洞，这对于需要处理私钥和用户凭证的系统至关重要。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGGhp26E8HD9DMVIiaU8vJuoEQQIcqM1fARKiaVoRahhibPicdq0CiaTouImcfgCjFXzAD2zv99jfl2FiaVtBmG3ibeZdexywMQaZYoSLg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

在安全架构上，IronClaw建立了四层纵深防御。

第一层是Rust本身提供的内存安全保证。

第二层是WASM沙箱隔离，所有第三方工具和AI生成的代码都在独立的WebAssembly容器中运行，即使某个工具是恶意的，其破坏范围也被严格限制在沙箱之内。

第三层是加密凭证保险库，所有API密钥和密码都使用AES-256-GCM加密存储，每一条凭证都绑定了策略规则，规定它只能用于特定域名。

第四层是可信执行环境（TEE），利用硬件级别的隔离保护数据，即使是云服务提供商也无法访问用户的敏感信息。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGEMRUMicnibgiaujaJPbAYpCictdzR2FFdiafKLNFB85aPzNgTibESMlWfa0FeZfL6VvpiaH81UEqt9qmcDf0SNicfJGiaKFthjGmSKROC0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

这套设计中最关键的一点是：大模型本身永远接触不到原始凭证。

只有当智能体需要与外部服务通信时，凭证才会在网络边界被注入。

菠萝哥举了一个例子，即使大模型被提示注入攻击，试图将用户的Google OAuth令牌发送给攻击者，凭证存储层也会直接拒绝这个请求，记录日志，并向用户发出警报。

然而开发者社区还是不放心，毕竟OpenClaw有2000多个公开实例被攻击，以及存在大量恶意技能，IronClaw一旦走红会不会重蹈覆辙？

菠萝哥的回应是，IronClaw的架构设计已经从根本上堵住了OpenClaw的核心漏洞。凭证始终加密存储且从不接触LLM，第三方技能无法在主机上执行脚本，只能在容器内部运行。

即便通过CLI访问，也需要用户的系统钥匙串来解密，拿到的加密密钥本身没有意义。

他同时表示，随着核心版本趋于稳定，团队计划进行红队测试和专业安全审查。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FA6fTew8FFGEJ8ToWAkm155icyTQengwJFNY5bqzg1qdC5VFRPia1s2s1mzfGrlv994p1LZ7tN6zZFZEmLd5YAZmwx3fAfrIL7CqkyYrhGhhKQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

关于提示注入这个业界公认的难题，菠萝哥给出了更详细的思路。

当前IronClaw使用启发式规则进行模式检测，未来目标是部署一个可持续更新的小型语言分类器来识别注入模式。

但他也承认，提示注入不仅可能窃取凭证，还可能直接篡改用户的代码库或通过通讯工具发送恶意消息。

应对这类攻击需要一套更智能的策略系统，能够在不查看输入内容的情况下审查智能体的行为意图，"还需要更多工作，欢迎社区贡献"。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FA6fTew8FFGHKq4KicR0j3ldGaYhKmqmSeOibCZ8icWia1KetJfKh9RibXjXHYAM580weYMcZChcwAXYicRbxHv8apMMic3aG82xcog3oBRHPgbZdcg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

有人问到本地部署和云端部署的取舍。

菠萝哥认为纯本地方案存在明显局限，设备关机时智能体就停止工作，移动端的能耗难以承受，复杂的长时间任务也无法运行。

他认为机密云（confidential cloud）是目前的最优折中方案，既能提供接近本地设备的隐私保障，又能解决「永远在线」的问题。

他还提到一个细节：用户可以设置策略，例如在跨境旅行时自动添加额外的安全屏障，防止未经授权的访问。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGFwLuuHT9Yd2KxjqkIYPKKlVeSicyh5EnBpDyKm7nMAmuYBgseTD2saJOlJictcWw9zY2l91ecwyH9X8nClONeZAlyxI7SLmoPYg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)

## 一个更大的野心

菠萝哥并非普通的开源开发者。

2017年，他作为八位共同作者之一发表了「Attention Is All You Need」，其中提出的Transformer架构奠定了当今所有大语言模型的基础。

虽然在署名中他排最后，但论文中有一条脚注写着「Equal contribution. Listing order is random.」排名纯属随机。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGGiaezFicXpyBdm35kNLnliazjsBDEKMSk2UCfiaNzrhla6VZooNZQIZ1qMv5VuTlZxXPm1RPYbxicTNfkVJeyPfF5X91suNUbFF0pc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)

但同年他从谷歌离职，创立NEAR Protocol，致力于将AI与区块链技术融合。

IronClaw背后是NEAR Protocol一个更大的战略构想：用户自有AI（User-Owned AI）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGEQ0HlY1qNeSsejNhJicA6EPA4lkLSKshN6xL4NyaAWR5o7ohRuGjlKCsNlS8Y24QbDV7TlyDWe9rQkUB8cibO3ibCBxhyHP8wvCU%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9)

在这个愿景中，用户完全掌控自己的数据和资产，AI智能体在可信环境中代替用户执行任务。

NEAR已经为此搭建了AI云平台和去中心化GPU市场等基础设施，IronClaw是这套体系的运行时层。

菠萝哥甚至开发了一个智能体互相雇佣的市场。

在NEAR的market.near.ai上，用户可以将自己专业化的智能体注册上线，随着智能体积累声誉，它将获得更多高价值的任务。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FA6fTew8FFGGicpNibpB1FQUQ0n7s5dYzkjmFt9QZb2DJcrEtxKxGsyI6mrmt7hicaXxCBMKHUOBfrfgibxGybvxgtYRY5jwWMiaVlMNcUFLxJLBI%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D10)

当被问到普通人未来五年如何适应AI时代时，菠萝哥的建议是尽快采用AI智能体的工作方式，学会将完整的工作流程交给它自动化处理。

他的这种判断并非近期才突然产生。

早在2017年创立NEAR AI时，菠萝哥就在告诉所有人"未来你只需要和计算机对话，不再需要写代码"。

当时人们觉得他们疯了，是在说胡话。

九年过去了，这件事正在变成现实。

"AI智能体是人类与线上一切交互的终极界面，"Polosukhin写道，"但让我们把它做得安全。"

GitHub地址：  
https://github.com/nearai/ironclaw

参考链接：  
\[1\]https://www.reddit.com/r/MachineLearning/comments/1rlnwsk/d_ama_secure_version_of_openclaw/


**一键三连** **「点赞」「转发」「小心心」**

**欢迎在评论区留下你的想法！**


--- **完** ---

🦞 **今天，你养虾了吗？**

欢迎加入【龙虾养成讨论组】，一起交流养虾经验！扫码添加小助手加入社群，记得备注【OPENCLAW】哦～

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FA6fTew8FFGE2A5FUdeYWwiaO8tGQZWo7TXBB1ncIzp6KiaMq8leYrBnIialOJAiblIf8S1ibygLTWelr2IQYwPnVeDSsuvA7pmVvsKdgaicZEOeYs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D11)

**一键关注 👇 点亮星标**

**科技前沿进展每日见**

![](https://image.cubox.pro/cardImg/14z8gf5kbumqt19jevpu5db2zudnou01s2jjqjv5of2bi3c0k8?imageMogr2/quality/90/ignore-error/1)

**量子位**

追踪人工智能新趋势，关注科技行业新突破

3707篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247872761&idx=1&sn=56933c472e903cb30cc4cefcbdf3b2fb&chksm=e9121281ed6ee07ab9b23a664fc565552c7d0705cc9fa9b1f03c2a6b9c1764f923c066a8ae7a&mpshare=1&scene=1&srcid=0306Wtw44Lu47FMMmlFp3q2B&sharer_shareinfo=b137ea0158d8cb6d8ba972c5cd75030f&sharer_shareinfo_first=b137ea0158d8cb6d8ba972c5cd75030f)

