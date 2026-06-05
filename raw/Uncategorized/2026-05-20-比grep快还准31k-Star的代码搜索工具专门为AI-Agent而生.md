---
id: "7456757270718711543"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzYzNjczNDI1Mw==&mid=2247484885&idx=1&sn=cb188c9089432e123fe732d6b05e3ee7&chksm=f1621f00f6f0f471f9dd23e141f293cf9d3e60e00aa07c0423a5ec254b7643c6734725318fa5&mpshare=1&scene=1&srcid=0520l3EJtOix3ePsdg3yPYbK&sharer_shareinfo=6473357670e768342a98f81706d7de10&sharer_shareinfo_first=6473357670e768342a98f81706d7de10
author: "晴天的码场 晴天的码场"
collected: 2026-05-20
tags: []
---

# 比grep快还准，3.1k Star的代码搜索工具专门为AI Agent而生

# 比grep快还准，3.1k Star的代码搜索工具专门为AI Agent而生

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYzNjczNDI1Mw==&mid=2247484885&idx=1&sn=cb188c9089432e123fe732d6b05e3ee7&chksm=f1621f00f6f0f471f9dd23e141f293cf9d3e60e00aa07c0423a5ec254b7643c6734725318fa5&mpshare=1&scene=1&srcid=0520l3EJtOix3ePsdg3yPYbK&sharer_shareinfo=6473357670e768342a98f81706d7de10&sharer_shareinfo_first=6473357670e768342a98f81706d7de10)晴天的码场 晴天的码场


<br />

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F65c9fHd9mrZPskw8ic3z1ibwK5WXa8kDfz5tzFAO01hUic5vsDFWvRaXGcljJC4UQ6ZFPWkky5gLiajkgSkgwBAMObYDF4zoG1syWicPQXKApjLw%2F640%3Fwx_fmt%3Dpng%26watermark%3D1%23imgIndex%3D0 "semble 项目 Logo")

前段时间在逛 GitHub 时发现了这个项目，发布没多久就收到了 3.1k+ ⭐，专门做给 AI 编程 Agent 用的代码搜索工具------semble。

**01**

## 它在解决什么问题

<br />

<br />

用过 Claude Code、Cursor 这类编程 Agent 的人多少都遇到过一个问题：Agent 想找某段代码，要么用 grep 搜关键词，要么直接把整个文件读进来，token 哗哗地烧。semble 要干的事就是：Agent 用自然语言问一句"这个项目怎么处理鉴权的"，semble 直接把相关代码片段精准返回，不读多余的东西。官方数据是比 grep+read 方式少用约 98% 的 token。

**02**

## 跑得有多快

<br />

<br />

semble 走的是轻量嵌入路线，全程跑在 CPU 上，不需要 API key，不依赖任何外部服务。按项目给出的数据：索引一个普通规模的代码库约 250ms，单次查询约 1.5ms。和专门做代码理解的 transformer 模型比，索引速度快约 200 倍，查询速度快约 10 倍，检索质量（NDCG@10）保持在 0.854，相当于专用模型的 99%。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F65c9fHd9mrbx0mXtOTNlvlF4CShsfCcbt0pbwg0OIianojxAEHdCBOXObLCFQgesDHLZf74ZUvFstMkJu5uJ9uIWqTodBgejl9w45iatmU6pU%2F640%3Fwx_fmt%3Dpng%26watermark%3D1%23imgIndex%3D1 "冷启动下速度与检索质量对比")

**03**

## 接入方式

<br />

<br />

两条路：MCP Server 或者 Bash/AGENTS.md。用 Claude Code 的话，一行命令搞定：

    claude mcp add semble -s user -- uvx --from "semble[mcp]" semble

Cursor、Codex、VS Code、Windsurf、Zed 等也都支持，各自往对应的配置文件里加一段 JSON 就行。子 Agent 不能直接调 MCP 工具，这种场景就用 Bash 方式，把 semble 的使用说明写进 `AGENTS.md` 或 `CLAUDE.md`，主流 Agent 都能识别。

**04**

## token 节省到底有没有那么夸张

<br />

<br />

semble 自带一个 `semble savings` 命令，会记录每次搜索节省了多少 token。计算方式是：用包含返回代码片段的文件总字符数减去实际返回的片段字符数，除以 4 估算 token 数。这是偏保守的估算，因为 Agent 探索陌生代码库时通常是整文件读入的。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F65c9fHd9mrYlFvw2ytzGBy7Rrb09cODAHp2dBahfk1zRURicJpLicKrDjVBApt29akTC8dP1qwGLbxPVUbW7LvnZ3hVC5FWQCkHPRtoExH2kU%2F640%3Fwx_fmt%3Dpng%26watermark%3D1%23imgIndex%3D2 "token 使用效率对比示意")

**05**

## CLI 直接用也行

<br />

<br />

不想走 Agent，脚本里直接调也没问题：

    # 自然语言搜索本地项目
    semble search "authentication flow" ./my-project

    # 搜远程仓库（自动 clone）
    semble search "save model to disk" https://github.com/MinishLab/model2vec

    # 找跟某行代码相似的代码
    semble find-related src/auth.py 42 ./my-project

**06**

## 适合谁用，门槛在哪

<br />

<br />

本质上是个开发者工具，目标用户是重度使用 AI 编程 Agent 的工程师。如果你的工作流里已经在用 Claude Code 或 Cursor 日常写代码，接入成本很低，一条命令或一段配置的事。如果你对 Agent 本身还不熟悉，semble 对你帮助有限。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F65c9fHd9mrYYH2LmaykO0YF9w5b24LJgJGRtFuLAkSkoLIaFwmstAr9KrPLxmMuawRcbd5bOuaOOmTwQkshn1fxf2mpU2ibsrL2qlDibWTlp4%2F640%3Fwx_fmt%3Dpng%26watermark%3D1%23imgIndex%3D3 "热启动下速度与检索质量对比")

*** ** * ** ***

<br />

觉得这个项目有意思的话，去 GitHub 给它点个 Star 支持一下。有在用 Claude Code 或 Cursor 的朋友，欢迎留言聊聊你现在的代码搜索工作流------是不是也遇到过 token 烧得莫名其妙的情况？

    # GitHub 项目地址
    https://github.com/MinishLab/semble


![](https://image.cubox.pro/cardImg/bslzex24vo6efq64hrry636cp2vis8mzuj42hfv31itn3kmkr?imageMogr2/quality/90/ignore-error/1)

**晴天的码场**

分享githubg开源工具

90篇原创内容

<br />

公众号  

，

谢谢你这么优秀还关注我✨

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzYzNjczNDI1Mw==&mid=2247484885&idx=1&sn=cb188c9089432e123fe732d6b05e3ee7&chksm=f1621f00f6f0f471f9dd23e141f293cf9d3e60e00aa07c0423a5ec254b7643c6734725318fa5&mpshare=1&scene=1&srcid=0520l3EJtOix3ePsdg3yPYbK&sharer_shareinfo=6473357670e768342a98f81706d7de10&sharer_shareinfo_first=6473357670e768342a98f81706d7de10)

