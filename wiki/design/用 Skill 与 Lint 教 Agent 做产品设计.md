---
title: "用 Skill 与 Lint 教 Agent 做产品设计"
summary: "Vercel 把产品设计决策编码成 SKILL.md + Lint rule + Eval 三件套,让 coding agent 不只复制模式还能继承 reasoning"
tags: [Agent Skill, Lint, Product Design, Vercel]
created: 2026-06-29
updated: 2026-06-29
type: index
---
# 用 Skill 与 Lint 教 Agent 做产品设计

> Sources: Vercel Blog, 2026-06-25
> Raw: [Teaching Agents Product Design at Vercel](../../raw/design/2026-06-29-Teaching-Agents-Product-Design-at-Vercel.md)

## Overview

Coding agent 能快速生成能跑的 UI,但更难的形状是另一回事:它们能复制产品的风格、匹配它的模式、试图遵循它的约定——**但做不到理解这些模式为什么存在**。代码展示了 agent 什么东西被 ship 了,但没有说明为什么某个组件、文案、交互会成为标准。

Vercel 在 2026-06-25 发布的这篇博客,把这套问题系统化了:**把 accepted product decisions 当代码对待,放在 repo 里、被 review、对所有 agent 可见**。具体形态是一个三部分系统:

1. **Agent skill** — 给 coding agent 提供需要产品或 codebase judgment 的决策 context
2. **Linters** — 把能 deterministic 执行的规则下沉成自动检查
3. **Review loop** — 从 Slack、Figma、GitHub 收集证据,准备 guideline updates 供 review

任何团队都可以围绕自己的标准建立同样的结构。这篇文章的核心价值不在于它解决了 AI 设计的所有问题,而在于**它示范了一个可操作的模式**:让"设计品味"从人脑里的隐性知识,变成代码库里可被 agent 读取和验证的显性资产。

## 为什么 shipping code 不等于 design system

Vercel 给出了非常尖锐的判断:**对 agent 来说,不在 codebase 里的 context 就不存在**。

这种 reasoning(为什么这个组件用 radio 而不是 select、为什么 destructive button 要 Verb + Noun、为什么 settings form 要 progressive disclosure)原本存在于:
- Design review 会议
- PR comments
- Slack threads
- "在场的那些人"的脑子里

当 agent 拿到一个 codebase,代码告诉它的是"这里 ship 了一个 Modal.Body",但**不**告诉它"Modal.Body 是必须的,因为非 Modal.Body 时长内容无法滚动,header/footer 也无法保持 sticky"——这就是 Vercel 一条 lint rule 的真实来历。

更进一步,shipping code 本身也**不是 automatic precedent**。Agent 应该用 shipped code 当作"存在性证据",而非"正确性证据"——shipped code 可能含 agent 应该改进而不是复制的缺陷。

## 三件套:Skill / Lint / Review

### 1. Agent Skill:决策的存放地

Vercel 的 `product-design` skill 住在 repo 里,跟它治理的代码在一起:

```
repository/
├── AGENTS.md                          # 告诉 coding agent 何时加载这个 skill
├── .agents/
│   └── skills/
│       └── product-design/
│           ├── AGENTS.md              # skill-local:加载顺序、验证、治理
│           ├── SKILL.md               # 运行时 workflow
│           ├── references/            # product-judgment / interface-quality / resilience / copy 等
│           └── exemplars/             # 从 shipped PR 里提炼的好决策和坏错误
└── tooling/scripts/evals/             # 测试 agent 是否真的应用了 guidance
```

**关键设计点**:
- 仓库根的 `AGENTS.md` 是 trigger 层,负责告诉 agent "何时该加载这个 skill"
- skill-local `AGENTS.md` 负责"加载顺序、验证、治理"等 skill 内部规则
- `SKILL.md` 是运行时入口,**先解析 request mode**(`shape` / `implement` / `review` / `copy` / `harden`),再 route 到对应 reference
- `references/` 按 surface 和决策类型组织细节,**不**复制 canonical source
- `exemplars/` 用 shipped PR 当例子,**同时记录好决策和坏错误**
- `coverage-gaps.md` 显式记录"还没有标准的区域"——缺失的 guidance 是显式的,不是沉默的

### 2. Request Mode:把 audit 跟 edit 分开

Vercel 的 SKILL.md 在做任何事之前,**先解析 mode**:

| Mode       | 典型请求                                                | 行为                                                                          |
|------------|---------------------------------------------------------|-------------------------------------------------------------------------------|
| Shape      | "Design this flow", "How should this work?"             | 定义 flow、states、acceptance criteria、risks、open decisions。**不**编辑     |
| Implement  | "Build", "fix", "improve", "make compliant"             | 解决 material 决策,实现最小 coherent end-to-end 变化                          |
| Review     | "Audit", "critique", "what's wrong?"                    | 检查 source 和 rendered evidence,报告排序的 findings。**不**编辑             |
| Copy       | "Fix the copy", "rewrite these errors"                  | 只编辑 user-facing language、accessible names、必需 JSX                       |
| Harden     | "Polish", "production-ready", "handle edge cases"       | 保留已定型的产品方向,只修 state、resilience、responsive、accessibility        |

这个设计的精髓:**intent ambiguous 时,用 verb 支持的最窄 mode**。一个 URL、screenshot、route、component 标识 scope,但**不**授权 edits。

这种 mode gating 防止一个常见事故:"你能 review 一下吗?" 然后 PR 被大刀阔斧地改。

### 3. Lint Rule:让 deterministic 检查机械地执行

如果 linter 能可靠执行规则,就**永远优先**用 deterministic checks。Linters 又快又便宜,所以开发者和 coding agents 在工作时就能拿到 feedback,而不是等到 review 才发现。

**示例 lint rule 集**(每条都解释为什么、推荐怎么修):

```javascript
// 2-3 个 static options 时,推荐 radio 而不是 select
// 让所有选择始终可见,免去点击展开
// (完整代码见原文)
```

Vercel 的 lint rule 覆盖的实际场景:
- 防止 nested modals(打破 focus management、键盘导航、layering)
- 2-3 个 static options 推荐 radio 而非 select
- icon buttons 和 form controls 要求 accessible names
- 拒绝绕过 shared focus tokens 的自定义 focus rings
- 防止 `className` 覆盖 design-system component 的 color/radius/shadow(但允许 layout classes)
- 要求 `Modal.Body` 让长内容正确滚动,header/footer 保持 sticky
- 用 theme-aware Material classes 替代 raw shadows
- 标记偏离 4px grid 的任意 spacing,有 standard utility 时建议使用

一些规则可以 autofix 安全迁移(比如替换 deprecated Tailwind utility names)。

### 4. Review Loop:让 guidance 跟上产品变化

Product standards 随 component、name、workflow、failure state 变化,每次更新都需要 evidence 和 human review。

Vercel 的 weekly evidence-intake workflow:

```
Collector (automation)
  ↓ 搜 Slack conversations,保留 Figma / PR / review comment / preview 链接
Judge (automation)
  ↓ 分组 evidence、验证 sources、记录 open questions
Review Packet (artifact)
  ↓ candidates / rejected topics / follow-up requests / coverage gaps
Human Review (gate)
  → 决定 candidate 是:agent guidance / lint rule / example / eval / coverage gap / no change
```

**核心原则**:
- Collector 只收集 raw artifacts,不提议 rules
- Judge 只验证和分组,不编辑 guidance
- **Automation 以 review packet 结束**——人决定什么成为标准
- 每个 candidate 链接到 source,保持 pending;经验 reviewer 的 comment 可提优先级,但每个 candidate 仍需要 evidence

## 决策权威的优先级

当 conflict 出现时,Vercel 的 skill 按这个顺序解决:

1. 用户的 explicit goal 和 constraints
2. Verified user/product evidence 和 system truth
3. Repository-canonical guidance(`AGENTS.md`、Geist component APIs、`STYLE_GUIDE.md`、routed skills)
4. Accepted product/design decisions 和 exemplars with stable evidence
5. Verified adjacent shipped patterns in the same product area
6. General interface heuristics

**简洁翻译**:用户 > 证据 > 本 repo 的 canonical 文档 > 已接受的决策 > 相邻已 ship 的 pattern > 通用启发式。

## 关键的 56% 数字

Vercel 在自己的 Next.js evals 里测过:**agents 56% 的情况下未能 invoke 可用的 skill**。

这意味着 trigger 设计远比 guidance 文本重要——agent 可能 guidance 写得再好,但因为 trigger 不清晰而完全没加载。所以 Vercel 强调:**分开测试 trigger 和 guidance**——"未能加载 skill"和"未能遵循 rule"是两个不同的问题,不要混在一起 debug。

## 决策树:何时用 lint 何时用 agent guidance

```
Can code identify the failure without rendering?
├─ No → use agent guidance
└─ Yes: can the rule avoid likely false positives?
   ├─ No → use agent guidance
   └─ Yes: does the violation have a concrete fix?
      ├─ Yes → use a linter
      └─ No → use a warning or agent guidance

Needs product or codebase context → use agent guidance
Establishes a new standard or product policy → require a human decision
```

对任何一条路径,**都要加一个 example 或 eval 来捕捉回归**。如果一条规则在不带许多 exceptions 的情况下无法保持可靠,就把它移回 agent guidance。

## 关键 takeaway

> 最难的部分是挑选第一个 surface。每个团队都有值得编码的 decisions。问题是它们活在某人的脑子里,还是 agents 能找到的地方。

对一个想要复用的团队,起手式是:

1. **从一个 surface 开始**——destructive actions、error states、settings forms、empty states 或 navigation,选择同样的 review comments 反复出现的那一个
2. **从 repeated decisions 出发**——避免 "clear / polished / intuitive" 这种 broad adjectives,agent 需要**可观察的决策**("Destructive actions use Verb + Noun" 可用,"Buttons should be clear" 不可用)
3. **用决策记录模板**:

```markdown
# Decision: {name}
Status: proposed | accepted | rejected
Scope:
Decision:
Rationale:
Evidence:
Exceptions:
Bad example:
Good example:
Assumptions:
Open decisions:
```

4. **添加 trigger 和严格边界**——`AGENTS.md` 里写明"何时加载"和"什么跳过"

5. **把 rules 跟人放一起**——新 standards、policy choices、未解决的 product decisions 留在人那里。Lint 只处理代码能可靠 check 的部分

## 对设计师的具体启示

Vercel 的模式对设计师有三个直接启示:

**1. Design review 跟 code review 是同一个东西**
- 当你在 PR comment 里写"这里应该用 Verb + Noun",你就在创造一条 candidate rule
- 当你在 Slack 里说"我们 modal 从不嵌套",你就在为一条 lint rule 投票

**2. Exemplars 比 guidelines 更有说服力**
- "我们 destructive buttons 长这样" 配一个 real PR link,远比"用 Verb + Noun 命名"管用
- Vercel 把好例子**和坏例子**都放进 `exemplars/`,因为只看好例学不会边界

**3. Coverage gaps 是诚实的资产**
- "我们还没有关于 onboarding empty state 的标准"——这条记录本身就是 agent 友好的元数据
- 让 agent 知道"这块没有标准,我应该 ask 而不是 assume"

## 跟现有 wiki 主题的关联

- **[Agent Skill 体系](AI%20Agent%20开发.md)**:Vercel 的 `product-design` 是迄今最具体的"SKILL.md + lint + eval"三位一体范例,把抽象的 Agent Skills 概念落到产品设计场景
- **Anthropic 的 Agent 工具论**:与"Anthropic 实用发布:如何为 Agent 构建工具"中的契约思想一致——skill 是工具,反映确定性系统与非确定性 Agent 之间的契约
- **Claude Code 工作流**:跟 Claude Code 的 system prompt 和 `SkillOpt` 文章里的"Skill 自进化"主题呼应——Skill 不是静态文档,是会随团队演化的资产
- **设计系统**:把"设计系统"从文档约束升级为 ESLint 级别的自动约束——这是 AI 时代协作基础设施的具体形态
- **路由与模式解析**:request mode 的 gating(防止 audit 变成 edit)可以泛化到任何 AI 工作流——明确"我现在能做什么、不能做什么"

## See Also

- [AI Agent 开发](AI%20Agent%20开发.md) — Agent Skills 与工具构建相关原始讨论
- [AI编程与Vibe Coding](AI编程与Vibe%20Coding.md) — Claude Code / Cursor / Codex 等 coding agent 生态
- [设计方法论](设计方法论.md) — AI 时代的设计方法论
- [设计系统](设计系统.md) — AI 时代的协作基础设施
- [Karpathy LLM Wiki](../.agents/skills/karpathy-llm-wiki/SKILL.md) — 同一个 SKILL.md 模式可以怎么用于个人 wiki