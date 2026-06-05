---
id: "7444626330030704078"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA==&mid=2247484448&idx=1&sn=7253e2da3b940d57ff98124667fd5546&chksm=f115d1b496dcec7ed8151181bba15578290d6b87b755b05f7b45df45af45ceb78750d98ae819&mpshare=1&scene=1&srcid=0417r1mIgrOZdOQOEgmlHUtm&sharer_shareinfo=394ed6e79a0378fa722545774164756a&sharer_shareinfo_first=394ed6e79a0378fa722545774164756a
author: "Koding 歪脖抠腚"
collected: 2026-04-17
tags: []
---

# 60+ 项目挤进同一赛道：AI 编程的下一个战场不是 Agent，是管 Agent 的人

# 60+ 项目挤进同一赛道：AI 编程的下一个战场不是 Agent，是管 Agent 的人

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA==&mid=2247484448&idx=1&sn=7253e2da3b940d57ff98124667fd5546&chksm=f115d1b496dcec7ed8151181bba15578290d6b87b755b05f7b45df45af45ceb78750d98ae819&mpshare=1&scene=1&srcid=0417r1mIgrOZdOQOEgmlHUtm&sharer_shareinfo=394ed6e79a0378fa722545774164756a&sharer_shareinfo_first=394ed6e79a0378fa722545774164756a)Koding 歪脖抠腚

## TL;DR

2025 年下半年到 2026 年初，一种新的产品形态在开发者工具领域集中爆发------**Agent Orchestrator** （编排器）。这类产品的核心交互模式是：左栏管理 repo/worktree/session，中间承载 AI Agent（终端或封装界面），右侧展示文件树、diff、commit 等。代表产品包括 Conductor、Orca、Superset、cmux、Superconductor 等。

这不是一个偶然的 UI 趋势，而是 AI 编程从"人机对话"范式进入"人管理 Agent 团队"范式的必然产物。当开发者从一次跑一个 Claude Code，进化到同时跑 5-10 个 Agent 并行处理不同 feature 时，原有的终端、IDE、Git 工作流全部断裂，需要一个新的控制面。

|          维度          |                          关键信息                           |
|----------------------|---------------------------------------------------------|
| 赛道定义                 | AI Coding Agent 的并行编排与管理界面                              |
| 爆发时间                 | 2025Q3 --- 2026Q1，awesome-agent-orchestrators 收录 60+ 项目 |
| 头部融资                 | Conductor $22M Series A（Spark + Matrix），YC S24          |
| 核心技术                 | Git worktree 隔离 + 终端复用 + Agent 生命周期管理                   |
| 商业模式                 | 本地免费/付费桌面应用 或 云端 SaaS（按席位/计算收费）                         |
| 与 CC/Codex/Cursor 关系 | 互补层------不替代 Agent，而是做 Agent 的"工头"                      |

*** ** * ** ***

## 一、这类产品到底在解决什么问题

### 1.1 从 Conductor 到 Orchestrator 的范式跃迁

Addy Osmani（Google Chrome 团队）在 O'Reilly AI CodeCon 上用了一个精准的类比：过去你是**指挥家（Conductor）** ，一对一地引导一个 AI 演奏者；现在你是**编排者（Orchestrator）** ，管理一整支交响乐团的异步协作。

这个转变的底层逻辑是三重天花板的同时到来：

**上下文窗口瓶颈** 。单个 Agent 的 context window 再大也有极限。一个大型项目塞进去，关键细节会被挤出去。分拆成多个专注型 Agent，每个只看自己负责的文件范围，质量反而更高。

**串行等待的时间浪费** 。Claude Code 跑一个 feature 平均 3-8 分钟。如果你有 10 个 feature 要做，串行跑就是 30-80 分钟的等待。并行跑 10 个 Agent，理论上压缩到一次等待的时间。这正是 Conductor 官网 slogan "Run a team of coding agents" 的含义------把开发者从 Agent 的等待循环中解放出来。

**隔离性缺失** 。多个 Agent 共享同一个工作目录会互相踩踏文件。Git worktree 提供了操作系统级别的目录隔离------每个 Agent 拥有独立的工作树、独立的分支，互不干扰，最后通过 PR merge 回主线。这是整个赛道的技术基石。

### 1.2 产品形态的收敛

尽管 awesome-agent-orchestrators 列表上有 60+ 个项目，但交互模式高度收敛：

**三栏布局** 成为事实标准。左栏是 session/worktree 列表（类似聊天应用的会话列表），中栏是 Agent 运行界面（终端或封装的 chat UI），右栏是 diff viewer / file tree / PR 状态。这套布局不是谁抄谁，而是"管理多个并行 Agent"这个任务的自然形态------你需要快速切换、需要看到每个 Agent 的状态、需要审查它的产出。

**Git worktree 是基础设施** 。几乎所有产品都把 worktree 管理做成了一等公民。用户创建一个新任务时，工具自动 git worktree add 一个隔离目录，Agent 在里面工作，完成后用户审查 diff、commit、push、创建 PR。这套流程已经标准化。

**Agent-agnostic 设计** 。没有产品绑定单一 Agent。Claude Code、Codex、Gemini CLI、OpenCode、Amp、Kiro......任何 CLI Agent 都能接入。产品竞争的不是"谁的 Agent 更好"，而是"谁的管理体验更好"。

*** ** * ** ***

## 二、头部产品横评

### 2.1 Conductor --- 赛道定义者


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTa2h2oOxYtLw9IfrvTDxhc0ewAsrsSXa0yPiaR2hFSqxJnYEG3gNNdu0KeNv1k9B5fzkH2y8xvmup0KLyuImvvBWCmMFeG5JmPLLOyicZ9Fx8%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

| 属性 |                                 详情                                  |
|----|---------------------------------------------------------------------|
| 团队 | Melty Labs（Charlie Holtz, Jackson de Campos），YC S24                 |
| 融资 | $22M Series A（2026.3），Spark Capital + Matrix 领投，Notion/Linear 创始人参投 |
| 形态 | macOS 原生桌面应用                                                        |
| 定价 | 免费下载，未公开付费计划                                                        |
| 用户 | Google、Meta、Hubspot、Ramp、Datadog、Spotify、Amazon 等"数十名工程师在用"         |

Conductor 是这个赛道的标杆。2024 年夏天上线，2026 年 1 月以来用户增长 10 倍。Charlie Holtz 在 Agents Hour 播客中明确了定位：不做 Agent，做 Agent 的人机界面。核心功能是一键克隆 repo 到隔离 worktree、启动 Claude Code 或 Codex 实例、实时看状态、审查 diff、merge 回主线。

Conductor 的战略愿景不止于桌面工具。Series A 公告中明确提到"从 MacBook 上的小型 AI 团队，进化为管理大型 AI 组织的平台，覆盖手机到 VPC"。这意味着它的目标是成为 AI 软件工厂的控制台，而不只是一个 tmux 替代品。

集成 Linear 做任务派发是一个差异化点------直接从 issue tracker 拉任务、自动分配给 Agent，完成后关联 PR，形成从需求到交付的闭环。

### 2.2 Orca --- 跨平台 + 浏览器集成


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTa2h2oOxYtJeVgXXSYrSjBSoVia8iaWc5AliaGCUibbibvIsbUTRjY45rfhmlnuWicBftxicHCE80xugJdUOtvAXuGa3DL2SiaQTM2TdsDE3nplVicHM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

| 属性  |              详情               |
|-----|-------------------------------|
| 团队  | Stably AI                     |
| 形态  | 桌面应用（macOS / Windows / Linux） |
| 定价  | 免费，无需登录，自带 Agent 订阅           |
| 差异化 | 跨平台、内置浏览器、Design Mode         |

Orca 是少数支持三大操作系统的产品。它的独特功能是 **Per Worktree Browser + Design Mode** ：每个 worktree 内置浏览器预览应用，切换到 Design Mode 后点击任意 UI 元素可以直接作为上下文发送给 Agent 对话。这把前端开发的"看效果 → 描述修改"循环从截图 + 复制选择器简化成了"点一下就说"。

另一个实用功能是 **Hot Swap Codex Accounts** ------如果你有多个 Codex 账号（为了拿更多 token 额度），Orca 支持一键切换，不需要重新登录或改配置文件。

Orca 还提供了 CLI 工具，让 Agent 反向控制 IDE------比如 Agent 可以通过命令行给 worktree 添加进度 checkpoint、创建新 worktree。这是一个有趣的方向：不只是人管理 Agent，Agent 也能管理自己的工作环境。

### 2.3 Superset --- 开源 + 代码编辑器定位


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTa2h2oOxYtLKoAe7buufRLic6rxzdN1icic30VyraF7VibGCwyNQ8eO08pLZsxK9bhZ0WD4hicv9zgIEWzdjytMqltWQkj7iaVEwia0fM0D8iarCl1Y%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

| 属性  |                     详情                      |
|-----|---------------------------------------------|
| 仓库  | github.com/superset-sh/superset             |
| 形态  | macOS 桌面应用（Bun + Electron/Tauri 技术栈）        |
| 许可  | Elastic License 2.0（Source Available，非 OSS） |
| 差异化 | 内置编辑器、Workspace Presets                     |

Superset 把自己定位为"AI Agent 时代的代码编辑器"而不仅仅是终端管理器。它内置了 diff viewer 和简易编辑器，支持 one-click handoff 到外部 IDE。Workspace Presets 功能允许为每个 repo 预设环境初始化脚本（安装依赖、拷贝 .env 等），新建 worktree 时自动执行，减少手动配置。

技术栈上使用 Mastra 框架，代码开源但采用 ELv2 许可------这意味着竞争对手不能直接拿它做 SaaS，但个人和企业可以自行部署。

### 2.4 cmux --- 终端原教旨主义


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FTa2h2oOxYtLRfdZuLiaw2l2hKsoImJJxdiaf7JQRgibdaKULPImRwoGHhyviafaLOFqgibgdS0VfnsguNLF0zUUgLrtnoQd8odym5gIzwuLGjiaqI%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

| 属性  |                   详情                    |
|-----|-----------------------------------------|
| 团队  | Manaflow AI，YC 孵化                       |
| 仓库  | github.com/manaflow-ai/cmux             |
| 形态  | macOS 原生应用（Swift + AppKit + libghostty） |
| 许可  | GPL-3.0（开源），商业许可另谈                      |
| 差异化 | Ghostty 渲染、极致性能、不做编排只做基础设施              |

cmux 的哲学截然不同。创始人在 README 中写道："cmux 是原语（primitive），不是方案（solution）。给一百万开发者可组合的原语，他们会比任何产品团队更快地找到最高效的工作流。"

它不自动管理 worktree，不做任务分配，不做 Agent 生命周期管理。它做的是：一个极快的终端（基于 Ghostty 的 libghostty，GPU 加速渲染），加上垂直标签页侧栏（显示 git branch、PR 状态、监听端口、最新通知），加上蓝色圆环通知（Agent 等待输入时高亮），加上内置可脚本化浏览器。

cmux 的竞争力在性能。纯 Swift + AppKit 构建，不走 Electron/Tauri，启动快、内存低。它还天然兼容 Ghostty 配置（字体、主题、颜色），对 Ghostty 用户零迁移成本。

Claude Code Teams 集成是一个亮点------cmux claude-teams 一条命令启动 Claude Code 的 teammate 模式，队友自动在原生分屏中展示，带侧栏元数据和通知，不需要 tmux。

### 2.5 Superconductor --- Rust 性能极客


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FTa2h2oOxYtKkDERjw4Ssic7IkwShQDLktcqjLJ0GQrPrqymRrjuCNFqjFUl1JIYic0JM93Wvicicr6A4Zeg68yfFu1gFuaibq7pzNIUqoNrO5S0I%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

| 属性  |                  详情                  |
|-----|--------------------------------------|
| 官网  | super.engineering                    |
| 形态  | macOS 原生应用（100% Rust + Metal GPU 渲染） |
| 定价  | Alpha 阶段免费                           |
| 差异化 | 极致性能、无限并行 Tab、Rich Text Chat 视图      |

Superconductor 选择了纯 Rust 技术路线，用 Metal API 做 GPU 加速终端渲染，启动时间 \< 50ms。它的核心卖点是"Web 技术栈的编排器通常 5-7 个 Agent 就是瓶颈，我们原生架构可以无限并行"。

交互设计上的独特点：同一个 Agent 会话可以在 **Raw Terminal** 和 **Rich Text Chat** 两种视图间自由切换------需要看原始输出时用终端模式，想要清晰对话体验时用 Chat 模式。另外支持 Picture-in-Picture 浮窗，可以把任意一个 Agent Tab 弹出为独立窗口钉在屏幕上。

目前处于 Alpha 阶段，只支持 macOS，Windows/Linux 计划中。

### 2.6 Superconductor（superconductor.com）--- 云端 SaaS 路线

注意：与 super.engineering 的 Superconductor 同名但不是同一个产品。superconductor.com 走的是**云端 SaaS** 路线，每个 Agent 运行在云端隔离容器中，提供 live browser preview，支持移动端访问和 Slack 集成。

| 属性  |                       详情                        |
|-----|-------------------------------------------------|
| 官网  | superconductor.com                              |
| 形态  | Web + iOS 应用                                    |
| 差异化 | 云端运行、Live Preview、团队协作、Slack 集成、Agent Benchmark |

它的杀手功能是 **Agent Benchmark** ：用你自己 codebase 的真实 PR 作为基准，对比不同 Agent（Claude Code / Codex / Amp / Gemini）在质量、成本、速度上的表现。这在选型阶段非常实用。

另一个设计选择是"同一个 ticket 启动多个 Agent，各自独立实现，然后对比 live preview 选最好的那个"。这本质上是用并行冗余来对冲 Agent 的非确定性------Claude Code 有一半概率跑偏，那就同时启动 3 个，挑最好的。

*** ** * ** ***

## 三、为什么是现在爆发

### 3.1 供给侧：CLI Agent 的成熟

2025 年是 CLI Agent 的元年。Claude Code（2025.2 公开 beta）、Codex CLI（2025.5）、Gemini CLI（2025.6）相继上线，加上 OpenCode、Aider、Amp 等开源方案。这些 Agent 有一个共同特征：它们是 **CLI-first** 的，跑在终端里，通过 stdin/stdout 交互。

这意味着它们天然可以被外部程序管理------spawn 一个子进程、监控输出、在需要时注入输入。这是 Conductor 类产品能够存在的技术前提。如果 Agent 都封装在 IDE 内部（像 Cursor 的 Agent Mode），外部工具就很难接管。

### 3.2 需求侧：并行开发成为刚需

Claude Max 的 $200/月订阅给了用户几乎无限的 Agent 调用额度。当调用不再是瓶颈时，瓶颈就变成了"我一次只能盯一个 Agent"。开发者开始在 tmux 里开 5 个窗口各跑一个 Claude Code，但手动管理 worktree 切换、diff 审查、PR 创建的体验极差。

Conductor 的 Series A 公告中引用了一位工程师的话："我的大量工作现在都是极度并行化的，这是我之前从没有过的。已经很久没有一个开发工具改变了我的生活。" 这不是营销话术，而是真实的工作流变化。

### 3.3 技术侧：Git Worktree 终于找到了 killer use case

Git worktree 这个特性存在了近十年，一直不温不火。绝大多数开发者用 branch 就够了，worktree 的"同一个 repo 多个工作目录"听起来有用但找不到痛点。

AI Agent 并行编码改变了这一切。当你需要 10 个 Agent 同时在同一个 repo 上工作时，branch 切换已经不够------你需要物理隔离的目录。Worktree 从一个晦涩的 Git 特性变成了整个 Agent 编排赛道的基础设施。

### 3.4 生态侧：YC 和 VC 的催化

Conductor（YC S24）、Manaflow/cmux（YC 孵化）、Orca 等多个产品都有加速器背景。Conductor 的 $22M Series A 由 Spark Capital 和 Matrix 领投，Notion 和 Linear 创始人参投------这些投资人的投资逻辑是一致的：AI 不会让开发者消失，但会彻底改变开发者的工具链。Agent 编排器就是新工具链中必不可少的一环。

awesome-agent-orchestrators 列表在短短几个月内膨胀到 60+ 项目，其中不乏 claude-squad、amux、dmux、grove 等 solo developer 的周末项目。这说明需求是真实存在的------写一个比 tmux 好用的 Agent 管理器，是每个重度 Claude Code 用户的冲动。

*** ** * ** ***

## 四、商业模式分析

### 4.1 本地桌面应用 --- 工具收费

Conductor 目前免费下载，但 $22M 的融资暗示了未来的付费路径。参考 Cursor 的模式（免费 tier + $20/月 Pro），Conductor 很可能走相似的路：基础功能免费，高级功能（更多并行 Agent、团队协作、企业 SSO、审计日志）收费。

这个模式的挑战在于：产品本身不提供 AI 能力，用户自带 Agent 订阅。Conductor 能收费的部分只有编排体验------UI、worktree 管理、通知系统、Linear/GitHub 集成。这类"瘦层"工具的付费意愿历史上不高（参考 tmux vs iTerm2），但 Conductor 的赌注是"AI Agent 团队管理"是一个比终端管理复杂得多的任务，值得付费。

### 4.2 云端 SaaS --- 平台收费

superconductor.com 走的是另一条路：Agent 跑在云端，按席位或计算资源收费。这个模式的优势是用户不需要本地算力，手机上也能操作；劣势是安全顾虑------企业代码上云是一个大门槛。

它的增值空间更大：云端环境的 live preview、网络沙箱、团队协作、Slack 集成、Agent benchmark------每一个都是可以单独收费的 feature。

### 4.3 开源 + 商业许可

cmux（GPL-3.0）和 Superset（ELv2）走开源路线。cmux 提供 "Founder's Edition" 付费版本，包含优先功能请求、iOS 同步、Cloud VM 等早期访问权。这是经典的 open core 模式。

### 4.4 共同的商业逻辑

不管哪种模式，底层逻辑是相同的：**Agent 的使用量正在指数增长，而管理 Agent 的界面是一个卡点。** 谁能成为 Agent 时代的"IDE"，谁就能收取 Agent 时代的"开发工具税"。Conductor 的野心是从桌面工具进化为"AI 组织的管理平台"，这个定位如果成立，天花板远高于一个终端管理器。

*** ** * ** ***

## 五、与 Claude Code / Codex / Cursor 的关系

### 5.1 互补关系，不是竞争

这一点需要非常明确：Conductor 类产品**不替代** Claude Code、Codex 或 Cursor。它们之间的关系类似于 Kubernetes 和 Docker------Kubernetes 不运行容器，它编排容器。Conductor 不写代码，它编排写代码的 Agent。

    ┌─────────────────────────────────────────────┐│            Conductor / Orca / cmux           │  ← 编排层│    (worktree 管理, 状态监控, diff 审查)        │├──────────┬──────────┬──────────┬────────────┤│ Claude   │ Codex    │ Gemini   │ OpenCode   │  ← Agent 层│ Code     │ CLI      │ CLI      │            │├──────────┴──────────┴──────────┴────────────┤│              Git Worktree                    │  ← 隔离层├─────────────────────────────────────────────┤│              本地 / 云端 Codebase             │  ← 代码层└─────────────────────────────────────────────┘


### 5.2 与 Claude Code 的关系最密切

Claude Code 是这个赛道最大的受益者和推动者。几乎所有编排器都把 Claude Code 列为首要支持的 Agent。原因有三：Claude Code 是 CLI-native 的（容易被管理）；Anthropic 的 Max 订阅提供了充足的配额（支撑并行）；Claude Code 本身支持 subagent 和 Agent Teams（有天然的多 Agent 基因）。

值得注意的是，Claude Code 自己的 Agent Teams 功能（CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1）与 Conductor 类产品有功能重叠。Agent Teams 提供了 shared task list、peer messaging、自动依赖解锁------这些是"内建编排"。Conductor 提供的是"外部编排"------多个独立的 Claude Code 实例在 worktree 中并行。

两者的适用场景不同：Agent Teams 适合一个 feature 内部的子任务分解（数据层 + 业务层 + API 层并行），Conductor 适合多个 feature 的并行（feature A + feature B + feature C 同时推进）。在实际使用中，可以在 Conductor 的每个 worktree 里各跑一个 Claude Code Agent Teams------编排套编排，并行套并行。

### 5.3 与 Codex 的关系

OpenAI Codex 本身就是云端沙箱执行，每个任务有独立环境。从这个角度看，Codex 和 Conductor 类产品有一定的功能重叠------Codex 自己就能并行跑多个任务。但 Codex 不能跑 Claude Code，不能跑 Gemini CLI。Conductor 的价值在于 Agent-agnostic：你可以在一个界面里同时跑 Codex 和 Claude Code，对比两者的产出，选更好的那个。

### 5.4 与 Cursor 的关系

Cursor 是 IDE-first 的产品，AI 能力嵌入编辑器。Conductor 类产品是 Agent-first 的，编辑器是可选的附件。两者服务的工作模式不同：Cursor 适合"人主导、AI 辅助"的精细编码，Conductor 适合"人规划、Agent 执行"的批量推进。

一个典型的工作流是：用 Conductor 并行跑 5 个 Agent 做粗活（新 feature、重构、bug fix），Agent 完成后在 Cursor 里做精细审查和微调。两者互补而非替代。

*** ** * ** ***

## 六、产品矩阵速览

|                   产品                    |   形态    |     技术栈      |       平台        |   开源    | 云端  |                 特色                  |
|-----------------------------------------|---------|--------------|-----------------|---------|-----|-------------------------------------|
| **Conductor**                           | 桌面应用    | ---          | macOS           | ✗       | 计划中 | YC S24, $22M A轮, Linear 集成          |
| **Orca**                                | 桌面应用    | ---          | macOS/Win/Linux | 部分      | ✗   | 内置浏览器 Design Mode, 跨平台              |
| **Superset**                            | 桌面应用    | Bun/Mastra   | macOS           | ELv2    | ✗   | 内置编辑器, Workspace Presets            |
| **cmux**                                | 终端应用    | Swift/AppKit | macOS           | GPL-3.0 | ✗   | Ghostty 渲染, 极致性能, 哲学纯粹              |
| **Superconductor** (super.engineering)  | 桌面应用    | Rust/Metal   | macOS           | ✗       | ✗   | 100% Rust, GPU 渲染, \<50ms 启动        |
| **Superconductor** (superconductor.com) | Web+iOS | ---          | 全平台             | ✗       | ✓   | 云端执行, Live Preview, Agent Benchmark |
| **claude-squad**                        | TUI     | ---          | 全平台             | ✓       | ✗   | 轻量终端管理器                             |
| **Grove**                               | TUI     | ---          | 全平台             | ✓       | ✗   | 社区项目, 并行 worktree                   |
| **Ralph TUI**                           | TUI     | ---          | 全平台             | ✓       | ✗   | 自动循环执行, 任务列表驱动                      |

*** ** * ** ***

## 七、趋势判断

### 7.1 赛道会快速整合

60+ 个项目是典型的早期爆发形态。大部分 solo project 会在 6-12 个月内停止维护。最终存活的可能是 3-5 个产品，分别占据不同生态位：一个商业化桌面应用（Conductor 领先）、一个开源终端方案（cmux 有优势）、一个云端 SaaS（superconductor.com 或类似产品）。

### 7.2 Agent 厂商会内建编排能力

Claude Code 的 Agent Teams 是一个信号------Anthropic 在自己做编排。如果 Claude Code 把并行 worktree 管理、状态监控、diff 审查全部内建，Conductor 的差异化空间会被压缩。但 Conductor 的 Agent-agnostic 属性是护城河：只要市场上有 2 个以上主流 Agent，就需要一个跨 Agent 的管理层。

### 7.3 从本地到云端是必然方向

Conductor 的 Series A 公告已经暗示了这一点。本地桌面应用有硬件限制（MacBook 同时跑 10 个 Agent 会吃满 CPU/内存），云端执行可以突破这个天花板。superconductor.com 的"手机上也能操作 Agent"是一个引人注目的方向------当 Agent 可以自主运行 30 分钟完成一个 feature 时，你不需要一直盯着终端，用手机偶尔看一眼进度就够了。

### 7.4 编排器会向上吃掉项目管理

现在的编排器管理的是"Agent 会话"。下一步是管理"项目进度"------从 Linear/Jira 拉 sprint backlog，自动分配给 Agent 团队，跑完自动提 PR，人类只做 code review。Conductor 集成 Linear 已经迈出了第一步。当这套流程跑通，编排器就从"开发工具"升级为"AI 软件工厂的控制台"。

这个方向的终局是：产品经理在 Linear 里写 ticket，编排器自动派发给 Agent 集群，Agent 交付代码 + 测试 + PR，人类工程师做最后的 review 和 merge。工程师的角色从"写代码"变成"管 Agent + 审 PR"。这不是科幻------有 YC 创业公司已经声称 100% 的代码都在 Conductor 里由 Agent 完成。

*** ** * ** ***

### References

[1] Conductor 官网:*https://conductor.build/*   
[2]Conductor Series A 公告:*https://www.conductor.build/blog/series-a*   
[3]Conductor 文档:*https://docs.conductor.build/*   
[4]Orca GitHub:*https://github.com/stablyai/orca*   
[5]Orca 官网:*https://orcabuild.ai/*   
[6]Superset GitHub:*https://github.com/superset-sh/superset*   
[7]cmux GitHub:*https://github.com/manaflow-ai/cmux*   
[8]Manaflow YC 页面:*https://www.ycombinator.com/companies/manaflow*   
[9]Superconductor (super.engineering):*https://super.engineering/*   
[10]Superconductor (superconductor.com):*https://www.superconductor.com/*   
[11]Awesome Agent Orchestrators:*https://github.com/andyrewlee/awesome-agent-orchestrators*   
[12]Addy Osmani: The Code Agent Orchestra:*https://addyosmani.com/blog/code-agent-orchestra/*   
[13]The New Stack: Conductor Review:*https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/*   
[14]AIBase: Superconductor 报道: *https://news.aibase.com/news/27070*

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA==&mid=2247484448&idx=1&sn=7253e2da3b940d57ff98124667fd5546&chksm=f115d1b496dcec7ed8151181bba15578290d6b87b755b05f7b45df45af45ceb78750d98ae819&mpshare=1&scene=1&srcid=0417r1mIgrOZdOQOEgmlHUtm&sharer_shareinfo=394ed6e79a0378fa722545774164756a&sharer_shareinfo_first=394ed6e79a0378fa722545774164756a)

