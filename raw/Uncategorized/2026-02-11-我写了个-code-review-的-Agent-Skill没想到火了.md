---
id: "7421285511093814725"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzU0MTU4OTU2MA==&mid=2247492512&idx=1&sn=f5fd3063f889fb162e42dedfd36c49b0&chksm=fa7c839b72a5e3ffe9b6083339bf5be780b0850273f2365309fc4653d866190b846cb565808a&mpshare=1&scene=1&srcid=0211zydzuH8jdsdH0xISTHmq&sharer_shareinfo=0f8231f07790e77512597f6bf22fc37b&sharer_shareinfo_first=0f8231f07790e77512597f6bf22fc37b
author: "三元同学 三元同学"
collected: 2026-02-11
tags: []
---

# 我写了个 code-review 的 Agent Skill，没想到火了

# 我写了个 code-review 的 Agent Skill，没想到火了

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0MTU4OTU2MA==&mid=2247492512&idx=1&sn=f5fd3063f889fb162e42dedfd36c49b0&chksm=fa7c839b72a5e3ffe9b6083339bf5be780b0850273f2365309fc4653d866190b846cb565808a&mpshare=1&scene=1&srcid=0211zydzuH8jdsdH0xISTHmq&sharer_shareinfo=0f8231f07790e77512597f6bf22fc37b&sharer_shareinfo_first=0f8231f07790e77512597f6bf22fc37b)三元同学 三元同学


前两天随手写了个 Agent Skill，专门做 Code Review 的，发了条推之后就没太在意。

结果第二天醒来一看，GitHub Star 刷刷往上涨，阅读量涨到了大几万，不少人也开始转发了，说效果奇好。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FnGvBg4GicsuntFQyLqId3I0DhiaAhQZtzTbTIRD6bnll97yfrVquAyAJKvTHcNbpEiby7g02KyibPAHb7KXTld73Vhk1a0rbtLED0jibMJmLqU8M%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

这个的确让我有点意外。

倒不是说这个 Skill 有多了不起，而是它戳中了一个很真实的痛点------**大部分团队的 Code Review，要么走过场，要么全靠人肉。**

## 先说说为什么要做这个

做这个 Skill 的起因其实很简单。

我自己平时写代码，改完了之后经常想让 Claude Code 帮我 review 一下。直接跟它说"帮我看看代码有没有问题"，它确实会给你一些反馈，但说实话，质量参差不齐。

这就跟新来的实习生做 Code Review 一样，不是他不想认真看，是他不知道该看什么、怎么看、按什么优先级来。

**所以问题的本质是：模型需要一套结构化的 Review 框架，告诉它该检查什么、怎么分级、用什么格式输出。**

这件事用 Skill 干非常合适。

## code-review-expert 是什么

一句话概括：**一个让 AI 用资深工程师的视角帮你做 Code Review 的 Skill。**

安装方式就一行：

    npx skills add sanyuan0704/code-review-expert

装好之后在 Claude Code 里输入 /code-review-expert，它就会自动 review 你当前的 git changes。

整个 review 流程我是精心设计过的，分成这么几步：

**第一步：Preflight（了解改动范围）**

它会先跑 git diff 看看你改了哪些文件、改了多少行。如果改动量超过 500 行，它会先按模块分批 review，不会一口气全看完然后给你一堆乱七八糟的反馈。

**第二步：SOLID + 架构检查**

这一步是我花了最多时间打磨的。我写了一份详细的 SOLID checklist，把每个原则对应的"坏味道"都列出来了。SOLID 是软件设计领域里面非常著名的一个优雅编程的规则，具体就不展开了。

**第三步：发现可以删掉的代码**

这步非常非常重要。很多项目里都有一堆死代码------feature flag 关掉的、被废弃的 API、没人用的工具函数。它会帮你找出来，然后提示你删除这些死代码。

**第四步：安全扫描**

XSS、SQL 注入、SSRF、路径穿越、竞态条件、密钥泄露......这些它都会检查。

其中竞态条件（Race Condition）这块我写的特别详细，因为这是很多人在 review 时最容易忽略的。它会专门去找并发数据库访问这些容易出问题的场景。

**第五步：代码质量扫描**

错误处理有没有吞掉异常？有没有数据库的 N+1 查询？空值检查到不到位？这些"小问题"在生产环境里都可能变成大事故或者性能问题。

**最后：结构化输出 + 确认**

所有发现按严重程度分成四个等级：

| 等级 | 含义 |         怎么处理          |
|----|----|-----------------------|
| P0 | 严重 | 必须 block merge        |
| P1 | 高危 | 应该在合并前修复              |
| P2 | 中等 | 这个 PR 修或者建个 follow-up |
| P3 | 低优 | 可选优化                  |


输出之后，它不会自作主张去改代码。而是先问你：要修全部，还是只修 P0/P1，或者修指定的。

**这个"先 review 再确认"的设计是我特意做的** ------Code Review 的价值不只是发现问题，更重要的是让你理解问题。如果 AI 直接帮你改了，你连有什么问题都不知道，那这个 review 就没意义了。

## 为什么我觉得它火了

评论区和私信里，大家反馈最多的是一点是：

**"跟以前不加 skill 的效果有天壤之别"。**

**![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FnGvBg4Gicsun3Ncva76pfibRAflRwqXMDnGsWjw548mlSibcAhuicuRbYW5XZ6TWzNWicpHyOyOpAjSgIKTXAbLPTun2PSnqyxoTmFYKkNesRqWg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)**

这要归功于那几份 checklist。我把 security-checklist、solid-checklist、code-quality-checklist 都放在了 references/ 目录下，每份都是实打实的检查清单，不是那种"注意安全问题"之类的废话。

比如安全检查那份，光竞态条件就列了四个子类：共享状态访问、TOCTOU（检查后使用）、数据库并发、分布式系统。每个子类下面都有具体的代码模式和需要问的问题。

这就是 Skill 的魅力------**你把专业知识结构化地喂给模型，它的输出质量会有质的提升。**

## 怎么做到的？聊聊 Skill 的设计思路

这个 Skill 的结构很简单：

    code-review-expert/
    ├── SKILL.md                  # 主文件，定义整个 review 流程
    ├── agents/
    │   └── agent.yaml            # Agent 配置
    └── references/
        ├── solid-checklist.md    # SOLID 原则检查清单
        ├── security-checklist.md # 安全检查清单
        ├── code-quality-checklist.md # 代码质量检查清单
        └── removal-plan.md       # 代码清理计划模板

核心设计有几个关键点：

### 1. references 实现按需加载

这是 Skill 体系最优雅的地方。

四份 checklist 的内容加起来好几千字，如果全塞进 SKILL.md，一上来就会吃掉大量上下文窗口。所以我把它们放在 references/ 里，SKILL.md 里只在需要的步骤写 Load references/xxx.md。

模型执行到那个步骤时才会去读对应的文件，用完就可以"忘掉"了。这就是 Skill 的 **Progressive Disclosure** （渐进式加载特性），是 Skills 最精妙的设计之一。

### 2. Workflow 要设计得有节奏感

我试过把所有检查点平铺在一起，效果很差------模型会东一榔头西一棒子，安全问题和命名规范混在一起说。

最后我按照真实的 Code Review 流程来编排：先看改动范围，再看架构设计，然后看安全，最后看代码质量。每一步之间是递进关系，从宏观到微观。

这个设计借鉴了人来做 Code Review 的习惯------好的 reviewer 不会上来就抠细节，而是先理解整体改动的意图和影响范围。

## 写在最后

你猜我写这个 skill 花了多久？

3,2,1,揭晓答案。

我只花了 10 分钟。不可思议吧。

怎么做到的？现在 claude 官方有一个叫 skill-creator 的 skill，帮你来写 skill，然后基于它可以很快搭出骨架来。后续，就是基于我的专业经验，引导 agent 帮我把一些关键的原则拆分为各个 checklist 文档，聊个几轮，这个高质量的 skill 就完工了。

回头看这件事，我觉得这也是 Skills 生态最让人兴奋的地方：**每个有专业积累的开发者，都可以很快把自己的经验沉淀成一个 Skill，让 AI 帮更多人受益。**

你不需要会写 MCP Server，不需要懂协议，不需要搞 OAuth 鉴权。就是一个 Markdown 文件 + 几份参考文档，仅此而已。

仓库在这里，欢迎 Star 和提 PR：
> **GitHub** : sanyuan0704/code-review-expert
>
> 安装：npx skills add sanyuan0704/code-review-expert

如果你也在做 Skill 开发，或者有什么好用的 Skill 推荐，评论区欢迎来聊。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0MTU4OTU2MA==&mid=2247492512&idx=1&sn=f5fd3063f889fb162e42dedfd36c49b0&chksm=fa7c839b72a5e3ffe9b6083339bf5be780b0850273f2365309fc4653d866190b846cb565808a&mpshare=1&scene=1&srcid=0211zydzuH8jdsdH0xISTHmq&sharer_shareinfo=0f8231f07790e77512597f6bf22fc37b&sharer_shareinfo_first=0f8231f07790e77512597f6bf22fc37b)

