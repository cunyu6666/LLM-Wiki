---
id: "7418772443059194917"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2450000939&idx=1&sn=e28cc2326731a1cbf853713245dbeca1&chksm=b097090d9fce128fbef052525cdb4b1c8bac6304883ad7bda0ba70f7ab159b0b4a4c5034e5cc&mpshare=1&scene=1&srcid=0205afkfVFKwOkyY3kry8zGw&sharer_shareinfo=6ff05ced3fd8ad2fa22ba244757652d9&sharer_shareinfo_first=6ff05ced3fd8ad2fa22ba244757652d9
author: "关注AI智能体 智猩猩AI"
collected: 2026-02-05
tags: []
---

# 斩获14.1k Star！AI智能体外挂记忆神器Beads开源，取代杂乱Markdown任务清单

# 斩获14.1k Star！AI智能体外挂记忆神器Beads开源，取代杂乱Markdown任务清单

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2450000939&idx=1&sn=e28cc2326731a1cbf853713245dbeca1&chksm=b097090d9fce128fbef052525cdb4b1c8bac6304883ad7bda0ba70f7ab159b0b4a4c5034e5cc&mpshare=1&scene=1&srcid=0205afkfVFKwOkyY3kry8zGw&sharer_shareinfo=6ff05ced3fd8ad2fa22ba244757652d9&sharer_shareinfo_first=6ff05ced3fd8ad2fa22ba244757652d9)关注AI智能体 智猩猩AI

智猩猩AI整理

编辑：没方

大家使用AI智能体时有没有这样的烦恼？昨天刚讨论完的方案，今天它却忘得一干二净。这是由于当前基于 Markdown 任务清单的智能体工作流存在根本性缺陷：

* **版本混乱** ：AI 无法区分"昨天刚决定"与"三周前的头脑风暴"；

* **缺乏关联** ：文档之间没有明确的依赖关系与优先级；

* **上下文断层** ：每次会话都需要从头重新解释项目状态；

* **更新滞后** ：手工维护的文档往往跟不上实际进展。

导致智能体给人感觉如同失忆一般，无法承接上下文，也无法自主推进复杂任务。

为此，今天要给大家介绍Steve Yegge大佬（曾任职于Geoworks、亚马逊、谷歌、Grab、Sourcegraph）的开源项目Beads------专为 AI 智能体设计的外部记忆工具。它用具备依赖感知的图结构取代传统杂乱无章的 Markdown 任务清单，提供显式依赖管理、执行任务溯源、会话状态持久化、多智能体任务隔离分配与语义化审计追踪能力。该项目在github上已收获 14.1k stars。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FDPAHibibAl3vTfFI9V78X2zqaLFnxNWCCx03ySvJ0PmiaDEoZQEsWTKgw93kwOl4IWMh2OiaRo6S1Edaiaf6J2ZTjrA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

* 项目地址：

  https://github.com/steveyegge/beads


***01***


**项目介绍**


传统 Markdown TODO 列表依赖人类的理解与上下文维护，而 Beads基于 Git 从底层重构了智能体任务管理范式，将当前工作进行结构化拆解，形成具备唯一ID、明确优先级、清晰依赖关系和完整审计日志的可寻址任务网络。Beads的核心设计包括：  

（1）依赖关系形式化

传统任务管理依赖自然语言描述，要求使用者进行语义解析与上下文推断。Beads则将依赖关系以显式、结构化的数据进行存储与查询。用户可通过 bd ready --- json 命令直接获取未被阻塞的可执行任务，无需人工解读文本。这种从"解释性 prose"到"可查询 structured data"的转变，显著降低了认知负荷，并为自动化决策提供了可靠输入。

（2）执行过程中的动态发现机制

传统方法仅将发现的新问题追加至扁平化的 TODO 列表中，导致上下文丢失。而Beads引入discovered-from 依赖类型，允许用户在创建新任务时明确其任务来源。由此构建的依赖图不仅记录任务间的逻辑关系，更映射了工作的真实演化路径，形成具有历史语义的任务网络，而非静态清单。

（3）会话持久化与上下文连续性

智能体受限于上下文窗口边界，传统工作流需要人工干预以维持任务状态连续性。Beads 基于Git持久化任务状态，使得智能体可在任意会话中通过标准查询命令（ bd ready --json）即时恢复完整工作上下文，无需依赖用户重复提供历史信息。

（4）保障多智能体协同可行性

多智能体协作时，传统Markdown列表极易引发状态冲突与重复劳动问题。Beads利用Git构建了一个共享的逻辑数据库。各智能体可实时查询任务状态（status: in_progress），并通过 --assignee 过滤器明确分工。这种基于显式状态与分配机制的协调策略，能够保障多智能体并行工作。

（5）可验证的操作审计日志

当任务状态变更时，传统 Markdown 仅能通过 git blame 查看行级文本变更，无法追溯语义化的状态流转，而Beads 会将其记录为带时间戳与操作者标识的事件日志，支持完整的语义级历史追溯。


***02***


**使用方法**


（1）安装beads

**快速脚本：**

    curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash


npm：

    npm install -g @beads/bd


Homebrew：

    brew install beads


Go：

    go install github.com/steveyegge/beads/cmd/bd@latest


系统要求：Linux、FreeBSD、macOS 或 Windows。Beads 是只需安装一次即可随处使用的 CLI 工具。无需将此仓库克隆到项目中。

（2）快速启动

    # 在项目中初始化cd your-projectbd init
    #告知智能体echo "Use 'bd' for task tracking" >> AGENTS.md


|             指令              |                  功能                  |
|-----------------------------|--------------------------------------|
| bd ready                    | 未被阻塞的可执行任务                           |
| bd create "Title" -p 0      | 创建P0优先级任务                            |
| bd dep add <child> <parent> | 关联任务 (blocks, related, parent-child) |
| bd show <id>                | 查看任务详情和审计记录                          |

Beads 支持层级 IDs ：

bd-a3f8 (Epic)

bd-a3f8.1 (Task)

bd-a3f8.1.1 (Sub-task)

隐身模式（Stealth Mode）：运行 bd init --stealth ，即可在不向主仓库提交任何文件的情况下本地使用 Beads。


***03***


**总结**


Beads通过**结构化依赖、执行**任务溯源、会话持久化、**多智能体协同机制与语义化审计追踪** ，构建了一个符合智能体认知特性的外部工作记忆系统。该系统不仅提升了任务执行效率，还**为多智能体协作提供了可靠且可扩展的工程基础设施** 。


**END**


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FDPAHibibAl3vTfFI9V78X2zqaLFnxNWCCxqncDOhngcxUUD1Fd106o7lnWYHbUwkCGOR3RGFOA3oK9FqIe86ITaA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)


**智猩猩矩阵号各专所长，点击名片关注**


![](https://image.cubox.pro/cardImg/6eskarf3wu77eddp0zyqucvvfteah9vewvomay76uvbm6qom5?imageMogr2/quality/90/ignore-error/1)

**智猩猩AI**

关注大模型驱动的AI浪潮，报道AI研究前沿与产品开发。

705篇原创内容

<br />

公众号  

，

![](https://image.cubox.pro/cardImg/22659ywrzhhsd7v1v4hthbtaeke948ckbr9w1rx2k61di2a43g?imageMogr2/quality/90/ignore-error/1)

**智猩猩具身**

关注具身智能新纪元，深究Physical AI新范式

525篇原创内容

<br />

公众号  

，

![](https://image.cubox.pro/cardImg/2kmcvtva2epu1ow1zhg7bnv2q2s9diwvaet0e89xvrzha99hhl?imageMogr2/quality/90/ignore-error/1)

**智猩猩Auto**

聚焦自动驾驶技术突破，追踪汽车智能化新进程

157篇原创内容

<br />

公众号  

，

![](https://image.cubox.pro/cardImg/45fd2y1elrs88i774b2x7o2p1vl1luabrq0gjo1ryqtcik1n6u?imageMogr2/quality/90/ignore-error/1)

**智猩猩芯算**

关注AI芯片的星辰大海，报道智算的黄金篇章

107篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MjM5ODExNDA2MA==&mid=2450000939&idx=1&sn=e28cc2326731a1cbf853713245dbeca1&chksm=b097090d9fce128fbef052525cdb4b1c8bac6304883ad7bda0ba70f7ab159b0b4a4c5034e5cc&mpshare=1&scene=1&srcid=0205afkfVFKwOkyY3kry8zGw&sharer_shareinfo=6ff05ced3fd8ad2fa22ba244757652d9&sharer_shareinfo_first=6ff05ced3fd8ad2fa22ba244757652d9)

