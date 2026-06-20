---
type: note
description: "频道/作者：Kyle Skelly"
timestamp: 2026-06-20
---
# Turn Claude Code into a Design GENIUS

> **频道/作者**：Kyle Skelly
> **链接**：[https://www.youtube.com/watch?v=fVPCbCH_c1c](https://www.youtube.com/watch?v=fVPCbCH_c1c)
> **时长**：9:09
> **发布日期**：2026-05-28
> **字幕抓取日期**：2026-06-20
> **字幕来源**：YouTube 自动生成字幕（en）
> **段落数**：17

---

## 信达雅中文翻译

> **作者**：Kyle Skelly（设计师、教育者）
> **翻译**：AI 译校 · 信达雅风格

今天这期视频，我来教大家怎么把 Claude Code 变成一个顶级设计师和策略师。方法是接入 Mobbin 的 MCP。这套工作流极其强大，你们一定要看。

先介绍一下 Mobbin——它是互联网上最大的 UI 合集之一，收录了各大公司的界面设计。Booking.com、Duolingo、Disney+、Tesla，各种 App 应有尽有。点进去不只是单个界面，而是从 UI 元素到完整用户流程的全套设计，非常全面。这是了解竞品做法、学习最佳实践的绝佳途径。资源覆盖 iOS 应用、Web 应用、落地页，全都是一线水准的高绩效设计——灵感宝库。

假设客户找你做一个新 App 设计。你列出 MVP 需求，构思整体方案。通常我会先看同类 App 怎么做——哪些好用、哪些不好用。Mobbin 的强大之处在于你可以按品类搜索。比如健身 App，你可以看 Tonal 获取灵感。但更有价值的是用户流程——你自己的 App 设计可能不同，但健身 App 之间的流程大同小异。

比如这里能看到某个 App 完整的注册引导流程。你可以逐个查看、复制，然后在 Figma 里拼成情绪板。不过更高效的方式是用 Mobbin 的 MCP。去 mobbin.com/mcp，安装很简单：需要 Mobbin 付费账号，选你的工具（这期用 Claude Code，也支持 Cursor、Codex、v0 等），在 Claude Code 设置里添加自定义连接器，输入服务器地址 `api.mobbin.com/MCP`，连接并授权即可。

连好之后，你可以问它："连接 Mobbin MCP，告诉我它能做什么。" 它能帮你找 UI 模式（比如"找几个健身 App 的注册引导流程"）、跨 App 对比设计、自动收集参考素材，甚至直接导入 Figma 文件。

本质上你给 Claude Code 装上了超能力——它能访问 Mobbin 超过 60 万个全球顶级 UI。

我的提示词："我在做一个健身 App。从 Mobbin 里找 10 个不同 App 的注册页面，生成一个 Figma 文件，做成情绪板。" 顺便说一下，我也通过 MCP 连了 Figma，所以它能直接创建 Figma 文件。

它帮我们自动从 Mobbin 整个库里搜索、筛选、生成文件。整个过程省去了手动逐个复制粘贴到 Figma 的大量时间。

然后我让 Claude Code 像设计师一样思考："你觉得这些里面哪些做得最好？为什么？有没有非健身类的 App 也能作为灵感来源？" 又问："把非健身 App 的欢迎页也找来，把你的分析和建议一起放进 Figma，按逻辑整理好。"

结果像变魔术一样出现在 Figma 里。它给出了详细反馈和分析：Strava 的社区信号最好——真实用户而非模特，橙色 CTA 保持高对比度；Gymshark 品牌感强——大写字母标题、运动员抠图、单一明确的行动按钮，没有给犹豫用户的退路；Peloton 被评为整体最佳——深色电影感照片、三个社交登录紧凑排列、品牌与产品一帧呈现、几乎零摩擦。我未必同意"最佳"，有点花哨了，但确实不错。

它还总结了制胜规律：展示真人而非吉祥物、减少摩擦但别冷冰冰。还推荐了非健身类的参考——克制就是教训，展示了极简风格和紧迫感两种方向。

然后我说："基于这些案例和 Mobbin 上的最佳实践，用 iPhone 16 画布，生成我们自己的概念稿。" 它根据所有反馈自动生成了这个。显然我们还没给具体的 App 信息——定位、功能、目标人群——但作为灵感起点和粗略原型已经非常棒了，因为流程经过了全球顶级 App 的验证。加一张全屏背景图，就已经像个打磨过的欢迎页了。

这就是把 Claude Code 和 Mobbin 连接起来当你的设计搭档和策略师——帮你做大量调研、整合信息、集中呈现。你作为设计师来审核、判断哪些同意、哪些不同意。至少你面前有了丰富的素材，是一个极佳的起点。

另一种用法是让 Mobbin MCP 帮你评审设计。我拿自己即将上线的课程落地页来试——把设计稿导出，发给 Claude Code，让它跟 Mobbin 上的落地页做对比，给出反馈。本质上是让它"烤"我一遍。

提示词："给我的课程落地页详细反馈。用 Mobbin 的落地页库做对比，找到更好的参考，按照 Mobbin 上的高端设计标准来评审我的设计。"

它告诉我哪里不行。从 Mobbin 拉了参考图，给出详细点评：色彩体系协调且跟得上潮流，但 Hero 区域尺寸不够——"我们目前差一个档次，不是品味问题——品味不错——而是布局比例和节奏。" 然后逐节反馈：Hero 部分主要讲尺寸和措辞，给了 Mobbin 上的参考——标题超大加粗、极度聚焦、或者加色彩。视频预告部分有点脱节。说实话，所有反馈都很有道理，而且能快速点开参考看它说的是什么——太有用了。

它甚至问我："要不要我在 Figma 里做一个修改版的 Hero 并排对比？" 虽然我现在不点，但这个选项本身就够疯狂了。

如果你们想试试这套工作流，强烈推荐。描述栏有 Mobbin 的注册链接。如果你想成为更好的 AI 辅助设计师，也欢迎报名我的课程。下期见。

---

## 英文文字稿（带时间戳）

> 段落格式：`[时:分:秒] 文字内容`

**[00:00:00]** In today's video, I'm going to show you guys how to turn Claude code into a master designer and a strategist. To do this, we're going to be connecting Mobbin using an MCP. And honestly, this workflow is so incredibly powerful, you guys are going to want to see this.

**[00:00:12]** >> [music] >> Okay, so if you guys aren't familiar with Mobbin, Mobbin is one of, if not the biggest collection of UIs from across the internet, across all the biggest companies out there. So, you can see here all the different apps. We have like booking.com, Duolingo, Disney Plus, Tesla. And if we click into one of these, you can see that it's not got just one, but it's got all sorts of different screens. It's got everything from UI elements all the way down to certain flows within the app. It's very, very comprehensive, and I think it's one of the best ways to see what other companies are doing out there, see what works. So, if we go up here, they've got everything from like iOS apps. They've also got web apps, and then they've also just got websites as well, like landing pages. But, all the stuff on here is kind of the top of the top, and these are generally just high-performing websites, so a great source of inspiration. So, let's just say a client comes to you and they need a new app design. You write down everything they need for their MVP, and you get an idea of how you're going to bring this all together. Generally, for me, I'll jump into similar sort of apps, things that are doing similar sort of things. How do they do it? What works? What doesn't?

**[00:01:16]** And that's where Mobbin is incredibly powerful cuz you can search by like categories. Well, let's just say it's a fitness app. Well, you could look at something like Tonal, and you can get a lot of inspiration. But, further than that, like what I said, the flows are where they can be really powerful. Cuz your app itself might differ in design, but the flows from one fitness app to the other probably be kind of similar.

**[00:01:35]** So, here we can see the entire onboarding flow for this app. You can go into each of these and just copy it, and then within Figma, we can just start pasting these in to build out a mood board. Now, there's a much better way of doing this using Mobbin's MCP, and I'll show you guys how to connect it. So, if we head to mobbin.com/mcp, now installing it is quite easy. So, you can see here the setup. So, first you need a paid plan to Mobbin, and then you can pick your tool. So, we're going to use Claude Code in this video, but you can also connect it to Cursor, Codex, V 0, or other. So, to install this, we will open Claude here, and we'll go down here to customize, and then we'll go to connectors. If we click on this plus icon, we'll do add custom connector, and then here we want to type Mobbin, and then for the server URL, we want to use this one here, api.mobbin.com/ MCP, and then we'll add this. You can see here it's not connected yet, so we'll click connect, and then we will just authenticate this just like this.

**[00:02:30]** So, now we've got it all connected. We could say, "Connect the Mobbin MCP and tell me all the things I can use it for." Here is what the Mobbin MCP lets you do. So, it can help you find UI patterns. So, you could tell it, for example, "Find me some fitness onboarding flows." You can compare designs across different apps, gather references for a feature we're designing. This is like what we already did here, but we can get this to do this automatically for us, and even bring it into a Figma file. Target specific platform to insert, get inline previews.

**[00:02:57]** We've essentially given Claude Code superpowers cuz it now has access to Mobbin's selection of over 600,000 of the world's best UIs. So, we're going to give it this prompt here. "I'm working on a fitness app. Generate me a Figma file with 10 different examples of different apps from Mobbin and their initial sign-up screen. Make me a mood board." Just so you know as well, I also have Figma connected via the MCP, so this allows it to make a Figma file and connect it with Figma, too. If you didn't have Figma connected, well, you could see that it would just pull it into the chat anyway, but we're going to get this to bring it over for us directly into Figma. And this is what it's given us. So, these are all the different screens that we've gotten from Mobbin. We allowed Claude Code to be able to search Mobbin's entire library to create this file for us automatically. So, as a source of inspiration, automating this whole entire process is incredibly useful. So, So, meant that we could save a lot of time instead of having to go into each of these and then copying and pasting these over at Figma ourselves. So, let's say this to Claude code, can you tell me what seems to work best between all of these and why? We're going to get Claude code to think like a designer here. Are there any other non-fitness apps on Mobbin that could be additional source of inspiration for this screen? Maybe we need some inspiration from one or two non-fitness apps that have a similar sign-up screen. And let's grab some of the welcome screen for non-fitness apps, too. We're going to say, add this into Figma with your feedback of what works and what doesn't. Add your analysis and organize accordingly. And then we now have this generated as if by magic over in Figma. It's given us detailed feedback and its analysis of all these different screens from Mobbin. So, you can see down here Strava and Gymshark and Peloton seem to have the best sort of flow. And the feedback for Strava, for example, is like best community signal, real people, not models, instantly tells you the app's social DNA, orange CTA stays high contrast.

**[00:04:45]** Now, I agree with all of that. Gymshark, strong brand voice, confident caps in the headline, cut out athletes, single back call to action, no soft path for hesitant users. You've got one button, it's very clear what you should do.

**[00:05:00]** Peloton is saying it's the best overall.

**[00:05:02]** We've got a dark cinematic photo, tight stack of three social sign-ins, logo overlay, brand, product in one frame, near zero friction. I wouldn't necessarily say it's the best overall. I think it's actually a little bit busy, but it is good. Then further down here, we have more of an analysis. The winning pattern, show people, not mascots, reduce friction without going cold. And then here we have other non-fitness references that are worth borrowing things from. Restraint is the lesson.

**[00:05:29]** This is showing you a very minimal approach. Depending on what we're building, this could be the best choice.

**[00:05:33]** And then we have this one here, which is showing just a kind of sense of urgency.

**[00:05:36]** Now, we're going to say, generate me our own concept for our own one now using these examples and other common practices from Mobbin. Also, use our analysis of what works best use iPhone 16 frame. And this here is what it's built us automatically based on all the feedback of what we've gathered here from Mobbin. Now, obviously, we haven't given it any specific info about our fitness app, what makes it different, what it's supposed to do, who the demographic is, but just as a source of inspiration and getting a rough sort of mock-up, it's already done all of these things for us and this is a great starting point because we know that the flow of this is all tried and tested with the biggest apps in the world. But you can see that if we added like a full-screen image to the back of this, this would already start looking like somewhat of a polished welcome screen.

**[00:06:24]** So, that's one great way of connecting Claude Code and Mobbin to be your design partner, your strategist, to do a lot of the research for you, collate that information, bring it into the one place, and then you as the designer is to review it all and decide if you agree with some of it or disagree with some of it, but at the very least you've got a lot of stuff in front of you and it's a really useful starting point. Another way you could use Mobbin's MCP with Claude is to critique your designs. Now, we're going to do this with a landing page of my upcoming course, Future Designer. We're going to send this to Claude Code and we're going to get it to review it. It's going to compare it with other landing pages on Mobbin and give us its feedback. So, it's going to roast me essentially, but let's see what it comes back with. So, this is the design of the landing page here in Figma. We are just going to export this and then I'll pull this over into Claude Code.

**[00:07:13]** Give me a detailed feedback on my course landing page. Use comparisons from Mobbin's library of landing pages. Find me better examples for sections and overall critique my design in line with the premium designs that are on Mobbin.

**[00:07:27]** All right, so here's when Claude Code tells me that my design sucks. So, it's pulled together some reference images from Mobbin and here's its detailed critique. The color system is cohesive and on trend. The hero is undersized for what it's trying to do. Currently, we're sitting one tier below premium because the layout proportions and pacing. Not taste, the taste is good. Well, that's that's fine. Then we've got detailed feedback about each section. Hero, it's talking mainly about the sizing and the voicing, and you can see it's given us some references here here on Mobbin. You can see that their headline super bold, and then this is super focused. We've also got this one where it's talking about maybe adding some color to our headline. And then this one which is mainly talking about just the actual size of the headline, which this is huge here. If anything, I think this is maybe a little too big. Trailer video seems a little disconnected. It's giving us this reference here. Obviously, you can see the trailer is a big part of this hero here. It's not really what I wanted to do for mine. Other example here for this, well, it's probably like a very high converting landing page, but I think it's a little bit boring. But honestly, all the feedback totally makes sense. And honestly, being able to just quickly click into these references and see what it's talking about. So useful.

**[00:08:40]** And it even asks me, "Want me to mock up a revised hero in Figma as a side-by-side comparison?" Which I'm not going to do right now, but it's insane that that is even an option. If you guys are interested in trying out this workflow for yourself, I highly recommend it. There's a link in the description so you could sign up to Mobbin. If you want to become a better AI assisted designer, then sign up to my upcoming course, and I will catch you guys soon with another video.

**[00:09:05]** Bye.
