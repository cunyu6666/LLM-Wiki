---
id: "7410770390714157144"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247501992&idx=1&sn=d842fee14bb40b54a057fa81fd5fd488&chksm=ed2adbd34a5ccf483f5c351d64ca69373b5db9003c6cd7190e6e3667cb29b893a63796436661&mpshare=1&scene=1&srcid=01130JmsJKwGaTlnpGiG939M&sharer_shareinfo=7995b5a547a64ab87469c663a6990f90&sharer_shareinfo_first=7995b5a547a64ab87469c663a6990f90
author: "louwill 机器学习实验室"
collected: 2026-01-13
tags: []
---

# MarkItDown，微软开源的超强AI文档转换工具

# MarkItDown，微软开源的超强AI文档转换工具

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247501992&idx=1&sn=d842fee14bb40b54a057fa81fd5fd488&chksm=ed2adbd34a5ccf483f5c351d64ca69373b5db9003c6cd7190e6e3667cb29b893a63796436661&mpshare=1&scene=1&srcid=01130JmsJKwGaTlnpGiG939M&sharer_shareinfo=7995b5a547a64ab87469c663a6990f90&sharer_shareinfo_first=7995b5a547a64ab87469c663a6990f90)louwill 机器学习实验室

大家好，我是鲁工。

不知道有多少人跟我一样，相较于看文档写文档，更喜欢的是跟代码打交道。PDF、Word、Excel、PPT，各种格式的文档堆在一起，想统一喂给大模型，光是格式转换就得折腾半天。

直到我最近发现了微软开源的MarkItDown，问题迎刃而解。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F4lN1XOZshfdYpxgico7lmJiaN70HmdlxexpvjWZwI3zuJ6iaqhsAibFyZibYfUbV5fIwz9hye4jyLGDWgjOnOcTRDxg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

在聊MarkItDown之前，先说说为什么要转成Markdown。

主流的大模型，不管是GPT-5还是Claude 4.5，都对Markdown有天然的亲和力。它们的输出经常自带Markdown格式，输入也是如此。

Markdown的好处在于：既保留了文档结构（标题、列表、表格、链接），又足够轻量，没有多余的格式标记。对于需要理解文档语义的AI来说，这是最理想的输入格式。

相比之下，纯文本丢失了结构信息，HTML又太臃肿。Markdown刚好在中间，是个平衡点。

MarkItDown是微软开源的一个Python库，专门用来把各种文件转成Markdown。

项目地址：

https://github.com/microsoft/markitdown

截至目前，GitHub上已经有85k+ Stars，发布两周就冲到了25k，热度相当高。

支持的格式非常全面：

* **办公文档：PDF、Word、PowerPoint、Excel**
* **多媒体：图片（支持OCR和EXIF提取）、音频（语音转文字）**
* **Web内容：HTML、YouTube视频链接**
* **数据格式：CSV、JSON、XML**
* **其他：ZIP压缩包、Outlook邮件、EPUB电子书**

基本上日常能碰到的文档格式都覆盖了。

安装很直接：

    git clone git@github.com:microsoft/markitdown.gitcd markitdownpip install -e 'packages/markitdown[all]'


使用时也只需要四行代码：

    from markitdown import MarkItDownmd = MarkItDown()result = md.convert("report.pdf")print(result.text_content)


```

```

也支持命令行直接运行：

    markitdown report.pdf -o report.md


## 就这么简单。不需要复杂的配置，不需要理解底层原理，拿来就能用。
我们看几个实用场景。首先是批量转换Office文档。比如你有一堆Word和PPT需要处理，几行脚本搞定：


    from markitdown import MarkItDownfrom pathlib import Pathmd = MarkItDown()for file in Path("docs").glob("*.docx"):    result = md.convert(str(file))    Path(f"output/{file.stem}.md").write_text(result.text_content)


```

```

**然后处理一下带图片的文档看看。MarkItDown支持OCR，可以提取图片中的文字。如果配合LLM使用，还能自动生成图片描述：**

    from markitdown import MarkItDownfrom openai import OpenAIclient = OpenAI()md = MarkItDown(llm_client=client, llm_model="gpt-4o")result = md.convert("document_with_images.pdf")


再试一下音频转文字。会议录音、播客音频，都可以直接转成Markdown格式的文字稿：

    result = md.convert("meeting.mp3")


底层用的是Google的语音识别API，效果还可以。

MarkItDown不是万能的，有几个已知的问题：

1. **PDF处理能力有限** ：对于扫描版PDF（没有文字层的），需要先做OCR预处理。另外PDF转换时会丢失格式信息，比如标题层级。

2. **表格处理一般** ：复杂表格的还原效果不太理想。

3. **速度优先，精度其次** ：如果对转换精度要求很高，可能需要考虑其他工具。

如果你的场景对表格和复杂排版要求很高，可以看看IBM的Docling。它的转换精度更好，但代价是安装包有1GB+，速度也慢不少。

MarkItDown的定位是又快又轻，覆盖80%以上的常规场景没问题。

## 最后，MarkItDown还提供了MCP服务器，可以直接和Claude Desktop集成。配置好之后，Claude就能直接读取你本地的各种文档了。在claude_desktop_config.json里加上：


    {  "mcpServers": {    "markitdown": {      "command": "uvx",      "args": ["markitdown-mcp"]    }  }}


这样Claude就多了一个convert_to_markdown的工具，可以处理本地文件。对于经常需要让AI分析文档的场景，相当实用。

MarkItDown解决的是一个很具体的问题：如何把各种格式的文档，高效地转成AI友好的格式。

它不追求完美的转换精度，但胜在简单、快速、格式支持全面。对于大多数AI应用场景来说，够用了。

微软能把这样一个实用的小工具开源出来，确实是方便了广大开发者处理文档了。

感谢您阅读我的文章。我是鲁工，八年AI算法老兵，AI全栈开发者。目前正在全面拥抱大模型和AIGC。感兴趣的小伙伴可以加我微信（louwill_）交个朋友。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F4lN1XOZshfekhSPOVhKyHjek97r6uIakcYsqZxEMvKBCYqOO6wGleHTNuz4sff6Xns2LDGah9Jb6c39iaOhvfpQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26wxfrom%3D13%26wx_lazy%3D1%26tp%3Dwxpic%23imgIndex%3D4)

\>/ 作者：louwill

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI4ODY2NjYzMQ==&mid=2247501992&idx=1&sn=d842fee14bb40b54a057fa81fd5fd488&chksm=ed2adbd34a5ccf483f5c351d64ca69373b5db9003c6cd7190e6e3667cb29b893a63796436661&mpshare=1&scene=1&srcid=01130JmsJKwGaTlnpGiG939M&sharer_shareinfo=7995b5a547a64ab87469c663a6990f90&sharer_shareinfo_first=7995b5a547a64ab87469c663a6990f90)

