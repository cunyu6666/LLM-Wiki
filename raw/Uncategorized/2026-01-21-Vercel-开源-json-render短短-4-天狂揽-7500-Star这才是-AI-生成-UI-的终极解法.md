---
id: "7413676180433274629"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247504904&idx=1&sn=260d3ebc8db1dffbed3e747d91a1b80c&chksm=c116d1456e6f189f9a7af6cbd2c51fa09c94916207f80c2dae044d8ae3d78be5d9aa65101c98&mpshare=1&scene=1&srcid=01215YZGSXEdkpxv4jmGb1mW&sharer_shareinfo=c0fb639c4620d28099871bbd100cf3b2&sharer_shareinfo_first=c0fb639c4620d28099871bbd100cf3b2
author: "痕小子 开源星探"
collected: 2026-01-21
tags: []
---

# Vercel 开源 json-render！短短 4 天狂揽 7500 Star，这才是 AI 生成 UI 的终极解法！

# Vercel 开源 json-render！短短 4 天狂揽 7500 Star，这才是 AI 生成 UI 的终极解法！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247504904&idx=1&sn=260d3ebc8db1dffbed3e747d91a1b80c&chksm=c116d1456e6f189f9a7af6cbd2c51fa09c94916207f80c2dae044d8ae3d78be5d9aa65101c98&mpshare=1&scene=1&srcid=01215YZGSXEdkpxv4jmGb1mW&sharer_shareinfo=c0fb639c4620d28099871bbd100cf3b2&sharer_shareinfo_first=c0fb639c4620d28099871bbd100cf3b2)痕小子 开源星探


如果你关注前端或 AI 圈，这几天一定被 Vercel 最新开源的 **json-render** 刷屏了。

四天时间，7500 Star。这不仅是火，这是"爆款"的节奏。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeLnPWxsuyes13BySE6dUtic5oNJl3oiaia84k4RdLzxAMv866nJgKhfdek2LjujGZicSGtDuIbRG4sc3Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)

究其原因是由于 Vercel 极其精准地踩中了当前 AI 应用开发最大的一个痛点：**生成式UI不可控** 。

以前我们让 AI 写界面，UI 结构一会儿一个样，组件乱飞，输出不可预测。Vercel Labs 发布的 **json-render** ，用一种极其优雅的工程化思路解决了这个问题。

**核心公式：AI → JSON → UI**

它不再让 AI 直接写代码，而是让 AI 生成符合特定 Schema 的 JSON 数据，然后前端根据这个 JSON，利用你已经写好的组件进行渲染。

它第一次把"AI 生成 UI"这件事，真正拉进了工程可控、可审计、可规模化的生产流程。

#### 核心机制

这个项目的精髓在于"约束"与"流式"的结合。

① Catalog

你需要先定义一个 catalog，告诉 AI：

*
  • 允许使用哪些组件
*
  • 每个组件有哪些 props（属性）
*
  • props 的类型、结构、枚举范围
*
  • 能触发哪些 action

比如：

*
  • 只能用 LineChart、StatCard、DataTable
*
  • LineChart 只能接收 data 和 color 两个参数。
*
  • 不允许自由写 JSX、不允许胡编组件

AI 在生成时，只能在这个清单里选组件，只能填这些参数，并生成标准的 Schema 用以校验。以此来彻底消灭幻觉，AI 绝对不会给你生成一个你没定义的 3DMap 组件。

② 流式渲染

传统的做法是：等 AI 把 JSON 全部生成完 -\> JSON.parse -\> 渲染。这中间会有几秒钟的白屏或加载动画。

json-render 支持增量解析。AI 吐出第一个字符，界面上可能就已经开始准备渲染卡片了。

用户感觉到的就是：字还没打完，界面就已经跳出来了。这种"无等待"的体验对于 B 端来说至关重要。

③ 反向生成源码

这是 Vercel 最懂开发者的地方。AI 生成的不仅是运行时的界面，它还内置了一个编译器。

它能基于当前的 JSON 和你的 Catalog，反向生成一份标准的 React 源码。你可以直接把这段代码下载到你的本地去部署。

#### 快速入手

官方已有一个线上可以演示的服务，浏览器输入 json-render.dev 就可体验。

比如我想：创建一个卡片式AI智能导航站。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeLnPWxsuyes13BySE6dUtic5dqMSiahVDbjbZibDXF7ibHMY8z7sWlcETBCQ4Agf58Aa5LKZ8QF3ZibAYw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

他就能立马给我设计一个通过内置规定的一些组件，以此生成 JSON 数据，再渲染到页面上。

也可以将关键代码拷贝或下载进行本地复用。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FNjA8gwicXyeLnPWxsuyes13BySE6dUtic50nCPcVCC1LwjK2vJxbfib5fC6hrfE55jhrsHJAWkF9VIeMHKE2zLqdA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

如果想要在本地搭建演示服务，可执行以下指令：

    git clone https://github.com/vercel-labs/json-render
    cd json-render
    pnpm install
    pnpm dev

其中：

*
  • http://localhost:3000 --- 文档和演示区
*
  • http://localhost:3001 --- 示例仪表板

如要在你实际的项目中引入该功能，需要安装 json-render。

安装指令：

    npm install @json-render/core @json-render/react

定义Catalog：

    import { createCatalog } from '@json-render/core';
    import { z } from 'zod';const
     catalog = createCatalog({
      components: {
        Card: {
          props: z.object({ title: z.string() }),
          hasChildren: true,
        },
        Metric: {
          props: z.object({
            label: z.string(),
            valuePath: z.string(),      // Binds to your data
            format: z.enum(['currency', 'percent', 'number']),
          }),
        },
        Button: {
          props: z.object({
            label: z.string(),
            action: ActionSchema,        // AI declares intent, you handle it
          }),
        },
      },
      actions: {
        export_report: { description: 'Export dashboard to PDF' },
        refresh_data: { description: 'Refresh all metrics' },
      },
    });

注册组件：

    const registry = {
      Card: ({ element, children }) => (
        <div className="card">
          <h3>{element.props.title}</h3>
          {children}
        </div>
      ),
      Metric: ({ element }) => {
        const value = useDataValue(element.props.valuePath);
        return <div className="metric">{format(value)}</div>;
      },
      Button: ({ element, onAction }) => (
        <button onClick={() => onAction(element.props.action)}>
          {element.props.label}
        </button>
      ),
    };

AI 生成：

    import { DataProvider, ActionProvider, Renderer, useUIStream } from '@json-render/react';function
     Dashboard() {
      const { tree, send } = useUIStream({ api: '/api/generate' });  return
     (
        <DataProvider initialData={{ revenue: 125000, growth: 0.15 }}>
          <ActionProvider actions={{
            export_report: () => downloadPDF(),
            refresh_data: () => refetch(),
          }}>
            <input
              placeholder="Create a revenue dashboard..."
              onKeyDown={(e) => e.key === 'Enter' && send(e.target.value)}
            />
            <Renderer tree={tree} components={registry} />
          </ActionProvider>
        </DataProvider>
      );
    }

#### 适用场景

*
  • 数据分析仪表盘
*
  • 电商营销配置后台
*
  • 动态表单/问卷
*
  • 展会/大屏可视化
*
  • 内部运营工具

凡是你不想手写、但又不能乱写 UI 的地方，json-render 都是非常理想的底座。

#### 写在最后

AI 天生是自由发挥型选手，而 UI 是强约束工程产物。

json-render 干的事，就是在这两者之间建了一条「硬管道」。

对于我们开发者来说，这不仅仅是一个工具，更是一种思维方式的转变。

以前我们写前端，是写"页面"；以后我们写前端，是写"组件库"和"约束规则Schema"。

而剩下的组装工作交给 AI 就好了。

GitHub：
> https://github.com/vercel-labs/json-render


![](https://image.cubox.pro/cardImg/4b5uzdwlzim32fi21mqn4gb4p09jfaphbqk26wxxock1xs0pv7?imageMogr2/quality/90/ignore-error/1)

**开源星探**

专注于分享GitHub上优质、有趣、实用的开源项目、工具及学习资源，为互联网行业爱好者提供优质的科技技术资讯。

615篇原创内容

<br />

公众号  

，

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNjA8gwicXyeKqAjyn8A3ob9xT4DDY8DB3JCvIaM6JKWXFsgCxznXicJhpRYJ5MIPb9xvgGA4WYhPagIKorlScib0Q%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D3)

如果本文对您有帮助，也请帮忙点个 赞👍 + 在看 哈！❤️


**在看你就赞赞我！**

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FNjA8gwicXyeLZdEkueqhds4y07sImrPvibkDIsnVCibl5ibS6jSiccRh6RtH8ZqBPBWSib0kn7Ep6mP5YPJCJkraJ3kw%2F640%3Fwx_fmt%3Dgif%23imgIndex%3D4)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ==&mid=2247504904&idx=1&sn=260d3ebc8db1dffbed3e747d91a1b80c&chksm=c116d1456e6f189f9a7af6cbd2c51fa09c94916207f80c2dae044d8ae3d78be5d9aa65101c98&mpshare=1&scene=1&srcid=01215YZGSXEdkpxv4jmGb1mW&sharer_shareinfo=c0fb639c4620d28099871bbd100cf3b2&sharer_shareinfo_first=c0fb639c4620d28099871bbd100cf3b2)

