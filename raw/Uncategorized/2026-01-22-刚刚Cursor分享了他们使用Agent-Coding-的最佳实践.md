---
id: "7413697056503499338"
cubox_url: 
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247502534&idx=1&sn=8c417dde199e31a5f6bc81e50d50d41c&chksm=c32f74b13b07035bd1a0a0730db9ffba9c9fffb2bfd397bfffad5bded18e0dc30d25fafe48c9&mpshare=1&scene=1&srcid=01220anXQfvilr9zpuGJ2uFp&sharer_shareinfo=570cf4bbf5ba7db307f42e49ed9fc3c3&sharer_shareinfo_first=570cf4bbf5ba7db307f42e49ed9fc3c3
author: "PaperAgent"
collected: 2026-01-22
tags: []
---

# 刚刚，Cursor分享了他们使用Agent Coding 的最佳实践

# 刚刚，Cursor分享了他们使用Agent Coding 的最佳实践

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247502534&idx=1&sn=8c417dde199e31a5f6bc81e50d50d41c&chksm=c32f74b13b07035bd1a0a0730db9ffba9c9fffb2bfd397bfffad5bded18e0dc30d25fafe48c9&mpshare=1&scene=1&srcid=01220anXQfvilr9zpuGJ2uFp&sharer_shareinfo=570cf4bbf5ba7db307f42e49ed9fc3c3&sharer_shareinfo_first=570cf4bbf5ba7db307f42e49ed9fc3c3)PaperAgent


**Cusor** 分享了他们在使用 **Agent 编码** 的最佳实践，原文较长，链接在文末，PaperAgent对核心内容进行了提炼：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681bV55XGNZ0H2iaqlOJe2R6mMJ8l4G8OzDXyOiagHkYjv62vhdR7BEhv0g%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

**编码 Agent 正在改变构建软件的方式** 。

模型现在可以连续运行数小时，完成大规模的多文件重构，并持续迭代直到测试通过。但要充分发挥 Agent 的能力，你需要理解它们的**工作原理** ，并形成新的**使用范式** 。

## 了解 agent harness

编码 Agent 正在改变软件构建方式：模型可连续运行数小时，跨文件重构并持续迭代至测试通过。发挥全部潜力的前提是理解其工作原理并形成新的使用范式。

Agent harness 三组件：

1.
   **Instructions** ：系统提示与行为规则
2.
   **Tools** ：文件编辑、代码搜索、终端执行
3.
   **User messages** ：用户指令与后续交互

Cursor 针对每个前沿模型单独调优 instructions 与工具组合，自动处理模型间差异，让用户专注业务逻辑。

## 从规划开始

芝加哥大学实验表明，经验丰富的开发者更倾向先规划再编码。规划迫使人们澄清需求，也为 Agent 提供可衡量的目标。

### 使用 Plan 模式

Shift+Tab 切换 Plan 模式后，Agent 会：

1.
   分析代码库并定位相关文件
2.
   提出澄清问题
3.
   输出带文件路径与代码引用的分步计划
4.
   待你确认后才开始改动

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz468167RvrlMGrc8xJstVjBd7DiaJ5gK7B0SRiaLvibb5kAYk408YTTiaKcQSJw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)Plan 模式实战：agent 会提出澄清问题并创建可审查的计划。

计划以 Markdown 打开，可直接删减步骤或补充上下文；点击"Save to workspace"存入 .cursor/plans/ 供团队复用。小修或重复性任务可直接执行，无需规划。

### 从计划重新开始

当实现偏离预期时，回滚改动、重新细化计划再跑一遍，比连续追加提示更快速也更干净。

## 管理上下文

把 Agent 当作新同事：提供刚好够、又不冗余的上下文，是决定成败的关键。

### 让 agent 自行获取上下文

Cursor 内置毫秒级 grep 与语义搜索，可自动定位"authentication flow"等相关文件。你知道确切文件就引用，不确定就交给 Agent，避免无关文件干扰。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681AyKNHQKB4ibs6eWEiawROTicIjWz7iaITnfuoUNsoYDfAbV8Tocia8ibc33Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)即时 grep 让 agent 能在毫秒级搜索你的代码库。

### 对话生命周期

**新开对话** ：任务切换、Agent 明显困惑、已完成独立单元  
**继续原对话** ：同一功能迭代、需先前上下文、调试刚生成的代码  
过长对话会被多次摘要，噪音累积导致失焦；效果下降时果断重启。

### 引用以往成果

用 @Past Chats 让 Agent 按需加载历史片段，避免整段复制，更高效也更精准。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681mXwsmsZtKzj1kz4BK0aBwFeUicX1pvr0LqtVutu92P356Tt3HSVFMmg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

## 扩展 Agent

Cursor 通过 **Rules** （静态）与 **Skills** （动态）提供两种扩展方式。

### Rules：项目级静态上下文

在 .cursor/rules/ 创建 Markdown，聚焦三要素：

*
  常用命令 (npm run build / typecheck / test)
*
  代码风格（ES 模块、解构引用、组件示范文件）
*
  工作流（先类型检查再提交、API 路由统一放 app/api/）

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681XYnOjbqHTibkicspyI0lHKXwytcdgbKyVNaVHZ8BPkvLPDYqoHMy9guw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D4)

引用示例文件而非复制内容，随代码演进及时更新并提交 Git。

### Skills：按需加载的动态能力

Agent Skills扩展了 agent 的能力范围。Skills 封装了特定领域的知识、工作流和脚本，agent 在需要时可以调用。

Skills 定义在 SKILL.md 文件中，并且可以包括：

*
  **Custom commands** ：通过在 agent 输入中使用 / 触发的可复用工作流
*
  **Hooks** ：在 agent 动作之前或之后运行的脚本
*
  **Domain knowledge** ：agent 可按需调用的针对特定任务的指令

与 Rules 不同，Skills 仅在 Agent 认为相关时加载，节省上下文窗口。

### 示例：长时间运行循环

一个常用且强大的模式是使用 Skills 来创建长时间运行的 agent，让它不断迭代直到实现某个目标。下面是一个示例，展示如何构建一个 hook，让 agent 一直工作，直到所有测试都通过。

首先，在 .cursor/hooks.json 中配置该 hook：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz46812iavXySQ6EiazkuHcfsJXPK9lSEHPnTmZOfA54PcmKrryTSibDS4swVsA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D5)

hook 脚本（ .cursor/hooks/grind.ts）从标准输入（stdin）接收上下文，并返回一个 followup_message，用于继续循环：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681Exggeib3Ts6CzZ3KmW6Cl386oUDLzVDTHo6p5P4eSlvc36YMEFmeXfg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D6)

## 包含图片

Agent 可直接读取粘贴或拖入的图片。

### 设计到代码

贴入设计截图，Agent 识别布局、颜色、间距并生成对应 JSX + CSS；可接入 Figma MCP 服务器直接拉取矢量数据。

### 可视化调试

对异常界面截图后提问，Agent 结合源码快速定位样式或逻辑错误；还能驱动浏览器自动截屏、点击、验证回归。

Agent 还可以控制浏览器自行截屏、测试应用，并验证界面变化。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681tSEyvhCMZu0JMUO6KciaMyMGOGP6ev78gzbu3r1xUymVAaq15icfPXTw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D7)浏览器侧边栏让你可以一边设计一边编码。

## 常见工作流

### 测试驱动开发

1.
   让 Agent 按输入/输出对写测试（声明这是 TDD，禁止写实现）
2.
   运行并确认测试失败
3.
   提交测试
4.
   让 Agent 写实现并迭代至全绿
5.
   提交实现

测试即目标，Agent 在可衡量信号下迭代最快。

### 理解代码库

像请教同事一样提问：

*
  "日志如何落盘？"
*
  CustomerOnboardingFlow 处理了哪些边界情况？ Agent 用 grep + 语义搜索一次性给出代码位置与解释，是上手陌生仓库的最高效方式。

### Git 工作流

把日常多步操作写成 .cursor/commands/ 中的 Markdown，例如：

*
  /pr：diff → 写提交信息 → push → gh pr create
*
  /fix-issue 128：拉取 issue → 定位相关代码 → 修复 → 开 PR
*
  /update-deps：逐依赖升级并跑测试

Agent 识别 / 命令并自动执行，减少重复劳动。

## 代码审查

AI 代码同样需审查，Cursor 提供三层检查：

1.
   **实时审查** ：Diff 随改动即时显示，方向不对按 Esc 中断
2.
   **Agent Review** ：完成后点击 Review → Find Issues，让另一 Agent 逐行扫描潜在缺陷![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681Xs3BnWh4dgec35dj8AtLMDxr9MFDvL0hE1DAqiaSE53TjpSgYYJS5iaQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D8)
3.
   **Bugbot** ：推送到 GitHub 后，自动在 PR 发表评论，指出逻辑、性能与安全风险

重大变更还可让 Agent 生成 Mermaid 架构图，提前暴露循环依赖或单点故障。

## 并行运行 Agent

Cursor 自动为并行任务创建 Git worktrees，各 Agent 在独立工作树内编辑、构建、测试，互不干扰；完成后点击 **Apply** 即可合并回当前分支。

同时用多模型跑同提示，结果并排展示，Cursor 会标出推荐方案，适合棘手算法或跨语言重构。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681P7E3w8KKlV2nzXTxJViaE7PDqlZRiab2uYLKboKibRbJibDyN2HbLTFZww%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D9)

## 云端 Agent

适合"待办列表"型任务：随机 Bug、技术债重构、补测试、写文档。网页或手机发起，远程沙箱运行，合上电脑也能继续；完成后自动开 PR 并通过 Slack/邮件通知。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681icicIu0m68LJbMc5RUbfOL4wlvOvKicQd1ytAIZFW6ffiaSeNxXHpG9PdA%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D10)

## Debug Mode（棘手 Bug）

与其盲猜，不如系统调试：

1.
   生成多个失败假设
2.
   自动埋点日志
3.
   你按步骤复现并回传运行时数据
4.
   Agent 基于证据定位根因
5.
   给出最小修复

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricFvQHHK2tiaUUpUVSRNz4681NR1A674nTfNOdjaIKictboav8Bcibu5cqdxHkxXxvVNQnupz33QmDXGw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D11)

专治竞争条件、性能泄漏、难复现回归。

## 打造你的工作流程

*
  **写具体提示** ：对比"add tests"与"为 auth.ts 登出边缘写测试，用 __tests__/ 内模式，禁 mock"
*
  **迭代配置** ：先简单，发现重复错误再加规则；命令成熟后再纳入 .cursor/commands/
*
  **认真 review** ：Agent 越快，人眼越要跟上；阅读 diff，验证边界
*
  **可验证目标** ：强类型 + linter + 测试，给 Agent 明确成功信号
*
  **当协作者** ：让 Agent 给计划、做解释，对不认可方案敢于质疑

Agent 能力随新模型持续进化，掌握上述范式即可长期保持高效。

    https://cursor.com/cn/blog/agent-best-practices


推荐阅读


[动手设计AI Agents：（编排、记忆、插件、workflow、协作）](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247492838&idx=2&sn=1e25832e7300ef312721325d0def30b4&scene=21#wechat_redirect)

[大模型虽好，但恕我直言：在OCR面前，开源小模型更香](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247501897&idx=1&sn=b899f9ed01e7dc5494a9b36ac17574c5&scene=21#wechat_redirect)  

[2026，新风向： 世界模型 × 具身智能 最新综述](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247502059&idx=1&sn=7e3a7a4a0ccf390b1904165aff3728d8&scene=21#wechat_redirect)   

[一篇最新自演化AI Agents全新范式系统性综述](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247497640&idx=1&sn=beb015fa84617bd1930222684ec9def8&scene=21#wechat_redirect)


*** ** * ** ***

每天一篇大模型Paper来锻炼我们的思维\~已经读到这了，不妨点个👍、❤️、↗️三连，加个星标⭐，不迷路哦\~


[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247502534&idx=1&sn=8c417dde199e31a5f6bc81e50d50d41c&chksm=c32f74b13b07035bd1a0a0730db9ffba9c9fffb2bfd397bfffad5bded18e0dc30d25fafe48c9&mpshare=1&scene=1&srcid=01220anXQfvilr9zpuGJ2uFp&sharer_shareinfo=570cf4bbf5ba7db307f42e49ed9fc3c3&sharer_shareinfo_first=570cf4bbf5ba7db307f42e49ed9fc3c3)

