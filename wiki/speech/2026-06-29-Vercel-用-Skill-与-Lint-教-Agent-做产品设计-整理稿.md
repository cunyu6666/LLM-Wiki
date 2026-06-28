---
title: "Vercel 用 Skill 与 Lint 教 Agent 做产品设计 · 整理稿"
source: https://vercel.com/blog/teaching-agents-product-design-at-vercel
published: 2026-06-25
collected: 2026-06-29
tags: [Agent Skill, Lint, Product Design, Vercel, 整理稿]
type: speech-compile
---
# Vercel 用 Skill 与 Lint 教 Agent 做产品设计

> 来源:[Vercel Blog](https://vercel.com/blog/teaching-agents-product-design-at-vercel) · 2026-06-25 · 7 分钟阅读
> 完整中文编译版已收录在 [wiki/design/用 Skill 与 Lint 教 Agent 做产品设计.md](../design/用%20Skill%20与%20Lint%20教%20Agent%20做产品设计.md),此为可独立传播的整理稿

## 一句话总结

Coding agent 能复制产品风格,但**不**理解这些风格为什么存在。Vercel 把"为什么"编码成 `SKILL.md` + Lint rule + Eval 三件套,让 agent 继承 reasoning 而非只复制模式。

---

## 三个核心判断

**1. shipping code ≠ design system**
代码告诉 agent 什么被 ship 了,但不告诉它为什么。对 agent 来说,design review 会议、PR comments、Slack threads、"在场的人"脑子里的 reasoning——只要不在 codebase 里,**就不存在**。

**2. trigger 比 guidance 重要**
Vercel 内部 Next.js evals 测出:**56% 的情况下 agent 未能 invoke 可用的 skill**。这意味着 trigger 设计远比 guidance 文本重要——分开测试"是否加载了 skill"和"是否遵循了 rule",是不同的问题。

**3. 模式设计 gating,避免 audit 变 edit**
SKILL.md 在做任何事之前先解析 `request mode`(`shape` / `implement` / `review` / `copy` / `harden`)。intent ambiguous 时,用 verb 支持的最窄 mode。URL/screenshot/component 标识 scope,但**不**授权 edits——否则一次 review 就会被改得面目全非。

---

## 三件套结构

### Skill:决策的存放地

`product-design` skill 住在 repo 里,跟代码在一起:

```
.agents/skills/product-design/
├── AGENTS.md              # skill-local:加载顺序、验证、治理
├── SKILL.md               # 运行时入口,先解析 mode
├── references/            # product-judgment / interface-quality / resilience / copy
└── exemplars/             # 从 shipped PR 提炼的好决策**和**坏错误
```

`coverage-gaps.md` 显式记录"还没有标准的区域"——缺失的 guidance 是显式的,不是沉默的。

### Lint:deterministic 检查机械执行

如果 linter 能可靠执行,**永远**用 deterministic checks。Vercel 的 lint rule 集覆盖的实际场景:

- 2-3 个 static options → 推荐 radio 而非 select(所有选择始终可见)
- Destructive CTAs → 必须 Verb + Noun(不用 Confirm / OK / 裸动词)
- Icon buttons / form controls → 必须有 accessible names
- 防止 `className` 覆盖 design-system component 的 color/radius/shadow
- 拒绝 nested modals(打破 focus、键盘、layering)
- 要求 `Modal.Body` 让长内容正确滚动
- 偏离 4px grid 的 spacing → 标记并建议 standard utility

每条规则都解释**为什么**和怎么修。一些可以 autofix 安全迁移(如 deprecated Tailwind utility 替换)。

### Review Loop:让 guidance 跟上产品变化

```
Collector (automation)        只收集 raw artifacts,提议 rules
  ↓ Slack / Figma / PR / preview
Judge (automation)           验证和分组,编辑 guidance
  ↓ candidates + rejected + follow-ups + coverage gaps
Review Packet (artifact)
  ↓
Human Review (gate)          决定 candidate 是:agent guidance / lint rule / example / eval / coverage gap / no change
```

**Automation 以 review packet 结束**——人决定什么成为标准。每个 candidate 链接到 source,保持 pending。

---

## 决策权威的优先级

当 conflict 出现时,按这个顺序解决:

1. 用户的 explicit goal 和 constraints
2. Verified user/product evidence 和 system truth
3. Repository-canonical guidance(AGENTS.md、component APIs、STYLE_GUIDE.md)
4. Accepted product/design decisions 和 exemplars with stable evidence
5. Verified adjacent shipped patterns
6. General interface heuristics

**翻译**:用户 > 证据 > 本 repo 的 canonical 文档 > 已接受的决策 > 相邻已 ship 的 pattern > 通用启发式。

---

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

对任何一条路径,都要加 example 或 eval 捕捉回归。如果一条规则在不带许多 exceptions 的情况下无法保持可靠,就移回 agent guidance。

---

## 决策记录模板

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

避免 broad adjectives("clear / polished / intuitive")——agent 需要**可观察的决策**。"Destructive actions use Verb + Noun" 可用,"Buttons should be clear" 不可用。

---

## 对设计师的三个启示

1. **Design review 跟 code review 是同一个东西**——在 PR comment 里写"这里应该用 Verb + Noun",你就在创造 candidate rule
2. **Exemplars 比 guidelines 更有说服力**——配一个 real PR link,远比一句原则管用;好例子**和坏例子**都进 exemplars/,只看好例学不会边界
3. **Coverage gaps 是诚实的资产**——"我们还没有关于 onboarding empty state 的标准"这条记录本身,就是 agent 友好的元数据

---

## 关键 takeaway

> 最难的部分是挑选第一个 surface。每个团队都有值得编码的 decisions。问题是它们活在某人的脑子里,还是 agents 能找到的地方。

**起手式**:从一个 surface 开始(destructive actions / error states / settings forms / empty states / navigation,选 review comments 反复出现的那一个),从 repeated decisions 出发,添加 trigger 和严格边界,把 rules 跟人放一起。

---

## 与本 wiki 其他主题的关联

- [AI Agent 开发](../design/AI%20Agent%20开发.md) — Agent Skills 与工具构建原始讨论
- [用 Skill 与 Lint 教 Agent 做产品设计(完整编译版)](../design/用%20Skill%20与%20Lint%20教%20Agent%20做产品设计.md) — 含完整代码片段和详细分析
- [AI编程与Vibe Coding](../design/AI编程与Vibe%20Coding.md) — Claude Code / Cursor / Codex 等 coding agent 生态
- [设计方法论](../design/设计方法论.md) — AI 时代的设计方法论
- [设计系统](../design/设计系统.md) — AI 时代的协作基础设施

---

## 附:原文关键数据

- **发布日期**:2026-06-25
- **阅读时长**:7 min
- **Vercel 内部 evals 数据**:Next.js evals 中,agents 56% 情况下未能 invoke 可用 skill
- **核心论点**:"对 agent 来说,不在 codebase 里的 context 就不存在"
- **Lint rule 数量**:文章列出的典型 rule 约 8 条,覆盖 modal、select/radio、accessible name、className override、focus ring、shadow/border、4px grid 等