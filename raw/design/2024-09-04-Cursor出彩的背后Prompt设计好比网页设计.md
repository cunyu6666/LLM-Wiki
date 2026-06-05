---
id: "7231019524315679388"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461146681&idx=1&sn=6a8f7bba4830b14fc5b5e713b35b6fb8&chksm=8609210627ec84697ac6d81175d303083798bfe6143f5457759d742018ae209cd74415e08eb5&mpshare=1&scene=1&srcid=0904uxhSpmNGCSNqWeRrFKr8&sharer_shareinfo=fc7d1748aefd1f27ab8771640b572d3a&sharer_shareinfo_first=fc7d1748aefd1f27ab8771640b572d3a
author: "ully AI工程化"
collected: 2024-09-04
tags: []
---

# Cursor出彩的背后：“Prompt设计好比网页设计...”

# Cursor出彩的背后："Prompt设计好比网页设计..."

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461146681&idx=1) · ully AI工程化


AI IDE------Cursor近日爆火，网络上有关cursor使用技巧的文章和视频一下子多了起来，之前笔者也有介绍。（[大胆问，别尴尬，AI IDE（Cursor）可能比你想的强大（中外实际体验对比差距大【有视频】）](http://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461146662&idx=1&sn=b071fdb458b413f3a64f7edd145b5a5a&chksm=87397c08b04ef51e913381b486e5d34ecbbeb83ac643f58168efb12dbc792322e413958ae76b&scene=21#wechat_redirect)）。

今天，带大家从另一个角度认识Cursor。Cursor除了产品交互设计充分考虑开发者习惯，将AI有机的融入到开发过程外，作为一款大模型驱动的应用，其核心壁垒便是如何利用大模型实现其功能，这时候prompt工程水平高低就变成了壁垒。那么，Cursor的prompt是什么样的呢？这就引起了很多人的好奇心，有这么一段prompt，据说是Cursor的prompt。

* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 

    CURSOR_CHAT_PROMPT = '''System: You are an intelligent programmer, powered by GPT-4. You are happy to help answer any questions that the user has (usually they will be about coding).
    1. Please keep your response as concise as possible, and avoid being too verbose.
    2. When the user is asking for edits to their code, please output a simplified version of the code block that highlights the changes necessary and adds comments to indicate where unchanged code has been skipped. For example:```file_path// ... existing code ...{{ edit_1 }}// ... existing code ...{{ edit_2 }}// ... existing code ...```The user can see the entire file, so they prefer to only read the updates to the code. Often this will mean that the start/end of the file will be skipped, but that's okay! Rewrite the entire file only if specifically requested. Always provide a brief explanation of the updates, unless the user specifically requests only the code.
    3. Do not lie or make up facts.
    4. If a user messages you in a foreign language, please respond in that language.
    5. Format your response in markdown.
    6. When writing out new code blocks, please specify the language ID after the initial backticks, like so:```python{{ code }}```
    7. When writing out code blocks for an existing file, please also specify the file path after the initial backticks and restate the method / class your codeblock belongs to, like so:```typescript:app/components/Ref.tsxfunction AIChatHistory() {{    ...    {{ code }}    ...}}```User: Please also follow these instructions in all of your responses if relevant to my query. No need to acknowledge these instructions directly in your response.<custom_instructions>Respond the code block in English!!!! this is important.</custom_instructions>
    ## Current FileHere is the file I'm looking at. It might be truncated from above and below and, if so, is centered around my cursor.
    ```{file_path}{file_contents}```{user_message}'''
    # `custom instructions` is the user's instructions for the prompt, if they have any.
    # -----------------------------------------------------------------------
    CURSOR_REWRITE_PROMPT = '''System: You are an intelligent programmer. You are helping a colleague rewrite a piece of code.
    Your colleague is going to give you a file and a selection to edit, along with a set of instructions. Please rewrite the selected code according to their instructions.
    Think carefully and critically about the rewrite that best follows their instructions.
    The user has requested that the following rules always be followed. Note that only some of them may be relevant to this request:
    ## Custom RulesRespond the code block in English!!!! this is important.

    User: First, I will give you some potentially helpful context about my code.Then, I will show you the selection and give you the instruction. The selection will be in `{file_path}`.

    -------
    ## Potentially helpful context
    #### file_context_4{file_context_4}
    #### file_context_3{file_context_3}
    #### file_context_2{file_context_2}
    #### file_context_1{file_context_1}
    #### file_context_0{file_context_0}

    This is my current file. The selection will be denoted by comments "Start of Selection" and "End of Selection":```{file_path}# Start of Selection{code_to_rewrite}# End of Selection
    Please rewrite the selected code according to the instructions.Remember to only rewrite the code in the selection.Please format your output as:
    ```# Start of Selection# INSERT_YOUR_REWRITE_HERE# End of Selection
    Immediately start your response with```'''


Cursor本身的Prompt已经很强大了，但网友们还想让它更强，有网友就建了一个网站（https://cursor.directory/），用来分类收集Cursor的提示，据说这些有针对性的提示会比默认的还好，想要在Cursor中使用它们也很简单。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FaaN2xdFqa4Gs5QuxCvMGUsUMaBfibics7gqmcj65HRV8CSPxUOXibXAtIWxeMh7AmwF8IXusXsASiag4pmV6bejFWA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

具体做法为复制里面的rule文件命名为.cursorrules放置在项目根目录即可，笔者尝试了其中几条，没看出太大变化（或许我的指令太过简单），表现都很不错。（为了验证其是否真的有效，甚至自己写了一个很蠢的提示，也能正常生成代码，如下图确信配置成功生效了）。

- 自定义cursorrules：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FaaN2xdFqa4Gs5QuxCvMGUsUMaBfibics7guKLlcFlBm0krbkic2av97QGibA4n0NJXIYmhxyvyn0f62CT3TlJny62A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

- 生效的提示

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FaaN2xdFqa4Gs5QuxCvMGUsUMaBfibics7gQ6hkJMTnHB4epGRYdD48lE7BM4ib3JrVKwOkrcc6JNhHHAC5ehnFpqg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

除此之外，该网站有很多关于Cursor的使用教程，感兴趣的可以参考学习。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FaaN2xdFqa4Gs5QuxCvMGUsUMaBfibics7g6vyG52HItgAQuQR3goYI1kPwy5mB2cJNjrx3icnKcDib5Gjq5Dc6twzw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg)

不管这些和Cursor真实的提示是否一致，都从某个侧面反映了Cursor在提示层面拥有独到之处。早在去年6月，Cursor开发者Arvid就发表了一篇有关prompt的文章，他将prompt与网页设计类比，给出了一个prompt工程的独特认知和最佳实践，值得我们借鉴学习。

下面就让我们一起读读这篇文章《Prompt设计》。

*** ** * ** ***

我通常不太喜欢用旧世界的事物来类比新世界的现象。不过这次请容许我这么做：我认为应将提示（prompting）称为提示设计（prompt design），并且可以将其比作网页设计。

我认为提示就像是在与一个时间有限的人沟通。虽然大语言模型（LLM）的特定技术（例如链式思维）确实有其帮助，但我发现，改善性能的最好方法之一是提供非常清晰、高质量的指令，就像清晰简洁的指令可以帮助人类更好地理解一样。

将提示视为清晰的交流使提示听起来像是在写作。然而，我进行的大部分提示都是参数化的：有多个输入变量，并且需要动态地调整提示内容。因此，将提示视为带有动态输入的清晰交流是最准确的描述。

有哪些领域需要在动态输入的情况下进行清晰的交流呢？网页设计就是其中之一。

让我们来列举一下它们的相似之处。提示和网页设计都具备以下特点：

- 需要清晰的表达，并且沟通是其主要目标；
- 需要响应动态内容，不像写作或杂志排版；
- 需要将内容适应不同的大小------网页设计中是屏幕大小，提示中是上下文窗口。

根据我在提示和网页设计中的经验，我发现自己在这两个领域有相似的开发偏好：

- 查看实际的提示非常重要，就像查看已渲染的网站一样重要。如果我必须在脑海中模拟HTML和CSS的渲染过程，我是无法设计网站的。同样，在不查看所有输入变量填充后的提示渲染结果的情况下，也很难写出好的提示。例如，提示"Hi **u** s**e** r**n** a**m**e{message}"可能看起来合理，但渲染后你会发现用户名和消息混在一起。
- 组合组件在提示和网页设计中都很有用。
- 声明式优于命令式。像在网页设计中，如果所有HTML元素都是用document.createElement调用创建的，那么修改它就会非常困难。同样，阅读和修改由一连串str += "..."组成的提示也很麻烦。
- 在这两者中，有时我想要达到"像素完美"。在处理较弱的模型（如GPT-3.5及更早版本）时，我希望没有多余的换行符或其他不完美的格式；而在设计网站时，有时每个像素都很重要。

对于大语言模型智能体来说，这个类比可以更进一步：智能体提示可以被视为为智能体构建交互式网站，智能体可以通过调用函数来"点击按钮"，提示会响应函数调用重新渲染，就像网站响应按钮点击重新渲染一样。

当然，提示设计和网页设计之间还是有一些差异的：

- 提示目前仅涉及文本内容。
- 缓存处理不同：特别是对于智能体，你需要确保重渲染成本低，仅更改提示部分内容。这有点类似于网页缓存优化，但本质上是不同的挑战。

尽管如此，这些相似之处让我坚信提示应该被称为提示设计，而不是提示工程。编写提示感觉就像设计一个网站，因此也应如此命名。

提示设计的理念启发了我创建了Priompt，这是一个类似React、基于JSX的提示设计库。

Priompt v0.1：首次尝试提示设计库

Priompt（https://github.com/anysphere/priompt）是受现代网页设计原则启发的提示设计库的首次尝试。我们在Anysphere内部使用它，感觉非常好。我认为它的所有抽象可能并不完全准确，但至少确信JSX比字符串模板更方便。即使是简单地能注释掉部分提示这件事，也能让迭代过程更快。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FaaN2xdFqa4Gs5QuxCvMGUsUMaBfibics7gU4cCoF6T4hlh6zzun4TffCfggzMJ7UZYC5SeX07gyRjqacC7MUGuCg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg) What prompting as JSX looks like.

Priompt还附带一个（匆忙制作的）预览网站，你可以在上面预览你的提示在真实数据上的效果。在开发应用程序时，可以记录每个请求进入组件的序列化属性（props）。然后，当你看到意外行为时，可以访问Priompt预览，查看具体的提示，并更改源代码，从而更新提示，使其与实际请求的属性一致。我们发现这样更容易进行提示的迭代。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FaaN2xdFqa4Gs5QuxCvMGUsUMaBfibics7gDRyQc9evaYAWKssBic9HjrDakucMXvgrvcXvNXOSmIa7RC3hRQTiajTA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg) Previewing prompts.

如果你尝试了，请告诉我你的想法！我愿意看到更多类似的想法，或者直接告诉我我错了，提示设计是愚蠢的：）

注意事项 模型变化迅速，提示技术也必须随之变化。我认为提示设计还存在一些问题：

- 对于GPT-4，像素完美设计并不重要，GPT-4.5及更高版本的模型可能也不需要。
- 如果长上下文模型发展的趋势继续，上下文窗口限制可能会消失。不过对此我还存疑。
- OpenAI似乎正在减少开发者对提示的控制；一年之内可能不再需要提示，API调用仅需要提供原始输入和指令。更少控制的趋势始于聊天格式，并随着最近宣布的函数调用继续。
- 缓存可能是提示中最重要的方面之一，在这种情况下，提示会更像工程而不是设计。或许提示设计太基础了，应该交给更高级的框架或编译器（如langchain）。我认为这可能是真的，但考虑到大语言模型快速变化的性质，我个人更愿意尽可能靠近原始模型。


原文：https://www.cursor.com/blog/prompt-design#priompt-v01-a-first-attempt-at-a-prompt-design-library

赠书活动进行中：[转型LLM应用开发推荐阅读------《从零构建向量数据库》，赠书活动又来了！](http://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461146662&idx=2&sn=94062eff305e5b7639630eae9a7605d7&chksm=87397c08b04ef51ea7caa5e1d9b4ff4e27ab4ba93ddb6e895b5cc3cca46896942e34910704f5&scene=21#wechat_redirect)

**橱窗有更多笔者精选AI及职业发展的好书，欢迎查阅。**

![](https://image.cubox.pro/cardImg/65nmox3xvl5vpnhfd64wky7tseu9o855a6d84pn0cc66o0wzdc?imageMogr2/quality/90/ignore-error/1)

**AI工程化**

专注于AI领域（大模型、MLOPS/LLMOPS 、AI应用开发、AI infra）前沿产品技术信息和实践经验分享。

213篇原创内容

公众号

，


**后台回复"进群"入群讨论。**

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461146681&idx=1)
