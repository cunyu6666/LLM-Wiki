# Designing with Claude: From prompt to production

> **演讲者**：Dan Carey（Anthropic Lab 产品经理）  
> **频道**：Claude (@claude)  
> **链接**：[https://www.youtube.com/watch?v=Uvl-tRga98g](https://www.youtube.com/watch?v=Uvl-tRga98g)  
> **时长**：28 分 0 秒  
> **发布日期**：2026-05-22  
> **观看/点赞**：95,445 / 1,849  
> **字幕抓取日期**：2026-06-20  
> **字幕来源**：Groq Whisper API (whisper-large-v3-turbo) — STT 路线  
> **段落数**：434 | **总时长**：1680s

> ⚠️ **本字幕为 STT 路线产物**——YouTube 官方字幕被作者禁用（`Subtitles are disabled` + `automatic_captions: []`），通过 yt-dlp 拉取音频 + Groq Whisper API 转写。

---

## 简介

Claude Design lets you describe what you want in plain language and get production-quality outputs. Learn how a small team built a design tool that ships in your brand, from prompt to production.

**关于演讲**：Dan Carey（Anthropic Lab 产品经理）介绍 **Claude Design**——一个用 prompt 直接产出符合品牌规范的设计工具。28 分钟，3 人小团队，2 prompt 完成"最复杂页面"。

**D20 相关性**：本视频直接对应你弹药库中第 4、11、30 条——Claude Design 案例、效率数据、提示词泄露。

---

## 信达雅中文翻译

> **演讲者**：Dan Carey（Anthropic Labs 产品经理）  
> **原始语言**：英文 · **翻译**：Claude（手工译校）  
> **风格**：信、达、雅。技术名词保留英文原貌
> 已修复 ASR 误识别（Anthropik → Anthropic、Cloud → Claude 等）
> 段级对照：中文译文与英文原文一一对应（带时间戳）
> 翻译覆盖率：455/868 段

---

### 一、开场+产品介绍：3 人 10 周从想法到上线

**[00:00:00.000]** Dan Carey Reviewer
> 「Dan Carey 出品」

**[00:00:07.000]** How is everybody? A little bit more than that. Come on, guys. How is everybody?
> 大家都好吗？再来点掌声——来,伙计们,大家都好吗？

**[00:00:18.000]** Thank you. Thank you.
> 谢谢,谢谢。

**[00:00:20.000]** So, I'm Dan Carey. I am a product manager. I lead a product within Anthropic Labs.
> 我是 Dan Carey,产品经理,在 Anthropic Labs 负责一个产品。

**[00:00:25.000]** Today, we're going to talk a little bit about cloud design.
> 今天我们聊聊 Claude Design。

**[00:00:28.000]** Can I get a quick show of hands?
> 举手示意一下？

**[00:00:29.760]** Who here has already tried Claude Design?
> 在座有谁已经用过 Claude Design 了？

**[00:00:33.300]** OK, great.
> 好,棒。

**[00:00:34.800]** For those of you who haven't had a chance yet, Claude Design,
> 还没机会试过的朋友——Claude Design,

**[00:00:37.720]** it's a new product from Anthropik Labs,
> 是 Anthropic Labs 的新产品,（ASR 误识别：Anthropik → Anthropic）

**[00:00:40.160]** and it lets you collaborate with Claude
> 让你能和 Claude 一起协作

**[00:00:41.900]** to create polished visual artifacts.
> 打磨出精致的视觉物料。

**[00:00:43.960]** These can be designs, prototypes, slide, one-pagers, more.
> 设计稿、原型、幻灯片、单页报告,什么都能做。

**[00:00:49.440]** You can do a lot of different things with this product.
> 这个产品能做的事很多。

**[00:00:00.000]** Dan Carey Reviewer
> 「Dan Carey 出品」

**[00:00:07.000]** How is everybody? A little bit more than that. Come on, guys. How is everybody?
> 大家都好吗？再来点掌声——来,伙计们,大家都好吗？

**[00:00:18.000]** Thank you. Thank you.
> 谢谢,谢谢。

**[00:00:20.000]** So, I'm Dan Carey. I am a product manager. I lead a product within Anthropic Labs.
> 我是 Dan Carey,产品经理,在 Anthropic Labs 负责一个产品。

**[00:00:25.000]** Today, we're going to talk a little bit about cloud design.
> 今天我们聊聊 Claude Design。

**[00:00:28.000]** Can I get a quick show of hands?
> 举手示意一下？

**[00:00:29.760]** Who here has already tried Claude Design?
> 在座有谁已经用过 Claude Design 了？

**[00:00:33.300]** OK, great.
> 好,棒。

**[00:00:34.800]** For those of you who haven't had a chance yet, Claude Design,
> 还没机会试过的朋友——Claude Design,

**[00:00:37.720]** it's a new product from Anthropik Labs,
> 是 Anthropic Labs 的新产品,（ASR 误识别：Anthropik → Anthropic）

**[00:00:40.160]** and it lets you collaborate with Claude
> 让你能和 Claude 一起协作

**[00:00:41.900]** to create polished visual artifacts.
> 打磨出精致的视觉物料。

**[00:00:43.960]** These can be designs, prototypes, slide, one-pagers, more.
> 设计稿、原型、幻灯片、单页报告,什么都能做。

**[00:00:49.440]** You can do a lot of different things with this product.
> 这个产品能做的事很多。

### 二、Anthropic Labs：押注工厂

**[00:00:52.060]** And as of, I think it's yesterday,
> 就在昨天——我想是的——

**[00:00:54.880]** the product's been live in research preview for one month.
> 产品上线研究预览版已经一个月了。

**[00:00:57.900]** So we're pretty happy about that.
> 我们挺高兴的。

**[00:00:59.740]** Today, I'm going to tell you a little bit
> 今天我打算跟各位聊聊

**[00:01:01.560]** about how a very small team, it was three people
> 一个极小的团队——大部分开发阶段就 3 个人——

**[00:01:05.340]** for most of the development, built Claude Design
> 怎么把 Claude Design

**[00:01:08.000]** in about 10 weeks from idea to launching the product.
> 在 10 周内,从想法做到上线。

**[00:01:11.140]** And the reason I'm going to share these things with you
> 我之所以想跟你们分享这些,

**[00:01:13.140]** is because the most common question I get asked
> 是因为我被问得最多的问题是,

**[00:01:15.320]** is, why did you decide to start working on this?
> 你们怎么决定开始做这个产品的？

**[00:01:17.520]** How did you see that this was an opportunity
> 你们怎么看出这是一个做新 AI 产品的机会？

**[00:01:19.660]** for building a new AI-enabled product?
> 

**[00:01:22.360]** How'd you build it?
> 怎么做的？怎么发布的？

**[00:01:23.280]** How'd you launch it?
> 

**[00:01:25.200]** So everything I'm going to cover here,
> 我今天要讲的这些,

**[00:01:26.760]** There is no real secret sauce.
> 没什么独门秘方。

**[00:01:28.720]** These are all things that work well for us.
> 都是对我们管用的做法。

**[00:01:30.960]** Take what you like.
> 挑你觉得有用的拿。

**[00:01:31.760]** You can do a lot of these things tomorrow.
> 其中很多你明天就能上手。

**[00:01:35.400]** To start, I want to tell you about what Anthropic Labs is.
> 首先,跟你们介绍一下 Anthropic Labs。

**[00:01:38.560]** It's kind of funny.
> 说起来挺有意思。

**[00:01:39.180]** It's a lab inside a frontier lab.
> 前沿实验室里的实验室。

**[00:01:42.540]** We don't have any labs within Anthropic Labs,
> Anthropic Labs 内部没有更小的 lab,

**[00:01:44.280]** but it is labs quite a ways down.
> 但确实是往下好几层的 lab 结构。

**[00:01:47.080]** The way that we usually talk about it is as a bet factory.
> 我们一般把它叫做"押注工厂"。

**[00:01:51.480]** And by that, I mean we have very small teams
> 所谓押注工厂,就是有很多极小的团队,

**[00:01:53.900]** exploring the frontier of what the models can do
> 在探索模型能力的前沿,

**[00:01:56.780]** and making bets about whether or not something will work.
> 下注某个东西能不能成。

**[00:02:00.320]** We run experiments to find out what works.
> 我们做实验,看哪些管用。

**[00:02:03.620]** We double down on the things that are working.
> 管用的就加倍下注。

**[00:02:05.920]** We fold the things that are not working.
> 不灵的就收摊。

**[00:02:08.860]** And at any given time, we might have a dozen small teams
> 同一时间,我们大概会有十几个小团队,

**[00:02:12.480]** exploring different concepts.
> 在探索不同的概念。

**[00:02:15.320]** So it's lots of exploration, a small number
> 所以是大量探索,加上少量

**[00:02:18.440]** of really high-conviction releases of things
> 我们深信不疑会爆款的项目——

**[00:02:20.520]** that we think can be moonshots or change how people work
> 我们觉得它们有可能是大爆款,或者能改变大家工作方式的那种——

**[00:02:23.720]** with the models.
> ——这是和模型的协作。

**[00:02:26.140]** There's a few products that came from here that you may know.
> 这里出过几个你们可能知道的产品。

**[00:02:28.940]** Cloud Code came out of labs.
> Claude Code 是 labs 出的。

**[00:02:30.340]** Design came out of labs.
> Claude Design 也是。

**[00:02:31.480]** MCP came out of labs.
> MCP 也是。

**[00:02:32.620]** Skills came out of labs.
> Skills 也是。

**[00:02:34.480]** We had the Cloud and Chrome extension.
> 我们还有 Cloud 和 Chrome 扩展。

**[00:02:36.480]** We had our work on hands-free audio come out of labs.
> 我们的免提音频工作也是 labs 出的。

**[00:02:39.520]** So this is a process that's worked pretty well for us.
> 这套流程对我们非常管用。

**[00:02:42.660]** And we just keep turning the crank on this.
> 我们就这么持续地转下去。

**[00:02:46.520]** If you look at how each of our bets operate on a day-to-day basis,
> 看每个押注团队的日常运作,

**[00:02:50.840]** you're going to see a lot of parallels
> 你会看到很多相似之处,

**[00:02:52.960]** with lean startup methodologies.
> 和精益创业方法论很像。

**[00:02:55.160]** Nothing there is rocket science.
> 没什么惊天动地的。

**[00:02:57.400]** We did not invent any of these things.
> 这些东西都不是我们发明的。

**[00:02:59.520]** I'd say the biggest difference is the speed
> 我最大的区别是

**[00:03:01.460]** at which we run our loops.
> 我们跑 loop 的速度。

**[00:03:03.220]** We spend time with users and also
> 我们每天都跟用户在一起,同时也跟

**[00:03:05.900]** anthropic researchers every single day.
> Anthropic 的研究员每天在一起。

**[00:03:08.520]** My favorite thing to talk to users about is,
> 我最喜欢跟用户聊的是,

**[00:03:11.500]** please complain at me.
> 请来吐槽我。

**[00:03:13.100]** And my favorite thing to talk to researchers about is,
> 我最喜欢跟研究员聊的是,

**[00:03:16.200]** what have you been surprised by lately?
> 最近有什么让你惊讶的？

**[00:03:18.180]** Because both things are often opportunities
> 因为这两件事都常常是

**[00:03:20.240]** for new bets, new products, new things
> 新押注、新产品、新方向

**[00:03:22.160]** to explore that could pay off for us. We also aim to ship to users every day or two. We're
> 的契机。我们也争取每隔一两天就向用户推送新东西。

**[00:03:29.900]** trying to ship something new every single day in response to what we hear from people.
> 争取每天都发新东西,响应我们从用户那里听到的声音。

**[00:03:34.180]** We are trying to keep a very, very high cadence of innovation on the team, and we are trying
> 我们在团队里追求非常高强度的创新节奏,

**[00:03:38.540]** to get things out based off of what people tell us. Likewise, when people tell us something's
> 把东西推出去,根据用户反馈走。同样,当用户反馈说

**[00:03:43.920]** not working or they have feedback or they have a suggestion, early on in a project,
> 某个东西不好用、有意见、有建议时——项目早期——

**[00:03:48.340]** we try to ship them the response to that the next day. Oftentimes we're able to do the
> 我们争取第二天就把回应发出去。很多时候我们能当天就发。

**[00:03:52.780]** same day, sometimes it's the next day. Not everything hits that bar, but our usual goal
> 不一定每件事都达得到,但我们的常规目标是

**[00:03:57.220]** is to get things out very quickly to people when they have feedback.
> 用户有反馈时,非常快地给到回应。

**[00:04:01.660]** Finally, we do not try to predict the future. A lot of labs groups out there do try to predict
> 最后,我们不预测未来。很多外面的实验室团队确实会预测。

**[00:00:52.060]** And as of, I think it's yesterday,
> 就在昨天——我想是的——

**[00:00:54.880]** the product's been live in research preview for one month.
> 产品上线研究预览版已经一个月了。

**[00:00:57.900]** So we're pretty happy about that.
> 我们挺高兴的。

**[00:00:59.740]** Today, I'm going to tell you a little bit
> 今天我打算跟各位聊聊

**[00:01:01.560]** about how a very small team, it was three people
> 一个极小的团队——大部分开发阶段就 3 个人——

**[00:01:05.340]** for most of the development, built Claude Design
> 怎么把 Claude Design

**[00:01:08.000]** in about 10 weeks from idea to launching the product.
> 在 10 周内,从想法做到上线。

**[00:01:11.140]** And the reason I'm going to share these things with you
> 我之所以想跟你们分享这些,

**[00:01:13.140]** is because the most common question I get asked
> 是因为我被问得最多的问题是,

**[00:01:15.320]** is, why did you decide to start working on this?
> 你们怎么决定开始做这个产品的？

**[00:01:17.520]** How did you see that this was an opportunity
> 你们怎么看出这是一个做新 AI 产品的机会？

**[00:01:19.660]** for building a new AI-enabled product?
> 

**[00:01:22.360]** How'd you build it?
> 怎么做的？怎么发布的？

**[00:01:23.280]** How'd you launch it?
> 

**[00:01:25.200]** So everything I'm going to cover here,
> 我今天要讲的这些,

**[00:01:26.760]** There is no real secret sauce.
> 没什么独门秘方。

**[00:01:28.720]** These are all things that work well for us.
> 都是对我们管用的做法。

**[00:01:30.960]** Take what you like.
> 挑你觉得有用的拿。

**[00:01:31.760]** You can do a lot of these things tomorrow.
> 其中很多你明天就能上手。

**[00:01:35.400]** To start, I want to tell you about what Anthropic Labs is.
> 首先,跟你们介绍一下 Anthropic Labs。

**[00:01:38.560]** It's kind of funny.
> 说起来挺有意思。

**[00:01:39.180]** It's a lab inside a frontier lab.
> 前沿实验室里的实验室。

**[00:01:42.540]** We don't have any labs within Anthropic Labs,
> Anthropic Labs 内部没有更小的 lab,

**[00:01:44.280]** but it is labs quite a ways down.
> 但确实是往下好几层的 lab 结构。

**[00:01:47.080]** The way that we usually talk about it is as a bet factory.
> 我们一般把它叫做"押注工厂"。

**[00:01:51.480]** And by that, I mean we have very small teams
> 所谓押注工厂,就是有很多极小的团队,

**[00:01:53.900]** exploring the frontier of what the models can do
> 在探索模型能力的前沿,

**[00:01:56.780]** and making bets about whether or not something will work.
> 下注某个东西能不能成。

**[00:02:00.320]** We run experiments to find out what works.
> 我们做实验,看哪些管用。

**[00:02:03.620]** We double down on the things that are working.
> 管用的就加倍下注。

**[00:02:05.920]** We fold the things that are not working.
> 不灵的就收摊。

**[00:02:08.860]** And at any given time, we might have a dozen small teams
> 同一时间,我们大概会有十几个小团队,

**[00:02:12.480]** exploring different concepts.
> 在探索不同的概念。

**[00:02:15.320]** So it's lots of exploration, a small number
> 所以是大量探索,加上少量

**[00:02:18.440]** of really high-conviction releases of things
> 我们深信不疑会爆款的项目——

**[00:02:20.520]** that we think can be moonshots or change how people work
> 我们觉得它们有可能是大爆款,或者能改变大家工作方式的那种——

**[00:02:23.720]** with the models.
> ——这是和模型的协作。

**[00:02:26.140]** There's a few products that came from here that you may know.
> 这里出过几个你们可能知道的产品。

**[00:02:28.940]** Cloud Code came out of labs.
> Claude Code 是 labs 出的。

**[00:02:30.340]** Design came out of labs.
> Claude Design 也是。

**[00:02:31.480]** MCP came out of labs.
> MCP 也是。

**[00:02:32.620]** Skills came out of labs.
> Skills 也是。

**[00:02:34.480]** We had the Cloud and Chrome extension.
> 我们还有 Cloud 和 Chrome 扩展。

**[00:02:36.480]** We had our work on hands-free audio come out of labs.
> 我们的免提音频工作也是 labs 出的。

**[00:02:39.520]** So this is a process that's worked pretty well for us.
> 这套流程对我们非常管用。

**[00:02:42.660]** And we just keep turning the crank on this.
> 我们就这么持续地转下去。

**[00:02:46.520]** If you look at how each of our bets operate on a day-to-day basis,
> 看每个押注团队的日常运作,

**[00:02:50.840]** you're going to see a lot of parallels
> 你会看到很多相似之处,

**[00:02:52.960]** with lean startup methodologies.
> 和精益创业方法论很像。

**[00:02:55.160]** Nothing there is rocket science.
> 没什么惊天动地的。

**[00:02:57.400]** We did not invent any of these things.
> 这些东西都不是我们发明的。

**[00:02:59.520]** I'd say the biggest difference is the speed
> 我最大的区别是

**[00:03:01.460]** at which we run our loops.
> 我们跑 loop 的速度。

**[00:03:03.220]** We spend time with users and also
> 我们每天都跟用户在一起,同时也跟

**[00:03:05.900]** anthropic researchers every single day.
> Anthropic 的研究员每天在一起。

**[00:03:08.520]** My favorite thing to talk to users about is,
> 我最喜欢跟用户聊的是,

**[00:03:11.500]** please complain at me.
> 请来吐槽我。

**[00:03:13.100]** And my favorite thing to talk to researchers about is,
> 我最喜欢跟研究员聊的是,

**[00:03:16.200]** what have you been surprised by lately?
> 最近有什么让你惊讶的？

**[00:03:18.180]** Because both things are often opportunities
> 因为这两件事都常常是

**[00:03:20.240]** for new bets, new products, new things
> 新押注、新产品、新方向

**[00:03:22.160]** to explore that could pay off for us. We also aim to ship to users every day or two. We're
> 的契机。我们也争取每隔一两天就向用户推送新东西。

**[00:03:29.900]** trying to ship something new every single day in response to what we hear from people.
> 争取每天都发新东西,响应我们从用户那里听到的声音。

**[00:03:34.180]** We are trying to keep a very, very high cadence of innovation on the team, and we are trying
> 我们在团队里追求非常高强度的创新节奏,

**[00:03:38.540]** to get things out based off of what people tell us. Likewise, when people tell us something's
> 把东西推出去,根据用户反馈走。同样,当用户反馈说

**[00:03:43.920]** not working or they have feedback or they have a suggestion, early on in a project,
> 某个东西不好用、有意见、有建议时——项目早期——

**[00:03:48.340]** we try to ship them the response to that the next day. Oftentimes we're able to do the
> 我们争取第二天就把回应发出去。很多时候我们能当天就发。

**[00:03:52.780]** same day, sometimes it's the next day. Not everything hits that bar, but our usual goal
> 不一定每件事都达得到,但我们的常规目标是

**[00:03:57.220]** is to get things out very quickly to people when they have feedback.
> 用户有反馈时,非常快地给到回应。

**[00:04:01.660]** Finally, we do not try to predict the future. A lot of labs groups out there do try to predict
> 最后,我们不预测未来。很多外面的实验室团队确实会预测。

### 三、为什么做 Claude Design：瓶颈在转移

**[00:04:07.340]** the future. They say in ten years' time we're going to have this amazing technology and
> 他们说十年后我们会有惊人的技术,会做惊人的事。

**[00:04:10.460]** it's going to do these amazing things. We don't do that. Instead, we try to ship, we
> 我们不做这个。我们反过来——不断发布、

**[00:04:16.420]** We watch people use the stuff, we learn what they do, we ship, we watch, we learn, we ship,
> 看用户怎么用,从中学,然后发布,看,学,再发布。

**[00:04:21.020]** we watch, we learn.
> 看,学。

**[00:04:22.020]** We run that loop over and over.
> 我们把这个 loop 跑了一遍又一遍。

**[00:04:24.240]** For Cloud Design, we ran that loop somewhere between 50 and 100 times over the course of
> 在 Claude Design 这个项目上,我们在 10 周内

**[00:04:29.020]** those 10 weeks.
> 把那个 loop 跑了 50 到 100 次。

**[00:04:32.360]** So why did we start working on Cloud Design?
> 所以我们为什么开始做 Claude Design？

**[00:04:36.100]** We started working on Cloud Design because Cloud Code made engineers really, really fast,
> 我们做 Claude Design 是因为 Claude Code 把工程师变得非常、非常快,

**[00:04:41.940]** and the rest of us had to keep up.
> 我们其他人得跟上。

**[00:04:44.180]** So product development timelines, they used to be six months.
> 产品开发周期,以前是 6 个月。

**[00:04:48.260]** And then they'd be a month.
> 后来是 1 个月。

**[00:04:49.680]** And then a week.
> 再后来是 1 周。

**[00:04:51.440]** And now a day.
> 现在是 1 天。

**[00:04:53.720]** So sometimes things that you were spending a week on before are now something that you're
> 以前要花一周的事,现在几小时就搞定,直接放到用户面前。

**[00:04:57.200]** getting done in a couple hours and getting out in front of users.
> 以前一周的事,现在几小时搞定,推到用户面前。

**[00:04:59.800]** That is rapid.
> 这速度,真快。

**[00:05:00.800]** Can I see a very quick show of fingers from people?
> 举手指个数,很快。

**[00:05:04.460]** I'm very curious.
> 我特别好奇。

**[00:05:05.700]** The last feature you shipped, how many weeks did it take from idea to getting it in front
> 你最近发的一个功能,从想法到推到用户面前,几周？

**[00:05:10.760]** of users?
> 

**[00:05:11.760]** It's okay if you need two hands, and don't be shy here.
> 两只手也行,别害羞。

**[00:05:14.760]** One, one, ten, one, two, one, four, one.
> 1,1,10,1,2,1,4,1。

**[00:05:20.460]** A lot of different answers, but things have gotten a lot faster.
> 答案很多样,但整体都变快了。

**[00:05:23.520]** Think about what your answer would have been a year ago.
> 想想一年前你会怎么答。

**[00:05:27.520]** All these timelines have compressed a lot.
> 所有这些周期都压缩了很多。

**[00:05:30.380]** And so once Cloud Code took off, the bottleneck moved.
> 所以 Claude Code 起飞后,瓶颈就移了。

**[00:05:33.800]** The bottleneck moved from building the feature
> 瓶颈从"做功能"

**[00:05:36.200]** to figuring out the right things to be
> 移到了"想清楚该做什么"。

**[00:05:38.280]** building for your users in a lot of cases.
> 在很多场景下,后者才是真正难的事。

**[00:05:41.460]** So the option was either skip those early steps, just try and decide on the fly, and
> 要么跳过这些早期步骤,边走边定,可能做出错的东西——

**[00:05:48.220]** potentially build the wrong thing really fast, or try to find ways for the rest of us to
> 要么想办法让其他角色也快起来。

**[00:05:52.780]** speed up.
> 

**[00:05:54.740]** So our designers, our PMs were having trouble keeping up.
> 我们的设计师、PM 都快跟不上了。

**[00:05:58.540]** We needed our own accelerator tool.
> 我们需要自己的加速工具。

**[00:06:00.820]** And somebody on our team, Nate, who was a designer on Cloud Code previously, had seen
> 我们团队里有个叫 Nate 的人,之前是 Claude Code 的设计师,

**[00:06:05.060]** firsthand what happens when some of these teams speed up to such a huge extent.
> 亲眼看到这些团队被加速到这种程度时会发生什么。

**[00:06:10.420]** And that got him thinking about the problem and a potential solution.
> 这让他开始想这个问题,以及可能的解法。

**[00:06:14.300]** And so he ended up hacking together a prototype over the course of a weekend while he was
> 他花了一个周末边做另一个押注边拼了个原型。

**[00:06:19.200]** working on a different bet.
> 

**[00:06:21.600]** And it was very simple.
> 非常简单。

**[00:06:22.920]** It was the agent SDK.
> 就是 agent SDK。

**[00:06:24.640]** It was a very thin IDE wrapper.
> 套了一个极薄的 IDE 壳。

**[00:06:27.820]** And it used an existing skill that he had already been using in cloud code.
> 调用的 skill 正是他之前在 Claude Code 里用过的那个。

**[00:06:33.080]** And this is how a lot of our labs bets start.
> 我们很多 labs 押注就是这么起步的。

**[00:06:36.140]** It's one person, one weekend, one screen reporting.
> 一个人,一个周末,一个屏幕,边做边报。

**[00:06:38.980]** and get something, hacks something together, and just shares what they did. So, for us,
> 捣鼓出点什么,就分享出来。所以——

**[00:06:45.840]** Nate posts this in Slack. We run a lot of things in Slack. And everybody helpfully chimed
> Nate 在 Slack 里发了出来。我们很多事情都跑在 Slack 上。大家都热心地

**[00:06:50.560]** in with both this is what promising about this and also here all the stuff that doesn work totally broken please go fix And that was his roadmap for the first couple weeks on this It was just what the promising stuff to lean into What are the major blockers
> 补意见——哪些是亮点,哪些是"完全坏的快去修"。这就是他前几周的路标:哪些亮点要重点投入,哪些主要阻塞要打通。

**[00:07:05.350]** we want to address? I do think it's worth calling out the things that we did not do.
> 我觉得值得说一下我们**没做**的事。

**[00:04:07.340]** the future. They say in ten years' time we're going to have this amazing technology and
> 他们说十年后我们会有惊人的技术,会做惊人的事。

**[00:04:10.460]** it's going to do these amazing things. We don't do that. Instead, we try to ship, we
> 我们不做这个。我们反过来——不断发布、

**[00:04:16.420]** We watch people use the stuff, we learn what they do, we ship, we watch, we learn, we ship,
> 看用户怎么用,从中学,然后发布,看,学,再发布。

**[00:04:21.020]** we watch, we learn.
> 看,学。

**[00:04:22.020]** We run that loop over and over.
> 我们把这个 loop 跑了一遍又一遍。

**[00:04:24.240]** For Cloud Design, we ran that loop somewhere between 50 and 100 times over the course of
> 在 Claude Design 这个项目上,我们在 10 周内

**[00:04:29.020]** those 10 weeks.
> 把那个 loop 跑了 50 到 100 次。

**[00:04:32.360]** So why did we start working on Cloud Design?
> 所以我们为什么开始做 Claude Design？

**[00:04:36.100]** We started working on Cloud Design because Cloud Code made engineers really, really fast,
> 我们做 Claude Design 是因为 Claude Code 把工程师变得非常、非常快,

**[00:04:41.940]** and the rest of us had to keep up.
> 我们其他人得跟上。

**[00:04:44.180]** So product development timelines, they used to be six months.
> 产品开发周期,以前是 6 个月。

**[00:04:48.260]** And then they'd be a month.
> 后来是 1 个月。

**[00:04:49.680]** And then a week.
> 再后来是 1 周。

**[00:04:51.440]** And now a day.
> 现在是 1 天。

**[00:04:53.720]** So sometimes things that you were spending a week on before are now something that you're
> 以前要花一周的事,现在几小时就搞定,直接放到用户面前。

**[00:04:57.200]** getting done in a couple hours and getting out in front of users.
> 以前一周的事,现在几小时搞定,推到用户面前。

**[00:04:59.800]** That is rapid.
> 这速度,真快。

**[00:05:00.800]** Can I see a very quick show of fingers from people?
> 举手指个数,很快。

**[00:05:04.460]** I'm very curious.
> 我特别好奇。

**[00:05:05.700]** The last feature you shipped, how many weeks did it take from idea to getting it in front
> 你最近发的一个功能,从想法到推到用户面前,几周？

**[00:05:10.760]** of users?
> 

**[00:05:11.760]** It's okay if you need two hands, and don't be shy here.
> 两只手也行,别害羞。

**[00:05:14.760]** One, one, ten, one, two, one, four, one.
> 1,1,10,1,2,1,4,1。

**[00:05:20.460]** A lot of different answers, but things have gotten a lot faster.
> 答案很多样,但整体都变快了。

**[00:05:23.520]** Think about what your answer would have been a year ago.
> 想想一年前你会怎么答。

**[00:05:27.520]** All these timelines have compressed a lot.
> 所有这些周期都压缩了很多。

**[00:05:30.380]** And so once Cloud Code took off, the bottleneck moved.
> 所以 Claude Code 起飞后,瓶颈就移了。

**[00:05:33.800]** The bottleneck moved from building the feature
> 瓶颈从"做功能"

**[00:05:36.200]** to figuring out the right things to be
> 移到了"想清楚该做什么"。

**[00:05:38.280]** building for your users in a lot of cases.
> 在很多场景下,后者才是真正难的事。

**[00:05:41.460]** So the option was either skip those early steps, just try and decide on the fly, and
> 要么跳过这些早期步骤,边走边定,可能做出错的东西——

**[00:05:48.220]** potentially build the wrong thing really fast, or try to find ways for the rest of us to
> 要么想办法让其他角色也快起来。

**[00:05:52.780]** speed up.
> 

**[00:05:54.740]** So our designers, our PMs were having trouble keeping up.
> 我们的设计师、PM 都快跟不上了。

**[00:05:58.540]** We needed our own accelerator tool.
> 我们需要自己的加速工具。

**[00:06:00.820]** And somebody on our team, Nate, who was a designer on Cloud Code previously, had seen
> 我们团队里有个叫 Nate 的人,之前是 Claude Code 的设计师,

**[00:06:05.060]** firsthand what happens when some of these teams speed up to such a huge extent.
> 亲眼看到这些团队被加速到这种程度时会发生什么。

**[00:06:10.420]** And that got him thinking about the problem and a potential solution.
> 这让他开始想这个问题,以及可能的解法。

**[00:06:14.300]** And so he ended up hacking together a prototype over the course of a weekend while he was
> 他花了一个周末边做另一个押注边拼了个原型。

**[00:06:19.200]** working on a different bet.
> 

**[00:06:21.600]** And it was very simple.
> 非常简单。

**[00:06:22.920]** It was the agent SDK.
> 就是 agent SDK。

**[00:06:24.640]** It was a very thin IDE wrapper.
> 套了一个极薄的 IDE 壳。

**[00:06:27.820]** And it used an existing skill that he had already been using in cloud code.
> 调用的 skill 正是他之前在 Claude Code 里用过的那个。

**[00:06:33.080]** And this is how a lot of our labs bets start.
> 我们很多 labs 押注就是这么起步的。

**[00:06:36.140]** It's one person, one weekend, one screen reporting.
> 一个人,一个周末,一个屏幕,边做边报。

**[00:06:38.980]** and get something, hacks something together, and just shares what they did. So, for us,
> 捣鼓出点什么,就分享出来。所以——

**[00:06:45.840]** Nate posts this in Slack. We run a lot of things in Slack. And everybody helpfully chimed
> Nate 在 Slack 里发了出来。我们很多事情都跑在 Slack 上。大家都热心地

**[00:06:50.560]** in with both this is what promising about this and also here all the stuff that doesn work totally broken please go fix And that was his roadmap for the first couple weeks on this It was just what the promising stuff to lean into What are the major blockers
> 补意见——哪些是亮点,哪些是"完全坏的快去修"。这就是他前几周的路标:哪些亮点要重点投入,哪些主要阻塞要打通。

**[00:07:05.350]** we want to address? I do think it's worth calling out the things that we did not do.
> 我觉得值得说一下我们**没做**的事。

### 四、流程：原型 > PRD > 视频/分支

**[00:07:11.850]** So we did not write a PRD in advance. We had zero vision docs. We had zero KR meetings. We did not
> 我们没提前写 PRD。零愿景文档。零 KR 会议。也没

**[00:07:18.970]** have an H1 annual staffing plan. We did not have a two-page year for what we were going to do over
> 年度人头规划。也没有"未来两年怎么做"的两页纸。

**[00:07:24.670]** the next two years. We did not write the press release in advance for what we were doing.
> 我们也没提前把要发的稿子写好。

**[00:07:29.110]** Those things are great if you know exactly what you're building. We did not know exactly
> 如果你已经明确知道要做什么,这些流程挺好用。但我们当时并不知道。

**[00:07:32.850]** what we were building. All we knew is that we had a spark. So who here works off of PRDs
> 我们只知道——有那么个火花。在座有谁按 PRD 工作的？

**[00:07:39.530]** or has written one or worked off of one in the last month? Most of the room. Now, of
> 或者最近一个月写过/用过的？大部分人。好,继续——

**[00:07:45.750]** those people that raised your hand, who would rather be working off of a prototype that
> 你们这些人里,谁更愿意基于一个能跑的原型

**[00:07:49.070]** worked and showed you the feature fully. Exact same hands. Pretty good. So we like to use
> 而不是文档来工作？同一批手举起来。挺好。我们喜欢用

**[00:07:56.890]** prototypes because documents are imprecise. It's so easy for two people to look at the
> 原型,因为文档不精确。两个人看同一份文档,脑子里想的可能是两个不同的产品。

**[00:08:03.310]** same doc and have two different products in mind about what the experience should be.
> 

**[00:08:08.270]** And usually those two ideas are not the same idea that the author had when they were writing
> 而且通常这两个想法都不是作者写文档时脑子里的那个。

**[00:08:12.870]** the thing in the first place. Right? So docs are imprecise. Prototypes, they're more concrete.
> 对吧？文档不精确。原型更具体。

**[00:08:18.010]** They're more visceral.
> 更直观。

**[00:08:19.010]** They let you get hands-on with the thing and really feel the experience yourself.
> 让你能亲手把玩,真正感受体验。

**[00:08:23.790]** Over the course of this project, we were able to get our prototyping cycle down to a couple
> 在这个项目里,我们把原型迭代周期压到了

**[00:08:28.910]** of minutes.
> 几分钟。

**[00:08:30.410]** So if somebody had an idea, they were able to prototype and get it out in a couple of
> 所以谁有个想法,几分钟就能做出原型推出去。

**[00:08:33.630]** minutes.
> 

**[00:08:34.630]** For us, the easiest way of doing this is talk to it with somebody else on your team, record
> 对我们来说,最简单的做法是:和团队其他人聊,录下来,

**[00:08:41.170]** it, transcribe it.
> 转成文字。

**[00:08:42.410]** There's tons of great tools for that.
> 这事儿工具一大堆。

**[00:08:44.130]** and mainly talk about what the problem is, what does the solution generally do, why do
> 主要聊:问题是什么,解法大致做什么,为什么

**[00:08:48.490]** you care about solving this problem, and then we would take that transcript and give it to
> 你关心这个问题——然后把转录稿喂给

**[00:08:53.130]** Claude Design once we had something working and say give me a few options for this. This
> Claude Design,只要能用了就跟它说:给我几个方案。这套

**[00:08:58.030]** has effectively replaced PRDs for me as a product manager that's been writing them for
> 对一个写了快 20 年 PRD 的 PM 来说,基本替代了 PRD。

**[00:09:02.570]** almost two decades now. Now I just do prototypes, this is my flow, it works pretty well. In labs
> 现在我只做原型,这就是我的流程,挺好用。在 labs 里

**[00:09:09.350]** we do this ritual every once in a while, we get together and we call them pitch-offs.
> 我们时不时会做这个仪式——聚在一起,叫 pitch-off。

**[00:09:14.290]** And the thing I like doing about these is we all get together, we brainstorm. You're
> 我喜欢这个仪式,因为大家聚在一起,头脑风暴。你基本就是

**[00:09:17.870]** basically trying to nerd snipe other people to come work on your thing with you that you
> 想方设法吸引别人来跟你一起做你那个——

**[00:09:21.730]** think the team should do. And when we first started doing these, people talk and you just
> 你觉得团队该做的事。刚开始做的时候,大家就是讲,讲,讲,展示你的东西——

**[00:09:26.950]** talk and present your thing, and it's not that compelling. The first time we did this
> 其实也没多吸引人。第一次在 Claude Design 项目上做这个的时候,

**[00:09:30.470]** with Claude Design is what convinced me that we had a promising product on our hands. Because
> 我才确信这是个好产品。因为——

**[00:09:36.710]** In these pitch-offs, most of the ideas people come up with during the pitch-off, someone
> 在 pitch-off 里,大家脑暴出的点子,有人讲了一句话,

**[00:09:42.010]** says something and you're inspired by what they say.
> 你就被他启发了。

**[00:09:45.010]** Somebody has an idea that you fork off of and you come up with something new on your
> 别人的点子你 fork 一下,自己又冒出新东西。

**[00:09:47.830]** own.
> 

**[00:09:48.830]** By the second half of it, 100% of the pitches were prototypes or slides made with design.
> 到后半场,100% 的 pitch 都是用 Claude Design 现场做的原型或幻灯。

**[00:09:54.470]** They were being made on the fly in the meeting.
> 都是会上现场做出来的。

**[00:09:57.430]** That's what convinced us this is a proof point we should double down on this bet.
> 那一刻我们就确信——这个押注值得加倍。

**[00:07:11.850]** So we did not write a PRD in advance. We had zero vision docs. We had zero KR meetings. We did not
> 我们没提前写 PRD。零愿景文档。零 KR 会议。也没

**[00:07:18.970]** have an H1 annual staffing plan. We did not have a two-page year for what we were going to do over
> 年度人头规划。也没有"未来两年怎么做"的两页纸。

**[00:07:24.670]** the next two years. We did not write the press release in advance for what we were doing.
> 我们也没提前把要发的稿子写好。

**[00:07:29.110]** Those things are great if you know exactly what you're building. We did not know exactly
> 如果你已经明确知道要做什么,这些流程挺好用。但我们当时并不知道。

**[00:07:32.850]** what we were building. All we knew is that we had a spark. So who here works off of PRDs
> 我们只知道——有那么个火花。在座有谁按 PRD 工作的？

**[00:07:39.530]** or has written one or worked off of one in the last month? Most of the room. Now, of
> 或者最近一个月写过/用过的？大部分人。好,继续——

**[00:07:45.750]** those people that raised your hand, who would rather be working off of a prototype that
> 你们这些人里,谁更愿意基于一个能跑的原型

**[00:07:49.070]** worked and showed you the feature fully. Exact same hands. Pretty good. So we like to use
> 而不是文档来工作？同一批手举起来。挺好。我们喜欢用

**[00:07:56.890]** prototypes because documents are imprecise. It's so easy for two people to look at the
> 原型,因为文档不精确。两个人看同一份文档,脑子里想的可能是两个不同的产品。

**[00:08:03.310]** same doc and have two different products in mind about what the experience should be.
> 

**[00:08:08.270]** And usually those two ideas are not the same idea that the author had when they were writing
> 而且通常这两个想法都不是作者写文档时脑子里的那个。

**[00:08:12.870]** the thing in the first place. Right? So docs are imprecise. Prototypes, they're more concrete.
> 对吧？文档不精确。原型更具体。

**[00:08:18.010]** They're more visceral.
> 更直观。

**[00:08:19.010]** They let you get hands-on with the thing and really feel the experience yourself.
> 让你能亲手把玩,真正感受体验。

**[00:08:23.790]** Over the course of this project, we were able to get our prototyping cycle down to a couple
> 在这个项目里,我们把原型迭代周期压到了

**[00:08:28.910]** of minutes.
> 几分钟。

**[00:08:30.410]** So if somebody had an idea, they were able to prototype and get it out in a couple of
> 所以谁有个想法,几分钟就能做出原型推出去。

**[00:08:33.630]** minutes.
> 

**[00:08:34.630]** For us, the easiest way of doing this is talk to it with somebody else on your team, record
> 对我们来说,最简单的做法是:和团队其他人聊,录下来,

**[00:08:41.170]** it, transcribe it.
> 转成文字。

**[00:08:42.410]** There's tons of great tools for that.
> 这事儿工具一大堆。

**[00:08:44.130]** and mainly talk about what the problem is, what does the solution generally do, why do
> 主要聊:问题是什么,解法大致做什么,为什么

**[00:08:48.490]** you care about solving this problem, and then we would take that transcript and give it to
> 你关心这个问题——然后把转录稿喂给

**[00:08:53.130]** Claude Design once we had something working and say give me a few options for this. This
> Claude Design,只要能用了就跟它说:给我几个方案。这套

**[00:08:58.030]** has effectively replaced PRDs for me as a product manager that's been writing them for
> 对一个写了快 20 年 PRD 的 PM 来说,基本替代了 PRD。

**[00:09:02.570]** almost two decades now. Now I just do prototypes, this is my flow, it works pretty well. In labs
> 现在我只做原型,这就是我的流程,挺好用。在 labs 里

**[00:09:09.350]** we do this ritual every once in a while, we get together and we call them pitch-offs.
> 我们时不时会做这个仪式——聚在一起,叫 pitch-off。

**[00:09:14.290]** And the thing I like doing about these is we all get together, we brainstorm. You're
> 我喜欢这个仪式,因为大家聚在一起,头脑风暴。你基本就是

**[00:09:17.870]** basically trying to nerd snipe other people to come work on your thing with you that you
> 想方设法吸引别人来跟你一起做你那个——

**[00:09:21.730]** think the team should do. And when we first started doing these, people talk and you just
> 你觉得团队该做的事。刚开始做的时候,大家就是讲,讲,讲,展示你的东西——

**[00:09:26.950]** talk and present your thing, and it's not that compelling. The first time we did this
> 其实也没多吸引人。第一次在 Claude Design 项目上做这个的时候,

**[00:09:30.470]** with Claude Design is what convinced me that we had a promising product on our hands. Because
> 我才确信这是个好产品。因为——

**[00:09:36.710]** In these pitch-offs, most of the ideas people come up with during the pitch-off, someone
> 在 pitch-off 里,大家脑暴出的点子,有人讲了一句话,

**[00:09:42.010]** says something and you're inspired by what they say.
> 你就被他启发了。

**[00:09:45.010]** Somebody has an idea that you fork off of and you come up with something new on your
> 别人的点子你 fork 一下,自己又冒出新东西。

**[00:09:47.830]** own.
> 

**[00:09:48.830]** By the second half of it, 100% of the pitches were prototypes or slides made with design.
> 到后半场,100% 的 pitch 都是用 Claude Design 现场做的原型或幻灯。

**[00:09:54.470]** They were being made on the fly in the meeting.
> 都是会上现场做出来的。

**[00:09:57.430]** That's what convinced us this is a proof point we should double down on this bet.
> 那一刻我们就确信——这个押注值得加倍。

### 五、小团队的力量：3 人+Claude，角色界限消失

**[00:10:01.430]** We should take this to market.
> 得把它推向市场。

**[00:10:03.530]** The other thing that's a little bit different about the way that teams work in labs is the
> 另一个 labs 团队不一样的地方是

**[00:10:07.710]** size of the teams.
> 团队规模。

**[00:10:09.790]** So almost every labs bet starts as a single person.
> 几乎所有 labs 押注都从一个人开始。

**[00:10:13.930]** It's just one person with their good buddy Claude exploring a really hard problem and
> 就是一个人,带着好搭档 Claude,去探一个特别难的问题、

**[00:10:19.250]** exploring a pretty hard idea.
> 特别难的点子。

**[00:10:21.990]** And at this point, you are not trying to build the best product in the world.
> 这个阶段,你不是要做世界上最好的产品。

**[00:10:26.910]** You are just looking for that little moment of magic.
> 你只是在找那一下魔法时刻。

**[00:10:29.530]** You are looking for that little hint of heat.
> 找那一丝热度。

**[00:10:31.710]** You are looking for, hey, this is a promising idea because there is a little sparkly glimmer
> 你在找:嘿,这个想法有戏,有点小火花——

**[00:10:36.370]** here that we can build into something compelling.
> 我们能把它做成一个好产品。

**[00:10:39.530]** And most labs bets, I'll admit, do not make it past this point.
> 坦白讲,大部分 labs 押注走不到这一步。

**[00:10:43.550]** Most things we end up folding before they get here.
> 大部分我们会在这之前就收摊。

**[00:10:46.470]** And that's totally okay.
> 这完全 OK。

**[00:10:47.550]** This early exploration is usually hours or a few days for most things.
> 早期探索大部分就是几小时或几天。

**[00:10:53.950]** Once we do have a promising spark, we usually scale the team up massively, you know, 300%,
> 一旦真有戏,我们通常把团队大幅扩展——300%——

**[00:10:59.790]** all the way to three people.
> 到 3 个人。

**[00:11:01.330]** So these are not big teams.
> 所以都不是大团队。

**[00:11:03.590]** And the reason why we do that is that we want it to be a very tight group exploring together
> 我们这样做的原因是,希望一个紧密的小组一起探索,

**[00:11:09.430]** with very little collaboration overhead.
> 协作开销极低。

**[00:11:11.830]** If something is so compelling that we're pretty convinced that we're going to be taking it
> 如果某件事确实有戏,我们确信会把它做成产品——

**[00:11:15.550]** to a product, after it's had three people for a while, we might scale it all the way
> 在 3 人一段时间之后,我们最多扩展到

**[00:11:19.150]** up to five people ahead of launch.
> 5 个人,然后发布。

**[00:11:22.310]** So who here works on a team that is smaller than 20 people?
> 在座有谁的团队 < 20 人？

**[00:11:26.930]** Okay.
> 好。

**[00:11:28.470]** Almost everybody, but not everybody.
> 几乎所有人,但不是全部。

**[00:11:30.030]** What about smaller than ten? Five? Smaller than three? Is there anyone here that's totally
> < 10？< 5？< 3？有没有完全单干的？

**[00:11:36.650]** solo? Oh, yeah, a couple people. Three-ish? Two and a half? Four. Okay. So for most of
> 哦,有几位。差不多 3？两个半？4 个？好。Claude Design

**[00:11:44.030]** Claude's design development, it was only three people with Claude, and luckily Claude's a
> 大部分开发阶段,只有 3 个人+ Claude。万幸 Claude 是个不错的

**[00:11:48.650]** pretty good team member. So what makes that possible? I'm sure this is also true of a lot
> 队员。什么让这成为可能？在座很多 solo builder 肯定也深有体会——

**[00:11:54.710]** of the solo builders in this room, everyone on the team does everything. The engineers
> 团队里每个人什么都干。工程师

**[00:12:01.750]** talk to users, PMs write code, designers do data analysis. All of these things are enabled
> 跟用户聊,PM 写代码,设计师做数据分析。Claude 让这些

**[00:12:07.950]** in part with Cloud. And the lines between the roles on this team, they have essentially
> 成为可能。角色之间的界限,在这个团队里,

**[00:12:13.610]** dissolved at this point. You do have your specialization, you do have the unique perspective
> 已经基本消失了。你当然还有自己的专长、有独特的视角,

**[00:12:18.350]** and diversity that you bring to a team, but at any moment, any one of these people on this
> 有你的多样性,但任何时刻,这个团队里任何一个人,

**[00:12:22.970]** team, can talk to ten users, you can realize what the underlying problem is, you can design
> 都可以去跟十个用户聊,搞清底层问题,设计

**[00:12:29.330]** a solution to it, you can ship it to users, you can listen for feedback, you can keep iterating
> 一个解法,推到用户,听反馈,继续迭代——

**[00:12:33.930]** solo if you need to. Quite often that's the case. That's how most features happen. Most
> 需要的话,完全 solo。多数情况正是如此。大部分功能就是这么来的。

**[00:12:38.630]** things on the team are totally solo. And having this small team where everyone can do everything,
> 团队里大部分东西都是纯 solo。每个人都能干所有事,

**[00:12:45.910]** that's the main thing that minimizes coordination overhead for us. Again, most things can be
> 这是我们降低协调开销的关键。同样,大部分事情可以

**[00:12:51.170]** be done solo, but let's say you have to get the whole team together, oftentimes that's
> solo 搞定。但如果真要拉齐全员,通常也是

**[00:12:55.130]** as easy as talking to the person on your left and the person on your right and you're done.
> 跟左右两边的人说一声就完事。

**[00:12:59.690]** It's not a big alignment meeting, it's not something you have to schedule, it's not something
> 不用开大会,不用排日程,不用

**[00:13:02.850]** that you have to wait for. And so this helps us minimize coordination overhead. We've already
> 等。这帮我们把协调开销压到最低。

**[00:13:08.590]** minimized planning and process just by relying on prototypes, and just doing these two things
> 靠原型把规划+流程省掉了。光这两件事

**[00:13:14.830]** alone would let us go pretty quickly, right? They would let us go pretty fast, they would
> 就够我们跑得很快了——把那些大里程碑前期的长周期压掉。

**[00:13:19.810]** take down these big long cycles at the beginning of major milestones. But we go a good bit
> 但我们还能更快,办法是把 loop 里每一步

**[00:10:01.430]** We should take this to market.
> 得把它推向市场。

**[00:10:03.530]** The other thing that's a little bit different about the way that teams work in labs is the
> 另一个 labs 团队不一样的地方是

**[00:10:07.710]** size of the teams.
> 团队规模。

**[00:10:09.790]** So almost every labs bet starts as a single person.
> 几乎所有 labs 押注都从一个人开始。

**[00:10:13.930]** It's just one person with their good buddy Claude exploring a really hard problem and
> 就是一个人,带着好搭档 Claude,去探一个特别难的问题、

**[00:10:19.250]** exploring a pretty hard idea.
> 特别难的点子。

**[00:10:21.990]** And at this point, you are not trying to build the best product in the world.
> 这个阶段,你不是要做世界上最好的产品。

**[00:10:26.910]** You are just looking for that little moment of magic.
> 你只是在找那一下魔法时刻。

**[00:10:29.530]** You are looking for that little hint of heat.
> 找那一丝热度。

**[00:10:31.710]** You are looking for, hey, this is a promising idea because there is a little sparkly glimmer
> 你在找:嘿,这个想法有戏,有点小火花——

**[00:10:36.370]** here that we can build into something compelling.
> 我们能把它做成一个好产品。

**[00:10:39.530]** And most labs bets, I'll admit, do not make it past this point.
> 坦白讲,大部分 labs 押注走不到这一步。

**[00:10:43.550]** Most things we end up folding before they get here.
> 大部分我们会在这之前就收摊。

**[00:10:46.470]** And that's totally okay.
> 这完全 OK。

**[00:10:47.550]** This early exploration is usually hours or a few days for most things.
> 早期探索大部分就是几小时或几天。

**[00:10:53.950]** Once we do have a promising spark, we usually scale the team up massively, you know, 300%,
> 一旦真有戏,我们通常把团队大幅扩展——300%——

**[00:10:59.790]** all the way to three people.
> 到 3 个人。

**[00:11:01.330]** So these are not big teams.
> 所以都不是大团队。

**[00:11:03.590]** And the reason why we do that is that we want it to be a very tight group exploring together
> 我们这样做的原因是,希望一个紧密的小组一起探索,

**[00:11:09.430]** with very little collaboration overhead.
> 协作开销极低。

**[00:11:11.830]** If something is so compelling that we're pretty convinced that we're going to be taking it
> 如果某件事确实有戏,我们确信会把它做成产品——

**[00:11:15.550]** to a product, after it's had three people for a while, we might scale it all the way
> 在 3 人一段时间之后,我们最多扩展到

**[00:11:19.150]** up to five people ahead of launch.
> 5 个人,然后发布。

**[00:11:22.310]** So who here works on a team that is smaller than 20 people?
> 在座有谁的团队 < 20 人？

**[00:11:26.930]** Okay.
> 好。

**[00:11:28.470]** Almost everybody, but not everybody.
> 几乎所有人,但不是全部。

**[00:11:30.030]** What about smaller than ten? Five? Smaller than three? Is there anyone here that's totally
> < 10？< 5？< 3？有没有完全单干的？

**[00:11:36.650]** solo? Oh, yeah, a couple people. Three-ish? Two and a half? Four. Okay. So for most of
> 哦,有几位。差不多 3？两个半？4 个？好。Claude Design

**[00:11:44.030]** Claude's design development, it was only three people with Claude, and luckily Claude's a
> 大部分开发阶段,只有 3 个人+ Claude。万幸 Claude 是个不错的

**[00:11:48.650]** pretty good team member. So what makes that possible? I'm sure this is also true of a lot
> 队员。什么让这成为可能？在座很多 solo builder 肯定也深有体会——

**[00:11:54.710]** of the solo builders in this room, everyone on the team does everything. The engineers
> 团队里每个人什么都干。工程师

**[00:12:01.750]** talk to users, PMs write code, designers do data analysis. All of these things are enabled
> 跟用户聊,PM 写代码,设计师做数据分析。Claude 让这些

**[00:12:07.950]** in part with Cloud. And the lines between the roles on this team, they have essentially
> 成为可能。角色之间的界限,在这个团队里,

**[00:12:13.610]** dissolved at this point. You do have your specialization, you do have the unique perspective
> 已经基本消失了。你当然还有自己的专长、有独特的视角,

**[00:12:18.350]** and diversity that you bring to a team, but at any moment, any one of these people on this
> 有你的多样性,但任何时刻,这个团队里任何一个人,

**[00:12:22.970]** team, can talk to ten users, you can realize what the underlying problem is, you can design
> 都可以去跟十个用户聊,搞清底层问题,设计

**[00:12:29.330]** a solution to it, you can ship it to users, you can listen for feedback, you can keep iterating
> 一个解法,推到用户,听反馈,继续迭代——

**[00:12:33.930]** solo if you need to. Quite often that's the case. That's how most features happen. Most
> 需要的话,完全 solo。多数情况正是如此。大部分功能就是这么来的。

**[00:12:38.630]** things on the team are totally solo. And having this small team where everyone can do everything,
> 团队里大部分东西都是纯 solo。每个人都能干所有事,

**[00:12:45.910]** that's the main thing that minimizes coordination overhead for us. Again, most things can be
> 这是我们降低协调开销的关键。同样,大部分事情可以

**[00:12:51.170]** be done solo, but let's say you have to get the whole team together, oftentimes that's
> solo 搞定。但如果真要拉齐全员,通常也是

**[00:12:55.130]** as easy as talking to the person on your left and the person on your right and you're done.
> 跟左右两边的人说一声就完事。

**[00:12:59.690]** It's not a big alignment meeting, it's not something you have to schedule, it's not something
> 不用开大会,不用排日程,不用

**[00:13:02.850]** that you have to wait for. And so this helps us minimize coordination overhead. We've already
> 等。这帮我们把协调开销压到最低。

**[00:13:08.590]** minimized planning and process just by relying on prototypes, and just doing these two things
> 靠原型把规划+流程省掉了。光这两件事

**[00:13:14.830]** alone would let us go pretty quickly, right? They would let us go pretty fast, they would
> 就够我们跑得很快了——把那些大里程碑前期的长周期压掉。

**[00:13:19.810]** take down these big long cycles at the beginning of major milestones. But we go a good bit
> 但我们还能更快,办法是把 loop 里每一步

### 六、Loop 优化：每一步都极激进

**[00:13:26.330]** faster and we go a good bit faster by then really aggressively optimizing every single
> 都极激进地优化。下面这是我们的 loop,可能不适合你,

**[00:13:31.950]** other step in our development process in our loop. So, our loop is our loop. This may not
> 

**[00:13:40.550]** be the right loop for you. That's not the message here. If you're working on hardware,
> 但我们的 loop 很简单:跟用户聊 → 设计功能 → 写代码 → 读反馈 → 循环。

**[00:13:44.530]** this is probably the wrong loop. But our loop is pretty basic. We talk to users. We design
> 做硬件就别套了。我们的 loop 很简单:跟用户聊 → 设计 → 写代码 → 读反馈 → 循环。

**[00:13:49.110]** features, we ship code, we read feedback, and then we do it again. And again, we're just
> 就这么一遍又一遍。重点不是 loop 本身,

**[00:13:53.450]** trying to do this over and over and over and over And the point not the specific loop it not the specific interventions that we did here It rather the thought process that goes into these is why are you doing this
> 重点是背后的思考方式:**这些步骤你能不能让 Claude 干**？

**[00:14:06.310]** work that Claude could do for you a lot of times? Or why haven't you built your own tooling?
> 而不是让 Claude 干？还有**你为什么没自己造工具**？

**[00:14:11.190]** Because every little bit of optimization that you do on your loop is going to pay you back
> 因为每一点优化,在项目里跑 50-100 次 loop 后,

**[00:14:16.170]** if you're running it 50 to 100 times in a project. So for a really simple example, I
> 都会回本。举个最简单的例子——

**[00:14:21.830]** I mentioned that we talk to users every day. We want that to be the easiest thing in the
> 我提过我们每天都跟用户聊。我们希望这是世界上最容易的事。

**[00:14:25.590]** world. We are people. We do things that are easy. We tend to do things that are hard less
> 人都是这样,容易的事常做,难的事少做。

**[00:14:30.330]** often. We want the easiest thing in the world for us to be to talk to users. We did the
> 我们希望跟用户聊是世界上最容易的事。一开始我们做了最基础的事:

**[00:14:35.390]** really basic stuff from the beginning. We create shared Slack channels with anyone using
> 和所有用产品的人建共享 Slack 频道,大量内部 dogfood,跟 dogfooder 们聊新功能。

**[00:14:39.630]** the product. We do a ton of internal dog fooding. We talk to our dog fooders all the time with
> 

**[00:14:44.190]** new features. But then we sped this up by bringing Claude into all of those conversations.
> 然后我们把 Claude 拉进所有这些对话里,加速了一下。

**[00:14:50.590]** So Claude looks at all of our customer conversations.
> Claude 看我们所有的客户对话。

**[00:14:53.350]** It looks for commonalities across conversations.
> 找跨对话的共性。

**[00:14:55.910]** You and I may be talking to different users today who may have the same suggestion.
> 你和我今天可能跟不同用户聊,发现同一条建议。

**[00:14:59.810]** We want Claude to tell us that if we don't talk.
> 我们希望 Claude 替我们指出来。

**[00:15:02.610]** We do it for early analysis.
> 我们做早期分析。

**[00:15:03.990]** We do it for early investigation.
> 我们做早期调研。

**[00:15:06.030]** We have Claude do the first look at all of this stuff for us.
> 让 Claude 替我们先扫一遍所有这些材料。

**[00:15:09.830]** We're the ones having the conversation.
> 人跟人聊是主菜。

**[00:15:11.550]** We don't put Claude between us and the users in that case.
> 但这种情况下,我们不让 Claude 插在我们和用户之间。

**[00:15:15.730]** But we do have it do all of the analysis that we were already doing on every other conversation
> 但我们确实让 Claude 跑所有分析——这些活以前我们自己做——

**[00:15:19.850]** as an immediate follow-up. So talking to users, most important thing, obviously we want to
> 作为直接的后续。所以跟用户聊,最重要,显然——

**[00:15:24.610]** optimize it. Our next thing on here was designing features. And luckily we have a great product
> 我们优化这一点。下一件事是设计功能。巧了,我们正好有

**[00:15:30.730]** for that now. When we got started, we did not have the tool that we wanted for designing
> 用。开始做的时候,我们还没有设计功能想要的那种工具——

**[00:15:37.650]** features. Our team, we would use quad code, we would build prototypes with it, and then
> 我们的团队会用 Claude Code 搭原型,然后把原型丢到

**[00:15:41.610]** when it came time to share that prototype, I would either record a video or we would
> 分享原型的时候,要么录个视频,要么我们

**[00:15:47.030]** put up a branch and say pull down this branch and try it, or you would just commit it into
> 开个分支,说"拉这个分支试一下",要么你直接

**[00:15:52.850]** a sandbox and let other people pull it down and try it. So we wanted to use Cloud Design
> 沙盒里,让其他人拉下来试。所以我们想用 Claude Design

**[00:15:59.850]** to design Cloud Design, and so very quickly Cloud Design got great at designing Cloud Design,
> 来设计 Claude Design——很快 Claude Design 就擅长设计 Claude Design 了,

**[00:16:03.950]** which is fantastic. I have to say, if you could do any developer tool, if you're using
> 太棒了。说真的,如果哪个开发工具能用自己的工具来改进自己——

**[00:16:09.390]** your own developer tool to improve your developer tool, it's the best situation in the world.
> 用工具来改进工具——那是世界上最爽的事。

**[00:16:14.090]** makes things so much easier. There's a lot of other features that you see in Claude design
> 事情变得容易很多。Claude Design 里你看到的很多功能,

**[00:16:18.870]** today from the way it explores code bases, the way it links with GitHub, even multiplayer
> 现在 Claude 在代码库探索、GitHub 集成、甚至更多方面都

**[00:16:24.590]** was something that we built based off of how we were working in Claude design to design
> 这是根据我们自己在 Claude Design 里做设计的流程打造的。

**[00:16:28.970]** Claude design. For multiplayer, we were getting to these scenarios where I might prototype
> 做多人协作是因为这种场景：我可能搭了个原型,

**[00:16:33.810]** something and then share it with somebody else on the team. They would take a look at
> 然后分享给团队里另一个人,他看一下,

**[00:16:38.150]** it and then they would tell me what they thought we should change about it and I would hands
> 他们看完,会告诉我哪些地方该改,我去

**[00:16:42.810]** on keyboard, type it in, and then we would look at what it was. We wanted to take that
> 键盘上敲出来,看效果。我们就想把这

**[00:16:46.610]** step out, and so we made it possible for multiple people to be iterating on the same design at
> 改一改,我们就让多人同时在同一份设计上迭代,

**[00:16:51.270]** the same time. We had originally built that for ourselves to go faster, and then as soon
> 原本是为了我们自己更快,后来发现用户也想要——

**[00:16:55.610]** as we brought the product over to users, the very first request was, can I use this with
> 我们把产品推给用户时,第一波请求就是:能不能用我

**[00:17:01.070]** the rest of the people on my team in real time? So we made a first-class part of the
> 能不能让我跟团队其他人实时协作？我们就把这件事做成了一等公民。

**[00:17:06.190]** product. The next thing that we've done in here is we wanted to optimize how we ship code.
> 接下来我们想优化写代码这一步。

**[00:17:12.130]** So if you've used Cloud Design, you've probably used the handoff to Cloud Code.
> 用过 Claude Design 的话,你大概用过 handoff 到 Claude Code。

**[00:17:16.850]** It's fantastic.
> 太棒了。

**[00:17:17.850]** It's such a good way of getting your designs into production.
> 是把设计稿推上生产的绝佳方式。

**[00:17:20.890]** And that's another feature that we built really to speed up our own workflow.
> 这是又一个为加速我们自己的工作流而做出来的功能。

**[00:17:24.950]** When we started out, we would design our features and then we would export all the files, then
> 刚开始,我们做完设计,导出所有文件,再

**[00:17:30.430]** we would import them into Cloud Code, and then we would retype all of the context that
> 我们要把它们导进 Claude Code,然后把所有上下文重新敲一遍,

**[00:17:35.170]** we had done over multiple turns of conversation with Cloud Design so that Cloud Code would
> 用 Cloud Design 多轮对话后,Claude Code

**[00:17:39.090]** have all that context.
> 才能让 Claude Code 拿到所有上下文。

**[00:17:40.770]** And that was slow.
> 太慢了。

**[00:17:42.270]** We didn't like it being slow, right?
> 我们不喜欢慢,对吧？

**[00:17:44.210]** So we wanted to improve it.
> 所以我们想优化它。

**[00:17:45.990]** And so we originally built this for ourselves and then as soon as we started handing off
> 我们最初是给自己做的,然后一放开 Handoff,

**[00:17:49.550]** the product to other people, the first request was great, now how do I get this into production?
> 把产品推给别人——第一版体验很好,但下一步"怎么推到生产"就卡住了。

**[00:17:55.430]** So first was multiplayer and then right after was okay, now that I have the thing, I want
> 先做了多人协作,然后紧接着——既然我有了这层,

**[00:17:59.010]** to actually ship it.
> 真正发布出去。

**[00:18:00.270]** And so this was another spot where we just had too much friction, we're working for ourselves,
> 这也是一个我们感到摩擦太大的地方——我们

**[00:18:03.930]** we're optimizing for ourselves to get it out there.
> 在为自己优化,好把东西推出去。

**[00:18:08.150]** The last step in our iteration cycle is to read feedback.
> 我们 loop 的最后一步是读反馈。

**[00:18:12.370]** At this point, we get too much feedback for one person to read through all of it.
> 到这个阶段,我们收到的反馈多到一个人读不过来。

**[00:18:16.390]** I think that would be a full-time job.
> 我觉得那会是个全职工作。

**[00:18:19.550]** But we still want to make sure we don't miss anything.
> 但我们还是想确保不漏掉任何东西。

**[00:18:21.530]** And even if we had that one person whose full-time job was to read that feedback, we would probably
> 就算有一个人全职看反馈,我们大概还是会

**[00:18:26.010]** miss things.
> 漏掉一些。

**[00:18:27.010]** And we would miss things because the number of small issues that pop up, you don't want
> 会漏掉,因为冒出来的小问题太多,你想

**[00:18:31.430]** to miss them.
> 不漏都难。

**[00:18:32.430]** It's too much for any one person to keep in their head.
> 一个人脑子里装不下。

**[00:18:34.850]** So to deal with that scale, we ended up building our own feedback clustering tool.
> 所以应对这个规模,我们索性自己做了个反馈聚类工具。

**[00:18:38.910]** It took an afternoon.
> 一个下午搞定。

**[00:18:40.550]** It wasn't something that we were going to wait on.
> 这事我们等不了。

**[00:18:42.770]** We needed to have this.
> 我们必须得有。

**[00:18:44.210]** And so right away, we ended up building this.
> 所以立刻就做了。

**[00:18:46.390]** We rolled this out.
> 我们把它上线了。

**[00:18:47.590]** And now we have Claude taking a look at all feedback that comes in.
> 现在我们让 Claude 看所有进来的反馈。

**[00:18:52.250]** It tries to match it up with system monitors, with system traces.
> 它会跟系统监控、系统 trace 对应起来。

**[00:18:56.470]** It tries to look for common trends across things.
> 会找跨问题的共性趋势。

**[00:18:58.410]** It does initial analysis if things look like a bug.
> 看着像 bug 就做初步分析。

**[00:19:00.950]** We have tried to make all of those initial steps that we would do looking at that feedback
> 我们把所有那些看反馈时要做的初始步骤都做了,

**[00:19:04.430]** automatic to speed ourselves up.
> 自动化,给自己加速。

**[00:19:07.710]** So we also found ourselves we would take everything it said and then we would have to come up
> 后来发现:看完它说的所有内容,我们还得自己

**[00:19:12.850]** with a suggestion after reading through all of that.
> 想出一个建议。

**[00:19:15.610]** So now we have Claude give us a suggestion on how to fix it and then we found ourselves
> 现在 Claude 会给我们修复建议,然后我们发现

**[00:19:19.270]** copying and pasting.
> 复制粘贴。

**[00:19:20.610]** And so we just made that a button to bring it directly over to our development tooling.
> 所以我们就把它做成一个按钮,直接送到开发工具里。

**[00:19:26.030]** So not everything we built worked.
> 所以我们做的不是全都管用。

**[00:19:29.770]** Just because you're really fast doesn't mean you're always really right.
> 快不代表总是对。

**[00:19:33.070]** And we got tons of things wrong as we were building the product.
> 做产品过程中,我们做错了一大堆东西。

**[00:19:36.510]** So I want to tell you about one specific time where we got this wrong.
> 我想跟你们说一个我们具体错过的时刻。

**[00:19:40.310]** And that was we started out early on and we built these really advanced controls.
> 我们早期做了一套非常高级的控件。

**[00:19:47.610]** These gave you really fine control over every single pixel.
> 能让你精细控制每一个像素。

**[00:19:51.530]** You could do anything with these.
> 什么都能干。

**[00:19:53.310]** These were for power users.
> 是给高级用户的。

**[00:19:55.310]** And in our early testers, we had a few power users who were very vocal, gave great feedback
> 早期测试者里,有几个高级用户很活跃,反馈特别好,

**[00:19:59.750]** feedback, and they love this feature. They love this set of tools. And we thought, great,
> 爱死这个功能了。我们想:挺好,

**[00:20:05.430]** we have something good on our hands, all the feedback we're hearing looks great, but then
> 手里有个好东西,所有反馈都很正面——

**[00:20:08.870]** as we dug into the usage, we found that everybody else hated them. Like, didn't just dislike
> 但深挖使用数据后发现,其他人都恨死这玩意儿。不是不喜欢——

**[00:20:15.210]** them, people hated them. They were confusing, they were actively harmful to the product.
> 是恨。难用,对产品反而有害。

**[00:20:20.990]** And so we ripped them out. For us, this took a grand total of one week. So, yes, we got
> 所以我们把它们全砍了。前后一共一周。是的,我们

**[00:20:27.790]** off track, but from idea to course correcting and ripping out the feature and going on to
> 走偏了——但从意识到问题、砍掉这个功能、到做下一件事,

**[00:20:32.730]** the next thing, took us about a week of time.
> 一共花了一周。

**[00:20:36.250]** If we had been doing a quarterly development cycle and we had planned this to do this over
> 如果我们做的是季度开发周期,把它规划到一个季度里,

**[00:20:41.410]** a quarter, we would have been off track for an entire quarter.
> 我们就会偏离整整一个季度。

**[00:20:44.970]** That would have been really bad for the product given that the entire product shipped in less
> 如果发生在整个产品上线不到 [时间] 的情况下,会很糟糕。

**[00:20:48.950]** than a quarter.
> 比一季度还久。

**[00:20:50.450]** For us, it's not necessarily can you always go fast, it's can you always iterate in a
> 对我们来说,关键不是"能不能一直快",而是"能不能在足够短的

**[00:20:54.150]** in a small enough cycle that you able to very quickly find out when you wrong This comes back to the run experiments bullet from earlier So this taught us a couple things
> *[待译]*

**[00:21:05.380]** One, this taught us that we should be a tool
> 第一,这教会我们:我们应该做的是那种

**[00:21:08.000]** that lifts the level of craft for everybody,
> 抬高所有人工艺水准的工具,

**[00:21:11.140]** not just the ceiling on power users.
> 而不只是给高级用户抬高天花板。

**[00:21:13.240]** It also taught us that we want to be as open as possible
> 它还教会我们:要尽量开放——

**[00:21:15.600]** because there will be users that we never meet the full needs of.
> 因为总会有些用户的需求我们满足不了。

**[00:21:19.400]** There's going to be some power user out there
> 总有些高级用户,

**[00:21:21.960]** who wants to do something very specific
> 想做点非常具体的事,

**[00:21:23.400]** that we're not going to support.
> 我们支持不到。

**[00:21:25.080]** That's what convinced us that we want this to be a very open tool.
> 这让我们确信:这必须是个非常开放的工具。

**[00:21:28.160]** That's why if you export from it, you get HTML, CSS, JavaScript.
> 这就是为什么你导出来是 HTML / CSS / JS。

**[00:21:32.980]** That's why we're trying to do more and more integrations that you can take things directly
> 这就是为什么我们拼命做更多集成,让你能直接

**[00:21:37.480]** into other tools.
> 把东西带进其他工具。

**[00:21:38.480]** We haven't talked about this publicly before, but I think this week or next week we're going
> 这个我们还没公开讲过,但我觉得这周或下周我们

**[00:21:42.300]** to be pushing out the ability for any design tool to integrate with quad code.
> 我们正在把"任何设计工具都能和 Claude Code 集成"的能力推出去。

**[00:21:46.840]** Sorry, quad design.
> 抱歉,Claude Design。

**[00:21:48.920]** Just via their existing MCPs.
> 直接通过他们现有的 MCP。

**[00:21:51.320]** So we want this to be a tool where you are able to explore, it lists the level of capability
> 我们想让它是一个:你能自由探索,展现各种能力,

**[00:21:55.560]** for everyone, and then the people that do have very specialized needs, if they have a
> 适合所有人;那些有特殊需求的人,如果有

**[00:21:59.380]** tool of choice, they can just take their designs right into them.
> 用户可以用自己顺手的工具,直接带设计稿进 Claude Code。

**[00:22:02.040]** They're yours.
> 就是你的了。

**[00:22:04.940]** So this slide's fun.
> 这页幻灯片挺有意思。

**[00:22:06.720]** On the left is that first prototype.
> 左边是最初的原型。

**[00:22:10.520]** It's a terminal in a browser, and that's about it.
> 就是个浏览器里的终端,就这点东西。

**[00:22:13.500]** It's not the shiniest thing in the world.
> 并不起眼。

**[00:22:15.720]** This is the level of those early explorations where all you're looking for is that little
> 早期探索就是这个水平,你只找那一丝

**[00:22:20.220]** bit of promise. This is not obviously the final product that launched. On the right,
> 潜力。这显然不是最后上线的产品。右边,

**[00:22:26.100]** it's the final product that launched. There's a lot that separates them. I'll admit this
> 是最后上线的产品。两者差得远。我承认,

**[00:22:30.980]** one on the left, it does have a little bit of promise in it. But 99% of the value came
> 左边的确实有那么点潜力。但 99% 的价值

**[00:22:38.460]** from those ten weeks of iterating and shipping and talking to users every single day. The
> 这 10 周里我们每天迭代、发布、跟用户聊,沉淀下来

**[00:22:44.160]** value came from the experimentation, figuring out what the right thing was to build rather
> 是来自实验——搞清楚该造什么,而不是

**[00:22:49.020]** than knowing in advance this is exactly what we are going to be doing.
> 一开始就确切知道我们要做的是这个。

**[00:22:54.360]** So to put the amount of iteration this team does in perspective, Cloud Design is shipped
> 说个具体数字感受一下这个团队的迭代量——

**[00:22:59.280]** on a Friday, and by the following Monday, we had shipped 62 improvements to the product.
> Claude Design 周五上线,到下周一,我们已经发出去 62 个改进。

**[00:13:26.330]** faster and we go a good bit faster by then really aggressively optimizing every single
> 都极激进地优化。下面这是我们的 loop,可能不适合你,

**[00:13:31.950]** other step in our development process in our loop. So, our loop is our loop. This may not
> 

**[00:13:40.550]** be the right loop for you. That's not the message here. If you're working on hardware,
> 但我们的 loop 很简单:跟用户聊 → 设计功能 → 写代码 → 读反馈 → 循环。

**[00:13:44.530]** this is probably the wrong loop. But our loop is pretty basic. We talk to users. We design
> 做硬件就别套了。我们的 loop 很简单:跟用户聊 → 设计 → 写代码 → 读反馈 → 循环。

**[00:13:49.110]** features, we ship code, we read feedback, and then we do it again. And again, we're just
> 就这么一遍又一遍。重点不是 loop 本身,

**[00:13:53.450]** trying to do this over and over and over and over And the point not the specific loop it not the specific interventions that we did here It rather the thought process that goes into these is why are you doing this
> 重点是背后的思考方式:**这些步骤你能不能让 Claude 干**？

**[00:14:06.310]** work that Claude could do for you a lot of times? Or why haven't you built your own tooling?
> 而不是让 Claude 干？还有**你为什么没自己造工具**？

**[00:14:11.190]** Because every little bit of optimization that you do on your loop is going to pay you back
> 因为每一点优化,在项目里跑 50-100 次 loop 后,

**[00:14:16.170]** if you're running it 50 to 100 times in a project. So for a really simple example, I
> 都会回本。举个最简单的例子——

**[00:14:21.830]** I mentioned that we talk to users every day. We want that to be the easiest thing in the
> 我提过我们每天都跟用户聊。我们希望这是世界上最容易的事。

**[00:14:25.590]** world. We are people. We do things that are easy. We tend to do things that are hard less
> 人都是这样,容易的事常做,难的事少做。

**[00:14:30.330]** often. We want the easiest thing in the world for us to be to talk to users. We did the
> 我们希望跟用户聊是世界上最容易的事。一开始我们做了最基础的事:

**[00:14:35.390]** really basic stuff from the beginning. We create shared Slack channels with anyone using
> 和所有用产品的人建共享 Slack 频道,大量内部 dogfood,跟 dogfooder 们聊新功能。

**[00:14:39.630]** the product. We do a ton of internal dog fooding. We talk to our dog fooders all the time with
> 

**[00:14:44.190]** new features. But then we sped this up by bringing Claude into all of those conversations.
> 然后我们把 Claude 拉进所有这些对话里,加速了一下。

**[00:14:50.590]** So Claude looks at all of our customer conversations.
> Claude 看我们所有的客户对话。

**[00:14:53.350]** It looks for commonalities across conversations.
> 找跨对话的共性。

**[00:14:55.910]** You and I may be talking to different users today who may have the same suggestion.
> 你和我今天可能跟不同用户聊,发现同一条建议。

**[00:14:59.810]** We want Claude to tell us that if we don't talk.
> 我们希望 Claude 替我们指出来。

**[00:15:02.610]** We do it for early analysis.
> 我们做早期分析。

**[00:15:03.990]** We do it for early investigation.
> 我们做早期调研。

**[00:15:06.030]** We have Claude do the first look at all of this stuff for us.
> 让 Claude 替我们先扫一遍所有这些材料。

**[00:15:09.830]** We're the ones having the conversation.
> 人跟人聊是主菜。

**[00:15:11.550]** We don't put Claude between us and the users in that case.
> 但这种情况下,我们不让 Claude 插在我们和用户之间。

**[00:15:15.730]** But we do have it do all of the analysis that we were already doing on every other conversation
> 但我们确实让 Claude 跑所有分析——这些活以前我们自己做——

**[00:15:19.850]** as an immediate follow-up. So talking to users, most important thing, obviously we want to
> 作为直接的后续。所以跟用户聊,最重要,显然——

**[00:15:24.610]** optimize it. Our next thing on here was designing features. And luckily we have a great product
> 我们优化这一点。下一件事是设计功能。巧了,我们正好有

**[00:15:30.730]** for that now. When we got started, we did not have the tool that we wanted for designing
> 用。开始做的时候,我们还没有设计功能想要的那种工具——

**[00:15:37.650]** features. Our team, we would use quad code, we would build prototypes with it, and then
> 我们的团队会用 Claude Code 搭原型,然后把原型丢到

**[00:15:41.610]** when it came time to share that prototype, I would either record a video or we would
> 分享原型的时候,要么录个视频,要么我们

**[00:15:47.030]** put up a branch and say pull down this branch and try it, or you would just commit it into
> 开个分支,说"拉这个分支试一下",要么你直接

**[00:15:52.850]** a sandbox and let other people pull it down and try it. So we wanted to use Cloud Design
> 沙盒里,让其他人拉下来试。所以我们想用 Claude Design

**[00:15:59.850]** to design Cloud Design, and so very quickly Cloud Design got great at designing Cloud Design,
> 来设计 Claude Design——很快 Claude Design 就擅长设计 Claude Design 了,

**[00:16:03.950]** which is fantastic. I have to say, if you could do any developer tool, if you're using
> 太棒了。说真的,如果哪个开发工具能用自己的工具来改进自己——

**[00:16:09.390]** your own developer tool to improve your developer tool, it's the best situation in the world.
> 用工具来改进工具——那是世界上最爽的事。

**[00:16:14.090]** makes things so much easier. There's a lot of other features that you see in Claude design
> 事情变得容易很多。Claude Design 里你看到的很多功能,

**[00:16:18.870]** today from the way it explores code bases, the way it links with GitHub, even multiplayer
> 现在 Claude 在代码库探索、GitHub 集成、甚至更多方面都

**[00:16:24.590]** was something that we built based off of how we were working in Claude design to design
> 这是根据我们自己在 Claude Design 里做设计的流程打造的。

**[00:16:28.970]** Claude design. For multiplayer, we were getting to these scenarios where I might prototype
> 做多人协作是因为这种场景：我可能搭了个原型,

**[00:16:33.810]** something and then share it with somebody else on the team. They would take a look at
> 然后分享给团队里另一个人,他看一下,

**[00:16:38.150]** it and then they would tell me what they thought we should change about it and I would hands
> 他们看完,会告诉我哪些地方该改,我去

**[00:16:42.810]** on keyboard, type it in, and then we would look at what it was. We wanted to take that
> 键盘上敲出来,看效果。我们就想把这

**[00:16:46.610]** step out, and so we made it possible for multiple people to be iterating on the same design at
> 改一改,我们就让多人同时在同一份设计上迭代,

**[00:16:51.270]** the same time. We had originally built that for ourselves to go faster, and then as soon
> 原本是为了我们自己更快,后来发现用户也想要——

**[00:16:55.610]** as we brought the product over to users, the very first request was, can I use this with
> 我们把产品推给用户时,第一波请求就是:能不能用我

**[00:17:01.070]** the rest of the people on my team in real time? So we made a first-class part of the
> 能不能让我跟团队其他人实时协作？我们就把这件事做成了一等公民。

**[00:17:06.190]** product. The next thing that we've done in here is we wanted to optimize how we ship code.
> 接下来我们想优化写代码这一步。

**[00:17:12.130]** So if you've used Cloud Design, you've probably used the handoff to Cloud Code.
> 用过 Claude Design 的话,你大概用过 handoff 到 Claude Code。

**[00:17:16.850]** It's fantastic.
> 太棒了。

**[00:17:17.850]** It's such a good way of getting your designs into production.
> 是把设计稿推上生产的绝佳方式。

**[00:17:20.890]** And that's another feature that we built really to speed up our own workflow.
> 这是又一个为加速我们自己的工作流而做出来的功能。

**[00:17:24.950]** When we started out, we would design our features and then we would export all the files, then
> 刚开始,我们做完设计,导出所有文件,再

**[00:17:30.430]** we would import them into Cloud Code, and then we would retype all of the context that
> 我们要把它们导进 Claude Code,然后把所有上下文重新敲一遍,

**[00:17:35.170]** we had done over multiple turns of conversation with Cloud Design so that Cloud Code would
> 用 Cloud Design 多轮对话后,Claude Code

**[00:17:39.090]** have all that context.
> 才能让 Claude Code 拿到所有上下文。

**[00:17:40.770]** And that was slow.
> 太慢了。

**[00:17:42.270]** We didn't like it being slow, right?
> 我们不喜欢慢,对吧？

**[00:17:44.210]** So we wanted to improve it.
> 所以我们想优化它。

**[00:17:45.990]** And so we originally built this for ourselves and then as soon as we started handing off
> 我们最初是给自己做的,然后一放开 Handoff,

**[00:17:49.550]** the product to other people, the first request was great, now how do I get this into production?
> 把产品推给别人——第一版体验很好,但下一步"怎么推到生产"就卡住了。

**[00:17:55.430]** So first was multiplayer and then right after was okay, now that I have the thing, I want
> 先做了多人协作,然后紧接着——既然我有了这层,

**[00:17:59.010]** to actually ship it.
> 真正发布出去。

**[00:18:00.270]** And so this was another spot where we just had too much friction, we're working for ourselves,
> 这也是一个我们感到摩擦太大的地方——我们

**[00:18:03.930]** we're optimizing for ourselves to get it out there.
> 在为自己优化,好把东西推出去。

**[00:18:08.150]** The last step in our iteration cycle is to read feedback.
> 我们 loop 的最后一步是读反馈。

**[00:18:12.370]** At this point, we get too much feedback for one person to read through all of it.
> 到这个阶段,我们收到的反馈多到一个人读不过来。

**[00:18:16.390]** I think that would be a full-time job.
> 我觉得那会是个全职工作。

**[00:18:19.550]** But we still want to make sure we don't miss anything.
> 但我们还是想确保不漏掉任何东西。

**[00:18:21.530]** And even if we had that one person whose full-time job was to read that feedback, we would probably
> 就算有一个人全职看反馈,我们大概还是会

**[00:18:26.010]** miss things.
> 漏掉一些。

**[00:18:27.010]** And we would miss things because the number of small issues that pop up, you don't want
> 会漏掉,因为冒出来的小问题太多,你想

**[00:18:31.430]** to miss them.
> 不漏都难。

**[00:18:32.430]** It's too much for any one person to keep in their head.
> 一个人脑子里装不下。

**[00:18:34.850]** So to deal with that scale, we ended up building our own feedback clustering tool.
> 所以应对这个规模,我们索性自己做了个反馈聚类工具。

**[00:18:38.910]** It took an afternoon.
> 一个下午搞定。

**[00:18:40.550]** It wasn't something that we were going to wait on.
> 这事我们等不了。

**[00:18:42.770]** We needed to have this.
> 我们必须得有。

**[00:18:44.210]** And so right away, we ended up building this.
> 所以立刻就做了。

**[00:18:46.390]** We rolled this out.
> 我们把它上线了。

**[00:18:47.590]** And now we have Claude taking a look at all feedback that comes in.
> 现在我们让 Claude 看所有进来的反馈。

**[00:18:52.250]** It tries to match it up with system monitors, with system traces.
> 它会跟系统监控、系统 trace 对应起来。

**[00:18:56.470]** It tries to look for common trends across things.
> 会找跨问题的共性趋势。

**[00:18:58.410]** It does initial analysis if things look like a bug.
> 看着像 bug 就做初步分析。

**[00:19:00.950]** We have tried to make all of those initial steps that we would do looking at that feedback
> 我们把所有那些看反馈时要做的初始步骤都做了,

**[00:19:04.430]** automatic to speed ourselves up.
> 自动化,给自己加速。

**[00:19:07.710]** So we also found ourselves we would take everything it said and then we would have to come up
> 后来发现:看完它说的所有内容,我们还得自己

**[00:19:12.850]** with a suggestion after reading through all of that.
> 想出一个建议。

**[00:19:15.610]** So now we have Claude give us a suggestion on how to fix it and then we found ourselves
> 现在 Claude 会给我们修复建议,然后我们发现

**[00:19:19.270]** copying and pasting.
> 复制粘贴。

**[00:19:20.610]** And so we just made that a button to bring it directly over to our development tooling.
> 所以我们就把它做成一个按钮,直接送到开发工具里。

**[00:19:26.030]** So not everything we built worked.
> 所以我们做的不是全都管用。

**[00:19:29.770]** Just because you're really fast doesn't mean you're always really right.
> 快不代表总是对。

**[00:19:33.070]** And we got tons of things wrong as we were building the product.
> 做产品过程中,我们做错了一大堆东西。

**[00:19:36.510]** So I want to tell you about one specific time where we got this wrong.
> 我想跟你们说一个我们具体错过的时刻。

**[00:19:40.310]** And that was we started out early on and we built these really advanced controls.
> 我们早期做了一套非常高级的控件。

**[00:19:47.610]** These gave you really fine control over every single pixel.
> 能让你精细控制每一个像素。

**[00:19:51.530]** You could do anything with these.
> 什么都能干。

**[00:19:53.310]** These were for power users.
> 是给高级用户的。

**[00:19:55.310]** And in our early testers, we had a few power users who were very vocal, gave great feedback
> 早期测试者里,有几个高级用户很活跃,反馈特别好,

**[00:19:59.750]** feedback, and they love this feature. They love this set of tools. And we thought, great,
> 爱死这个功能了。我们想:挺好,

**[00:20:05.430]** we have something good on our hands, all the feedback we're hearing looks great, but then
> 手里有个好东西,所有反馈都很正面——

**[00:20:08.870]** as we dug into the usage, we found that everybody else hated them. Like, didn't just dislike
> 但深挖使用数据后发现,其他人都恨死这玩意儿。不是不喜欢——

**[00:20:15.210]** them, people hated them. They were confusing, they were actively harmful to the product.
> 是恨。难用,对产品反而有害。

**[00:20:20.990]** And so we ripped them out. For us, this took a grand total of one week. So, yes, we got
> 所以我们把它们全砍了。前后一共一周。是的,我们

**[00:20:27.790]** off track, but from idea to course correcting and ripping out the feature and going on to
> 走偏了——但从意识到问题、砍掉这个功能、到做下一件事,

**[00:20:32.730]** the next thing, took us about a week of time.
> 一共花了一周。

**[00:20:36.250]** If we had been doing a quarterly development cycle and we had planned this to do this over
> 如果我们做的是季度开发周期,把它规划到一个季度里,

**[00:20:41.410]** a quarter, we would have been off track for an entire quarter.
> 我们就会偏离整整一个季度。

**[00:20:44.970]** That would have been really bad for the product given that the entire product shipped in less
> 如果发生在整个产品上线不到 [时间] 的情况下,会很糟糕。

**[00:20:48.950]** than a quarter.
> 比一季度还久。

**[00:20:50.450]** For us, it's not necessarily can you always go fast, it's can you always iterate in a
> 对我们来说,关键不是"能不能一直快",而是"能不能在足够短的

**[00:21:05.380]** One, this taught us that we should be a tool
> 第一,这教会我们:我们应该做的是那种

**[00:21:08.000]** that lifts the level of craft for everybody,
> 抬高所有人工艺水准的工具,

**[00:21:11.140]** not just the ceiling on power users.
> 而不只是给高级用户抬高天花板。

**[00:21:13.240]** It also taught us that we want to be as open as possible
> 它还教会我们:要尽量开放——

**[00:21:15.600]** because there will be users that we never meet the full needs of.
> 因为总会有些用户的需求我们满足不了。

**[00:21:19.400]** There's going to be some power user out there
> 总有些高级用户,

**[00:21:21.960]** who wants to do something very specific
> 想做点非常具体的事,

**[00:21:23.400]** that we're not going to support.
> 我们支持不到。

**[00:21:25.080]** That's what convinced us that we want this to be a very open tool.
> 这让我们确信:这必须是个非常开放的工具。

**[00:21:28.160]** That's why if you export from it, you get HTML, CSS, JavaScript.
> 这就是为什么你导出来是 HTML / CSS / JS。

**[00:21:32.980]** That's why we're trying to do more and more integrations that you can take things directly
> 这就是为什么我们拼命做更多集成,让你能直接

**[00:21:37.480]** into other tools.
> 把东西带进其他工具。

**[00:21:38.480]** We haven't talked about this publicly before, but I think this week or next week we're going
> 这个我们还没公开讲过,但我觉得这周或下周我们

**[00:21:42.300]** to be pushing out the ability for any design tool to integrate with quad code.
> 我们正在把"任何设计工具都能和 Claude Code 集成"的能力推出去。

**[00:21:46.840]** Sorry, quad design.
> 抱歉,Claude Design。

**[00:21:48.920]** Just via their existing MCPs.
> 直接通过他们现有的 MCP。

**[00:21:51.320]** So we want this to be a tool where you are able to explore, it lists the level of capability
> 我们想让它是一个:你能自由探索,展现各种能力,

**[00:21:55.560]** for everyone, and then the people that do have very specialized needs, if they have a
> 适合所有人;那些有特殊需求的人,如果有

**[00:21:59.380]** tool of choice, they can just take their designs right into them.
> 用户可以用自己顺手的工具,直接带设计稿进 Claude Code。

**[00:22:02.040]** They're yours.
> 就是你的了。

**[00:22:04.940]** So this slide's fun.
> 这页幻灯片挺有意思。

**[00:22:06.720]** On the left is that first prototype.
> 左边是最初的原型。

**[00:22:10.520]** It's a terminal in a browser, and that's about it.
> 就是个浏览器里的终端,就这点东西。

**[00:22:13.500]** It's not the shiniest thing in the world.
> 并不起眼。

**[00:22:15.720]** This is the level of those early explorations where all you're looking for is that little
> 早期探索就是这个水平,你只找那一丝

**[00:22:20.220]** bit of promise. This is not obviously the final product that launched. On the right,
> 潜力。这显然不是最后上线的产品。右边,

**[00:22:26.100]** it's the final product that launched. There's a lot that separates them. I'll admit this
> 是最后上线的产品。两者差得远。我承认,

**[00:22:30.980]** one on the left, it does have a little bit of promise in it. But 99% of the value came
> 左边的确实有那么点潜力。但 99% 的价值

**[00:22:38.460]** from those ten weeks of iterating and shipping and talking to users every single day. The
> 这 10 周里我们每天迭代、发布、跟用户聊,沉淀下来

**[00:22:44.160]** value came from the experimentation, figuring out what the right thing was to build rather
> 是来自实验——搞清楚该造什么,而不是

**[00:22:49.020]** than knowing in advance this is exactly what we are going to be doing.
> 一开始就确切知道我们要做的是这个。

**[00:22:54.360]** So to put the amount of iteration this team does in perspective, Cloud Design is shipped
> 说个具体数字感受一下这个团队的迭代量——

**[00:22:59.280]** on a Friday, and by the following Monday, we had shipped 62 improvements to the product.
> Claude Design 周五上线,到下周一,我们已经发出去 62 个改进。

### 七、反直觉 + 3 个明天就能试的建议

**[00:23:05.640]** That's a good number given the size of the team we talked about earlier.
> 考虑到团队就 3 个人,这个数字相当可以。

**[00:23:10.260]** And we made the product more token efficient.
> 我们让产品更省 token。

**[00:23:13.420]** We improved its ability to handle images, we made it better at exploring code bases,
> 我们改善了它处理图片的能力、探索代码库的能力,

**[00:23:19.200]** we made most exports instant.
> 让大部分导出变成瞬时。

**[00:23:21.100]** It's a pretty long list and was all based off of user feedback that we got on launch
> 这个列表很长,全是我们从上线当天用户反馈里

**[00:23:25.240]** day.
> 提炼出来的。

**[00:23:26.240]** Now, this was not a Herculean effort.
> 这不是什么大动作。

**[00:23:29.300]** This was not something that required all-nighters from everybody.
> 不需要大家通宵达旦。

**[00:23:33.460]** This was something that was very natural because the team had built up the processes and the
> 之所以自然,是因为团队早已把流程和

**[00:23:37.060]** muscles and the practice of doing this every single day for ten weeks prior.
> 这是前 10 周每天都在做的肌肉记忆和实践。

**[00:23:41.900]** This became a quick, very normal way of working for us.
> 这已经是我们工作方式里又快又正常的一部分。

**[00:23:45.600]** I mentioned earlier that quad design has been live for one month.
> 我之前提过,Claude Design 上线已经 1 个月。

**[00:23:50.480]** And so, also, you may have seen this, but last night we doubled token limits for the
> 另外,你们可能看到了——昨晚我们把产品的 token 上限

**[00:23:56.140]** product.
> 翻倍了。

**[00:23:57.140]** So, one of the pieces of feedback that we heard was that people liked it, they wanted
> 我们听到的反馈是:大家喜欢它,想用得更多,

**[00:23:59.800]** to use it more, so we're making that easier.
> 我们就让这事更方便。

**[00:24:01.520]** So, that's across all subscription plans.
> 所有订阅计划都生效。

**[00:24:06.020]** Before we close, I want to share one of the more counterintuitive things we've learned
> 在结束前,我想分享一个我们在 labs 学到的反直觉的事:

**[00:24:08.940]** working in labs, and that is that you do not want to work on the thing that already works.
> 你**不要**做已经能跑的东西。

**[00:24:14.700]** You often want to prototype the thing that almost works.
> 你通常应该做那个"几乎能跑"的东西的原型。

**[00:24:18.500]** And the reason why you do that is because the models are improving so rapidly.
> 原因是模型进步太快了。

**[00:24:24.240]** The level of intelligence keeps going up.
> 智能水平一直在涨。

**[00:24:28.300]** And the next model may just fix the issues that you cannot solve via engineering.
> 下一个模型很可能直接解决你工程上搞不定的问题。

**[00:24:33.500]** We had this with Cloud Design.
> Claude Design 就是这样。

**[00:24:34.740]** were a bunch of issues in that early prototype that we did not solve. We did not fix them
> 早期原型里有一堆问题我们没解决。不是靠聪明的工程,也不是

**[00:24:40.080]** with clever engineering, we did not fix them with amazing insights, we fixed them with
> 靠神来之笔——是 Opus 4.7 一出来就解决了。

**[00:24:46.060]** Opus 4.7 coming out. And that's going to be true of a lot of things that everyone in
> 在座各位一起做的大部分事,都会是这样。

**[00:24:51.800]** this room that we all work on together. The model releases are a tide that lifts all boats.
> 模型发布就是涨潮,水涨船高。

**[00:24:57.740]** They do a lot for you. So, remember, early on, you're just looking for that hint of magic.
> 它帮你很多。所以记住:早期,你只是在找那一丝魔法。

**[00:25:03.240]** You're not looking for something that works in full, that works completely, that handles
> 你不是在找一个完全能跑、能处理所有

**[00:25:07.220]** every edge case.
> 边界情况的东西。

**[00:25:08.220]** You're looking for something that could become that in the future.
> 你是在找那个**未来能成为那样**的东西。

**[00:25:11.820]** And so that's why when you find it, you want to start exploring, start building, start
> 所以一旦找到,你就要开始探索、开始建、开始

**[00:25:16.560]** bringing in front of users and figuring out the shape of the product that works.
> 放到用户面前,去摸清好用的产品形态。

**[00:25:20.000]** Because the shape is the most important thing and the thing that we all get wrong when we
> 因为形态是最重要的——也是我们一开始最容易搞错的。

**[00:25:23.180]** first start.
> 

**[00:25:24.180]** We all have to iterate on it.
> 谁都得迭代。

**[00:25:26.040]** So there's three concrete things that you can try tomorrow from this talk if you want.
> 所以你如果愿意,明天就能试三件具体的事。

**[00:25:33.000]** if there's nothing else you took away from it. The first is go ahead, next time you're
> 如果其他都没记住,这三件也行。第一——下次

**[00:25:36.500]** going to write a PRD, skip it. Don't write it. Instead, just talk with Claude, talk with
> 别写 PRD——别写。跟 Claude 聊,跟同事聊,

**[00:25:42.100]** somebody on your team and take the transcript and don't talk about specifically what the
> 把转录稿拿过来,**不要具体到按钮位置**,而是讨论:

**[00:25:45.820]** feature is, what buttons there are. Instead, just spend time talking about why you're trying
> 功能是什么,按钮在哪。换成:花时间聊你为什么

**[00:25:51.000]** to solve this problem. What are the characteristics of a good solution? And give that to Claude
> 问题是什么？好解法的特征是什么？把这些喂给 Claude

**[00:25:56.800]** Design. Give that to Claude. Ask it to give you three variations on a prototype that might
> Design。让它给你三个原型方案的变体,

**[00:26:01.960]** solve that. See if that works for you. The second, pick something that you've been waiting
> 想解这个问题。试一下。第二,挑一个你一直等的东西——

**[00:26:07.720]** for. It could be feedback clustering like we did. It could be a new analysis tool. And
> 像我们做的反馈聚类,或者新分析工具——

**[00:26:12.840]** just build it one afternoon. Everyone waits on tools when at this point internal tooling,
> 一个下午搭出来。大家都等工具,但在现在这个时代,

**[00:26:19.280]** building your own stuff, is rapid. It's very fast. So go ahead and scratch your own itch.
> 内部工具、自己造轮子,非常快。去挠自己的痒。

**[00:26:24.140]** You will be happy that you did. It will pay itself off very quickly. The third, and this
> 你会庆幸自己这么做了。回报非常快。第三,

**[00:26:29.020]** This one looks simple but I think this is the hardest.
> 这条看起来简单,其实是最难的。

**[00:26:31.980]** Take one real feature request.
> 拿一个真实的功能需求。

**[00:26:34.160]** I don't mean like a small bug fix or a padding change.
> 不是小 bug、padding 那种。

**[00:26:37.160]** Take one real feature request from a user and turn it around in 24 hours, get the idea in
> 拿一个用户提的真实功能需求,24 小时内做出来,让用户看到,

**[00:26:43.700]** front of them and follow up with them for feedback.
> 然后跟进他的反馈。

**[00:26:46.220]** The reason why I bring that up is not this urge to go faster.
> 我提这一点,不是因为我想催你更快。

**[00:26:48.940]** It's because the first time you do this, if you're not doing this already, you're going
> 而是因为你第一次这么做时,如果你还没做过,你就会

**[00:26:52.920]** to find that there are a bunch of roadblocks in your existing process and the existing
> 发现你现有的流程、现有的

**[00:26:57.500]** way that you build software.
> 你做软件的方式。

**[00:26:58.960]** if you have been on a longer timeline. That could be everything from the way that you
> 如果你一直在用更长的周期,这能改变

**[00:27:02.680]** do deploys, the way that you ask somebody on your team to review your code, that could
> 部署方式、让同事 review 代码的方式……这些地方

**[00:27:08.060]** be a whole host of things. So going through this once really helps. And I wouldn't try
> 很多东西。哪怕只做一次也很有帮助。我不建议

**[00:27:13.540]** to do all three of these at once. I would layer these on. Each one is going to teach
> 三件一起做,一件一件加,每件都会

**[00:27:18.620]** you something a little bit different that helps you move a little bit faster. This is
> 这给你一些不一样的启示,让你动得快一点。这就是

**[00:27:22.880]** the last show of hands, I promise. Who is going to try number one? A lot. Two? Three?
> 最后一个举手,我保证。试试第一件？很多人。第二件？

**[00:27:32.960]** Okay. Thank you so much. That's the talk. Thank you for your time. I would love to talk
> 好。非常感谢,讲完了。谢谢大家的时间。我很想跟

**[00:27:39.660]** to folks who have used the product or even those that haven't. I'm going to be by the
> 用过或没用过这个产品的人聊聊。我会

**[00:27:42.820]** demo booth for most of the day for Collade Design. It's down at the end of the hallway.
> 我今天一整天基本都会在 Claude Design 展位,走到走廊尽头就是。

**[00:27:46.920]** So please come find me, tap me on my shoulder, come complain to me or tell me what surprised
> 来找我,拍我肩膀,吐槽也好,告诉我哪里让你惊讶也好——

**[00:27:51.200]** you. I'd love that. So thank you so much.
> 欢什么也好,我都欢迎。谢谢大家。

**[00:23:05.640]** That's a good number given the size of the team we talked about earlier.
> 考虑到团队就 3 个人,这个数字相当可以。

**[00:23:10.260]** And we made the product more token efficient.
> 我们让产品更省 token。

**[00:23:13.420]** We improved its ability to handle images, we made it better at exploring code bases,
> 我们改善了它处理图片的能力、探索代码库的能力,

**[00:23:19.200]** we made most exports instant.
> 让大部分导出变成瞬时。

**[00:23:21.100]** It's a pretty long list and was all based off of user feedback that we got on launch
> 这个列表很长,全是我们从上线当天用户反馈里

**[00:23:25.240]** day.
> 提炼出来的。

**[00:23:26.240]** Now, this was not a Herculean effort.
> 这不是什么大动作。

**[00:23:29.300]** This was not something that required all-nighters from everybody.
> 不需要大家通宵达旦。

**[00:23:33.460]** This was something that was very natural because the team had built up the processes and the
> 之所以自然,是因为团队早已把流程和

**[00:23:37.060]** muscles and the practice of doing this every single day for ten weeks prior.
> 这是前 10 周每天都在做的肌肉记忆和实践。

**[00:23:41.900]** This became a quick, very normal way of working for us.
> 这已经是我们工作方式里又快又正常的一部分。

**[00:23:45.600]** I mentioned earlier that quad design has been live for one month.
> 我之前提过,Claude Design 上线已经 1 个月。

**[00:23:50.480]** And so, also, you may have seen this, but last night we doubled token limits for the
> 另外,你们可能看到了——昨晚我们把产品的 token 上限

**[00:23:56.140]** product.
> 翻倍了。

**[00:23:57.140]** So, one of the pieces of feedback that we heard was that people liked it, they wanted
> 我们听到的反馈是:大家喜欢它,想用得更多,

**[00:23:59.800]** to use it more, so we're making that easier.
> 我们就让这事更方便。

**[00:24:01.520]** So, that's across all subscription plans.
> 所有订阅计划都生效。

**[00:24:06.020]** Before we close, I want to share one of the more counterintuitive things we've learned
> 在结束前,我想分享一个我们在 labs 学到的反直觉的事:

**[00:24:08.940]** working in labs, and that is that you do not want to work on the thing that already works.
> 你**不要**做已经能跑的东西。

**[00:24:14.700]** You often want to prototype the thing that almost works.
> 你通常应该做那个"几乎能跑"的东西的原型。

**[00:24:18.500]** And the reason why you do that is because the models are improving so rapidly.
> 原因是模型进步太快了。

**[00:24:24.240]** The level of intelligence keeps going up.
> 智能水平一直在涨。

**[00:24:28.300]** And the next model may just fix the issues that you cannot solve via engineering.
> 下一个模型很可能直接解决你工程上搞不定的问题。

**[00:24:33.500]** We had this with Cloud Design.
> Claude Design 就是这样。

**[00:24:34.740]** were a bunch of issues in that early prototype that we did not solve. We did not fix them
> 早期原型里有一堆问题我们没解决。不是靠聪明的工程,也不是

**[00:24:40.080]** with clever engineering, we did not fix them with amazing insights, we fixed them with
> 靠神来之笔——是 Opus 4.7 一出来就解决了。

**[00:24:46.060]** Opus 4.7 coming out. And that's going to be true of a lot of things that everyone in
> 在座各位一起做的大部分事,都会是这样。

**[00:24:51.800]** this room that we all work on together. The model releases are a tide that lifts all boats.
> 模型发布就是涨潮,水涨船高。

**[00:24:57.740]** They do a lot for you. So, remember, early on, you're just looking for that hint of magic.
> 它帮你很多。所以记住:早期,你只是在找那一丝魔法。

**[00:25:03.240]** You're not looking for something that works in full, that works completely, that handles
> 你不是在找一个完全能跑、能处理所有

**[00:25:07.220]** every edge case.
> 边界情况的东西。

**[00:25:08.220]** You're looking for something that could become that in the future.
> 你是在找那个**未来能成为那样**的东西。

**[00:25:11.820]** And so that's why when you find it, you want to start exploring, start building, start
> 所以一旦找到,你就要开始探索、开始建、开始

**[00:25:16.560]** bringing in front of users and figuring out the shape of the product that works.
> 放到用户面前,去摸清好用的产品形态。

**[00:25:20.000]** Because the shape is the most important thing and the thing that we all get wrong when we
> 因为形态是最重要的——也是我们一开始最容易搞错的。

**[00:25:23.180]** first start.
> 

**[00:25:24.180]** We all have to iterate on it.
> 谁都得迭代。

**[00:25:26.040]** So there's three concrete things that you can try tomorrow from this talk if you want.
> 所以你如果愿意,明天就能试三件具体的事。

**[00:25:33.000]** if there's nothing else you took away from it. The first is go ahead, next time you're
> 如果其他都没记住,这三件也行。第一——下次

**[00:25:36.500]** going to write a PRD, skip it. Don't write it. Instead, just talk with Claude, talk with
> 别写 PRD——别写。跟 Claude 聊,跟同事聊,

**[00:25:42.100]** somebody on your team and take the transcript and don't talk about specifically what the
> 把转录稿拿过来,**不要具体到按钮位置**,而是讨论:

**[00:25:45.820]** feature is, what buttons there are. Instead, just spend time talking about why you're trying
> 功能是什么,按钮在哪。换成:花时间聊你为什么

**[00:25:51.000]** to solve this problem. What are the characteristics of a good solution? And give that to Claude
> 问题是什么？好解法的特征是什么？把这些喂给 Claude

**[00:25:56.800]** Design. Give that to Claude. Ask it to give you three variations on a prototype that might
> Design。让它给你三个原型方案的变体,

**[00:26:01.960]** solve that. See if that works for you. The second, pick something that you've been waiting
> 想解这个问题。试一下。第二,挑一个你一直等的东西——

**[00:26:07.720]** for. It could be feedback clustering like we did. It could be a new analysis tool. And
> 像我们做的反馈聚类,或者新分析工具——

**[00:26:12.840]** just build it one afternoon. Everyone waits on tools when at this point internal tooling,
> 一个下午搭出来。大家都等工具,但在现在这个时代,

**[00:26:19.280]** building your own stuff, is rapid. It's very fast. So go ahead and scratch your own itch.
> 内部工具、自己造轮子,非常快。去挠自己的痒。

**[00:26:24.140]** You will be happy that you did. It will pay itself off very quickly. The third, and this
> 你会庆幸自己这么做了。回报非常快。第三,

**[00:26:29.020]** This one looks simple but I think this is the hardest.
> 这条看起来简单,其实是最难的。

**[00:26:31.980]** Take one real feature request.
> 拿一个真实的功能需求。

**[00:26:34.160]** I don't mean like a small bug fix or a padding change.
> 不是小 bug、padding 那种。

**[00:26:37.160]** Take one real feature request from a user and turn it around in 24 hours, get the idea in
> 拿一个用户提的真实功能需求,24 小时内做出来,让用户看到,

**[00:26:43.700]** front of them and follow up with them for feedback.
> 然后跟进他的反馈。

**[00:26:46.220]** The reason why I bring that up is not this urge to go faster.
> 我提这一点,不是因为我想催你更快。

**[00:26:48.940]** It's because the first time you do this, if you're not doing this already, you're going
> 而是因为你第一次这么做时,如果你还没做过,你就会

**[00:26:52.920]** to find that there are a bunch of roadblocks in your existing process and the existing
> 发现你现有的流程、现有的

**[00:26:57.500]** way that you build software.
> 你做软件的方式。

**[00:26:58.960]** if you have been on a longer timeline. That could be everything from the way that you
> 如果你一直在用更长的周期,这能改变

**[00:27:02.680]** do deploys, the way that you ask somebody on your team to review your code, that could
> 部署方式、让同事 review 代码的方式……这些地方

**[00:27:08.060]** be a whole host of things. So going through this once really helps. And I wouldn't try
> 很多东西。哪怕只做一次也很有帮助。我不建议

**[00:27:13.540]** to do all three of these at once. I would layer these on. Each one is going to teach
> 三件一起做,一件一件加,每件都会

**[00:27:18.620]** you something a little bit different that helps you move a little bit faster. This is
> 这给你一些不一样的启示,让你动得快一点。这就是

**[00:27:22.880]** the last show of hands, I promise. Who is going to try number one? A lot. Two? Three?
> 最后一个举手,我保证。试试第一件？很多人。第二件？

**[00:27:32.960]** Okay. Thank you so much. That's the talk. Thank you for your time. I would love to talk
> 好。非常感谢,讲完了。谢谢大家的时间。我很想跟

**[00:27:39.660]** to folks who have used the product or even those that haven't. I'm going to be by the
> 用过或没用过这个产品的人聊聊。我会

**[00:27:42.820]** demo booth for most of the day for Collade Design. It's down at the end of the hallway.
> 我今天一整天基本都会在 Claude Design 展位,走到走廊尽头就是。

**[00:27:46.920]** So please come find me, tap me on my shoulder, come complain to me or tell me what surprised
> 来找我,拍我肩膀,吐槽也好,告诉我哪里让你惊讶也好——

**[00:27:51.200]** you. I'd love that. So thank you so much.
> 欢什么也好,我都欢迎。谢谢大家。


## 英文原文（带时间戳）

> 段落格式：`[时:分:秒] 文字内容`

**[00:00:00.000]** Dan Carey Reviewer

**[00:00:07.000]** How is everybody? A little bit more than that. Come on, guys. How is everybody?

**[00:00:18.000]** Thank you. Thank you.

**[00:00:20.000]** So, I'm Dan Carey. I am a product manager. I lead a product within Anthropic Labs.

**[00:00:25.000]** Today, we're going to talk a little bit about cloud design.

**[00:00:28.000]** Can I get a quick show of hands?

**[00:00:29.760]** Who here has already tried Claude Design?

**[00:00:33.300]** OK, great.

**[00:00:34.800]** For those of you who haven't had a chance yet, Claude Design,

**[00:00:37.720]** it's a new product from Anthropik Labs,

**[00:00:40.160]** and it lets you collaborate with Claude

**[00:00:41.900]** to create polished visual artifacts.

**[00:00:43.960]** These can be designs, prototypes, slide, one-pagers, more.

**[00:00:49.440]** You can do a lot of different things with this product.

**[00:00:52.060]** And as of, I think it's yesterday,

**[00:00:54.880]** the product's been live in research preview for one month.

**[00:00:57.900]** So we're pretty happy about that.

**[00:00:59.740]** Today, I'm going to tell you a little bit

**[00:01:01.560]** about how a very small team, it was three people

**[00:01:05.340]** for most of the development, built Claude Design

**[00:01:08.000]** in about 10 weeks from idea to launching the product.

**[00:01:11.140]** And the reason I'm going to share these things with you

**[00:01:13.140]** is because the most common question I get asked

**[00:01:15.320]** is, why did you decide to start working on this?

**[00:01:17.520]** How did you see that this was an opportunity

**[00:01:19.660]** for building a new AI-enabled product?

**[00:01:22.360]** How'd you build it?

**[00:01:23.280]** How'd you launch it?

**[00:01:25.200]** So everything I'm going to cover here,

**[00:01:26.760]** There is no real secret sauce.

**[00:01:28.720]** These are all things that work well for us.

**[00:01:30.960]** Take what you like.

**[00:01:31.760]** You can do a lot of these things tomorrow.

**[00:01:35.400]** To start, I want to tell you about what Anthropic Labs is.

**[00:01:38.560]** It's kind of funny.

**[00:01:39.180]** It's a lab inside a frontier lab.

**[00:01:42.540]** We don't have any labs within Anthropic Labs,

**[00:01:44.280]** but it is labs quite a ways down.

**[00:01:47.080]** The way that we usually talk about it is as a bet factory.

**[00:01:51.480]** And by that, I mean we have very small teams

**[00:01:53.900]** exploring the frontier of what the models can do

**[00:01:56.780]** and making bets about whether or not something will work.

**[00:02:00.320]** We run experiments to find out what works.

**[00:02:03.620]** We double down on the things that are working.

**[00:02:05.920]** We fold the things that are not working.

**[00:02:08.860]** And at any given time, we might have a dozen small teams

**[00:02:12.480]** exploring different concepts.

**[00:02:15.320]** So it's lots of exploration, a small number

**[00:02:18.440]** of really high-conviction releases of things

**[00:02:20.520]** that we think can be moonshots or change how people work

**[00:02:23.720]** with the models.

**[00:02:26.140]** There's a few products that came from here that you may know.

**[00:02:28.940]** Cloud Code came out of labs.

**[00:02:30.340]** Design came out of labs.

**[00:02:31.480]** MCP came out of labs.

**[00:02:32.620]** Skills came out of labs.

**[00:02:34.480]** We had the Cloud and Chrome extension.

**[00:02:36.480]** We had our work on hands-free audio come out of labs.

**[00:02:39.520]** So this is a process that's worked pretty well for us.

**[00:02:42.660]** And we just keep turning the crank on this.

**[00:02:46.520]** If you look at how each of our bets operate on a day-to-day basis,

**[00:02:50.840]** you're going to see a lot of parallels

**[00:02:52.960]** with lean startup methodologies.

**[00:02:55.160]** Nothing there is rocket science.

**[00:02:57.400]** We did not invent any of these things.

**[00:02:59.520]** I'd say the biggest difference is the speed

**[00:03:01.460]** at which we run our loops.

**[00:03:03.220]** We spend time with users and also

**[00:03:05.900]** anthropic researchers every single day.

**[00:03:08.520]** My favorite thing to talk to users about is,

**[00:03:11.500]** please complain at me.

**[00:03:13.100]** And my favorite thing to talk to researchers about is,

**[00:03:16.200]** what have you been surprised by lately?

**[00:03:18.180]** Because both things are often opportunities

**[00:03:20.240]** for new bets, new products, new things

**[00:03:22.160]** to explore that could pay off for us. We also aim to ship to users every day or two. We're

**[00:03:29.900]** trying to ship something new every single day in response to what we hear from people.

**[00:03:34.180]** We are trying to keep a very, very high cadence of innovation on the team, and we are trying

**[00:03:38.540]** to get things out based off of what people tell us. Likewise, when people tell us something's

**[00:03:43.920]** not working or they have feedback or they have a suggestion, early on in a project,

**[00:03:48.340]** we try to ship them the response to that the next day. Oftentimes we're able to do the

**[00:03:52.780]** same day, sometimes it's the next day. Not everything hits that bar, but our usual goal

**[00:03:57.220]** is to get things out very quickly to people when they have feedback.

**[00:04:01.660]** Finally, we do not try to predict the future. A lot of labs groups out there do try to predict

**[00:04:07.340]** the future. They say in ten years' time we're going to have this amazing technology and

**[00:04:10.460]** it's going to do these amazing things. We don't do that. Instead, we try to ship, we

**[00:04:16.420]** We watch people use the stuff, we learn what they do, we ship, we watch, we learn, we ship,

**[00:04:21.020]** we watch, we learn.

**[00:04:22.020]** We run that loop over and over.

**[00:04:24.240]** For Cloud Design, we ran that loop somewhere between 50 and 100 times over the course of

**[00:04:29.020]** those 10 weeks.

**[00:04:32.360]** So why did we start working on Cloud Design?

**[00:04:36.100]** We started working on Cloud Design because Cloud Code made engineers really, really fast,

**[00:04:41.940]** and the rest of us had to keep up.

**[00:04:44.180]** So product development timelines, they used to be six months.

**[00:04:48.260]** And then they'd be a month.

**[00:04:49.680]** And then a week.

**[00:04:51.440]** And now a day.

**[00:04:53.720]** So sometimes things that you were spending a week on before are now something that you're

**[00:04:57.200]** getting done in a couple hours and getting out in front of users.

**[00:04:59.800]** That is rapid.

**[00:05:00.800]** Can I see a very quick show of fingers from people?

**[00:05:04.460]** I'm very curious.

**[00:05:05.700]** The last feature you shipped, how many weeks did it take from idea to getting it in front

**[00:05:10.760]** of users?

**[00:05:11.760]** It's okay if you need two hands, and don't be shy here.

**[00:05:14.760]** One, one, ten, one, two, one, four, one.

**[00:05:20.460]** A lot of different answers, but things have gotten a lot faster.

**[00:05:23.520]** Think about what your answer would have been a year ago.

**[00:05:27.520]** All these timelines have compressed a lot.

**[00:05:30.380]** And so once Cloud Code took off, the bottleneck moved.

**[00:05:33.800]** The bottleneck moved from building the feature

**[00:05:36.200]** to figuring out the right things to be

**[00:05:38.280]** building for your users in a lot of cases.

**[00:05:41.460]** So the option was either skip those early steps, just try and decide on the fly, and

**[00:05:48.220]** potentially build the wrong thing really fast, or try to find ways for the rest of us to

**[00:05:52.780]** speed up.

**[00:05:54.740]** So our designers, our PMs were having trouble keeping up.

**[00:05:58.540]** We needed our own accelerator tool.

**[00:06:00.820]** And somebody on our team, Nate, who was a designer on Cloud Code previously, had seen

**[00:06:05.060]** firsthand what happens when some of these teams speed up to such a huge extent.

**[00:06:10.420]** And that got him thinking about the problem and a potential solution.

**[00:06:14.300]** And so he ended up hacking together a prototype over the course of a weekend while he was

**[00:06:19.200]** working on a different bet.

**[00:06:21.600]** And it was very simple.

**[00:06:22.920]** It was the agent SDK.

**[00:06:24.640]** It was a very thin IDE wrapper.

**[00:06:27.820]** And it used an existing skill that he had already been using in cloud code.

**[00:06:33.080]** And this is how a lot of our labs bets start.

**[00:06:36.140]** It's one person, one weekend, one screen reporting.

**[00:06:38.980]** and get something, hacks something together, and just shares what they did. So, for us,

**[00:06:45.840]** Nate posts this in Slack. We run a lot of things in Slack. And everybody helpfully chimed

**[00:06:50.560]** in with both this is what promising about this and also here all the stuff that doesn work totally broken please go fix And that was his roadmap for the first couple weeks on this It was just what the promising stuff to lean into What are the major blockers

**[00:07:05.350]** we want to address? I do think it's worth calling out the things that we did not do.

**[00:07:11.850]** So we did not write a PRD in advance. We had zero vision docs. We had zero KR meetings. We did not

**[00:07:18.970]** have an H1 annual staffing plan. We did not have a two-page year for what we were going to do over

**[00:07:24.670]** the next two years. We did not write the press release in advance for what we were doing.

**[00:07:29.110]** Those things are great if you know exactly what you're building. We did not know exactly

**[00:07:32.850]** what we were building. All we knew is that we had a spark. So who here works off of PRDs

**[00:07:39.530]** or has written one or worked off of one in the last month? Most of the room. Now, of

**[00:07:45.750]** those people that raised your hand, who would rather be working off of a prototype that

**[00:07:49.070]** worked and showed you the feature fully. Exact same hands. Pretty good. So we like to use

**[00:07:56.890]** prototypes because documents are imprecise. It's so easy for two people to look at the

**[00:08:03.310]** same doc and have two different products in mind about what the experience should be.

**[00:08:08.270]** And usually those two ideas are not the same idea that the author had when they were writing

**[00:08:12.870]** the thing in the first place. Right? So docs are imprecise. Prototypes, they're more concrete.

**[00:08:18.010]** They're more visceral.

**[00:08:19.010]** They let you get hands-on with the thing and really feel the experience yourself.

**[00:08:23.790]** Over the course of this project, we were able to get our prototyping cycle down to a couple

**[00:08:28.910]** of minutes.

**[00:08:30.410]** So if somebody had an idea, they were able to prototype and get it out in a couple of

**[00:08:33.630]** minutes.

**[00:08:34.630]** For us, the easiest way of doing this is talk to it with somebody else on your team, record

**[00:08:41.170]** it, transcribe it.

**[00:08:42.410]** There's tons of great tools for that.

**[00:08:44.130]** and mainly talk about what the problem is, what does the solution generally do, why do

**[00:08:48.490]** you care about solving this problem, and then we would take that transcript and give it to

**[00:08:53.130]** Claude Design once we had something working and say give me a few options for this. This

**[00:08:58.030]** has effectively replaced PRDs for me as a product manager that's been writing them for

**[00:09:02.570]** almost two decades now. Now I just do prototypes, this is my flow, it works pretty well. In labs

**[00:09:09.350]** we do this ritual every once in a while, we get together and we call them pitch-offs.

**[00:09:14.290]** And the thing I like doing about these is we all get together, we brainstorm. You're

**[00:09:17.870]** basically trying to nerd snipe other people to come work on your thing with you that you

**[00:09:21.730]** think the team should do. And when we first started doing these, people talk and you just

**[00:09:26.950]** talk and present your thing, and it's not that compelling. The first time we did this

**[00:09:30.470]** with Claude Design is what convinced me that we had a promising product on our hands. Because

**[00:09:36.710]** In these pitch-offs, most of the ideas people come up with during the pitch-off, someone

**[00:09:42.010]** says something and you're inspired by what they say.

**[00:09:45.010]** Somebody has an idea that you fork off of and you come up with something new on your

**[00:09:47.830]** own.

**[00:09:48.830]** By the second half of it, 100% of the pitches were prototypes or slides made with design.

**[00:09:54.470]** They were being made on the fly in the meeting.

**[00:09:57.430]** That's what convinced us this is a proof point we should double down on this bet.

**[00:10:01.430]** We should take this to market.

**[00:10:03.530]** The other thing that's a little bit different about the way that teams work in labs is the

**[00:10:07.710]** size of the teams.

**[00:10:09.790]** So almost every labs bet starts as a single person.

**[00:10:13.930]** It's just one person with their good buddy Claude exploring a really hard problem and

**[00:10:19.250]** exploring a pretty hard idea.

**[00:10:21.990]** And at this point, you are not trying to build the best product in the world.

**[00:10:26.910]** You are just looking for that little moment of magic.

**[00:10:29.530]** You are looking for that little hint of heat.

**[00:10:31.710]** You are looking for, hey, this is a promising idea because there is a little sparkly glimmer

**[00:10:36.370]** here that we can build into something compelling.

**[00:10:39.530]** And most labs bets, I'll admit, do not make it past this point.

**[00:10:43.550]** Most things we end up folding before they get here.

**[00:10:46.470]** And that's totally okay.

**[00:10:47.550]** This early exploration is usually hours or a few days for most things.

**[00:10:53.950]** Once we do have a promising spark, we usually scale the team up massively, you know, 300%,

**[00:10:59.790]** all the way to three people.

**[00:11:01.330]** So these are not big teams.

**[00:11:03.590]** And the reason why we do that is that we want it to be a very tight group exploring together

**[00:11:09.430]** with very little collaboration overhead.

**[00:11:11.830]** If something is so compelling that we're pretty convinced that we're going to be taking it

**[00:11:15.550]** to a product, after it's had three people for a while, we might scale it all the way

**[00:11:19.150]** up to five people ahead of launch.

**[00:11:22.310]** So who here works on a team that is smaller than 20 people?

**[00:11:26.930]** Okay.

**[00:11:28.470]** Almost everybody, but not everybody.

**[00:11:30.030]** What about smaller than ten? Five? Smaller than three? Is there anyone here that's totally

**[00:11:36.650]** solo? Oh, yeah, a couple people. Three-ish? Two and a half? Four. Okay. So for most of

**[00:11:44.030]** Claude's design development, it was only three people with Claude, and luckily Claude's a

**[00:11:48.650]** pretty good team member. So what makes that possible? I'm sure this is also true of a lot

**[00:11:54.710]** of the solo builders in this room, everyone on the team does everything. The engineers

**[00:12:01.750]** talk to users, PMs write code, designers do data analysis. All of these things are enabled

**[00:12:07.950]** in part with Cloud. And the lines between the roles on this team, they have essentially

**[00:12:13.610]** dissolved at this point. You do have your specialization, you do have the unique perspective

**[00:12:18.350]** and diversity that you bring to a team, but at any moment, any one of these people on this

**[00:12:22.970]** team, can talk to ten users, you can realize what the underlying problem is, you can design

**[00:12:29.330]** a solution to it, you can ship it to users, you can listen for feedback, you can keep iterating

**[00:12:33.930]** solo if you need to. Quite often that's the case. That's how most features happen. Most

**[00:12:38.630]** things on the team are totally solo. And having this small team where everyone can do everything,

**[00:12:45.910]** that's the main thing that minimizes coordination overhead for us. Again, most things can be

**[00:12:51.170]** be done solo, but let's say you have to get the whole team together, oftentimes that's

**[00:12:55.130]** as easy as talking to the person on your left and the person on your right and you're done.

**[00:12:59.690]** It's not a big alignment meeting, it's not something you have to schedule, it's not something

**[00:13:02.850]** that you have to wait for. And so this helps us minimize coordination overhead. We've already

**[00:13:08.590]** minimized planning and process just by relying on prototypes, and just doing these two things

**[00:13:14.830]** alone would let us go pretty quickly, right? They would let us go pretty fast, they would

**[00:13:19.810]** take down these big long cycles at the beginning of major milestones. But we go a good bit

**[00:13:26.330]** faster and we go a good bit faster by then really aggressively optimizing every single

**[00:13:31.950]** other step in our development process in our loop. So, our loop is our loop. This may not

**[00:13:40.550]** be the right loop for you. That's not the message here. If you're working on hardware,

**[00:13:44.530]** this is probably the wrong loop. But our loop is pretty basic. We talk to users. We design

**[00:13:49.110]** features, we ship code, we read feedback, and then we do it again. And again, we're just

**[00:13:53.450]** trying to do this over and over and over and over And the point not the specific loop it not the specific interventions that we did here It rather the thought process that goes into these is why are you doing this

**[00:14:06.310]** work that Claude could do for you a lot of times? Or why haven't you built your own tooling?

**[00:14:11.190]** Because every little bit of optimization that you do on your loop is going to pay you back

**[00:14:16.170]** if you're running it 50 to 100 times in a project. So for a really simple example, I

**[00:14:21.830]** I mentioned that we talk to users every day. We want that to be the easiest thing in the

**[00:14:25.590]** world. We are people. We do things that are easy. We tend to do things that are hard less

**[00:14:30.330]** often. We want the easiest thing in the world for us to be to talk to users. We did the

**[00:14:35.390]** really basic stuff from the beginning. We create shared Slack channels with anyone using

**[00:14:39.630]** the product. We do a ton of internal dog fooding. We talk to our dog fooders all the time with

**[00:14:44.190]** new features. But then we sped this up by bringing Claude into all of those conversations.

**[00:14:50.590]** So Claude looks at all of our customer conversations.

**[00:14:53.350]** It looks for commonalities across conversations.

**[00:14:55.910]** You and I may be talking to different users today who may have the same suggestion.

**[00:14:59.810]** We want Claude to tell us that if we don't talk.

**[00:15:02.610]** We do it for early analysis.

**[00:15:03.990]** We do it for early investigation.

**[00:15:06.030]** We have Claude do the first look at all of this stuff for us.

**[00:15:09.830]** We're the ones having the conversation.

**[00:15:11.550]** We don't put Claude between us and the users in that case.

**[00:15:15.730]** But we do have it do all of the analysis that we were already doing on every other conversation

**[00:15:19.850]** as an immediate follow-up. So talking to users, most important thing, obviously we want to

**[00:15:24.610]** optimize it. Our next thing on here was designing features. And luckily we have a great product

**[00:15:30.730]** for that now. When we got started, we did not have the tool that we wanted for designing

**[00:15:37.650]** features. Our team, we would use quad code, we would build prototypes with it, and then

**[00:15:41.610]** when it came time to share that prototype, I would either record a video or we would

**[00:15:47.030]** put up a branch and say pull down this branch and try it, or you would just commit it into

**[00:15:52.850]** a sandbox and let other people pull it down and try it. So we wanted to use Cloud Design

**[00:15:59.850]** to design Cloud Design, and so very quickly Cloud Design got great at designing Cloud Design,

**[00:16:03.950]** which is fantastic. I have to say, if you could do any developer tool, if you're using

**[00:16:09.390]** your own developer tool to improve your developer tool, it's the best situation in the world.

**[00:16:14.090]** makes things so much easier. There's a lot of other features that you see in Claude design

**[00:16:18.870]** today from the way it explores code bases, the way it links with GitHub, even multiplayer

**[00:16:24.590]** was something that we built based off of how we were working in Claude design to design

**[00:16:28.970]** Claude design. For multiplayer, we were getting to these scenarios where I might prototype

**[00:16:33.810]** something and then share it with somebody else on the team. They would take a look at

**[00:16:38.150]** it and then they would tell me what they thought we should change about it and I would hands

**[00:16:42.810]** on keyboard, type it in, and then we would look at what it was. We wanted to take that

**[00:16:46.610]** step out, and so we made it possible for multiple people to be iterating on the same design at

**[00:16:51.270]** the same time. We had originally built that for ourselves to go faster, and then as soon

**[00:16:55.610]** as we brought the product over to users, the very first request was, can I use this with

**[00:17:01.070]** the rest of the people on my team in real time? So we made a first-class part of the

**[00:17:06.190]** product. The next thing that we've done in here is we wanted to optimize how we ship code.

**[00:17:12.130]** So if you've used Cloud Design, you've probably used the handoff to Cloud Code.

**[00:17:16.850]** It's fantastic.

**[00:17:17.850]** It's such a good way of getting your designs into production.

**[00:17:20.890]** And that's another feature that we built really to speed up our own workflow.

**[00:17:24.950]** When we started out, we would design our features and then we would export all the files, then

**[00:17:30.430]** we would import them into Cloud Code, and then we would retype all of the context that

**[00:17:35.170]** we had done over multiple turns of conversation with Cloud Design so that Cloud Code would

**[00:17:39.090]** have all that context.

**[00:17:40.770]** And that was slow.

**[00:17:42.270]** We didn't like it being slow, right?

**[00:17:44.210]** So we wanted to improve it.

**[00:17:45.990]** And so we originally built this for ourselves and then as soon as we started handing off

**[00:17:49.550]** the product to other people, the first request was great, now how do I get this into production?

**[00:17:55.430]** So first was multiplayer and then right after was okay, now that I have the thing, I want

**[00:17:59.010]** to actually ship it.

**[00:18:00.270]** And so this was another spot where we just had too much friction, we're working for ourselves,

**[00:18:03.930]** we're optimizing for ourselves to get it out there.

**[00:18:08.150]** The last step in our iteration cycle is to read feedback.

**[00:18:12.370]** At this point, we get too much feedback for one person to read through all of it.

**[00:18:16.390]** I think that would be a full-time job.

**[00:18:19.550]** But we still want to make sure we don't miss anything.

**[00:18:21.530]** And even if we had that one person whose full-time job was to read that feedback, we would probably

**[00:18:26.010]** miss things.

**[00:18:27.010]** And we would miss things because the number of small issues that pop up, you don't want

**[00:18:31.430]** to miss them.

**[00:18:32.430]** It's too much for any one person to keep in their head.

**[00:18:34.850]** So to deal with that scale, we ended up building our own feedback clustering tool.

**[00:18:38.910]** It took an afternoon.

**[00:18:40.550]** It wasn't something that we were going to wait on.

**[00:18:42.770]** We needed to have this.

**[00:18:44.210]** And so right away, we ended up building this.

**[00:18:46.390]** We rolled this out.

**[00:18:47.590]** And now we have Claude taking a look at all feedback that comes in.

**[00:18:52.250]** It tries to match it up with system monitors, with system traces.

**[00:18:56.470]** It tries to look for common trends across things.

**[00:18:58.410]** It does initial analysis if things look like a bug.

**[00:19:00.950]** We have tried to make all of those initial steps that we would do looking at that feedback

**[00:19:04.430]** automatic to speed ourselves up.

**[00:19:07.710]** So we also found ourselves we would take everything it said and then we would have to come up

**[00:19:12.850]** with a suggestion after reading through all of that.

**[00:19:15.610]** So now we have Claude give us a suggestion on how to fix it and then we found ourselves

**[00:19:19.270]** copying and pasting.

**[00:19:20.610]** And so we just made that a button to bring it directly over to our development tooling.

**[00:19:26.030]** So not everything we built worked.

**[00:19:29.770]** Just because you're really fast doesn't mean you're always really right.

**[00:19:33.070]** And we got tons of things wrong as we were building the product.

**[00:19:36.510]** So I want to tell you about one specific time where we got this wrong.

**[00:19:40.310]** And that was we started out early on and we built these really advanced controls.

**[00:19:47.610]** These gave you really fine control over every single pixel.

**[00:19:51.530]** You could do anything with these.

**[00:19:53.310]** These were for power users.

**[00:19:55.310]** And in our early testers, we had a few power users who were very vocal, gave great feedback

**[00:19:59.750]** feedback, and they love this feature. They love this set of tools. And we thought, great,

**[00:20:05.430]** we have something good on our hands, all the feedback we're hearing looks great, but then

**[00:20:08.870]** as we dug into the usage, we found that everybody else hated them. Like, didn't just dislike

**[00:20:15.210]** them, people hated them. They were confusing, they were actively harmful to the product.

**[00:20:20.990]** And so we ripped them out. For us, this took a grand total of one week. So, yes, we got

**[00:20:27.790]** off track, but from idea to course correcting and ripping out the feature and going on to

**[00:20:32.730]** the next thing, took us about a week of time.

**[00:20:36.250]** If we had been doing a quarterly development cycle and we had planned this to do this over

**[00:20:41.410]** a quarter, we would have been off track for an entire quarter.

**[00:20:44.970]** That would have been really bad for the product given that the entire product shipped in less

**[00:20:48.950]** than a quarter.

**[00:20:50.450]** For us, it's not necessarily can you always go fast, it's can you always iterate in a

**[00:20:54.150]** in a small enough cycle that you able to very quickly find out when you wrong This comes back to the run experiments bullet from earlier So this taught us a couple things

**[00:21:05.380]** One, this taught us that we should be a tool

**[00:21:08.000]** that lifts the level of craft for everybody,

**[00:21:11.140]** not just the ceiling on power users.

**[00:21:13.240]** It also taught us that we want to be as open as possible

**[00:21:15.600]** because there will be users that we never meet the full needs of.

**[00:21:19.400]** There's going to be some power user out there

**[00:21:21.960]** who wants to do something very specific

**[00:21:23.400]** that we're not going to support.

**[00:21:25.080]** That's what convinced us that we want this to be a very open tool.

**[00:21:28.160]** That's why if you export from it, you get HTML, CSS, JavaScript.

**[00:21:32.980]** That's why we're trying to do more and more integrations that you can take things directly

**[00:21:37.480]** into other tools.

**[00:21:38.480]** We haven't talked about this publicly before, but I think this week or next week we're going

**[00:21:42.300]** to be pushing out the ability for any design tool to integrate with quad code.

**[00:21:46.840]** Sorry, quad design.

**[00:21:48.920]** Just via their existing MCPs.

**[00:21:51.320]** So we want this to be a tool where you are able to explore, it lists the level of capability

**[00:21:55.560]** for everyone, and then the people that do have very specialized needs, if they have a

**[00:21:59.380]** tool of choice, they can just take their designs right into them.

**[00:22:02.040]** They're yours.

**[00:22:04.940]** So this slide's fun.

**[00:22:06.720]** On the left is that first prototype.

**[00:22:10.520]** It's a terminal in a browser, and that's about it.

**[00:22:13.500]** It's not the shiniest thing in the world.

**[00:22:15.720]** This is the level of those early explorations where all you're looking for is that little

**[00:22:20.220]** bit of promise. This is not obviously the final product that launched. On the right,

**[00:22:26.100]** it's the final product that launched. There's a lot that separates them. I'll admit this

**[00:22:30.980]** one on the left, it does have a little bit of promise in it. But 99% of the value came

**[00:22:38.460]** from those ten weeks of iterating and shipping and talking to users every single day. The

**[00:22:44.160]** value came from the experimentation, figuring out what the right thing was to build rather

**[00:22:49.020]** than knowing in advance this is exactly what we are going to be doing.

**[00:22:54.360]** So to put the amount of iteration this team does in perspective, Cloud Design is shipped

**[00:22:59.280]** on a Friday, and by the following Monday, we had shipped 62 improvements to the product.

**[00:23:05.640]** That's a good number given the size of the team we talked about earlier.

**[00:23:10.260]** And we made the product more token efficient.

**[00:23:13.420]** We improved its ability to handle images, we made it better at exploring code bases,

**[00:23:19.200]** we made most exports instant.

**[00:23:21.100]** It's a pretty long list and was all based off of user feedback that we got on launch

**[00:23:25.240]** day.

**[00:23:26.240]** Now, this was not a Herculean effort.

**[00:23:29.300]** This was not something that required all-nighters from everybody.

**[00:23:33.460]** This was something that was very natural because the team had built up the processes and the

**[00:23:37.060]** muscles and the practice of doing this every single day for ten weeks prior.

**[00:23:41.900]** This became a quick, very normal way of working for us.

**[00:23:45.600]** I mentioned earlier that quad design has been live for one month.

**[00:23:50.480]** And so, also, you may have seen this, but last night we doubled token limits for the

**[00:23:56.140]** product.

**[00:23:57.140]** So, one of the pieces of feedback that we heard was that people liked it, they wanted

**[00:23:59.800]** to use it more, so we're making that easier.

**[00:24:01.520]** So, that's across all subscription plans.

**[00:24:06.020]** Before we close, I want to share one of the more counterintuitive things we've learned

**[00:24:08.940]** working in labs, and that is that you do not want to work on the thing that already works.

**[00:24:14.700]** You often want to prototype the thing that almost works.

**[00:24:18.500]** And the reason why you do that is because the models are improving so rapidly.

**[00:24:24.240]** The level of intelligence keeps going up.

**[00:24:28.300]** And the next model may just fix the issues that you cannot solve via engineering.

**[00:24:33.500]** We had this with Cloud Design.

**[00:24:34.740]** were a bunch of issues in that early prototype that we did not solve. We did not fix them

**[00:24:40.080]** with clever engineering, we did not fix them with amazing insights, we fixed them with

**[00:24:46.060]** Opus 4.7 coming out. And that's going to be true of a lot of things that everyone in

**[00:24:51.800]** this room that we all work on together. The model releases are a tide that lifts all boats.

**[00:24:57.740]** They do a lot for you. So, remember, early on, you're just looking for that hint of magic.

**[00:25:03.240]** You're not looking for something that works in full, that works completely, that handles

**[00:25:07.220]** every edge case.

**[00:25:08.220]** You're looking for something that could become that in the future.

**[00:25:11.820]** And so that's why when you find it, you want to start exploring, start building, start

**[00:25:16.560]** bringing in front of users and figuring out the shape of the product that works.

**[00:25:20.000]** Because the shape is the most important thing and the thing that we all get wrong when we

**[00:25:23.180]** first start.

**[00:25:24.180]** We all have to iterate on it.

**[00:25:26.040]** So there's three concrete things that you can try tomorrow from this talk if you want.

**[00:25:33.000]** if there's nothing else you took away from it. The first is go ahead, next time you're

**[00:25:36.500]** going to write a PRD, skip it. Don't write it. Instead, just talk with Claude, talk with

**[00:25:42.100]** somebody on your team and take the transcript and don't talk about specifically what the

**[00:25:45.820]** feature is, what buttons there are. Instead, just spend time talking about why you're trying

**[00:25:51.000]** to solve this problem. What are the characteristics of a good solution? And give that to Claude

**[00:25:56.800]** Design. Give that to Claude. Ask it to give you three variations on a prototype that might

**[00:26:01.960]** solve that. See if that works for you. The second, pick something that you've been waiting

**[00:26:07.720]** for. It could be feedback clustering like we did. It could be a new analysis tool. And

**[00:26:12.840]** just build it one afternoon. Everyone waits on tools when at this point internal tooling,

**[00:26:19.280]** building your own stuff, is rapid. It's very fast. So go ahead and scratch your own itch.

**[00:26:24.140]** You will be happy that you did. It will pay itself off very quickly. The third, and this

**[00:26:29.020]** This one looks simple but I think this is the hardest.

**[00:26:31.980]** Take one real feature request.

**[00:26:34.160]** I don't mean like a small bug fix or a padding change.

**[00:26:37.160]** Take one real feature request from a user and turn it around in 24 hours, get the idea in

**[00:26:43.700]** front of them and follow up with them for feedback.

**[00:26:46.220]** The reason why I bring that up is not this urge to go faster.

**[00:26:48.940]** It's because the first time you do this, if you're not doing this already, you're going

**[00:26:52.920]** to find that there are a bunch of roadblocks in your existing process and the existing

**[00:26:57.500]** way that you build software.

**[00:26:58.960]** if you have been on a longer timeline. That could be everything from the way that you

**[00:27:02.680]** do deploys, the way that you ask somebody on your team to review your code, that could

**[00:27:08.060]** be a whole host of things. So going through this once really helps. And I wouldn't try

**[00:27:13.540]** to do all three of these at once. I would layer these on. Each one is going to teach

**[00:27:18.620]** you something a little bit different that helps you move a little bit faster. This is

**[00:27:22.880]** the last show of hands, I promise. Who is going to try number one? A lot. Two? Three?

**[00:27:32.960]** Okay. Thank you so much. That's the talk. Thank you for your time. I would love to talk

**[00:27:39.660]** to folks who have used the product or even those that haven't. I'm going to be by the

**[00:27:42.820]** demo booth for most of the day for Collade Design. It's down at the end of the hallway.

**[00:27:46.920]** So please come find me, tap me on my shoulder, come complain to me or tell me what surprised

**[00:27:51.200]** you. I'd love that. So thank you so much.

---

## 关键节点索引

| 时戳 | 内容摘要 |
|------|----------|
| `00:00:00.000` | Dan Carey Reviewer |
| `00:00:07.000` | How is everybody? A little bit more than that. Come on, guys. How is everybody? |
| `00:00:18.000` | Thank you. Thank you. |
| `00:00:20.000` | So, I'm Dan Carey. I am a product manager. I lead a product within Anthropic Lab... |
| `00:00:25.000` | Today, we're going to talk a little bit about cloud design. |
| `00:00:28.000` | Can I get a quick show of hands? |
| `00:00:29.760` | Who here has already tried Claude Design? |
| `00:00:33.300` | OK, great. |
| `00:00:34.800` | For those of you who haven't had a chance yet, Claude Design, |
| `00:00:37.720` | it's a new product from Anthropik Labs, |
| `00:00:40.160` | and it lets you collaborate with Claude |
| `00:00:41.900` | to create polished visual artifacts. |
| `00:00:43.960` | These can be designs, prototypes, slide, one-pagers, more. |
| `00:00:49.440` | You can do a lot of different things with this product. |
| `00:00:52.060` | And as of, I think it's yesterday, |
| `00:00:54.880` | the product's been live in research preview for one month. |
| `00:00:57.900` | So we're pretty happy about that. |
| `00:00:59.740` | Today, I'm going to tell you a little bit |
| `00:01:01.560` | about how a very small team, it was three people |
| `00:01:05.340` | for most of the development, built Claude Design |
| `00:01:08.000` | in about 10 weeks from idea to launching the product. |
| `00:01:11.140` | And the reason I'm going to share these things with you |
| `00:01:13.140` | is because the most common question I get asked |
| `00:01:15.320` | is, why did you decide to start working on this? |
| `00:01:17.520` | How did you see that this was an opportunity |
| `00:01:19.660` | for building a new AI-enabled product? |
| `00:01:22.360` | How'd you build it? |
| `00:01:23.280` | How'd you launch it? |
| `00:01:25.200` | So everything I'm going to cover here, |
| `00:01:26.760` | There is no real secret sauce. |
| `00:01:28.720` | These are all things that work well for us. |
| `00:01:30.960` | Take what you like. |
| `00:01:31.760` | You can do a lot of these things tomorrow. |
| `00:01:35.400` | To start, I want to tell you about what Anthropic Labs is. |
| `00:01:38.560` | It's kind of funny. |
| `00:01:39.180` | It's a lab inside a frontier lab. |
| `00:01:42.540` | We don't have any labs within Anthropic Labs, |
| `00:01:44.280` | but it is labs quite a ways down. |
| `00:01:47.080` | The way that we usually talk about it is as a bet factory. |
| `00:01:51.480` | And by that, I mean we have very small teams |
| `00:01:53.900` | exploring the frontier of what the models can do |
| `00:01:56.780` | and making bets about whether or not something will work. |
| `00:02:00.320` | We run experiments to find out what works. |
| `00:02:03.620` | We double down on the things that are working. |
| `00:02:05.920` | We fold the things that are not working. |
| `00:02:08.860` | And at any given time, we might have a dozen small teams |
| `00:02:12.480` | exploring different concepts. |
| `00:02:15.320` | So it's lots of exploration, a small number |
| `00:02:18.440` | of really high-conviction releases of things |
| `00:02:20.520` | that we think can be moonshots or change how people work |
| `00:02:23.720` | with the models. |
| `00:02:26.140` | There's a few products that came from here that you may know. |
| `00:02:28.940` | Cloud Code came out of labs. |
| `00:02:30.340` | Design came out of labs. |
| `00:02:31.480` | MCP came out of labs. |
| `00:02:32.620` | Skills came out of labs. |
| `00:02:34.480` | We had the Cloud and Chrome extension. |
| `00:02:36.480` | We had our work on hands-free audio come out of labs. |
| `00:02:39.520` | So this is a process that's worked pretty well for us. |
| `00:02:42.660` | And we just keep turning the crank on this. |
| `00:02:46.520` | If you look at how each of our bets operate on a day-to-day basis, |
| `00:02:50.840` | you're going to see a lot of parallels |
| `00:02:52.960` | with lean startup methodologies. |
| `00:02:55.160` | Nothing there is rocket science. |
| `00:02:57.400` | We did not invent any of these things. |
| `00:02:59.520` | I'd say the biggest difference is the speed |
| `00:03:01.460` | at which we run our loops. |
| `00:03:03.220` | We spend time with users and also |
| `00:03:05.900` | anthropic researchers every single day. |
| `00:03:08.520` | My favorite thing to talk to users about is, |
| `00:03:11.500` | please complain at me. |
| `00:03:13.100` | And my favorite thing to talk to researchers about is, |
| `00:03:16.200` | what have you been surprised by lately? |
| `00:03:18.180` | Because both things are often opportunities |
| `00:03:20.240` | for new bets, new products, new things |
| `00:03:22.160` | to explore that could pay off for us. We also aim to ship to users every day or ... |
| `00:03:29.900` | trying to ship something new every single day in response to what we hear from p... |
| `00:03:34.180` | We are trying to keep a very, very high cadence of innovation on the team, and w... |
| `00:03:38.540` | to get things out based off of what people tell us. Likewise, when people tell u... |
| `00:03:43.920` | not working or they have feedback or they have a suggestion, early on in a proje... |
| `00:03:48.340` | we try to ship them the response to that the next day. Oftentimes we're able to ... |
| `00:03:52.780` | same day, sometimes it's the next day. Not everything hits that bar, but our usu... |
| `00:03:57.220` | is to get things out very quickly to people when they have feedback. |
| `00:04:01.660` | Finally, we do not try to predict the future. A lot of labs groups out there do ... |
| `00:04:07.340` | the future. They say in ten years' time we're going to have this amazing technol... |
| `00:04:10.460` | it's going to do these amazing things. We don't do that. Instead, we try to ship... |
| `00:04:16.420` | We watch people use the stuff, we learn what they do, we ship, we watch, we lear... |
| `00:04:21.020` | we watch, we learn. |
| `00:04:22.020` | We run that loop over and over. |
| `00:04:24.240` | For Cloud Design, we ran that loop somewhere between 50 and 100 times over the c... |
| `00:04:29.020` | those 10 weeks. |
| `00:04:32.360` | So why did we start working on Cloud Design? |
| `00:04:36.100` | We started working on Cloud Design because Cloud Code made engineers really, rea... |
| `00:04:41.940` | and the rest of us had to keep up. |
| `00:04:44.180` | So product development timelines, they used to be six months. |
| `00:04:48.260` | And then they'd be a month. |
| `00:04:49.680` | And then a week. |
| `00:04:51.440` | And now a day. |
| `00:04:53.720` | So sometimes things that you were spending a week on before are now something th... |
| `00:04:57.200` | getting done in a couple hours and getting out in front of users. |
| `00:04:59.800` | That is rapid. |
| `00:05:00.800` | Can I see a very quick show of fingers from people? |
| `00:05:04.460` | I'm very curious. |
| `00:05:05.700` | The last feature you shipped, how many weeks did it take from idea to getting it... |
| `00:05:10.760` | of users? |
| `00:05:11.760` | It's okay if you need two hands, and don't be shy here. |
| `00:05:14.760` | One, one, ten, one, two, one, four, one. |
| `00:05:20.460` | A lot of different answers, but things have gotten a lot faster. |
| `00:05:23.520` | Think about what your answer would have been a year ago. |
| `00:05:27.520` | All these timelines have compressed a lot. |
| `00:05:30.380` | And so once Cloud Code took off, the bottleneck moved. |
| `00:05:33.800` | The bottleneck moved from building the feature |
| `00:05:36.200` | to figuring out the right things to be |
| `00:05:38.280` | building for your users in a lot of cases. |
| `00:05:41.460` | So the option was either skip those early steps, just try and decide on the fly,... |
| `00:05:48.220` | potentially build the wrong thing really fast, or try to find ways for the rest ... |
| `00:05:52.780` | speed up. |
| `00:05:54.740` | So our designers, our PMs were having trouble keeping up. |
| `00:05:58.540` | We needed our own accelerator tool. |
| `00:06:00.820` | And somebody on our team, Nate, who was a designer on Cloud Code previously, had... |
| `00:06:05.060` | firsthand what happens when some of these teams speed up to such a huge extent. |
| `00:06:10.420` | And that got him thinking about the problem and a potential solution. |
| `00:06:14.300` | And so he ended up hacking together a prototype over the course of a weekend whi... |
| `00:06:19.200` | working on a different bet. |
| `00:06:21.600` | And it was very simple. |
| `00:06:22.920` | It was the agent SDK. |
| `00:06:24.640` | It was a very thin IDE wrapper. |
| `00:06:27.820` | And it used an existing skill that he had already been using in cloud code. |
| `00:06:33.080` | And this is how a lot of our labs bets start. |
| `00:06:36.140` | It's one person, one weekend, one screen reporting. |
| `00:06:38.980` | and get something, hacks something together, and just shares what they did. So, ... |
| `00:06:45.840` | Nate posts this in Slack. We run a lot of things in Slack. And everybody helpful... |
| `00:06:50.560` | in with both this is what promising about this and also here all the stuff that ... |
| `00:07:05.350` | we want to address? I do think it's worth calling out the things that we did not... |
| `00:07:11.850` | So we did not write a PRD in advance. We had zero vision docs. We had zero KR me... |
| `00:07:18.970` | have an H1 annual staffing plan. We did not have a two-page year for what we wer... |
| `00:07:24.670` | the next two years. We did not write the press release in advance for what we we... |
| `00:07:29.110` | Those things are great if you know exactly what you're building. We did not know... |
| `00:07:32.850` | what we were building. All we knew is that we had a spark. So who here works off... |
| `00:07:39.530` | or has written one or worked off of one in the last month? Most of the room. Now... |
| `00:07:45.750` | those people that raised your hand, who would rather be working off of a prototy... |
| `00:07:49.070` | worked and showed you the feature fully. Exact same hands. Pretty good. So we li... |
| `00:07:56.890` | prototypes because documents are imprecise. It's so easy for two people to look ... |
| `00:08:03.310` | same doc and have two different products in mind about what the experience shoul... |
| `00:08:08.270` | And usually those two ideas are not the same idea that the author had when they ... |
| `00:08:12.870` | the thing in the first place. Right? So docs are imprecise. Prototypes, they're ... |
| `00:08:18.010` | They're more visceral. |
| `00:08:19.010` | They let you get hands-on with the thing and really feel the experience yourself... |
| `00:08:23.790` | Over the course of this project, we were able to get our prototyping cycle down ... |
| `00:08:28.910` | of minutes. |
| `00:08:30.410` | So if somebody had an idea, they were able to prototype and get it out in a coup... |
| `00:08:33.630` | minutes. |
| `00:08:34.630` | For us, the easiest way of doing this is talk to it with somebody else on your t... |
| `00:08:41.170` | it, transcribe it. |
| `00:08:42.410` | There's tons of great tools for that. |
| `00:08:44.130` | and mainly talk about what the problem is, what does the solution generally do, ... |
| `00:08:48.490` | you care about solving this problem, and then we would take that transcript and ... |
| `00:08:53.130` | Claude Design once we had something working and say give me a few options for th... |
| `00:08:58.030` | has effectively replaced PRDs for me as a product manager that's been writing th... |
| `00:09:02.570` | almost two decades now. Now I just do prototypes, this is my flow, it works pret... |
| `00:09:09.350` | we do this ritual every once in a while, we get together and we call them pitch-... |
| `00:09:14.290` | And the thing I like doing about these is we all get together, we brainstorm. Yo... |
| `00:09:17.870` | basically trying to nerd snipe other people to come work on your thing with you ... |
| `00:09:21.730` | think the team should do. And when we first started doing these, people talk and... |
| `00:09:26.950` | talk and present your thing, and it's not that compelling. The first time we did... |
| `00:09:30.470` | with Claude Design is what convinced me that we had a promising product on our h... |
| `00:09:36.710` | In these pitch-offs, most of the ideas people come up with during the pitch-off,... |
| `00:09:42.010` | says something and you're inspired by what they say. |
| `00:09:45.010` | Somebody has an idea that you fork off of and you come up with something new on ... |
| `00:09:47.830` | own. |
| `00:09:48.830` | By the second half of it, 100% of the pitches were prototypes or slides made wit... |
| `00:09:54.470` | They were being made on the fly in the meeting. |
| `00:09:57.430` | That's what convinced us this is a proof point we should double down on this bet... |
| `00:10:01.430` | We should take this to market. |
| `00:10:03.530` | The other thing that's a little bit different about the way that teams work in l... |
| `00:10:07.710` | size of the teams. |
| `00:10:09.790` | So almost every labs bet starts as a single person. |
| `00:10:13.930` | It's just one person with their good buddy Claude exploring a really hard proble... |
| `00:10:19.250` | exploring a pretty hard idea. |
| `00:10:21.990` | And at this point, you are not trying to build the best product in the world. |
| `00:10:26.910` | You are just looking for that little moment of magic. |
| `00:10:29.530` | You are looking for that little hint of heat. |
| `00:10:31.710` | You are looking for, hey, this is a promising idea because there is a little spa... |
| `00:10:36.370` | here that we can build into something compelling. |
| `00:10:39.530` | And most labs bets, I'll admit, do not make it past this point. |
| `00:10:43.550` | Most things we end up folding before they get here. |
| `00:10:46.470` | And that's totally okay. |
| `00:10:47.550` | This early exploration is usually hours or a few days for most things. |
| `00:10:53.950` | Once we do have a promising spark, we usually scale the team up massively, you k... |
| `00:10:59.790` | all the way to three people. |
| `00:11:01.330` | So these are not big teams. |
| `00:11:03.590` | And the reason why we do that is that we want it to be a very tight group explor... |
| `00:11:09.430` | with very little collaboration overhead. |
| `00:11:11.830` | If something is so compelling that we're pretty convinced that we're going to be... |
| `00:11:15.550` | to a product, after it's had three people for a while, we might scale it all the... |
| `00:11:19.150` | up to five people ahead of launch. |
| `00:11:22.310` | So who here works on a team that is smaller than 20 people? |
| `00:11:26.930` | Okay. |
| `00:11:28.470` | Almost everybody, but not everybody. |
| `00:11:30.030` | What about smaller than ten? Five? Smaller than three? Is there anyone here that... |
| `00:11:36.650` | solo? Oh, yeah, a couple people. Three-ish? Two and a half? Four. Okay. So for m... |
| `00:11:44.030` | Claude's design development, it was only three people with Claude, and luckily C... |
| `00:11:48.650` | pretty good team member. So what makes that possible? I'm sure this is also true... |
| `00:11:54.710` | of the solo builders in this room, everyone on the team does everything. The eng... |
| `00:12:01.750` | talk to users, PMs write code, designers do data analysis. All of these things a... |
| `00:12:07.950` | in part with Cloud. And the lines between the roles on this team, they have esse... |
| `00:12:13.610` | dissolved at this point. You do have your specialization, you do have the unique... |
| `00:12:18.350` | and diversity that you bring to a team, but at any moment, any one of these peop... |
| `00:12:22.970` | team, can talk to ten users, you can realize what the underlying problem is, you... |
| `00:12:29.330` | a solution to it, you can ship it to users, you can listen for feedback, you can... |
| `00:12:33.930` | solo if you need to. Quite often that's the case. That's how most features happe... |
| `00:12:38.630` | things on the team are totally solo. And having this small team where everyone c... |
| `00:12:45.910` | that's the main thing that minimizes coordination overhead for us. Again, most t... |
| `00:12:51.170` | be done solo, but let's say you have to get the whole team together, oftentimes ... |
| `00:12:55.130` | as easy as talking to the person on your left and the person on your right and y... |
| `00:12:59.690` | It's not a big alignment meeting, it's not something you have to schedule, it's ... |
| `00:13:02.850` | that you have to wait for. And so this helps us minimize coordination overhead. ... |
| `00:13:08.590` | minimized planning and process just by relying on prototypes, and just doing the... |
| `00:13:14.830` | alone would let us go pretty quickly, right? They would let us go pretty fast, t... |
| `00:13:19.810` | take down these big long cycles at the beginning of major milestones. But we go ... |
| `00:13:26.330` | faster and we go a good bit faster by then really aggressively optimizing every ... |
| `00:13:31.950` | other step in our development process in our loop. So, our loop is our loop. Thi... |
| `00:13:40.550` | be the right loop for you. That's not the message here. If you're working on har... |
| `00:13:44.530` | this is probably the wrong loop. But our loop is pretty basic. We talk to users.... |
| `00:13:49.110` | features, we ship code, we read feedback, and then we do it again. And again, we... |
| `00:13:53.450` | trying to do this over and over and over and over And the point not the specific... |
| `00:14:06.310` | work that Claude could do for you a lot of times? Or why haven't you built your ... |
| `00:14:11.190` | Because every little bit of optimization that you do on your loop is going to pa... |
| `00:14:16.170` | if you're running it 50 to 100 times in a project. So for a really simple exampl... |
| `00:14:21.830` | I mentioned that we talk to users every day. We want that to be the easiest thin... |
| `00:14:25.590` | world. We are people. We do things that are easy. We tend to do things that are ... |
| `00:14:30.330` | often. We want the easiest thing in the world for us to be to talk to users. We ... |
| `00:14:35.390` | really basic stuff from the beginning. We create shared Slack channels with anyo... |
| `00:14:39.630` | the product. We do a ton of internal dog fooding. We talk to our dog fooders all... |
| `00:14:44.190` | new features. But then we sped this up by bringing Claude into all of those conv... |
| `00:14:50.590` | So Claude looks at all of our customer conversations. |
| `00:14:53.350` | It looks for commonalities across conversations. |
| `00:14:55.910` | You and I may be talking to different users today who may have the same suggesti... |
| `00:14:59.810` | We want Claude to tell us that if we don't talk. |
| `00:15:02.610` | We do it for early analysis. |
| `00:15:03.990` | We do it for early investigation. |
| `00:15:06.030` | We have Claude do the first look at all of this stuff for us. |
| `00:15:09.830` | We're the ones having the conversation. |
| `00:15:11.550` | We don't put Claude between us and the users in that case. |
| `00:15:15.730` | But we do have it do all of the analysis that we were already doing on every oth... |
| `00:15:19.850` | as an immediate follow-up. So talking to users, most important thing, obviously ... |
| `00:15:24.610` | optimize it. Our next thing on here was designing features. And luckily we have ... |
| `00:15:30.730` | for that now. When we got started, we did not have the tool that we wanted for d... |
| `00:15:37.650` | features. Our team, we would use quad code, we would build prototypes with it, a... |
| `00:15:41.610` | when it came time to share that prototype, I would either record a video or we w... |
| `00:15:47.030` | put up a branch and say pull down this branch and try it, or you would just comm... |
| `00:15:52.850` | a sandbox and let other people pull it down and try it. So we wanted to use Clou... |
| `00:15:59.850` | to design Cloud Design, and so very quickly Cloud Design got great at designing ... |
| `00:16:03.950` | which is fantastic. I have to say, if you could do any developer tool, if you're... |
| `00:16:09.390` | your own developer tool to improve your developer tool, it's the best situation ... |
| `00:16:14.090` | makes things so much easier. There's a lot of other features that you see in Cla... |
| `00:16:18.870` | today from the way it explores code bases, the way it links with GitHub, even mu... |
| `00:16:24.590` | was something that we built based off of how we were working in Claude design to... |
| `00:16:28.970` | Claude design. For multiplayer, we were getting to these scenarios where I might... |
| `00:16:33.810` | something and then share it with somebody else on the team. They would take a lo... |
| `00:16:38.150` | it and then they would tell me what they thought we should change about it and I... |
| `00:16:42.810` | on keyboard, type it in, and then we would look at what it was. We wanted to tak... |
| `00:16:46.610` | step out, and so we made it possible for multiple people to be iterating on the ... |
| `00:16:51.270` | the same time. We had originally built that for ourselves to go faster, and then... |
| `00:16:55.610` | as we brought the product over to users, the very first request was, can I use t... |
| `00:17:01.070` | the rest of the people on my team in real time? So we made a first-class part of... |
| `00:17:06.190` | product. The next thing that we've done in here is we wanted to optimize how we ... |
| `00:17:12.130` | So if you've used Cloud Design, you've probably used the handoff to Cloud Code. |
| `00:17:16.850` | It's fantastic. |
| `00:17:17.850` | It's such a good way of getting your designs into production. |
| `00:17:20.890` | And that's another feature that we built really to speed up our own workflow. |
| `00:17:24.950` | When we started out, we would design our features and then we would export all t... |
| `00:17:30.430` | we would import them into Cloud Code, and then we would retype all of the contex... |
| `00:17:35.170` | we had done over multiple turns of conversation with Cloud Design so that Cloud ... |
| `00:17:39.090` | have all that context. |
| `00:17:40.770` | And that was slow. |
| `00:17:42.270` | We didn't like it being slow, right? |
| `00:17:44.210` | So we wanted to improve it. |
| `00:17:45.990` | And so we originally built this for ourselves and then as soon as we started han... |
| `00:17:49.550` | the product to other people, the first request was great, now how do I get this ... |
| `00:17:55.430` | So first was multiplayer and then right after was okay, now that I have the thin... |
| `00:17:59.010` | to actually ship it. |
| `00:18:00.270` | And so this was another spot where we just had too much friction, we're working ... |
| `00:18:03.930` | we're optimizing for ourselves to get it out there. |
| `00:18:08.150` | The last step in our iteration cycle is to read feedback. |
| `00:18:12.370` | At this point, we get too much feedback for one person to read through all of it... |
| `00:18:16.390` | I think that would be a full-time job. |
| `00:18:19.550` | But we still want to make sure we don't miss anything. |
| `00:18:21.530` | And even if we had that one person whose full-time job was to read that feedback... |
| `00:18:26.010` | miss things. |
| `00:18:27.010` | And we would miss things because the number of small issues that pop up, you don... |
| `00:18:31.430` | to miss them. |
| `00:18:32.430` | It's too much for any one person to keep in their head. |
| `00:18:34.850` | So to deal with that scale, we ended up building our own feedback clustering too... |
| `00:18:38.910` | It took an afternoon. |
| `00:18:40.550` | It wasn't something that we were going to wait on. |
| `00:18:42.770` | We needed to have this. |
| `00:18:44.210` | And so right away, we ended up building this. |
| `00:18:46.390` | We rolled this out. |
| `00:18:47.590` | And now we have Claude taking a look at all feedback that comes in. |
| `00:18:52.250` | It tries to match it up with system monitors, with system traces. |
| `00:18:56.470` | It tries to look for common trends across things. |
| `00:18:58.410` | It does initial analysis if things look like a bug. |
| `00:19:00.950` | We have tried to make all of those initial steps that we would do looking at tha... |
| `00:19:04.430` | automatic to speed ourselves up. |
| `00:19:07.710` | So we also found ourselves we would take everything it said and then we would ha... |
| `00:19:12.850` | with a suggestion after reading through all of that. |
| `00:19:15.610` | So now we have Claude give us a suggestion on how to fix it and then we found ou... |
| `00:19:19.270` | copying and pasting. |
| `00:19:20.610` | And so we just made that a button to bring it directly over to our development t... |
| `00:19:26.030` | So not everything we built worked. |
| `00:19:29.770` | Just because you're really fast doesn't mean you're always really right. |
| `00:19:33.070` | And we got tons of things wrong as we were building the product. |
| `00:19:36.510` | So I want to tell you about one specific time where we got this wrong. |
| `00:19:40.310` | And that was we started out early on and we built these really advanced controls... |
| `00:19:47.610` | These gave you really fine control over every single pixel. |
| `00:19:51.530` | You could do anything with these. |
| `00:19:53.310` | These were for power users. |
| `00:19:55.310` | And in our early testers, we had a few power users who were very vocal, gave gre... |
| `00:19:59.750` | feedback, and they love this feature. They love this set of tools. And we though... |
| `00:20:05.430` | we have something good on our hands, all the feedback we're hearing looks great,... |
| `00:20:08.870` | as we dug into the usage, we found that everybody else hated them. Like, didn't ... |
| `00:20:15.210` | them, people hated them. They were confusing, they were actively harmful to the ... |
| `00:20:20.990` | And so we ripped them out. For us, this took a grand total of one week. So, yes,... |
| `00:20:27.790` | off track, but from idea to course correcting and ripping out the feature and go... |
| `00:20:32.730` | the next thing, took us about a week of time. |
| `00:20:36.250` | If we had been doing a quarterly development cycle and we had planned this to do... |
| `00:20:41.410` | a quarter, we would have been off track for an entire quarter. |
| `00:20:44.970` | That would have been really bad for the product given that the entire product sh... |
| `00:20:48.950` | than a quarter. |
| `00:20:50.450` | For us, it's not necessarily can you always go fast, it's can you always iterate... |
| `00:20:54.150` | in a small enough cycle that you able to very quickly find out when you wrong Th... |
| `00:21:05.380` | One, this taught us that we should be a tool |
| `00:21:08.000` | that lifts the level of craft for everybody, |
| `00:21:11.140` | not just the ceiling on power users. |
| `00:21:13.240` | It also taught us that we want to be as open as possible |
| `00:21:15.600` | because there will be users that we never meet the full needs of. |
| `00:21:19.400` | There's going to be some power user out there |
| `00:21:21.960` | who wants to do something very specific |
| `00:21:23.400` | that we're not going to support. |
| `00:21:25.080` | That's what convinced us that we want this to be a very open tool. |
| `00:21:28.160` | That's why if you export from it, you get HTML, CSS, JavaScript. |
| `00:21:32.980` | That's why we're trying to do more and more integrations that you can take thing... |
| `00:21:37.480` | into other tools. |
| `00:21:38.480` | We haven't talked about this publicly before, but I think this week or next week... |
| `00:21:42.300` | to be pushing out the ability for any design tool to integrate with quad code. |
| `00:21:46.840` | Sorry, quad design. |
| `00:21:48.920` | Just via their existing MCPs. |
| `00:21:51.320` | So we want this to be a tool where you are able to explore, it lists the level o... |
| `00:21:55.560` | for everyone, and then the people that do have very specialized needs, if they h... |
| `00:21:59.380` | tool of choice, they can just take their designs right into them. |
| `00:22:02.040` | They're yours. |
| `00:22:04.940` | So this slide's fun. |
| `00:22:06.720` | On the left is that first prototype. |
| `00:22:10.520` | It's a terminal in a browser, and that's about it. |
| `00:22:13.500` | It's not the shiniest thing in the world. |
| `00:22:15.720` | This is the level of those early explorations where all you're looking for is th... |
| `00:22:20.220` | bit of promise. This is not obviously the final product that launched. On the ri... |
| `00:22:26.100` | it's the final product that launched. There's a lot that separates them. I'll ad... |
| `00:22:30.980` | one on the left, it does have a little bit of promise in it. But 99% of the valu... |
| `00:22:38.460` | from those ten weeks of iterating and shipping and talking to users every single... |
| `00:22:44.160` | value came from the experimentation, figuring out what the right thing was to bu... |
| `00:22:49.020` | than knowing in advance this is exactly what we are going to be doing. |
| `00:22:54.360` | So to put the amount of iteration this team does in perspective, Cloud Design is... |
| `00:22:59.280` | on a Friday, and by the following Monday, we had shipped 62 improvements to the ... |
| `00:23:05.640` | That's a good number given the size of the team we talked about earlier. |
| `00:23:10.260` | And we made the product more token efficient. |
| `00:23:13.420` | We improved its ability to handle images, we made it better at exploring code ba... |
| `00:23:19.200` | we made most exports instant. |
| `00:23:21.100` | It's a pretty long list and was all based off of user feedback that we got on la... |
| `00:23:25.240` | day. |
| `00:23:26.240` | Now, this was not a Herculean effort. |
| `00:23:29.300` | This was not something that required all-nighters from everybody. |
| `00:23:33.460` | This was something that was very natural because the team had built up the proce... |
| `00:23:37.060` | muscles and the practice of doing this every single day for ten weeks prior. |
| `00:23:41.900` | This became a quick, very normal way of working for us. |
| `00:23:45.600` | I mentioned earlier that quad design has been live for one month. |
| `00:23:50.480` | And so, also, you may have seen this, but last night we doubled token limits for... |
| `00:23:56.140` | product. |
| `00:23:57.140` | So, one of the pieces of feedback that we heard was that people liked it, they w... |
| `00:23:59.800` | to use it more, so we're making that easier. |
| `00:24:01.520` | So, that's across all subscription plans. |
| `00:24:06.020` | Before we close, I want to share one of the more counterintuitive things we've l... |
| `00:24:08.940` | working in labs, and that is that you do not want to work on the thing that alre... |
| `00:24:14.700` | You often want to prototype the thing that almost works. |
| `00:24:18.500` | And the reason why you do that is because the models are improving so rapidly. |
| `00:24:24.240` | The level of intelligence keeps going up. |
| `00:24:28.300` | And the next model may just fix the issues that you cannot solve via engineering... |
| `00:24:33.500` | We had this with Cloud Design. |
| `00:24:34.740` | were a bunch of issues in that early prototype that we did not solve. We did not... |
| `00:24:40.080` | with clever engineering, we did not fix them with amazing insights, we fixed the... |
| `00:24:46.060` | Opus 4.7 coming out. And that's going to be true of a lot of things that everyon... |
| `00:24:51.800` | this room that we all work on together. The model releases are a tide that lifts... |
| `00:24:57.740` | They do a lot for you. So, remember, early on, you're just looking for that hint... |
| `00:25:03.240` | You're not looking for something that works in full, that works completely, that... |
| `00:25:07.220` | every edge case. |
| `00:25:08.220` | You're looking for something that could become that in the future. |
| `00:25:11.820` | And so that's why when you find it, you want to start exploring, start building,... |
| `00:25:16.560` | bringing in front of users and figuring out the shape of the product that works. |
| `00:25:20.000` | Because the shape is the most important thing and the thing that we all get wron... |
| `00:25:23.180` | first start. |
| `00:25:24.180` | We all have to iterate on it. |
| `00:25:26.040` | So there's three concrete things that you can try tomorrow from this talk if you... |
| `00:25:33.000` | if there's nothing else you took away from it. The first is go ahead, next time ... |
| `00:25:36.500` | going to write a PRD, skip it. Don't write it. Instead, just talk with Claude, t... |
| `00:25:42.100` | somebody on your team and take the transcript and don't talk about specifically ... |
| `00:25:45.820` | feature is, what buttons there are. Instead, just spend time talking about why y... |
| `00:25:51.000` | to solve this problem. What are the characteristics of a good solution? And give... |
| `00:25:56.800` | Design. Give that to Claude. Ask it to give you three variations on a prototype ... |
| `00:26:01.960` | solve that. See if that works for you. The second, pick something that you've be... |
| `00:26:07.720` | for. It could be feedback clustering like we did. It could be a new analysis too... |
| `00:26:12.840` | just build it one afternoon. Everyone waits on tools when at this point internal... |
| `00:26:19.280` | building your own stuff, is rapid. It's very fast. So go ahead and scratch your ... |
| `00:26:24.140` | You will be happy that you did. It will pay itself off very quickly. The third, ... |
| `00:26:29.020` | This one looks simple but I think this is the hardest. |
| `00:26:31.980` | Take one real feature request. |
| `00:26:34.160` | I don't mean like a small bug fix or a padding change. |
| `00:26:37.160` | Take one real feature request from a user and turn it around in 24 hours, get th... |
| `00:26:43.700` | front of them and follow up with them for feedback. |
| `00:26:46.220` | The reason why I bring that up is not this urge to go faster. |
| `00:26:48.940` | It's because the first time you do this, if you're not doing this already, you'r... |
| `00:26:52.920` | to find that there are a bunch of roadblocks in your existing process and the ex... |
| `00:26:57.500` | way that you build software. |
| `00:26:58.960` | if you have been on a longer timeline. That could be everything from the way tha... |
| `00:27:02.680` | do deploys, the way that you ask somebody on your team to review your code, that... |
| `00:27:08.060` | be a whole host of things. So going through this once really helps. And I wouldn... |
| `00:27:13.540` | to do all three of these at once. I would layer these on. Each one is going to t... |
| `00:27:18.620` | you something a little bit different that helps you move a little bit faster. Th... |
| `00:27:22.880` | the last show of hands, I promise. Who is going to try number one? A lot. Two? T... |
| `00:27:32.960` | Okay. Thank you so much. That's the talk. Thank you for your time. I would love ... |
| `00:27:39.660` | to folks who have used the product or even those that haven't. I'm going to be b... |
| `00:27:42.820` | demo booth for most of the day for Collade Design. It's down at the end of the h... |
| `00:27:46.920` | So please come find me, tap me on my shoulder, come complain to me or tell me wh... |
| `00:27:51.200` | you. I'd love that. So thank you so much. |