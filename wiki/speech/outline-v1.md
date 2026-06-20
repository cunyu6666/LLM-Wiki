---
type: speech-meta
description: "状态：讨论稿 · 待打磨"
timestamp: 2026-06-20
---
# 演讲大纲 v1：从 Design 到 Build

> 状态：讨论稿 · 待打磨
> 受众：还在旧时代或刚接触 AI 的设计师
> 调性：前沿、干货、有冲击力（对标 Cursor / Anthropic 对外分享）

---

## 核心主张（One Big Idea）

**设计师的交付物正在从「图片」变成「代码」——这不是工具升级，是物种进化。**

> 类比：就像摄影师从胶片到数码不是换了个相机，而是整个成像逻辑变了。
> 设计师从 Design 到 Build，不是"多学了一个技能"，而是角色本身在重新定义。

---

## 演讲结构（5 段式，约 45-55 分钟）

---

### 开场 · 一个反直觉的事实（3 min）

**目标**：制造认知冲突，抓住注意力。

> "在座各位，有多少人觉得自己是设计师？"
> "那我告诉大家，过去 6 个月，我作为设计师，做了这些事——"

快速亮出个人实践：
- 我是 QoderWork 的设计师——几乎所有前端界面和 UI/UX 都是我做的
- 设计了 Agent Loop 的交互流程（不是画流程图，是定义了 Agent 的决策逻辑）
- 用 Cursor / Claude Code 开发了产品的前端（没有传统前端工程师参与）
- 维护了一套设计组件库，但消费者不只是人类工程师，还有 AI Agent
- 用 AI 消灭了设计走查这种纯体力活（"以前走查占我一半时间，现在 AI 自动跑"）
- 做了 QoderWork 设计工作台（Design Desk）——"想法即产品，设计即代码"

> "这些事情在传统分工里，没有一件是设计师该干的。但今天，它们全是我工作的一部分。"
> "我不是'转行做了工程师'，我还是设计师——只是设计师的工作方式变了。"

**补充行业信号：**
> "设计师正在从'使用 AI'转向'围绕 AI 重建工作'。AI 已经不是插件，而是设计流程的基础设施。"

📎 来源：[`Cubox/AI in Design Report 2026…`](../../Cubox/AI%20in%20Design%20Report%202026：设计师正在从使用AI转向围绕AI重建工作-2026-06-06.md)

**关键转折**：这不是因为我"额外努力"，而是因为整个行业的底层逻辑变了。

---

### 第一部分 · 旧地图已经失效（8 min）

**目标**：让听众意识到自己正处于范式转换中。

#### 1.1 设计行业的三次范式转移

| 时代 | 交付物 | 核心能力 | 代表工具 |
|------|--------|----------|----------|
| 1.0 手工艺时代 | 视觉稿 | 审美 + 技法 | PS / AI |
| 2.0 系统化时代 | 设计系统 | 系统思维 + 协作 | Figma |
| **3.0 构建时代** | **可运行的产品** | **意图定义 + 评估** | **Cursor / Claude Code** |

> 关键洞察：每一次转移，设计师的边界都在扩大，但核心能力——对人机交互的理解——从未过时。

**John Maeda《2026 科技中的设计报告》的权威背书：**

这份横跨 2015-2026 的全景复盘报告，给出了 7 个核心判断：

> **① 从 UX 到 AX**：AI Agent 可以跳过层层界面，直接将用户送达目标。设计师不再只为用户设计，还要为智能体设计。

📎 来源：[`Cubox/2026科技中的设计报告 - 从UX到AX…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)

> **② 从"执行鸿沟"到"评估鸿沟"**：过去 20 年，设计师致力于优化"用户怎么操作"（执行鸿沟）；未来，设计师的核心任务将转向设计"用户怎么判断 AI 执行的结果是否正确"（评估鸿沟）。

📎 来源：同上

> **③ 设计师从"执行者"变为"评估者"**：大部分设计工作将围绕反馈循环、评估循环、批评循环展开。

📎 来源：同上

> **④ 品味是 AI 学不会的壁垒**：AI 擅长有对错之分的编码，但在主观性强的"品味"面前仍显无力。好的设计 = 高熟悉度 + 高新颖度，这需要运气、直觉与文化的积累。

📎 来源：同上

> **⑤ 从 T 型到树型设计师**：设计师需以设计为根，向"AI 能力"和"工程能力"两个方向生长，成为"树型设计师"。

📎 来源：同上

> **⑥ 系统 3 思维**：在系统 1（本能直觉）和系统 2（理性分析）之外，引入系统 3——利用 AI 增强思维，拓展判断的深度与广度。

📎 来源：同上

> **⑦ 韧性 > 效率**：效率让系统脆弱，冗余让系统有韧性。AI 时代同样需要这种思维。

📎 来源：同上

> **⑧ 开发者文化的崛起**：等宽字体、终端界面、纯文本交互正成为新的设计美学。简洁的文本指令是与机器沟通的最高效路径。

📎 来源：同上

#### 1.2 三个信号，说明你已经站在新时代门口

**信号 1：Figma IPO 估值 563 亿美金**
> "AI 越强，专业设计工具越贵"的反共识逻辑——当 AI 降低执行门槛，品味和系统思维反而更值钱。

📎 来源：[`wiki/design/AI设计工具.md`](../design/AI设计工具.md) → Overview 段

**信号 2：Cursor 华人设计负责人 Ryo Lu 的判断**
> "设计师将开始写代码，工程师将开始做设计，我们的共同语言就是代码。"
> "不是 AI 替代了创作者，而是 AI 覆盖掉他们不擅长的那部分。"

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Cursor 生态段
📎 原始素材：[`Cubox/Cursor Composer 2.5 拆解…`](../../Cubox/Cursor%20Composer%202.5%20拆解：最强大的%20RL%20环境，就是你自己的产品-2026-05-27.md)

**信号 3：OpenAI 设计师的公开表态**
> "不写代码的设计师将成为团队瓶颈。"

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Prompt 设计与工作流段

#### 1.3 为什么旧地图失效了

- 传统流程：PM 写 PRD → 设计师出图 → 工程师还原 → 走查修改
- 新流程：**设计师直接定义意图 → AI 生成 → 设计师评估迭代**

**Vercel 设计团队已经不按传统流程干活了：**
> "他们没有整齐划一地迁移到某一个 AI 工具，也没有抛弃 Figma。真正发生的，是设计、代码、浏览器和 agent 正在缠成一套新的混合工作流。"

📎 来源：[`wiki/design/设计师成长.md`](../design/设计师成长.md) → AI 时代的角色转型段
📎 原始素材：[`Cubox/Vercel 设计团队，已经不按传统设计流程干活了-2026-05-27.md`](../../Cubox/Vercel%20设计团队，已经不按传统设计流程干活了-2026-05-27.md)

**效率对比：**
> "最复杂的页面在别的工具里要写 20 个以上 prompt，Claude Design 里只要 2 个。"

📎 来源：[`wiki/design/AI设计工具.md`](../design/AI设计工具.md) → Claude Design 与开源替代品段
📎 原始素材：[`Cubox/Claude Design 发布设计的新时代…`](../../raw/design/2026-04-18-Claude-Design-发布设计的新时代.md)

> "当你还在等 PM 写 PRD 的时候，有人已经用 Claude Design 2 个 prompt 做出了可交互原型。"

---

### 第二部分 · Design → Build 到底在发生什么（15 min）

**目标**：用具体案例展示"从设计到构建"的真实含义。这是演讲的核心干货段。

#### 2.1 第一层：设计工具在变——从画图到生成

**Claude Design：一句话出界面**
> 3 个人、10 周做出了 Claude Design。"不是说他们用了什么惊天动地的黑科技，恰恰相反——他们做的事情特别朴素。但就是这种朴素的打法，配合 AI 的速度，产生了一种让我觉得'回不去'的效果。"

📎 来源：[`wiki/design/AI设计工具.md`](../design/AI设计工具.md) → Claude Design 与开源替代品段
📎 原始素材：[`Cubox/3 个人、10 周做出了 Claude Design…`](../../Cubox/3%20个人、10%20周做出了%20Claude%20Design%20——%20看完这个分享我坐不住了-2026-05-27.md)

**HTML版剪映：3 天 3 万行代码**
> Open Design 团队 3 天写出 3 万行代码，做出完整的视频制作工具 html-video。一句话描述 → Agent 选模板 → 填内容 → 渲染 MP4。自动识别本地 14 种 Code Agent。

📎 来源：[`Cubox/HTML版剪映来了！…`](../../Cubox/HTML版剪映来了！Open%20Design%20团队最新开源力作，3天时间，写了3万行代码！-2026-06-08.md)
📎 GitHub：https://github.com/nexu-io/html-video

**Claude Design 系统提示词泄露 → 底层是模板引擎：**
> 系统提示词泄露后发现其底层依赖预设的设计模式库，产出容易趋于平庸。但一个月后就出现了 open-codesign（本地优先、支持 71 套设计系统）等开源替代品。

📎 来源：[`wiki/design/AI设计工具.md`](../design/AI设计工具.md) → Claude Design 与开源替代品段
📎 原始素材：[`Cubox/暴击设计行业的 Claude Design 系统提示词在 GitHub 上泄露了…`](../../raw/design/2026-04-24-暴击设计行业的-Claude-Design-系统提示词在-GitHub-上泄露了.md)
📎 原始素材：[`Cubox/open codesign 开源版 Claude Design…`](../../raw/design/2026-04-25-open-codesign开源版-Claude-Design-本地优先的-AI-设计神器.md)

**Codex Annotation：设计最后一公里被补上**
> "新增 Annotation 功能支持像在 Figma 中一样直接在预览界面标注 UI 元素。"

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Codex 与前沿编程工具段
📎 原始素材：[`Cubox/Codex 这次更新，直接把设计最后一公里也补上了-2026-05-27.md`](../../Cubox/Codex%20这次更新，直接把设计最后一公里也补上了-2026-05-27.md)

**DESIGN.md（684k Star）：AI 可读的设计规范成为新标准**

📎 来源：[`wiki/design/设计系统.md`](../design/设计系统.md) → Overview 段

**Tolaria：10 万行代码，一行没写**
> 开源者 Luca 用 Claude Code 写了整个 Tolaria（1.1 万 Star 的笔记工具），代码库超过 10 万行，自己一行都没亲手写。
>
> "这不是'开发者消失了'的证据，而是一种扎实的开发证明：**人跨得过去，工具才能跨得过去。**"
>
> 他不是先有软件就来写了——而是先将自己的知识管理工作流运转了多年，再用代码实现出来。Files-first + Git-first + AI-first，AI 的每次修改都有 diff 可回滚。

📎 来源：[`Cubox/1.1万 Star，又一款笔记工具火出圈了！-2026-05-24.md`](../../Cubox/1.1万%20Star，又一款笔记工具火出圈了！-2026-05-24.md)

> 关键转变：设计的交付物从 .fig 文件变成了可运行的代码。

#### 2.2 第二层：设计师在变——从执行者到构建者

**用自己的工作举例（这是最有说服力的部分）**：

**案例 0（核心案例）：QoderWork — 设计师如何 Build 一个 AI 产品**
> "我是 QoderWork 的设计师。这个产品 5 个人 7 天做出来，没有传统前端工程师。几乎所有的前端界面和 UI/UX 都是我做的。"

- QoderWork 的定位：把 AI Coding 的能力交给不会写代码的人
- 我的角色：不只是"画界面"，而是定义了 Agent 的交互逻辑、工作台的 UI 架构、设计组件库
- AI-native 协作方式：PM 直接写代码画线框图，我直接把设计变成符合前端规范的视觉组件放进代码库——不给高保真图
- Design Desk（设计工作台）："想法即产品，设计即代码"，支持语音输入，在无限画布上获得可运行、可编辑、可交付的设计产物

📎 来源：[`raw/Uncategorized/2026-04-12-我们还是低估了AI-Coding的真正天花板-对谈谢吉宝QoderWork技术负责人.md`](../../raw/Uncategorized/2026-04-12-我们还是低估了AI-Coding的真正天花板-对谈谢吉宝QoderWork技术负责人.md)
📎 来源：[`raw/来自抖音/想法即产品设计即代码 QoderWork正式上线设计工作台Design Desk…`](../../raw/来自抖音/想法即产品设计即代码%20QoderWork正式上线设计工作台Design%20Desk支持语音输入_7641157358437010707.md)
📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md)

> 金句（来自对谈）："UED 同事构思好设计调性后，不是给一张高保真图，而是直接把设计变成了符合前端规范的视觉组件，放进代码库。"

**案例 1：Agent Loop 设计**
- 传统设计师画 Agent 的界面长什么样
- 我在做什么：定义 Agent 的决策循环、工具调用逻辑、人机协作的边界
- 为什么设计师最适合做这件事：因为我们最懂"人机交互的边界在哪里"

📎 支撑观点 — Karpathy："未来十年没有 AGI，只有 Agent"
- 来源：[`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) → Agent 概念与趋势段
- 原始素材：[`raw/…/Andrej-Karpathy-2小时访谈…`](../../raw/Uncategorized/2025-10-20-Andrej-Karpathy-2小时访谈未来十年没有-AGI只有-Agent-附中文版音频.md)

📎 支撑观点 — "Agent 不只是能用工具的 ChatGPT，它需要感知环境、制定计划、执行动作、从反馈中学习"
- 来源：[`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) → Agent 概念与趋势段

📎 支撑观点 — "Agent 时代，UI 不是壳是边界"
- 来源：[`Cubox/Agent时代，UI不是壳是边界-2026-06-01.md`](../../Cubox/Agent时代，UI不是壳是边界-2026-06-01.md)

📎 支撑观点 — "不能被 Agent 用的产品没有未来"——Notion 创始人 Ivan Zhao
- 来源：[`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) → Overview 段

**案例 2：前端开发**
- 用 Cursor + Tailwind + shadcn/ui 直接开发产品界面
- 不需要传统前端工程师——因为设计师最懂 UI 交互
- "figma → MCP → Codex" 工作流已经是实际提效最多的流程

📎 支撑观点 — "figma → mcp → codex 是目前用在工作中实际提效最多的流程"
- 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Prompt 设计与工作流段

📎 支撑观点 — Tailwind + shadcn/ui 正在取代 ElementUI/Ant Design 成为新主流
- 来源：[`wiki/design/前端实现.md`](../design/前端实现.md) → Overview 段

📎 支撑观点 — "Cursor 出彩的背后，Prompt 设计好比网页设计"
- 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Prompt 设计与工作流段

📎 支撑观点 — Jason Liu 把 Codex 改造成持续接管的自主工作系统：跨月存活线程、Heartbeats 定时调度、口述下任务不打字
- 来源：[`Cubox/OpenAI大神教你如何榨干Codex-2026-05-23.md`](../../Cubox/OpenAI大神教你如何榨干Codex-2026-05-23.md)
- 金句："没有验证机制的野心，顶多算个愿望而已。"
- 金句："文件系统仍然是最可靠的记忆基础设施。"

**案例 3：设计组件库维护**
- 不只是给人类工程师用的组件库
- Design Tokens 成为连接设计与 AI 的桥梁
- AI Agent 也需要"读得懂"的设计规范

**案例 4：Agent + 硬件（探索中）**
- 设计师的触角从屏幕延伸到了物理世界
- 当 Agent 有了"身体"——ESP32 小屏幕放在桌面上显示 Claude Code 配额、墨水屏智能手表、桌面 AI 交互设备……
- 为什么设计师适合做这件事：因为我们最懂"人机交互的边界在哪里"——而这个边界正在从屏幕扩展到物理空间
- 从 UX → AX → **Ambient AX**：Agent 不只活在界面里，它正在进入你的桌面、你的手腕、你的房间

📎 来源：[`wiki/design/硬件项目.md`](../design/硬件项目.md)
📎 来源：[`wiki/design/UX与交互研究.md`](../design/UX与交互研究.md) → UX→AX 段
📎 来源：[`Cubox/Agent时代，UI不是壳是边界-2026-06-01.md`](../../Cubox/Agent时代，UI不是壳是边界-2026-06-01.md)

> "当 Agent 从屏幕里走出来，谁来决定它跟物理世界的交互方式？还是设计师。"

📎 支撑观点 — "Design Tokens 成为连接设计与 AI 的关键桥梁"
- 来源：[`wiki/design/设计系统.md`](../design/设计系统.md) → Overview 段

📎 支撑观点 — "AI 时代的设计系统需要为 AI 做好准备：清晰的组件语义、可机器解析的规范"
- 来源：[`wiki/design/设计系统.md`](../design/设计系统.md) → Overview 段

#### 2.3 第三层：行业在变——从 UX 到 AX

**UX → AX（Agent Experience）：设计师不只为用户设计，还要为智能体设计**

📎 来源：[`wiki/design/UX与交互研究.md`](../design/UX与交互研究.md) → Overview 段

**HAX（Human-AI Experience）：新的人机交互范式**

📎 来源：[`wiki/design/UX与交互研究.md`](../design/UX与交互研究.md) → Overview 段

**CHI 最佳论文"塑造 AI 的魔法：一个设计分类法"**

📎 来源：[`wiki/design/UX与交互研究.md`](../design/UX与交互研究.md) → Overview 段

**八/九个 AI 时代产品设计模式被总结出来**

📎 来源：[`wiki/design/UI设计与组件.md`](../design/UI设计与组件.md) → Overview 段
📎 原始素材：[`Cubox/值得收藏关注的8个AI时代产品设计模式-2026-05-22.md`](../../Cubox/值得收藏关注的8个AI时代产品设计模式-2026-05-22.md)

> "当 AI 可以直接'做事'而非'展示结果'时，界面设计的角色是什么？答案是：定义边界。"

#### 2.4 第四层：设计系统在变——消费者不只是人了

**Design Tokens 成为连接设计与 AI 的关键桥梁**
**DESIGN.md（684k Star）：AI 可读的设计规范成为新标准**
**设计系统需要为 AI 做好准备：清晰的组件语义、可机器解析的规范、与 AI Agent 的集成接口**

📎 来源：[`wiki/design/设计系统.md`](../design/设计系统.md) → Overview 段

**Anthropic Skill 方法论的本质：文件夹结构化 + 渐进式暴露 + 隐性经验沉淀**
> "Skill 要沉淀隐性经验而非重复操作步骤，采用文件夹结构化设计避免上下文爆炸，将重复劳动交给脚本而非指令。"

📎 来源：[`wiki/design/AI实操与工具.md`](../design/AI实操与工具.md) → Skill 生态与上下文工程段
📎 原始素材：[`Cubox/Anthropic终于公开了他们内部Skill方法论-2026-06-08.md`](../../Cubox/Anthropic终于公开了他们内部Skill方法论-2026-06-08.md)

**rico-design-md：一个设计师把网站变成设计系统文档**
> 设计师 rico 做了一个 Skill：给一个网站 URL → 自动提取颜色/排版/间距/圆角/阴影 → 输出 DESIGN.md + preview.html + tokens.json + variables.css + theme.css。
>
> "它不是帮你偷一个网站的样子，而是帮你理解一个好网站到底是怎么被组织起来的。"
>
> "这比一句'做得像 Linear 一点'要靠谱太多。"

📎 来源：[`Cubox/设计 SKILL：提取网站规范 DESIGN md 和 HTML 预览-2026-06-05.md`](../../Cubox/设计%20SKILL：提取网站规范%20DESIGN%20md%20和%20HTML%20预览-2026-06-05.md)
📎 GitHub：https://github.com/ricocc/rico-skills

**UI/UX 设计 Skill：把设计流程拆成 7 步自动化**
> 海外设计师把 UI/UX 工作流拆成 7 个 Skill（追问梳理→设计 brief→信息架构→设计 tokens→任务拆解→前端设计→设计审查），每个阶段自动生成结构化产出。
>
> 与 Claude Design 对比：Claude Design 视觉更好，但 Skill 的前期需求梳理更严谨。推荐组合：前期用 Skill 梳理需求 → 最后用 Claude Design 出图。

📎 来源：[`Cubox/测评：海外设计大神分享，最强UI-UX界面设计skill-2026-05-27.md`](../../Cubox/测评：海外设计大神分享，最强UI-UX界面设计skill-2026-05-27.md)
📎 GitHub：https://github.com/julianoczkowski/designer-skills

> "你的设计组件库，现在的消费者不只是人类工程师，还有 AI Agent。"

---

### 第三部分 · 为什么设计师是最适合 Build 的人（12 min）

**目标**：给听众信心——这不是"转行做工程师"，而是设计师能力的自然延伸。
**核心翻转**：你以为你在"学编程"，其实你在用的就是设计思维。

#### 3.1 一个被忽略的事实：你一直在做 Build

> "很多人问我怎么学会写代码的。我说我没学——我只是在做设计。"

**论点 A：Prompt 设计 = 设计思维的新形态**

> "上下文情境工程用设计思维重构 AI 协作逻辑——不是在写代码，而是在定义意图、约束和期望。这与传统设计思维（定义问题→发散→收敛→原型→测试）异曲同工，只是'原型'变成了'对话'。"

📎 来源：[`wiki/design/设计方法论.md`](../design/设计方法论.md) → Overview 段
📎 原始素材：[`Cubox/上下文（情境）工程：用设计思维重构 AI 协作逻辑和方式-2026-06-05.md`](../../Cubox/上下文（情境）工程：用设计思维重构%20AI%20协作逻辑和方式-2026-06-05.md)

**论点 B：上下文工程（Context Engineering）= 设计师的母语**

> "筛选高价值少量信息构建结构化上下文，让 AI 成为稳定可靠的设计协作工具。"

📎 来源：[`wiki/design/AI实操与工具.md`](../design/AI实操与工具.md) → Skill 生态与上下文工程段

**论点 D：行业 Know-how 是冰山下的竞争力**

> "Agentic Workflow 解决的不是意图理解准确率的问题，而是流程上被干预后的可控性。行业的 Know-how 就像冰山，你只看到了表面，冰山下的不可被观测的，才是这个时代个人的竞争力。"

📎 来源：[`Cubox/Agentic Workflow：AI重塑了我的工作流-2026-06-03.md`](../../Cubox/Agentic%20Workflow：AI重塑了我的工作流-2026-06-03.md)

> "Reshape your workflow with AI? or Reshape your AI workflow?" — 这个反问本身就说明了：不是换个工具的问题，是整个工作逻辑在变。

**论点 C：Anthropic 内部 Skill 方法论的本质 = 设计系统思维**

📎 来源：[`wiki/design/AI实操与工具.md`](../design/AI实操与工具.md) → Skill 生态与上下文工程段
📎 原始素材：[`Cubox/Anthropic终于公开了他们内部Skill方法论-2026-06-08.md`](../../Cubox/Anthropic终于公开了他们内部Skill方法论-2026-06-08.md)

> 金句："Prompt 设计好比网页设计"——Cursor 团队的原话
> 📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Prompt 设计与工作流段

#### 3.2 设计师的隐藏优势矩阵

**John Maeda 的"树型设计师"模型：**
> 设计师需以设计为根，向"AI 能力"和"工程能力"两个方向生长。不是 T 型（一个专业 + 广泛涉猎），而是树型——根是设计判断力，枝干是两个方向的延伸能力。

📎 来源：[`Cubox/2026科技中的设计报告 - 从UX到AX…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)

| 能力 | 传统场景 | Build 场景 |
|------|----------|------------|
| 人机交互理解 | 设计界面 | 定义 Agent 行为边界 |
| 信息架构 | 导航设计 | 上下文工程、Skill 结构化 |
| 系统思维 | 设计系统 | 架构产品逻辑、Design Tokens |
| 用户同理心 | 用户研究 | 定义 AI 的"好输出"标准 |
| 视觉品味 | UI 设计 | 评估 AI 生成结果的质量 |
| 原型思维 | 快速出图 | 快速验证产品假设 |

**系统 3 思维——设计师的第三种武器：**
> 在系统 1（本能直觉："这个好看"）和系统 2（理性分析："这个符合规范"）之外，设计师正在发展出系统 3——利用 AI 增强思维，拓展判断的深度与广度。
>
> 设计师天然就是"系统 3 使用者"——我们一直在用工具（Figma、原型工具）来增强自己的判断力，现在只是工具从 Figma 变成了 AI Agent。

📎 来源：[`Cubox/2026科技中的设计报告 - 从UX到AX…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)

#### 3.3 "品味"是 AI 学不会的壁垒

**Claude Design 系统提示词泄露的启示：底层是模板引擎，谁都能用。但有人做出的东西就是好看，有人做的就是平庸——差距在品味。**

📎 来源：[`wiki/design/AI设计工具.md`](../design/AI设计工具.md) → Claude Design 与开源替代品段
📎 原始素材：[`Cubox/暴击设计行业的 Claude Design 系统提示词在 GitHub 上泄露了…`](../../raw/design/2026-04-24-暴击设计行业的-Claude-Design-系统提示词在-GitHub-上泄露了.md)

**Figma VP 的判断：**
> "为 LLM 定义好的设计非常困难"——最终不得不缩小到几个核心布局，并定义非常具体的规则。

📎 来源：[`wiki/design/设计方法论.md`](../design/设计方法论.md) → Overview 段

**"执行交给 AI，判断留给人"**

📎 来源：[`wiki/design/UX与交互研究.md`](../design/UX与交互研究.md) → Overview 段

**"设计师的圣诞树"现象：技能树不断膨胀但收入不涨**

📎 来源：[`wiki/design/设计师成长.md`](../design/设计师成长.md) → AI 时代的角色转型段
📎 原始素材：[`raw/design/2024-08-28-笑哭了设计师的圣诞树…`](../../raw/design/2024-08-28-笑哭了设计师的圣诞树直击心脏不要太真实.md)

**实战案例：设计走查——AI 帮你做尺子的活**
> 一位设计师把占日常一半时间的设计走查完全自动化了：用 Codex + iPhone 镜像 + Computer Use，AI 自动翻页截图比对，输出走查报告。他把走查逻辑写成 Skill，一次编写永久复用。
>
> "AI 帮你量尺寸、比颜色、数像素，这些都是尺子的活。但什么时候该打破规范、整体调性对不对，只有设计师自己知道。"
>
> 日本有个词叫**目利き**——一眼就能看出好坏的那种眼力。

📎 来源：[`Cubox/设计走查这个苦活，我终于用AI跑通了全自动-2026-06-01.md`](../../Cubox/设计走查这个苦活，我终于用AI跑通了全自动-2026-06-01.md)

#### 3.4 不需要"从零学编程"

**Vibe Coding 的本质：用自然语言描述意图，AI 生成代码**

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Overview 段

> "从来没有一款所谓的'最好'的工具，只有最适合你思考、设计及构建方式的工具。"

📎 来源：[`wiki/design/设计师成长.md`](../design/设计师成长.md) → AI 时代的角色转型段
📎 原始素材：[`raw/design/2026-01-08-值得每一位新时代设计师尝试的 8 款 Vibe Coding AI 应用.md`](../../raw/design/2026-01-08-值得每一位新时代设计师尝试的%208%20款%20Vibe%20Coding%20AI%20应用.md)

**8 款 Vibe Coding AI 应用已经为设计师准备好了入门路径**

📎 来源：[`wiki/design/设计师成长.md`](../design/设计师成长.md) → AI 时代的角色转型段

#### 3.5 一个反直觉的论据：DeepSeek 的启示

**DeepSeek 案例："UI 无关紧要"——当产品核心能力足够强时，界面设计退居次要位置。**

📎 来源：[`wiki/design/设计师成长.md`](../design/设计师成长.md) → Overview 段

> 这不意味着设计不重要，而是说：**设计师需要理解什么阶段设计最重要**。
> 在 AI 时代，最重要的设计不是"画界面"，而是"定义 AI 该怎么行为"——这是更上层的设计。

---

### 第四部分 · 怎么开始你的 Design → Build 之路（8 min）

**目标**：给可执行的行动指南，让听众觉得"我也可以"。

#### 4.1 工具链选择（按场景推荐）

| 场景 | 推荐工具 | 上手难度 | 来源 |
|------|----------|----------|------|
| 快速原型 | Claude Design / v0 | ⭐ | 📎 [`wiki/design/AI设计工具.md`](../design/AI设计工具.md) |
| 前端开发 | Cursor + Tailwind + shadcn/ui | ⭐⭐⭐ | 📎 [`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) |
| Agent 交互设计 | Claude Code + MCP | ⭐⭐⭐⭐ | 📎 [`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) |
| 设计系统 AI 化 | DESIGN.md + Design Tokens | ⭐⭐ | 📎 [`wiki/design/设计系统.md`](../design/设计系统.md) |

**其他推荐工具来源：**

> bolt 被评为"目前最好用的全栈 AI 编程软件"

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Prompt 设计与工作流段

> Lovable 员工写了"AI 设计师手册"

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Claude Code 与可视化段

> Huashu Design（14.9K Star）：一句话出设计，让 Claude Code 变身大厂设计团队

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Claude Code 与可视化段
📎 原始素材：[`Cubox/一句话出设计！14.9K Star 的开源神器Huashu Design…`](../../Cubox/一句话出设计！14.9K%20Star%20的开源神器Huashu%20Design，让%20Claude%20Code%20变身大厂设计团队-2026-05-25.md)

#### 4.2 三步走路径

1. **第一周**：用 Claude Design 或 v0 做出第一个可交互原型（建立信心）
2. **第一个月**：用 Cursor 完成一个小产品的前端开发（突破边界）
3. **第一个季度**：参与 Agent Loop 设计，定义 AI 行为逻辑（进入深水区）

#### 4.3 心态转变

> "不是 AI 替代了创作者，而是 AI 覆盖掉他们不擅长的那部分。"
> — Ryo Lu

📎 来源：[`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) → Cursor 生态段

> "我们需要的不是智能体而是工作流。"

📎 来源：[`wiki/design/AI实操与工具.md`](../design/AI实操与工具.md) → Overview 段

> **"韧性 > 效率"**：效率让系统脆弱，冗余让系统有韧性。不要追求"AI 帮我做到 100%"，而是追求"AI 帮我做到 80%，我来判断剩下 20% 该不该做"。

📎 来源：[`Cubox/2026科技中的设计报告 - 从UX到AX…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)

- 从"我不是工程师"到"我是最懂人机交互的构建者"
- 从"学编程"到"学与 AI 协作"
- 从"等别人实现"到"我自己就能 Build"

---

### 收尾 · 一个预言（3 min）

**目标**：留下记忆点，制造传播性。

**用 John Maeda 的"评估鸿沟"收束全场：**
> "过去 20 年，设计师的工作是弥合'执行鸿沟'——让用户知道怎么操作。未来 20 年，设计师的工作是弥合'评估鸿沟'——让用户知道 AI 做得对不对。"
>
> "执行鸿沟已经快被 AI 填平了。但评估鸿沟，只有设计师能填。"

📎 来源：[`Cubox/2026科技中的设计报告 - 从UX到AX…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)

> "我的预言：两年后，最好的产品经理是设计师出身的。最好的前端工程师也是设计师出身的。因为在这个时代，最稀缺的能力不是写代码，而是知道该写什么代码。"

> "设计师从来不是'只会画图的人'。我们是最懂人机交互的人。当 AI 让代码变成新的设计媒介，我们天然就是这场变革的主角。"

> "问题不是'设计师能不能 Build'，而是'除了设计师，谁最适合 Build？'"

**收尾可引用的权威判断：**

> "AI 正在消灭软件，我们要做 Agent 时代的入口。"
> — Bridge 创始人 Enther

📎 来源：[`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) → Agent 概念与趋势段
📎 原始素材：[`raw/…/Bridge首次发声…`](../../raw/Uncategorized/2026-05-12-Bridge-首次发声AI-正在消灭软件我们要做-Agent-时代的入口.md)

> "Agent 产品，快者为王。"
> — Anthropic 与 Databricks CEO 对话

📎 来源：[`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) → Agent 概念与趋势段
📎 原始素材：[`raw/…/Agent产品快者为王…`](../../raw/时事评论/2025-05-10-Agent产品快者为王Anthropic-和-Databrick-CEO-对话解读.md)

---

## 金句清单（可做成 slides 强调页）

| #   | 金句                                                            | 出处                                                                                                                                       |
| --- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | "设计的交付物从图片变成了代码——这不是工具升级，是物种进化。"                              | 演讲者原创                                                                                                                                    |
| 2   | "不写代码的设计师将成为团队瓶颈。"                                            | OpenAI 设计师 · 📎 [`AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md)                                                                 |
| 3   | "执行交给 AI，判断留给人。"                                              | 📎 [`UX与交互研究.md`](../design/UX与交互研究.md) Overview                                                                                         |
| 4   | "最稀缺的能力不是写代码，而是知道该写什么代码。"                                     | 演讲者原创                                                                                                                                    |
| 5   | "除了设计师，谁最适合 Build？"                                           | 演讲者原创                                                                                                                                    |
| 6   | "不能被 Agent 用的产品没有未来。"                                         | Notion Ivan Zhao · 📎 [`AI Agent 开发.md`](../design/AI%20Agent%20开发.md)                                                                   |
| 7   | "设计师不只为用户设计，还要为智能体设计。"                                        | 📎 [`UX与交互研究.md`](../design/UX与交互研究.md)                                                                                                  |
| 8   | "不是 AI 替代了创作者，而是 AI 覆盖掉他们不擅长的那部分。"                            | Ryo Lu · 📎 [`AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md)                                                                     |
| 9   | "Prompt 设计好比网页设计。"                                            | Cursor 团队 · 📎 [`AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md)                                                                  |
| 10  | "未来十年没有 AGI，只有 Agent。"                                        | Karpathy · 📎 [`AI Agent 开发.md`](../design/AI%20Agent%20开发.md)                                                                           |
| 11  | "没有验证机制的野心，顶多算个愿望而已。"                                         | Jason Liu · 📎 [`Cubox/OpenAI大神教你如何榨干Codex…`](../../Cubox/OpenAI大神教你如何榨干Codex-2026-05-23.md)                                             |
| 12  | "AI 帮你量尺寸、比颜色、数像素，这些都是尺子的活。"                                  | 📎 [`Cubox/设计走查这个苦活…`](../../Cubox/设计走查这个苦活，我终于用AI跑通了全自动-2026-06-01.md)                                                                  |
| 13  | "目利き——一眼就能看出好坏的那种眼力。"                                         | 📎 [`Cubox/设计走查这个苦活…`](../../Cubox/设计走查这个苦活，我终于用AI跑通了全自动-2026-06-01.md)                                                                  |
| 14  | "行业 Know-how 就像冰山，冰山下的不可被观测的，才是这个时代个人的竞争力。"                   | 📎 [`Cubox/Agentic Workflow…`](../../Cubox/Agentic%20Workflow：AI重塑了我的工作流-2026-06-03.md)                                                  |
| 15  | "Reshape your workflow with AI? or Reshape your AI workflow?" | 📎 [`Cubox/Agentic Workflow…`](../../Cubox/Agentic%20Workflow：AI重塑了我的工作流-2026-06-03.md)                                                  |
| 16  | "AI 已经不是插件，而是设计流程的基础设施。"                                      | 📎 [`Cubox/AI in Design Report 2026…`](../../Cubox/AI%20in%20Design%20Report%202026：设计师正在从使用AI转向围绕AI重建工作-2026-06-06.md)                  |
| 17  | "更像代码实习生拿到需求后做了一层思考并自主推进，只不过速度快 10 倍。"                        | 📎 [`Cubox/MiniMax M3 首发体验…`](../../Cubox/MiniMax%20M3%20首发体验：被挤崩、被惊艳，接入%20Codex%20后也真香-2026-06-03.md)                                   |
| 18  | "最终我们要教模型的，和我们教孩子的是同一件事。"                                     | 📎 [`Cubox/Claude Code之父…`](../../Cubox/Claude%20Code之父：「品味」不是人类护城河；当工程师不再写代码，招聘看什么？-2026-06-07.md)                                      |
| 19  | "想法即产品，设计即代码。"                                                | QoderWork Design Desk · 📎 [`raw/来自抖音/想法即产品…`](../../raw/来自抖音/想法即产品设计即代码%20QoderWork正式上线设计工作台Design%20Desk支持语音输入_7641157358437010707.md) |
| 20  | "5 个人，7 天做出 QoderWork。"                                       | 📎 [`raw/Uncategorized/2026-04-12-…对谈谢吉宝…`](../../raw/Uncategorized/2026-04-12-我们还是低估了AI-Coding的真正天花板-对谈谢吉宝QoderWork技术负责人.md)            |
| 21  | "UED 不是给高保真图，而是直接把设计变成组件放进代码库。"                               | 📎 同上                                                                                                                                    |
| 22  | "我不是'转行做了工程师'，我还是设计师——只是设计师的工作方式变了。"                          | 演讲者原创（基于 QoderWork 实践）                                                                                                                   |
| 23  | "过去 20 年设计师弥合'执行鸿沟'，未来 20 年设计师弥合'评估鸿沟'。"                      | John Maeda · 📎 [`Cubox/2026科技中的设计报告…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)                                |
| 24  | "设计师要以设计为根，向 AI 能力和工程能力两个方向生长——成为树型设计师。"                      | John Maeda · 📎 同上                                                                                                                       |
| 25  | "好的设计 = 高熟悉度 + 高新颖度，这需要运气、直觉与文化的积累。"                          | John Maeda · 📎 同上                                                                                                                       |
| 26  | "人跨得过去，工具才能跨得过去。"                                             | Tolaria 作者 · 📎 [`Cubox/1.1万 Star…`](../../Cubox/1.1万%20Star，又一款笔记工具火出圈了！-2026-05-24.md)                                                 |
| 27  | "它不是帮你偷一个网站的样子，而是帮你理解一个好网站到底是怎么被组织起来的。"                       | rico · 📎 [`Cubox/设计 SKILL…`](../../Cubox/设计%20SKILL：提取网站规范%20DESIGN%20md%20和%20HTML%20预览-2026-06-05.md)                                 |
| 28  | "韧性 > 效率：效率让系统脆弱，冗余让系统有韧性。"                                   | John Maeda · 📎 [`Cubox/2026科技中的设计报告…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md)                                |
| 29  | "等宽字体、终端界面、纯文本交互正成为新的设计美学。"                                   | John Maeda · 📎 同上                                                                                                                       |

---

## 完整引用索引

> 按 wiki 文章分类，列出本大纲引用的所有 wiki 文章和原始素材。

### 引用的 wiki 编译文章（9 篇）

| wiki 文章 | 引用段落 | 路径 |
|-----------|----------|------|
| AI设计工具 | Claude Design、Codex、Lovart、系统提示词泄露 | [`wiki/design/AI设计工具.md`](../design/AI设计工具.md) |
| AI编程与Vibe Coding | Ryo Lu、Cursor、Codex Annotation、Prompt 设计、工作流 | [`wiki/design/AI编程与Vibe Coding.md`](../design/AI编程与Vibe%20Coding.md) |
| AI Agent 开发 | Karpathy、Ivan Zhao、Agent 概念、Bridge、HAX | [`wiki/design/AI Agent 开发.md`](../design/AI%20Agent%20开发.md) |
| 设计系统 | Design Tokens、DESIGN.md、AI 可读规范 | [`wiki/design/设计系统.md`](../design/设计系统.md) |
| 设计方法论 | 上下文工程、Figma VP、Prompt = 设计思维 | [`wiki/design/设计方法论.md`](../design/设计方法论.md) |
| UX与交互研究 | UX→AX、HAX、CHI 论文、执行交给AI | [`wiki/design/UX与交互研究.md`](../design/UX与交互研究.md) |
| 设计师成长 | Vercel 团队、圣诞树、DeepSeek、Vibe Coding 8 款应用 | [`wiki/design/设计师成长.md`](../design/设计师成长.md) |
| 前端实现 | Tailwind/shadcn 新主流、AI 入侵前端 | [`wiki/design/前端实现.md`](../design/前端实现.md) |
| AI实操与工具 | Anthropic Skill 方法论、上下文工程、工作流 | [`wiki/design/AI实操与工具.md`](../design/AI实操与工具.md) |
| UI设计与组件 | 8 个 AI 时代产品设计模式 | [`wiki/design/UI设计与组件.md`](../design/UI设计与组件.md) |

### 引用的原始素材（Cubox / raw）

| 原始素材 | 路径 |
|----------|------|
| Cursor Composer 2.5 拆解 | [`Cubox/Cursor Composer 2.5 拆解…`](../../Cubox/Cursor%20Composer%202.5%20拆解：最强大的%20RL%20环境，就是你自己的产品-2026-05-27.md) |
| Vercel 设计团队新工作流 | [`Cubox/Vercel 设计团队…`](../../Cubox/Vercel%20设计团队，已经不按传统设计流程干活了-2026-05-27.md) |
| Claude Design 发布 | [`raw/design/2026-04-18-Claude-Design-发布…`](../../raw/design/2026-04-18-Claude-Design-发布设计的新时代.md) |
| Claude Design 系统提示词泄露 | [`raw/design/2026-04-24-暴击设计行业的…`](../../raw/design/2026-04-24-暴击设计行业的-Claude-Design-系统提示词在-GitHub-上泄露了.md) |
| open-codesign 开源替代品 | [`raw/design/2026-04-25-open codesign…`](../../raw/design/2026-04-25-open-codesign开源版-Claude-Design-本地优先的-AI-设计神器.md) |
| Codex Annotation 更新 | [`Cubox/Codex 这次更新…`](../../Cubox/Codex%20这次更新，直接把设计最后一公里也补上了-2026-05-27.md) |
| 3 个人 10 周做 Claude Design | [`Cubox/3 个人、10 周…`](../../Cubox/3%20个人、10%20周做出了%20Claude%20Design%20——%20看完这个分享我坐不住了-2026-05-27.md) |
| Agent 时代 UI 不是壳是边界 | [`Cubox/Agent时代…`](../../Cubox/Agent时代，UI不是壳是边界-2026-06-01.md) |
| 8 个 AI 时代产品设计模式 | [`Cubox/值得收藏关注的…`](../../Cubox/值得收藏关注的8个AI时代产品设计模式-2026-05-22.md) |
| Anthropic Skill 方法论 | [`Cubox/Anthropic终于公开了…`](../../Cubox/Anthropic终于公开了他们内部Skill方法论-2026-06-08.md) |
| 上下文情境工程 | [`Cubox/上下文（情境）工程…`](../../Cubox/上下文（情境）工程：用设计思维重构%20AI%20协作逻辑和方式-2026-06-05.md) |
| Karpathy 2 小时访谈 | [`raw/…/Andrej-Karpathy-2小时访谈…`](../../raw/Uncategorized/2025-10-20-Andrej-Karpathy-2小时访谈未来十年没有-AGI只有-Agent-附中文版音频.md) |
| Agent 产品快者为王 | [`raw/…/Agent产品快者为王…`](../../raw/时事评论/2025-05-10-Agent产品快者为王Anthropic-和-Databrick-CEO-对话解读.md) |
| Bridge 首次发声 | [`raw/…/Bridge首次发声…`](../../raw/Uncategorized/2026-05-12-Bridge-首次发声AI-正在消灭软件我们要做-Agent-时代的入口.md) |
| 设计师的圣诞树 | [`raw/design/2024-08-28-笑哭了…`](../../raw/design/2024-08-28-笑哭了设计师的圣诞树直击心脏不要太真实.md) |
| 8 款 Vibe Coding 应用 | [`raw/design/2026-01-08-值得每一位…`](../../raw/design/2026-01-08-值得每一位新时代设计师尝试的%208%20款%20Vibe%20Coding%20AI%20应用.md) |
| Huashu Design | [`Cubox/一句话出设计！…`](../../Cubox/一句话出设计！14.9K%20Star%20的开源神器Huashu%20Design，让%20Claude%20Code%20变身大厂设计团队-2026-05-25.md) |
| **🆕 OpenAI 大神榨干 Codex** | [`Cubox/OpenAI大神教你如何榨干Codex-2026-05-23.md`](../../Cubox/OpenAI大神教你如何榨干Codex-2026-05-23.md) |
| **🆕 设计走查全自动** | [`Cubox/设计走查这个苦活…`](../../Cubox/设计走查这个苦活，我终于用AI跑通了全自动-2026-06-01.md) |
| **🆕 Agentic Workflow 重塑工作流** | [`Cubox/Agentic Workflow…`](../../Cubox/Agentic%20Workflow：AI重塑了我的工作流-2026-06-03.md) |
| **🆕 HTML版剪映 3天3万行** | [`Cubox/HTML版剪映来了！…`](../../Cubox/HTML版剪映来了！Open%20Design%20团队最新开源力作，3天时间，写了3万行代码！-2026-06-08.md) |
| **🆕 AI in Design Report 2026** | [`Cubox/AI in Design Report 2026…`](../../Cubox/AI%20in%20Design%20Report%202026：设计师正在从使用AI转向围绕AI重建工作-2026-06-06.md) |
| **🆕 MiniMax M3 首发体验** | [`Cubox/MiniMax M3 首发体验…`](../../Cubox/MiniMax%20M3%20首发体验：被挤崩、被惊艳，接入%20Codex%20后也真香-2026-06-03.md) |
| **🆕 Claude Code 之父** | [`Cubox/Claude Code之父…`](../../Cubox/Claude%20Code之父：「品味」不是人类护城河；当工程师不再写代码，招聘看什么？-2026-06-07.md) |
| **🆕 Claude 设计负责人** | [`Cubox/Claude 设计负责人…`](../../Cubox/Claude%20设计负责人：下一个%2010%20年，这%203%20个能力最重要-2026-06-06.md) |
| **🆕 Anthropic 产品负责人** | [`Cubox/Anthropic产品负责人…`](../../Cubox/Anthropic产品负责人：面了上百个产品经理后，发现大多人缺少的是这种底层思维方式（下篇）-2026-06-06.md) |
| **🆕 QoderWork 对谈（5人7天）** | [`raw/Uncategorized/2026-04-12-我们还是低估了AI-Coding的真正天花板…`](../../raw/Uncategorized/2026-04-12-我们还是低估了AI-Coding的真正天花板-对谈谢吉宝QoderWork技术负责人.md) |
| **🆕 QoderWork Design Desk** | [`raw/来自抖音/想法即产品设计即代码 QoderWork…`](../../raw/来自抖音/想法即产品设计即代码%20QoderWork正式上线设计工作台Design%20Desk支持语音输入_7641157358437010707.md) |
| **🆕 2026科技中的设计报告（Maeda）** | [`Cubox/2026科技中的设计报告 - 从UX到AX…`](../../Cubox/2026科技中的设计报告%20-%20从UX到AX，设计正在经历一场范式革命-2026-06-02.md) |
| **🆕 Tolaria（10万行代码全AI写）** | [`Cubox/1.1万 Star，又一款笔记工具火出圈了！…`](../../Cubox/1.1万%20Star，又一款笔记工具火出圈了！-2026-05-24.md) |
| **🆕 rico-design-md（设计SKILL）** | [`Cubox/设计 SKILL：提取网站规范…`](../../Cubox/设计%20SKILL：提取网站规范%20DESIGN%20md%20和%20HTML%20预览-2026-06-05.md) |
| **🆕 UI/UX 设计 Skill 测评** | [`Cubox/测评：海外设计大神分享…`](../../Cubox/测评：海外设计大神分享，最强UI-UX界面设计skill-2026-05-27.md) |

---

## 待讨论的问题

- [ ] 演讲的具体时长？（当前按 45-55 min 设计）
- [ ] 是否需要 live demo 环节？（比如现场用 Cursor 做一个小产品）
- [ ] 听众的具体画像？（纯设计师？还是有工程师/PM 在场？）
- [ ] 是否需要更多个人案例的具体细节？
- [ ] 演讲的场合和平台？（影响调性和深度）
- [ ] 标题是否需要更有冲击力？
- [ ] 是否需要加入"Context Engineering = Design Thinking"作为独立的核心论点？
- [ ] 是否要讲"设计系统的消费者变了"这个点？

---
*基于 wiki 知识库 10 篇编译文章 + 30 篇原始素材整理 · 29 条金句 · 另有 5 篇待抓取原文*
