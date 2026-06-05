---
id: "7447013672213283046"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649107404&idx=1&sn=8a57aa2fcbad64c8ecb5903f6ced9bf1&chksm=821d465705c93fac0e63101a56f2959419b7d48e2bb82528793bf8eefd6b850e6bd00e5a23a6&mpshare=1&scene=1&srcid=0423vYL39NrioVpiHitjnnMJ&sharer_shareinfo=8b03d9184d96faba5f128c76513bfc7c&sharer_shareinfo_first=8b03d9184d96faba5f128c76513bfc7c
author: "Mario Zechner 十字路口Crossing"
collected: 2026-04-23
tags: []
---

# ”为什么我开始反对 Vibe Coding?“

# "为什么我开始反对 Vibe Coding?"

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649107404&idx=1&sn=8a57aa2fcbad64c8ecb5903f6ced9bf1&chksm=821d465705c93fac0e63101a56f2959419b7d48e2bb82528793bf8eefd6b850e6bd00e5a23a6&mpshare=1&scene=1&srcid=0423vYL39NrioVpiHitjnnMJ&sharer_shareinfo=8b03d9184d96faba5f128c76513bfc7c&sharer_shareinfo_first=8b03d9184d96faba5f128c76513bfc7c)Mario Zechner 十字路口Crossing


乌龟那张脸，就是我看着我们这个行业时的表情。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2Fa16Y4PLxPqkK9EX6aJtVqJR3nOc7ZpZo7naE94ERviaIfryicrfBOr0XFejFJTI3jrwbp0N1PxZMPbpLkItCp4gDaictdMh7V47df9XEyvGDes%2F640%3Ffrom%3Dappmsg%23imgIndex%3D0)

👦🏻 作者: Mario Zechner  

🧑‍🎨 翻译/排版: Zeoooo  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fa16Y4PLxPqnSj4lKf7KodtNZ358KIBnNVT4QVRqFibdkCv7Y5nrXWSJEEFyLkDWicFjG7pCX1X0KaBPiacq0d0ibp8TAfcXA6UsabuORQMiaYqTI%2F640%3Ffrom%3Dappmsg%23imgIndex%3D1)

**Mario Zechner 居然写了一篇来痛批 vibe coding。**   

他是谁？PI 框架的作者------同时也是 libGDX 这个跨平台游戏框架的创造者。PI 是 OpenClaw 的底层 agent 框架，而 OpenClaw 是不到三个月内从零涨到 25 万 GitHub stars 的项目。  

然而 Mario 写了这篇文章，说：  

你们都在用 agent 把自己搞进死胡同。

这是我们最近读到的关于 AI coding 很特别的一篇文章，也几乎是唯一的反对声音。Mario 没有鼓吹「AI 要取代程序员」，也不是在直接否定「AI Coding 根本没用」，而是在说：  

当你把所有 AI coding 的判断都外包给 agent 的那一刻，你丢掉的不是工作量，是 agency。

文章最后一句话，甚至值得打印出来贴在墙上------  

All of this requires humans.

这一切，都需要人类。


🚥  

距离那一代真正能帮你从零搭建完整项目的 coding agents 出现，已经差不多一年了。之前也有 Aider 和早期 Cursor 这样的先驱，但它们更像助手，而不是真正的 agent。新一代工具令人着迷，我们很多人花了大量业余时间，用它们把那些一直想做却没时间做的项目都做了出来。  

我觉得这没什么问题。把业余时间用来做东西非常享受，大多数时候你根本不需要在意代码质量和可维护性。如果你想学新技术栈，这也是个好机会。  

圣诞假期期间，Anthropic 和 OpenAI 都发了些福利，让人们沉迷于他们的老虎机。对很多人来说，这是他们第一次体验到 agentic coding 的魔力。入坑的人越来越多。  

**现在，coding agents 也开始被引入到生产代码库中。经过 12 个月，我们开始看到这些「进步」所带来的后果。**   

以下是我目前的看法。  

一切都坏掉了  

虽然这些都是道听途说，但软件确实感觉变成了一团脆弱的乱麻------仅仅 98% 的 uptime 正在成为常态而非例外，就连大型服务也不例外。而用户界面出现的那些奇葩 bug，任何一个 QA 团队都应该能发现。当然，这个问题比 agents 的出现早得多。  

**但我们似乎正在加速。**   

我们无法了解公司内部的情况。但偶尔会有一些消息溜出来被记者捅到媒体上。比如这起据说是 AI 导致的 AWS 故障^\[1\]^，AWS 随即「辟谣」^\[2\]^，然后又内部跟进了一个 90 天重置计划^\[3\]^。  

微软 CEO Satya Nadella 一直在鼓吹微软有多少代码现在是由 AI 编写的^\[4\]^。虽然我们没有直接证据，但 Windows 感觉正在走下坡路。微软自己似乎也认同这一点，看看这篇博文^\[5\]^就知道了。  

**那些声称产品 100% 代码由 AI 编写的公司，持续产出你能想象到的最差劲的垃圾。** 几个 GB 的内存泄漏、UI 错乱、功能残缺、频繁崩溃------这可不是他们以为的质量认证，也绝对不是「让 agent 替你干所有活儿」可行的广告。  

通过小道消息，你越来越多地听到来自大大小小软件公司的人说，**他们用 agentic coding 把自己逼进了死角** 。没有代码 review，架构决策全权委托给 agent，堆出了一堆没人要的功能。  

这就是结果。  

我们不该如何与 agents 合作，以及原因  

**我们基本上已经放弃了所有的纪律和自主性，换来了一种上瘾------你最高的追求就是在最短时间内产出最多的代码。** 后果？管它呢。  

你在搭一个编排层来指挥一支自主 agent 大军。你装了 Beads，完全没意识到它基本上是无法卸载的恶意软件。  

网上都这么说的，这才是你应该工作的方式，否则你就完了。你在无脑地跑循环。

你看，Anthropic 用 agent 集群搭了个 C 编译器------有点残，但下一代 LLM 肯定能修好的。天啊，Cursor 用一个 agent 大队搭了个浏览器。是的，确实没怎么跑通，中间还需要人类时不时拨一下轮子。但下一代 LLM 肯定能修好的，保证！分布式、分而治之、自主性、黑暗工厂，软件问题再六个月内彻底解决。**SaaS 已死，我奶奶刚让她的 Claw 给她搭了个自己的 Shopify！**   

再说一遍，这对于几乎没人用（包括你自己）的副业项目来说也许可行。也许有人真的能让这套东西在一款不是一坨热气腾腾的垃圾、还有真实用户在认真使用的软件产品上跑通。如果你做到了，那真的厉害。  

但至少在我身边的同行圈子里，我还没找到任何证据表明这套东西有效。也许我们都有技术问题。  

零学习、无瓶颈、延迟爆发的复利式 booboo  


booboo是什么？------ **单个的小 bug、小失误；**一个没用的方法、一段重复代码、一个说不通的类型。

agents 的问题在于它们会犯错。这没关系，人类也会犯错。也许只是些正确性错误，容易发现和修复，顺手加一个回归测试，加分项。也可能是 linter 捕捉不到的代码坏味道------一个没用的方法、一个说不通的类型、那边一段重复代码。单独来看，这些都无伤大雅。人类也会犯这种 booboo。  

**但机器人不是人类。** 人类会把同一个错误犯几次，最终会学会不再犯------要么是因为有人对他大喊大叫，要么是因为他在真正成长。Agent 没有这种学习能力，至少不是开箱即用的。它会反复犯同样的错误，取决于训练数据，它甚至可能创造性地把各种错误混搭出新花样。  

你当然可以试着训练你的 agent。在 AGENTS.md^\[6\]^ 里告诉它别再犯那个 booboo，设计最复杂的记忆系统，让它查阅以往的错误和最佳实践。这对特定类型的错误可以有效。但前提是你真的有观察到 agent 犯了那个错误。  

**机器人和人类之间还有一个更重要的区别：人类是瓶颈。**   

人类不可能在几小时内堆出 2 万行代码。就算人类以很高的频率制造 booboo，每天能往 codebase 里引入的 booboo 数量也是有限的。booboo 会以极慢的速度复利积累。通常，当 booboo 的痛苦大到一定程度，厌恶痛苦的人类会花时间去清理它们。或者这个人被炒了，别人来清理。所以痛苦会消退。  

有了一支编排好的 agent 大军，瓶颈消失了，也没有人类的痛感。那些微小的、无害的 booboo 突然以不可持续的速度复利。你把自己从循环里移出去了，所以你根本不知道那些无辜的 booboo 已经合体成了一只 codebase 怪兽。你只会在为时已晚的时候才感受到痛苦。  

某天你回过头，想加一个新功能。但架构------此时基本上就是一堆 booboo------不允许你的 agent 大军以正常运作的方式完成修改。或者你的用户在冲你大喊大叫，因为最新版本的某个东西崩了，还删掉了一些用户数据。  

你意识到你已经无法信任这个 codebase 了。更糟糕的是，你让机器人写的那数以万计的单元测试、快照测试和 e2e 测试，同样不可信。唯一还能可靠衡量「这玩意儿能不能用」的，就是手动测试产品。

恭喜，**你把自己（和你的公司）给坑了！**   

复杂度的贩子  

你对发生了什么毫无头绪，因为你把所有的自主权都委托给了你的 agents。你让它们自由驰骋，而**它们是复杂度的贩子** 。它们在训练数据中见过太多糟糕的架构决策，也经历了 RL 训练。你让它们来架构你的应用。结果你猜怎样？  

无穷无尽的复杂度，是各种糟糕的「行业最佳实践」货物崇拜的大杂烩------而你在事情无法挽回之前没有管住它。但还不止这些。  

你的 agents 彼此看不到对方的运行，看不到你完整的 codebase，看不到在它们做出改动之前你或其他 agents 做过的所有决定。因此，agent 的决策永远是局部的，这正是导致上述 booboo 的根本原因。大量的代码重复，为抽象而抽象。  

这一切复合成一团无法挽救的复杂度乱麻。和你在人工编写的企业级 codebase 里见到的那种烂摊子一模一样。那种烂摊子之所以形成，是因为痛苦分散在大量的人身上------个体的痛苦还没到「我需要修这个」的阈值，个体可能根本没有能力去修，而组织的疼痛耐受力极高。但人工编写的企业级 codebase 需要数年才能烂到那种程度，组织会随着复杂度以一种病态的协同缓慢演化，并学会如何应对它。  

而有了 agents 和一个两人团队，你可以在几周内就到达那种复杂度。  

Agentic Search 的召回率很低  

现在你希望你的 agents 能修复这团乱麻，重构它，让它重焕清爽。但你的 agents 也已经无力应对了。因为 codebase 和复杂度太大，它们只能看到这团乱麻的局部视图。  

我说的不只是上下文窗口大小或长上下文注意力机制在面对百万行代码庞然大物时的失效------这些是显而易见的技术局限。这件事更狡猾。  

在你的 agent 尝试帮你修复乱麻之前，它需要找到所有需要改动的代码，以及所有可以复用的现有代码。我们称之为 agentic search。agent 怎么做到这一点，取决于它拥有什么工具。你可以给它一个 Bash 工具，让它用 ripgrep 翻遍整个 codebase；你可以给它一个可查询的 codebase 索引、一个 LSP server、一个 vector database。最终差别不大。**codebase 越大，召回率越低。** 低召回率意味着你的 agent 实际上找不到它做好工作所需的全部代码。  

这也是那些代码坏味道 booboo 一开始就会发生的原因。agent 漏掉了现有代码，重复造轮子，引入不一致性。

**然后它们盛开成一朵美丽的 💩 复杂度之花**。

**我们怎么避免这一切？**   

我们目前应该如何与 agents 合作  

Coding agents 是塞壬，用它们的代码生成速度和参差不齐的智能诱惑你，经常以极快的速度高质量地完成一个简单任务。当你开始想「哦天哪，这东西真棒，电脑，帮我干活！」的时候，事情就开始崩坏了。  

把任务委托给 agents 当然没问题。好的 agent 任务有一些共同特征：  

它们可以被界定范围，使得 agent 不需要理解整个系统

循环可以被闭合，也就是说 agent 有办法评估自己的工作

输出并非关键任务，只是某个没人的生命或收入依赖于它的临时工具或内部软件

或者你只是需要一个橡皮鸭来碰撞想法------把你的想法与互联网的压缩智慧和合成训练数据碰撞一下

如果以上任何一点适用，你就找到了 agent 的完美任务------**前提是你这个人类是最终的质量关口。**   

Karpathy 的^\[7\]^ auto-research^\[8\]^ 用于加速你的应用启动时间^\[9\]^？很好！只要你明白它吐出来的代码根本没有生产就绪。Auto-research 之所以有效，是因为你给了它一个评估函数，让 agent 可以用某个指标（比如启动时间或 loss）来衡量自己的工作。但那个评估函数只捕捉了一个非常狭窄的指标。对于评估函数没有捕捉到的指标------比如代码质量、复杂度，或者在你的评估函数本身就有问题时的正确性------agent 会毫不在意地忽略掉。  

**重点是：让 agent 做无聊的事，那些不会让你学到新东西的事，或者尝试你否则没时间尝试的各种方案。** 然后你评估它给出的结果，把真正合理且正确的想法取出来，并完成最终实现。是的，当然，你也可以用 agent 来做这最后一步。  

他妈的慢下来，才是正道。给自己时间，想清楚你究竟在做什么、为什么做。给自己一个机会说，去你的，我们不需要这个。给自己设一个限制，规定每天你允许机器人生成多少代码，与你实际能 review 的量相匹配。

**任何定义你系统格局的东西------也就是架构、API 等等------都亲手写。**

也许用 tab 补全来找点怀旧感。或者跟你的 agent 做结对编程。待在代码里。

因为不得不亲手写出东西、或者一步步看着它被构建出来这个简单的行为，会引入摩擦，让你更好地理解你想构建什么，以及这个系统的「手感」。这就是你的经验和品味所在，而**这恰恰是当前 SOTA 模型尚无法取代的。**   

他妈的慢下来，承受一些摩擦，才能让你学习和成长。

最终的结果，是那些持续可维护的系统和 codebase------至少和 agents 出现之前我们的老系统一样可维护。是的，那些也不完美。你的用户会感谢你，因为你的产品现在令人愉悦而不是一坨糊弄。**你会做更少的功能，但都是对的功能。学会说不，本身就是一个功能。**   

你可以安然入睡，因为你清楚地知道发生了什么，你掌握着主动权。你的理解能力解决了 agentic search 的召回问题，带来更好的机器人输出，需要更少的修改。如果事情出了岔子，你有能力介入并修复它。如果你最初的设计不够理想，你能理解为什么它不够理想，以及如何将它重构成更好的东西。有没有 agent 辅助，都无所谓。  

这一切都需要纪律和自主性。  

**这一切都需要人类。**   

参考资料

\[1\]AI 导致的 AWS 故障：https://www.ft.com/content/00c282de-ed14-4acd-a948-bc8d6bdb339d

\[2\]「辟谣」：https://www.aboutamazon.com/news/aws/aws-service-outage-ai-bot-kiro

\[3\]90 天重置计划：https://www.businessinsider.com/amazon-tightens-code-controls-after-outages-including-one-ai-2026-3

\[4\]微软有多少代码现在是由 AI 编写的：https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/

\[5\]博文：https://blogs.windows.com/windows-insider/2026/03/20/our-commitment-to-windows-quality/

\[6\]AGENTS.md：http://agents.md/

\[7\]Karpathy 的：https://x.com/karpathy

\[8\]auto-research：https://github.com/karpathy/autoresearch

\[9\]加速你的应用启动时间：https://x.com/badlogicgames/status/2035469013480869912


[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxMDMxOTI2NA==&mid=2649107404&idx=1&sn=8a57aa2fcbad64c8ecb5903f6ced9bf1&chksm=821d465705c93fac0e63101a56f2959419b7d48e2bb82528793bf8eefd6b850e6bd00e5a23a6&mpshare=1&scene=1&srcid=0423vYL39NrioVpiHitjnnMJ&sharer_shareinfo=8b03d9184d96faba5f128c76513bfc7c&sharer_shareinfo_first=8b03d9184d96faba5f128c76513bfc7c)

