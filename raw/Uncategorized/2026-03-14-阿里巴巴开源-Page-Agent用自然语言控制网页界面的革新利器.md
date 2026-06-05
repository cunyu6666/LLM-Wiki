---
id: "7432480008716685232"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzI2NjY5MjQzNQ==&mid=2247483834&idx=1&sn=c1b84653cf04c6d2f5ae0588cc7cf3a0&chksm=eb0f72c3a0cb69f424db0fcbacdf26ccbcab915bff4dd06b3b0f3ac073d10c90b296193b332a&mpshare=1&scene=1&srcid=0314nAXh6Cvgmn3qcAt54AK1&sharer_shareinfo=41420c570c43931608addf408488906e&sharer_shareinfo_first=41420c570c43931608addf408488906e
author: "未来基因派 未来基因派"
collected: 2026-03-14
tags: []
---

# 阿里巴巴开源 Page-Agent：用自然语言控制网页界面的革新利器

# 阿里巴巴开源 Page-Agent：用自然语言控制网页界面的革新利器

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI2NjY5MjQzNQ==&mid=2247483834&idx=1&sn=c1b84653cf04c6d2f5ae0588cc7cf3a0&chksm=eb0f72c3a0cb69f424db0fcbacdf26ccbcab915bff4dd06b3b0f3ac073d10c90b296193b332a&mpshare=1&scene=1&srcid=0314nAXh6Cvgmn3qcAt54AK1&sharer_shareinfo=41420c570c43931608addf408488906e&sharer_shareinfo_first=41420c570c43931608addf408488906e)未来基因派 未来基因派


在人工智能浪潮席卷全球的今天，如何让 AI 技术与 Web 应用深度融合一直是开发者们探索的核心命题。就在近期，阿里巴巴正式开源了一款名为 **Page-Agent** 的 JavaScript 库，它能够赋予网页"智能大脑"，让用户通过自然语言就能操控任意 Web 界面。这款工具的出现，标志着 Web 端 AI 代理技术迈入了一个全新的发展阶段。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F7S0yOPibNEGDhZHSZ6WmhnwC2sNaRwUq5kXzS3fD6gjt2Bo366s90npv0AQwcw03YZmKDX1wkBrDIGv8AaZf1PFyxHs9PaMIcOCGB6bIzSP4%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

## 一、Page-Agent 是什么

Page-Agent 是一款嵌入式的 GUI Agent（图形用户界面智能体），它可以直接运行在网页内部，让任何网站都拥有 AI 控制能力。与传统的浏览器自动化工具不同，Page-Agent 从一开始就是为 Web 开发者和 Web 应用量身打造的。

想象一下这样的场景：用户不再需要繁琐地点击多个按钮、填写各种表单，只需对 着网页说一句"帮我登录并提交这份报表"，AI 就能自动完成所有操作。这正是 Page-Agent 想要实现的愿景------让网页交互变得像说话一样简单。

从技术架构来看，Page-Agent 完全运行在客户端，不需要任何后端支持。它采用"自带密钥"（Bring Your Own Key）的架构设计，开发者只需引入相应的 JavaScript 库，配置好大语言模型的 API 接口，就能在自己的网页中集成这个强大的 AI 代理。目前该项目已在 GitHub 上获得超过 2900 颗星标，足以见得其受欢迎程度。

## 二、核心特性解析

Page-Agent 之所以能够在众多同类产品中脱颖而出，主要归功于其四大核心特性。

**智能 DOM 分析** 是 Page-Agent 的第一大亮点。它采用了高强度的 DOM 脱水技术，不需要任何视觉识别，仅通过纯文本方式就能快速精准地定位页面元素并执行操作。这意味着即使用户的网页没有精美的视觉设计，Page-Agent 依然能够准确理解页面结构并完成指令。

**安全可控** 是企业在选择技术方案时最为关注的维度之一。Page-Agent 提供了操作白名单机制，开发者可以精确控制 AI 能够执行哪些操作；同时还支持数据脱敏保护，有效防止敏感信息泄露。更贴心的是，开发者还能注入自定义知识库，让 AI 按照特定的规则和逻辑来工作，这对于业务场景复杂的企业级应用来说尤为重要。

**零后端依赖** 让 Page-Agent 的部署变得异常简单。开发者既可以通过 CDN 引入，也可以使用 NPM 包管理工具进行安装，然后只需配置自己的大语言模型端点即可正常工作。这种轻量级的集成方式大大降低了使用门槛，让中小型项目也能轻松享受 AI 带来的便利。

**无障碍智能** 是 Page-Agent 的又一重要应用方向。它能为复杂的 B2B 系统和管理后台提供自然语言交互接口，这对于视力障碍用户、老年用户群体来说意义重大。通过与屏幕阅读器或语音助手的结合，Page-Agent 能够让任何人都能轻松使用复杂的 Web 应用，真正践行科技普惠的理念。

## 三、简单易用的集成方式

对于开发者而言，Page-Agent 最令人惊叹的地方在于其极简的集成方式。只需要几行代码，就能让网页拥有 AI 控制能力。

### 最简入门示例

首先，通过 npm 安装 page-agent 包：

```
npm install page-agent 
```

然后在 JavaScript 代码中引入并初始化：

```
import { PageAgent } from 'page-agent'; 

const agent = new PageAgent({ 

  model: 'qwen3.5-plus', 

  baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1', 

  apiKey: 'YOUR_API_KEY', 

  language: 'zh-CN' 

}); 

// 让AI执行自然语言指令 

await agent.execute('点击登录按钮'); 
```

这就是全部代码量------仅需三行核心代码，你的网页就拥有了一个能够理解自然语言的 AI 助手。用户只需通过语音或文字发出指令，AI 就能自动分析页面结构并完成相应操作。

### 支持多种大模型

Page-Agent 对大语言模型的兼容性非常出色，目前已经过测试的模型包括：阿里云 Qwen 系列（含 qwen3.5-plus、qwen3.5-flash 等推荐型号）、OpenAI GPT 系列、Google Gemini 系列、Anthropic Claude 系列、DeepSeek 系列、MoonshotAI Kimi 系列等。这意味着开发者可以根据自己的需求和预算灵活选择合适的模型。

## 四、典型应用场景

了解了 Page-Agent 的技术特性后，让我们来看看它在实际业务中的典型应用场景。

**SaaS AI 副驾驶** 是最具商业价值的应用方向之一。几行代码就能为你的产品加上 AI 副驾驶功能，无需重写后端代码。无论是客户管理系统、内容编辑平台还是协作工具，都可以快速集成 AI 助手，让用户在产品内直接获得智能辅助体验，大幅提升产品竞争力和用户黏性。

**智能表单填写** 是 Page-Agent 的杀手级应用。想象一下，原本需要 20 次点击、填写十几个字段的复杂表单，现在只需对 AI 说一句"帮我填写这份客户登记表"，AI 就能自动识别表单结构并完成填写。这对于 ERP、CRM、管理后台等需要大量数据录入的场景来说，简直是效率神器。

**跨页面 Agent** 是另一个强大的功能。通过可选的 Chrome 扩展，你可以让 AI Agent 跨越多个浏览器标签页工作。比如让 AI 在电商平台上搜索商品、比价、然后完成下单，这种跨流程的自动化能力为商业场景带来了更多可能性。

**legacy 系统现代化改造** 是企业在发展过程中经常面临的挑战。企业往往积累了大量年代久远的内部系统，这些系统操作复杂、界面陈旧，员工培训成本高昂。通过引入 Page-Agent，可以将这些老旧系统快速升级为具有 AI 交互能力的现代化应用，让新员工也能轻松上手，预计能够显著降低企业的支持成本并提升员工满意度。

**无障碍增强** 对于提升产品包容性至关重要。用自然语言让任何网页实现无障碍访问，视障用户可以借助屏幕阅读器和语音指令轻松操作网页。这不仅是社会责任的体现，在某些国家和地区更是法律合规的要求。

**交互式培训与演示** 在企业内部培训中具有巨大价值。比如新员工想知道"如何提交报销单"，AI 可以直接在真实的系统界面上演示完整流程，比看文档或看视频教程要直观得多。这种"做中学"的方式能够大幅提升培训效率和效果。

## 五、与 Browser-Use 的对比

提到 GUI Agent，不得不提另一个知名项目 Browser-Use。那么 Page-Agent 与它相比有什么不同呢？

从部署方式来看，Page-Agent 是嵌入到网页中的组件形式，而 Browser-Use 是作为外部工具运行；从作用范围来看，Page-Agent 专注于当前页面，而 Browser-Use 可以控制整个浏览器；从目标用户来看，Page-Agent 主要面向 Web 开发者，强调为 Web 应用增强用户体验，而 Browser-Use 更适合自动化脚本和爬虫开发者。

简单来说，如果你的目标是提升自己产品的用户体验，让用户能更便捷地操作你的网站，那么 Page-Agent 是更好的选择；如果你需要自动化执行跨网站的批量任务，Browser-Use 可能更合适。

## 六、总结与展望

Page-Agent 的出现为 Web 应用的智能化升级提供了一条全新的思路。它将原本只存在于实验室或大型科技公司的 AI 代理技术，以开源轻量的方式带到了每一位 Web 开发者的手中。随着技术的不断成熟和社区的持续贡献，我们有理由相信，未来的 Web 交互将会变得更加智能、便捷和人性化。

无论你是希望提升产品竞争力的创业者，还是致力于优化用户体验的前端工程师，Page-Agent 都值得你花时间去了解和研究。这或许就是 Web 应用下一个风口的开始。

*** ** * ** ***

**参考资料：**

\[1\] GitHub - alibaba/page-agent

\[2\] PageAgent.js 官方文档

\[3\] Page-Agent Models 配置文档

*** ** * ** ***

如果你觉得这篇文章对你有帮助，欢迎**点赞** 、**收藏** 、**转发** 给身边的朋友一起学习！

如果你对 Page-Agent 还有其他疑问，或者想了解更多 AI 前沿技术，欢迎在评论区留言交流。也欢迎**关注** 我，我会持续为大家带来更多优质的技术内容。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI2NjY5MjQzNQ==&mid=2247483834&idx=1&sn=c1b84653cf04c6d2f5ae0588cc7cf3a0&chksm=eb0f72c3a0cb69f424db0fcbacdf26ccbcab915bff4dd06b3b0f3ac073d10c90b296193b332a&mpshare=1&scene=1&srcid=0314nAXh6Cvgmn3qcAt54AK1&sharer_shareinfo=41420c570c43931608addf408488906e&sharer_shareinfo_first=41420c570c43931608addf408488906e)

