---
id: "7429602184347518194"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649009111&idx=1&sn=a2c566b457bff9eda388665930a4649c&chksm=86df5f608cf2e75e2f91baab0c62972c45b394d7ae1ba2900a2cad26e745b992a0d6b9be769e&mpshare=1&scene=1&srcid=0306QrsyYFXinU5Pa12xr0vh&sharer_shareinfo=a8970d229ae98997db2a0cc240c7a89d&sharer_shareinfo_first=a8970d229ae98997db2a0cc240c7a89d
author: "老章很忙 Ai学习的老章"
collected: 2026-03-06
tags: []
---

# Claude-Code 桌面客户端，开源免费，Windows可用

# Claude-Code 桌面客户端，开源免费，Windows可用

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649009111&idx=1&sn=a2c566b457bff9eda388665930a4649c&chksm=86df5f608cf2e75e2f91baab0c62972c45b394d7ae1ba2900a2cad26e745b992a0d6b9be769e&mpshare=1&scene=1&srcid=0306QrsyYFXinU5Pa12xr0vh&sharer_shareinfo=a8970d229ae98997db2a0cc240c7a89d&sharer_shareinfo_first=a8970d229ae98997db2a0cc240c7a89d)老章很忙 Ai学习的老章


![](https://image.cubox.pro/cardImg/wwe5gf0aegvpjff6y0rvh6vm2tde5evcymq5nvy8xbh3l29no?imageMogr2/quality/90/ignore-error/1)

**Ai学习的老章**

长期跟踪关注统计学、机器学习算法、深度学习、人工智能、大模型技术与行业发展动态，日更精选技术文章。回复机器学习有惊喜资料。

906篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FwibWVO7K9ltYbjTeXsYBibrx8ibppHyfuUfqn1iaNr9ctjvLNXXCf33YRcVOKrsKORbppPpxPgGUYiaOXnpgVk5StbJn10BRk7wjQ41axWCbzhtY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

大家好，我是 Ai 学习的老章

*
  [大模型世界新宠，从 Claude 走向开源，OpenAI 入局，Agent Skills 10000 字教程](http://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649006999&idx=1&sn=f7ac86380ca2572cc91a66f4c2f16da8&chksm=879331bdb0e4b8abf6ea86b057649ae5ff8ab0bae8b140092446c256cbca9918fdad6a4bb24f&scene=21#wechat_redirect)
*
  [Claude Code 配置太痛苦？试试这个神器](http://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649007136&idx=1&sn=17eb37522718519d867a10ab66069088&chksm=8793360ab0e4bf1c723b697978fbc6f34535e0c42a4205c3021517df4b597572595975d11f36&scene=21#wechat_redirect)

推荐一个开源的桌面 Agent 客户端，直接把 Claude Code 的核心能力包装成了一个漂亮的 GUI 应用------ **Craft Agents**

### 简介

Craft Agents 是 Craft（就是那个苹果生态圈很火的笔记应用 craft.do）团队开源的 Agent 桌面客户端。

它基于 Anthropic 官方的 **Claude Agent SDK** 构建，相当于给 Claude Code 套了一层精致的外壳，同时还增加了很多 Claude Code 没有的功能。

下图是 Craft Agents 的主界面，左侧是会话列表（像邮件收件箱一样），右侧是对话区：


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FwibWVO7K9ltbaicV5FiakMId4qzYSP4wsic3IlWuibiaLXaMhicP6CU7pCaREvKSOwshZ2TjvQuhC6FpOSiahLI3X3dpcKGYnFJZe1urNuvob4xlEhE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

<br />

Craft Agents 主界面

**核心功能与特点：**

*
  **多会话收件箱** ：终于不用开一堆终端窗口了！所有任务都在一个地方管理，支持状态标记（Todo → In Progress → Done）、旗标、归档
*
  **Sources 数据源连接** ：这是我最喜欢的功能。你只要告诉 Agent「添加 Slack 作为数据源」，它就会自动帮你找 MCP 服务器、读取文档、配置认证，全程不用碰 JSON 文件
*
  **三种权限模式** ：Explore（只读）、Ask to Edit（每次修改都问你）、Auto（全自动），用 SHIFT+TAB 一键切换，这个设计太贴心了
*
  **Skills 技能系统** ：和 Claude Code 的 Skills 类似，但管理更方便，可以通过 @ 直接调用
*
  **完整的 Claude Code 体验** ：流式响应、工具调用可视化、实时更新，该有的都有

**和 Claude Code 的对比：**

|    方面     | Claude Code | Craft Agents |
|-----------|-------------|--------------|
| 界面        | 终端 CLI      | 桌面 GUI       |
| 多任务       | 开多个终端       | 收件箱式管理       |
| MCP 配置    | 手动编辑 JSON   | 对话式配置        |
| Skills 管理 | 文件夹         | @ 提及         |
| 会话持久化     | 需要手动保存      | 自动保存         |
| 开源协议      | 私有          | Apache 2.0   |


### 安装

安装超级简单，一行命令搞定。

**macOS / Linux：**

    curl -fsSL https://agents.craft.do/install-app.sh | bash

**Windows（PowerShell）：**

    irm https://agents.craft.do/install-app.ps1 | iex

也可以直接从官网下载安装包：

*
  macOS ARM64：https://agents.craft.do/electron/latest/Craft-Agent-arm64.dmg
*
  macOS Intel:https://agents.craft.do/electron/latest/Craft-Agent-x64.dmg
*
  Windows：https://agents.craft.do/electron/latest/Craft-Agent-x64.exe
*
  Linux：https://agents.craft.do/electron/latest/Craft-Agent-x64.AppImage

如果你是喜欢折腾源码的开发者：

    git clone https://github.com/lukilabs/craft-agents-oss.git
    cd craft-agents-oss
    bun install
    bun run electron:start

注意，项目用的是 **Bun** 作为运行时，不是 Node.js。技术栈很现代：Bun + Electron + React + shadcn/ui。

### 使用

启动后，先选择 API 连接方式：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwibWVO7K9ltblzPX0j66IyTQyOLj1IiagiaoEtgfXaYjUcNiaPWvj5BooUXibG1BicTIaZvlzjSmUyX7IdNqg1F2QqnAQK3hfEE4fdWHKMqpYQJWw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

我选择的 API Key 方式
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwibWVO7K9ltYSy5dtNbJeianlzwJiccKoAGl9vSicCiablYqdK3LouaGqmSzKCSWmDISIVPIJhosTvnjJ5xHcgIuawABwoN9vrYayj6SlD86ph8E%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

可以对接 Ollama，也可以自定义，这里我选择了 Custom

但是必须是支持 Anthropic 格式 API，上次从[土豪英伟达，Kimi-K2.5 免费用，API 支持OpenCode](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649008850&idx=1&sn=20f1424f14eceaa735d3932193dba259&scene=21#wechat_redirect) 申请的 K2.5 用不了
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FwibWVO7K9ltbG8uoQsicuXrerMv7EOVkzYttu7vbViaetICibibrQS4TvRXJxHWYTc074QQckWjBFGtT2cQZSLOcyiatrvjcqFMdgkNdEIqhN27Kg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

但是 siliconflow 还行，去掉/v1 就可以用了

https://cloud.siliconflow.cn/i/YefhGWlT
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FwibWVO7K9ltazLCJFMia4y6rOd1rE2VibcIRibibsloHMW3vIkYzTK23BIQTeBSxicK69V0BVMxw4EEia4xaN4BqAsLyYsVRnwDpK5BHwUsZCLXia7A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)

然后创建一个 Workspace，就可以开始聊天了。

**连接各种服务（这是最爽的部分）：**

Agent 会自动搜索公开的 MCP 服务器或 API 文档，帮你配置好一切。你甚至可以直接粘贴 OpenAPI Spec 或 API 文档截图进去，它能自己搞定。

官方说他们甚至把它连上了一个跳板机后面的 Postgres 数据库，Skills + Sources 的组合威力可见一斑。

**已有 Claude Code 配置？**

如果你之前在 Claude Code 里配置了一堆 Skills 和 MCP，直接告诉 Agent「从 Claude Code 导入所有 Skills」，它会帮你迁移过来。

**权限模式切换：**

我日常用的是 ask 模式（Ask to Edit），每次写文件或执行命令都会问我。确认流程顺畅后，切到 allow-all 让它自动跑。

用 **SHIFT+TAB** 快捷键可以在三种模式之间循环切换。

### 实测

我把它接入了我日常使用的几个数据源：GitHub、本地 Obsidian 笔记库、一个自建的 MCP 服务器。

**优点：**

1.
   **UI 确实漂亮** ，比起终端看着舒服多了，长时间工作不那么累
2.
   **多会话管理真的方便** ，终于能像处理邮件一样处理 Agent 任务了
3.
   **数据源配置太丝滑了** ，以前配个 MCP 要翻半天文档改 JSON，现在一句话搞定
4.
   **会话自动保存** ，关掉重开还在，这点 Claude Code 做不到
5.
   **开源许可友好** ，Apache 2.0，魔改无压力

### 总结

如果你是 Claude Code 的重度用户，想要一个更友好的 GUI 界面，Craft Agents 绝对值得一试。

如果你是 Agent 开发者，想要一个开源的桌面 Agent 框架作为参考，这套 Electron + React + Claude Agent SDK 的架构也很值得学习。

**适合人群：**

*
  用 Claude Code 觉得终端不够友好的开发者
*
  需要同时管理多个 Agent 任务的人
*
  想要把各种服务（GitHub、Slack、Google 全家桶）接入 Agent 工作流的人
*
  想要一个开源 Agent 桌面应用作为二次开发基础的团队

最后说一句，Craft 团队提到他们「用 Craft Agents 开发 Craft Agents」------完全不用代码编辑器，任何定制都只需要一句话。

这个理念挺有意思的，可能这才是 Agent Native 软件的未来形态。

官网：https://agents.craft.do/

GitHub：https://github.com/lukilabs/craft-agents-oss

演示视频：https://www.youtube.com/watch?v=xQouiAIilvU

#CraftAgents #ClaudeCode #Agent #MCP #开源

**制作不易，如果这篇文章觉得对你有用，可否点个关注。给我个三连击：点赞、转发和在看。若可以再给我加个🌟，谢谢你看我的文章，我们下篇再见！**
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FwibWVO7K9ltaucpXXK6cKfW7eZ4JxIh7T7F4NeKK0EtcAdsHZhjOaCAmeaQ0pTyr5F24wFo28loF8ZMAjJtFUPEJQEzHFDh5gA01uOH9WMyM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzA4MjYwMTc5Nw==&mid=2649009111&idx=1&sn=a2c566b457bff9eda388665930a4649c&chksm=86df5f608cf2e75e2f91baab0c62972c45b394d7ae1ba2900a2cad26e745b992a0d6b9be769e&mpshare=1&scene=1&srcid=0306QrsyYFXinU5Pa12xr0vh&sharer_shareinfo=a8970d229ae98997db2a0cc240c7a89d&sharer_shareinfo_first=a8970d229ae98997db2a0cc240c7a89d)

