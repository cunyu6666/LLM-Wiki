---
title: "Claude Code 构建经验：我们如何使用 Skills"
source: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
author: Anthropic
date: 2026-06-03
tags: [Claude Code, Skills, AI Agent, 开发工具]
translated: true
---

# Claude Code 构建经验：我们如何使用 Skills

> Anthropic 内部构建和扩展数百个 Skills 的实战经验总结。

Skills 已经成为 Claude Code 中使用最广泛的扩展点之一。它们灵活、易于创建、也便于分发。

但这种灵活性也带来了一个问题：什么才是最佳实践？什么样的 Skills 值得做？如何组织一个 Skill 的结构？什么时候该分享给他人？

Anthropic 内部一直在大量使用 Claude Code Skills，目前有数百个 Skills 在活跃运行。以下是我们总结的、能够加速开发效率的实战经验。

## 什么是 Skills？

Skills 是一組包含指令、脚本和资源的文件夹，Agent 可以发现并利用它们来更准确、高效地完成任务。本文默认你已了解 Skills 基础知识；如果是新手，建议先从 Skilljar 上的 Agent Skills 入门课程学起。

一个常见的误解是 Skills "不过是 Markdown 文件"。实际上，它们是可以包含脚本、素材、数据等内容的文件夹，Agent 可以发现、探索并操作这些内容。

在 Claude Code 中，Skills 还支持丰富的配置选项，包括注册动态钩子（hooks）。

我们发现，Claude Code 中最高效的 Skills，往往能充分利用这些配置选项和文件夹结构。

## Skills 的九大类型

在梳理了 Anthropic 内部所有 Skills 之后，我们发现它们可以归纳为九个类别。最优秀的 Skills 通常只聚焦于一个类别；那些试图面面俱到的 Skills 往往跨越多个类别，反而让 Agent 困惑。这不是一个权威分类，但作为一个框架，可以帮助你发现自身 Skills 库中的空白。

### 1. 库与 API 参考

这类 Skills 用于解释如何正确使用某个库、CLI 工具或 SDK。既可以是内部库，也可以是 Claude Code 有时难以处理的通用库。这类 Skills 通常包含一个参考代码片段文件夹，以及一份 Claude 在编写脚本时需要避免的"坑"清单。

示例：
- **billing-lib** — 你的内部计费库：边界情况、常见陷阱等
- **internal-platform-cli** — 内部 CLI 封装工具的所有子命令，附带使用场景示例
- **sandbox-proxy** — 配置组织的出口网关用于开发工作：哪些主机可达、如何调试"连接被拒绝"错误、如何添加白名单条目

### 2. 产品验证

这类 Skills 用于描述如何测试或验证代码是否正常工作。它们通常与 Playwright、tmux 或其他外部验证工具配合使用。

在 Anthropic 内部，验证类 Skills 对 Claude 输出质量的提升效果最为显著，可量化。值得花一整个工程师的工作周来打磨你的验证 Skills。

可以考虑的技术手段：让 Claude 录制其输出的视频，这样你就能看到它具体测试了什么；或者在每个步骤强制执行程序化的状态断言。这些通常通过在 Skill 中包含各种脚本来实现。

示例：
- **signup-flow-driver** — 在无头浏览器中运行注册→邮箱验证→引导流程，每一步都有状态断言钩子
- **checkout-verifier** — 用 Stripe 测试卡驱动结账 UI，验证发票确实落入正确状态
- **tmux-cli-driver** — 用于需要 TTY 的交互式 CLI 测试

### 3. 数据获取与分析

这类 Skills 用于连接你的数据和监控体系。可能包含带凭证的数据获取库、特定的仪表盘 ID，以及常见工作流或数据获取方式的说明。

示例：
- **funnel-query** — "我需要关联哪些事件来看注册→激活→付费"，加上实际包含规范 user_id 的表名
- **cohort-compare** — 比较两个群组的留存或转化率，标记具有统计显著性的差异，链接到群组定义
- **grafana** — 数据源 UID、集群名称、问题→仪表盘查找表
- **datadog** — 字段参考（@request_id vs trace_id）、服务列表、指标前缀约定

### 4. 业务流程与团队自动化

这类 Skills 将重复性工作流自动化为一条命令。通常指令比较简单，但可能依赖其他 Skills 或 MCP。对于这类 Skills，将之前的结果保存在日志文件中，可以帮助模型保持一致性并回顾之前的执行记录。

示例：
- **standup-post** — 聚合你的工单追踪器、GitHub 活动和之前的 Slack 消息→格式化的每日站会报告，仅显示增量
- **create-\<ticket-system\>-ticket** — 强制执行 schema（有效枚举值、必填字段）加上创建后的工作流（通知审阅者、在 Slack 中关联）
- **weekly-recap** — 合并的 PR + 关闭的工单 + 部署→格式化的周报

### 5. 代码脚手架与模板

这类 Skills 用于生成代码库中特定功能的框架模板代码。你可以将这些 Skills 与可组合的脚本结合使用。当你的脚手架需求包含无法纯靠代码覆盖的自然语言要求时，这类 Skills 尤其有用。

示例：
- **new-\<framework\>-workflow** — 用你的注解脚手架新的服务/工作流/处理器
- **new-migration** — 你的迁移文件模板加上常见陷阱
- **create-app** — 新的内部应用，预装你的认证、日志和部署配置

### 6. 代码质量与审查

这类 Skills 用于在组织内强制执行代码质量标准并辅助代码审查。可以包含确定性脚本或工具以获得最大健壮性。你可能希望将这些 Skills 作为钩子的一部分或在 GitHub Action 中自动运行。

示例：
- **adversarial-review** — 启动一个"新鲜视角"的子 Agent 进行批判，实施修复，迭代直到发现退化为小问题
- **code-style** — 强制执行代码风格，特别是 Claude 默认不擅长的风格
- **testing-practices** — 关于如何编写测试以及测试什么的指导

### 7. CI/CD 与部署

这类 Skills 用于帮助你在代码库中获取、推送和部署代码。可能会引用其他 Skills 来收集数据。

示例：
- **babysit-pr** — 监控 PR → 重试不稳定的 CI → 解决合并冲突 → 启用自动合并
- **deploy-\<service\> → 构建 → 冒烟测试 → 逐步流量发布并比较错误率 → 回归时自动回滚
- **cherry-pick-prod** — 隔离的 worktree → cherry-pick → 冲突解决 → 带模板的 PR

### 8. 运维手册

这类 Skills 接收一个症状（如 Slack 线程、告警或错误签名），通过多工具调查，生成结构化报告。

示例：
- **\<service\>-debugging** — 映射症状→工具→查询模式，针对你流量最高的服务
- **oncall-runner** → 获取告警 → 检查常见嫌疑 → 格式化发现结果
- **log-correlator** — 给定一个请求 ID，从所有可能接触过它的系统中拉取匹配日志

### 9. 基础设施运维

这类 Skills 执行日常维护和运维操作，其中一些涉及破坏性操作，需要防护栏。它们使工程师更容易在关键操作中遵循最佳实践。

示例：
- **\<resource\>-orphans** — 查找孤立的 pod/卷 → 发布到 Slack → 冷却期 → 用户确认 → 级联清理
- **dependency-management** — 你的组织的依赖审批工作流
- **cost-investigation** — "为什么我们的存储/出口账单飙升"，附带特定的存储桶和查询模式

## Skills 编写技巧

一旦你决定要制作某个 Skill，如何编写它？以下是 Claude Code 团队的最佳实践、技巧和窍门。

### 不要陈述显而易见的事

Claude 已经会写代码，也能读懂你的代码库。一个只是重复 Claude 默认行为的 Skill，只是增加了上下文而没有增加价值。如果你发布的 Skill 主要是知识性的，要专注于那些能让 Claude 跳出常规思维模式的信息。

前端设计 Skill 就是一个很好的例子：它由 Anthropic 的一位工程师通过与客户反复迭代，改进 Claude 的设计品味，避免 Inter 字体和紫色渐变等经典模式而打造出来的。

### 建立"踩坑"章节

任何 Skill 中信号量最高的内容就是"踩坑"（Gotchas）章节。这些章节应该从 Claude 使用你的 Skill 时遇到的常见失败点中积累而来。理想情况下，你会随着时间推移不断更新 Skill 来记录这些踩坑经验。

例如：
- "subscriptions 表是只追加的。你要的行是 version 最高的那条，不是 created_at 最新的那条。"
- "这个字段在 API 网关中叫 @request_id，在计费服务中叫 trace_id。它们是同一个值。"
- "Staging 环境即使 Stripe webhook 没有实际处理也会返回 200。去查 payment_events 表看真实状态。"

### 善用文件系统与渐进式披露

如前所述，Skill 是一个文件夹，而不仅仅是一个 Markdown 文件。你应该把整个文件系统视为一种上下文工程和渐进式披露的形式。告诉 Claude 你的 Skill 中有哪些文件，它会在适当的时候去读取。

最简单的渐进式披露形式是：指向其他 Markdown 文件供 Claude 使用。例如，你可以把详细的函数签名和使用示例拆分到 references/api.md 中。

另一个例子：如果你的最终输出是一个 Markdown 文件，你可以在 assets/ 中放一个模板文件供复制使用。

你可以有 references、scripts、examples 等文件夹，帮助 Claude 更高效地工作。

### 避免过度约束 Claude

Claude 通常会尽量遵循你的指令，而由于 Skills 的可复用性很强，你需要避免指令过于具体。给 Claude 它需要的信息，但也要给它根据情况灵活调整的空间。

### 想好初始化流程

有些 Skills 可能需要根据用户提供的上下文进行设置。例如，如果你要做一个将每日站会发到 Slack 的 Skill，你可能需要 Claude 询问要发到哪个 Slack 频道。

一个好的模式是：将设置信息存储在 Skill 目录下的 config.json 文件中。如果配置尚未设置，Agent 就可以向用户询问信息。

如果你想让 Agent 呈现结构化的多选题，可以指示 Claude 使用 AskUserQuestion 工具。

### 为模型写描述，而不是为人写

当 Claude Code 启动一个会话时，它会构建一个包含所有可用 Skills 及其描述的列表。Claude 扫描这个列表来判断"这个请求有没有对应的 Skill？"这意味着，description 字段不是摘要，而是触发时机的描述。

### 帮助 Claude 记忆

有些 Skills 可以通过在内部存储数据来包含某种形式的记忆。你可以用任何方式存储数据——简单到一个只追加的文本日志文件或 JSON 文件，复杂到一个 SQLite 数据库。

例如，一个 standup-post Skill 可以维护一个 standups.log，记录它每次发布的站会内容。这样下次运行时，Claude 就能读取自己的历史记录，判断与昨天相比有什么变化。

你可以使用环境变量 `${CLAUDE_PLUGIN_DATA}` 来获取一个稳定的存储目录。

### 存储脚本并生成代码

你能给 Claude 的最强大工具之一就是代码。给 Claude 脚本和库，能让它把算力花在组合和决策下一步做什么上，而不是重建模板代码。

例如，在你的 data-science Skill 中，你可以有一个从事件源获取数据的函数库。为了让 Claude 能做复杂分析，你可以给它一组辅助函数。Claude 就可以即兴生成脚本来组合这些功能，完成更高级的分析，比如处理"周二发生了什么？"这样的提示。

### 使用按需钩子

Skills 可以包含只在 Skill 被调用时才激活、且只持续当前会话期间的钩子。将那些不想一直运行、但偶尔非常有用的"强主张"钩子放在这种模式下。

例如：
- **/careful** — 通过 Bash 的 PreToolUse 匹配器阻止 rm -rf、DROP TABLE、force-push、kubectl delete。只有在你确定要操作生产环境时才需要——一直开着会把人逼疯。
- **/freeze** — 阻止对特定目录以外的任何编辑/写入。在调试时很有用："我想加日志，但我总是不小心'修复'了不相关的代码。"

## 分发 Skills

Skills 最大的优势之一就是可以与团队共享。

与他人共享 Skills 有两种方式：
- 将你的 Skills 提交到代码仓库（放在 ./.claude/skills 下）
- 创建一个插件，通过 Claude Code 插件市场让用户上传和安装插件

对于仓库较少的小团队，将 Skills 提交到仓库效果很好。但每个提交的 Skills 都会增加模型的上下文负担。随着规模扩大，内部插件市场可以让你分发 Skills，让团队自行决定安装哪些，并包含设置流程。

## 管理 Skills 市场

如何决定哪些 Skills 进入市场？人们如何提交？

在 Anthropic，我们没有一个中心化的团队来决定；我们尽量让最有用的 Skills 自然浮现。如果有人有一个想让大家试用的 Skills，他们可以上传到 GitHub 的沙盒文件夹，然后在 Slack 或其他论坛中推荐。

一旦一个 Skills 获得了足够的关注（这由 Skills 的创建者来判断），他们可以提交 PR 将其移入市场。

## 组合 Skills

你可能需要 Skills 之间相互依赖。例如，你可能有一个文件上传 Skill 用于上传文件，还有一个 CSV 生成 Skill 用于制作 CSV 并上传。这种依赖管理目前还没有原生构建到市场或 Skills 中，但你可以通过名称引用其他 Skills，模型会在它们已安装的情况下调用它们。

## 衡量 Skills 的效果

为了了解一个 Skills 的表现，我们使用了一个 PreToolUse 钩子来记录公司内部的 Skills 使用情况。这样我们就能发现哪些 Skills 受欢迎，或者哪些 Skills 的触发率低于预期。
