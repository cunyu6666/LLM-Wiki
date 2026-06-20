---
type: note
description: "频道/作者：Griffin Wooldridge (@griffinwdesigns)"
timestamp: 2026-06-20
---
# How to Use Codex as a Designer

> **频道/作者**：Griffin Wooldridge (@griffinwdesigns)  
> **链接**：[https://www.youtube.com/watch?v=GOtHFZnagO0](https://www.youtube.com/watch?v=GOtHFZnagO0)  
> **时长**：16 分 43 秒  
> **发布日期**：2026-06-08  
> **观看/点赞**：34,030 / 1,016  
> **字幕抓取日期**：2026-06-20  
> **字幕来源**：YouTube auto-generated English  
> **段落数**：34

---

## 简介

Get 20% off your Mobbin subscription: https://mobbin.com/griffin

Designers are now one of the fastest-growing groups on Codex - and most videos won't tell you how to actually use it for design work. In this video I break down the full Codex workflow for designers: how to set up context so it stops generating generic output, how to use plugins (MCPs) and skills to shape the quality of what you get, and how to generate and iterate on a real UI from scratch. Then I give you my honest take on how Codex stacks up against Claude Code for design work.

**作者**：Griffin Wooldridge（设计师、内容创作者）。
**核心价值**：本视频是直接面向设计师讲 Codex 用法的实操指南——配套 MCP/skill 设置、context 工程、与 Claude Code 的对比。**与你 D20 演讲"设计师用 AI"主题直接相关**。

---

## 中文文字稿（带时间戳）

> 段落格式：`[时:分:秒] 文字内容`

**[00:00:00.000]** OpenAI 刚刚正式宣布 Codex 面向设计师开放。设计师现在是 Codex 增长最快的用户群体之一，OpenAI 也在持续推出插件、标注批注、可分享站点等功能——对于设计师来说，现在正是拥抱 Codex 的最佳时机。所以在这期视频里，我会手把手教所有设计师如何使用 Codex：怎么喂给它足够的上下文，让它别再吐出千篇一律的 AI 风格界面；怎么生成真正精致的 UI；以及如何在第一版基础上快速迭代，让它像一个全职设计师一样为你工作。

**[00:00:27.680]** 最后，我还会给你一个坦诚的对比——Codex 和 Claude Code 做设计到底谁强谁弱，因为这两个工具的差异，可能比你想的要大得多。好，我们开始。先简单交代一下背景：如果你只听过 Codex 这个名字，那 Codex 是 OpenAI 的编程智能体，可以跑在终端、IDE 里，现在还有了专属桌面应用。它能接收一个任务，然后自主执行——阅读你的项目、编写代码、自我检查，最后交付成果供你审查。背后最新的模型比如 GPT-5.5，就是专门为这类工作调优的：有适合快速任务的低延迟版本，也有适合复杂深度任务的更强版本。对设计师来说最关键的一点是：Codex 一开始是个开发者工具，但 OpenAI 刚刚确认，设计师、营销人员等非工程背景的用户已经占到 Codex 总用户的五分之一，而且增速是工程师的三倍。所以 OpenAI 正在针对这个群体大量开发新功能——面向你角色的插件、原地标注批注来精调结果的能力，以及可分享的交互式站点和应用预览。

**[00:01:23.840]** 也就是说，这不再是一个让你作为设计师用起来觉得格格不入的工具了。

**[00:01:27.840]** 它正在为你而构建。好，让我们在 Codex 桌面应用里正式开始。跟大多数 AI 工具一样，界面简洁直观。左侧边栏可以新建对话、搜索已有对话、浏览插件等等。你所有的项目——比如建网站、做应用——都列在这里，而对话部分基本就是你在 Codex 里进行的所有 ChatGPT 对话记录。现在，Codex 产出垃圾还是产出可用之物，最大的区别就在于你动手之前给它的上下文。如果你打开 Codex 直接说"给我做个仪表盘"，Codex 当然会给你做一个，但它完全不知道你想要什么样的仪表盘、什么风格，你几乎注定会得到一个跟所有 AI 生成界面撞脸的产物。解决办法是先做好三件事。第一，一个 agents.md 文件。

**[00:02:15.880]** 在 Codex 里开始新项目时，我建议你打开这个下拉菜单，悬停在"新建项目"上，如果选择"使用已有文件夹"，就可以指定一个工作目录。这意味着每次你给 Codex 发指令，它只会在该目录下检索上下文，不会扫描你整台电脑、翻无关文件、白白烧掉一堆 token。你可以看到我的目录里已经有一个 agents.md 文件了。我在 VS Code 里打开它给你看看里面的内容。把它理解为随项目携带的设计简报——你的设计惯例、组件规范、设计 token、该做什么不该做什么。Codex 每次执行任务都会自动读取它，所以你只需写一次，不用每轮对话都重复解释。这基本上就是你的设计系统在直接跟智能体对话。这只是一个示例 agents.md，但里面包含了一些有助于 Codex 理解上下文的板块。我告诉它我的视觉风格、色彩体系，甚至在文件下方放了一个示例色板，包含具体的色值。当然这些细节不是必须的，特别是如果你在一个全新项目上工作、没有需要遵循的设计系统，你可以在 agents.md 里写一些更通用的指导，Codex 会自己帮你梳理出一套设计系统和风格指南。再展示一下文件里的其他内容——我有排版规范，比如我要求始终使用干净现代的无衬线字体，像 Inter、SF Pro 或 Geist。我给了建议的字号阶梯，而且文件末尾这部分很重要——我告诉了它应该避免什么：高饱和渐变、玻璃拟态风格、过于花哨的卡片。所以在告诉智能体"该做什么"的同时，也一定要告诉它"不该做什么"。最后，把这个文件保存为 .md 格式，确保它放在你在 Codex 中的工作目录里就行。接下来第二个必要的设置步骤是插件。OpenAI 的插件就是你接入 MCP 服务器和技能集合的地方。简单解释一下 MCP 服务器和技能：MCP 服务器说白了就是让你的 AI 智能体能跟外部工具通信。比如我想让 Codex 读写管理我的 Slack，就可以接入 Slack 的 MCP 服务器——也就是 Codex 所说的"插件"。而技能呢，就是一组可复用的指令集，教你的 AI 智能体按你想要的方式工作。它跟 agents.md 类似，你可以在里面写关于希望智能体如何做设计之类的指导。Codex 里有一些 OpenAI 官方为设计师打造的实用插件。我要装的第一个是 Product Design 插件。

**[00:04:43.680]** 它包含 11 个不同的技能，能帮你探索更好的产品方向、审计用户流程、研究用户痛点，以及从真实 URL 出发做原型。其中我觉得特别好用的两个技能是 Product Design 技能和 URL to Live Code——后者能让你把互联网上的一个真实 URL 直接转成可以在本地运行的交互原型。我现在就把这个插件装到我的 Codex 里，就这样，装好了。另一个我强烈推荐你看的插件是 Figma 插件，尤其如果你已经在用 Figma 的话。这基本上是从 Figma 设计稿到真实代码最快的路径，你甚至可以让 Codex 直接在你的 Figma 文件里做设计。还有一个我最喜欢的插件是 Mobbin MCP 服务器。Mobbin 是一个设计灵感平台，收录了数十万个来自 Uber、Netflix、Apple 等顶级品牌的真实上线应用的界面截图。接入 Mobbin MCP 后，Codex 可以分析这些顶级应用中的成功设计模式，并应用到你的 AI 生成设计中。这样你的 AI 就不再是盲猜了。

**[00:05:45.360]** 如果你想开始用 Mobbin MCP，我会在描述栏里留链接。除了 Mobbin，我建议你把自己日常设计工作中用到的工具都接上。比如你们团队用 Linear 做项目管理，就试试接 Linear；用 Notion 做设计文档，Notion 也是好选择。去插件库看看，找到适合你的。插件就是打包了 AI 工作流和对应 MCP 配置的可安装包，你不需要每次手动配置。

**[00:06:11.760]** 第三步是使用技能。前面说过，技能就是一组 Codex 会遵循的可复用指令。通过 skill.md 文件，你可以教 Codex 怎么生成或编辑图片。你可以用 Skill Creator 创建自己的技能，写入你的设计规范和规则。也有一些跟设计更直接相关的现成技能。我最受欢迎的几个视频其实就是在讲技能的使用，如果你还没看过，强烈推荐你去了解一下设计师该怎么用技能。在这些视频里你会看到我这里已经装了不少技能，比如 Emil Kowalski 的 Design Engineering 技能、大名鼎鼎的 Front-end Design 技能，还有很多教 Codex 如何做更好设计的技能。所以在开始生成之前，我的准备工作是：一份扎实的 agents.md、适合当前项目类型的 MCP 插件，以及几个设计技能。整个设置流程就这么简单。

**[00:07:02.280]** 现在进入第一次生成环节。有了这些上下文打底，第一条提示词就能完成大部分工作。

**[00:07:07.560]** 在发第一条指令之前，我要特别说明一下——这次我用 GPT-5.5。它是 OpenAI 目前最新最强的模型，也是设计师的最佳选择。这个演示我把推理强度设在 medium，但如果你做更复杂的项目，可以考虑切到 high 或 extra high。当然这会消耗更多 token，但如果最终能用更少的对话轮次搞定，那就值了。我的第一条指令是："创建一个深色模式的投资仪表盘 UI，桌面端尺寸。包含仪表盘、交易、预算与目标、分析与报告、设置这几个页面。参考 agents.md 文件和附上的灵感图来打磨 UI。"

**[00:07:45.560]** 注意我提到了"附上的灵感图"。我的习惯是，尤其是第一轮，除了 agents.md 会被自动读取之外，再额外附一张你特别喜欢、想作为风格和整体设计参考的截图。需要注意的是，agents.md 里的规范和灵感图最好不要冲突——比如你在 .md 里写了要亮色模式，灵感图却是暗色的，这会让 Codex 困惑，结果可能不理想。好，这就是我的完整提示词了。最后我还想加上之前展示过的 Product Design 技能。我可以用斜杠命令调用——输入斜杠，打"product"几个字母，回车。现在 Codex 在构建 UI 时会调用这个技能。可以看到它找到了 agents.md 文件，并且把灵感图作为强视觉参考。注意看——如果 Codex 觉得信息不够，它会主动问你。它在问我：这应该是一个以静态精美 UI 为主、页面间可点击导航的原型，还是一个带功能筛选器、设置控件等的完整交互原型？

**[00:08:47.000]** GPT-5.5 足够强，所以我直接让它上完整交互原型。提醒一下，如果你做更复杂的项目，我建议一步步来，先让它把 UI 的视觉风格定下来。但这个投资仪表盘比较简单，我可以直接跳到原型阶段。现在它在构建过程中告诉我，Product Design 技能要求在完成前做一轮视觉 QA。因为我们用了 Product Design 插件，UI 构建完成后它会自动在浏览器中打开、截取屏幕状态，然后把明显偏离参考的地方收紧修正。这一步非常关键——让 AI 自己检查自己的产出，而且最好是视觉层面的检查。毕竟我们追求的是一个美观、好用、可用的 UI。在它还在构建的时候，我们已经可以预览它在写的文件了。

**[00:09:32.640]** 趁它在构建，我再介绍一下 UI 界面的细节——右上角有三个按钮。

**[00:09:37.800]** 第一个是固定摘要面板。

**[00:09:39.840]** 它展示你在本次会话中生成的所有产出，以及 Codex 参考过的所有来源。

**[00:09:45.400]** 你还可以调出底部面板。

**[00:09:47.080]** 这是你在 Codex 里可以使用的终端，右侧边栏则是文件浏览器/IDE。

**[00:09:53.800]** 好，6 分钟后，第一版仪表盘构建完成了，我们来看看。点击"在…中打开"，可以选择在 Codex 内置浏览器中查看（不用离开应用），或者用我更喜欢的外部浏览器。为了留在 Codex 里，我用内置浏览器。Codex 给我们生成了一个完整的仪表盘：Dashboard 页面顶部有四个 KPI 指标，一个大大的图表，还有几张卡片展示我的核心持仓和优先操作。看起来相当扎实。它很好地遵循了我给的灵感图和 agents.md 中的规范。

**[00:10:24.080]** 深色模式、圆角、绿色表示增长——到目前为止我没看到任何一眼 AI 味的设计痕迹。这就是因为我们做了前期设置、附了参考图。当然，第一版永远是起点，不是终点。接下来我教你怎么告诉 Codex 哪里需要改进，从而快速迭代设计。我注意到一个问题：这个图表没有 X 轴和 Y 轴的标签，完全看不出它在展示什么数据。我还希望有悬浮提示，鼠标移到折线某个位置时能看到精确数值。这正好是展示我最爱的 Codex 功能之一——标注批注——的绝佳机会。

**[00:10:59.080]** 这是一个新功能，使用方法很简单：点击上面这个按钮，就进入了标注模式。这意味着我可以选中屏幕上的任意元素，然后针对选中的元素写指令，不用费劲跟 Codex 解释"我说的是哪个元素"。我来标注这个图表区域，写："添加 X 轴和 Y 轴，清楚展示追踪的数值；同时为折线图添加悬浮交互提示。" 可以看到左侧边栏里它已经做了这些修改。不过有个要注意的地方——Codex 每次修改后你可能需要刷新内置浏览器才能看到变化。好，现在动态悬浮提示做好了，效果不错，但 X 轴和 Y 轴的标签明显有点错位。我再发一条后续指令让 Codex 修复。这其实是个典型案例——你同时让 Codex 做两件事，第一件事做得很好，第二件事就翻车了。

**[00:11:56.200]** 所以有时候，把指令拆成单独的多轮对话效果更好。我敢打赌，如果我用了 high 或 extra high 的推理模式，它第一轮就能把两件事都做对，只是会多消耗一些 token。我还想修的一个问题是第一排 KPI 和下面那排之间的间距。现在看起来只有几个像素，我肯定想把它拉大一些，跟这里的水平间距匹配。这种修改用标注功能也能轻松搞定。好，前面我们要求的是完整原型，所以除了仪表盘页面，还有其他所有页面。

**[00:12:31.960]** 交易页面，看起来相当扎实。预算与目标页面——我喜欢这里用不同颜色区分各类资金目标。分析与报告页面——可以看到同样的 X/Y 轴和悬浮提示也被应用到了这个图表上。最后还有这个设置页面。

**[00:12:47.680]** 还有一个我要检查的点：仪表盘是否做了响应式适配。肯定会有用户在手机上用这个仪表盘。

**[00:12:54.640]** 所以考虑移动端屏幕尺寸非常重要。在 Codex 里我们可以这样检查。

**[00:13:00.360]** 点击下拉菜单，显示设备工具栏，然后这个按钮可以在桌面和移动端视图之间切换。可以很明显地看到，我们的仪表盘完全没有做响应式。所有内容被挤成一团，左侧导航栏理想情况下应该折叠成汉堡菜单。这说明响应式不是默认就有的。你绝对应该在 agents.md 里或者第一条指令中就考虑到这一点。好，我现在这样告诉 Codex。

**[00:13:27.680]** "完全没有响应式。为移动端和平板设置完善的断点，并在每个屏幕尺寸下做视觉检查，确保完全响应式。" 注意关键点——我让它做视觉检查。意思是不要只看代码确认断点写没写，而是要实际看应用长什么样，这才是判断是否真正响应式的更可靠标准。好，Codex 刚完成了，我们刷新浏览器。

**[00:13:52.400]** 现在在移动端屏幕尺寸下，关键 KPI 变成了纵向排列，图表缩小适配屏幕，底部出现了导航栏。这说明了什么——你在 AI 智能体里做的每一个修改都可以通过自然语言完成，但有标注工具和桌面/移动端双尺寸预览这样的功能，会让一切方便得多。

**[00:14:12.880]** 如果我打开之前展示过的那个摘要面板——之前是空的——现在它列出了构成整个设计的 index.html 文件，以及我们正在运行的内置浏览器。还有一点值得了解，因为这是录制时的全新功能：Codex 现在可以构建交互式站点和应用，并给你一个可分享的链接。对设计师来说这是大事——做一个能跑的原型、一个作品集网站、甚至一个有真实功能的完整应用，然后发一个链接出去，而不是一个需要解释半天的 Figma 文件。

**[00:14:41.560]** 这个功能还很早期，目前只有企业版用户能用预览版，但值得关注。好，进入坦诚对比环节——如果你看过我的频道，你知道我个人非常喜欢 Claude Code，工作中也大量使用它，但你值得一个诚实的对比。

**[00:14:53.640]** 经过大量实际测试，规律是一致的。

**[00:14:57.360]** 纯视觉和 UI 工作，Claude Code 往往更强。它的第一版产出往往更接近可交付状态，把 Figma 设计稿转成代码时也能更好地保留原始设计结构。Codex 的原始 UI 输出则更偏向功能性和开箱即用的美感。

**[00:15:11.880]** 那么 Codex 对设计师来说到底赢在哪里？当你能写出一份清晰、详细的设计简报时，Codex 能精准执行。它的 token 消耗更低——如果你用 Claude Code 做设计时曾经一条指令烧掉十万 token，换 Codex 会好很多。它在同时启动多个任务然后回头审查方面也表现不错。而且前面说过，OpenAI 已经开始大量推出面向设计师的新功能，没有任何放缓的迹象，我非常期待后续。

**[00:15:41.400]** 说说我的真实看法。如果你想要最少配置下拿到最漂亮的第一版稿，选 Claude Code。我认为仅凭这一点，目前用 Claude Code 的设计师就比 Codex 多。

**[00:15:50.600]** 但如果你愿意做好前期设置——agents.md 文件、合适的技能和 MCP——Codex 能弥补大部分差距，而且会给你那种技术背景的人会更欣赏的编码精度。很多人，包括我自己，最终两个都用。Claude Code 做更偏探索性的视觉工作，Codex 做更偏技术的设计工作——尤其是涉及更复杂代码库的时候。当然还有那些新推出的设计师专属功能。核心教训就一句话：前期设置决定了产出质量。这就是本期视频的核心。以上就是 Codex 的设计师用法。你学会了怎么用 agents.md、插件和技能来提供上下文，怎么生成尊重你设计系统的 UI，怎么用标注和视觉反馈循环快速迭代。你也看到了跟 Claude Code 的坦诚对比，可以根据项目和流程选择合适的工具。如果你想让我做更多 Codex 相关的视频，评论区告诉我，因为每条评论我都会看。下个视频见，别忘了订阅，成为更好的设计师。

---

## 英文文字稿（带时间戳）

> 段落格式：`[时:分:秒] 文字内容`

**[00:00:00.000]** Open AI just made Codex for designers official. Designers are now one of the fastest growing groups using it, and Open AI is shipping plugins, annotations, shareable sites, and more, making it a super exciting time to be using Codex as a designer. So, in this video, I'm going to show all of you designers how to use it, how to feed it context so it stops spitting out generic AI output, how to generate a real polished UI, and how to iterate on that first pass so it's like having a full-time designer working for you.

**[00:00:27.680]** Then, I'll give you my honest take on Codex first Claude for design work because they are actually more different tools than you may think at first. Let's get into it. Quick context if you've only heard the name. Codex is Open AI's coding agent. It runs in your terminal, your IDE, and now a dedicated desktop app, and it can take a task and run it on its own, read your project, write the code, check its work, and hand you something to review. The newest models behind it, like GPT-5.5, are tuned specifically for this kind of work with a faster, low-latency version for quicker work, and a deeper one for heavier tasks. Here's the part that matters for designers. Codex started as a developer tool, but Open AI just confirmed designers, marketers, and other non-engineers are now about a fifth of all Codex users and are growing three times faster than engineers. So, they're shipping features aimed straight at that crowd. Plugins tuned to your role, ability to refine a result by annotating it in place, and a preview of shareable interactive sites and apps.

**[00:01:23.840]** So, this is no longer a tool you'll feel out of place when using as a designer.

**[00:01:27.840]** It's being built for you now. Let's get started in the Codex desktop app. Just like most AI tools, the UI is pretty simple and easy to navigate. You have your sidebar on the left where you can start a new chat, search your existing chats, browse plugins, and more. All of your projects, like building websites or apps, are listed here, while the chat section basically shows you all the chat GPT conversations you've had inside Codex. Now, the single biggest difference between Codex producing garbage and Codex producing something usable is the context that you give it before you build anything. If you open Codex and just say build me a dashboard, Codex will go ahead and build something for you, but it'll have no idea what kind of dashboard you want, what kind of styling you want, and you're almost guaranteed to end up with a UI that looks like every other AI-generated UI out there. The fix is to set up three things first. One, an agents.md file.

**[00:02:15.880]** When you're starting a new project in Codex, I recommend you open this drop down, hover over add new project, and if you choose use an existing folder, this is going to let you choose a directory to work in. This means that every time you send a prompt to Codex, it's only going to search for context within this directory. It's not going to scan your entire computer looking at irrelevant files and burning a ton of extra tokens in the process. Now, you can see inside my directory I already have an agents.md file. I've opened it in VS Code just to show you what's inside it. Think of this as the brief that travels with your project, your design conventions, your component patterns, your tokens, your dos and don'ts. And I've opened it here in VS Code just to show you what's inside it. Codex will read it automatically on every task, so you write it once instead of re-explaining yourself every prompt. This is basically your design system talking directly to the agent. Now, this is just a demo agents.md file, but it includes some sections that will be helpful for Codex to give it more context. I tell it my visual style, my color system, and down here I've even included an example color palette including hex values. Now, all this detail isn't essential, especially if you're working on a brand new project with no design system to adhere to. You can just include some more general instructions in your agents.md and Codex will figure out a design system and style guide and so on for you. Just to show you what else is in here, I have typography guidelines. For example, I always want to use a clean, modern sans-serif font like Inter, SF Pro, or Geist. I gave it a suggested type scale, and this part of the end of my file is important. I've told it what to avoid: bright gradients, glassmorphism style, overly colorful cards. So, on top of telling my agent what to do and what guidelines to to it's important that you also give it the don'ts. Now, you'll want to save this agent's file as a .md file and just make sure it's inside the directory that you're going to be working in in Codex. The next essential setup step before we start building is plugins. OpenAI plugins are where you access MCP servers and collections of skills. Quick word about MCP servers and skills for those who don't know what those are. An MCP server, to put it simply, just lets your AI agent communicate with outside tools. For example, if I wanted Codex to be able to read and manage my Slack, I could connect the Slack MCP server or as Codex calls them plugins. Now, a skill on the other hand is just a reusable set of instructions that teaches your AI agent to work the way you want it to. It's similar to your agents.md file in that you can include instructions about how you want your agent to design, for example. Now, there's a handful of useful plugins for designers inside Codex that are built by OpenAI themselves. The first one I want to install is this product design plugin.

**[00:04:43.680]** It's a collection of 11 different skills that enable you to explore better product directions, audit user flows, research user friction, and prototype from a live URL. A couple skills in particular that I think are very useful inside this plugin are the product design skill and URL to live code, which actually lets you take a live URL from the internet and turn it into an interactive prototype that you can run locally. So, I'm adding this plugin to my Codex right now and just like that I have it installed. Another plugin that I highly recommend you check out, especially if you already use Figma, is the Figma plugin. This is pretty much the fastest way to go from a Figma design to real code or you can even prompt Codex to design for you inside your Figma file. Now, one more of my favorite plugins is the Mobbin MCP server. Mobbin, if you haven't heard of it, is a design inspiration platform with hundreds of thousands of screens from real shipped apps from some of the biggest brands like Uber, Netflix, Apple, and many more. And with the Mobbin MCP, Codex can analyze successful design patterns in top apps and apply them in your AI generated designs. This way your AI isn't just guessing anymore.

**[00:05:45.360]** If you want to get started with the Mobbin MCP, I'll leave a link in the description. Aside from Mobbin, I recommend you just connect whatever tools you already use day-to-day for your design work. For example, if your team uses Linear for project management, try connecting this. If you use Notion for design documentation, this is a good one, too. Just go check out their plugins library and see what works for you. Plugins are simply the installable package that bundles the AI workflow plus its MCP setup. So, you're not configuring this by hand every time.

**[00:06:11.760]** Now, the third setup step for Codex is using skills. Like I said, a skill is just a reusable set of instructions that Codex will follow. Through skill.md files, you can teach Codex how to generate or edit images. You could use the skill creator to create your own skill with your guidelines, your design rules, but there's also a handful of skills more closely related to design. A couple of my most popular videos are actually about skills. So, if you haven't already seen those, I highly recommend you go check those out to learn more about how to use them as a designer specifically. In those videos, you'll see a lot of the skills that I already have installed listed here. Like Emil Kowalski's design engineering skill, the infamous front-end design skill, and quite a few others that teach Codex how to design better. So, before I generate anything, my setup is a solid agents.md file, having the right MCPs ready for whatever kind of design project I'm working on, and a few design skills. That's the entire setup process.

**[00:07:02.280]** Now, it's time for the first generation, and with all that context in place, the first prompt does most of the work.

**[00:07:07.560]** Right before the first prompt, I want to call out that I'm going to use GPT 5.5 for this generation. It's OpenAI's latest and strongest model, and by far the best one for designers. For this demo, I'm going to leave the reasoning on medium, but if you're working on a more complex project, that's when you might want to consider switching to high or extra high. This will, of course, use more tokens, but it's worth it if it means a smaller number of prompts in the end. The first prompt I'm using is create a dark mode investment dashboard UI at desktop dimensions. Include screens for dashboard, transactions, budgets and goals, analytics and reports, and settings. Refer to the agents.md file and the attached inspiration image as you craft our UI.

**[00:07:45.560]** So, note that I said the attached inspiration image. Something I usually do, especially on the first prompt, is on top of the agents.md file that it's going to read, give it a screenshot of a design that you really like and want to use the style and overall design of as inspiration. Keep in mind that ideally the guidelines in your agents.md file and your attached inspiration image don't conflict because, for example, if you say you want light mode in the .md file and then dark mode in the inspiration image, that's going to confuse Codex and you might not get a good result. Now, this is my whole prompt. The last thing I want to add to this prompt is that product design skill that I showed you earlier. I can run this as a slash command, meaning I just hit slash, start typing product, then hit enter. And now Codex is going to invoke that skill as it starts building our UI. We can see that it's found the agents.md file and it's referencing the inspiration image as a strong visual target. Now, check this out. If Codex feels like it's missing any information from you, it'll tell you. It's asking me if this should be mostly a static, polished UI with clickable screen navigation or a fully interactive prototype with functional filters, settings controls, and more.

**[00:08:47.000]** GPT-5.5 is so powerful that I'm going to tell it to go straight to the fully interactive prototype. Here's the thing, if you're working on a much more complex project, I recommend that you take baby steps and have it just decide on the look of the UI first. But for this investment dashboard, I'm comfortable going straight to the prototype. Now, as it's building, it tells me that the product design handoff wants a visual QA pass before I call this done. Now, because we're using the product design plugin, after it builds the UI, it's going to open it itself in browser, capture the desktop state, and tighten anything that visibly drifts from the reference. This is a pretty essential step that you have AI do, check its own work, and ideally check its own work visually. Because after all, what we're trying to achieve is a beautiful, functional, and usable UI. Now, while it's still building, we can already review the file that it's writing to.

**[00:09:32.640]** Now, to give you a little more detail about the UI while it's building, we have three buttons in the upper right.

**[00:09:37.800]** This first one prompts a pinned summary.

**[00:09:39.840]** It shows whatever outputs you've created during the session and any sources that it's followed to build those outputs.

**[00:09:45.400]** You can also bring up a bottom panel.

**[00:09:47.080]** This is your terminal that you can use inside Codex and a right sidebar, which is basically your file explorer or IDE.

**[00:09:53.800]** Now, after 6 minutes, it's built the first version of our dashboard, so let's check it out. If I hit open in, I can either view it in the Codex browser without even leaving the app or my preferred external browser. For the sake of staying inside Codex, I'm going to use the in-app browser. We have a full dashboard produced by Codex. We have this dashboard page with four KPIs at the top, a huge chart right here, and a couple cards showing my top holdings and priority actions. It's looking pretty solid. It adhered to the inspiration image I gave it pretty well along with the guidelines in the agents.md file.

**[00:10:24.080]** Dark mode, rounded corners, green to indicate growth, and so far I'm not seeing any design patterns that scream AI-generated. That's because we went through that setup process and attached a reference image. The first generation is, of course, a starting point, never the finish. So, here's how I teach Codex what it can improve on so that I can iterate on my design fast. One thing I'm noticing is that this chart doesn't have any X or Y values, so I really can't tell what the graph is conveying or measuring. I also wish there were tooltips here so that I could hover over a certain part of the line and see the exact value at that point. So, this is a great opportunity to show you one of my favorite features in Codex, annotating.

**[00:10:59.080]** This is a newer feature, and to use it, all I have to do is click this button up here. And just like that, I'm in annotating mode. What this means is I can select any element on the screen and write a prompt targeted at that element that I've selected. This keeps you from having to explain what element you're talking about when you prompt Codex. So, I'm going to annotate this chart area and say, "Add X and Y axes that clearly convey what values are being tracked, and then also add interactive tooltips upon hover of the line graph." Now, we can see in the left sidebar that it's made those changes. Now, the thing that might throw you off about Codex is you'll likely have to refresh this Codex browser every time a change is made to see those changes live. So, we have this working dynamic tooltip now, that's looking great, but the labels in the X and Y axes are clearly getting a little bit distorted. So, I'm going to give a follow-up prompt telling Codex to fix this. This is actually a great example of you telling Codex to do two different things at once and nailing the execution of the first thing, but then butchering the implementation of the second thing.

**[00:11:56.200]** So, sometimes you're better off giving Codex these instructions in individual prompts. I'm willing to bet that if I was using a higher reasoning mode like high or extra high, it would have gotten the execution right on the first pass at the cost of using more tokens. Something I would also want to fix is the spacing in between the first row of KPIs and the next row below it. There only seems to be a couple pixels of spacing in between and that's something I would definitely want to bump up a bit to match this horizontal spacing here. And this is yet another fix you could easily make with that annotation feature. Now, like you saw in the beginning, we asked for a full prototype. So, we have the dashboard page, but then we also have all the other pages included, too.

**[00:12:31.960]** Transactions, which is looking pretty solid. Budgets and goals. I like the colors being used here to differentiate each type of funding goal. Analytics and reports. And we can see it's applied those same X and Y axes and tooltip to this chart, as well. Then we also have this final settings page.

**[00:12:47.680]** Now, one more thing about my dashboard that I want to check is whether it's responsive or not. I would definitely have mobile users using this dashboard.

**[00:12:54.640]** So, taking mobile screen sizes into consideration is super important. Here's how we can check for that in Codex.

**[00:13:00.360]** Click this drop-down, show device toolbar, and then this button right here is going to switch our view from desktop to mobile. And we can clearly see that our dashboard is not mobile responsive whatsoever. All the content is just getting absolutely smooshed, and the left side navbar should ideally get collapsed into a hamburger menu. So, this just shows you that you don't get mobile responsiveness by default. And this is something you should definitely consider including in that agents.md file or just in your first prompt. So, here's what I'm going to tell Codex now.

**[00:13:27.680]** It's not responsive at all. Set up robust breakpoints for mobile and tablet and check your work visually at each screen size to make sure it's fully responsive. Now, here's the important thing. I'm telling it to check it visually. This means don't just review the code and make sure those breakpoints are technically there. See what our app looks like because that's a much better indicator of whether the app is actually responsive or not. Now, Codex just finished, so let's refresh our browser.

**[00:13:52.400]** And now from that prompt at mobile screen size the key API is stacked vertically, the chart shrinks to fit the screen size, and we have this bottom navbar for navigation. So, this just shows you that every change you want to make in these AI agents can be done through natural English, but it makes it more convenient having tools like annotation and seeing your designs at both mobile and desktop screen sizes.

**[00:14:12.880]** Now, if I open the summary panel that I showed you earlier when it was empty, it's now listing this index.html file that's making up this whole design and the in-app browser that we have running right now. One more thing worth knowing because it's brand new at the time of recording. Codex can now build interactive sites and apps and give you a live URL so you can share them. For a designer, that's a huge deal. Spin up a working prototype, a portfolio site, even a full app that has real functionality, and send a link instead of a Figma file that needs explaining.

**[00:14:41.560]** Still early and right now it's only available in preview for business users, but keep an eye on it. Now, the honest part because if you've watched my channel, you know that I love Cloud Code personally and use it a lot for my work, but you deserve an honest comparison.

**[00:14:53.640]** Across a lot of real-world testing that I've done, the pattern is consistent.

**[00:14:57.360]** For pure visual and UI work, Cloud Code tends to win. It's first pass is often closer to shippable, and it preserves more of the original design structure when converting a Figma design. Codex's raw UI output tends to lean more functional and beautiful out of the box.

**[00:15:11.880]** So, where does Codex actually win for a designer? Well, when you can write a clear detailed brief, Codex can execute it exactly. It's leaner on token usage, so if you've ever used Cloud Code to design and ended up burning through 100,000 tokens in one prompt, this is something you'll probably experience less of using Codex. It's pretty strong at kicking off several tasks and then reviewing them later. And like I said before, OpenAI has started shipping a ton of new features targeted toward designers. There's no sign of them slowing down anytime soon, so I'm very excited to see what else is coming.

**[00:15:41.400]** Here's my honest take. If you want the prettiest first draft with the least setup, go for CloudCode. I think for that reason alone, CloudCode is used by more designers than Codex at this point.

**[00:15:50.600]** If you're willing to do the setup with an agents.md file, the right skills, and MCPs, Codex closes most of that gap and gives you that coding precision that more technical folks will appreciate. A lot of people, myself included, end up using both. CloudCode for more exploratory visual work, Codex for more technical design work that involves a more complex code base. And of course, the new designer features that are being shipped. The setup beforehand is what makes the main difference. That's the main lesson of this video. So that's Codex for designers. You saw how to give it context with an agents.md file, plugins, and skills, how to generate a UI that respects your design system, and how to iterate fast with annotations and the visual loop. And you got the honest comparison against CloudCode, so you can pick the right one depending on your project and workflow. If you want me to make more videos like this on Codex, let me know in the comments because I read every single one. I'll see you in the next video and don't forget to subscribe to become a better designer.

---

## 关键节点索引

| 时戳 | 内容摘要 |
|------|----------|
| `00:00:00.000` | OpenAI 正式宣布 Codex 面向设计师开放，设计师是最快增长的用户群体 |
| `00:00:27.680` | Codex 与 Claude Code 的差异比想象中大，将做坦诚对比 |
| `00:01:23.840` | Codex 不再是设计师用着格格不入的工具，OpenAI 正在为你而建 |
| `00:01:27.840` | Codex 桌面应用界面介绍；产出质量的关键在于上下文 |
| `00:02:15.880` | 第一步：创建 agents.md 文件——随项目携带的设计简报 |
| `00:04:43.680` | 第二步：安装插件——Product Design 插件（11 个技能）、Figma 插件、Mobbin MCP |
| `00:05:45.360` | 接入日常使用的工具（Linear、Notion 等），插件是打包好的 AI 工作流 |
| `00:06:11.760` | 第三步：使用技能（Skills）——可复用的指令集，教 Codex 如何做设计 |
| `00:07:02.280` | 设置完毕，进入第一次生成环节 |
| `00:07:07.560` | 使用 GPT-5.5 + medium 推理，发出第一条指令：创建深色模式投资仪表盘 |
| `00:07:45.560` | 附上灵感图作为视觉参考，调用 Product Design 技能 |
| `00:08:47.000` | 直接生成完整交互原型；Product Design 插件自动做视觉 QA |
| `00:09:32.640` | Codex 界面详解：摘要面板、终端、文件浏览器 |
| `00:09:37.800` | 摘要面板展示会话产出和参考来源 |
| `00:09:45.400` | 底部面板和右侧边栏 |
| `00:09:47.080` | 终端和文件浏览器/IDE |
| `00:09:53.800` | 6 分钟后第一版仪表盘完成，效果扎实，遵循灵感图和 agents.md 规范 |
| `00:10:24.080` | 深色模式、圆角、绿色增长标识——没有 AI 味；第一版是起点不是终点 |
| `00:10:59.080` | 标注批注功能：选中元素精准下指令，添加坐标轴和悬浮提示 |
| `00:11:56.200` | 同时做两件事容易翻车，建议拆成单独指令；高推理模式可改善 |
| `00:12:31.960` | 浏览所有页面：交易、预算与目标、分析报告、设置 |
| `00:12:47.680` | 检查响应式适配——肯定有移动端用户 |
| `00:12:54.560` | 移动端屏幕尺寸考虑至关重要 |
| `00:13:00.360` | 设备工具栏切换桌面/移动端视图——仪表盘完全没有响应式 |
| `00:13:27.680` | 指令：设置断点并做视觉检查，确保完全响应式 |
| `00:13:52.400` | 移动端适配完成：KPI 纵排、图表缩放、底部导航栏 |
| `00:14:12.880` | 摘要面板更新；Codex 新功能：可分享的交互式站点和应用 |
| `00:14:41.560` | 分享功能尚处早期预览，仅企业版可用 |
| `00:14:53.640` | 大量实测后的规律一致 |
| `00:14:57.360` | 纯视觉 UI 工作 Claude Code 更强，第一版更接近可交付 |
| `00:15:11.880` | Codex 的优势：精准执行详细简报、token 消耗更低、多任务并行 |
| `00:15:41.400` | 真实看法：要最少配置最漂亮的第一版，选 Claude Code |
| `00:15:50.600` | 做好设置后 Codex 能弥补差距；两个都用是最佳策略 |
