---
id: "7263427434026896374"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzUxMzUzNzUzMw==&mid=2247498714&idx=1&sn=71924ce49da857f3cf2536cbc8baaf09&chksm=f87f76fc0b96c52e1f5fa2ad1caded0eff89b02c85e0b4ba091ff4c65305835450d619716837&mpshare=1&scene=1&srcid=1203lAlLct5uUuJhnkucL8BX&sharer_shareinfo=7cda1ceaf89f8c3958c51de9ee603827&sharer_shareinfo_first=7cda1ceaf89f8c3958c51de9ee603827
author: "极客见识 AI Interface"
collected: 2024-12-03
tags: []
---

# AI Agent与UX的研究与分析

# AI Agent与UX的研究与分析

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzUxMzUzNzUzMw==&mid=2247498714&idx=1&sn=71924ce49da857f3cf2536cbc8baaf09&chksm=f87f76fc0b96c52e1f5fa2ad1caded0eff89b02c85e0b4ba091ff4c65305835450d619716837&mpshare=1&scene=1&srcid=1203lAlLct5uUuJhnkucL8BX&sharer_shareinfo=7cda1ceaf89f8c3958c51de9ee603827&sharer_shareinfo_first=7cda1ceaf89f8c3958c51de9ee603827)极客见识 AI Interface


![](https://image.cubox.pro/cardImg/18sitckllothfkvn8c8sv36qsne1nwx2bp6jxk6jtr3ftzf5m?imageMogr2/quality/90/ignore-error/1)

**未来交互趋势**

Ai交互设计学习，了解最前沿的人机交互知识

11篇原创内容

<br />

公众号  

，

Paz Perez（在 Google 从事人工智能的设计师）近期做了一个关于 AI Agents 研究，Paz Perez 将AI Agents 视为角色，引入了 Agent Computer Interaction 。

我总结了几个重要的观点：

* **AI Agent的角色转变：** AI Agent从工具转变为数字环境中的积极参与者，需要被设计和考虑。

* **Agent Computer Interaction：** AI Agent可以独立浏览界面并执行复杂任务，开启了一个新的交互时代，即Agent与计算机的交互。

* **AI Agent的定义和能力：** Google I/O将AI Agent定义为能够推理、规划、保留信息和提前思考多个步骤的智能系统。AI Agent能够直接与图形用户界面交互，控制光标、输入输入，并像人类用户一样浏览应用程序。

* **AI Agent与软件交互的两种方法：** 直接API集成（工具使用）和可视化界面交互（人类工具）。

* **为AI Agent设计体验：** 用户体验设计师需要扩展他们的实践，考虑AI Agent作为新参与者的需求和能力。

虽然用户体验社区已迅速将大型语言模型作为设计工具，但我们在很大程度上忽视了它们更深远的影响。现在，随着 AI Agent 融入我们的数字产品中，我们面临着根本性的转变：这些系统正在从工具演变为我们数字环境中的积极参与者，我们需要为它们进行设计。

AI Agent 正在成为一类新的用户，它们可以独立浏览我们设计的界面并代表我们执行复杂任务。这标志着一个新交互时代的开始，即 Agent 与计算机交互，其中用户体验不仅包括人机关系，还包括 AI Agent 的体验。

不可否认的是，人类仍然是这一新动态不可或缺的一部分，提供监督和指导。不过，AI Agent 现在应该被视为具有独特需求、能力和目标的不同用户角色。这需要为人类和 Agent 设计体验，设计适合两者的界面，并确保他们拥有有效运作所需的资源和信息。


**01 了解 AI Agent**

Google I/O 将 AI Agent 定义为能够推理、规划、保留信息和提前思考多个步骤的智能系统，同时在人类监督下跨各种软件和系统运行。

其他公司可能对其定义不同，但它们都具有相同的基本概念：能够提前思考多个步骤并在独立工作时保留上下文的 AI。这就像拥有一个能够真正预测您的需求并主动解决问题的数字助理。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FRVXAjXCKhtyxkZqMMGprBoVrJlnfmAEhyY4IKQ9Ry3icWfv9JqJDxMneWicUP5hvCBXqPCfgojTtsKmrkib0hOribg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

图片来自 Google I/O


虽然早期的 AI Agent 仅依靠 API 与其他系统交互，但前段时间的突破，尤其是 Claude 等模型开创的"计算机使用"（Computer Use）方面的突破，已经开启了 Agent 的新水平。这些高级代理现在可以直接与图形用户界面交互，控制光标、输入输入，并像人类用户一样浏览应用程序。这让它们能够前所未有地访问基于浏览器的产品，使它们能够以我们从未见过的自主性和复杂程度执行任务。

在这个 Agent 计算机交互的新时代，AI 团队必须在两种方法之间做出选择，以实现 AI Agent 与软件交互：

1. **直接 API 集成或"工具使用"：** 使用函数调用和 API 以编程方式与系统交互。这通常更有效，因为它避免了渲染可视化界面的开销。但是，API 的质量和覆盖范围可能会有所不同。

2. **可视化界面交互或"人类工具"：** 让人工智能代理通过图形用户界面与软件交互，就像人类一样。虽然速度可能较慢，但这种方法提供了更大的透明度，并允许人类更好地监控和控制人工智能的行为。

API 集成可能非常适合处理大量、定义明确的任务，因为速度和效率是最重要的。可视化界面交互可能更适合需要仔细人工监督的任务，提供更高的透明度和控制力。用户体验从业者和跨职能合作伙伴面临的关键挑战是确定每个用例最有效的交互方法以及与最终用户的关系。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FRVXAjXCKhtyxkZqMMGprBoVrJlnfmAEhBmZ0FbKALVwnoUQV2cKpQG1n7gLcKEO5clsh9tJ2WicDmN5ic6SJ55Og%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Anthropic 的计算机使用


**02 为 AI Agent 设计体验**

随着 AI Agent 逐渐成为我们数字产品的活跃用户，用户体验设计师需要扩展他们的实践以考虑这些新参与者。就像我们研究人类用户的需求一样，我们现在必须了解他们的能力、他们需要什么才能有效运作，以及他们如何实现指定的目标。

虽然 Agent 最终是为了满足人类的意图，但它们通常在复杂的网络中工作，在网络中它们与其他代理交互以完成任务。例如，一个 Agent 可能会处理另一个 Agent 用来提出建议的数据，所有这些都是为了满足人类的原始请求。这创造了设计师必须考虑和支持的新交互层。

在我们为人类用户创建角色的同时，我们现在应该为 AI Agent 开发角色。这些角色应该捕捉 Agent 行为的细微差别、其优势和局限性，以及随着技术和环境的发展而不断发展的能力。这将使我们能够设计针对 Agent 工作流程优化的界面和交互，就像他们只是人一样。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FRVXAjXCKhtyxkZqMMGprBoVrJlnfmAEhzmKnumg9Xf1Clk6FGfHXd7f1QTJdW2gkBXibvlxiau28V5FC114kRHHg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Agent persona（修改的 FigmaJam 模板）

准备采用新的研究方法，例如对不同的界面设计进行 A/B 测试，以确定哪种设计最能支持 Agent 性能。虽然 AI 系统可能没有感知能力，但它们具有动机，可以推理、计划和适应。

这个新时代给我们提出了一个基本问题：界面应该针对人类、Agent 还是两者进行优化？当我们探索这个未知领域时，答案仍然难以捉摸。关键在于认识到 AI Agent 不仅仅是工具，而且是拥有权利的用户，探索周到的设计考虑和对代理独特需求的细致理解。

当移动设备打断桌面世界时，它首先被视为桌面体验的缩小版。然而，我们很快就释放了移动设备的独特潜力，它以一种以前难以预测的方式改变了世界。同样，我们现在正通过现有范式的视角来看待人工智能的发展，时间将告诉我们新的体验将如何以我们意想不到的方式形成。很明显，我们似乎正走在从网络应用到移动应用的轨道上，现在正走向一个由 AI Agent 塑造的未来。

**03 塑造人工智能思维**

大型语言模型 (LLM) 是 AI Agent 背后的"大脑"，赋予它们智能和推理能力。但用户体验设计师在塑造这些 LLM 方面发挥着至关重要的作用，他们的作用不仅限于界面设计，还影响着代理行为的核心。

在"模型设计师的崛起"中，我指出，作为设计师，我们需要参与塑造 AI 模型。我们对用户需求和心理模型有着独特的理解。这种专业知识对于制定有效的提示以引导 LLM 实现预期结果非常有价值。通过与工程师密切合作，开发符合用户意图的系统提示，我们可以确保 AI Agent 为人们提供相关且有意义的体验通过与工程师密切合作，开发符合用户意图的系统提示，我们可以确保 AI Agent 为人们提供相关且有意义的体验


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FRVXAjXCKhtyxkZqMMGprBoVrJlnfmAEhp9Da73Qa2DvASeP0yr2XwxaUVstiaE0UdyB904hfcENzwnyvUBCN2icQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

来自"模型设计师"文章的 AI 模型训练和用户体验参与

此外，UX 设计师应积极参与制定评估代理绩效的策略，并利用用户反馈来改进 LLM 行为。这涉及建立一个数据飞轮，以不断提高代理理解和响应用户需求的能力。

***关键要点是：为 AI Agent 进行设计需要转变思维方式。我们不仅要为他们打造产品，还要积极塑造代理本身，通过仔细提示和持续反馈来影响他们的智力和行为。这代表了 UX 的新领域，我们的专业知识延伸到了 AI 的核心。***

**04 让人类参与其中**

虽然为 AI Agent 进行设计带来了令人兴奋的新挑战，但我们绝不能忽视我们的最终目标：增强人类体验。人工智能应该服务于人类，我们的设计工作必须优先考虑人类的需求和价值观。

控制至关重要。用户体验从业者必须仔细考虑如何让用户在与人工智能互动时拥有自主权。这包括设计清晰的权限授予机制、提供有关数据访问的背景信息，以及为那些不愿意与 AI Agent 互动的用户提供退出选项。通过用户控制建立信任对于成功采用代理驱动的体验至关重要。

透明度同样至关重要。用户需要清楚地了解 AI Agent 如何利用其数据、与其工具交互以及与其他代理协作。在涉及来自不同公司的多个代理的场景中，用户应该能够了解参与者，并能够选择允许哪些实体进入其数字生态系统。

幸运的是，我们可以利用现有的用户体验框架来应对这一复杂局面。例如，系统设计提供了有价值的工具，可以可视化 Agent 驱动生态系统中的复杂关系，同时保持以人为本的视角。通过采用服务设计中常用的蓝图等映射技术，我们可以有效地表示人类、Agent 和产品之间的相互作用，突出可见性和控制的界限。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FRVXAjXCKhtyxkZqMMGprBoVrJlnfmAEhrgQoggPapzl6841Evmsczxz5uS4YQXJAF3uM93iaYGc3UtBzyYLGjVw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

Agentic 体验地图草稿（修改的 FigmaJam 模板）

这些修改后的蓝图，我们或许可以称之为"Agent 体验地图"，不仅应该描绘交互流程，还应包含与代理训练和评估相关的元素。这种整体观点将使我们能够设计出既强大又值得信赖的系统，确保人工智能真正以人为本。

**05 总结**

我们正在进入数字设计的新阶段，其中 AI Agent 正在成为我们系统的活跃用户，而不仅仅是其中的工具。这种转变要求用户体验设计师扩大他们的视野，考虑人类和 AI Agent 如何与界面以及彼此交互。

尽管人工智能技术的快速发展令人感到不知所措，但这一领域仍处于早期阶段。用户体验设计的核心原则仍然很有价值------我们只是将它们扩展到涵盖人类用户和人工智能用户。这为设计师提供了一个独特的机会来塑造 AI Agent 如何与系统交互并满足人类需求。

UX 的未来在于理解和设计这种代理计算机交互。现在在这个领域发展专业知识的人将有助于确定未来几年的最佳实践。


*** ** * ** ***

*以上研究的资料来源：*

* *Anthropic------ 介绍计算机的使用*

*https://www.anthropic.com/news/3-5-models-and-computer-use*

* *NNg ------ 服务蓝图*

*https://www.nngroup.com/articles/service-blueprints-definition/*

* *潜在空间播客 ------ 语言代理：从推理到行动*

*https://www.youtube.com/watch?v=8t65bss7U74*

* *认知 ------ Devin简介*

*https://www.cognition.ai/blog/introducing-devin*

* *《麻省理工技术评论》------谷歌Astra是其首款万能AI Agent*

*https://www.technologyreview.com/2024/05/14/1092407/googles-astra-is-its-first-ai-for-everything-agent/*

* *Alex Klein ------ UX 的代理时代*

*https://uxdesign.cc/the-agentic-era-of-ux-4b58634e410b*

*** ** * ** ***


![](https://image.cubox.pro/cardImg/50r95eswjiilar456ewar740cm1ovxod6ltngilhtxi82os6r5?imageMogr2/quality/90/ignore-error/1)

**全球AI趋势**

每日推送全球AI资讯

12篇原创内容

<br />

公众号  

，

![](https://image.cubox.pro/cardImg/pi87iky0293iato2gs1jj3euunpou279aqnx3mql9tc6rh0zf?imageMogr2/quality/90/ignore-error/1)

**科技早读**

全球科技侦察兵，每日科技早报推送！

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FxqClUvyGjq3W7jiaib6pVsCIteM7ib1mOmiaZkKKl8Or7tJQNtnqlKXcsU1LAzDqGXUUuoxZAiaNSMQSJCb6MNiblabw%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**Agentic**

AI Agent 智能体来了

<br />

公众号  

，


[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzUxMzUzNzUzMw==&mid=2247498714&idx=1&sn=71924ce49da857f3cf2536cbc8baaf09&chksm=f87f76fc0b96c52e1f5fa2ad1caded0eff89b02c85e0b4ba091ff4c65305835450d619716837&mpshare=1&scene=1&srcid=1203lAlLct5uUuJhnkucL8BX&sharer_shareinfo=7cda1ceaf89f8c3958c51de9ee603827&sharer_shareinfo_first=7cda1ceaf89f8c3958c51de9ee603827)

