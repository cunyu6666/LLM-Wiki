---
id: "7421062489774755820"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzU0NzkwOTE0MQ==&mid=2247483845&idx=1&sn=81957e988790c077c984c0e8e4c3d12c&chksm=fa9e140deff778160cdebcd5a769d109dcdd3bb439b905be0a2f9df71fe1c90e412b557c7e44&mpshare=1&scene=1&srcid=0211jYiFaJlqxujdZlNjywnu&sharer_shareinfo=c1c99a9a17e57ac2fd651b715fcd2069&sharer_shareinfo_first=c1c99a9a17e57ac2fd651b715fcd2069
author: "CoderBuffer CoderBuffer"
collected: 2026-02-11
tags: []
---

# 从A2UI到Json-Render！AI可能真的要改变应用的交互方式了！！

# 从A2UI到Json-Render！AI可能真的要改变应用的交互方式了！！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0NzkwOTE0MQ==&mid=2247483845&idx=1&sn=81957e988790c077c984c0e8e4c3d12c&chksm=fa9e140deff778160cdebcd5a769d109dcdd3bb439b905be0a2f9df71fe1c90e412b557c7e44&mpshare=1&scene=1&srcid=0211jYiFaJlqxujdZlNjywnu&sharer_shareinfo=c1c99a9a17e57ac2fd651b715fcd2069&sharer_shareinfo_first=c1c99a9a17e57ac2fd651b715fcd2069)CoderBuffer CoderBuffer


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amtoolU3kbFR77XNQ6libRsXiafzWNiatlLC809IakL1ic5cNK0KqVyG3daxAQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)  


从Google发布A2UI协议，到Vercel在GitHub发布Json-Render，也许AI实时生成交互应用的时代真的快要来临了。快来一起了解下完整的故事脉络吧，后半部分有案例实战嗷。

## 什么是A2UI？

**A2UI** （Agent-to-User Interface，智能体到用户界面）是一个开放协议，旨在让 AI 智能体能够以安全、原生且高性能的方式驱动用户界面。

简而言之：**让远程AI智能体在不向客户端发送危险的可执行代码的情况下，生成复杂的交互式界面**

它的工作流程如下：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amto8M4tlMFBz0pDjTyPOjsdeC1mnrmaJ2jCY21Ac4f2swKibYqMgjwHXxA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

1.
   用户与AI智能体应用交流
2.
   智能体生成A2UI Message（描述了UI）
3.
   流式Message响应到客户端（JsonLine）
4.
   客户端通过预定义本地组件渲染（Angular, Flutter, React, etc.）
5. **用户与UI交互，发送操作给Agent**
6.
   AI智能体生成下一个A2UI Message（循环）


A2UI 与你使用的底层大模型或编排框架（如 LangChain、AutoGen、PydanticAI 等）无关。它的核心作用是作为智能体循环（Agent Loop）中的 **"输出层"** ------ 将智能体的决策转化为用户可以交互的界面。

在传统的 Web 开发中，开发者会编写静态代码。而在 A2UI 中，智能体扮演的是**即时 UI 设计师** 的角色。它关注的是 布局、结构、组件元信息、数据、动作，而不是具体的HTML、CSS和JS。

    {  "a2ui": "1.0",  "component": "Card",  "props": {    "title": "股票报价",    "content": "AAPL 目前价格为 $185.92"  }}


## 如何编写 A2UI 有效载荷？

一个有效的 A2UI 消息包含以下几个核心部分：

1. **version** : A2UI 协议版本。

2. **component** : 要渲染的组件名称（例如 Button, Container, LineChart）。

3. **props** : 传递给组件的参数（如 label, color, value）。

4. **children** (可选): 嵌套在其中的其他组件数组。

5. **action** (可选): 定义当用户与组件交互时（如点击按钮）应触发的操作。


    {  "a2ui": "0.9",  "type": "updateComponents",  "payload": {    "components": [      {        "id": "btn_1",        "name": "Button",        "props": {          "label": "确认预订",          "variant": "primary"        }      }    ]  }}


### A2UI使用邻接表来定义组件关系，而不是用嵌套的Tree。这样能够更好进行流式渲染（生成JsonLine）。

这意味着组件是作为**扁平列表** 发送的，通过 children 属性中的 ID 相互引用。

### 为什么使用这种结构？

1. **流式友好：** 智能体可以先发送父组件，随后再发送子组件，而无需重新发送整个树。

2. **局部更新：** 如果一个深层嵌套的按钮需要改变颜色，智能体只需发送该按钮的 ID 和新属性，而不需要发送整个页面布局。

3. **大语言模型 (LLM) 效率：** 对于 LLM 来说，生成扁平的 JSON 结构比生成深度嵌套的结构更不容易出错。


    {  "surfaceUpdate": {    "components": [      {"id": "root", "component": {"Column": {"children": {"explicitList": ["greeting", "buttons"]}}}},      {"id": "greeting", "component": {"Text": {"text": {"literalString": "Hello"}}}},      {"id": "buttons", "component": {"Row": {"children": {"explicitList": ["cancel-btn", "ok-btn"]}}}},      {"id": "cancel-btn", "component": {"Button": {"child": "cancel-text", "action": {"name": "cancel"}}}},      {"id": "cancel-text", "component": {"Text": {"text": {"literalString": "Cancel"}}}},      {"id": "ok-btn", "component": {"Button": {"child": "ok-text", "action": {"name": "ok"}}}},      {"id": "ok-text", "component": {"Text": {"text": {"literalString": "OK"}}}}    ]  }}


*** ** * ** ***


A2UI如何处理交互 (Interactivity)？

A2UI 不仅仅是展示。你可以定义 actions，当用户点击或提交时，这些操作会发回给智能体：

* **回传 (Callback)：** 客户端向智能体发送一条隐式消息（例如："用户点击了支付按钮"）。

* **路由 (Routing)：** 客户端导航到另一个 UI 页面。

* **工具触发 (Tool Trigger)：** 用户在 UI 上的操作直接触发智能体的另一个函数。


A2UI 不仅仅是一个 JSON 格式，它是一个**通信协议** 。它解决了 AI 时代的一个关键矛盾：如何在保持安全性的同时，让远程智能体拥有构建复杂、美观且响应式界面的能力。

## 为了保持生态系统的整洁和高性能，请遵循以下原则：

* **命名规范：** 使用大驼峰命名法（PascalCase），例如 UserProfile 而非 user_profile。

* **属性解耦：** 尽量保持 props 扁平化且简单。只传递数据，不要传递复杂的逻辑或序列化的代码。

* **默认值：** 在客户端代码中为属性提供健壮的默认值，以防智能体遗漏了某些参数。

* **文档化：** 为你的自定义组件维护一份简单的 JSON Schema 或文档，以便你可以轻松地将其喂给不同的大语言模型。

开发 A2UI 智能体的关键在于**解耦** ：

1. **智能体** 负责逻辑、数据检索和决定 UI 结构（JSON）。

2. **协议** 负责安全地传输这些结构。

3. **客户端** 负责最终的样式渲染和平台适配。

虽然 A2UI 提供了一套标准的跨平台组件（如容器、文本、按钮等），但该协议真正的强大之处在于其**可扩展性** 。你可以定义特定于你业务领域的自定义组件，并让智能体（Agent）像使用标准组件一样驱动它们。

自定义组件的工作原理是将 **JSON 标识符** 映射到 **客户端代码实现** ：

1. **定义 (Implementation)：** 你在客户端（Web、Flutter、移动端）编写一个原生 UI 组件。

2. **注册 (Registration)：** 你将该组件注册到 A2UI 的渲染器中，并赋予它一个唯一的名称（例如 "StockTicker"）。

3. **生成 (Generation)：** 智能体在生成的 JSON 有效载荷中使用这个名称。

4. **渲染 (Rendering)：** A2UI 渲染器识别出该名称，并将 JSON 中的 props 传递给你的原生组件。


说了这么多，如何才能集成A2UI到你的Agent应用中？

将 A2UI 引入你的智能体主要有两种模式：**工具调用 (Tool Calling)** 和 **结构化输出 (Structured Output)** 。

### 模式 A：工具调用

这是最常用的方法。你为智能体提供一个名为 render_ui 的工具。

* **工作原理：** 智能体决定何时需要展示界面（例如展示图表、表格或确认表单），然后调用该工具。

* **优点：** 允许智能体在同一个对话中混合使用文本响应和 UI 响应。

**提示词示例：**
> "你可以使用 render_ui 工具来显示交互式组件。当你需要展示数据分析、复杂的列表或需要用户确认的操作时，请使用此工具。"

### 模式 B：结构化输出

在这种模式下，你强制模型始终（或在特定条件下）根据 JSON Schema 输出 A2UI 格式的数据。

* **工作原理：** 利用 OpenAI 的 response_format: { type: "json_object" } 或 Anthropic 的工具强制调用功能。

* **优点：** 保证了 100% 的机器可读性，非常适合构建纯图形化界面的智能体（如仪表盘生成器）。


也就是说我们仍然是通过提示词约束AI响应符合A2UI规范的响应。当然。A2UI的协议是精简的，而不是完整的DomTree。

提示词工程 (Prompt Engineering) 建议

为了让 LLM 更好地生成 A2UI，建议在系统提示词（System Prompt）中加入以下内容：

* **提供组件库清单：** 告诉模型客户端支持哪些组件（如：DataTable, SummaryStat, Calendar）。

* **强调简洁性：** 提醒模型只发送必要的数据，不要生成冗余的样式代码，因为样式由客户端处理。

* **上下文关联：** 鼓励模型在 UI 旁边提供简短的文本解释。


Json-Render实战

接下来我们让我们了解下Json-Render中，并用它去实现一个创建"服务器"的案例：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amtoXARBYicKRHkKGrAv3Sk0iaTicfVmxYfiaOUGDYKo8DPa2U6UweLrqdBZ1A%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

JSON-Render由Vercel于2026/01/15日发布，是符合A2UI理念的一个实现，但注意它仍然还没完全支持A2UI规范。

json-render 让终端用户能够通过自然语言提示词生成 UI ------ 且安全地限制在你定义的组件范围内。通过预先设定限制规则，比如：存在哪些组件、它们接受哪些属性（Props）、有哪些可用的动作（Actions）。AI 生成符合你模式（Schema）的 JSON，而你的组件会对其进行原生渲染。

## 工作原理

1. **定义护栏** ------ 设定 AI 可以使用哪些组件、动作和数据绑定。

2. **用户输入提示词** ------ 终端用户用自然语言描述他们想要的内容。

3. **AI 生成 JSON** ------ 输出始终是可预测的，且受限于你的组件目录。

4. **快速渲染** ------ 随着模型响应进行流式传输和渐进式渲染。


理念和上面提到的A2UI一致，接下来看下代码实现：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amtoicpmHOo4aViaRBcicemib27qa2QxXbAxScALo2pfic6HMVGeMKUNbD0OIoQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

首先我们需要在客户端注册组件的样式和布局（这里组件是一个整体，后期各大组件库都有可能发布自己的A2UI基础组件）。

而AI需要的是组件的元信息，这里称之为catalog，它是组件的目录和约束规范，也是需要配置成提示词给AI的。它目前主要关注以下三个方面：

* **组件** --- Agent可以创建的界面元素；

* **操作** --- Agent可以触发的功能；

* **验证函数** --- 用于表单输入的自定义校验规则。


本案例完整catalog内容如下：

    // catalog.ts - 定义 AI 可以使用的组件目录import { createCatalog } from '@json-render/core';import { z } from 'zod';export const catalog = createCatalog({  components: {    // Card 组件 - 可容纳子元素    Card: {      props: z.object({        title: z.string(),        description: z.string().nullable(),      }),      hasChildren: true,    },    // Metric 组件 - 展示指标数据    Metric: {      props: z.object({        label: z.string(),        valuePath: z.string(), // 绑定到数据源的 JSON Pointer 路径        format: z.enum(['currency', 'percent', 'number']),      }),    },    // Button 组件 - 触发动作    Button: {      props: z.object({        label: z.string(),        action: z.string(),        variant: z.enum(['primary', 'secondary', 'danger']).default('primary'),      }),    },    // Text 组件 - 显示文本    Text: {      props: z.object({        content: z.string(),        size: z.enum(['sm', 'base', 'lg', 'xl']).default('base'),      }),    },    // Grid 组件 - 网格布局    Grid: {      props: z.object({        columns: z.number().min(1).max(4).default(2),      }),      hasChildren: true,    },    // Chart 组件 - 显示图表（简化版）    Chart: {      props: z.object({        type: z.enum(['bar', 'line', 'pie']),        title: z.string(),        dataPath: z.string(),      }),    },  },  // 定义可用的动作  actions: {    confirm_order: {      description: '确认订单配置',      params: z.object({}),    },  },});


通过上面代码我们可以看到它定义了组件的名称，组件的属性类型和名称，以及对应数据源的JsonPoint数据路径。JsonPoint是一种规范，通过路径读取JSON数据。

    // Given this data:{  "user": {    "name": "Alice",    "email": "alice@example.com"  },  "metrics": {    "revenue": 125000,    "growth": 0.15  }}
    // These paths access:"/user/name"        -> "Alice""/metrics/revenue"  -> 125000"/metrics/growth"   -> 0.15


那么如何渲染AI响应的JSON呢，参考下面代码：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amtoficmRy2mF2PsvleotCo7O5WHnsyAsbC70icpiaxZ5LCxTZfVibulxOKsYA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

通过DataProvider我们可以传入默认数据，可以立即为select元素的默认option，以及当表单变化时的触发事件，用于保存我们需要的数据。

ActionProvider提供本地的catelog action实现，当用户点击AI响应的UI元素时，比如某个button，Json-Render会自动调用同名的action handler来处理（所以对于AI来说，语义比魔法值更重要）。

最核心的是Renderer负责渲染AI响应的UI，将Json渲染成UI。一个模拟AI响应JSON可能如下：

    {  root: 'form-card',  elements: {    'form-card': {      key: 'form-card',      type: 'Card',      props: {        title: '�️ 服务器配置',        description: '请选择您需要的服务器规格',      },      children: ['cpu-select', 'memory-select', 'storage-select', 'confirm-btn'],      parentKey: null,    },    'cpu-select': {      key: 'cpu-select',      type: 'Select',      props: {        label: 'CPU 规格',        options: ['2核', '4核', '8核', '16核'],        valuePath: '/server/cpu',      },      parentKey: 'form-card',    },    'memory-select': {      key: 'memory-select',      type: 'Select',      props: {        label: '内存大小',        options: ['4GB', '8GB', '16GB', '32GB'],        valuePath: '/server/memory',      },      parentKey: 'form-card',    },    'storage-select': {      key: 'storage-select',      type: 'Select',      props: {        label: '存储空间',        options: ['100GB SSD', '200GB SSD', '500GB SSD', '1TB SSD'],        valuePath: '/server/storage',      },      parentKey: 'form-card',    },    'confirm-btn': {      key: 'confirm-btn',      type: 'Button',      props: {        label: '确认配置',        action: 'confirm_order',        variant: 'primary',      },      parentKey: 'form-card',    },  },}


Stream JsonLine形式格式如下（本次案例没有通过此形式）：

    {"op":"set","path":"/root","value":{"key":"root","type":"Card","props":{"title":"Dashboard"}}}{"op":"add","path":"/root/children","value":{"key":"metric-1","type":"Metric","props":{"label":"Revenue"}}}{"op":"add","path":"/root/children","value":{"key":"metric-2","type":"Metric","props":{"label":"Users"}}}


具体可参考官方文档：https://json-render.dev/

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amto8EK0WzXQlBKcWD4LnHqicnST35SpQyuYYlINMeuIV6PDQfpmPcjdaAA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

Json-Render同时提供了根据catalog生成提示词功能：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amtoVuyhdvB9EJawibjtWkqSOKM12Xia4LEibAu3yw4qJibwLLicBFDaibDvtmFg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

将提示词传输给AI，可获得实际的Json。

最终案例效果展示：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNtGWMOKwsbNhl0iakqrqqqicDwpva0amtoqNv0ToMyAlpS6z3rLWqyiaFibz5Y7blLMBy7UMmwEU3O1b5xYVsWmnZQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg%23imgIndex%3D7)

结语：我想通过集成A2UI，以后会诞生很多新兴的AI应用，A2UI也会重塑现有的工作流体系，虽然现在还在起步阶段，但是AI的世界日新月异，提前学习储备这些知识，未尝不是一种对自己的投资。

读者老爷们，这是一个新的AI技术前沿资讯（channel）合集，包含AI生态发展，AI工具分享，技术实战，感兴趣关注点赞，此合集将持续更新。

本次案例源码后台发送"jsonrender"获取。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNtGWMOKwsbODXTrgU7ialZlod1xVZ7Jon5sCib5lRpnJk5pqFK3A0DsyZU2AhFlLRkY5qzIKg9qEGMHhuhibgicM7Q%2F300%3Fwx_fmt%3Dpng%26wxfrom%3D19&valid=false)

**CoderBuffer**

分享AI Stack，系统架构，技术研发，云原生，云计算相关

4篇原创内容

<br />

公众号  

，

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0NzkwOTE0MQ==&mid=2247483845&idx=1&sn=81957e988790c077c984c0e8e4c3d12c&chksm=fa9e140deff778160cdebcd5a769d109dcdd3bb439b905be0a2f9df71fe1c90e412b557c7e44&mpshare=1&scene=1&srcid=0211jYiFaJlqxujdZlNjywnu&sharer_shareinfo=c1c99a9a17e57ac2fd651b715fcd2069&sharer_shareinfo_first=c1c99a9a17e57ac2fd651b715fcd2069)

