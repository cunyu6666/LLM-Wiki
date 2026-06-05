---
id: "7423721250612053158"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA==&mid=2247483834&idx=1&sn=feb7d75a0fa287396feaddfa5cf42902&chksm=f1d825c1b3e591a686be3f4275794c8882c8aa5e76355c40f42582925bec84f67410656b3f61&mpshare=1&scene=1&srcid=0218osYrWwsp7r9s1RTrhnHs&sharer_shareinfo=1438c08f637b0cfd0e85ccad5972758b&sharer_shareinfo_first=1438c08f637b0cfd0e85ccad5972758b
author: "Boding 歪脖抠腚"
collected: 2026-02-18
tags: []
---

# Claude Code 核心成员 Thariq：Bash 被严重低估，Verification 要贯穿整个 Loop，以及如何定义高效的 Agent Loop

# Claude Code 核心成员 Thariq：Bash 被严重低估，Verification 要贯穿整个 Loop，以及如何定义高效的 Agent Loop

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA==&mid=2247483834&idx=1&sn=feb7d75a0fa287396feaddfa5cf42902&chksm=f1d825c1b3e591a686be3f4275794c8882c8aa5e76355c40f42582925bec84f67410656b3f61&mpshare=1&scene=1&srcid=0218osYrWwsp7r9s1RTrhnHs&sharer_shareinfo=1438c08f637b0cfd0e85ccad5972758b&sharer_shareinfo_first=1438c08f637b0cfd0e85ccad5972758b)Boding 歪脖抠腚

## 这不是一场普通的 SDK 分享：Thariq 想聊的是"怎么做出能干活的 Agent"

这篇文章整理自 Anthropic 的一次内部式 workshop 分享。分享者是 Claude Code 团队的 Thariq Shihipar，他围绕 Claude Code、agent 框架与工具体系展开，核心讨论的是\*\*"怎么构建能真正持续产出的 agent 系统"\*\*，而不仅是"如何调用 SDK"。内容聚焦在工程判断、方法论与取舍上，尤其适合关注 AI coding、agent 框架、Skills 与 Bash 工具体系的人阅读。

## 几条可能惹人不爽的判断：Agent 不是模型、Bash 被严重低估、Skill 只是"节流阀"

下面是 Thariq 在分享中反复强调的关键观点，按逻辑重组为 1-4：

1. **Agent 的本质是系统，而不是模型**   


   ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wDee3GJUeXWDy3zzZ66Wtl21gblklDorUpRb5zaMROm4CtLmjVqQhF4g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

   在他看来，Agent 不是单次调用的模型能力，而是一个由模型、工具、文件系统与验证机制构成的系统。真正有效的 agent 不是"更会答题"，而是"能在工程里持续交付结果"。
2. **Agent loop 的三步循环决定上限：Gather Context / Take Action / Verify Work**   

   ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wDmwRNoVjGic1LibGBAP0bxOantWcRfjZE9C6Gm5J4HmsesncVD7hWd4Vw%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)许多 agent 的失败不是因为模型不强，而是缺少可靠的上下文收集与验证机制。验证越强，agent 就越能承担复杂任务；验证越弱，越只能停留在演示级别。
3. **行动方式不是"工具至上"，而是 Tools / Bash / Codegen 的组合权衡**

   **![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wDU5O5RAUTOaku3G0xc62PJkobB7OoNsq0n1lC43oHKYTj4dWw5bYTEg%2F640%3Fwx_fmt%3Dwebp%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)**
   *
     Tools 结构化、可控、低风险，但上下文成本高、可组合性差
   *
     Bash 组合能力强、上下文更省，但需要发现成本
   *
     Codegen 最灵活，但执行成本最高、风险最大  
     他的判断是：很多团队过度依赖 Tools，而低估了 Bash 的价值。Bash 能把工具输出沉淀为文件，成为 agent 的"外部记忆"与可复查证据。
4. **Skills 与文件系统是"渐进式上下文披露"的工程解法**   

   ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wD5b1SDicoxZ9kPJ5y8M9Ajvv6PXzOU0wMYqALB1aCyFjqLQAiaK3BVhlw%2F640%3Fwx_fmt%3Dwebp%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)  

   ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wDnIYicVEic3q41MZ3Bibar0PArlt5lLdDLl0zUicv50gscdSibic2ElJVibNHg%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)Skills 不是"塞进 prompt 的资料包"，而是按需加载的专业流程；文件系统本身可以充当 memory，让 agent 在长任务中保持可复查、可迭代的状态。

## 大家追着问的问题：如何选工具、如何做验证、如何把 Agent 真正用在业务里？

**问题 1: "Code generation for non-coding" 具体是什么意思?**   
**提问者** : 可以解释一下 "code generation for non-coding" 具体是什么意思吗?  
**Thariq** : 好,这基本上是说当你让 cloud code 去做一个任务时,举个例子:比如你问它"找一下旧金山的天气并告诉我今天该穿什么",它可能会开始写一个脚本去调用天气 API,然后可能希望变得可复用,比如动态获取你的位置信息(基于 IP),然后检查天气,可能再调用一个 sub agent 给出建议,或者连到你衣橱的 API,等等。这就是 codegen 的一个例子。总体上是组合 API 的高层次思路。

**问题 2: Workflow vs Agent------对于重复或确定性的业务流程,更适合用哪个?**   

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wD8CBdqRbewGDODvqP1NQJq8xYr9m0YFpnhm4vt6qiaAvISErpatdpRtw%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)**提问者** : 关于 workflow vs agent,对于重复或确定性的业务流程,你会更愿意用 agent 还是完全确定性的 workflow?  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfVlZOGIylX30XnOqEKqZ6WPksgh2I5wDtEy6Zjveqr5Im0eGeTQV9lgCX5RjbibHeKkgUSCJLQFt26G4Rteft9w%2F640%3Fwx_fmt%3Dwebp%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)**Thariq** : 你是说对于工作流 vs agent 的问题,是否仍会用 cloud agent SDK 来实现工作流?是这样吗?嗯,答案是肯定的。我们内部确实这样做。我们在 cloud agent SDK 上构建了许多 GitHub 自动化和 Slack 自动化。例如,我们有一个 bot 用来对新进来的 issue 做 triage。这就是一个相当像工作流的例子,但我们发现为了做 triage,agent 有时需要 clone 代码库、有时需要启动 Docker 容器并测试它,因此中间需要很多自由流程的步骤,最后再给出结构化的输出。  
所以,是的,你完全可以用 agent SDK 来做 workflow。我们还刚刚发布了对 structured outputs 的支持,Google 的 agent SDK 里也有类似功能。总之,这两者都能用 agent SDK 来实现。接下来我会主要讲 agents,很多从这里学到的东西同样适用于 workflows。

**问题 3: 什么时候会生成一个 plan?**   
**提问者** : 什么时候会生成一个 plan?  
**Thariq** : 你可以在 gather context 和 take action 之间插入 planning 步骤,让 agent 逐步思考,但这会增加延迟,所以要在延迟和计划质量之间权衡。agent SDK 提供了一些帮助来做计划。

**问题 4: 能让 agent 为自己创建一个 to-do list 并完全按此执行吗?**   
**提问者** : 能让 agent 为自己创建一个 to-do list 并完全按此执行吗?  
**Thariq** : 是的。如果使用 agent SDK,我们自带一些 to-do 工具,agent 可以维护并勾选 to-dos,并在过程展示给你。

**问题 5: 有没有现成的工具去 offload 长输出到文件系统以避免 polluting history?**   
**提问者** : 有没有现成的工具去 offload 长输出到文件系统以避免 polluting history?  
**Thariq** : 是的,这是一个常见实践:每次 tool call 我们都会建议把结果存入文件,并让 tool 返回文件路径,这样便于后续搜索、复查与验证。

**问题 6: 关于自定义的内部 bash 工具,如何让 agent 发现这些工具?**   
**提问者** : 关于自定义的内部 bash 工具。你如何让 agent 发现这些工具?还是这些必须成为 tool?  
**Thariq** : 问题是如果你有自定义的 agent bash 工具,如何让 agent 发现它?你说的自定义 bash 工具是 bash 脚本吗?  
**提问者** : 我们有 bash 脚本,是的。  
**Thariq** : 嗯,我认为------把它放到文件系统里面,然后告诉它"嘿,这里有个脚本",你可以调用它。我主要是在 cloud agent SDK 的上下文里思考,这里有文件系统并且 bash 工具是绑定在一起的。有一种反模式是人们把 bash 工具放到某个虚拟化的地方,它不会与 agent loop 的其他部分交互。如果 tool 的结果把东西保存成文件,那么你的 bash 工具就无法读取它,除非所有东西都在同一个容器里运行。这样能回答你的问题吗?  
**提问者** : 有点儿。我是说你只是把它放到 system prompt 里吗?  
**Thariq** : 是的,我会在 system prompt 里写"你有权访问这些脚本"。我会把所有 CLI 脚本设计成带有 --help 或类似子命令的形式,这样模型可以调用它并逐步发现脚本的子命令。

**问题 7: 什么时候应该采用 agent SDK?用于通用 chat agent 还是特定的输入输出场景?**   
**提问者** : 我想问的是什么时候应该采用 agent SDK。你会建议有人使用 agent SDK 来构建通用的 chat agent,还是像那种有输入、agent 去做一些事情、最后只关注输出的场景?你会用 agent SDK 去做像 cloud.ai 这种传统的聊天应用吗?  
**Thariq** : 这是个好问题。cloud code 作为一个界面并不是传统的 chatbot 接口,但它的输入输出是类似的:你输入文本或代码,得到文本输出,并在过程中采取行动。你们可能见过我们为 cloud.ai 推出的文档生成功能,现在它能 spin up 一个文件系统并生成电子表格、PowerPoint 等,通过生成代码来实现。所以我们正在把 agent loops 与这些东西融合。总体来看,cloud.ai 正在逐步吸收 skills、memory tool 和更多文件系统能力。因此,agent SDK 可以被用在更广泛的场景上,我很乐意跟你们讨论具体示例。

**问题 8: 何时该把某个东西做成 tool、何时用脚本包装?数据库访问应该怎么选?**   
**提问者** : 还有一个问题:何时该把某个东西做成 tool、何时用脚本包装,何时就直接让 agent 在 bash 上"放飞自我"?举个例子,我需要不定期访问数据库。我可以用 MCP(注:应该指某种 API 网关),也可以把它包装成脚本,然后让 agent 在 bash 里直接调用 endpoint。应该怎么选?  
**Thariq** : 好问题。确实没有一种通用的最佳实践,这是个系统设计问题。如果你的数据库非常结构化并且访问需要严格控制(比如敏感用户数据),你就应当把访问封装成 tool------限制输入输出,以屏蔽其他数据。但如果 agent 需要生成完整的 SQL 查询,可能更适合让它通过 bash 或 codegen 来生成、运行、查看错误并迭代修正。总体策略是尽量给 agent 灵活性,但在敏感操作上加 guard rails。我会给 agent 有限的权限并写一些规则,当它尝试做超权限的事情时给出反馈。我们为此构建了 bash tool parser 来解决这类复杂问题。

**问题 9: 关于 role-based access control(基于角色的访问控制)**   
**提问者** : 那关于 role-based access control(基于角色的访问控制)呢?  
**Thariq** : 通常这是在你如何 provision API key 或后端服务时处理的。常见做法包括:创建临时的 API keys,或在代理层插入 proxy 来注入凭据(以防信息外泄)。给 agent 的 API keys 应该是有作用域限制的,后端可以根据它尝试的动作做额外检查并返回不同的反馈。

**问题 10: 关于 memory tool**   
**提问者** : 再问一个关于 memory tool 的问题。你能多说点内置 memory tool 吗?  
**Thariq** : 我并不想卖关子,但我没读过内核代码。总体上 memory 是基于文件系统实现的。在 cloud agent SDK 里,我会建议你直接用文件系统,比如建一个 memories 文件夹,让 agent 把记忆写到那里。memory tool 底层就是以这种方式工作,所以直接用文件系统就很方便。

**问题 11: 关于可重用性------如果同一个 agent 被部署给上百个用户,如何做到重用?**   
**提问者** : 好,最后一个关于可重用性的问题:如果同一个 agent 被部署给上百个用户,每次它都生成相同的代码并执行,我们如何做到重用?  
**Thariq** : 这是个好问题。传统的 web 应用是一个应用服务大量用户,而 agent 常常是 one-to-one 的容器(每个用户一个容器)。如何让 agents 之间共享工作成果是一个待探索的问题。一种直接的方式是让 agents 使用现有的通信手段(HTTP、API keys、命名管道等)彼此交互,或者把结果发到一个共享的论坛让其他 agents 订阅。我们不需要发明全新的通信系统,使用已有的基础设施通常就足够。

**问题 12: 如何把流程步骤形成序列?例如先 search 再 do X 再 do Y?**   
**提问者** : 如何把流程步骤形成序列,例如先 search 再 do X 再 do Y?是把这些步骤写在 system prompt 里吗?  
**Thariq** : 是的,通常在 system prompt 里我们会告诉 agent:"gather context、read your files、run lint 等",但 agent 并非总是需要严格按照这些步骤执行------有时某些步骤并不必要(例如只读查询时无需做写入相关的验证)。给 agent 自由但提供合适的工具与提示通常是最好的方式。

**问题 13: 关于 verification 的具体放置**   
**提问者** : 关于 verification 的具体放置:例如在 SQL 生成后先验证语句是否正确,还是先执行再验证?agent 如何动态选择路径?  
**Thariq** : 验证应该尽可能到处进行,而不是只放在最后。我们在 cloud code 的读取步骤就做了部分验证,这很有帮助。你当然也应该在最终步骤验证,但如果在中间有规则或启发式检查(例如限制一次搜索的列数不要超过特定阈值),可以在早期就抛错并给出反馈,模型会读取错误输出并作出相应调整。总之,把验证放在尽可能多的地方,形成一个循环式的验证与修正流程。

**问题 14: 如果把这个部署给客户,cloud code 应该以 swarm(集群)形式运行,还是能够把 cloud code 部分抽离,只用 agent SDK?**   
**提问者** : 如果把这个部署给客户,cloud code 应该以 swarm(集群)形式运行,还是能够把 cloud code 部分抽离,只用 agent SDK?  
**Thariq** : 你可以这样看:我会先在本地用 agent SDK 做原型,文件系统是 context engineering 的主要入口点。我的实际 agent 文件可能只有 50 行左右,很多只是 boilerplate。它会在一个循环里运行查询并处理工作目录。  
把原型 productionize,有两种常见方式:

1.
   把应用打包成本地应用(用户安装并在本地运行 cloud code)
2.
   把它托管在 sandbox(例如 Cloudflare 等)中,为每个用户或会话启动隔离的容器  
   一些 sandbox 提供商(例如 Cloudflare)已经把 agent SDK 的运行抽象化了,你可以用类似 sandbox.start 之类的命令,然后运行 bun agent.ts 之类的脚本来启动 agent。这样能减少运维复杂度。

**问题 15: 关于 UI 个性化**   
**提问者** : 关于 UI 个性化,如何实现?  
**Thariq** : 如果你希望 agent 实时适配用户,你可以在 sandbox 中运行一个 dev server(bun 或 node),agent 可以编辑代码并触发 live-reload,用户在浏览器中就能看到实时的界面变化,这也是很多 site-builder 的实现思路。

**问题 16: 关于 monetization(货币化)**   
**提问者** : 关于 monetization(货币化)方面有什么建议?  
**Thariq** : 目前构建 agent 仍然有成本,因为 agent 功能更复杂、使用的模型更"agentic"。常见商业模式包括:

* **订阅制**
* **基于用量的计费**
  (rate limits + usage-based pricing)
* **面向解决"难题"的高价付费客户**


  关键是先确认你解决的问题是用户愿意为之付费的,然后再选择合适的计费模型。

**问题 17: 关于 Hooks**   
**提问者** : 能讲讲 hooks 吗?  
**Thariq** : 我想补充:hooks 是我们提供的事件机制,常用于 deterministic verification 或插入额外上下文。  
比如在每次 tool call 后触发一个 hook 来把用户最近的更改同步进 agent 的上下文,这样 agent 就能实时获取到用户在表格中做的变更。hooks 文档里有很多示例,适合做验证、插入动态上下文或监控工具调用。

*** ** * ** ***

原视频参考：https://www.youtube.com/watch?v=TqC1qOfiVcQ

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA==&mid=2247483834&idx=1&sn=feb7d75a0fa287396feaddfa5cf42902&chksm=f1d825c1b3e591a686be3f4275794c8882c8aa5e76355c40f42582925bec84f67410656b3f61&mpshare=1&scene=1&srcid=0218osYrWwsp7r9s1RTrhnHs&sharer_shareinfo=1438c08f637b0cfd0e85ccad5972758b&sharer_shareinfo_first=1438c08f637b0cfd0e85ccad5972758b)

