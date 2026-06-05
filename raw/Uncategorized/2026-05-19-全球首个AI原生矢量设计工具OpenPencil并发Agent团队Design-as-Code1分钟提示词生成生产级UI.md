---
id: "7456229981757114561"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485438&idx=1&sn=fe9962c03fa964dac4fdfc146c426f9a&chksm=f5d838a25e0d990dd90686ed8be54ce12a47db8869b8f187593e01361310cf2d1130b40cbf1d&mpshare=1&scene=1&srcid=0519OUA1cO0CqLyisMDO8Dah&sharer_shareinfo=1d140fd042619333d9a864d8400b453b&sharer_shareinfo_first=1d140fd042619333d9a864d8400b453b
author: "小K 如此才是"
collected: 2026-05-19
tags: []
---

# 全球首个AI原生矢量设计工具OpenPencil：并发Agent团队+Design-as-Code，1分钟提示词生成生产级UI代码，程序员&设计师彻底解放双手！

# 全球首个AI原生矢量设计工具OpenPencil：并发Agent团队+Design-as-Code，1分钟提示词生成生产级UI代码，程序员\&设计师彻底解放双手！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485438&idx=1&sn=fe9962c03fa964dac4fdfc146c426f9a&chksm=f5d838a25e0d990dd90686ed8be54ce12a47db8869b8f187593e01361310cf2d1130b40cbf1d&mpshare=1&scene=1&srcid=0519OUA1cO0CqLyisMDO8Dah&sharer_shareinfo=1d140fd042619333d9a864d8400b453b&sharer_shareinfo_first=1d140fd042619333d9a864d8400b453b)小K 如此才是


![](https://image.cubox.pro/cardImg/61npp5byny7sc228ha8drwlyk7ia16yavmyekza5respls3a8m?imageMogr2/quality/90/ignore-error/1)

**如此才是**

介绍最新的科技信息与娱乐信息

181篇原创内容

<br />

公众号  

，

当Figma还在手动拖拽、代码还要手动敲的时候，**全球首个开源AI原生矢量设计工具OpenPencil** 横空出世。OpenPencil不仅仅是"提示词生成UI"，而是真正实现了**Design-as-Code** 、**并发Agent团队** 、**MCP服务器深度集成** 的全链路AI设计革命,还能一键导出React+Tailwind、Vue、Svelte、Flutter、SwiftUI等多框架生产代码。

### 一、OpenPencil核心功能

OpenPencil的核心定位是**AI-native vector design tool** ，强调"提示词直接在无限画布上实时生成UI"，并首创**并发Agent Teams** 。

**1. AI-Native Design（AI原生设计）**

●**Prompt to Canvas** ：自然语言描述任意UI，实时流式（streaming）动画在无限画布上生成生产级矢量UI（矩形、文本、图标、布局等）。

●**Orchestrator（编排器）** ：自动将复杂页面分解为空间子任务（如Hero区、功能区、页脚），支持并行生成。

●**Concurrent Agent Teams（并发Agent团队）** ：多个AI Agent同时工作，每个Agent有独立的画布指示器（per-member canvas indicators），支持delegate工具和fallback策略。

●**Design Modification** ：选中画布元素后，用自然语言聊天修改。

●**Vision Input** ：附加截图或线框图作为参考生成。

●**Style Guides** ：内置50+风格库（glassmorphism、brutalist、retro等），基于tag的模糊匹配，一键应用一致视觉语言。

●**Anti-Slop** ：跨生成多样性追踪，防止AI输出重复"slop"。

**2. Multi-Model Intelligence（多模型智能）**

自动适配9+提供商（Anthropic、OpenAI、Google、DeepSeek等）：

●Full-tier（如Claude）：完整prompt+thinking。

●Standard-tier（如GPT-4o、Gemini、DeepSeek）：禁用thinking。

●Basic-tier（如MiniMax、Qwen、Llama、Mistral）：简化nested-JSON prompt，确保可靠性。

**3. MCP Server（Model Context Protocol服务器）**

内置pen-mcp，支持一键安装到Claude Code、Codex、Gemini、OpenCode、Kiro、Copilot等CLI。支持stdio和streamable HTTP传输，默认HTTP端点http://localhost:3100/mcp。可从终端/编辑器读取、创建、修改.op文件，实现**终端即设计工具** 。

**4. Design-as-Code（设计即代码）**

●**.op文件** ：纯JSON格式，人可读、Git友好、可diff。

●设计变量自动生成CSS custom properties，支持$variable引用。

●**Code Export** ：从单个.op文件导出到React+Tailwind、HTML+CSS、Vue、Svelte、Flutter、SwiftUI、Jetpack Compose、React Native。

**5. CLI工具（op命令）**

全局安装后可批量设计、节点操作、Figma导入等，支持inline/@file/stdin三种输入方式。

**6. Embeddable SDK**

●pen-engine（headless引擎）+ pen-react（React UI SDK）。

●可将设计引擎嵌入自定义应用，提供DesignProvider、DesignCanvas、hooks、panels、toolbar等组件。

**7. Design System Kit**

可复用UIKit，支持style switching、component composition，从.pen文件导入/导出，内置registry和MCP工具。

**8. 其他硬核功能**

●**无限画布** ：平移、缩放、对齐参考线、吸附；支持Rectangle、Ellipse、Line、Polygon、Pen（Bezier）、Frame、Text；布尔运算（union/subtract/intersect）。

●**Auto-layout** ：垂直/水平、gap、padding、justify、align。

●**多页面文档** + Figma .fig文件完整导入（保留布局、fills、strokes、effects、text、images、vectors）。

●**Git集成** ：Clone向导、分支操作、Pull/Push、三路合并、冲突面板（per-node diff + JSON编辑器）。

●**Export** ：PNG/JPEG/WEBP/PDF + 代码。

●**i18n** ：完整支持15种语言（含简体/繁体中文）。

●**Runs Everywhere** ：Web + Electron桌面（自动更新、.op文件关联）。

### 二、安装方法

**1. 桌面端Prebuilt安装（最推荐）**

●macOS：brew tap zseven-w/openpencil && brew install --cask openpencil

●Windows：scoop bucket add openpencil https://github.com/zseven-w/scoop-openpencil && scoop install openpencil

●Linux/Windows直下：GitHub Releases 下载 .exe / .AppImage / .deb

**2. CLI安装**

```
●●●bashnpm install -g @zseven-w/openpencil
```

**3. Docker部署（多镜像变体）**

●轻量版（仅Web）：docker run -d -p 3000:3000 ghcr.io/zseven-w/openpencil:latest

●完整版（含所有CLI）：openpencil-full:latest（\~1GB）

●Claude专用版需volume持久化登录：先claude login，再启动。

**4. 从源码安装\&开发（硬核玩家必备）**

前提：Bun \>=1.0、Node.js \>=18（可选Zig \>=0.14构建agent-native）。

```
●●●bashgit clone https://github.com/ZSeven-W/openpencil.git
cd openpencil
bun install
bun --bun run dev          # 启动Web开发服务器 http://localhost:3000
bun run electron:dev       # 以桌面App形式运行
```

●MCP开发：bun run mcp:dev

●CLI开发：bun run cli:dev

●Electron打包：bun run electron:build

### 三、高效使用方法

**快速启动** ：安装后运行op start启动App。

**Prompt生成示例** ：

在画布输入"Create a modern SaaS landing page with hero, features, pricing, footer in glassmorphism style"，实时流式生成。

**CLI实战** （高效批量/脚本化）：

●op design @landing.txt（从文件批量设计）

●op design:skeleton {json} → op design:content section-id {json} → op design:refine（分层工作流）

●op import:figma design.fig

●cat design.dsl | op design -

**MCP工具调用** （外部Agent自动化）：

支持open_document、batch_get、insert_node、update_node、batch_design DSL等，实现"LLM直接操作设计文档"。

**Git工作流** ：内置Clone、Branch、Merge、冲突解决面板。

**代码导出** ：Cmd+Shift+P 或面板选择目标框架，一键生成。

### 四、技术原理、架构与实现方式

OpenPencil采用**Bun monorepo** 架构，技术栈：React 19 + TanStack Start + Tailwind CSS v4 + CanvasKit/Skia WASM + Electron 35 + Zustand v5 + Vercel AI SDK + TypeScript（严格模式）。

**核心包结构与职责** （packages/目录）：

●**pen-types** ：PenDocument模型类型定义。

●**pen-core** ：文档树操作、布局引擎、变量解析、布尔运算（Paper.js）。

●**pen-engine** ：Headless设计引擎（document、selection、history、viewport，无框架依赖）。

●**pen-react** ：React UI SDK（DesignProvider、DesignCanvas、hooks、panels、toolbar）。

●**pen-codegen** ：多平台代码生成器（增量pipeline：plan → submit chunks → assemble）。

●**pen-figma** ：.fig文件解析转换器。

●**pen-renderer** ：独立CanvasKit/Skia渲染器（GPU加速矢量绘制）。

●**pen-mcp** ：MCP服务器（stdio + HTTP transport，默认3100端口），提供工具集（CRUD、batch_design DSL、segmented prompts、postProcess自动语义补全）。

●**pen-ai-skills** ：AI prompt skill引擎（phase-driven prompt loading：skeleton/content/refine）。

●**pen-sdk** ：统一出口。

●**agent-native** ：Zig NAPI原生Agent运行时（多提供商、Agent Teams）。

**数据流架构** （单向数据流+防循环同步）：

```
●●●codeReact UI (Toolbar/Panel) 
   ↓ Zustand stores (canvas-store + document-store)
   ↓ CanvasKit/Skia (仅渲染)
   ↑ canvas-sync-lock (防止循环)
document-store 是唯一真相源
```

**多页面与变量实现** ：

●PenDocument支持pages数组 + children fallback。

●$variable引用在resolveNodeForCanvas()时实时解析，代码输出自动转为var(--name)。

**AI Orchestrator与Concurrent Agents** ：

编排器空间分解任务 → Agent Teams并行（每个有canvas indicator）→ 流式SSE更新画布。

**MCP分层工作流** ：

Single-shot / Layered（skeleton → content × N → refine）+ Segmented Prompt（仅加载所需schema/layout/style等子集）。

**渲染与性能** ：

CanvasKit/Skia WASM提供GPU加速矢量+布尔运算；postProcess自动处理icon、layout、text height、clipContent等。

**Git与冲突解决** ：

三路合并 + per-node JSON diff + 批量操作面板。

这一切全部开源，你可以直接在源代码中看到apps/web/src/services/ai/（orchestrator、streaming）、packages/pen-mcp/（tools/routes/document manager）等实现细节。

OpenPencil是**设计与开发的融合桥梁** 。让提示词成为生产力，让Agent团队并行工作，让.op文件像代码一样Git化，让MCP让终端也能设计。

**------ 如此才是**

![](https://image.cubox.pro/cardImg/61npp5byny7sc228ha8drwlyk7ia16yavmyekza5respls3a8m?imageMogr2/quality/90/ignore-error/1)

**如此才是**

介绍最新的科技信息与娱乐信息

181篇原创内容

<br />

公众号  

，

**把复杂的技术，讲成你真正能用上的生产力**

**[零基础也能玩转卫星！开源Ground Station + SDR 打造个人地面站全攻略](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484408&idx=1&sn=fa96368ff3647cd53bad3ee9391103ee&scene=21#wechat_redirect)**

**[OpenClaw \& Hermes刷屏后，GitHub Mercury Agent如何打动用户？ 灵魂驱动+权限铁闸+24/7永动 vs 两大竞品](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484903&idx=1&sn=8ea193b342d5f61ed5ed30de9ebb32b9&scene=21#wechat_redirect)**

**[苹果M系列芯片的福音！无需H100、无需云GPU，本地MacBook就能微调Gemma 4多模态模型](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484529&idx=1&sn=63e2f7f4ac65540fd05ef9d05f0d28a8&scene=21#wechat_redirect)**

**[开源Minecraft终极杀手！12.7K星GitHub神器Luanti（原Minetest）完整中文攻略：零基础安装、2800+模组随便玩、服务器+源码编译](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484515&idx=1&sn=f7cac21fab871c06cee81d780a1e37af&scene=21#wechat_redirect)**

**[AI 直接操控 Unity/Godot/Unreal 编辑器！用 OpenClaw + TomLeeLive 插件，聊天就能把你的游戏梦想变成现实](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484263&idx=1&sn=49474c84d4c0c6a1dd7925d821680aca&scene=21#wechat_redirect)**

[开源项目Paseo，AI编码代理跨设备统一指挥中心：统管Claude Code、Codex、OpenCode（以及Copilot、Pi等）](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484927&idx=1&sn=b4d7d4aed5a5ad7263bff54b50c395a5&scene=21#wechat_redirect)

[老婆/女朋友每天早上纠结45分钟穿什么？GitHub 开源AI衣柜神器 Wardrowbe 彻底解放！完整自托管安装+使用教程](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484594&idx=1&sn=2a9832be4fd2b3d423f9c62fbae5b0a3&scene=21#wechat_redirect)

[Notebook LM平替，开源Open Notebook：隐私零泄露、18+AI模型随意切、1-4人定制播客秒生成](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484913&idx=1&sn=a3307c1fb6b981881b22ca1c1ca407e2&scene=21#wechat_redirect)

[30MB Rust无头浏览器Obscura：击败Chrome、V8真实JS+CDP全兼容，AI Agent与爬虫的隐形核武器](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485078&idx=1&sn=84152e9774e0eab3d16839db3a7657de&scene=21#wechat_redirect)

[Rust重写的jcode：性能碾压Cursor Claude Code 139倍的下一代Coding Agent Harness，人类级内存图谱+多会话Swarm](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485066&idx=1&sn=2a563ec1e199af1807b6541f91d0842b&scene=21#wechat_redirect)

[Warp开源震撼发布！5年Rust GPU终端+Oz Agentic开发环境完整拆解：功能全览、源码编译教程、核心架构深度解析](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485052&idx=1&sn=f612497afd348acd327221233af635c2&scene=21#wechat_redirect)

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485438&idx=1&sn=fe9962c03fa964dac4fdfc146c426f9a&chksm=f5d838a25e0d990dd90686ed8be54ce12a47db8869b8f187593e01361310cf2d1130b40cbf1d&mpshare=1&scene=1&srcid=0519OUA1cO0CqLyisMDO8Dah&sharer_shareinfo=1d140fd042619333d9a864d8400b453b&sharer_shareinfo_first=1d140fd042619333d9a864d8400b453b)

