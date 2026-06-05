---
id: "7459180054870755235"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzIyOTc4NjE2NA==&mid=2247496454&idx=1&sn=86a36688e01fe2141dae14b62f16be87&chksm=e9ceaafaede03562ae8839b81f7079609133dcbab1e9de952f5969d796ce4eb9a0ab83cce489&mpshare=1&scene=1&srcid=052749nlvA2cOV8sEvzBOMVy&sharer_shareinfo=b67653450ba8f7fd85a751488c65d40e&sharer_shareinfo_first=b67653450ba8f7fd85a751488c65d40e
author: "RaDesign RaDesign"
collected: 2026-05-27
tags: []
---

# Codex 这次更新，直接把“设计最后一公里”也补上了- Annotation

# Codex 这次更新，直接把"设计最后一公里"也补上了- Annotation

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIyOTc4NjE2NA==&mid=2247496454&idx=1) · RaDesign RaDesign


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FtAlIKXfSZiax24ia3Zic2KIfsrNyA8ib9MXHOTAH4G19DsYtefzgj0oPK386TrrL64oLra4Zia8icMRhlAIEBYBLxsByN10DpYGdYv0ADWicsrXsAY%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%23imgIndex%3D0)

这两天 OpenAI 又给 Codex 更新了一波能力，大家应该也都被刷屏了，现在更新 Codex 的内容越来越多，各种保姆级教程，足以说明它现在强到什么程度。以至于我最早我准备写的网页 0-1 上线的流程教程烂尾了，因为这些更新后，比我几个月前用的更简单了，会说话表达自己的诉求就行，根本不需要什么教程，所以还没动手的同学，不要想太多，玩两次你就上手了。

每次更新基本都是里面解决上一次更新的遗留问题，上次还在说生成的设计最后优化效果不行，这不就来了......

还是带大家快速过下这次主要更新了什么，然后我们重点聊下 Annotation 设计标注 - 像 Figma 一样编辑代码界面。

如果只看功能名，可能会觉得这次只是常规增强：

- Appshots、

- Goal Mode、

- 浏览器改进、

- 远程锁屏继续工作、

- 插件共享、

- 页面标注......

把这些能力放在一起，会发现 Codex 它不再只是一个"帮你写代码的聊天窗口"，而是在往真实的产品、设计、开发工作流里走。以前用 AI Coding，最麻烦的地方经常不是"AI 会不会写代码"，真正麻烦的是：

- 页面问题很难描述清楚；

- 一个复杂任务很难持续推进；

- 团队里的提示词、规范和工作流很难复用；

- UI 修改经常要靠一大段文字解释"到底改哪里"。

这次更新，基本都在解决这些问题。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FtAlIKXfSZiaxyDl3YialnBNy3arbobxeozxkNKgs9t1IRWNd3US5MgiaXMicrFzd7icG4T3uVDw2ScA5lq4JpTVicDDmDYuQIGbh3Hj9XUnOXD2A4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

## 这次 Codex 更新，核心信息先快速过一遍，Codex 正在从 "代码生成工具" ，变成一个能看现场、能持续执行、能接收视觉反馈、能沉淀团队工作流的 AI 协作系统。这次比较重要的更新主要有几类：

第一，Appshots

在 macOS 的 Codex App 里，可以通过快捷键把当前最前面的应用窗口发给 Codex。官方文档里提到，Appshots 可以包含当前窗口截图，以及该窗口可用的文本内容。你不需要再手动截图、复制页面文字、解释当前状态。

比如你正在看一个前端页面、Figma 设计稿、报错窗口、设置面板，直接把当前窗口交给 Codex，它就能拿到更接近"现场"的上下文。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FtAlIKXfSZiawVS0bN6rrhVQiblKMdyDCP4UicJ2O13D99wbEgNZ34ml9HwJLuqE62vuL1UXuRgfay33xhfVYIC9jYiaibQL45tJcmBHnH2AvA0BY%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

第二，Goal Mode

Goal Mode 现在已经在 Codex App、IDE extension 和 CLI 中可用。它的重点不是"写一个更长的 Prompt"，而是给 Codex 一个持续目标和完成标准。

比如不要只说：
> 帮我优化首页。

更适合说：
> 优化首页首屏加载性能，保持现有交互不变，定位主要性能瓶颈，完成后运行测试，并输出修改前后的性能对比。

这类描述里有目标、有边界、有验收条件，Codex 才更像是在围绕一个任务持续推进，而不是只回答你一轮。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FtAlIKXfSZiay1libIUsJOYicVjlqIvWY48TLoz7A8K8UODibiaqRRMtR9aHTCQeabxZ5ia8s76fYibDovbiaLxzpdz58mm0w1Gx2vic5aCvibt2lxiblcI%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

第三，浏览器能力继续增强

Codex 的 in-app browser 现在不只是打开网页预览，还可以用于点击、输入、检查渲染状态、截图、下载页面资源、运行只读页面检查脚本，以及验证页面修复结果。对于前端开发来说，这个方向很关键。

因为很多 UI 问题只有页面真正跑起来才看得出来。以前 AI 看代码是一层，浏览器真实效果又是另一层，中间总要靠人来回传话。

现在 Codex 开始把 "页面预览、页面反馈、代码修改、结果验证" 放到同一个工作流里。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FtAlIKXfSZiayGmIUfOvVx3tXWJKfXUOr7miczicaZ5PL0BnibfxvJ5M3JTaCia4YNDqL76vbu90MJaiagibkZiceImCvZMW0VczLeXJVMzfBbpcNy2U%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D4)

第四，插件共享和团队工作流。

企业和教育版的更新里还提到，团队可以共享本地构建的插件，管理员也能看到更多 Codex 使用分析。团队可以把自己的设计规范、代码规范、Review 流程、PRD 模板、项目约束沉淀成可复用的能力。

*** ** * ** ***

不过这篇文章最想重点说的，不是这些。我从我的角度来说，真正觉得这次最值得关注的，是 Annotation。

Annotation：UI 修改开始像设计批改一样自然

Codex 开始支持你直接在网页上标注，让 UI 修改更像设计批注而不是评论，看下图就知道了。

就是现在你可以直接在 Vibe coding 的网页或者 app 预览窗口，直接选择元素，就是你在 figma 里面改设计一样改，这太猛了！（虽然我早就也开发了类似的插件，我又慢了一步）

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FtAlIKXfSZiawDItAAPd5icf4YAGHSpl862EmZFwjjicBS004KDV5blYpYnT88HUzCe13BUGicxoZ2ibVfDdV8o4KnlIEBerIlt5ibVAhzvywd5VwM%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%23imgIndex%3D5)

上个版本我就说我已经基本不打开 Figma 了，很多群友还是反馈实现的效果不理想，还原度低，不好看不好调。这下解决了，虽然这次可能功能还不完整，但是下个版本如果把 Figma 的编辑能力都搬进来呢，阁下如何应对？

以前用 AI 改 UI，最累的其实不是"改"，而是"说清楚改哪里"。比如一个中后台页面里有很多区域：顶部筛选区、数据卡片、趋势图、表格、右侧详情、底部操作栏......

你想让 AI 改其中一个按钮，往往要先截图，再圈位置，再描述：

"不是左上角那个按钮，是表格右上方那个导出按钮。"

"不是整块卡片变小，是卡片里的指标数字层级太重。"

"不是整个页面重排，是这个筛选区和表格之间的间距太挤。"

这类反馈用文字描述非常别扭。因为 UI 问题本来就是视觉问题。人眼一看就知道哪里不对，但要把它翻译成 Prompt，就会变得很绕。

现在这个问题不存在，这就是 Annotation 的价值。

Codex 的 in-app browser 现在支持在页面上直接留下 comments。你可以打开页面，进入 Annotation mode，选中某个元素或区域，然后直接改，它就可以精准修改，指哪打哪。它让 Codex 从"听你描述页面"，变成"看着页面接收反馈"。这一步对前端开发、产品设计、Landing Page 调整、中后台系统、数据大屏、Figma 还原都很实用。

因为这些场景都有一个共同点：页面能不能用，很多时候不是代码逻辑问题，而是视觉沟通问题。

Codex 右侧预览窗口现在更像是一个编辑窗口，可以直接选择项目下对应的文件。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FtAlIKXfSZiayaOoXAib0AhGU6IlPK2xCovUraQQSzQyzbN57MiaCAqo4d21fFxUWWJoqCv6xiaTtAsniadJLJcrB0JImhpwyViahwuL5BZHJYGo0E%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D6)

它会自动定位你项目下面的内容，直接点击就可以预览。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FtAlIKXfSZiazxfAkqCH0BbxbNU1IWz411qsWZzV2gdf1MGib6Pb6Yy0ZA6RlznXEmk9CoGp1UUA0U8iaFhIx2Hd40VUJfSc2icXcOOicjQVFicLQw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D7)

点击注释，现在可以直接选中对应的元素，可以直接像Figma一样修改字号、字体、颜色、透明度... 操作方式和界面基本都和 Figma 的dev模式一样。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FtAlIKXfSZiaw0dDA9Cs4rOtic6jFia6sNRDs3fw0g1KMavPYIe8YkVYxMG7yBbLSadyh0Vyic6HdiaXQdRmMACGYrQCZumIiaVng4JW0AWfDiaQVOM%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D8)

同样的，选中图形元素，可以改圆角、边框、填充、效果等，直接就可以理解为，选中的是代码结构，但是编辑的能力是把Figma 的编辑搬进来了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FtAlIKXfSZiazaMRyvJ94Rrs6P0VySEIz3xsL7cMIC14CRE3JjfUCIwLOSxRBcpHia7Zv96Y85oOqoQh5SXQPDsUiadTMpqqFeFfg91RxCWr7mQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D9)

当然现在它还不能你改完后代码立即生效，还是以标记的形式，提交后，Codex 就会精准修改，设计和开发直接无缝衔接，后续的工作流变化将会更快更扁平。

## 这次更新背后的趋势

把这次 Codex 更新连起来看，方向其实很清楚。

- Appshots 解决的是"Codex 怎么理解你当前正在看的东西"。

- Goal Mode 解决的是"Codex 怎么围绕一个目标持续工作"。

- Browser improvements 解决的是"Codex 怎么进入真实页面里验证结果"。

- Plugin sharing 解决的是"团队怎么复用自己的 AI 工作流"。

- Annotation 解决的是"人怎么把视觉反馈准确交给 Codex"。

所以这次更新真正重要的，不是某一个按钮、某一个快捷键、某一个模式。而是 Codex 正在进入真实工作现场。它开始看页面、接收批注、理解视觉目标、执行修改、再回到浏览器验证结果。

这就是 AI Coding 下一阶段很重要的变化：

真的能参与产品、设计和前端、很快能替你跑完工作流的协作者。

尤其是用过这次更新的 Annotation。这个功能很小，但对和开发，或者是对设计有一些自己看法的人来说，非常实用，之前只能描述改，还要考虑一堆软件之间切换，交接问题，现在甚至很快，我一直在提的 Codex 基本可以、快要可以取代很多应用。

*** ** * ** ***

👉 如果觉得不错，随手点个赞、在看、转发三连

👉 如果想第一时间收到推送，也可以给我个星标 ⭐

👉 我们组了一群热爱探索的设计师，欢迎加入一起探索→

「 VibeCoding 设计实验室」

「 Image2 设计实验室」

「 GPT/CC/Gemini 拼车实验室」

> 来源: [mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzIyOTc4NjE2NA==&mid=2247496454&idx=1)
