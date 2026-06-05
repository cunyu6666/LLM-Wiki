---
id: "7461808426004254517"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkxMzUyODQ3OA==&mid=2247484208&idx=1&sn=5597ddda7572d7da8080ae5a920ec49e&chksm=c0d4c3810ba2cbc24122fcb111e5f7670ee665f427a8fa97a2d736c12194cfb258f1a44d141e&mpshare=1&scene=1&srcid=0603xNSS2yWLPSxo3bCcBWwA&sharer_shareinfo=1056ccceb0041970eadbb5418ded2ada&sharer_shareinfo_first=1056ccceb0041970eadbb5418ded2ada
author: "nimbus AI产品银海"
collected: 2026-06-03
tags: []
---

# Agentic Workflow：AI重塑了我的工作流

# Agentic Workflow：AI重塑了我的工作流

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxMzUyODQ3OA==&mid=2247484208&idx=1&sn=5597ddda7572d7da8080ae5a920ec49e&chksm=c0d4c3810ba2cbc24122fcb111e5f7670ee665f427a8fa97a2d736c12194cfb258f1a44d141e&mpshare=1&scene=1&srcid=0603xNSS2yWLPSxo3bCcBWwA&sharer_shareinfo=1056ccceb0041970eadbb5418ded2ada&sharer_shareinfo_first=1056ccceb0041970eadbb5418ded2ada)nimbus AI产品银海


![](https://image.cubox.pro/cardImg/4p3mlet033q60if93brcy2k6uob241yu7e1ph61vkq91391p5x?imageMogr2/quality/90/ignore-error/1)

**AI产品银海**

银海，专注于AI领域产品应用分享。

222篇原创内容

<br />

公众号  

，
>
>
> "Reshape your workflow with AI."
>
> 在Agentic Workflow的这件事情上，我先完成了自己的工作流重塑。
>
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMeRD2t9HMzW6SGjlBKWkBFELfC9ichDJw5n5DShDPsJCicZpdx3R0odAg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

近期在「特工宇宙」分享了一场关于Agentic Workflow主题的内容，现在同步分享给大家一些关于个人在使用AI Agent Workflow上的思考、AI-Native应用「Pailido｜AI拍立得」创建的初衷和实现流程，在个人工作流重塑上分享了一些体悟。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaM8aUWtZuEclSoNIylnBQeXrlR5ftjFDDJgWe1YY5JRnRuUln6ZrlJ6A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

本次分享大纲整体围绕着AI Agent和Agentic Workflow从"认识、定义、应用、偏见、实践以及延伸"进行展开，正式拉开「仰望星空，脚踏实地」的序幕。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMkXPSyiapT3lKd9JvMur36xO5JUsKdXicR5WnC106k9fibeU3dwgqFzl7Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

在今年的 4 月初，吴恩达老师在美国红杉做了一场演讲，介绍了 4 种主要的 Agentic Workflow 设计模式。

**Reflection（反思）：** 让 Agent 审视和修正自己生成的输出。

**Tool Use（工具）：**LLM 生成代码、调用 API 等工具进行操作。

**Planning（规划）：** 让 Agent 分解复杂任务并按计划执行。

**Multiagent Collaboration（多智能体协同）：** 多个 Agent 扮演不同角色合作完成任务。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMBkia4ibMEcoBwj8zbYwCbg9hXj2cspSupj84hDSAMiaCBtNXibMwaFJUvw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

**Reflection**

反思在根本上其实是一个博弈的过程：如果你让大模型写一段代码，它会立刻给你反馈。这时你可以将它输出的代码片段再输入回去，让大模型仔细检查代码的准确性和结构规范性，并给出评论。然后，你可以将这些反馈结果再次输入给大模型，它可能会输出一个比第一版更好的代码，如果有两个 Agent：一个负责 Coding，另一个负责 Code Review，效果会更佳。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMg87SRYWiaZBIRuF1R2PH5GJ2RNibej0wbpPLribnEk2cIMHny4q03KWqg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

**Tool Use**

如果大家使用 Kimi Chat 来查询某个问题，你会发现它会在互联网上检索相关内容，并基于检索结果进行总结分析，最后给出结论。这其实是大模型利用「网页搜索」工具的一个典型例子，同时你也会看到PPT中介绍了非常多的不同领域类型的工具，它其实是为大模型在获取、处理、呈现信息上做额外的补充。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMwfgF7yiaCQjMsHzCWK6eSDtbExkXQSc57eZBQPu6FGfB13ygYJypSuQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

**Planning**

Agent 通过自行规划任务执行的工作流路径，面向于简单的或者一些线性流程的运行。比如下图中：Agent 会先识别男孩的姿势，并可能找到一个姿势提取模型来识别姿势，在接下来要找到一个姿势图像模型来合成一个新的女孩图像，然后再使用图像理解文本的模型，并在最后使用语音合成输出，完成这个流程任务。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMSv8k5cN2EevQJjLgz4MQuKxvdaVkEP0YQ8uv1pqEWKtALGic3bZz90g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

**Multiagent Collaboration**

吴恩达通过开源项目 ChatDev 进行举例，你可以让一个大语言模型扮演不同的角色，比如让一个 Agent 扮演公司 CEO、产品经理、设计师、代码工程师或测试人员，这些 Agent 会相互协作，根据需求共同开发一个应用或者复杂程序。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMw4ur2PVuE8rrMc4l8j1CqoK1LmVYRKLbRickibrY2HweoDghFqqCMxicw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)

**AI Agent 基本框架**

OpenAI 的研究主管 Lilian Weng 曾经写过一篇博客叫做《 LLM Powered Autonomous Agents 》，其中就很好的介绍了 Agent 的设计框架，她提出了"Agent = LLM + 规划 + 记忆 +工具使用"的基础架构，其中大模型 LLM 扮演了 Agent 的"大脑"。

* Planning（规划）

主要包括子目标分解、反思与改进。将大型任务分解为较小可管理的子目标处理复杂的任务。而反思和改进指可以对过去的行动进行自我批评和自我反思，从错误中学习并改进未来的步骤，从而提高最终结果的质量。

* Memory（记忆）

分为短期记忆和长期记忆。其中短期记忆是指的将所有的上下文学习看成是利用模型的短期记忆来学习；而长期记忆是提供了长期存储和召回信息的能力，它们通常通过利用外部的向量存储和快速检索来存储和召回信息。

* Tools（工具）

通过学会调用外部不同类型API来获取模型（通常在预训练后很难修改）中缺少的额外信息，代码执行能力，访问专有信息源等（例如获取此时此刻的天气、联网网搜索等）

* Action（动作）

根据上述大模型结合问句（Query）、上下文的规划（Context）、各类工具，最终大模型才能决策出最终需要执行的动作是什么。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMHA1TicXhQ2T5qcTQvGIkUj36M59ul4IibyTeblmZlT0EEZgI2PB00fqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D8)

Agentic Workflow 解决什么问题？我认为是可以从从提升效率、提高质量、节省时间的角度上进行思考。好比一台"印钞机"，按照指定好的流程重复着机械性的活动，但是它在源源不断的产生价值。

Productivity （效率） = 产生价值的速率

Agentic Workflow 通过将一个复杂的任务分解成较小的步骤，在整个过程中中融入了更多人类参与到流程中的规划与定义。它减少了对 Prompt Engineering 和模型推理能力的依赖，提高了 LLM 应用面向复杂任务的性能，更丰富、更精确。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMOicxjTk7leu0csq7VQ3x0nz3rNTsMuBc1Qkc7chCicFqhEaaVoqQicVDw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D9)

下面是Coze（扣子）平台上的工作流编排器的示例，这个话其实是一个抽卡游戏的流程，你可以看到在整个工作流中间会有很多节点前后之间有节点以及连线，然后每个节点之间它是通过不同的定义，比如说图片处理工具，或者说是通过多模态模型进行图片理解工具等等其他各种各样的工具组合而成。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMhiaGibSKmVjPcTV23DFkLfAtFj2MX0Rq5szIQ0N0EjDnK7T3icgH4nAOQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D10)

单Agent模式下，在这里可以看到一些例如"技能"、"知识"、"记忆"、"对话体验"等等点，其实在我们上面这个多个Agent和workflow编辑器里面里面也有这类工具。它是将一整套工作流组合起来，每个工具在每一个节点里面，它执行了一个任务。大家感兴趣的话可以去体验一下，可以在自己工作流中整个使用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMa0TZnXXdoPqgG3o2lEZnTJxlgc8Y1lfUSD0bfvvnibtKJWhUibj2vibwg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D11)

**Agentic Workflow 的"套娃"设计**

体验过不同 Agent 流程编排开发平台的同学会发现，workflow 会成为一个组件被调用，同时 workflow 中又能够嵌套新的workflow，实际上不管是基础节点、插件工具、LLM、逻辑条件处理等，都实际上是一个以输入、输出的组装的模块，不同的组件之间通过连接构成一个更大的模块。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMlr2eRKGjbFfRkZlJ4FTmpoCW1RvIC0zUemmbz4Es9ibSKFSkBwjagyw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D12)

即便看上去Agentic workflow解决了很多问题，但是实际上来说：大模型根源的"不太聪明"，是加上workflow也解决不了的。因为工作流它解决的并不是意图理解准确率的问题，而是在流程上的被干预后的可控性，吴恩达老师也在红杉的演讲上提到提升大模型本身质量依旧十分重要。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaM1u7rSVcWE1K5odJzdooeWibuIYZstkGfxGGzoxPKp0k3om76Xh8MT0w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D13)

下面也会带着大家重新看一下工作流其实一直都有出现，目前的工作流编辑器是将Agent的处理流程可视化和可控化了。  

**LangGPT 提示词框架工作流设计**

与传统的 Prompt 从输入直接到输出的映射方式相比，LangGPT 提示词框架应用了CoT（Chain of Thought）完成了从输入到思维链再到输出的映射，即\<input------\>reasoning chain------\>output\>。

最后你会发现浓缩成一句话可以解决模型在规划过程中的路径拆解，CoT的思维："Let's think step by step."（让我们一步一步思考）

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMVGU3FuMjiaTCq1YW14lrXicxDV4AaoboWc2pN1kyqY0td2juibvJYSMFA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D14)

**RPA 的工作流设计**

RPA其实很早就已经出现，就是做工作流编排领域。流程机器人（RPA）软件的目标是使符合某些适用性标准的基于桌面的业务流程和工作流程实现自动化，一般来说这些操作在很大程度上是重复的，数量比较多的，并且可以通过严格的规则和结果来定义，现在越来越多的RPA软件带上了LLM。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMliahzibYUe5UiaydLdxZU8zGQVXSgVYFfcEibqHRQQu6u8iaxl6wI0naicIQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D15)

**ComfyUI 的工作流设计**

近期出现的ComfyUI 是将开源绘画模型 Stable Diffusion 进行工作流化操作模式，用户需要在流程编辑器中配置出每一个的pipeline，并通过不同节点和连线来完成模型的操作和图片内容生成，提高了流程的可复用性，降低了时间成本，同时它的 DSL 配置文件还支持导出导入。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMMItVICv3U70R4Ko2uoBwMlyicAnqVnHiadO7DogPcUKHYJeCoibMSq7KQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D16)

**Dify.AI 可被复制的工作流设计**

在 Dify.AI 中，我很兴奋的看到它的工作流设计语言跟 ComfyUI 会有一些相似之处，都是定义了一套标注化的DSL语言，并且非常方便的可以使用导入导出的功能进行工作流的复用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMicpuMUw4YvEiaG0svqMDTl7aianhLvnR3qWXWW2gk2rpE69vT1exHK3PQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D17)

**模仿式工作流是最快的学习方法**

Large Action Model 采用称为"通过演示进行模仿"的技术。检查人们在单击按钮或输入数据时如何与界面互动，然后准确地模仿这些操作，他们收集知识并从用户提供的示例中学习，使他们更能适应进一步的变化并能够处理不同的任务。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMDBO2nFc9KH4vjjEW7ZicERuAPT1kRZA1YghKfib8zU8NWSE1WpybeEMQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D18)

但是，有没有想过一个问题：Agentic Workflow看起来十分美好，但是使用的用户究竟有多少呢？我看了很多Agent商店，通过工作流创建的应用目前来看还是比较少的（可能是出现周期、工作流使用的上手难度等等一系列因素导致），此外Agentic Workflow似乎在复杂流程上的开发又并不是那么稳定可靠。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaM9oIty4a7umiaSrtBwCdUMhibQwlue6VSf1GTKvYFwO0gKdIWVzlnh3zA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D19)

**Idea Time：通过自然语言创建工作流**

复杂的工作流搭建怎么会如此麻烦...这似乎跟我我理想中的Agentic Workflow并不太一样！有没有一种更加方便高效的方式，让我能够在短时间内创作一个符合我预期的Agentic Workflow原型？有了，通过自然语言来构建DSL并还原工作流。

我在之前就比较喜欢使用自然语言描述，然后使用Mermaid语法进行创建流程图表，其实DSL也是可以遵循一套约定俗成的规范进行创作。  

我认为可以通过口喷需求的方式，在0-1的时候辅助我快速生成一个看上去还不错的工作流程，然后我再修修改改，这会降低用户上手的门槛。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMmPMRbpyGHE89viaNuhbAdW6qZXf1Lo9EEU7B9SNpyBFT62cwuusmiaHg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D20)

一个小思考题，Agentic Workflow该给谁用？

之前在讨论Agentic Workflow的可用性观点，有人给我说了这么一句话："研发看不上，产品看不懂，小白不知所云。"

目前我觉得Agentic Workflow拿来做MVP的产品测试是非常好的一个途径，能够在短时间内通过低代码或者零代码的方式进行创作一个小而美的应用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMZiafpDBGkhUOGjkDA0fWEFVMfzhzoxrXbmsQtAudjX5Ja3sPXkgqQFQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D21)

我的AI-Native应用就是这么玩的。

**Pailido｜AI 拍立得**

这是一款文案快速生成的 AI-Naitive 产品，各个场景由 AI Agent 驱动，仅需选中场景后点击拍摄即可快速生成对应文案。它的服务端可以是使用类似Dify.AI、Coze这种在线编辑好一个Agent应用，然后再通过API的方式进行集成，你仅仅需要关心你的前端、用户输入、你的输出反馈就可以了，打磨好一款小而美的产品。

使用多模态模型，理解图片特征和输出场景期待，搞定小红书文案、外卖点评写作、闲鱼商品发布文案...真的太快了！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMib2kJ1eFibIOQh5pt3vTQga9xzugz9mFwYC6PmE8sIwmYJGO66CWicUMQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D22)

所以有个问题要问问诸位了：

Reshape your workflow with AI ?

or

Reshape your AI workflow ?

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMbQuNdk4BrEfeic50NdXGKKXj8ABHXHL0nmIfNVaicZ3Z4F6ZDtuOfEug%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D23)

**AI 与人的协同关系**

生成式 AI 的人机协同分为 3 种产品设计模式：Embedding（嵌入式）、Copilot（副驾驶）、Agent（智能代理），在这 3 种模式下，人与 AI 的协作流程也是有所差异。

* Embedding 模式：人类完成大多数工作。

* Copilot 模式：人类和AI协同工作。

* Agents 模式：AI完成大多数工作。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMcNicxhtdTiaCE7ibTK70PhKrnP0W2xxygGkzibb3kBK7nGoicwSyt1YKicxw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D24)

**Agentic Workflow驱动角色工作流变革**

使用Multiagent Collaboration的方法，让不同角色的 Agent 按照根据任务要求自主规划选择工具、流程进行协作完成一件任务。

我作为一个产品经理角色，我的诉求很简单，需要完成某一个产品功能设计，这个时候通过Agents拆解成多个独立的任务，然后遵循不同的工作流，最后给我生成一份在大体上符合我期望的输出结果，我再修修改改就能够达到可用的阶段了。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaM5ho54KOia5Z7Na2DWFaW3FibywIcOeMqgyJzzy888cb0ItN2jFmUAXWw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D25)

所以，我从原子能力层重新思考，面对这个快速变化的时代，我该如何去重塑我自己的工作流，以不变应万变呢？  

我抽象化拆解了大模型的一些底层能力，例如：翻译、识别、提取、格式化等等，其实所有的一些都会围绕几个词"输入"、"处理"、"输出"、"反馈"。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMAibNpYMt0KH7nTpAvsltgjbfZSJGSDTBXMHVt8fVXynVUw82eZbt9NA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D26)

"输入"、"处理"、"输出"、"反馈"构建了我最底层的信息处理逻辑，我把它比作四个齿轮，齿轮之间通过不同的衔接工具逐步推动运转，从需求作为输入、结果作为输出，围绕着信息加速，不断驱动我向前。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMPVKT567H4g7ebYE9gUE0WAwHrtg4IoSPvgKribMQwGwKZtQks1yeChg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D27)

**重塑获取信息的方式**

搜索引擎作为互联网基础设施，同时也是互联网的入口，对于用户而言，从解决问题出发，搜索引擎和基于大模型的聊天机器人的目标从根本上是一致的。自 2022 年底 ChatGPT 发布，其通过问答形式被认为将对传统搜索引擎带来颠覆。

近期出现的各类AI搜索引擎，类似perplexity.ai、metaso、360搜索、ThinkAny等等，都是在不断颠覆传统的搜索引擎。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMzDzMY95SmSCoaPtyITKVfCibnkStprwAo9jRiaIiabBZibe37qMzxCwJpQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D28)

**辅助高效的处理信息**

阅读完一份 10 万字的 PDF 研究报告需要多久？这份报告主要讲了什么内容？有没有我要关注的点？

智能摘要是目前我用的超顺手的一个功能，能够辅助我快速的筛选信息，什么值得看，什么不容错过，真正的实现信息的降噪。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMZ8YShicbMiavAzoibtFUwWs8zQlabVP5q8FyTTMwRTfFEicN6wH6CYtHHw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D29)

**信息表达更简便**

放在以往很难想象，如果要实现下面这俩张图，可能会设计一系列的思考、草稿、理清逻辑等等流程。

现在用自然语言描述一句话就给你生成了这样美观可用的图片，极大的降低了不同角色的创作门槛和周期，是真的简便。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMnj8NGZpRHOSTem5x1k8NuMzn4BLKGiaElAzAffEiaKK2dVdPAVsMOL3Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D30)

那么新型的产品设计方式也就出现了，在我原来的工作流中，我作为一名产品经理，我会开始使用AI去重新构建我的工作流：使用 AI 进行搞定用户画像、使用 AI 进行竞品调研、使用 AI 设计产品测试用例、使用 AI 绘制产品功能流程图...真的太多了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMNjh0sibTRFmtPHsyKT4ctJeTwhhcUGdw60IYvqyHHQlfTPaG1DoqJgw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D31)

虽然我也推荐了一些我自己的工作流上使用的产品，但是我比较建议的是：每个人都是独特的个体，应该先摸清楚自己的日常工作流是怎么样的，然后通过每一个工作节点线索，去找到适合你自己使用的工具。

就好比，我现在初出茅庐，手上握着+1攻击力的武器，+1的防御装备，这不影响我去打怪升级这个事情，假如你找到了一件合适自己的武器，它可能是+1000攻击力，你换上就好了，是能够快速的在你原来的这套工作流里进行战力升级。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMGnVR7oBaLXYYb8ljUxiasBnrNm9Y9d2YsuTyYUYJn4wDgv4KicmcaBnQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D32)

关于Agent的未来，我只想说：曾被认为的异想天开的想法，都可能会是 AI Agent 的未来。AI Agent我们其实可以理解为一个技术浪潮中不断前进的新名词，而技术迭代会不断向前。

我很惊讶的发现：曾经五年前躺在我手机备忘录里的一些在当时不可能实现的想法，在如今时代也逐一被验证。

所以，还有什么不能想的呢？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMXvV2icSKbDy0VJ1lCdk2KgQSs7AfK9Jian1blZzdXq988LicZBSTib7rWA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D33)

脚踏实地，仰望星空。

Agent的未来是一个浩渺的宇宙，行业的Know-how是每一个人在短期内不可被替代的固有知识资产，你可能会说我可以通过一系列的方法论去获取到很多行业信息，但是非常多的行业潜规则，就像冰山一样，你可能只看到了表面的一些内容，冰山下的不可被观测的，也是这个时代个人的竞争力。

毫无疑问，LLM会有更低的成本、推理处理速度更快、支持多模态全面接入、会有更多AI-Native应用开始诞生...

我肯定是，AGI的时代会离我们越来越近了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaMEBIHkJVjjzYic1JIENkTQKjkVJfWBkGqFd6KhqlXe1RMj937vIDpxLw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D34)

感谢你看到这儿，如果你觉得不错，欢迎点赞分享关注我哈哈，我们下期再见。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaM1ajSxf3Eo17Bgz5xwfiaCb1jlkQFMpVWql877UKRFA5aOn3RyaOibYAA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D35)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FGkSBRc9GpQ7LmLw9beRB1Ix9lUGTsMiaM8zo3eyrRBxNB8LxgdHJSZj5M0rEZ854UhUUkSGL0cs0pk7ibQ4Yt72g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D36)

获取完整内容文件和视频回放

请在公众号后台回复"工作流"

© THE END

🤪 只想整活做点有趣的事儿

欢迎点击下方公众号关注我

觉得我的内容还不错，顺手点个赞、分享、在看

都是对我最好的认可，谢谢您！

![](https://image.cubox.pro/cardImg/4p3mlet033q60if93brcy2k6uob241yu7e1ph61vkq91391p5x?imageMogr2/quality/90/ignore-error/1)

**AI产品银海**

银海，专注于AI领域产品应用分享。

222篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkxMzUyODQ3OA==&mid=2247484208&idx=1&sn=5597ddda7572d7da8080ae5a920ec49e&chksm=c0d4c3810ba2cbc24122fcb111e5f7670ee665f427a8fa97a2d736c12194cfb258f1a44d141e&mpshare=1&scene=1&srcid=0603xNSS2yWLPSxo3bCcBWwA&sharer_shareinfo=1056ccceb0041970eadbb5418ded2ada&sharer_shareinfo_first=1056ccceb0041970eadbb5418ded2ada)

