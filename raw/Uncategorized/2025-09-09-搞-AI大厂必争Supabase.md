---
id: "7364960688915089821"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzAxNjk5NjI1Mg==&mid=2247484046&idx=1&sn=6150ebc39ace0872819fbf9198e5d28f&chksm=9a73787f1bd3025fc4e73eb3033a5f866cd776c80b76cb70782f317325564dcfdbdc344b0daf&mpshare=1&scene=1&srcid=0909XVHDNAaHQdYkoYSrwmEk&sharer_shareinfo=15c854b37364591a8eaac5983bbf82f8&sharer_shareinfo_first=15c854b37364591a8eaac5983bbf82f8
author: "飞哥 飞哥专栏"
collected: 2025-09-09
tags: []
---

# 搞 AI，大厂必争Supabase

# 搞 AI，大厂必争Supabase

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxNjk5NjI1Mg==&mid=2247484046&idx=1&sn=6150ebc39ace0872819fbf9198e5d28f&chksm=9a73787f1bd3025fc4e73eb3033a5f866cd776c80b76cb70782f317325564dcfdbdc344b0daf&mpshare=1&scene=1&srcid=0909XVHDNAaHQdYkoYSrwmEk&sharer_shareinfo=15c854b37364591a8eaac5983bbf82f8&sharer_shareinfo_first=15c854b37364591a8eaac5983bbf82f8)飞哥 飞哥专栏

> 大厂为什么都在布局Supabase，一切为了基础AI设施。

## 大厂的Supabase布局

*
  阿里云推出了 Supabase服务
*
  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F20JHa4P2JY7yAHkQkToG16IjTQlutl7EoyMEIvicwO7OTGk74Hr1p0E0yo4RPURPXGz99oaf0YLqc3qY9ZMQNKg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

<!-- -->

* 腾讯 CodeBuddy 直接和 Supabase集成

* 字节 Trae Solo也是集成的 Supabase

*
  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F20JHa4P2JY7yAHkQkToG16IjTQlutl7EicDNLoNCprEuULaJUKhwGdxDDC7f96k3TrHK41dkFIKo1MjmuErO3mg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

<!-- -->

*
  n8n、Dify.ai天然集成Supabase
*
  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F20JHa4P2JY7yAHkQkToG16IjTQlutl7EmaIvxDp4SdSK34VSxTc6tHtuqvj5Wk8CJULtyZ6otfiaCV4AM0YzW2Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

  ![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F20JHa4P2JY7yAHkQkToG16IjTQlutl7EMKQZCWHpHJhoOuaFbiaHlYxRLvESPO6LXuaSYTiaibrseTia2pqcaiawGAQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

## Supabase 介绍


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F20JHa4P2JY7yAHkQkToG16IjTQlutl7Ef7mmiaibKLptHgbUHHRgOS3shR9R66rnt95M7mA10JaW8FXiavDibK6fnQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

Supabase 作为列后端即服务（BaaS）的开源 Firebase 替代品，目前github 已有86.8K, 基于 PostgreSQL 数据库构建，帮助开发者快速构建应用。

**PostgreSQL 数据库**

Supabase 使用 PostgreSQL（关系型数据库），支持 SQL 查询、事务、存储过程等高级功能，并提供可视化管理工具（Table Editor）。PostgreSQL 的关系型模型和 SQL 支持非常适合存储结构化数据（如用户对话记录、知识库、标注数据），能高效处理多表关联、聚合查询，比 NoSQL（如 Firestore）更适应复杂业务逻辑。

**实时 API**

通过 PostgreSQL 的实时订阅功能，任何数据变更（增删改）可即时推送到客户端（类似 Firebase 的 Firestore 实时更新）。通过 PostgreSQL 的监听机制，AI 生成的结果（如聊天消息、任务状态）可实时推送到前端，无需轮询（类似 Websocket 但更简单）

**Serverless 扩展**

低成本集成 AI 逻辑：用 Deno/TypeScript 编写轻量级函数，处理 AI 相关任务（如调用 OpenAI API、数据预处理），无需维护完整后端

**身份认证（Auth）**

支持多种登录方式（邮箱/密码、OAuth、Magic Link、SSO），集成 JWT 和第三方提供商（Google、GitHub 等）。

**存储（Storage）**

类似 Firebase Storage，提供文件上传、下载和管理功能，支持权限控制。

**Edge Functions**

基于 Deno 的 serverless 函数，允许运行自定义后端逻辑（类似 Firebase Cloud Functions）。

**Auto-generated APIs**

自动为数据库生成 RESTful API 和 GraphQL API（需搭配第三方工具），无需手动编写后端代码。

## 为什么Supabase 这么重要

**全栈一体化** ：数据库、认证、API 和 AI 逻辑在一个平台完成，减少技术碎片化。

**开源可控** ：避免厂商锁定，适合需要定制化 AI 流水线的团队。

**性能与扩展** ：PostgreSQL 的成熟生态支撑高并发 AI 请求。

Supabase 在 AI 领域的优势源于 PostgreSQL 的灵活性 + 实时能力 + 开源可控，特别适合需要复杂数据处理、实时交互或自定义 AI 工作流的场景。如果你的 AI 产品依赖结构化数据或需要高效检索，Supabase 是一个更强大的选择，也可以作为企业解决方案的技术选型方案。未来一定会有更多关于Supabase的成熟解决方案。

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxNjk5NjI1Mg==&mid=2247484046&idx=1&sn=6150ebc39ace0872819fbf9198e5d28f&chksm=9a73787f1bd3025fc4e73eb3033a5f866cd776c80b76cb70782f317325564dcfdbdc344b0daf&mpshare=1&scene=1&srcid=0909XVHDNAaHQdYkoYSrwmEk&sharer_shareinfo=15c854b37364591a8eaac5983bbf82f8&sharer_shareinfo_first=15c854b37364591a8eaac5983bbf82f8)

