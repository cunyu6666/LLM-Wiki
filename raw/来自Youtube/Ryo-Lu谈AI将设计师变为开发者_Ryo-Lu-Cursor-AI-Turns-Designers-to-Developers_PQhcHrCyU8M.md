---
type: note
description: "频道/作者：a16z Deep Dives"
timestamp: 2026-06-20
---
# Ryo Lu (Cursor): AI Turns Designers to Developers

> **频道/作者**：a16z Deep Dives
> **链接**：[https://www.youtube.com/watch?v=PQhcHrCyU8M](https://www.youtube.com/watch?v=PQhcHrCyU8M)
> **时长**：50:47
> **发布日期**：2025-11-21
> **字幕抓取日期**：2026-06-20
> **字幕来源**：YouTube 自动生成字幕（en）
> **段落数**：108

---

## 信达雅中文翻译

> **嘉宾**：Ryo Lu（Cursor 设计负责人，前 Notion 设计主管）
> **主持**：Jennifer（a16z Deep Dives）
> **翻译**：AI 译校 · 信达雅风格

### 开场

**Jennifer**：过去十五年左右，软件制作的技艺高度碎片化了。我们被拆成不同的角色，每个角色用自己的工具、自己的产出物、自己的术语和行话。而 Cursor 让一切翻转了过来——这是第一次，"设计"对更多人来说变成了一个触手可及的概念和技能。它把那些有设计抱负的人、想造东西的人、想做原型的人、想把美好事物放进世界的人，聚到了一起。

但总得有人来定义什么是好、什么是对、我想要怎么做。如果你不注入自己的观点，它只会产出 AI 泔水。

人们永远会有自己的长处和独特技能。我把 AI 看作一种通用接口。

设计的本质，就是为所有人找到最佳配置和最简状态。美，在于把一切整合到一起。

Ryo，欢迎来到 a16z 播客。

**Jennifer**：你一直在思考设计的演进，以及它与基础设施和软件开发的关系。为什么这么兴奋要请 Ryo 来聊？

过去几个月，Ryo 和我一直在聊大语言模型和 AI 工具将如何影响设计师、设计工程师，以及人们构建原型和产生创意的方式。我觉得这是第一次，设计对更多人来说变得如此平易近人——它把有设计抱负的人、想造东西的人、想把美好事物放进世界的人，更紧密地连在一起，也更快了。Ryo 经历了很多思考，关于设计意味着什么、Cursor 如何成为构建基石。我很想请他来聊聊编程与设计的未来。

### Ryo 的职业 journey 与软件制作的演变

**Ryo Lu**：做软件有太多层抽象和深度了。要做出真正伟大的东西，你要么什么都懂，要么组建一个各层都有强项的团队——最好的 infer 工程师、做 ML 的人、能手写完美 CSS 的设计工程师。要让一个人学会所有这些，需要漫长的试错，从最简单的东西开始，逐步升级，公开你的作品，看反馈，循环迭代。

如果在团队里，有时更慢。你只是个设计师，在 Figma 里画图，分享出去，拿到反馈，然后 PM 要搞 PR 流程，开更多会，更多人卷入，一年后你的设计上线了，但只实现了你想要的 20%。

但有了 Cursor 这样的新工具，你只需要有一个想法——哪怕有点模糊——告诉 Agent，它可能第一枪就给你 60%、70% 的结果。你跳过了大量复杂性。

我们从"你得先理解所有软件概念才能做事"，变成了"我现在就能做，可能不完美，但迭代和推敲的过程变得极快"。随着 Agent 进化、模型变强、它能对接更多工具——更好地理解视觉、能连 Figma 读你的设计稿、能连 Notion 读文档和会议纪要——最重要的是，它理解代码库，也就是我们构建软件的真实材料。

这改变了一切。

工具不仅影响个人工程师。对 Cursor 来说，我们尽量适配更多工作流和人。有些人以自己的代码洁癖为傲，他们可以用 Tab 补全——Tab 已经好到几乎知道你想做什么。也有越来越多的人开始用 Agent，连最资深的程序员也在尝试这种新方式。

### 角色的融合与协作的坍缩

**Jennifer**：我之前在产品侧工作，和设计师、设计工程团队紧密合作。那时候还不叫"设计工程"，叫设计师、前端工程师、UX 设计师。工作流非常割裂。设计工作在孤立中进行——设计师花两周出概念，和 UX 设计师一起定义体验，然后交给产品团队和工程师。Figma 已经把这个流程拉近了很多，大家可以在一个产出物上协作、给反馈、做原型，让东西更接近真实。而 Cursor 又近了一步——你可以直接操作和体验那些功能性的、可运行的产出物。

**Ryo Lu**：过去十五年左右，软件制作高度碎片化，我们被拆成不同角色，每个角色用自己的工具、自己的产出物、自己的术语。设计师困在 Figma 里，之前是 Sketch，再之前是文件。PM 写文档、开会，在 Google Docs 里。数据人员在别的工具里。每个人都在自己的孤岛里，然后我们需要发明流程来串联一切，或者造更好的工具来统一。

我们在 Notion 试过，但问题是人们已经养成了太多习惯，有惯性，你没法强迫任何人采用一个不完全适合自己的新东西。

但有了 AI，有了 Cursor，一切又翻转了。我们想造一个能连接和吸收所有这些产出物和格式的东西。

未来在 Cursor 里，同一段代码可以有不同视图——原始代码，或者更高层次的视图。本质上，做软件就是改代码。PM 写 PRD 也是在改代码，只是通过一种更被动的、组织化的方式。设计师更多影响视觉层面。但当你割裂地做这些事，随着团队增长，协作问题越来越多，事情变得越来越复杂，不再统一。

我们总是说"交付你的工作"，然后不同角色开始争论——设计师对的、工程师对的、PM 对的——但有一个共享的真相，就是代码。你可以围绕它收集、综合所有信息，Agent 可以处理那些你可能不完全了解但它知道真相的事情。

它知道现在——代码库里有什么、正在运行的任务和项目。它也知道过去——你积累的所有知识、团队偏好、代码库的演变。它甚至能触及未来——你在规划、在构想更大的想法。你可以用一个 Agent 做所有这些，只是对每个用户或团队，它可能呈现不同的形态。

我们想要的是一个几乎适用于任何人、任何事的基础体验，但如果你知道自己在做什么、有特殊需求，你可以更深入。未来你甚至可能用 Cursor 就像用 Figma 一样。但区别在于，你不再跟孤立的 App 和它们各自的格式打交道，不用手动开会做转换——它直接做了。你只需要思考想法，用最适合你的方式迭代。对工程师可能是代码编辑器，对设计师可能是更视觉的东西，对 PM 可能是更像文档的界面。

### 品味（Taste）到底是什么

**Jennifer**：AI 来了之后，"品味"这个概念被反复提起。现在有了一个 Agent 同事帮你写代码、设计元素。品味住在哪里？它从哪来？你能依赖 Agent 有好品味吗？还是说这仍然严重依赖人类创作者？

**Ryo Lu**：我不太喜欢人们把"品味"当一个词来说，因为太模糊了。

我怎么看呢？品味有一部分是你在所有选项中做选择。但要做选择，你得先见过一切——你挖掘过过去，知道人们以前怎么做这类事；你把过去的某些东西和自然中的、人造的东西联系了起来；或者你随着时间建立了一种偏好——几乎是在自我划定边界：这是对的、这是美的、这是好的。每个人都很不同，没有对错，更多取决于你见过什么。

这几乎就像一个 LLM。但 LLM 的问题是：它其实见过一切，却没有自己的观点——或者说它把自己搞糊涂了，以为人们到处都想要紫色渐变。

LLM 的好处是它见过太多东西，能极快极好地做出基线。而在基线之上的东西，就是品味——你自我选择的边界。那是你的决定。

虽然 AI 越来越能帮你做这件事。比如 Cursor 有个新功能叫 Plan Mode。你输入提示词，不想填细节，可以切到 Plan 模式——它会帮你搭建规格，然后你可以加细节、随意修改。

但说实话，我不信你给 Agent 一长串模糊的、非特定的提示词，然后指望它给你 exactly 想要的东西。不会奏效的。总得有人来定义什么是好、什么是对、我想要怎么做。如果你不注入自己的观点，它只会产出 AI 泔水。

### 角色的未来

**Jennifer**：你之前提到 PM、设计师、工程师之间的博弈。随着界限模糊，这些角色会怎么演变？

**Ryo Lu**：人们永远会有自己的长处和独特技能。有些人擅长协调，有些人擅长视觉，有些人擅长底层架构。但我把所有这些人看作同一类人——软件建造者、创造者。

回头看早期计算时代，没有头衔。研究人员可能设计底层架构、构建 UI、决定怎么在屏幕上显示——整个东西可能就是一两个人或五个人做的。那时候也没那么多经济约束，他们被资助着，不太想着赚钱，所以做出了完整的东西。

现在呢？你把一切拆开，用流程和成本优化来优化，人被框进小领域和问题集，而整个东西其实是合在一起的。

我认为这造成了很多问题。人们做软件时不再想那个理想的东西了——人们太关注技术问题、设计问题、钱的问题，而不是我们在为人们造什么。

但我们现在在往回走。像 Cursor 这样的工具——如果你自认是设计师或开发者，我以前也纠结这个。我开始自己做东西，整个东西。然后我来到美国，得到一份"产品设计师"的工作。我不再写代码了。我做模型和原型，等它们发生。等了好几年。它们没发生——或者说，最终以上传 YouTube 视频的形式发生了。

太疯狂了。但有了这个新工具，设计师可以建造了。他们可以在自己真正关心的手艺上打磨，让 Agent 处理其余的。他们可以把品味放在顶层，把不想操心的事交给 Agent。

你也可以组建一个非常好的团队——好的工程师、前端工程师、不只是开会的 PM——把所有人聚在一起，给他们同一个工具、同一个代码库，他们能开始互补弱点、放大长处，Agent 把一切串起来。不用再追着人问"你的设计在哪"。

### 设计不只是美学

**Jennifer**：你之前在 Notion、Asana 这些以设计为中心的公司工作过。现在谁能触碰产品外在的美学部分了，你怎么影响当前团队和 Cursor 的人花更多精力思考这些，而不只是功能？

**Ryo Lu**：有一点我想强调：设计不只是美学。

我看待设计的方式是——它其实包含了所有东西：架构设计、这个产品是什么的概念、公司的概念。以 Notion 为例，Notion 是一个纯粹的概念性产品——每一个概念都是人设计的。

Notion 的核心就是：区块、页面、数据库、工作区。一切都围绕这些概念运转。每一层都有它们的表征——最顶层是 UI、品牌、视觉、美学；但也有每一层的美学——前端代码架构怎么设计、响应式状态怎么同步、怎么渲染、怎么存储这些对象、它们怎么互相关联。

如果你看软件，看概念本身，其实非常简单。设计的本质，就是为这一切找到最佳配置和最简状态。

有些人可能只关注视觉或交互或某个切面。但我觉得美在于把一切尽可能好地整合在一起。所以设计不是纠结用 6 像素还是 4 像素的圆角。而是：我怎么设计最简单的系统、最少的概念、最少的代码路径，为最多的人做最多的事。

### Cursor 与设计师

**Jennifer**：你们和开发者有极强的 PMF。能分享一下你们怎么思考服务设计师的吗？或者你觉得有机会提供什么样的工具？

**Ryo Lu**：Cursor 的主要焦点仍然是专业开发者和团队。但因为他们周围的人已经来了。

其实很长一段时间，我们有意让 Cursor 对非技术人员来说相当难入门。但他们现在来了，真的很难进来，又真的很想进来。

一个例子：打开 Cursor，三个按钮——"打开项目"、"连接 SSH"、"克隆仓库"。作为新手或非技术人员，我一个都看不懂。但如果我们直接给你一个空白的 Agent 视图，你可以直接开始做事呢？

有很多小细节可以修，让 Cursor 对这些人更友好——他们可能懂软件概念的某些层，但不会写代码。我要确保他们进来时不会被吓到，不会觉得"啊这是个代码编辑器、是个 IDE"。而是"我能开始做事了"。随着做事，他们可以选择自己喜欢的路径。设计师可能就在旁边开个浏览器聊天。Agent 在改代码的时候，他们可以预览变化、在浏览器里交互、点这个元素说"啊我想把这个换掉"——然后就发生了。

怎么做呢？不是创建新产品或拆分 Cursor。是同一件事，只是不同的预配置和包装。

因为就像我说的，想概念——Cursor 本身其实很简单，AI Agent 整体也很简单。你看 ChatGPT Agent、Cursor、Replit、v0、Notion Agent——架构或工作方式几乎一样。

如果我们能想出一套通用的、共享的概念来与 AI、Agent、代码、软件交互，但可以把每一个变异成更适合不同人和不同用例的形态呢？每一个都可以用最适合的模型做 UI 的事，用最适合我的视图。我可以随意配置。想看一切，可以。什么都不想看，也行。

### 万能工具 vs 专用工具

**Jennifer**：过去几年有"为特定角色打造的专用工具"的概念——Webflow 给设计师、v0 给前端开发者。现在更流行"万能应用"的概念——ChatGPT 是万能应用、Notion 是万能应用、Cursor 也越来越是。万能应用是我们正在走的方向吗？专用工具还有位置吗？

**Ryo Lu**：这只是做软件的不同哲学。

几乎有两种看问题的方式。一种是以用户为中心的设计路径——你从一个具体问题出发，识别有这个问题的人群，弄清楚他们想要什么，为他们构建非常具体的解决方案。另一种是更系统的角度——你看软件本身、它怎么构成的，然后想我在哪里微调一下来满足这个约束、让这个用例跑通、让这个工具为这些人服务。

这是两种根本不同的哲学。以用户为中心的方式更容易起步，但它从一开始就限制了你——当你构建了只适用于特定人群的解决方案，如果你想扩大人群或用例，你得拆掉核心概念，很多人做不到。

所以他们加更多东西、更多概念、更多功能，直到有一天这个东西不再服务最初那群人了。简单的东西不再简单，专用的东西不再简单。

所有这些专用 App，它们有点自私。它们在孤岛化人们、孤岛化工作流、孤岛化文件格式，制造岛屿。

如果你看 Notion 怎么做——Notion 的核心概念其实是：区块、页面、数据库、工作区。每个区块几乎就是一个 JSON 对象，页面就是一个 JSON 对象数组，我们按类型和布局渲染每个区块。它们可以放进数据库，有更多属性，共享更多东西，有层级，页面可以嵌套。这就是 Notion。然后你可以用它做任何事——任务、项目、数据库，它们都能协作。

问题是，这种更通用的 App 因为太开放，很难上手。如果我没耐心搞清楚它怎么运作，我可能连任务和项目都碰不到。

所以总有这个张力，但可以修复。你可以做更好的包装，可以用 AI。我个人偏好是：尝试构建对所有人都更好用的东西，而不是"这些人是我在乎的，其他人我不 care，他们应该用我的东西"。不是这么做的。

### AI 作为通用接口

**Jennifer**：我们聊 AI、聊 Agent、聊它如何加速构建和原型。但作为设计领导者，与 AI 交互如何真正提升产品的可用性和实用性？

**Ryo Lu**：我把 AI 几乎看作一种通用接口。最低限度就是一个提示词，然后你得到一些响应。然后你可以把它放进不同形态——可以是一个小输入框、一个聊天框、一个侧边栏、选中某个元素后弹出的操作。也可以完全改变这一层——不是聊天、不是输入框，而是更有目的性的东西。但底层是一样的——同一个 AI、同一个 Agent、同一个架构，可以切换不同模型和提示词。

正因为如此，你可以构建很多不同的层和形态。每个人可以找到适合自己的形态，感觉更舒适。但也总有那个基线——它几乎就像 Google，ChatGPT 就是一个框，你什么都可以放。但会有更具体的工具，更适合每个人或用例。

**Jennifer**：从现在起每个软件都从一个聊天框开始吗？UX 设计在其中扮演什么角色？

**Ryo Lu**：想象一下，只有聊天。那也会是很糟糕的体验——你对着一个空白框，得主动发起、问对的问题、输入对的提示词。除非你已经玩了很多次，否则你不知道会得到什么回应。新人试一次，得到的不是想要的，就觉得"啊这不适合我、这很烂"。

但这里有太多潜力了。今天的模型已经能为很多人、很多用例做太多事了。我们需要设计一种机制，帮他们把输入输出转化为适合他们的形式、格式、视图、工作流——引导他们到达目的地，而不是强迫他们"现在你得用这个工具"，然后不知道它怎么跟自己的工作流连接。

那些才是更适合个人或用例的形态。因为我不想每次都打字问问题，也不想读一大堵文字回复。而自动补全那一行直接出现、我按 Tab 就行；或者我在画布上选几个元素说"给我做四个变体"——然后就出来了。底层是同一个东西。

### 约束与创造力

**Jennifer**：聊到创造力，很多时候更多约束和护栏反而是创造力的朋友。现在我们有了更开放的世界、更有能力的工具。你怎么在工作中保持约束？

**Ryo Lu**：最大的约束，某种意义上，是简洁。

也就是说，在任何给定时间、对任何给定个人，你能暴露的概念和东西的数量是有上限的。这是一个天然的约束。

比如认知层面有约束，空间层面也有约束。Cursor 的窗口可以这样拉、那样拉。如果就这么大呢？你就开始削减——你在优先排什么该显示、什么最重要。这些东西其实不怎么变。搞清楚这些很重要，然后你可以构建一种机制来容纳更多东西——比如第二层的东西，某些人想做的更具体的操作模式或工作流部分，针对不同人或偏好。但它们仍然是核心概念的层，不是线性地一次性把所有东西都堆给你。

界面——软件怎么呈现自己、我们怎么设计——会开始不再是"设计师决定按钮放哪，然后就是固定的"。而是有共享的概念和共享的机制，但可以呈现不同形态——你可以暴露方式让人们自定义、变成自己的。

设计师真正在思考的是：最重要的概念是什么？它们在每一层怎么关联？对 80% 的人，默认值应该是什么？这个 App 最简单的状态是什么？然后你可以为不同人分叉——在第二层暴露更多高级用户功能或不同原型。但默认应该保持简单。

理想状态是——很多工具不告诉你发生了什么、怎么运作的。比如今天大多数 CLI 编程 Agent，它们逼你用这个小小的窗口和小小的提示框——那几乎是你所有的交互，你把一切都委托给 Agent，不太知道 things 怎么运作。

而 Cursor，如果你喜欢极简，完全可以。但你可以开始挖更深——你可以自定义 Agent、创建自己的自定义模式、选不同模型偏好、选哪些工具、哪些提示词。你可以选择看代码、看预览、看文档、看浏览器。可以改所有颜色。可以用键盘、可以用鼠标。

而设计师在做的是——思考最小抽象集、那个能处理所有这些排列组合的系统。

### 灵感与日常

**Jennifer**：你有无可挑剔的品味和设计感。日常生活中你怎么培养周围环境来持续找到灵感、把最好的设计带向世界？有什么习惯想分享的？

**Ryo Lu**：我没有固定的日常，比较零散。

我不会整天坐在 Figma 里做模型。我喜欢同时做所有事的那种 vibe。我可能在思考一个更长期的问题。

我喜欢写作，用要点列表思考。我会走出办公室散步，手机开着 Notion 页面，开始写。

我会画草图、玩单个空间、做原型写代码。很多灵感来自不强迫它、留一些空白让东西慢慢炖。

很多来自看东西——看一切，不只是软件。印刷设计、平面设计、动态、电影、音乐、艺术——人类做的一切。自然的东西也很酷。学习自然系统。我学生物的，所以很多东西有相似性——你能构建多少层、它们怎么交互。看过去也很有帮助。

我的 Ryo OS 项目就是从去年开始的。我买了一堆旧 Mac 和 iPod，就是玩它们，想重现那种感觉。

**Jennifer**：很多设计师的个人主页都是最闪亮的、面向未来的设计，你却放了一个 Mac OS 界面和初代 iPod 图标。多讲讲 Ryo OS 项目？

**Ryo Lu**：我离开 Notion 的时候，开会时会弄出声音。就想给他们做个小礼物。我用 Cursor 做了一个音效板 App——就一个 App，看起来是很烂的 Tailwind 默认样式。然后我想，如果做得更像复古 Mac OS 呢？它就把界面放进了一个复古 Mac OS 风格的窗口里。然后我说加个菜单栏，加在顶部。然后我想，我有了菜单栏和窗口，为什么不干脆多做几个 App 和窗口？就这么开始了。然后我停不下来了，三四个月。

很多界面我从 System 7 的灵感开始。有准确性，但也加了一些未来的东西。后来我做了更多主题——Mac OS 10 的第一个 Aqua 主题、Windows 95 和 XP。切换之间，玩这个 OS，每个都很地道，但其实底层是同一个东西。

这就是我想传达的信息：我们从一开始就在反复做同样的事，只是每个时代的技术约束不同，所以它呈现成那个样子。

但我们把很多这些概念和模式一直带到了现在，我们仍然活在其中。我不认为 things 会改变那么多。有些永恒的东西不怎么变。归根到底，是人们试图想出一些非常熟悉的想法，然后把它们带到新的媒介。

1984 年我们在做同样的事，现在人们只是用 Paint 画画、有文本编辑器可以打字、有图标、有桌面——这些都没怎么变。

**Jennifer**：那些永恒的概念——浏览器、播放器、聊天窗口——都在 Ryo OS 项目上。想体验的观众可以去 os.real.loo。

**Ryo Lu**：没错。

**Jennifer**：太好了。到此结束。非常感谢 Ryo 来做客。太棒了。

---

## 英文文字稿（带时间戳）

> 段落格式：`[时:分:秒] 文字内容`

**[00:00:00]** Over the last I don't know 15 years or so the art of making software fragmented a lot and then we kind of split into different roles. Each role kind of used their own tool. You use their own artifact. They think in their own kind of words and lingo with cursor things kind of flip again. for the first time that design is such an approachable concept and skill set to a lot more people and it brings together sort of people who have aspirations for design and wanting to build things, wanting to prototype things, putting beautiful stuff out in the world. There needs to be something for the human to specify what is good, what is right, how I want to do it. If you don't put in that opinion, it will just produce AI slot.

**[00:00:45]** People will always have their strength or their unique special skill. I see AI almost like it's almost like a universal interface.

**[00:00:58]** So design is kind of like trying to figure out what is the best configuration and the simplest state for all of us. The beauty is actually putting things all together.

**[00:01:07]** Rio, welcome to the Async Z podcast.

**[00:01:16]** >> Mhm. Uh Jennifer, you've been thinking a lot about sort of evolution of design um evolution sort of as it relates to uh infra as well as software development.

**[00:01:26]** Why don't you talk about what got you so excited about having Rio and you know why we have this conversation? Rio and I uh got to know each other over the past few months talking about how large language models and AI tools are going to impact not just designers, design engineers and how people are building prototypes and coming up with great ideas. I I feel like for the first time that um design is such an approachable concept and skill set to a lot more people and it brings together sort of people who have aspirations for design and wanting to build things, wanting to prototype things, putting beautiful stuff out in the world much much easier and uh faster. So uh Rio has gone through a lot of thinking and journey of you know um what design means what design means in the sense of having cursor being part of like the the building blocks of it like I I just really wanted to have him on the podcast and talk about uh the future of both coding and design.

**[00:02:23]** >> Rio Rio you've been at notion now obviously head of design cursor why don't you take us through your journey and how you've been thinking about some of these topics. I think to me it's like building software um there's like so many layers of abstractions and depth that you you need to take care of and in order to do something really great you actually need to know everything or like you assemble a team that works really well together with you know people with different strength on every layer. Maybe you have the greatest infer engineers, people doing ML. Uh maybe you have, you know, um really good design engineers who really like they can just handwrite CSS and then they'll be like perfect. Um in order for say one person to do all of this or learn all of this, it takes a long time of trial and error. You have to build from the simplest things to you know gradually more complex, scale it up to more people. um share your workout to the public, see what happens, do this feedback loop. And if you're doing it in a team, sometimes it takes even longer because say you're just a designer, you you're doing some mocks in Figma and then you shared it out, you got some feedback, then your PM needs to do this like PR thing and then run more meetings and then there's like more people involved and then they're like and takes a long time.

**[00:03:54]** and then maybe like a year later your design came out but then it's like 20% of what you wanted.

**[00:04:01]** But with this new thing to with cursor you can just say you have an idea it might be a little ambiguous you just tell it to tell the agent and then it might give you something maybe like 60% 70% uh on the first shot but you kind of kind of skipped a lot of the you know complexities.

**[00:04:29]** Um we kind of transformed from like you need to understand all this thing all these concepts of making software then you can do something to I can do something now and then I might get something that's maybe imperfect not exactly what I want but the process of iterating and like kind of poking at it becomes really quick and then as the agents evolve As the models get better, as it talks to more tools, it understands visuals better, it can talk to Figma, the mocks that I had, it can talk to notion, all the, you know, ideas, the docs, the the meeting knows anything.

**[00:05:16]** And the most important thing is it knows the codebase, which is the truth, the material of how we, you know, build software.

**[00:05:27]** So that kind of changes the whole thing.

**[00:05:28]** It's like the tool not only you know impacts the individual software engineers like for them maybe like for cursor like we kind of try to fit as many workflows and people as we can say there's like people who they pride themselves at like you know really think thoroughly write the most clean code for those people they can just type and then we do the tab thing and the tab got really good at like it's almost like it knows what you want to do next. Um so for those people they can do that but there's like increasingly more people doing the agent. Um where like even for the most professional coders they start to do this new thing.

**[00:06:18]** >> Yeah. >> Yeah. >> I am trying to think of even myself as a uh as example um prior to joining the firm I was on the product side. I was working with a lot of designing designers, uh, design engineering teams back then. It wasn't called that way.

**[00:06:33]** It's more like designers, front-end engineers, uh, and then, uh, UX designers too. Um, >> it was still a very disjointed workflow.

**[00:06:41]** It's like, you know, a lot of the the design work happens more in isolated fashion with just the designers themselves. Like >> they spend two weeks coming up with a concept.

**[00:06:54]** >> Yeah. what does the UI look like and work with design uh UX designers on what the UX look like and then hand it off to the product team and works with engineers. Figma already bring that sort of process a lot closer that you can collaborate around one artifact that everybody can give inputs and prototype and bring sort of more of a close to um uh the reality artifacts into into uh these people's hands. where with cursor it's even one step closer is you can actually poke around and play with uh these artifacts that are functional and working.

**[00:07:34]** >> I'm curious what does it mean for collaboration among these teams as you're >> mentioning um the collapse of that iteration >> um and and the speed um and also what is what does it mean for the different roles that's involved in design?

**[00:07:50]** >> Yes. So I think maybe like over the last I don't know 15 years or so I think the the art of making software fragmented a lot and then we kind of split into different roles each role kind of use their own tool you use their own artifact they think in their own kind of words and lingo say the designers are stuck in Figma before maybe it's like sketch their word actually like you know files and then the the PMs maybe they're like just writing docs and running meetings or maybe they're in Google Docs um and say the data people maybe like you know some other tool and then everyone's like kind of siloed in their own way and then we need to kind of come up with a process to tie everything uh or like build better tools to kind of unify everything. We tried that at notion but the problem is like people have like already developed like so much like habits there's like inertia to kind of change that or like change people's tools um or like kind of um like you can't really force anyone to like adopt something new.

**[00:09:10]** um that doesn't perfectly fit them. Um but with AI, with no uh with cursor, things kind of flip again cuz we want to kind of build something where it can kind of, you know, connect and absorb all of these artifacts um and formats.

**[00:09:34]** And later maybe even like within cursor like there could be different views of the same code like showing the code as raw code or like as is almost like just the very beginning.

**[00:09:49]** um the act of making software is really just modifying the code like in some sense like the PM writing the PRD is modifying the code but they're doing it through a more passive like organizational way maybe the designers influence it more on the visuals um but when you do this you know disjointedly there's so much like back and forth collaboration issues as you grow the team it gets even more complex.

**[00:10:19]** People start like breaking the software apart. Things are no longer simple, no longer unified. like we always talk about like you kind of ship your work chart type of thing and then the different roles kind of fight uh like designers are right the engineers are right the PMs are right but like you know there's this shared truth which is the code where like you know you can also gather a lot of information around putting everything synthesizing everything together um then the agent can kind of handle all these things that you might actually not know fully but it kind of you know knows the truth. It could know the present which is maybe like you know what's in your codebase what are the actual you know running tasks or projects even gathering fe feedback or information from the real world. It could be also like you know from the past say like all the knowledge that you've accumulated your team preferences your like how the codebase evolved in goods maybe there's also the future which is like say you're planning ahead you're like thinking about the the vision you're maybe like ideating some like bigger ideas you can actually do all of this with just one to one agent but it might you know for each individual user or team, it might take a different shape.

**[00:11:50]** And then like what we want is like there's like a base experience that almost works for anyone, anything, but you can get more specific um if you know what you're doing or if you have specific needs. You can even maybe you know use cursor as if you were using Figma at some point in the future. Um but the difference is you are not interacting with these siloed apps with their own like formats and then you don't have to do the conversion manually with meetings or whatever like it just does it. Then all you need to do is you're kind of thinking about the idea you're like iterating on it in whatever way that is the best for you. For the for the engineer, it might be like a code editor, but maybe for a designer is something more visual. For the PM, it might be something more like a document.

**[00:12:48]** >> That makes sense. I'm curious given that there's a lot more focus and emphasis on this concept of taste after AI comes about and now there's also this coworker that's an agent helping with >> writing code designing elements uh of the product. Where would the taste live?

**[00:13:10]** Where does that come from? Can you rely on >> agents for having good taste? Um, is that still heavily reliant on the creator that's the human designer or developer?

**[00:13:22]** >> I don't really like people talking about taste as a word because I think it's so ambiguous.

**[00:13:28]** >> Like how I see it is more like I think taste is kind of like there's a part of like you're selecting out of you know all the options. Um but in order to do that you have to kind of see everything or like you have seen it.

**[00:13:48]** You have maybe dug into the past. You have kind of figured out oh these are the ways people did this kind of thing.

**[00:13:56]** you made a connection of, you know, some some stuff from the past where you've seen in nature or, I don't know, some human made it or nature made it and then you kind of connected that to to your thing or the thing you want to do. Um, or you kind of over time build like a like a preference. It's almost like you're self- selecting a boundary of uh this is what is right, this is what is beautiful, this is what is good. Um and I think it's very different for each person. There is no right, there is no wrong. Um it's more dependent on say like the things that you've seen. It's almost like an LLM. But the problem with an LLM is like it actually has seen everything and it doesn't really have an opinion or like it kind of confused itself thinking that people prefer purple gradients everywhere.

**[00:15:01]** Um but what is good is like the LM because it has seen a lot of things. It can do the baseline really fast and really good. Then the thing on top is taste or like your self- selection of what is good like you're kind of drawing the boundary. That is your decision.

**[00:15:24]** Though the AI can increasingly help you do that. Say we have a new thing in cursor called plan mode. If you type in the prompt and then you don't really want to fill in the details, you can switch to plan go. it will kind of just build the spec for you and then you can add details, you can change it as you want. Um, >> yeah, >> but it's almost like I don't really believe in say you give the agent something longunning or like it's really like oluded like a really non-specific prompt and then expected to give you exactly what you want. like it's just not going to work. There needs to be something for the human to specify what is good, what is right, how I want to do it. If you don't put in that opinion, it will just produce AI slop.

**[00:16:21]** >> Yeah, you were alluding earlier to this sort of, you know, fight between product managers, designers, and engineers to or this sort of dance. um an engine of you were saying a few years ago the categories were somewhat different as there is this blurring um how do you think these categories will evolve um over the years?

**[00:16:44]** >> I think like people will always have their strength or their unique special skill or some spike.

**[00:16:55]** um say like some people are more good at coordinating, some people are good at the visual space, some people are maybe good at architecting like you know the lower level constructs. Um, but I I think of all of these people as just like like they're software builders or makers.

**[00:17:18]** Like we kind of started there like if you look back when so like the early computing era there was no title or people were maybe like researchers were like but they they maybe designed the low-level architecture they maybe even you know built the UI and how to display the UI on the screen and the whole thing maybe one person or two or five and when you did bad. And also I think back then there were like less say economic constraints where they were funded and they weren't like trying to make money as much. So they kind of made the whole thing really whole. And now it's like you kind of break everything down.

**[00:18:06]** You try to optimize them with like processes and cause optimizations and people's become like you know boxed into little areas and problem sets when the whole thing is actually all together.

**[00:18:26]** Um, and that causes a lot of problems I think like people people now make software that I don't know like they don't even think of like like there's some like ideal that's kind of lost and people think too much on the technical problems, the design problems, the money problems, not the whole thing or what we're trying to make better for people but you know we're kind of going backwards now as you know they say tools like cursor if you were you know self identified as a designer or developer or something like I used to also struggle with this I started like making stuff myself the whole thing and then I came to the US I got a job titled product designer I I stopped coding I made mocks and prototypes and I waited for them to happen for like years and they don't happen or like they ended up shipping as like a YouTube video.

**[00:19:39]** That's crazy. But, you know, with this new tool, a designer can build. they can actually like, you know, work on their craft, the the stuff that they really care about, make that really good and let the rest, you know, be handled by the agents.

**[00:19:59]** They can, you know, kind of put their taste on top and all the stuff that they don't want to worry about, give it to the agents.

**[00:20:12]** Um, but you can also assemble like a really good team. So like there's like really good in for engineers, front end engineers, PMs who are like I don't know not just running meetings get all of them together give them the same tool the same code base they can start covering each other's like you know weaknesses and then amplify their strength and the agent kind of holds everything and you know instead of you pinging this guy uh where is your design and knows.

**[00:20:47]** >> Yeah, that resolves a lot of um the common conflicts of spending more effort on the functional part of the software or spending more time on the >> artistic um aesthetic side of >> the the product itself and being appealing to the users. And you have worked at many of the very design focused design ccentric companies from notion to even prior to that Asana like now given sort of the democratization of who can touch that external facing um aesthetic part of the product. How do you think about influencing even I guess your current team and uh people at cursor to spend more effort in thinking about that versus just the functional part of the product itself?

**[00:21:39]** >> Yeah. Yeah. One thing I want to call out is design is not just about aesthetics.

**[00:21:43]** It is act like how I think of it is like it's all it's it actually includes all the say the architectural designs or like all the concepts of what this thing is or like the company say for notion as an example notion is a pure conceptual product meaning every single concept was designed by a person.

**[00:22:10]** So like in in notion it is really just blocks pages databases the workspace and then everything kind of works around these concepts and then at every layer there's like a representation of them there could be like you know at the very top is like the UI or like the brand or like the visuals the aesthetics but then there's actually the aesthetics every layer how you architect say like the front-end code and architecture how you know, how the reactive stays sync and how you render stuff to like how do you like store these objects, how they, you know, relate to each other to all the core concepts of the thing. And if you look at software, it's like it's actually really simple if you look at the concepts themselves. Um, so design is kind of like trying to figure out what is the best configuration and the simplest state for all of this.

**[00:23:09]** Some people maybe only focus on the visuals or the interactions or certain slices. Um, but I think the the beauty is actually putting things all together as well as you can. So I think it it is really about what I just talked about is like not seeing design as just should we use a six pixel border radius or four.

**[00:23:37]** Um but it's rather like how do I design the most simple system, fewest number of concepts, fewest code paths to do the most things for most people.

**[00:23:52]** You you guys obviously have incredible product market fit with developers. Can and we've alluded to a bunch of it, but can you share more about maybe either how you guys have navigated the idea maze of how you want to serve designers or just more around what what kind of tooling you you think there's an opportunity to provide?

**[00:24:10]** >> Mhm. Yeah. So, I think cursor like is still like our primary focus is on professional developers and teams. Um but because of that like people around them are already here.

**[00:24:30]** >> Yeah. >> And I think for the longest time we've been actually intentionally making cursor pretty hard to get in for say the nontechnical people. Um but they're are here now and they actually struggle to get in and they really want to get in.

**[00:24:48]** Um, one example is like when you open up cursor, there's like three buttons. It says open project, connect to SSH, clone repo or something. As a beginner or like a non-techno person, I can't understand any of this. Um, but what if say like we just kind of give you the agent view blank, you can just start doing things.

**[00:25:16]** Like there's a lot of little things we can kind of fix to just make cursor feel more friendly and welcoming for these people um who are like kind of engine people who are um maybe they know software concepts or certain layers but they might not be able to code. Um I want to make make sure that when they come in they can like without feeling overwhelmed or like feeling like ah this is like a code editor. It's an IDE. It is more like I can start doing things and as I start doing things um I can maybe like pick the path that I prefer. So like a designer maybe maybe they're just like kind of chatting with the browser next to it.

**[00:26:09]** Um as the agent is like making edits they can kind of preview the changes they can maybe like interact in the browser pick this element change like ah I want to swap this with something else and then boom it happens. Um so how we do it is not um say creating new products or splitting cursor that is the same thing but just like different preconfigurations and packaging of the same thing.

**[00:26:39]** Because like kind of like what I just said like thinking about the concepts like cursor itself is actually really simple or like AI agents in general are pretty simple.

**[00:26:52]** um what you want to do is actually like not um like if you look at I don't know like a chat GPT agent versus like a cursor versus like a replet a vzero a notion agent even the architecture or how they work or like they're almost the same.

**[00:27:13]** Um so what if we can come up with like a set of you know universal shared concepts for interacting with AI with agents with code with software but you can kind of mutate each each one to fit more people and to fit more use cases.

**[00:27:38]** Um, and then each of them can leverage say the best model to do this UI thing with the best view that fits me. I can configure it however I want. If I want to see everything, I can. If I don't want to see anything, I can too.

**[00:27:52]** This leads to my question of over the last few years um and I don't know if it's few years or a decade there is the concept of purpose-built tools for certain persona whether it's web flow for you know um persona or use cases like for landing pages >> vers um visero for more of the you know front-end developers building um building uh nextjs apps um there's tools for designers there tools handle from design to engineering >> where now there's more of a concept of >> the everything app chatbt is kind of everything app >> notion is kind of everything app uh you can go to it for your note takingaking but you can also publish notion pages cursor is becoming more of a everything app is a path that we're going down towards of having these all-encompassing apps that can do a lot more things that used to be captured by a single purpose app is there still place for purpose-built tools for a specific use case or persona. How do you see that?

**[00:28:55]** >> Yeah. >> Dynamic. >> I think it's just like different philosophies of doing things and making software.

**[00:29:03]** Um I think there's like almost like two ways you can look at the thing. There is this like the user centric human centered design path which is you know you start from a problem you identify the group of people who have this problem figure out you know what they want build really specific solutions for them versus like there's the more system angle to think about things where you're just kind of looking at the software itself, how it is composed and then think about where do I tweak a little bit to satisfy this constraint or to make this use case work or to enable this tool to work for these people.

**[00:29:57]** I think it's like fundamentally two different philosophies and then I think it is much easier to do the say the user centric uh way um but it kind of limits you from the beginning because when you start building these specific solutions they only work for those specific people. If you want to grow the people or you want to grow the use cases, you actually need to kind of tear apart everything you have your core concepts and a lot of people just can't do that.

**[00:30:35]** So what they do is instead of doing that they add more things, more concepts, more features and then there will be a point where this thing no longer serves your initial group of people anymore. The simple thing is no longer simple. the purposeful thing is no longer simple.

**[00:30:53]** And all of these purposeful apps, they're kind of selfish. They are siloing people, siloing workflows for file formats, creating islands.

**[00:31:07]** When if you look at the thing like all these purposeful app whatever like I also work at ASA asauna the core concepts are really tasks and projects everything around tasks and projects everything they add needs to work with those and that naturally limits what it can do versus say like notion like how we see notion it is not taking it is disguised as note takingaking Um like you come in you can start from a blank page you can type but then what you're doing is actually like you know blog pages databases and a workspace each block is almost like a JSON objects a page is just a array of JSON objects and then we render each block in the you know the layout and the type it is and then you can put them in a database. Now they have you know more properties they share more stuff there's more hierarchy and all pages can nest each other that is notion but then you can do whatever with it you can have a task project database they all work together they can be a list they can be a board do whatever you want but then the problem is you know for these more universal type of apps it's like because it's so open-ended it's kind of hard to get started that if I don't have the patience to kind of figure out how it works, I might not even get to the test and projects.

**[00:32:44]** So there's always that tension, but it is fixable.

**[00:32:50]** You can build better packaging, you can use AI. Um, so I think there's just like my personal uh preference is I would try to build something that works better for everyone than just ah this these people are the people we care about. I don't care about everything else and then I think they should use my thing. That's not how you do it.

**[00:33:19]** We talk about AI, we talk about agents and we talk about how it really um speeds up um building things and prototyping. But when it really comes to these type of you know helping users to understand a product better on boarding learning the new concepts also to you as a as a designer design leader um how does like interacting with AI really improves the usability utility of the product?

**[00:33:50]** Mhm. Yeah. I see AI almost like it's almost like a universal interface and then the the bare minimum of it is really just a prompt and then you get some response. Then you can kind of put this into like different forms. It could be like a little input like a chat box.

**[00:34:12]** Um it could be like a sidebar, you know, you see the chat. It could be maybe you select something, you can do stuff with it, but it could also say like you completely transform this layer. It's not chat. It's not like an input. It's more fitted to say it's more purposeful even. Um, but underneath it is still the same thing.

**[00:34:38]** It is still the same AI, same agent, same architecture, same like we can flip different models and prompts and stuff.

**[00:34:44]** And then fundamentally that that is what it is. But because of that you can actually build a lot of different layers and shapes. Then each person can find the shape that fits them and then it will feel more comfortable. Um but also there's always this like baseline thing which is it's just it's almost like Google like chat GPT is just a box. You can actually put whatever but there will be more specific tools that fit each person or each use case better.

**[00:35:18]** >> Does every software from now on becomes a chat box to begin with and what's the role >> of UX design plays in that?

**[00:35:30]** >> Yeah, I think like imagine um there is only chat.

**[00:35:38]** I think that will also be like a really bad experience because you know you stare at a blank and put you need to do something. You need to initiate the thing. You need to ask the right questions. Put in the right prompt. You might not know what kind of response you will get unless you play with this thing a lot. as a new person maybe like you know they might try it the first time they get something that doesn't feel like what they wanted and they're like ah this is not for me this is bad um but I think there's there's so much potential where like I think the models today can already do so much stuff for a lot of people for a lot of use cases we need to kind of design a mechanism to kind of help transform that input output into the form or format or views or workflows of the people you know today get them through that thing to hear instead of like forcing people to be ah now you need to use this tool and then you actually don't know how it connects with your current workflow you need to figure it out you don't really know what how it works it feels kind of scary ah what do I do you know versus like you actually ease them in through the thing they are used to. And I think those are actually the more optimal form factors for say the individual person or the use case itself cuz I I know like I I just don't want to like typing a question every time or ah it's give me like this wall of text of text response I need to like read versus say like uh your you know the lines that you autocomplete just appears you just press tab or like Maybe I just select some element in my artboard and say ah make four variants of it and boom it's there but underneath it's the same thing.

**[00:37:44]** >> On this question um I I I have um one more one more thought is um when when thinking about creativity a lot of times when you have more constraints and more guard rails it's actually more of a friend to uh to bring to creativity than not. Whereas now we have a much more open-ended world. We have a much more capable um tool that we can explore a lot more unconstrained domain and fashions.

**[00:38:13]** >> How do you still try to apply constraint I guess in your um line of work?

**[00:38:21]** >> Yeah. And how do you think the software itself now that we have uh this open chat window and chat box that can still brings that constraints in to give the builders >> more inspirations and creativity?

**[00:38:34]** >> Yeah, I think the biggest constraint is it's kind of like simplicity in a sense.

**[00:38:49]** Um meaning like there's a limit of how much concepts or things you can expose to any given individual at any given time for them to kind of figure things out.

**[00:39:07]** So there is a natural constraint on that side. For example, like on the cognitive side, there's maybe like a constraint on space. So like cursor the window you can stretch it like this or up. What if it's like this then you start reducing things where like you're kind of like prioritizing what to show what is the most important and then those things actually don't change that much or like it is really important to figure those things out and then you can kind of build a mechanism where you can kind of accommodate more things.

**[00:39:46]** say like there's secondary level things that maybe some people want to do. Maybe it's like more specific modes of operations or parts of the workflow.

**[00:39:56]** Maybe it is like um for different kinds of individual or preferences. Um but they are still like kind of layers of the core concepts or things. They're not kind of linearly like additive throw out all at all all at you at once.

**[00:40:21]** Um and I think the the the interface where how software manifests themselves or how we design even it will start becoming less about say the designer decides ah these are the buttons where they are and then it's like a fixed thing but rather it's like there's like shared concepts and shared me mechanisms of the same thing but it could say they take different forms where you can kind of expose ways for people to customize and make them their own. Um then it's like the designer what they're really thinking about is like what are the most important concepts? How do they relate to each other at every layer? Say like for 80% of people the defaults what should they be what should be the simplest state of this app or this thing what is the default for maybe like you can start forking it for different people and then it's like maybe at the second layer there's like you start exposing more like the power user features or the the different archetypes of what you can do but the default should still stay simple and then the ideal is like a lot of the tools um they don't really tell you what's going on or how the things work.

**[00:41:53]** Um one example is like you know most of the CLI coding agents today is like they kind of force you to use this tiny little window with this tiny prompt like that's almost like all the interactions you can do and then you're kind of delegating everything to the agent. you don't really know how things work versus for cursors like if you prefer something minimal I think it's fine you can do that but you can start digging into more things you can customize the agent you can make your own custom mode with like different model preferences and which tools I want which prompts I want you can pick like uh maybe like instead of viewing just code I want like a preview I want like a doc thing I want a browser I can change all the colors. Like it's all up to you. I can prefer the keyboard. I can prefer the mouse.

**[00:42:48]** And then the designers, what they're really doing is they're thinking of what is the minimal set of abstractions, the system to kind of handle all of these permutations.

**[00:43:03]** I love that concept of you're not just seeing the tool itself as a tool, but it's actually a toolbox where you can customize and configure it to fit your purpose and build your own tool >> um that you know fits uh your workflow and and give a ton of flexibility to to the end user. That's sort of the eos of cursor and notion that the more you unpack from the beginning, there's more to come.

**[00:43:29]** >> Yeah. >> Um >> there's more to play and tinker, >> right? because I think there's a lot of us who are actually really into that kind of stuff.

**[00:43:36]** >> For sure. Yeah. Rio, you have an impeccable taste and sense of design. Uh I'm very curious on your day-to-day life, how do you cultivate um your envir the surrounding environments, your own >> um surroundings uh to continue to find inspirations and bring the best design out to the world.

**[00:43:57]** Mhm. >> Are there things you do, practices you want to share with the audience?

**[00:44:04]** >> I don't really have like a routine or like it's kind of sporadic.

**[00:44:09]** Um like I don't sit in Figma all day and making mocks. Um, I like um it's like doing everything at once type of type of vibe. So like I might be thinking about a like longer problem.

**[00:44:32]** Um, I would maybe like just write. I like writing and kind of thinking in bullets.

**[00:44:42]** I'll like go out of the office on a walk and then take my phone with like a notion page and I'll just start writing.

**[00:44:54]** I'll make sketches. I'll maybe play individual space. I'll maybe like, you know, build a prototype and code. Um, a lot of my inspirations come from like not forcing it and kind of leaving some blank space to let things simmer.

**[00:45:24]** A lot of it comes from like just looking at stuff or look looking at everything, not just software.

**[00:45:38]** So like you can look at print design, graphic design, motion, films, music, art, anything that humans made. The nature side of things are really cool, too.

**[00:45:51]** Like learning about natural systems. I I have a biome major. So like there's a lot of similarities and like you know how many layers of things you can build, how they interact with each other. Um, looking at the past helps a lot. Um, so like my Rio OS project kind of started from like last year I was just like a b I bought a bunch of old Macs and iPods and I was just playing with them and I wanted to like kind of recreate the feelings. I actually really want to ask about that because a lot of you know designers profile page has the most >> shiny forwardlooking futuristic designs where you have like I don't know which year it is like a Mac OS >> interface with like the original version of iPod icon.

**[00:46:48]** >> Yeah. >> Yeah. >> Um tell us more about about the real OS project.

**[00:46:55]** >> Yeah. I started the thing um from so I was leaving notion and I make noises when I am in meetings. So like, oh no, we're it's all the same thing, stuff like that. And I wanted to make them a little gift. So I built like a soundboard app uh with cursor. It was just one app.

**[00:47:15]** Like it looked like really bad like Tailwind default styles. And then I just said, hm, what if we like made it more like retro Mac OS? And then it put it in like a almost like a more retro Mac OS type window basically like put it in the box and then I'm like add a menu bar and I add it on on top. Um then I'm like now I have a menu bar and a window. Why not just make more apps and more windows? And then that's how it kind of started. And then I just couldn't stop for like I don't know four or three months.

**[00:47:59]** >> Yeah. But a lot of the interfaces that I created I started from it's like it's kind of inspired from system 7.

**[00:48:10]** There is like accuracy but also like I added some like future stuff in it. Um and then I actually made like more themes. I added like a Mac OS 10 theme like the first Aqua theme. I added like Windows 95 and XP and then if you swap between them and you play with the OS it feels really authentic to each but then it's actually the same thing. So that's kind of like the the message I want to kind of tell people is like we've been almost doing the same thing over and over again from the very beginning but maybe given you know the technical constraints of each era.

**[00:48:53]** There's like just that's how it ended end ended there and how it ended how how it came to be.

**[00:49:02]** Um but we kind of carried a lot of these concepts and patterns over to even now and then we we are actually still living in it. Um and I don't think things will change that much. Meaning um there is these like timeless things that don't change much and like it kind of all comes back to people who are trying to come up with some really familiar ideas and then bringing them to like a new medium.

**[00:49:42]** But we're doing the same thing again with back in 1984 and now like people are just I don't know using paint to draw some pictures. There's like a text editor. You can type some stuff. There's like a you know different different concepts that we put in little pictures. The icons >> the desktop like none of that really changed.

**[00:50:10]** >> Yeah. the uh timeless uh concepts and and software we're using is the browser, the the player, the uh the chat windows and those are all on the on the real OS um project. So for the audience who want to check it out, it's at real.loo.

**[00:50:26]** >> Yes, os.real.loo. >> OS.real.loo.

**[00:50:31]** Awesome. We'll wrap there. Thank you so much, Rio, for for coming. This is awesome.
