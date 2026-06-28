# Teaching agents product design at Vercel

- **URL**: https://vercel.com/blog/teaching-agents-product-design-at-vercel
- **发布日期**: 25 Jun 2026
- **阅读时长**: 7 min read
- **来源**: Vercel Blog

---

## 核心观点

Coding agents 能快速生成能跑的 UI,但更难的形状是另一回事:它们能复制产品的风格、匹配它的模式、试图遵循它的约定。**它们做不到的是理解这些模式为什么存在。**

代码展示了 agent 什么东西被 ship 了,但没有说明为什么某个组件、文案、交互会成为标准。这种 reasoning 存在于 design reviews、PR comments、Slack threads,以及"在场的那些人"那里。对 agent 来说,**不在 codebase 里的 context 就不存在**。

Vercel 是一个 agent-native team。他们把 accepted product decisions 当代码对待——保存在 repo 里、reviews 跟它们比对、对所有 agent 可见。具体做法是通过 `product-design`,一个三部分系统:

1. **Agent skill** — 给 coding agents 提供需要产品或 codebase judgment 的决策 context
2. **Linters** — 自动执行明确规则
3. **Review loop** — 从 Slack、Figma、GitHub 收集证据,然后准备 guideline updates 供 review

任何团队都可以围绕自己的标准建立同样的结构。

---

## Inside the product-design skill

Skill 住在 repo 里,跟它治理的代码在一起。

### 仓库结构

```
repository/
├── AGENTS.md
├── .agents/
│   └── skills/
│       └── product-design/
│           ├── AGENTS.md
│           ├── SKILL.md
│           ├── references/
│           │   ├── product-judgment.md
│           │   ├── interface-quality.md
│           │   ├── resilience.md
│           │   ├── surfaces.md
│           │   ├── surfaces-{surface}.md
│           │   ├── copy.md
│           │   ├── rules.md
│           │   ├── glossary.md
│           │   ├── patterns.md
│           │   └── coverage-gaps.md
│           └── exemplars/
│               └── pr-{name}.md
└── tooling/
    └── scripts/
        └── evals/
            ├── fixtures.json
            ├── rules-checklist.json
            └── <fixture>/
                ├── before/
                └── after/
```

- 仓库 `AGENTS.md` 告诉 coding agents 何时加载这个 skill
- skill-local `AGENTS.md` 定义加载顺序、验证、治理
- `SKILL.md` 拥有运行时 workflow
- `references/` 存 product-judgment、interface-quality、resilience、copy、规范产品名、交互模式、按 surface 的决策
- `exemplars/` 记录值得重复的决策(从 ship 过的 PR),以及需要避免的错误
- `coverage-gaps.md` 列出还没有标准的区域
- `copywriting-eval/` 测试 copy 和界面语言行为。**不**评估更广的 product-design workflow

---

## How the skill routes

`SKILL.md` 先解析 request mode:`shape`、`implement`、`review`、`copy`、`harden`。这能防止 audits 变成 edits,copy passes 变成 redesigns。

**会跳过**:backend-only work、telemetry、console errors、generated files、没有 shipped UI 影响的测试。

Skill route 到 canonical sources 而不是复制它们。Component APIs、design-system rules、accessibility criteria、interaction guidance 留在它们的所有者那里。

Routing 对 task 和 surface 都做具体匹配:
- Material changes 先加载 `product-judgment` 和 `interface-quality`
- Copy、component、layout、interaction、accessibility、resilience work 各自 route 到 focused references
- Modal 加载 destructive-action patterns 和 canonical verbs
- Settings form 加载 labels、validation、progressive disclosure、accessible-name guidance

### SKILL.md 简化模板

```yaml
---
name: product-design
description: >
  Single entry point for product design and user-facing product implementation
  in apps/vercel-site. Use whenever work changes what a user sees, understands,
  chooses, or does: shaping requirements and flows; building or redesigning
  pages and components; reviewing URLs, screenshots, diffs, or Vercel Agent
  findings; improving product copy, information architecture, component choice,
  Geist compliance, hierarchy, layout, interaction, accessibility, responsive
  behavior, and loading, empty, error, permission, billing, or destructive
  states. Trigger on design, UX, UI, usability, flow, onboarding, settings,
  dashboard, build, improve, fix, audit, review, polish, simplify, or
  production-ready requests. Also use when backend behavior changes a
  user-visible outcome. Not for backend-only work with no user-visible effect,
  tests with no shipped UI impact, telemetry-only work, documentation, or
  marketing content.
---

# Vercel Product Design

Make the interface correct for the user, the product, and Vercel. Working code is not enough: choose the right interaction, make scope and consequences clear, cover reality beyond the happy path, and verify the rendered result.

## Operating Contract
- **Start with the job, not the pixels.** Identify who is acting, what they are trying to accomplish, the product object involved, and what the system will change.
- **Define the outcome before the output.** Establish the current user problem, desired behavior, success signal, and non-goals before choosing a surface or component.
- **Use evidence, not taste.** Trace decisions to product behavior, canonical repository guidance, an accepted design decision, or a verified adjacent pattern.
- **Separate facts from decisions.** Mark assumptions and unresolved product choices explicitly; do not hide them inside implementation details.
- **Treat shipped code as evidence, not automatic precedent.** It proves what exists, not why it is correct. Check it against current components, product behavior, and explicit guidance.
- **Choose the smallest coherent intervention.** Consider better defaults, behavior, or reuse before adding UI. Do not solve one job by creating unrelated settings or abstractions.
- **Decide before decorating.** Resolve information architecture, component semantics, interaction, and state behavior before styling or rewriting copy.
- **Design every reachable state.** Include only states the product can actually enter, but do not stop at the populated success case.
- **Verify the real surface.** Source inspection establishes behavior; a rendered interface establishes visual and interaction quality. Never claim visual verification from code alone.
- **Keep one user-facing entry point.** Invoke `product-design`; route internally to the canonical sources below.

## Request Modes

Resolve the mode from the user's verb and artifact before acting.

| Mode    | Typical request                                          | Required behavior                                                                                                                                                              |
|---------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shape   | "Design this flow", "How should this work?", feature brief without settled UI | Frame the problem and evidence, compare material alternatives, then define the flow, states, acceptance criteria, risks, and open decisions. Do not edit unless asked.       |
| Implement | "Build", "fix", "improve", "make compliant", or "run product-design on everything" | Resolve material product decisions, then implement the smallest coherent end-to-end change within scope. Do not absorb unrelated review findings.                          |
| Review  | "Audit", "critique", "what's wrong?", code review        | Inspect source and rendered evidence, then report prioritized findings. Do not edit unless asked.                                                                              |
| Copy    | "Fix the copy", "rewrite these errors"                   | Edit user-facing language, accessible names, and directly required JSX only. Report structural blockers without silently broadening scope.                                   |
| Harden  | "Polish", "production-ready", "handle edge cases"        | Preserve the settled product direction while fixing state, resilience, responsive, accessibility, and finish defects.                                                          |

When intent is ambiguous, use the narrowest mode supported by the verb. A URL, screenshot, route, or component identifies scope; it does not by itself authorize edits.

A material decision changes the user's task, default, scope, consequence, navigation, interaction surface, or reachable states. Copy mechanics, token replacement, and established component substitutions usually are not material.

## Decision Authority

Resolve conflicts in this order:

1. The user's explicit goal and constraints.
2. Verified user/product evidence and system truth.
3. Repository-canonical guidance: `AGENTS.md`, Geist component APIs, `packages/geist/STYLE_GUIDE.md`, and routed skills.
4. Accepted product/design decisions and exemplars with stable evidence.
5. Verified adjacent shipped patterns in the same product area.
6. General interface heuristics.

## Workflow

### 1. Set scope and mode
Name the target surface and request mode in the work plan or review notes.

### 2. Load product context
Before proposing UI, read the applicable `AGENTS.md` chain, supplied briefs and designs, and the product logic that determines mutations, permissions, validation, errors, and side effects.

### 3. Model the product decision
For Shape, Implement, Harden, full Review, or any material product/flow change, read `product-judgment.md` and write a compact internal brief covering user, job, current behavior, desired outcome, success signal, non-goals, object, scope, action, consequence, reversibility, permissions, and open decisions.

### 4. Map the surface and states
Inventory entry points, visible regions, overlays, transitions, exits, and return paths. Map only reachable states including loading, empty, sparse, populated, validation, error, permission, disabled, optimistic, stale, destructive, and responsive variants.

### 5. Load the routed references

| Need                                                       | Load                                                         |
|------------------------------------------------------------|--------------------------------------------------------------|
| Product/flow/component decision                            | `product-judgment.md` + `component-guide`                   |
| Implementation, material visual change, or full review     | `interface-quality.md`                                       |
| Copy or accessible names                                   | `copy.md` + `surfaces.md` routing                            |
| Layout, typography, color, spacing, Geist APIs             | `design-guidelines` + `packages/geist/STYLE_GUIDE.md`        |
| Keyboard, focus, forms, touch, animation, URL state, performance | `web-interface-guidelines`                              |
| Overflow, localization, extreme data, network/error resilience | `resilience.md`                                            |

### 6. Decide, then implement
For each non-mechanical change, be able to answer: what user problem does this solve, why is this component appropriate, what consequence must the interface communicate, which evidence supports the decision, and what is the smallest coherent change?

### 7. Verify
1. Confirm the primary job and acceptance criteria.
2. Run repository lint checks.
3. Inspect relevant compact and wide viewports.
4. Exercise every materially changed reachable state.
5. Verify keyboard order, focus movement, loading behavior, and pointer/touch targets.
6. Test long content, large values, constrained width, and localization/RTL risk.
7. Load `review-design-system` for structural visible changes.

## Product Design Standards
- Make the user's primary task and primary action unmistakable.
- Preserve the user's mental model and current context unless changing it solves a verified problem.
- Name the exact object, scope, and consequence of important actions.
- Use navigation components for navigation and action components for actions.
- Choose surface persistence to match importance.
- Prefer inline disclosure before adding a modal.
- Expose advanced controls when needed without making the default path carry their complexity.
- Prefer strong defaults and direct behavior over adding configuration the user must learn and maintain.
- Use semantic Geist components and their APIs before custom HTML or styling.
- Use hierarchy, spacing, and alignment before adding containers.
- Preserve user input through validation and recoverable errors.
- Keep loading control labels stable; use the component's loading/busy affordance.
- Make destructive actions proportional to impact and provide undo when the system can honestly support it.
- Do not add decorative novelty, motion, or copy unless it clarifies structure, state, or brand intent.

## Review Output
Lead with findings, ordered by user impact:
- **P0:** blocks the primary task, creates severe accessibility failure, or can cause unrecoverable user harm.
- **P1:** likely task failure, misleading consequence, missing critical state, or major responsive/accessibility defect.
- **P2:** meaningful friction, inconsistency, weak hierarchy, or recoverability issue.
- **P3:** minor craft or consistency improvement.

For each finding include: file/line or rendered location, verification status, canonical source, user consequence, and smallest concrete fix.

## Skill Integrity
- Add or change a rule only after current-source verification and human acceptance.
- Record scope, rationale, evidence, exceptions, and a bad/good example.
- Prefer the narrowest destination: canonical source, routed reference, exemplar, lint/eval check, or coverage gap.
- Keep deterministic checks mechanical. Keep judgment in prose with its evidence and degree of freedom.
- Never promote one screenshot, one shipped file, or one reviewer comment into a universal rule by itself.
```

---

## Make findings traceable

Copy rules 有稳定的 ID,指向它们的 canonical sources:

```yaml
rule/destructive-names-action
  Source: copy.md > Actionable; verbs.md
  Rule: Destructive CTAs follow Verb + Noun. Never use Confirm, OK, or a bare verb.
  Example
```

当 Vercel Agent 提出 patch 时,它会在 secure Vercel Sandbox 里用 repo 的 builds、tests、linters 验证变更,然后才发布建议。

---

## Use linters for faster feedback

如果 linter 能可靠执行规则,就优先用 deterministic checks。Linters 又快又便宜,所以开发者和 coding agents 在工作时就能拿到 feedback,而不是等到更晚的 review。

代码能数 2-3 个 static options,所以 linter 能推荐 radio buttons。命名正确的 object 和 destructive action 的 consequence 需要 product context,所以 skill 处理。

**例子规则**(防止模式错误,自动捕获一类问题):
- 防止 nested modals(打破 focus management、键盘导航、layering)
- 2-3 个 static options 时推荐 radio 而不是 select,让所有选择始终可见
- icon buttons 和 form controls 要求 accessible names,拒绝绕过 shared focus tokens 的自定义 focus rings
- 防止 `className` 覆盖 design-system component 的 color、radius、shadow,同时仍允许 layout classes
- 要求 `Modal.Body`,让长内容正确滚动,headers 和 footers 可以保持 sticky
- 用 theme-aware Material classes 替代 raw shadows,拒绝重复 Material 内置处理的 borders
- 标记偏离 4px grid 的任意 spacing,有 standard utility 时建议使用

每条规则都解释为什么这个模式是个问题,并建议具体修复。一些规则可以 autofix 安全迁移(比如替换 deprecated Tailwind utility names)。

### Rule 接受路径

Accepted decisions 可以是几种形式:
- Geist component 旁边的人类可读 guidance(比如 Checkbox best practices)
- product-design skill 里的 agent guidance
- 代码能可靠 check 时的 lint rule

### 示例 lint rule:`prefer-radio-for-few-static-options.js`

```javascript
/** @type {import('eslint').Rule.RuleModule} */
module.exports = {
  meta: {
    type: 'suggestion',
    docs: {
      description: 'Suggest Radio buttons when Select has 2-3 static options',
      category: 'Design System',
      recommended: true,
    },
    schema: [],
    messages: {
      preferRadio:
        'Select with {{ count }} static options. Consider using Radio buttons — they show all options at once without requiring a click to open.',
    },
  },
  create(context) {
    return {
      JSXElement(node) {
        const opening = node.openingElement;
        if (opening.name.type !== 'JSXIdentifier') return;
        if (opening.name.name !== 'Select') return;
        const hasDynamic = node.children.some(
          (child) =>
            child.type === 'JSXExpressionContainer' &&
            child.expression.type === 'CallExpression',
        );
        if (hasDynamic) return;
        const optionChildren = node.children.filter(
          (child) =>
            child.type === 'JSXElement' &&
            child.openingElement.name.type === 'JSXIdentifier' &&
            child.openingElement.name.name === 'option',
        );
        if (optionChildren.length < 2 || optionChildren.length > 3) return;
        context.report({
          node: opening,
          messageId: 'preferRadio',
          data: { count: String(optionChildren.length) },
        });
      },
    };
  },
};
```

---

## How we test the guidance with evals

Lint rules 是 deterministic 的,但 agent behavior 会变化,所以在 agent 没见过的新 interfaces 上测试 skill。

- Agent 编辑 before state,然后 judge 根据 rubric 检查结果
- Evals 来自 skill 里记录的 shipped examples
- Holdouts 隐藏它们期望的 edits,测试 guidance 是否能泛化
- 也跑不带 skill 的 fixtures,衡量 skill 是否改变了 agent 的 behavior
- **分开打分 rule correctness 和与 shipped result 的相似度**——shipped code 可能含 agent 应该改进而不是复制的缺陷

---

## Keep the guidance current

Product standards 随 component、name、workflow、failure state 变化,每次更新都需要 evidence 和 human review。

每周的 evidence-intake workflow 收集可能改进 product-design 的 design feedback。它搜索 Slack conversations,保留到 Figma files、pull requests、review comments、previews 的链接作为 evidence。当 evidence 不完整时,它记录验证所需的 code 或 commit。

**workflow 分离 collection 和 judgment**:
- Collector 收集 messages、links、nearby context,不提议 rules
- 单独的 judge 分组 evidence、验证 sources、记录 open questions
- Job 创建 review packet,包含 candidates、rejected topics、follow-up requests、coverage gaps
- 每个 candidate 链接到它的 source,保持 pending
- 经验丰富的 reviewer 的 comment 可以提高它的 priority,但每个 candidate 仍需要 evidence

**Automation 以 review packet 结束**。人类决定 candidate 是成为 agent guidance、lint rule、example、eval,还是 no change。Accepted changes 进入最窄的相关文件,通过相关 checks 后合并。

---

## How to build product-design into your codebase

Vercel 的 setup 反映他们的 product、components、review history,但其他团队可以适配结构到自己的标准。

### 1. 从重复的决策开始

选择一个同样的 review comments 反复出现的 product surface:destructive actions、error states、settings forms、empty states、navigation。

从 shipped code 和真实 reviews 收集 examples,写下决策、为什么重要、exceptions、source。

**避免**用 broad adjectives 开始(clear、polished、intuitive)。Agents 需要可观察的决策。

- "Destructive actions use Verb + Noun" — 可用
- "Buttons should be clear" — 不可用

**决策记录模板**:

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

在扩展到其他 surface 前,先填写针对你 surface 的字段。

### 2. 添加明确的触发器和严格边界

在持久的 repository instructions 里告诉 agents 何时加载 skill,并定义它覆盖的文件和 surfaces,以及必须跳过的区域。

> **关键数据**:在单独的 Next.js evals 里,agents **56% 的情况下**未能 invoke 可用的 skill。分开测试 trigger 和 guidance——未能加载 skill 和未能遵循 rule 是不同的问题。

```markdown
When shaping, editing, or reviewing user-facing UI, load .agents/skills/product-design/SKILL.md.

Applies to:
- user-facing pages and components
- copy, interaction, accessibility, responsive behavior, and states

Skip:
- backend-only work with no user-visible effect
- telemetry, generated files, documentation, and marketing
```

让 agent 报告它加载了哪些 surfaces 和 references,然后验证它的 findings 引用了那些 sources。

### 3. 分离 routing、rules、evidence

- 用一个短的 entry point 来识别 surface 和加载 focused references
- 围绕 reviewers 已经在讨论的 surfaces 和 decisions 来组织细节:forms、modals、navigation、product vocabulary、workflow states、cross-surface patterns
- 给 rules 稳定的 IDs,链接到 examples 和 sources
- 用有用的 decisions **和** 已知 flaws 记录 shipped examples
- 把缺失的 guidance 放在 coverage-gap list 里,让它可见

**规则参考模板**:

```markdown
# {Surface}

Load when:
Canonical owner:

## rule/{stable-id}
Scope:
Rule:
Why:
Exceptions:
Source:

## Examples
Bad:
Good:

## Coverage gaps
- {missing decision or evidence}
```

Coverage-gap list 让缺失的 guidance 显式化。

### 4. 用代码表达明确规则

如果 linter 能可靠地识别问题,就在那里执行规则。当决策需要 product 或 codebase context 时,用 agent guidance。

- 把新 standards、policy choices、未解决的 product decisions 跟人放在一起
- 从记录的 examples 构建 training fixtures
- 从期望 edits 不出现在 skill 里的 interfaces 构建 holdouts
- **分开测试 retrieval 和 application**——agent 是否加载了 skill 和是否遵循了 rule 是不同的问题

**决策树:何时用 linter vs agent guidance**

```
Can code identify the failure without rendering?
├─ No: use agent guidance.
└─ Yes: can the rule avoid likely false positives?
   ├─ No: use agent guidance.
   └─ Yes: does the violation have a concrete fix?
      ├─ Yes: use a linter.
      └─ No: use a warning or agent guidance.

Needs product or codebase context: use agent guidance.
Establishes a new standard or product policy: require a human decision.
```

对于任何一条路径,添加一个 example 或 eval 来捕捉回归。如果一条规则在不带许多 exceptions 的情况下无法保持可靠,就把它移回 agent guidance。

### 5. 指派所有权和更新循环

定期 review 新 evidence,但在改变 guidance 或 checks 前要求 human approval。

- 维护 decision log,记录改了什么、为什么、哪个 source 支持
- 把新 rules 当作 product changes,review 和 test 每一条,移除不再有帮助的

**Evidence-review prompts**:

```
Collector prompt
You are the collector. Gather messages, links, files, and nearby context. Write raw artifacts only. Do not score candidates or propose rules.

Judge prompt
You are the judge. Validate coverage before grouping related evidence. Separate verified facts, inferences, and open questions. Keep every candidate pending. Do not edit the guidance.

Human review
Choose: rule, reference, exemplar, lint rule, eval, coverage gap, or no change. Require stable evidence, explicit scope and exceptions, and an approver.
```

从一个 surface 和你团队已经重复的 decisions 开始。把这些 decisions 放在写代码和 review 的地方,让人对什么成为标准负责。

---

## 关键 takeaway

> 最难的部分是挑选第一个 surface。每个团队都有值得编码的 decisions。问题是它们活在某人的脑子里还是 agents 能找到的地方。

如果你用这个 pattern 建了东西或对 setup 有问题,可以告诉 Vercel。

---

## 与现有 wiki 主题的关联

- **AGENTS.md / Skills 体系**:与 `karpathy-llm-wiki` 的 SKILL.md 模式高度一致——agent 通过 markdown 文件获得 context
- **Lint as Code for Design**:把"设计系统"从文档约束升级为 ESLint 级别自动约束,任何 team 都可以做
- **Routing 模式**:request mode (shape/implement/review/copy/harden) 防止 audit 变成 edit,值得借鉴到 wiki 整理流程
- **Evidence loop**:collector / judge / human review 三段式,跟 karpathy wiki 的"先 raw 后 processed"理念相通
- **Coverage gaps 文件**:显式记录"我还不知道什么",这本身就是种 agents 友好的元数据