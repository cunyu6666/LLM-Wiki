---
id: "7451688015115585191"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIzODMwNzYwOQ==&mid=2247484504&idx=1&sn=c4fdc3354266ba8eb1f7d2802ee13361&chksm=e8854b11c98d02c591da401b01c1b6ed57cca531efb7b00aed5a009dcad8453b5412acdb386b&mpshare=1&scene=1&srcid=0506KUsaf9brjPH1jgdHWByT&sharer_shareinfo=243c9903102fa6696edbc2890232668f&sharer_shareinfo_first=243c9903102fa6696edbc2890232668f
author: "AI 技术小林 AI技术小林"
collected: 2026-05-06
tags: []
---

# HyperFrames：用 HTML 生成视频的开源渲染框架

# HyperFrames：用 HTML 生成视频的开源渲染框架

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzODMwNzYwOQ==&mid=2247484504&idx=1&sn=c4fdc3354266ba8eb1f7d2802ee13361&chksm=e8854b11c98d02c591da401b01c1b6ed57cca531efb7b00aed5a009dcad8453b5412acdb386b&mpshare=1&scene=1&srcid=0506KUsaf9brjPH1jgdHWByT&sharer_shareinfo=243c9903102fa6696edbc2890232668f&sharer_shareinfo_first=243c9903102fa6696edbc2890232668f)AI 技术小林 AI技术小林


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2F02iaTltC9YnDznPYyicuxc0Qdu0INGtcqJ664c5VnAd7rmPpp2nbicPAUJN5QibUGibtgBZAUFAhEG87LjbZJxnzdQB1ayZvdHegC0F7VwGF3UeY%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D0)HyperFrames demo

## 一句话定位

HyperFrames 是 HeyGen 开源的 HTML 视频渲染框架：用写网页的方式定义视频画面、时间轴和动画，再通过浏览器预览并渲染成 MP4。

## 基础信息卡片


|   项目   |                         信息                         |
|--------|----------------------------------------------------|
| GitHub | https://github.com/heygen-com/hyperframes          |
| 官方文档   | https://hyperframes.heygen.com/introduction        |
| NPM 包  | hyperframes                                        |
| 主要语言   | TypeScript                                         |
| 开源协议   | Apache-2.0                                         |
| 当前版本   | 0.4.41                                             |
| 运行要求   | Node.js \>= 22、FFmpeg                              |
| 项目定位   | HTML-native、AI-first、deterministic video rendering |


## 解决什么问题

做视频自动化时，常见路线大概有两种：一种是使用传统剪辑工具，适合人工制作，但不适合批量生成；另一种是使用代码化视频框架，适合自动化，但经常要求开发者进入特定组件体系或 DSL。

HyperFrames 选择了一条更贴近 Web 开发的路线：视频本身就是 HTML。

它把视频里的片段、字幕、图片、音频、时间点、轨道关系都放进 HTML 元素和 data-* 属性里。你可以像写页面一样组织画面，用 CSS / GSAP / Lottie / Three.js 等熟悉的前端技术做动画，再用命令行把它渲染成 MP4。

这个思路对 AI Agent 也很友好。因为大模型本来就擅长生成 HTML、CSS 和简单脚本，HyperFrames 又提供了面向 Agent 的 skills / plugin / CLI 工作流，让 Agent 可以从"描述一个视频"一路做到"生成项目、预览、检查、渲染"。

## 核心功能

### 1. 用 HTML 描述视频结构

HyperFrames 的核心输入是一份 HTML。每个元素通过 data-start、data-duration、data-track-index 等属性表达它在视频中的出现时间、持续时间和轨道位置。

一个简单的视频可以由视频素材、标题、图片、背景音乐这些普通 HTML 元素组成：

    <div id="stage" data-composition-id="my-video" data-start="0" data-width="1920" data-height="1080">
      <video
        id="clip-1"
        data-start="0"
        data-duration="5"
        data-track-index="0"
        src="intro.mp4"
        muted
        playsinline
      ></video>

      <h1
        class="clip"
        data-start="1"
        data-duration="4"
        data-track-index="1"
      >
        Welcome to HyperFrames
      </h1>

      <audio
        data-start="0"
        data-duration="5"
        data-track-index="2"
        data-volume="0.5"
        src="music.wav"
      ></audio>
    </div>

这种设计的好处是门槛很低：不需要先学习一个全新的视频编辑格式，也不要求把所有内容改写成 React 组件。

### 2. 浏览器预览，本地渲染成 MP4

HyperFrames 提供 CLI，可以直接初始化、预览和渲染项目：

    npx hyperframes init my-video
    cd my-video
    npx hyperframes preview
    npx hyperframes render

预览阶段会在浏览器里实时查看效果；渲染阶段则通过 headless Chrome 逐帧捕获画面，并交给 FFmpeg 输出最终视频。官方文档强调的是确定性渲染：同样的输入应得到一致的输出，这对自动化流水线很重要。

### 3. 面向 AI Agent 的工作流

HyperFrames 不只是一个 CLI，还提供了面向 AI 编程工具的配套能力。项目 README 中推荐先安装 skills：

    npx skills add heygen-com/hyperframes

这些 skills 会教 Agent 如何写正确的 composition、GSAP 时间线、Tailwind v4 浏览器运行时样式，以及不同动画运行时的适配方式。

项目还提供了面向 Claude Code、Cursor、Codex、Gemini CLI 等工具的使用说明或插件入口。也就是说，它不是只把"AI 支持"当营销词，而是把 Agent 能不能无交互地初始化、lint、预览、渲染，作为框架设计的一部分。

### 4. 支持多种动画与素材运行时

HyperFrames 使用 Frame Adapter 模式来接入动画运行时。你可以使用 GSAP、Lottie、CSS animation、Three.js、Web Animations API 等方式构建动画，只要它们能够按帧 seek，就可以被纳入确定性渲染流程。

这点对视频自动化很关键：视频不是简单录屏，而是要在指定帧上得到确定画面。HyperFrames 把"页面如何播放"和"渲染器如何按帧捕获"之间的关系抽象出来，让不同动画技术能进入同一条视频生成链路。

### 5. 内置组件目录与多个子包

项目提供了 50+ ready-to-use blocks and components，例如社交媒体覆盖层、shader transition、数据可视化、电影感效果等，可以通过命令添加：

    npx hyperframes add flash-through-white
    npx hyperframes add instagram-follow
    npx hyperframes add data-chart

从仓库结构看，它是一个 monorepo，主要包含：

|                包                |                    作用                     |
|---------------------------------|-------------------------------------------|
| hyperframes / @hyperframes/cli  | 初始化、预览、lint、渲染的 CLI                       |
| @hyperframes/core               | 类型、解析器、生成器、linter、runtime、frame adapters  |
| @hyperframes/engine             | 基于 Puppeteer + FFmpeg 的页面到视频渲染引擎          |
| @hyperframes/producer           | 完整渲染流水线，包括捕获、编码和音频混合                      |
| @hyperframes/studio             | 浏览器端 composition editor UI                |
| @hyperframes/player             | 可嵌入的 <hyperframes-player> Web Component   |
| @hyperframes/shader-transitions | 用于 composition 的 WebGL shader transitions |


## 官方视频示例

    npx hyperframes init my-video --example warm-grain


|      示例       |      类型      |                                       视频链接                                       |
|---------------|--------------|----------------------------------------------------------------------------------|
| Warm Grain    | 品牌 / 生活方式    | https://static.heygen.ai/hyperframes-oss/docs/images/templates/warm-grain.mp4    |
| Play Mode     | 社交媒体 / 产品发布  | https://static.heygen.ai/hyperframes-oss/docs/images/templates/play-mode.mp4     |
| Swiss Grid    | 企业 / 技术 / 数据 | https://static.heygen.ai/hyperframes-oss/docs/images/templates/swiss-grid.mp4    |
| Kinetic Type  | 标题卡 / 宣传片    | https://static.heygen.ai/hyperframes-oss/docs/images/templates/kinetic-type.mp4  |
| Decision Tree | 解释型视频 / 教程   | https://static.heygen.ai/hyperframes-oss/docs/images/templates/decision-tree.mp4 |
| Product Promo | 产品展示         | https://static.heygen.ai/hyperframes-oss/docs/images/templates/product-promo.mp4 |
| NYT Graph     | 数据故事 / 图表视频  | https://static.heygen.ai/hyperframes-oss/docs/images/templates/nyt-graph.mp4     |
| Vignelli      | 竖屏标题 / 公告    | https://static.heygen.ai/hyperframes-oss/docs/images/templates/vignelli.mp4      |


## 适合谁

HyperFrames 比较适合这几类场景：

1.
   1. **熟悉前端技术、想用代码生成视频的开发者**   
   如果你会写 HTML、CSS、JS，理解它的成本会比较低。
2.
   2. **需要批量生成营销视频、教程视频、数据视频的团队**   
   例如把 CSV 变成动态图表、把产品文档变成短视频、把模板批量填充成不同版本的视频。
3.
   3. **正在搭建 AI Agent 内容生产流程的人**   
   它的 CLI、skills 和插件设计都偏向自动化，适合作为 Agent 生成视频的执行层。
4.
   4. **希望视频生成链路可复现、可集成到流水线的人**   
   相比人工剪辑工具，HyperFrames 更适合放进脚本、CI、Docker 或后端任务里运行。

## 快速上手

如果想让 AI Agent 参与生成，官方推荐先安装 skills：

    npx skills add heygen-com/hyperframes

然后可以直接让 Agent 按 /hyperframes 的上下文生成视频，例如：

    Using /hyperframes, create a 10-second product intro with a fade-in title, a background video, and background music.

如果想手动创建项目，可以走 CLI：

    npx hyperframes init my-video
    cd my-video
    npx hyperframes preview
    npx hyperframes render --output output.mp4

本地需要准备：

*
  • Node.js \>= 22
*
  • FFmpeg
*
  • 可以运行 Chromium / Puppeteer 的环境

## 结论

HyperFrames 的核心价值不在于"又做了一个视频编辑器"，而在于它把视频生成问题重新拉回 Web 技术栈：HTML 负责结构，CSS 和动画库负责表现，浏览器负责渲染，FFmpeg 负责输出。

对于开发者来说，这意味着视频可以像页面一样被生成、版本管理和自动化；对于 AI Agent 来说，这意味着它有了一个更容易理解和操作的视频生成目标格式。

如果你正在做内容自动化、批量视频生成、数据视频，或者想让 AI Agent 从文本直接生成可渲染的视频项目，HyperFrames 是一个值得关注的开源项目。

*** ** * ** ***

END

AI技术小林

持续分享 AI、技术、工具和实战干货，关注前沿趋势，也关注真实落地。

如果你想获取这些内容：

1 AI 实用技巧

2 技术经验总结

3 工具与效率方法

4 实战案例拆解

欢迎关注公众号 「AI技术小林」，第一时间获取更多高质量内容。

如果想加入微信群，和更多朋友一起交流学习，后台回复 「加群」 即可。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIzODMwNzYwOQ==&mid=2247484504&idx=1&sn=c4fdc3354266ba8eb1f7d2802ee13361&chksm=e8854b11c98d02c591da401b01c1b6ed57cca531efb7b00aed5a009dcad8453b5412acdb386b&mpshare=1&scene=1&srcid=0506KUsaf9brjPH1jgdHWByT&sharer_shareinfo=243c9903102fa6696edbc2890232668f&sharer_shareinfo_first=243c9903102fa6696edbc2890232668f)

