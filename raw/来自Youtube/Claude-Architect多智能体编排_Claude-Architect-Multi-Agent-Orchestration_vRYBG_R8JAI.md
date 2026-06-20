---
type: note
description: "频道/作者：ExamPro"
timestamp: 2026-06-20
---
# Claude Architect: Multi-Agent Orchestration

> **频道/作者**：ExamPro
> **链接**：[https://www.youtube.com/watch?v=vRYBG_R8JAI](https://www.youtube.com/watch?v=vRYBG_R8JAI)
> **时长**：2:09:42
> **发布日期**：2026-04-29
> **字幕抓取日期**：2026-06-20
> **字幕来源**：YouTube 自动生成字幕（en）
> **段落数**：747

---

## 信达雅中文翻译

> **频道**：ExamPro（Andrew Brown）
> **翻译**：AI 译校 · 信达雅风格
> **说明**：本期为 2 小时编程教程，讲解 Claude 多智能体编排（Multi-Agent Orchestration）的核心模式与实现。以下按主题分章整理，保留关键技术细节。

### 一、Hub-and-Spoke 架构：协调者模式

Hub-and-Spoke 是一种模式：一个协调者 Agent 居中，所有子 Agent 只与协调者通信。

关键约束：
- 子 Agent 之间没有直接通信线路。研究 Agent 不能直接跟审查 Agent 说话——必须经过协调者
- 协调者负责：路由决策、上下文共享、错误处理、可观测性
- 可观测性天然好——所有信息经过一个瓶颈点，方便检查和收集

协调者的任务生命周期：
1. **任务分解**（Decomposition）：把大任务拆成子任务
2. **任务委派**（Delegation）：决定谁来做
3. **结果聚合**（Aggregation）：把所有结果合在一起产出最终输出
4. **路由决策**：根据查询复杂度决定调哪些子 Agent

路由不是静态的。简单事实问题用一个 Agent；多步任务串行委派、结果前传；独立子任务并行委派。聚合时要解决冲突、让数据漂亮。

### 二、基础协调者实现

用 Haiku 4.5 快速搭了一个基础协调者——有创建任务、获取状态、完成任务等工具。但问题很明显：太泛了，用例不具体，很难判断它到底在做什么。

切回 Sonnet，要求改进：加入分解、路由、聚合的明确步骤。让 Claude 提 10 个可能的用例——最终选了**求职申请筛选器**。

子 Agent（spokes）：关键词扫描器、深度评估器、红旗检测器。协调者负责调用每个 spoke、决定调谁、收集和合并输出。

代码实现：每个 spoke 有独立的 prompt 和调用逻辑，有调度工具决定路由。协调者 prompt 明确定义："你是求职申请筛选协调者，编排三个独立筛选 Agent，聚合结果。"

运行结果：协调者路由到关键词扫描→深度评估→红旗检测→最终推荐。"Alex 与高级职位强匹配，7 年经验，无红旗，建议录用。"

### 三、窄分解问题（Narrow Task Decomposition）

当 Claude 分解任务时，它只能委派它想到的东西。

例：给一个"全面分析电动车市场"的任务，它可能只拆成"研究销量、电池技术、主要厂商"——而遗漏了充电基础设施、政府补贴、二手市场、消费者情绪、供应链（锂和钴）、电网容量等。

原因：每个子 Agent 只看到自己的隔离上下文，没有一个能标记遗漏了什么。

解决方案：
1. **在 prompt 中要求自我反思**："分解后问自己——我遗漏了什么视角、利益相关者或维度？补齐后再开始委派。"
2. **用工具做保障**：在委派前触发工具检查——"你提交了子任务分解供审核了吗？"
3. **在聚合层做保障**：聚合时检查——"你确认覆盖了所有维度了吗？"

实际实现中，把"窄协调者"和"好协调者"做对比：窄协调者用固定清单（技能 X 是否在简历上列出？），好协调者先生成筛选角度、自我反思遗漏、补齐后再委派。

### 四、动态选择（Dynamic Selection）

如果对每个 spoke 都跑完整流水线，token 消耗巨大。协调者应该思考需要什么路由，在特定条件下只跑必要的部分。

实现：给协调者路由指导——"简单事实匹配就跳过关键词扫描"、"非传统背景就走技能迁移评估"、"永远不要调用不回答真实问题的筛选 Agent"。

关键洞察：动态协调者实际上在运行时即时生成路由——不是从预定义列表中选，而是根据简历内容动态创建筛选角度。

### 五、研究分区（Research Partitioning）

给三个研究 Agent 同一个简报，你会得到三份重叠的答案和浪费的 token。

解决方案：把范围切分，每个 Agent 拥有一个不重叠的切片。用 JSON 结构定义分区——每个分区有 agent_name、scope、cover、excluded 等字段。

实现：一个分区规划器（partition planner）先生成不重叠的分区 JSON，然后协调者按分区精确调用筛选 Agent。关键 prompt："两个分区不得覆盖相同方面。只包含真正需要的分区。"

可以混合使用代码驱动逻辑和 Agent 驱动逻辑——没有规则说必须全交给 Agent。

### 六、精化循环（Refinement Loop）

之前都是一次性输出。精化循环的思路：把结果反馈回去，迭代改进直到满意。

实现：在协调者 prompt 中加入最多 4 次精化迭代。流程：
1. 初始筛选：按分区调用筛选 Agent
2. 覆盖度评估：所有分区 Agent 报告后，调用评估工具检查覆盖是否充分
3. 精化：如果覆盖不足，只针对识别出的缺口调用额外筛选
4. 最终提交：覆盖充分后才调用提交最终推荐

运行结果：做了两次迭代，覆盖度分数在下降——说明系统在收敛。但是否"好"需要更多数据和测试来判断。

### 七、可观测性（Observability）

中心化协调者的优势：所有信息经过它，天然适合做可观测。

没有可观测性的问题：无法调试或审计运行、静默崩溃、无法回放检查错误、协调者不知道是否所有维度都覆盖了。

实现改进：
- **结构化日志**：带时间戳、级别、分区范围
- **错误处理**：JSON 解析包装 try-catch
- **持久化 spoke 输入输出**：不只是打印到 stdout
- **覆盖度评估工具**：运行中检测缺口
- **显式退出门**：必须先评估覆盖度才能提交最终推荐

### 八、重构（Refactoring）

代码逐渐变成了一个巨大的 main.py——能跑，但不可维护。

重构目标：
- 把代码拆成多个文件：spoke prompt 各自独立、工具函数分离、日志模块独立
- 写一个 refactor.md 文档列出重构任务清单
- 让 Claude 按清单逐项完成、打勾确认

关键原则：
- "如果这不是程序员，你可能不知道这是烂代码。它能跑，但如果我们以后回来看，完全看不懂。"
- "Agent 能看懂不够——必须让人也能看懂。"
- "没有魔法。我们能很快写出代码，但确保它们真正好用是另一回事。"

### 九、核心经验

1. **垃圾进垃圾出**：提示词质量决定一切。"仅仅因为它能产出东西不代表它设计得好。"
2. **没有 100% 的坏方案**：可以混合代码驱动和 Agent 驱动，没有规则。
3. **协调者拥有全局视图**：spoke 是无状态函数，不知道彼此存在。
4. **可观测性不是可选的**：生产环境中需要日志、错误处理、审计追踪、token 计数、延迟监控。
5. **迭代式构建**：从基础开始，逐步加入窄分解修复→动态选择→研究分区→精化循环→可观测性→重构。
6. **测试是必须的**：如果有 100 个申请人样本跑一遍看结果分布，才能真正评估质量。

---

## 英文文字稿（带时间戳）

> 段落格式：`[时:分:秒] 文字内容`

**[00:00:01]** Let's take a look at hub and spoke architecture. So, hub and spoke architecture is a pattern where one coordinator agent sits at the center and all sub agents talk to the coordinator.

**[00:00:07]** I highlighted that weird word coordinator because you're going to be seeing a lot of coordinator agent. And when you think of like Claude Claude code, I have a feeling that this is at least one of the means at least when you're working with sub agents of our communication, right? So, this is going to be something really really useful to learn.

**[00:00:29]** It's going to be really fun and something that you can apply like immediately, okay? So, sub agents never have direct lines to each other.

**[00:00:36]** So, if you have like a research agent over here, it cannot directly talk to the review agent a river agent. It has to go through the coordinator.

**[00:00:44]** And so, that is pretty clear. And the coordinator is going to own the routing.

**[00:00:49]** So, it's going to decide how to route things. Context sharing, so what will be shared? So, the research agent is not going to be aware of what everyone's doing unless the coordinator passes that information along and it gets injected.

**[00:00:59]** So, it really won't know. And any kind of error handling, any kind of observability, any anything like that, okay?

**[00:01:07]** And obviously that would make it really good for observability because now everything's passing through there and we have a choke point where we can check and collect information, right?

**[00:01:17]** And so, here we have kind of the task life cycle of like, okay, we have something that needs to be done and how is it going to get executed out? So, the role of that coordinator is task decomposition. So, break break the task into subtasks, right? Then we have task delegation. So, who is going to be working on that problem? Result aggregation. So, bring it all back together to produce a final result and decide which sub agents to invoke based on query complexity. So, um you know, we have a a lot of things going on here, but let's just kind of walk through it.

**[00:01:56]** So, imagine you're a coordinator and when given a task, it'll break down subtask for each of the available tools and we're saying do not do the work yourself. So, we're basically here defining you know, that you are a coordinator and this is what you're going to be doing, okay?

**[00:02:13]** And then here it's like you're a coordinator and use your judgment.

**[00:02:15]** Simple factual questions, use a single agent. Multi-step task, delegate out to a sequential passing the results forward. Independent subtask, delegate in parallel. So, we're basically defining, okay, what does the routing look like? So, it's not just like static routing. Like it's, you know, use the routing you need to route based on the use case, right?

**[00:02:34]** Which I think is really really interesting. And then down below here it's like, okay, you've gotten all the outputs from multiple agents, combine them into a single coherent response, resolve any conflicts and make the data pretty. So, that's the most basic thing when we're talking about this coordinator agent.

**[00:02:50]** There's a lot of stuff we have to consider when implementing this, but we will go and set up a super skeleton one really quickly here and then we will iterate on it, okay?

**[00:03:01]** Okay, folks. So, what I want to do in this follow along is implement a very simple coordinator agent. So, we'll say coordinator agent simple or basic.

**[00:03:16]** And in here we will make a new main .py And I suppose that we could um pull up some code. I'm going to see if we can switch over to Haiku and save some credits here because it might be able to do it. We'll see.

**[00:03:37]** Haiku. There we go. So, now it's switched over to the Haiku 4.5 model.

**[00:03:40]** And so, I'm going to tell it uh um create uh a very basic coordinator agent um in coordinator basic main.py Please follow our general um coding example would be uh what was one we did? Decision making would probably be one model driven model driven.py. And so, I'm hoping that by giving it that reference, it will know how to reference that stuff and produce something that's going to be generally okay, but we'll see how Haiku does. I really should run Haiku a lot more. I just kind of stick at Sonnet. Um and that's my that's my fault there, right? And so, we will give it a bit of time here, let it accept here and then we will decide whether Haiku could even do it or not and does it have all the components we need? And there it is.

**[00:04:40]** That was pretty darn fast. Maybe it needs a little bit more work to do.

**[00:04:43]** But we have the start of it. Let's close out the tab here. Sometimes it helps to close out the tab and reopen it for whatever reason. It's already done. So, here it says I've created a basic coordinator. We have create task, get task status, complete task task list.

**[00:04:55]** And so, we have the basic stuff. Let's take a look here and see if it's any good. Um so, we have tool implementation. So, tool create task.

**[00:05:05]** Um task status. And so, it's talking about how it has to manage the tasks generically.

**[00:05:13]** Right? Um then down below here, yep, so we have that.

**[00:05:17]** Create a task with an optional list of task IDs.

**[00:05:20]** Um get the current status of the specific task, mark it as complete, list all tasks as completed.

**[00:05:26]** Um so, it seems like it's pretty simple.

**[00:05:28]** Your role is to manage and coordinate tasks.

**[00:05:32]** Well, a coordinator does that in general, but I guess the thing is like this is literally it sounds like it's managing tasks. Create tasks as needed for the workflow, check the task status and dependencies, complete tasks when appropriate. So, what I'm trying to figure out here is what is the use case?

**[00:05:45]** So, set up a Let's go down here for a second. So, we have user message. So, set up a workflow create a task design and then create a task implementation that depends on design and then complete design task first. This is so generic, it's really hard to make sense of it. We have our while loop here. It brought in the while true, so we don't have that max iteration.

**[00:06:09]** Um And maybe maybe might not be a a major issue, but we still might want that in there. I probably should have referenced the other code.

**[00:06:16]** And Mhm. So, I'm just carefully looking here at what we have.

**[00:06:26]** So, we have our tools over here.

**[00:06:29]** And so, I'm not really sure if that really fits our pattern exactly. I'm going to go take a look at our uh diagram here. What do we have? We have decom decompose uh the routing and the aggregation, right? So, um I don't think I see all those steps here. Okay, so what I'm going to do is I'm going to go back to our smarter model here, Sonnet.

**[00:06:53]** Okay. And I'm going to go and ask the coordinator or I'm going to ask it to improve our coordinator code. So, uh you know, for a coordinator agent we should have decomposition tasks.

**[00:07:12]** Um Just a moment here. Routing.

**[00:07:25]** It says assess complexity, but we have routing.

**[00:07:28]** Um We'll say assess complexity complexity and routing and aggregate results. The use case here is um too generic.

**[00:07:47]** Need a better use case. Okay. And so, we'll go ahead and we'll see if it can improve that code. And if not, I might have to write even more detailed prompt. I'm just kind of low on our usage unless the window has rolled over.

**[00:08:06]** Let me take a look here. Nope, I still got 50 minutes for my time to roll over over here, but we'll see.

**[00:08:13]** And so, I just wanted to kind of see it mimic these patterns here. And so, it's not to say that it's not exactly doing it, but it's definitely uh not that sophisticated, right?

**[00:08:25]** Because I would expect there to be a prompt for the routing component here and I'm not seeing it here, right?

**[00:08:32]** It does say set up a workflow. So, technically that is that that right there.

**[00:08:38]** So, maybe maybe it is kind of being implemented, but we'll give it a second here. Now, I'll rewrite a concrete use case. Technical due diligence, decompose the complex software review.

**[00:08:45]** Oh, I don't like that. No, I'm going to stop this for a second here. Stop stop stop stop. I I don't like the use case.

**[00:08:55]** Oh, it already stopped, basically.

**[00:09:00]** So, it says breaks the request into five fixed areas. Well, I already got the code, I guess. Let's just take a look here.

**[00:09:10]** Um So, here it says a user submits a software system for technical review.

**[00:09:19]** The coordinator has a decomposed the requests assesses the complexity per area, routes and and does that, runs an appropriate handler, aggregates all findings into a single report. So, that sounds good.

**[00:09:31]** Uh we have tool decompose request, tool assess complexity.

**[00:09:36]** Um I don't really like the use case because I want something that's going to be easy for us to validate and test and this will be too complicated. I don't like the use case.

**[00:09:50]** Can you propose to me uh 10 possible use cases.

**[00:09:56]** I want something that, uh, is not super complex that will be like super computational but would need complex routing and choices.

**[00:10:12]** Uh, don't implement, just suggest ideas. Okay. And so, I want to see if we can pick something a bit better. If it can't, then I might have to, uh, decide on myself here. Here's a So, job application screener.

**[00:10:26]** Um, event planning coordinator, bug triage, restaurant order customizer.

**[00:10:33]** I mean, I like the travel one that might have to go through the internet. I don't necessarily want to do that.

**[00:10:43]** Mm. Okay. So, like with number what would be the subtasks?

**[00:10:58]** The subagents used. Because this is what I'm trying to figure out. And this comes back to, you know, this idea where we have an idea and it's doing a bunch of stuff, right?

**[00:11:10]** So, like coder, writer, researcher, planner, data, right? So, I'm trying to see what we have.

**[00:11:15]** And so, we go over to here. And so, we have request to composer. So, takes the job posting resume extracts it out.

**[00:11:24]** Looks at each criteria and decides the routing.

**[00:11:30]** Okay. Executing execution phase.

**[00:11:32]** Um, the actual routing targets.

**[00:11:36]** Aggregation phase. And so, it has two different ones here.

**[00:11:43]** So, I guess my question is like, is the ownership I mean, like, should the coordinator be routing to a decomposer and uh, router routing because I thought the composer is supposed to own it in a hub and spoke architecture. And so, that's the only thing I'm I'm just making sure like maybe these are just tools and it's calling out to them and so, it still has ownership. So, you're right. In a proper hub and spoke architecture, the coordinator is the hub. It owns it. The decomposer isn't a sub subagent. That's why the coordinator owns its responsibility. So, we have that. Sure.

**[00:12:30]** That looks like something. So, the coordinator decomposes, assess complexity, decides routing, aggregates.

**[00:12:35]** The spokes just execute. This smells like something belongs to the coordinator versus subagent. Does it need a full picture?

**[00:12:43]** Does it need the full picture to do the its job? Decomposer is always routing, always needs the full picture.

**[00:12:50]** Uh, I don't I don't I don't know what you mean by full picture.

**[00:12:59]** But we are implementing hub and spoke model architecture. Okay. So, I don't know what he's trying to say there, but, um, maybe it means like I think I think that the context. You're right. Okay. So, it says you're right. Oh, yeah, of course I'm always right. Um, receives the request, call spokes, aggregates the results.

**[00:13:24]** Independent workers, each job does one, no knowledge of each other. That's right. Okay. So, for job app application screener, now we have keyword scanner, deep evaluation, red flag detector, score aggregator.

**[00:13:34]** Takes all the spoke spoke outputs.

**[00:13:36]** The coordinator owns calling each spoke with the right input deciding which spoke to call collecting and combining their outputs.

**[00:13:46]** Yes. Okay. And so, now we're getting something there.

**[00:13:50]** Just because it said it did it, does not mean it did. And this is me looking at it going, "Uh, that doesn't seem right." Right?

**[00:13:56]** Um, and so, we will let it go ahead and do that. I'm not getting any more warnings. So, oh, it says now using extra credits.

**[00:14:03]** So, I'm over my usage. >> [laughter] >> But I should be okay.

**[00:14:08]** This is You'd be surprised how long or how far five five dollars will take you here.

**[00:14:15]** Okay. So, it says it's completed the architecture here.

**[00:14:17]** Um, let's go take a look and check out the code.

**[00:14:22]** So, now we got a lot of stuff here.

**[00:14:23]** Okay. So, keyword scanner prompt. You are a resume keyword scanner. Check whether it required skills from the job posting, uh, appear explicitly in the resume.

**[00:14:33]** For each required skill, output one line. Be literal. Do not infer or extrapolate. Report only what is explicitly stated. Okay. And so, then we basically have all the ones here and they're fine. Of course, if we're doing this for real, we would be tweaking this all by hand, of course. And then here we have the actual, um, I guess they're saying the spokes. We could say subagents, if you would, or they have them called the spokes.

**[00:14:58]** And each of them are individually calling uh, this stuff. I'm not sure why they're doing it this way. It seems like this could be easily refactored. This seems a little bit, uh, messy. Maybe they're doing this so that you could improve it later on, but to me this, um, seems like this should all be just one function.

**[00:15:16]** And then we have the spoke aggregator where there actually is a little bit different. So, they do have that there, which is fine.

**[00:15:22]** Then we have our dispatch tool.

**[00:15:24]** Okay. So, basically like where should it go? We have And yeah, whether it should go there or not. Tool schema. So, what the coordinator hub sees.

**[00:15:33]** Mhm. So, we have run keyword scanner.

**[00:15:39]** Oh, like these are the actual tools deciding whether they should get triggered or not. That's fine.

**[00:15:45]** Then we have our coordinator prompt. So, you are a job application screening coordinator. That's fine. Your job is to orchestrate three independent screening agents.

**[00:15:53]** Mhm. Uh, your job is to orchestrate the three independent screening agents and then aggregate the results.

**[00:16:01]** You may run three screening agents in order. Do not skip any of them. And so, here it's defining that saying you have a explicit order. And so, obviously there could be more complex routing than this, but this is all there is.

**[00:16:14]** Then we'll go down to here. And so, here we have our job postings. I was going to wonder where this data was.

**[00:16:20]** Cuz I was going to be like, is there, are the resumes generated here? And they do. So, our we have our job posting, then we have our our resume. We only have we only have a single resume, which is fine.

**[00:16:31]** Alex Chen, that's interesting. Okay. So, we go down here and we're passing that data in. It's going through that loop.

**[00:16:37]** Again, we have this while true. So, I'm not sure if that's the best idea to have that while true like there, but I will run it and uh, take the risk.

**[00:16:50]** I think it's fine. Uh, you know what? I I do want a max iteration. So, I'm going to go here and just say like uh, the while loop is true. Do you think we should have a max iteration or any other suggestions so it doesn't go on forever.

**[00:17:19]** Okay. And so, that's what I want it to answer there. We have the max We might just do the max iteration cuz now I've basically told it to do that.

**[00:17:28]** So, here it says, um, a while true loop with no exit condition. I mean, there is an exit condition. It's the break right here.

**[00:17:37]** Um, And then we have a timeout for this use case.

**[00:17:41]** So, a max steps caps is is the right fit. That's what it's suggesting.

**[00:17:46]** Fair enough. Mhm. How's it uh, counting the max steps?

**[00:17:57]** So, the loop executes only when the condition becomes false, max steps, and not when and not when the break is hit.

**[00:18:06]** So, it cleanly catches runaway loops without needing extra flag. Okay, that's fine. The cap is 10, double the expected five steps, give the model room to retry. I just don't see where it's counting them. Oh, I guess it's right here.

**[00:18:21]** Oh, sure. I I guess so, but I mean, that's the same thing as a max iteration.

**[00:18:26]** Um, so, max steps is the same as max iteration.

**[00:18:36]** I guess it's fine. I mean, I'm sure it will still work. So, if it doesn't, we'll find out. And again, you know, you can just watch and see what my outcome is before you do this if you do not want to waste credits because I've made a poor decision. Um, you know, like I'm loading my thing up with like five dollars at a time. So, I'm I'm not that worried about, um, uh, small losses like that. So, we'll go ahead and go into here.

**[00:19:03]** And let's go ahead and execute this.

**[00:19:05]** And yeah, I'm not using my subscription.

**[00:19:12]** Now, we could probably port this over to agent SDK, um, and this would be greatly simplified. We might do that later to see what's happening here, but won't do it right away. So, here it says, um, coordinator routes to the spoke.

**[00:19:23]** Okay. So, it's found stuff. Something's missing. Coordinator routes to the run deep evaluator.

**[00:19:30]** Uh, strong alignment with the senior level role with seven years of total experience. Cool. Strong fit.

**[00:19:36]** Uh, coordinator routes to the red flag detector.

**[00:19:41]** Imagine someone, uh, just coded this and this is what's keeping people out of their jobs. That that would be a bummer.

**[00:19:45]** And then we have step two of 10. So, match keywords.

**[00:19:49]** Uh, strong, no flags, decision higher.

**[00:19:52]** Alex demonstrates strong alignment with senior level requirements. Coordinator for final recommendation for hire, so it's recommending it.

**[00:20:02]** Six out of the seven, strong, no red flags.

**[00:20:06]** All core required skills present.

**[00:20:07]** Seven years experience, whatever, whatever.

**[00:20:11]** And so we just implemented our own coordinator. Again, the only thing that's really simple, like I'm still not the confident about the wild loop, but the only thing that is um very simple is the routing. But the routing obviously is being handled here.

**[00:20:23]** Um and so, you know, like in that diagram, it just seems like it's a separate step. Like you cut them up and then you do that.

**[00:20:32]** Um and so I'm not sure if that should be separated out, but the point is we did implement coordinator agent. Um and that's something we could decide later on if we wanted to have an individual step for more intelligent routing. So, that's the only thing that I might um consider. Like I I would probably ask it right now like if it should be ran twice, but I'm I don't know. I don't want to cuz I don't think it's going to just tell me. I think it's going to actually try to do it. And so I don't want to muck with it. And so I'd say that's fine, but just consider that that's an uncertainty that I have right now.

**[00:21:02]** And so I'm going to go back a directory here. We'll just say get at all, get commit {hyphen} M. Uh basic coordinator.

**[00:21:10]** I thought that was kind of fun.

**[00:21:12]** I thought the results were pretty good.

**[00:21:15]** Okay, and I will see you in the next one, okay? Ciao, ciao.

**[00:21:20]** Okay, let's take a look at narrow task decomposition. So, when uh Claude decom- decomposes a task, it can only delegate what it thinks to ask for. Okay, so here we have an example where it says, "Give me a comprehensive analysis of the EV market. Break the user's task into subtasks and delegate them out." And so here we see the subtasks. We have research EV sales figures, research EV battery technology, research major EV manufacturers. So, the initial decomposition is too narrow, entire topics never get researched. It's because each subagent only sees its uh its its own isolated context. None of them can flag what's missing. So, what got missed? Charging infrastructure, government policies and subsidies, second-hand EV markets, consumer sentiment and adoption barriers, supply chains like lithium and cobalt, grid capacity implications. Okay? Um so, you need to be very specific on the task so it fully covers what you expect. So, here it says, "Give me a comprehensive analysis of the EV market." Again, and so as the coordinator, when decomposing the task, of course we're generating out the the subtasks, but ask yourself, you know, more information. Ask subtasks to cover those gaps. Only then begin delegating. And for research tasks, specifically consider this information.

**[00:22:42]** Now, what's interesting here is like we created um in our our job application thing, but this thing is talking about research.

**[00:22:51]** So, they might they might have just a single subagent that just does research.

**[00:22:53]** And so the idea is that all these tasks are going to the same subagent as maybe separate um instances that are spawned, and they're being tasked with doing different things. And so this is where you have a little bit more complex routing, right?

**[00:23:06]** Or different kinds of routing. Um and so one thing that we can do to catch weak decomposition is uh cuz like let's say um for whatever reason, in here, uh this coordinator uh that you wrote here to help it be very specific, uh it fails or you just don't do a good job. Then you could implement a tool.

**[00:23:28]** And so the tool um can try to catch it.

**[00:23:31]** Because now when the court or when the agent goes and does a task, it's going to say, "Oh, did you submit a a subtask breakdown for review for delegating?"

**[00:23:42]** Well, then trigger this tool and then make sure right here that you do this up. And this gives you a guarantee um you know, of this. Or maybe you want to be a little bit more flexible what the input is from the user. And uh so this thing being decoupled might do that. Um another way uh that you can fix this problem is at the aggregate level. So, after you're aggregating the results, it can check here and say, "Hey, um did you make sure before writing the answer that you uh met these things?" And so you now have basically two different safeguards for um improving over uh narrow task decomposition. So, I'm not sure if this will work in the one that we're building right now or we'll have to build a new little coordinator. Um but we'll go and try it out, okay?

**[00:24:28]** All right, so we are back. And um what we'll do here is we'll try to figure out this narrow task decomposition. I don't know if it's going to work for our case.

**[00:24:36]** Because um for research, it's a really good um use case, but will it be for this one? I don't know.

**[00:24:43]** Um so, I'm going to go ahead and just copy all this code here because we already have some of this. Good.

**[00:24:48]** And Claude's going to have an easier time working with tweaking that.

**[00:24:52]** I would have an easier time working off of this.

**[00:24:57]** So, um let's go down to where the main coordinator prompt is. So, here it says, "Uh you're a job application screening coordinator. Your job is to orchestrate three independent screening agents and the aggregate their results. Run all three screening agents, keywords, deep evaluators, detectors.

**[00:25:16]** So, um let's go ahead and just ask it."

**[00:25:19]** Okay, so we'll go here. We'll say, um for our narrow task decomposition main for uh our coordinator prompt, is the uh decomposition um is our task decomposition too narrow?

**[00:25:49]** And what do we need to ask for better decomposition?

**[00:25:56]** Okay, because this one's pretty darn simple, right? It's just like there's these three things, feed it into those three things. Cuz it's not conducting research, right? Um it's not going out and looking at large bodies of text and trying to figure it out.

**[00:26:11]** So, you know, maybe if there was like more than one source, then that would be useful. And so maybe that's what we might recommend here in just a moment. I might say, "Hey, like uh you know, assume that you're ingesting more than one source of information, um and that might be a better example." But let's see what it comes back with here, and then I'll tell you whether I agree with it or not. Just because it will produce something doesn't mean that it's useful.

**[00:26:32]** So, we will find out here, okay?

**[00:26:33]** Also, I was just thinking about this.

**[00:26:36]** What we should have done is just taken the coordinator information and provided it uh to here with the basic information because I feel like it's consuming a lot more um tokens than it should require. I mean, it's not saying there's that many here, but it is taking uh some time here, and I again I'll just wait, but I should have really just extracted out that individual information.

**[00:26:54]** So, let's take a look here. And oh, yeah, we can edit the main file. That's fine, yep. I thought it was done. I guess it's not done.

**[00:27:02]** Okay, so let's take a look at the problem here.

**[00:27:05]** Spokes are narrowly scoped but appropriately interpretive. That's actually reasonable. But if you're designing new coordinators, well, I'm not designing new coordinators. But we'll we'll take a look here. Spokes answers what is X.

**[00:27:18]** Python found. But without access to the resume.

**[00:27:23]** Um spokes answers what does X mean for the higher?

**[00:27:32]** Receives pre-interpreted signals and can make the uh integrated judgment.

**[00:27:38]** So, I guess we're trying to determine like is it fine? So, what to ask? So, so is it narrow? So, is skill X listed?

**[00:27:45]** Does experience demonstrate the skills X required? So, if it's narrow, saying like is it just listed or is it actually telling us? So, that would be better.

**[00:27:56]** That's true. Uh narrow, resume only. And so this is what I was talking about where we would have more than one type of um uh information feed. But here it's saying in feed in the resume and the job posting for the fit.

**[00:28:08]** Context, what granu- granularity? So, one spoke per keyword, one spoke per uh decision dimension, whatever. So, this file runs both the coordinator of the same candidate.

**[00:28:22]** So, you can see how the narrow decomposition loses the 50 million requests per day nuance.

**[00:28:29]** While the better one catches it.

**[00:28:33]** Okay, so we'll go back up to here. I'm just trying to make clear the this thing that we're looking at. So, narrow antipattern.

**[00:28:40]** What is X? Python found. Six years, three, no gaps. That's probably like how actually recruitment people work. They aggregate receives new facts, it still has to do all the reasoning, but now without access to the resume.

**[00:28:54]** So, it spokes answers what does X mean for the higher?

**[00:28:57]** Strong trajectory risk. Okay, so one thing I I was thinking of is like you need to cross-coordinate this information, right?

**[00:29:05]** So, um I would say, you know, one thing one thing I noticed is, you know, can we validate the number of years based on based on the resume information?

**[00:29:21]** Can we mock other data sources that uh that we would feed in where uh if we didn't do better task decomposition with very specific things to check, we would run into an issue?

**[00:29:44]** Because that's I think what's going to take it, but like that was one example of like, okay, well, you know, if you had to validate how many years someone had experience, you'd look at the resume, but you might also look at uh projects or references or other stuff.

**[00:29:56]** And so, let's just see if it can, you know, consider other data sources.

**[00:30:00]** Uh maybe we should just want to do EV one because research is a really a really good one, but I mean in the sense like we are researching if there are multiple things. Like maybe they have blog posts and stuff like that. But we'll we'll see what comes back here and I might make send uh suggestions for data sources, okay?

**[00:30:17]** All right, it is back. Let's see what it's done. So, we'll go up to here. Key addition. So, show activity since 2018 from uh a Git profile. Let's see. All All assessed skills are above senior threshold. Verified 7.6 years experience.

**[00:30:34]** Um okay. I mean, did it run it again? I didn't tell it to run it, but um I guess what we should do is just take a look at what the new coordinator information is.

**[00:30:46]** Your job is to coordinate uh three independent screening agents and then aggregate the results.

**[00:30:53]** I mean, this isn't this is showing steps, which is fine.

**[00:30:57]** But we're not seeing it doesn't seem to understand what I'm trying to tell it. Okay. So, No, I don't think it understands. So, what I'll do, just give me a second here.

**[00:31:10]** I need to give it an example and I just need to extract out of that.

**[00:31:13]** Give it a better example here and we're just going to plot I have my screenshot.

**[00:31:18]** I just don't have the raw data. And so, I'm just going to uh chat GPT or something here off screen be like, uh get me get me the text.

**[00:31:24]** Okay. And just give me just a moment here.

**[00:31:30]** Just getting the text here off screen.

**[00:31:32]** See, so getting the text. And I'm going to feed it as an example of like more information.

**[00:31:41]** Okay, so like we'll go back here.

**[00:31:51]** Uh so, you know, you know, you know, I don't think you understood.

**[00:31:57]** Uh to improve narrow task decomposition, we should be giving it specific considerations.

**[00:32:14]** Okay. Oh, no, I didn't say it to do that yet.

**[00:32:21]** Okay, we'll paste that in as an example, right? So, I don't know if it knows that's an example, but I think it might know.

**[00:32:28]** So, hopefully it understands cuz we're talking about this this area here.

**[00:32:37]** Um and if this fails, then we could just again just make it it might even try to change to EV, but we will see what happens here.

**[00:32:45]** Um and wait a moment and see what it comes back with.

**[00:32:48]** Okay, so some of your examples general through that Now, did it change it to EV stuff or is it actually changing it to uh a better part here. So, let's take a look here.

**[00:33:02]** So, what did it change? Let's take a look here. So, here's what changed. The domain EV. No, I didn't want you to change the domain. I just wanted you to use that as an example of uh specific task decomposition.

**[00:33:21]** Okay, so there it's already kind of messed up and I had a feeling that it would do that because I literally did not put e.g. or stuff in there. And maybe it's just that what we're trying to do does not work for our use case.

**[00:33:33]** Right? Maybe but it like I I still think it is because you are doing research.

**[00:33:37]** You're collecting information and and gathering it, but we're just assuming that we already have these things and doing analysis on that information. But uh you know, when you're doing broad research and there's a lot of information, then it can do do more there. So, revert the domain name, but we'll do self-reflection structure into the hiring coordinator.

**[00:33:55]** Um And so, we'll take a look at what it has and maybe we still will do the EV example separately.

**[00:34:02]** Um I mean, it still has these in here. So, I'm not sure what it was saying. I should don't save cuz I'm not trying to change that right now.

**[00:34:10]** Yeah, so like you are a research coordinator.

**[00:34:16]** >> [laughter] >> And uh I don't know if this is the way that uh the topic makes money where uh you tell something and it doesn't do the right thing and uh it's making more stuff here. But we'll wait a little bit, okay?

**[00:34:26]** All right, so it's back. And so, we say, okay, um back to original domain right in the pattern. What changed? Narrow coordinator mirrors the agent basic tells them all exactly the three checks. Fix the pipeline, no self-reflection. But that's not what I want. Better coordination. Same domain, same spokes. General initial screening angles. What am I missing? Fill the gaps.

**[00:34:45]** And you know, I think I think it's struggling here. Let's go back down here. So, we'll go and take a look here again.

**[00:34:52]** Well, here we have the narrow coordinator. So, it says here, screen the uh the candidate by running the following checks.

**[00:34:59]** And then down below here we have better coordinator. So, generate initial list of screening angles. Ask yourself, what perspective stakeholders or dimensions are missing? Add screening angles to cover those gaps. Only then begin delegating to screening agent tool. For hiring decisions, specifically consider technical skills and soft skills, hard requirements, what candidate has done and etc. After all screening angles are covered, synthesize report here. So, now I would imagine that it's basically just hitting a single agent. Yes, it is. And so, before we had those separated out tasks, right?

**[00:35:36]** But just as I thought, it's like in order to do it, um the idea is that you say you're you're screening agent and then you are contextualizing each one of it. So, in a sense, each of these are basically turning that into a specialized um a specialized one as before we literally had three separated one out.

**[00:35:57]** Right? So, that I think that's what we're getting at. So, that is what we want. That's actually good. So, we'll go all the way down here.

**[00:36:04]** And what we'll do is we'll go It says both the screen agent is identical both.

**[00:36:08]** The only variable is the coordinator prompt. So, with a uh hiring specific checklist of what the coordinator routinely uh looks for. So, let's go ahead and run that. I believe that's going to give us a better result. Okay, so we'll go here.

**[00:36:19]** We'll say, python main.py. I'll run it.

**[00:36:24]** And so, here it's going through it. So, and we're seeing the numbered values of what it's checking for.

**[00:36:36]** Okay. Does the resume demonstrate all the required skills? Does the candidate experience depth? Are there there any red flags?

**[00:36:47]** Has somebody else experience the limited?

**[00:36:53]** Um uh in the 5-8 senior range. No employment gaps or job hopping detected. The career directory is logical etc.

**[00:37:03]** Um and so, we have that there. This is the narrow one, right? So, fixed checklist, no gap check. Okay, so let's go down to the more complex one.

**[00:37:13]** Um So, we'll go down to this one. So, now we have way more information. So, instead of those three individualized things, um and remember there there was three separate things before. Now, we have um these I just want to compare the old one quickly here cuz I just can't fully remember.

**[00:37:31]** We go here. Yeah, notice that we have three individualized prompts. And even with the narrow one, I guess it's still only passing it through those three. And so, um that's interesting. But anyway, So, here does the candidate demonstrate mastery of etc. Okay, so we go down here.

**[00:37:49]** And I guess we can't really see the individualized results. So, that would be something that you might want to do is like output all of them and then save them and then save the generated uh final one to to exactly see what it is.

**[00:38:03]** So, core stack matches excellent. Okay.

**[00:38:05]** Risk and gaps. Questions for interviews. Final Final recommendation. Now, we have a maybe.

**[00:38:12]** Alex is qualified candidate, but has some gaps for a true senior role. Hire if your team values this passive whatever. Bottom line, Alex is a strong back-end engineer. And then we have coverage.

**[00:38:23]** So, it's way better in terms of its information. But really to test this, you'd actually have to um you know, create sample data, right? And test it and then and then adjust and say, hey look, uh this is not how I would have judged it, right? Based on that information. But this is the example that we wanted, but really that works when you know, there's a generic research agent and then these individualized things are going in and kind of helping to specialize that research agent for its task. Um but yeah, that was cool.

**[00:38:52]** All right, let's talk about dynamic selection. So, the idea here is that when you have your coordinator and you have sub agents, um you might uh find that if you run the entire pipeline for every single possible spoke uh in a sequence, that you are consuming as much as you can. And so, with your coordinator, you probably want to tell it to think about what kind of passing it needs or what kind of routing it should have and give it ideas of kind of routing that it can perform under certain circumstances so that it's doing exactly what it needs to do. Even here it's saying like, you know, uh only invoke it if it makes sense. Um and a way we can catch that problem. So, if we have a a poorly designed um uh dynamic selection system, you can set up a tool just like how we talked about with the narrow task decomposition, you could set up a tool that says, "Hey, did you do a good job here?" You can do the same thing with a tool as well.

**[00:39:48]** Um and I mean, it's really going to depend depend on what you're doing, but that's something that you know, you you'll want to consider, okay?

**[00:39:57]** Hey folks, we are back and we are going to try to do some dynamic selection. So, um you know, for hours, uh our our job application, um basically, we are taking in um information from from one thing, but basically, uh it's just checking everything. And so, you know, the question is like, can we even think of any kind of select dynamic selection that would be needed to be performed for a job application? Because I feel like it would be more if you were to ask certain questions to the agent along with this coordinator, then that's where it would want to choose different types of pathing. And so, I'm not exactly sure. We'll let it help us think of an idea, but I do want to remind that we are just doing this to learn. If you are doing this for real, write these things by hand yourself. Use your brain. That's how you're going to get the best result. Garbage in means garbage out. So, just cuz this thing works, doesn't mean that this is well-designed. We're just going through this uh to learn these concepts, right? Okay?

**[00:40:59]** Um I'm not saying that this is the best.

**[00:41:02]** But anyway, we'll go ahead here and make a new folder. This one will be called dynamic selection.

**[00:41:08]** Okay, and I'm going to go ahead and make a new main.py file.

**[00:41:12]** And I'm going to go ahead and select this code.

**[00:41:18]** And we're going to copy this. And we'll paste this into here. And so, I need to give it a concrete example of what we're talking about for dynamic selection.

**[00:41:30]** I do not have my text here. I put it in there. I'm going to get uh ChatGPT to extract it out just how we did with the narrow narrow one. So, just ask it to you know, extract out the text for me here. I'm just doing this off-screen here cuz I need to give it a practical example and try to describe what we're doing here. We're going to CD back a couple and we'll open that up.

**[00:41:55]** And so, we'll go here and just say, you know, I want to implement dynamic dynamic selection for my uh uh coordinator.

**[00:42:12]** Um so that it's not running the entire pipeline, but trying to choose the best uh things to run based on use case.

**[00:42:27]** Here is an example of good dynamic selection where we have different pipelines.

**[00:42:38]** Okay. You can use to uh help you.

**[00:42:42]** Okay? And the other thing is like, edit the dynamic selection main.py file. Okay. So, it's going to go off and do that and uh we'll see what it comes back with. Hopefully, something that is useful. But, you know, if we don't kind of guide and say like, these are the use cases, you know, I'm I'd be surprised if it doesn't come back with anything good, but we will try here um just for learning purposes, okay?

**[00:43:10]** All right, it's come back with something. Let's take a look at what we have.

**[00:43:14]** Um so, dynamic coordinator. Oh, we still have that narrow coordinator in there.

**[00:43:19]** We should really remove that out of there because it probably is confusing.

**[00:43:21]** We now have like three coordinators. Um I don't want to have three.

**[00:43:28]** So, [snorts] we'll go here. I'm just going to tell like, look, I I only need a single coordinator prompt. So, uh we'll I'm being lazy here. If we don't need the other ones, we can just delete them out, right? We have this narrow one.

**[00:43:48]** So, we know this one is not something we want, so we'll take that out.

**[00:43:54]** Then audits the gaps if we're delegating specific domains.

**[00:44:00]** And then here we have the dynamic one.

**[00:44:01]** So, we'll take this one out. Okay. Look at that. We wasted no tokens.

**[00:44:05]** There's no reason we can't do that. We don't have to prompt everything. Then we'll go down here and take a look. So, this coordinator reads the roles, then decides which dimensions actually matter. So, routing the logic.

**[00:44:15]** So, strong technical match or whatever whatever. Let's take a look and see what we have.

**[00:44:21]** So, routing guidance. Adapt to what you observe. Don't apply mechanically. So, simple factual match. Skip keyword scan.

**[00:44:28]** Go to straight to this. Non-traditional background. Transfer skills. Oh, this is cool. I like this. Never invoke a screening agent unless it's answers a real question. So, I think that actually um worked out perfectly.

**[00:44:43]** That's a great example of of that. And so, we'll go ahead here and I'm just going to go and run it. So, we'll CD into dynamic selection.

**[00:44:53]** This has actually been quite fun. Um is it useful? I don't know. Depends on what you're building.

**[00:44:59]** And oh yeah, we don't have the narrow coordinator. So, we'll go here and just make sure narrow coordinator.

**[00:45:04]** Um I want to get rid of these other ones. I don't want to waste all that here.

**[00:45:09]** And so, uh I'm just going to go back a step and just say, uh this should be fine. Let's just do that.

**[00:45:19]** I didn't realize there's more to rip out.

**[00:45:22]** I think it'll still work though.

**[00:45:23]** This is all three coordinators. There's only one though, right? Because I ripped them out.

**[00:45:28]** So, here it says, "Describe the most complex screening angles delegated."

**[00:45:34]** Okay. And the only the only way to really know if this is different What happened here?

**[00:45:49]** Uh we have narrow QS. We still have some of that remaining remaining code there.

**[00:45:54]** So, it's just some of this stuff.

**[00:45:55]** And so, I'll go ahead and try that again.

**[00:45:59]** I'm not sure if that will work if it's just a single item, but I'm hoping that it does.

**[00:46:06]** Um but here, um you know, my best guess is that it's choosing exactly what it needs cuz if we go back up to here, that's what it looks like it's doing.

**[00:46:15]** Oh my goodness. So, I'm going to go back a directory here um cuz this is very frustrating.

**[00:46:27]** Uh remove the better I only have a single coordinator.

**[00:46:37]** But, I remove some of the other code uh because I only really need a single coordinator here.

**[00:46:46]** Can you fix fix the code? You know what's funny is that sometimes like I will type things and every single letter will be wrong and it still knows what I'm saying because it like it does the off-shift, which I think is really cool. As someone that's dyslexic, as long as it understands me, I I love that. Um Yeah, and so, I'm just asking it to clean it up. I just want to make sure that it's in a working state before we move on here.

**[00:47:12]** All right. So, it thinks it's cleaned it up. We'll go into here again.

**[00:47:15]** And we'll run this again. So, screening angles detected.

**[00:47:24]** What I'm trying to determine when it runs here is like, how is it selecting stuff? So, in your current role at the fintech, what is the scale of your system that you worked on?

**[00:47:33]** Your transmission from this. Have you designed or refactored it?

**[00:47:36]** So, what it looks like it's doing is it's actually uh generating out uh possible angles based on this information. And so, it's literally creating dynamic routing on the fly. So, it's not like, here is a list that we had before here, but literally like, here are things that you can check and then choose what you want to put in here. So, it's not always applying the same thing.

**[00:47:58]** And we'll go back up to here. It's still conditional maybe, but yeah, we're getting something that is it's again very interesting to see this play out.

**[00:48:08]** Um again, you know, we don't know if it's actually useful, but it's fun to see the system working.

**[00:48:13]** Um and there you go, okay? Let's take a look at partitioning research. So, if you give three research agents the same brief, you get three overlapping answers and wasted tokens.

**[00:48:26]** So, if you're trying to paralyze things, right and say, "Research CV market.

**[00:48:31]** Research CV market." And they're all doing the same thing, that's going to be nonsense, right? So, carve up the scope so each agent owns a distinct slice. And so, here we are seeing partition information where um we are creating structured data and we're providing detailed information like topic, cover, excluded, things like that and providing that information there. And as per usual, we can create a tool that would check and make sure that we're dividing the research scope into non-overlapping assignments before delegation. What's really interesting here is that it's making a structure.

**[00:49:03]** Um and I mean, you know, in the last thing that we did, technically it is already kind of assembling um its own way of doing stuff, but um I suppose what we could do is we could generate out into partitions um in this sense and make sure that it's even more detailed in terms of what it's covering as an intermediate step um to make sure that it's not doing the exact same thing. But, this one's more focused on very specific things that it's researching.

**[00:49:28]** Um but yeah, the question is like, does our current one, even if it's not the exact same one, is it having overlapping tasks? And that's what we don't know. And so maybe um putting a structured structure a structure with partitions might help.

**[00:49:40]** But we'll have to experiment, okay?

**[00:49:43]** Okay, so let's see if we can implement partitioning in here.

**[00:49:49]** So what I'm going to do is make a new folder here called research partitioning.

**[00:49:54]** Partitioning. And we'll go ahead and make ourselves another new main.py file. We're having lots of fun here. And so we'll grab this wasn't this one this is the last one we worked on, right?

**[00:50:06]** Going to grab this here. Copy it.

**[00:50:11]** And um go all the way down. And oh wait, no no no this one's empty.

**[00:50:17]** Here we go. Okay. So now we are back with our dynamic one. So here we have uh off screen here I just told it to extract it out.

**[00:50:26]** Right? And um I'm going to just say here like, you know, I want to make sure I want to make sure um my uh research what are they called?

**[00:50:41]** What did they call them here? My research agent agents aren't wasting credits uh tokens by having and time by having uh overlapping tasks.

**[00:51:01]** And so I would like to have another step where we have uh partitions.

**[00:51:09]** Um And I mean like the thing is like you could manually make this stuff, but I'd rather just generate it out so it makes it easier for us. So we have partitions uh uh have a step where we generate out partitions based on a JSON structure.

**[00:51:30]** And then we can determine if there is if they are truly not doing the same task.

**[00:51:42]** Make sure to print out the structure so the human can uh see it on the run of the coordinator agent.

**[00:51:52]** Update the research partitioning main.py and here is an example of partitioning uh from a different use case.

**[00:52:13]** Okay. And so I'm going to copy this over.

**[00:52:18]** Bring it on over here. Right? And I'm hoping that this will work.

**[00:52:25]** Right? But I mean like this could also could just be like a static way. Like if you were just statically building a research agent that this would be a means to which you could do it and you don't have to delegate so much out to the agent if you will. But then now we're kind of relying more on um code driven logic. But you can mix them by the way. We didn't We didn't mention that, but you can take a hybrid approach where some of it is the coordinator and some of it is code driven. There's nothing wrong with it. There's no rules here, folks.

**[00:52:54]** There's no 100% bad. It's what you want to do, right? Um and so we will see if it can come up with something here and then we will review that code, okay?

**[00:53:02]** Okay, let's take a look and see what it thinks it's doing here. So uh narrow We still got this language like narrow versus better. I probably should get that out of there.

**[00:53:16]** Mhm mhm mhm. I really should be taking this out so that uh it's not getting as complicated here. So screening agent prompt You are a specialist hiring analyst. You will be given specific screening uh questions about a candidate. Answer the questions two to three focus sentences. Be concrete and specific. So really changed it in this case.

**[00:53:41]** Um Oh no no, this is fine. This is still the same.

**[00:53:46]** Runs a specialized agent, calls once per screening, etc. etc.

**[00:53:49]** Um I don't want Oh, I do not want multiple agents. Look, I don't want more more than one coordinator.

**[00:54:00]** Uh we don't need the narrow coordinator, okay? And so it's just because we copied it and I had some of the code still lying around and that's what's Oh, no no no no no no no no no no no.

**[00:54:16]** I just realized I was editing the wrong file.

**[00:54:19]** >> [laughter] >> Okay. So I went back there and I'm going to make sure I didn't muck that one up.

**[00:54:23]** Uh yeah, I don't want to muck with this one.

**[00:54:29]** Oh now I don't know. Did I break it good?

**[00:54:36]** Um Mhm. I think I can just go ahead here and discard the changes. I think it'll be fine.

**[00:54:50]** Okay. And so we'll go over to here and this is the one we actually wanted.

**[00:54:53]** And so it still has that logic in here which is kind of a problem, but I will see if it actually is an issue.

**[00:54:59]** Cuz we only have one, right? And I'm just going to remove it. I just don't want it to get confused.

**[00:55:05]** And I don't want to explain any of that here. So I'm just going to take that out.

**[00:55:14]** So let's take a look here. Says for both coordinators. So spoke system prompts. I'm just going to take that out.

**[00:55:21]** It keeps talking about like Okay.

**[00:55:26]** And now let's take a look here. So you are a partitioning uh a screen partitioning planner given a job posting resume. Output a JSON array of non overlapping screen partitions. Each partition object must have an agent, a scope.

**[00:55:43]** Um rules design partitions so that together they cover all relevant hiring questions. No two partitions may share the same cover uh cover aspect. Only include partitions that are genuinely needed for this candidate. I feel like uh we lost uh information here.

**[00:55:59]** We have Oh this is the planner part. Okay, so this is actually a separate part. Okay, so that just generates the partition, all right? And then down below here we have um the actual dynamic coordinator. So you you're here invoke exactly one screen partition call per partition, no more or less. Formulate the questions for each cell. Do not invent additional screening angles beyond the partitions provided.

**[00:56:25]** They were designed to cover all relevant dimensions without overlap. And so I mean like that's another way where it's just specifying it in a different way, but I guess it's generating out the partitions.

**[00:56:38]** So in the other one we literally listed out possible things and here it's generating them out. Oh here it is.

**[00:56:44]** Um Mhm. Is this good? Because before we had a list, right? So if we go back over to our um we'll just put this for a second.

**[00:56:57]** And we go back to our dynamic selection here.

**[00:57:01]** Right? And so here we had this, but we lost our routing guidance.

**[00:57:11]** So this is what I'm going to ask.

**[00:57:14]** I'm going to resume the last conversation we had.

**[00:57:19]** Going to make this a bit larger here.

**[00:57:22]** No. So does it We don't have it anymore, unfortunately. Or maybe I ran into a subfolder and that's my problem. So I'm going to go here and ask it like We have uh we have a dynamic What is it that we have? We have a uh research partition so that we don't have uh overlapping researchers doing the same thing.

**[00:57:58]** Did we lose uh selective routing based on task? Uh and do we need to bring that back in while preserving our partitioning?

**[00:58:20]** Okay. And so I'm going to go point to dynamic selection has the original prompt that had routing.

**[00:58:33]** And then here we have research partitioning is our um new prompt with partitioning.

**[00:58:45]** But the routing was removed. And so how would it know to do routing?

**[00:58:57]** Like do like how would it know to choose the appropriate dynamic selection?

**[00:59:06]** Okay. And so that's where I think there's a bit of an issue.

**[00:59:12]** Okay? Because sure, like we now it will generate out that structure and things, but how does it know to drive what to generate?

**[00:59:22]** Cuz it doesn't say that, right?

**[00:59:24]** And so dynamic both selects the angles, matters, and delegates. It has routing that skips the scan and strong matches.

**[00:59:31]** Now owns the selection step, but it has no routing rules. It just generates non-overlapping partitions without guidance which on which one will skip.

**[00:59:40]** And so here Okay. I'm just going to hit tab here.

**[00:59:55]** Okay, you are moving it back in, but are you thinking about how it will work or you're just dumping it back in?

**[01:00:06]** Okay? Because I could have done that.

**[01:00:13]** That doesn't mean that's a smart approach.

**[01:00:17]** And maybe that's all we need to do.

**[01:00:19]** But let's take a look and see what it comes up with.

**[01:00:23]** I'm telling you these things aren't smart, folks. You've got to think for it. So here we go. Fair point.

**[01:00:29]** Let me think about it. So we have partitioning that sees the resume and then the dynamic coordinator which sees the partitions. Where does the routing actually live now? So dynamic selection the coordinator was doing two of one things, deciding what to check and calling agents. Uh and the research partitioning now splits routing partition planner planner's job and then the coordinator's job. So the routing rules do belong to the partitioning planner, but they need to be reframed. In the original one it says never invoke the rules unless here we should say only create partition if the rules govern partition creation.

**[01:00:59]** The coordinator in the new architecture should stay as is. It's correct to be dumb selection because the decision was already made upstream.

**[01:01:07]** Uh giving it routing logic again would create a conflict of two places fighting over what gets evaluated. Um the partition planner currently says only include the partition genuinely needed.

**[01:01:18]** That's vague. Adding a specific heuristic routing. I mean like I would have thought and you might agree with me is that in the dynamic coordinator we had that list.

**[01:01:31]** Uh but the thing is is like it was saying like okay, if you do this then then do this or do that, but maybe the the problem was is that when we looked at the EV research, it literally had pipelines where in this dynamic router it just had things that you could choose from that you might want to consider.

**[01:01:45]** Okay, but it wouldn't run them all.

**[01:01:48]** So here it says we receive a set of pre-planning partitions as JSON.

**[01:01:52]** Invoke exactly one screening agent.

**[01:01:55]** Uh-huh. Okay, well let's just see what we get.

**[01:02:02]** Okay. I'm not sure if I like it, but we're trying here, right?

**[01:02:11]** And we'll go main.py and we'll run it.

**[01:02:13]** And see what happens. So we have we have core stack proficiency.

**[01:02:24]** Assess REST API capabilities. Okay, so we have here um core stack proficiency. Evaluate mastery of required technologies directly matching the job stack.

**[01:02:42]** Uh-huh. Access REST API design capabilities.

**[01:02:49]** Evaluate exposure to scaling patterns and nice-to-have technologies. Confirm senior-level experience.

**[01:02:56]** And then here we have screening angles delegated. Does the candidate demonstrate mastery of required stuff?

**[01:03:05]** Uh okay. And here we're getting partials. So we have a maybe recommendation. Alex is qualified to mid to senior.

**[01:03:17]** And we have different coverage. So I still don't know this is better. I mean like we should be dumping all these logs out and then comparing them and then and doing stuff. So obviously we were just trying to meet the requirements of learning this stuff and kind of having a sense of it, but is it good? Is it is another question that will take more time and I'm going to keep repeating that because I just want you to know just cuz we're doing it doesn't mean it's great.

**[01:03:42]** And you should be thinking about like okay, if I had these three four different ways um you know, determine usage, determine outcomes, have your examples. Don't have them for you here.

**[01:03:51]** That'd be a lot of work for me to set up for you. Um but uh yeah, it's interesting trying to try out these techniques and apply them, okay?

**[01:03:59]** Let's take a look at a refinement loop.

**[01:04:01]** So the idea right now is that um everything's been one shot. The idea is it goes through it, it produces an evaluation and then then it's over. But what if we could feed it back in the loop and refine it until we are happy with it and that's the idea behind a refinement loop to make our research system really really good.

**[01:04:18]** Um so if you look at this prompt here for our coordinator the idea here is that we are telling it that we can have up to maximum four refinement iterations and that we are going to delegate the information back into here. And so you'll notice here we have like an evaluation coverage and when to submit final uh and uh uh creating the synthesis and things like that. And so we will go ahead and try to apply refinement loop to our um our agent, okay?

**[01:04:49]** Hey folks, this is Andrew. In this video we're going to implement our own refinement loop. Uh so what we'll do as per usual, I'm going to go ahead and make a new folder. This will be my refinement loop.

**[01:05:01]** Okay. And then what we're going to do is we're going to go ahead. Let's just grab our code here, main.py. We're going to go grab our last one which was research partitioning.

**[01:05:12]** Cuz we're building off of it every single time trying to make this thing a little bit better. And we are going to implement the refinement loop. I need to extract the text out because again I I don't have it on on hand, but let me go grab it from that slide, okay?

**[01:05:28]** There we go. I grabbed it. And if you want to grab it, too, all you got to do is take a screenshot, feed it to Claude or ChatGPT and extract it out, folks. Um because you can. You can. Make sure you do that, okay? It's not hard. Just build up those skills, okay?

**[01:05:44]** So I'm going to go ahead here and just CD out here. We're going to go into our Claude. And um you know, I need to implement a refinement loop um uh in my agent for research partitioning main. Here is uh a example from another use case you can use as inspiration.

**[01:06:15]** As guidance. Okay. And so I'm going to paste that in there. And so the idea though is that with that information I'm hoping that it can develop that refinement loop in here. So we will see what it produces, okay?

**[01:06:32]** All right. So in here we have um changes. Let's take a look and well it's still trying to edit stuff. So yes.

**[01:06:38]** Um and let's see uh what we have. Okay, so it is bringing in um evaluate coverage. Okay, so we have that.

**[01:06:53]** Uh submit final. So it's setting different states based on whether you know, higher maybe or pass. Only call this when the evaluation confirms uh sufficient coverage.

**[01:07:02]** And final recommendation. So we have that in our loop.

**[01:07:06]** Here it is adding the evaluation agent, okay?

**[01:07:10]** And we have some tweaks here. So we have initial screening. Invoke exactly one screening agent call per partition.

**[01:07:15]** Formulate each question. That's fine.

**[01:07:20]** Phase two, evaluate coverage. After all initial partitions agents have reported call evaluation coverage with plain text.

**[01:07:27]** And here we have refinement max three iterations. If the evaluation coverage returns sufficient false invoke screening agents to fill only identified gaps.

**[01:07:36]** Uh call submit final etc. etc. Do not call the submit final before evaluation uh if it's only once, okay? So here is obviously done a lot. I'm kind of curious to think like maybe it's just like you're brute forcing to make it either that you really want this person or you really don't want this person.

**[01:07:51]** It'd be interesting to have a larger data set like let's say 100 applicants and you ran it through and to see if it just skewed it to one location or or one side or not. Um but it'd be very interesting to find out, but we'll go back up to here and so we can see the changes.

**[01:08:07]** And let's go and run this thing.

**[01:08:11]** Notice as we are progressing it's becoming easier and easier for us to update our agent. And so far we've been just using the Anthropic um SDK not using the agent SDK. The agent SDK is awesome, but uh we will just continue on here. It'd be interesting to convert it over and see what the code looks like and we'll probably do that. Um but let's go ahead and do python main.py and we'll go ahead and run that. And the idea it's going to run it says dynamic coordinator.

**[01:08:39]** Obviously it's the refinement one. We don't change those names. And so here reads candidates first, routes to the relevant checks only. So evaluate depth.

**[01:08:46]** Access to database caching. Verify API.

**[01:08:50]** Confirm senior-level experience.

**[01:08:53]** And is the candidate senior level? Okay, great. So now we're going into iteration one.

**[01:09:00]** Okay. So we have coverage score, code quality practices, no evidence etc. etc. And so it is going again here.

**[01:09:09]** Asking questions. They are I think they are different questions.

**[01:09:18]** It's hard to be because we have the this up here, right? And then down below Oh look, the the coverage score is going down now. Interesting.

**[01:09:26]** And so we are done and over with.

**[01:09:31]** We'll go and uh look up here. So did two iterations.

**[01:09:37]** And their score went down. So yeah, that's iteration loop. Is that good? I don't know. It takes a lot of work to evaluate this stuff. We would spend hours hours upon hours tweaking this to figure out is this valuable information? Is our data set good? Etc.

**[01:09:56]** etc. There's no magic here, folks. We can uh code these out very quickly, but to make sure they actually work good is a different story. I'm going to keep repeating that because it's true. Uh but that is what the refinement look uh refinement loop looks like, okay?

**[01:10:11]** Okay, folks. Let's take take a look at observability. So the idea of having this centralized coordinator is the fact that everything's going to pass through it, okay? So no matter who has to talk to who, it's going to pass that coordinator. And because of that, um the coordinator is at a choke point where it can observe um anything and catch any kind of errors because it is coordinating stuff. But when you uh do not have that, then everyone is just communicating with each other and you can't observe what was said. You can't catch errors consistently. You can't control what information crosses boundaries. But the coordinator can do all those things. And so we are using the coordinator pattern.

**[01:10:49]** Um do we have observability? That's a good question. So I would say let's go back to our thing and see uh if it is working. I would probably ask like, "Hey, can it actually wrote to other ones and is it capturing information?"

**[01:11:00]** Um I know it already probably is working this way, but let's confirm and go back to our code, okay?

**[01:11:07]** Hey folks, we are back and I'm going to make a new folder and this will be uh coordinator observability.

**[01:11:13]** Because the idea here is that our coordinator should act as an observable layer. And so I want to make sure that it actually is doing that. So let's go back here.

**[01:11:26]** And we'll uh uh go into um Well, we'll type cloud here, right? And we already have the refinement loop over here. So I'm going to go ahead and grab all this code.

**[01:11:35]** Okay, I'm going to grab all this code and we'll make a new file called main.py. You're starting to get the pattern here what we're doing, right?

**[01:11:44]** Very repetitive, but it really is good in iteration. So um what I want to figure out is do we actually have those values? Is the coordinator acting like a coordinator? So um I'm just thinking about this for a second. So what we want to do, so we're going to say uh I have an agent uh a coordinator agent uh here. So we'll say uh coordinator observability.

**[01:12:15]** Here, I'm going to put this in a plan mode. Here are the questions I have. Is my coordinator operating from observability level?

**[01:12:26]** Observability and um uh I'm trying to think of what like and controlling controlling flow of information.

**[01:12:40]** Uh you know, is it uh managing, you know, like is it I'm trying to think like here. I have a coordinator agent, right?

**[01:12:49]** Here are the questions I have. Is my coordinator operating operating from uh uh operating with an observability layer?

**[01:12:57]** So we can capture uh any errors.

**[01:13:05]** All messages that that that are being uh sent to our spokes.

**[01:13:09]** Sub agents. Is it controlling context in what is passed uh to my um uh spokes and only those sub agents can talk to the coordinator.

**[01:13:34]** Right? Is there something I am missing to make my coordinator a good coordinate coordinator, right?

**[01:13:53]** That's what we want to know. And we'll go ahead and hit plan there. You're thinking, "Well, you know, you're just writing whatever out." But that's that's a fine problem. You can't make perfect prompts here, folks.

**[01:14:02]** I mean, you can make better prompts yourself and spend time engineering them, but this is good enough to start getting some information. So let's see what it comes back with. And I'd be curious to uh layer something here uh there. So I'm just curious what we can do um to make our observability better.

**[01:14:18]** Um but we will wait for that generation, okay?

**[01:14:23]** Okay, so let's take a look and see what it thinks.

**[01:14:28]** Um So we'll go all the way to the top here. So the user's coordinator uses a partition-based hub-spoke pattern for job screening. They want to know, does it have proper observability? Does it capture all messages to spoke? Does it control context passed to spokes? Is Is the spoke-coordinator communication isolated? What is missing to be a good coordinator? So it says observability is weak. I absolutely agree. We haven't done anything for it. Um Could we do something better than just Oh, yes, it's only print statements. I agree with that. Um uh error handling anywhere it says JSON loads. Yeah, that makes sense. API level tracing. No token counts. No latency. No request IDs. Yeah, token counts would be really useful.

**[01:15:05]** Uh no persistent audit trail of all output and ephemeral stdout. We have message capture partial. So delegate list. We are printing some stuff, right?

**[01:15:13]** Cuz I told it to do that, but um Tracks questions sent to spokes. Spokes responses are never stored. They go straight into the tool results and are lost out of the coordinator. No record of partition each question uh uh addressed X. No log of coordinator's own reasoning text between tool calls. Mhm.

**[01:15:31]** Every spoke receives the full job posting.

**[01:15:37]** And so it's saying context control loose. Resume regardless of its partition.

**[01:15:42]** I mean, it would need it anyway, right?

**[01:15:43]** Like all of them need it. So we're not really giving them separate data.

**[01:15:46]** Uh regardless of its partition scope.

**[01:15:48]** So cover exclude is only advisory passed by JSON to the coordinator prompt, but not enforced at the spoke level.

**[01:15:58]** Uh the coordinator uh could ask any question. No mechanism validates the question stays within the uh assigned partition.

**[01:16:07]** Fair enough. Spoke isolation one direction one directional enforce. So spokes are stateless functions called by the coordinator. No cross no cross spoke communication. So that's good. But spokes have no awareness of their assigned partitions. They can't reject out of scope questions. Oh, that's actually a good good point. No uh only these spokes can talk to coordinator mechanism is just a single plane one. So where are gaps? Can't debug or audit the run. Silent crashes on failures. Can't replay or inspect what's wrong. Coordinator doesn't know if all dimensions are covered mid run.

**[01:16:40]** Recommendation may be issued before all uh angles are addressed. Spokes are all data even if relevant. All partitions even if some obviously irrelevant. A single pass cannot fill gaps during it.

**[01:16:51]** And also our data like if I'm really if we maybe want to make this better, we would be sending like different payloads of different information to specific research agents. But right now everyone's getting the same job posting.

**[01:17:02]** Um So here they have recommend fixes so structured logging with timestamp levels.

**[01:17:08]** That seems good. Uh that's fine, sure.

**[01:17:09]** And it's going to log that out. Error handling. So wrap the JSON load.

**[01:17:14]** Generate the partition. Uh persist spoke inputs outputs so extend beyond the tracking.

**[01:17:20]** Add coverage evaluation tool at at explicit gates.

**[01:17:24]** Force the coordinator to call submit final.

**[01:17:27]** And so these are fine. Um The only challenge here is I don't I feel like there's a lot of tasks here. So I'm just going to go here and say, "There is a lot of am concerned uh you will uh not be able to remember all the tasks.

**[01:17:49]** Can you create this uh plan in a readme with a task checklist?

**[01:17:57]** And can you check off the tasks as you complete them?"

**[01:18:04]** Okay. And so the goal there is to help it out a bit. Um that's not exactly spec-driven development, but the only thing is like if we really wanted this to drive and be really good, we would want something that would clear context each time. But we're not set up that way. I'm not here to roll a a small spec-driven development little thing for us here. So that's totally fine.

**[01:18:26]** And um readme with tasks and checklist.

**[01:18:31]** As long as it knows what it's doing that, that's fine. But where's it going to put that file?

**[01:18:36]** Yeah, I'm just going to trust that it can do it.

**[01:18:39]** Let's go ahead and let her rip.

**[01:18:40]** Okay? Um and so the idea again here is to improve observability and we will uh see how that goes. Another thing is like I would imagine that if you were to put this into production, you want to productionize it, you might want to contain these sub agents into containers. And then you might want to use Otel as another observability layer.

**[01:19:01]** That's how I'm kind of thinking about it.

**[01:19:04]** But we're keeping it all monolith for now and we're not going to overly complicate it at this stage. Um and I'm going to let it go and burn away all my credits. Look at that. 6.2 thousand credits. Wow. Let's go over here. It's like the worst time to do this. People are like there's a on Twitter they're like, "Oh, it's down." And the usages are gone and stuff like that. It's me.

**[01:19:24]** It's me. I'm the I'm the problem.

**[01:19:26]** So go over here and right off the bat like we are Oh, resets in 9 minutes though, that's really good. But we're only 33% Well, let's burn, burn, burn, baby. Though my week is is is getting up to use very quickly there. Um but anyway, Oh, yeah, it's it's going up. So, yeah, we're going to consume tokens like it's nobody's business.

**[01:19:51]** Um but I think it'll be worth it for this stage of the thing as we are continually refining it, okay?

**[01:19:57]** Uh that was fast. I feel like it should have taken longer than that. All six fixed fixes are implemented. I mean, I would rather have been more granular and clearing contacts between it so that we would have um you know, better stuff. Well, that's fine. So, is my coordinator operating with observability? No, it had only print statements, etc., etc. What was I missing? Error handling, mid-run gap detection, no exit gate. And I'm not even saying like this is the best, but um you know, it's pretty good for us throwing things here together. Let's see if we can see what I mean, it probably will just tell us what code changes were made.

**[01:20:30]** I suppose that's the easiest way to check.

**[01:20:33]** And um I'm just going to go all the way up here. Let's take a look here. So, we've added logging, okay?

**[01:20:39]** And we are implementing the logger.

**[01:20:43]** Here, it says scope to each partition.

**[01:20:46]** Partition agent name uh is the names the question belongs to from the partition JSON. Okay, so it's being very particular to make sure that it's scoped. That's good. Evaluate coverage.

**[01:20:57]** So, mid-run gap detection tool. Evaluate whether the screening finds are efficient to make a confident recommendation.

**[01:21:04]** Um confident that all partitions agents have reported. Return a coverage score, etc., etc.

**[01:21:11]** Okay, submit final explicit exit gate.

**[01:21:13]** Submit the final hiring recommendation only this Call this only after evaluate coverage.

**[01:21:20]** Fair enough. So, go down below here.

**[01:21:24]** Mhm. Fix error handling. So, here we have uh Here's down the error handling down here below. Fair enough. That's very basic.

**[01:21:37]** That's not really that important.

**[01:21:39]** And then we have the screening agent.

**[01:21:42]** So, we are seeing Oh, to scope it in the boundary, right?

**[01:21:50]** So, making sure that it's scoped.

**[01:21:52]** Fair enough. Here we have rule changes.

**[01:21:57]** And so, it's about passing that information and it's talking about that evaluation coverage in the final recommendation.

**[01:22:04]** Okay. And then we got logs, logs.

**[01:22:08]** And more logic. Now, this thing is pretty wild. I would probably want to take it farther and refactor it, but I don't really want to uh Like this is just this is a mess. Like this is not how you should have your code base. But I don't want to go overboard at this stage. I just want to make sure that this works.

**[01:22:36]** Okay, so what we're going to do cuz I'm expecting logging to appear, right?

**[01:22:39]** Um And so, I would probably say like we could just run it.

**[01:22:46]** But the other challenge would be like we need actual ways to test that the stuff works. So, probably what would have been better but it would have taken a lot like this would have took an hour or two and you folks don't want to wait around that long to test that. But what I would have done if we had the time and you wanted to go through it, what I would do is I would stage examples and and and I would want to see if like we could pollute um pollute the context between agents and make sure that it is only receiving proper questions and it rejects it and those would be things that we test for.

**[01:23:20]** So, we really are skipping a lot of that stuff and that's stuff that you would still have to do. But just because I'm not doing it here doesn't mean that I wouldn't do it. Um it's just I'm not doing it because you folks don't like when I make like two, three-hour videos.

**[01:23:33]** Um even though that's the actual effort for the work and I can't really just you know, fake that along, right? So, we'll go ahead and we'll run that. I think it's spelled observability wrong, which is fine. And so, what I'm interested in is do we get any logging?

**[01:23:46]** Where is our logging? I don't see it.

**[01:23:48]** Okay. I mean, it's just going to ST out. So, it's not logging to anywhere in particular.

**[01:23:57]** Which is fine. Uh so, I you know, I'd probably just have it log to like into in a log directory and that's the only thing that might be missing here.

**[01:24:11]** Okay. And I'm just going to wait for it to run Oh, there we go. There it's done.

**[01:24:24]** And so, we have our final information.

**[01:24:26]** Did it call that final evaluation step?

**[01:24:27]** Yeah, final recommendation. There it is.

**[01:24:32]** So, there you go. That's all it took to improve it.

**[01:24:36]** Definitely better than what we had before.

**[01:24:39]** Um but yeah, I would probably want to refactor this so that's like you shouldn't have one big dumb file like this. Um and so, we might do that in a separate video. Especially if we want to convert it over to the agent SDK to compare. That might be something we might want to do, okay? Um but yeah, now we've added observability.

**[01:24:57]** Hey folks, it's Andrew and in this video, what I want to do is I want to refactor our coordinator that we've been working on up to this point as I'm going to want to port it over maybe to agent SDK to just take a look and see what that looks like. And so, we're just going to say um uh coordinator refactor here.

**[01:25:15]** And I'm going to go ahead and grab the code here.

**[01:25:19]** And we are going to ask it to refactor.

**[01:25:23]** Um and let's just see if we can make this a little bit more maintainable, okay? If you are not a programmer, you might not know that this is not good code.

**[01:25:33]** Okay? And it like it works for this point that we've been able to hold this all into memory, but if we came back later, we wouldn't be able to really make sense of it. And just because the agent can make sense of it and summarize it to it, that's not good enough. We need to make it so that it is more human-readable um and that is what we are going to do.

**[01:25:51]** So, I'm just going to CD out of here and we're going to go into Claude. And uh we are going to get some refactoring going on. So, what I'm going to do is I'm going to make a new file called refactor.

**[01:26:04]** Um refactor MD. And I'm going to go say refactor um tasks.

**[01:26:13]** So, this is this document um is the tasks I want completed to refactor uh this uh our coordinator agent.

**[01:26:28]** Uh currently, all code sits in the main.py and we need to uh break it into multiple files.

**[01:26:39]** Okay? So, uh let's go ahead and start making some tasks. I'm just going to make my observations of what I don't like. So, the first thing is um the prompt. So, all prompts should be uh stored as um All prompts should be stored All prompts should be stored as markdown files in a prompts directory.

**[01:27:14]** Okay? So, that's step number one. The other thing is like tools. See how tools is very uh wieldy? So, uh tools should be uh individually defined as their own files in the tools directory.

**[01:27:32]** We should have .py files for each actual tool code.

**[01:27:39]** And the um tools. The tools I mean, like can we this is JSON, right?

**[01:27:47]** Um can we? I don't think there's anything special about this and the um tools.json for the long tool.

**[01:27:58]** Right? I I think it will understand what that is for the uh gets passed to create. So, that is definitely something I would like fixed.

**[01:28:12]** What else? What else? Um Do your partitions.

**[01:28:18]** We do have the partition system.

**[01:28:22]** So, say partition uh generation should be in lib as its own file. That's something else I would do.

**[01:28:36]** Um that's a function that is that. Run coordinator.

**[01:28:42]** Um The logging is inconsistent. I don't like how the logging is. So, um we should have a logger that um refactors all the logs to be consistent in a file in a file called logger in our logger.py in our uh lib directory.

**[01:29:11]** That'd be another thing I would want.

**[01:29:13]** Um Yeah, so I think that's a start.

**[01:29:20]** And so I'm going to go ahead and just say uh coordinator I want you to refactor my code base on that markdown file's tasks for the main.py in the coordinator refactor, okay? And so we will let it go do that and we'll see if we can really reduce and organize that code base cuz it really should be really easy for us to read. Right? Like I know we can make sense of it because we've been carrying forward it, but we really need to be at 100% like yes, absolutely, I know what I'm looking at, okay?

**[01:30:05]** Um So I'm just going to accept everything that goes along here and then we will take a look and see what we have. So it's already off to the races. We have our prompt, our partition planner, our screening uh agent.md. For me like I would probably want these to be templates that you can inject stuff into, but there's no reason for that right now. We don't really need dynamic injection, but it's definitely something that would be uh interesting to do. We have our tools directory. I think we only have the one agent here and then we have our tools JSON, so that is uh working out pretty well so far. It's going pretty quick, too. Man, these things are getting really, really better. Here we have our logger and then we are going to have our partitions.py.

**[01:30:44]** I really don't like that we have constants. I do not like using constants whatsoever. I think they're just it's just bad, bad code. Um but we'll continue on here and uh check it out in a moment. I'm going to just check how my usage is going.

**[01:30:57]** And uh you doesn't matter, it just reset. I'm back at 2%. Look at that.

**[01:31:01]** Lucky me, eh? Okay. So we are just chilling out here waiting for this to generate.

**[01:31:08]** I'm going to pause here and we will come back in a moment.

**[01:31:13]** I think it might be done. I didn't even really wait that long. And so we'll go up here and take a look.

**[01:31:18]** And so we have our main.py, we have our prompts, we have our tools, we have our libs. Let's go take a look here and see if this is reduced enough.

**[01:31:27]** Okay, and I probably should have told it to check box off these.

**[01:31:33]** Uh which is fine. So I'll just go here and just check them off myself.

**[01:31:39]** I just didn't feel like telling it to do that. I don't know.

**[01:31:42]** I assumed it would be fine. I could also ask it like hey, is there anything else that we could do to refactor to make it more human readable?

**[01:31:50]** But I don't feel like it would know cuz it's not a human.

**[01:31:54]** And then it's trained on garbage repos.

**[01:31:58]** Okay, so let's go into our main, wherever that is. Hold on here, our main.

**[01:32:04]** And I I usually just have a sense of like is this readable, right? Um and it's still yuck. It's really, really long.

**[01:32:17]** So there's still some stuff in here that needs to be refactored. We'll go over to here.

**[01:32:25]** Um So say coverage report. Coverage report should be its own file in lib called coverage report.

**[01:32:43]** Okay. Um The other thing is like the data, so right now we have hard-coded data.

**[01:32:58]** Make a data folder and store data artifacts and load them into the app.

**[01:33:12]** Okay. That's another thing. Um Mhm.

**[01:33:27]** I really dislike the logging. Yeah, and we have the trace append.

**[01:33:40]** It's still very, very verbose. And there are still things that's like I'm noticing here like um There are There are templates for content for messages that should really be uh templated uh files that take variables.

**[01:34:11]** And load it in. Maybe um Okay, like is that a prompt? I mean like we have this, it's technically a prompt.

**[01:34:27]** So technically technically they are prompts.

**[01:34:30]** Our prompts for content. And so uh prompts So move them.

**[01:34:40]** Them to prompts folders. Okay. So there's that. There's a lot of those.

**[01:34:49]** Okay, and so we'll go back here, we'll save the file.

**[01:34:51]** Um all the way down to here. There are new tasks in the refactor.

**[01:34:57]** md, okay? And so we're going to have it go off and do those tasks.

**[01:35:09]** And so we'll give it a moment there. I'm going to pause and I mean I really should tell it to check them off. I didn't tell it to do that. Uh but we'll come back and take a look and then we'll ask it to do a general refactor. I'm still like I really don't like this.

**[01:35:29]** Like we see how we have like double lines and stuff like that. I don't need that kind of level logging. Um but I would have to explain to it um why that's an issue.

**[01:35:37]** Yeah, it's still just making them md files. It's not marking them whether they're templates or not, but we'll just treat them as templates.

**[01:35:44]** And here we're getting a lot more in here, so that's better.

**[01:35:47]** But I I just know what good code looks like and I I know that's not good code.

**[01:35:52]** Um but there's only so much you can do with Python.

**[01:35:55]** Certain languages have um the ability to have better readability like Ruby's really, really good at that.

**[01:36:00]** I'd love to port this over to Ruby. I just didn't check if the agent SDK is available. I don't think it is available in Ruby. I just think that the Anthropic one is and so if the agent SDK was in Ruby, I would absolutely be using it over uh the Python one as I really do not like Python code and um it do it just you just can't get it to be extremely human readable. Um unfortunately we are all kind of using it because of the way the industry is.

**[01:36:22]** Um as they've adopted it, not because it's good, just because of mass adoption in the uh data data science and stuff like that.

**[01:36:30]** So it just became de facto. Oh look, it's already done. And so we have uh that there and so we will again look at the main file. I'm just going to close it and reopen it. Sometimes it doesn't always show me right away.

**[01:36:42]** It didn't check box these off. I really should tell it to check box them off when it does that. So we'll go ahead and save that. We'll go back over to our main.py and we'll scroll up. And I get I'm looking that looking at this for uh for refactorability.

**[01:36:56]** And I would say like they haven't done a good job with logging, so I'd say you haven't done a good job refactoring the logging, right? So for example we have log log info partition like partition uh you should be making helper functions.

**[01:37:23]** Uh so these logs e.g. like log partition.

**[01:37:30]** Um or you know, like log right? Log warn and they will add uh the you know tags. The uh other thing is um you have superfluous logging that is great for human readability.

**[01:38:02]** But we want to focus on logging good for for uh logs. And uh we should be outputting logs to a log folder relative to the uh folder of this agent.

**[01:38:22]** Okay, and so that you know, that's one thing that's really bothering me.

**[01:38:25]** I really hate constants, so that'll be another thing that we fix here in just a moment.

**[01:38:33]** But again, we're just trying to get this to be in shape. Um Did it also move this out of here? Like what's this big thing? Like why is the tool used so large here?

**[01:38:44]** Okay. Um And while that is thinking, let's go review our other parts of code.

**[01:38:52]** Okay, I mean this is fine. I think I wouldn't mind if we had like this is a big JSON object, but I wouldn't mind if we had a shorter syntax for this. I don't want to do that right now because it's totally possible that um uh we will be able to do that in agent SDK where it probably already has like a shorthand to make that code smaller. And so I don't want to uh uh muck with that.

**[01:39:22]** And we'll look at the partition here.

**[01:39:25]** Really hate those those constants.

**[01:39:27]** And also I I really dislike how it's loading in the prompt template. So there should be a way to uh manage that.

**[01:39:35]** Look look at all this logger logic. Oh, no, that's the logger file.

**[01:39:39]** Yeah, here now we're starting to get those things that I that I was asking for. That's good.

**[01:39:43]** Um Okay. The other thing that that's And I mean we don't need to do this, but like technically, you know, we have all these subagents that are calling create. We could technically delegate them out to different models if we needed to.

**[01:40:01]** Um or we could even say like, "Hey, can you try to choose the best model as it's working through there?" But yeah, I guess the next thing on my task is to fix that um Like I'm not updating the refactor. We could keep updating that as a means to keep uh keep track of stuff, but I just don't care.

**[01:40:16]** Um And so Yeah, I want to fix those constants.

**[01:40:20]** And I want to get something that loads in the templates.

**[01:40:24]** I'm just going to take a look here at our usage.

**[01:40:28]** 9% doing okay over here. Okay. And so now that is uh fixed up.

**[01:40:35]** We'll take a look here. Again, I'm looking at my main seeing if it's shorter.

**[01:40:41]** Yeah, it's looking Yeah, this is way less messier.

**[01:40:45]** Um I don't like using constants.

**[01:40:48]** EG like this is a var. Please don't use these in the folder for the coordinator refactor. Fix the code.

**[01:41:05]** Okay, so that's something I really dislike.

**[01:41:09]** And so we will get that improvement there.

**[01:41:14]** This This to me is like there's a big issue with the loop. So I feel that we need to give it a better instructions on like how to better refactor the loop. I mean it's using just a big if self block. There might be some kind of uh state flow machine or something that could improve that loop. Um as I'm not happy about it. Before we do that, I want you to fix the template reading and loading of files.

**[01:41:37]** Um And so there it's just making basic changes for names.

**[01:41:44]** Right there. So those are getting changed. Good.

**[01:41:47]** And it'll be done here in probably just a moment. Yeah, it's just updating the main.py and then we will have those fixed. Come on. Come on.

**[01:41:56]** Hurry up. Hurry up. And also like loading these templates and populating them probably needs to be um its own thing. Yeah, great. Thanks.

**[01:42:13]** Okay. Another thing is uh loading loading files and templates where you uh inject variables.

**[01:42:22]** Um you can make a new uh uh uh template template um template file in the uh lib directory.

**[01:42:37]** And this should uh refactor having you know, large load code EG like this. Okay. And so that's another thing that's kind of bothering me. So we will get that cleaned up as well.

**[01:42:58]** Um There's other things like this. Like see how this is like something's happening here. So that should be refactored out into a function.

**[01:43:08]** Uh like everything here. Like just the units of code is is just not explainable.

**[01:43:13]** So the run coordinator definitely needs to be broken up into tons of functions.

**[01:43:18]** Every single of these if else blocks should be functions.

**[01:43:21]** Um And I would probably prefer stateless classes. I really prefer stateless classes as that makes it really easy to track inputs and outputs of stuff. Um And Python's pretty good for that because of the way it defines uh these label tags. I can't remember what they're called. The prop named properties.

**[01:43:40]** And so that will be good. I'm making a lot of changes here. So there's a high chance this might not work, but that's fine.

**[01:43:46]** Uh we can always work through that.

**[01:43:47]** Uh it's fine. You're fine, Claude.

**[01:43:49]** You're fine. >> [laughter] >> Okay. And so now that that's loaded. I'm not sure if uh that actually changed.

**[01:43:55]** We'll go back over to here. And so with that, now when it needs it, I feel Yeah, like load prompt exactly like this.

**[01:44:03]** Um So yeah, the big problem still is the run coordinator.

**[01:44:07]** So the run coordinator file is giant.

**[01:44:14]** Uh we should refactor um into a stateless uh uh a stateless function.

**[01:44:27]** And all the parts of code uh should be chunked into functions.

**[01:44:39]** So the functions basically act as documentation.

**[01:44:44]** You know, for example, the contents of if if uh if blocks are really uh should be uh function calls, right?

**[01:44:54]** We'll go ahead and we'll see if it understands what I'm trying to say. But like when you write good code, you know, like this would be a function.

**[01:45:01]** This would be a function. This would be a function. Um whatever this is.

**[01:45:09]** Right? These if blocks. And we'll see if it understands what I'm talking about.

**[01:45:14]** Um But I feel like that's a really important component. In fact, this run coordinator could also be in the lib directory. Um and we might suggest it to move that in a moment. But right now I want to see if it could even handle what I'm asking it to do. It might not understand. Uh cuz if I don't have like an example, it's just not going to know what I'm trying to ask for. Again, checking my coverage here. Uh we're at 11% usage. Some folks were suggesting that like when it's high peak usage, it depends on like if you overlap with Europe European time. I'm not uh obviously in Europe. And so um they said like just try a bit later when everyone's sleeping. And it's way later.

**[01:45:52]** So uh you know, it would be maybe um off-peak usage time. But anyway, we'll just wait here and see what happens.

**[01:45:59]** Okay? It's back with functions. And again, we could call plan to ask it to do this before, but I I don't really care that much. So we have plan partitions, validate index partitions, run. I've seen something like with partition information. I'm almost wondering if that should be really part of the partitions.py.

**[01:46:15]** Right? Um log coordinator reasoning, handle this information. And so those partition ones, there's three with partition ones.

**[01:46:25]** Right? And so we'll go over to here.

**[01:46:28]** Um I mean like sure, you could do it that way. That's not what I asked for. I need to verify this. So I got to go over here. Like what does a stateless class look like in Python? Can it be a class with static methods?

**[01:46:50]** Okay, cuz that's what I was asking for.

**[01:46:54]** Yeah, okay. So look. I don't It did not do what I wanted. I mean close. So Okay. We'll go all the way down here.

**[01:47:06]** You know, I wanted a stateless class.

**[01:47:13]** That is a class with static functions.

**[01:47:21]** Okay? Right? So you didn't uh And I noticed some of the functions were handling partition logic.

**[01:47:35]** Is that something that should really be part of the partitions uh py?

**[01:47:44]** Right? So that's something I'm noticing as we are shaping that code.

**[01:47:50]** Okay? And so we're going to give that a moment to shuffle those things around.

**[01:48:07]** Now, is it thinking about that or is it just shoving things over there? Index by agent for partitions. Sure.

**[01:48:15]** Build initial messages. Again, is that for partition? Is it actually asking that question? Does it belong over there or is it just that it's handling partition data?

**[01:48:25]** Because it moved it and it didn't actually question whether it goes there or not.

**[01:48:30]** Um But anyway, we'll go over to here and we'll take a look of what's changed.

**[01:48:38]** What's it still working? It's now this is looking a lot better.

**[01:48:44]** Um Cuz now we can see what is going in, what's going out, right?

**[01:48:51]** Okay. And so we have all these steps.

**[01:49:06]** So we have call. So create a message.

**[01:49:11]** Log reasoning. Again, like it does this logging stuff belong with the logger?

**[01:49:19]** Handle screening agent. Handle evaluation coverage. Handle files. Handle submit final.

**[01:49:28]** Process tool calls. Run. Did they put these at the bottom?

**[01:49:34]** They did. Sometimes people put these at the top or sometimes they put at the bottom, but like the one that obviously is the big one is this one here. And so the idea is that we should be able to easily see what it's doing. So we have generate partitions, partitions.

**[01:49:46]** Validate overlap. Index agents, right?

**[01:49:48]** And so this should be self-documenting as you read it. We go down here. We call the coordinator. We do the log reasoning.

**[01:49:57]** Why are these functions? Are these just loose functions?

**[01:50:01]** They are. Well, no, they're part of the partition. And so I would go over to here and I would say, you know, give the um give the partitions.py the partitions.py like all of our lib directory Now I'll say our partitions.py should be a stateless class.

**[01:50:26]** I So a class with static functions.

**[01:50:31]** Please update. And that's just the way I prefer it, okay? I like to group them into domain. I don't like having loose functions where we don't know where they're coming from and who who respects them or owns them.

**[01:50:47]** Um people in the data space are very much used to just randomly importing a bunch of stuff, so they have a less sensitivity to to that kind of thing, but to me as a very professional developer I I want to see where that stuff is coming from. We still have some of our if else stuff here. And notice in here like these again, these should be functions.

**[01:51:07]** Right? All they're all they're doing is calling these things, but still I want these as functions.

**[01:51:12]** If there's an if else statement in here, especially in our main loop, that's what it should be. We have a range of 1 to 31, so that's kind of defining how many steps it can take. Um I would rather that uplifted as a variable.

**[01:51:23]** But we're not going to go too crazy on this. I just want to get it in enough shape here. And mostly just to show you like what good code looks like. Um and what you should be doing before you move on stuff. You might say, "Well, Andrew, why like this is more work to read?"

**[01:51:37]** Yeah, but if if you want to write test code for this then you have an input and an output and you know exactly what to mock going in there and out of there.

**[01:51:44]** The only thing that I would also change is like if these are complex um objects I'd want them to be dumber and only pass in really dumb data so that we could mock it a lot easier. And this is pain points if you've spent a lot of time writing uh code. And you might say, "Well, you know, the AI can write the test code for us." But that doesn't make it good test reliable test and and you'll only know that by uh writing that stuff. But we'll go over here. We'll take a look at our partitions.

**[01:52:09]** And so that is fine. There's still lots of little improvements to be made like I'm looking at like why is that like that? I don't like hard-coded stuff like that. Um there's just a bunch of little things. But I'll just say we'll move the coordinator over. So uh the coordinator uh can be in its uh coordinator class should be uh in a its own file in the lib directory.

**[01:52:35]** Okay? And we'll move that over there. That'll be the last thing we do here.

**[01:52:40]** Um and then what we will do is we'll just run it, make sure it still works.

**[01:52:45]** And then we'll call this, you know done-ish, right? But again, you know, if this was something that I would want to put in production, I would take the time and fine-tune it. I would take the time and fine-tune it and and because that's about getting um uh the word I'm looking for is um uh technical ownership, right? That you have ownership of the code and and you know exactly what it's doing. When you shape it like that, then you have a better sense of it. So now the coordinator is over there. I want to just run it to make sure it works. So I'm going to CD into the coordinator refactor and we're going to go ahead and run python. or python.main.py.

**[01:53:22]** Okay? So we're going to run that and we will take a look and hopefully it still works.

**[01:53:29]** There we go. I wonder if it's going to make the log file.

**[01:53:36]** We do get our logs. Excellent. Coordinator.log. Okay, and see that's what I meant when I said I wanted it to be nice and uh and whatever. I might even suggest like I'd probably prefer it to log out JSON structure because then we could parse that information.

**[01:53:50]** Um yeah, I think I would that's what I would prefer especially like if you're data-driven and you have JSON L data as logs, it's super super useful.

**[01:53:58]** Um so instead of having like coordinator and delegate um I would probably just have JSON objects and then I could parse it and ingest it into something else.

**[01:54:05]** But again, these are little tricks that you learn building applications of all kinds. Um but the point is that it is running. We just want to see it to completion and then we will call this done and then we will move on because the next section of stuff we are looking at is um stuff that I feel like agent SDK is going to be uh very useful for.

**[01:54:25]** Um they'll all have to decide on that.

**[01:54:29]** And so it did run. Worked great. The only thing that I'd probably ask it to do, which it's not doing right now is that I would have it dump the coverage report into its own file. So that'll be the last thing that we do here.

**[01:54:39]** Okay, and so I'm going to go here.

**[01:54:42]** Cuz that would actually make it useful, right? So I'm going to go and just say um you know, for my coordinator refactor uh it currently generates it generates a coverage report in the logs but it really should be outputting outputting um uh the a a report timestamped uh in a reports directory um and formatted nicely for uh human to read.

**[01:55:20]** Right? And so that's the last thing I would absolutely say we need to do. I just realized that that's a little bit um gross on how it currently is.

**[01:55:30]** Uh and we never looked at our data, but yeah, we have our job posting and stuff.

**[01:55:34]** And this is we could enrich these later, but they're fine.

**[01:55:38]** There's really no new data here.

**[01:55:39]** Uh we could have made a research that would grab job postings and make it for us. Not that anyone really should care about job postings anymore because agents are just going at it, but we'll wait for this to finish. Okay? And then we might run this one more time.

**[01:55:54]** Okay, there we go. And so um it says it's there. The other thing is that I don't think we're logging uh usage.

**[01:55:58]** So that would be nice to be able to log that information out. But again, these might be things we get for free when we use the agent SDK.

**[01:56:08]** So I'm not exactly sure. Um and so now that is done, I'm going to go ahead and run this one more time. Clear.

**[01:56:13]** I have no idea how many um credits I'm burning. Like again, I haven't hit my I have like $5 or whatever. I haven't hit it yet and Bako's not going to get mad if I load up another $5. So so far it is not a pain problem. People don't know, Bako is the other Andrew, Andrew B. I'm Andrew B. And so we call him Bako so it's not confusing. He's definitely a real person. He's not um an agent. Or is he? We don't know. No one ever sees him.

**[01:56:37]** Uh so we're going to run this again. I'm going to pause here and then I just want to confirm the reports are there. But again, you can just see my thoughts of like what would be good to do. Okay?

**[01:56:46]** We still have the coverage report being logged here, which I don't like, but that's fine. As long as we got a I didn't we didn't tell tell it to not do that there. But we'll go here and then here is our report. We can go ahead and view it over like this.

**[01:56:59]** And so there is our final coverage assessment.

**[01:57:03]** Um I really don't like how long it's written this stuff. Like if you were human, would you want to read this much information? Probably not. Or you'd want it summarized in a different way, but we never gave it a coverage report template, so that's fine. We will consider this done. We'll say get add all, get commit refactor.

**[01:57:21]** But that wasn't bad for a quick refactor. Still lots of work to be done there, right? Um I'll see you in the next one. Ciao ciao.

**[01:57:30]** Hey folks, it's Andrew. We're back and it's time for us to port our coordinator application over to agent SDK. And the reason why is that we're going to be getting into um uh specific agent SDK um arguments and if we want to know how they work, we need to have an example over there. And I think we should just continue this project forward and I think it's not a bad idea. So what we are going to do um is we're going to call this uh port to to agent SDK.

**[01:58:05]** Okay? And so what I'm going to do here is I'm going to grab the contents of all this. Not the logs. We don't need the logs or the reports. But we will grab this, this, this, this, this, and this.

**[01:58:15]** Right click copy. We'll go down over to our port to agent SDK. We will paste this stuff in.

**[01:58:25]** And we're are going to let her rip and see if it will allow us to port it over in one go here.

**[01:58:32]** So I need to port the my code base uh of Anthropic SDK based on uh for my agent that uses directly the Anthropic SDK to use Claude agent SDK for this folder.

**[01:58:56]** Port SDK. And so we're going to ask it to go ahead and do that. That's a big thing. Again, we probably should have put it in a plan mode and ask it what it can do.

**[01:59:06]** But I'm just going to go off of the races and do that. And if it works, we will explore it and we'll have time to look at the code base quite a bit as we walk through other features, okay?

**[01:59:18]** All right, let's take a look here and see what we have.

**[01:59:21]** So we have the run updated. I'm not sure why it did that. It's not really that big of a deal.

**[01:59:28]** We removed the async Anthropic and coordinator. These are now internal to the coordinator. Sure.

**[01:59:35]** It has a complete rewrite. I was expecting that.

**[01:59:39]** That I assume that would be the largest rewrite for us.

**[01:59:43]** And I guess all those are unchanged.

**[01:59:45]** That's really interesting. And then we need to do a a update here. I mean, you know, you know, can you make the requirements.txt for me?

**[01:59:54]** Cuz that's what it should have done. But I we never copied it from a prior one.

**[01:59:58]** That's probably why. Yeah, we didn't. So let's go take a look at the the major changes. So we'll look at the main.py. And here we can see async Anthropic. Oh, so there's where it's different. Default async client. That's why there was a change there. This is the new one, right?

**[02:00:18]** There we go. Okay. And so this more or less looks the same.

**[02:00:21]** But we'll go into our coordinator directory here.

**[02:00:27]** And let's see if we can make the difference here.

**[02:00:35]** Okay. So I'm going to do is scroll up here. What I might do, just so that we can really clearly see the difference, we might refactor a smaller one because it's very hard to see the changes. They don't even show us the code changes here, right? Um So what I'm going to do, I'm going to make another repo.

**[02:00:58]** We have uh Make another folder here. Let's see.

**[02:01:03]** Port to Anthropic uh port to agent SDK small.

**[02:01:09]** And the reason I want to do that again is to really clearly see the difference.

**[02:01:20]** And so I'm trying to think of one that we were doing before, like narrow task decomposition.

**[02:01:25]** Yeah, where we have this one. This one's a lot simpler, right?

**[02:01:29]** And we actually might want to go one step before that where we are using tool use.

**[02:01:34]** Um Could be decision-making, model-driven, right? So this one here is a very simple one with multiple tools. So what we're we'll do is we'll copy this over here. And then I go into this directory just so we can clearly see the difference. And then also maybe just have another one that we can work on.

**[02:01:55]** Though I don't really like this use case per se. Okay. And so I'm going to go and say, "Okay, great.

**[02:02:01]** Can we Can we convert the code for port to agent uh SDK small?"

**[02:02:09]** over to agent SDK. Again, we haven't tested if these actually work. Hopefully it knows Claude agent SDK, not just some generic one. Um but anyway, I think it knows. I hope it knows. We'll wait here a moment, okay? All right, so we have the refactor already done for this one.

**[02:02:29]** Didn't take too long. Let's see what it's changed. So the imports are different.

**[02:02:34]** Yeah, it is using Anthropic, the correct one.

**[02:02:39]** No, no, no, no, no. It Yeah, it is.

**[02:02:40]** Okay, here it is. So here it is and here instead of handling tools here, we have a decorator.

**[02:02:48]** And then the functions are probably defined a particular way. See this whole big thing is probably gone. Yep. And so we have decorators on top of our functions making this code a lot smaller.

**[02:02:59]** Okay. Um the call is a bit different. So that's one thing.

**[02:03:06]** And we are creating the SDK MCP server to pass the tools over. So that is another thing that's changing.

**[02:03:16]** Okay. Um I mean, we have new modes and we're setting our MCP server with our tooling in it.

**[02:03:27]** Um okay. So basically we basically have an internal internal MCP. That's really interesting they make that with super super easy.

**[02:03:36]** And this call is a little bit different.

**[02:03:38]** So basically the big thing that we're seeing is that tool use.

**[02:03:41]** Um so let's go back to our larger refactor. And I want to take a look at our tools.

**[02:03:49]** And so that tool.json, do we even need that anymore? Does that even make any sense? So what we'll do is go back over here.

**[02:03:56]** Cuz now we know what was refactored, right? And we'll say, "Do we even need the tools.json anymore? And shouldn't we be using the decorator?"

**[02:04:10]** for port to agent SDK base for Claude agent SDK.

**[02:04:32]** And I imagine that you can probably pass in that JSON tools cuz it's it's doing it. No, we don't we don't know if it actually works or not. Um Like we go here, tools.json.

**[02:04:44]** Like I don't see it loaded in here.

**[02:04:47]** Maybe it's getting loaded in the main.

**[02:04:48]** It is refactoring probably right now, so we wouldn't even know.

**[02:04:51]** But we'll see what it says here.

**[02:04:55]** Cuz we do have tool right here, right?

**[02:04:57]** So it is. It's right here. So maybe it just has to delete it out.

**[02:05:01]** But if the tool is here, then why isn't that defined? Or does it have to sit in the same place?

**[02:05:08]** Right? So we have this one here. Is this just a repeat?

**[02:05:13]** Okay. And like look at all this inline stuff, eh?

**[02:05:31]** Object maybe pass rationals key strings.

**[02:05:39]** That's the structure that we actually wanted from before.

**[02:05:43]** Um And so here all three tool decorators are now using the simple peram.

**[02:05:49]** Okay, but like does the coordinator still have them in here?

**[02:05:53]** Do we have to have the tools in the coordinator .py or can they actually they live in the um tools directory as separate functions?

**[02:06:18]** Or it doesn't work because tight coupling of the decorator.

**[02:06:30]** Which is this part here. It might be the reason why they can't do that. And I mean, hopefully it knows what last directory we're in.

**[02:06:40]** Is it more than one? But we'll ask that question. And you know, this is what I'm trying to figure out.

**[02:06:46]** Let's see what it says here. So the key insight tools of decorator runs at call time, not import time. So you can apply it inside the factory function that captures state via normal closures.

**[02:06:57]** Okay. Well, speak English to me here.

**[02:07:06]** Can we move it or not? Coordinator class.

**[02:07:12]** Tools. Screening agent. Look look, I'm trying to keep my stuff lean here, folks.

**[02:07:20]** Did it move it out? Did it even tell me that it moved it out?

**[02:07:27]** Okay. So here coordinator state, make coordinator. So it did move it out from tools.

**[02:07:35]** I don't like how they're make coordinator tools.

**[02:07:39]** Okay. And then we have coordinator state.

**[02:07:45]** All right. Okay, I see. So they they have a state file separately for the I mean, state wouldn't belong in tools, now would it?

**[02:07:55]** So that doesn't make any sense.

**[02:07:56]** Unless it's coming from that file. Maybe it it's part of it. That's why. Okay.

**[02:08:00]** And so we go over to here. And we have make coordinator tools. Oh, and they do have it in here. Okay, so they were able to move it out.

**[02:08:07]** And so here we have our multiple tools. Okay. And so to me, that's what I would like it to be.

**[02:08:15]** So I'm going to go ahead and we're going to stop this. And we're going to CD into the port to agent SDK. And I just want to make sure that this still works.

**[02:08:23]** So we'll go ahead and say main.python.

**[02:08:25]** dot We have main or main. Python. I got it backwards.

**[02:08:31]** Python main. Whatever. Whoops. Okay.

**[02:08:40]** And I just want to make sure that it still runs. Because we've changed a lot of code or at least one large file to another framework.

**[02:08:50]** And um It's logging. We'll pause here and see the end result, but I'm pretty certain that it's going to work.

**[02:09:02]** Okay, so it ran without issue and we are in good shape. Um Yeah, so we are set up and the question will be like, you know, do we use this to test out all the agency decay stuff or do we come back to this project? We will see, but at least we made it to this point and I think the key takeaway here is the fact that uh the tool use call got easier and it's setting up an MCP server. Okay, so literally it's an internal NPC server.

**[02:09:30]** Um and so clearly uh Entropic is obviously making that a priority tool. But anyway, there we go and we will move on from that, okay? Ciao ciao.
