---
id: "7450199407510685913"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI4OTc4MzI5OA==&mid=2247882654&idx=1&sn=67e763406a73e085bb94e9222103739f&chksm=ed52b3008698afba4077369ad71443b061850fa8c84ab3ce61101f0d0caf463382f01b2a1b83&mpshare=1&scene=1&srcid=0502HYGsZ1clwm234d2HM2vn&sharer_shareinfo=6cefefd3c6b3ffc3fefa081f89114c1d&sharer_shareinfo_first=6cefefd3c6b3ffc3fefa081f89114c1d
author: "大单网 云头条"
collected: 2026-05-02
tags: []
---

# 开源版 Claude Design 爆火！

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI4OTc4MzI5OA==&mid=2247882654&idx=1) · 大单网 云头条


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2FXqPzJxoFaUtWiaVM4f2c0aaTtGkAicVWWRze2yquMe9braic60Lz6j79B6qN7hjmNEXBuKTXz6wJG4VE9Yjibib5XPg%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D0)

Claude Design 刚刚掀起 AI 设计工具的热潮，开源社区已经开始给出另一种答案。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FlETfxQqKSMb1SMYgOuHibCquXenFXyItibILw8hf0urta57VaFCQCLicFDq4Xp2QI9QPeSmZiaRqPkH7o8icqQ1tFaFuQR4lxFictYzSLiayncyZ1I%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

为什么做这个？ Open Design 表示：

Anthropic 的 Claude Design（2026-04-17 发布，基于 Opus 4.7）让大家第一次看到：当一个 LLM 不再写废话、开始直接交付设计成品，会是什么样子。它瞬间出圈 ------ 然后保持**闭源** 、付费、只跑在云上、绑定 Anthropic 的模型和 Anthropic 的内部 skill。没有 checkout，没有自托管，没有 Vercel 部署，也换不了自己的 agent。

**Open Design（OD）就是它的开源替代品。** 同一套 loop、同一种「artifact-first」心智模型，但没有锁定。我们不做 agent ------ 你笔记本上最强的 coding agent 已经装好了。我们要做的，是把它接进一个 skill 驱动的设计工作流：本地用 pnpm tools-dev 跑完整本地闭环，云端可单独部署 Web 层，每一层都 BYOK（自带 Key）。

输入「帮我做一份杂志风的种子轮 pitch deck」。在模型挥洒第一个像素之前，**初始化问题表单** 已经先跳出来。Agent 从 5 套精挑的视觉方向里选一个。一张活的 TodoWrite 计划卡片实时流入 UI。Daemon 在磁盘上构建出一个真实的项目目录，里面有 seed 模板、布局库、自检 checklist。Agent **强制 pre-flight** 读取它们，对自己的输出跑一轮**五维评审** ，几秒后吐出一个 <artifact>，渲染在沙盒 iframe 里。

这不是「AI 试图做点设计」。这是一个被提示词栈训练得像高级设计师一样工作的 AI ------ 有可用的文件系统、有确定性的色板库、有 checklist 文化 ------ 也就是 Claude Design 立下的那条线，只是这次它开源、归你。

2026 年 5 月 1 日，Nexu Labs 开源 Open Design 0.1.0。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FlETfxQqKSMY9lxmMYjbpPWxaAOSwc7iaqe0v3MeByk6gARV4F6KMUUFVPRd48PEKdFdNibTdmaLLtHL1ibHY5J2aadAp1IF219icMUf0qwrU8N0%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D2)

项目方直接把它定位为 Claude Design 的开源替代品，本地优先、可自行部署、支持 BYOK，也就是用户自带 API Key。

横向对比：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FlETfxQqKSMZE12K0UYHbicr3SJsMLqXkCIE4Hd6W3aVKicic5wpxUqRdBMNnuXW4Wwob4Mk1eXansUIZSK8B4DN6FJAkvMYGB64s6Q8Bicvpehc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

目前已有 1.32万 Star、1500 次 Fork。

Open Design 的做法，不是再造一个封闭的 AI 设计平台，而是将用户已有的 coding agent 变成设计引擎。

它可以自动识别本机 PATH 里的 11 类命令行工具，包括 Claude Code、Codex、Cursor Agent、Gemini CLI、OpenCode、Qwen、GitHub Copilot CLI、Hermes、Kimi、Pi 和 Kiro。

没有 CLI agent 的用户，也可以通过 OpenAI-compatible BYOK proxy 接入模型服务。

这让它和 Claude Design 形成了明显区别。

Claude Design 更像一个官方云端产品，用户在 Anthropic 的产品体系里完成设计生成。

Open Design 则更像一个开源工作台，将模型、agent、设计系统、技能和预览环境拆开，让用户自己组合。

Claude Design 技术架构：


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FlETfxQqKSMa3A18E22NhAicbQav2WsdL5ap5x9Fh5sTibOfFmvJ97U3Xb4J8YyFxYPv9sb9UppxicM4Bf7JBtOm5d7e86n96kmfLFLypRWIkog%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)


Open Design 0.1.0 开始就塞进了不少设计资产。

官方称，首发版本内置 72 套品牌级 Design Systems、31 个可组合 Skills，以及 57 份来自社区的设计规范。

支持在聊天旁边实时预览 SVG、Markdown、多文件 HTML、图片、视频、音频等内容，还可以导入多文件、预览文档，甚至支持 Claude Design 的 .zip 文件导入。

部署方式也已经初步成型。

Open Design 0.1.0 提供经过签名和公证的 macOS Apple Silicon 应用、Windows x64 测试安装包、终端模式，以及一键 Vercel 自部署。

界面语言首发支持 9 种，包括简体中文、繁体中文、英文、日文、德文、西班牙文、俄文、波斯文和巴西葡萄牙文。

不过，这仍然是一个很早期的版本。

macOS 目前只支持 Apple 芯片，Intel Mac 不能直接使用安装包；Windows 安装包还没有签名，首次启动可能触发 SmartScreen 或杀毒软件提示；Linux 也还没有桌面端打包版本，只能从源码运行。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FlETfxQqKSMZ7p9Ekznj719LZu0aSiaFjGFibTOAVKuHEmp3DFibb9gsxkYETsjJbsrXc5IHxB7OBt4lQgWhfMImjhV04Ef9ibXvmePmDkBKib4aM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D5)


Open Design 的出现，真正值得关注的地方，是 AI 设计工具正在被"拆平台化"。

过去，用户想用 AI 生成设计稿，往往要进入某个厂商的云端入口，模型、能力、素材、导出方式都被打包在一个产品里。

Open Design 走的是相反方向，已有的 coding agent 可以拿来用，模型可以换，设计系统可以扩展，项目文件可以留在本地，部署也可以自己控制。

这对普通用户未必是最简单的选择，但对开发者、独立团队和重视数据控制的企业来说，吸引力很明确。

AI 设计不再只是"输入一句话，生成一张图"，而是开始进入真实工程流程，有文件、有预览、有导出、有版本、有可替换的 agent。

Claude Design 推动了 AI 设计产品化，Open Design 则是将这套能力拉向开源和本地化。

目前主力的三个模型：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FlETfxQqKSMZfaCfmQkd5kQdWNv2RVDKnB3fbANeCCqPbY8uO430aoh0ATCs9XAAiaeE2zPn1QFKIwO0olY5PcFpxyjDHNOZiaNCmCBBEActGs%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

https://github.com/nexu-io/open-design/tree/open-design-v0.1.0

![](https://image.cubox.pro/cardImg/1z1odudh9x0o4a40csiqmse43jacnds90vtso3qwoozut52sa0?imageMogr2/quality/90/ignore-error/1)

**云头条**

引领科技变革，连接技术与商业

424篇原创内容

<br />

公众号  

，

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI4OTc4MzI5OA==&mid=2247882654&idx=1)
