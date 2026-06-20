---
type: index
description: "文章来源：Google Cloud · Data Analytics 团队 · 2026-06-12 发布"
timestamp: 2026-06-20
---
# OKF（Open Knowledge Format）与本 Wiki 的对照分析

> 文章来源：Google Cloud · Data Analytics 团队 · 2026-06-12 发布
> 作者：Sam McVeety（Tech Lead, Data Analytics）& Amir Hormati（Tech Lead, BigQuery）
> 小红书抓取笔记 ID：`6a2eb950000000001702f828`
> 抓取日期：2026-06-20

---

## 摘要

Google Cloud 2026-06-12 发布 **OKF v0.1**（Open Knowledge Format）——**正式把 LLM-wiki pattern 标准化为开放规范**。本 wiki（Obsidian + YAML frontmatter + wikilink + 反向链接）正是 LLM-wiki pattern 的活样本。OKF 定义的 6 个核心字段：`type / title / description / resource / tags / timestamp`。

---

## OKF v0.1 核心定义

> *"As foundation models continue to improve, the lack of relevant context often limits what they can do, especially as they are used to build agentic systems."*

OKF v0.1 = 一个目录的 **Markdown 文件 + YAML frontmatter**，配合一组**通用约定**——让不同生产者写的知识，能被不同 agents 无需翻译地消费。

### 三大组成

- **Just markdown** — 任何编辑器可读，GitHub 可渲染，任意搜索工具可索引
- **Just files** — 可打包成 tarball，可托管在任何 git repo，可挂载在任何文件系统
- **Just YAML frontmatter** — 仅 6 个结构化字段：`type / title / description / resource / tags / timestamp`

### 适用对象

> *"If you've used Obsidian, Notion, Hugo, or any of the LLM wiki patterns that have emerged over the past year, the shape will feel familiar."*

OKF 是 **Obsidian / Notion / Hugo / LLM-wiki** 这类 pattern 的形式化标准。

### 解决的问题

> *"A fragmented context landscape."*

企业内部 FM 需要的 context 是**极度碎片化**的：
- 表的 schema
- 业务对某个指标的定义
- 事件 runbook
- 两个系统的 join paths
- 老 API 的 deprecation notice
- ……

OKF 把这些碎片**统一成一种结构**，让任意 agent 能自动读、自动用。

---

## 本 Wiki vs OKF v0.1 对照表

| OKF 字段 | OKF 含义 | 本 Wiki 现状 | 差距 |
|---|---|---|---|
| `type` | 文档类型 | ❌ **缺失**（用目录 `wiki/Agent/`、`raw/小红书/` 隐式表达） | 应在 frontmatter 加 `type: index / raw / note / guide / log` |
| `title` | 文档标题 | ✅ H1 标题 + 文件名 | 一致 |
| `description` | 文档摘要 | ⚠️ 部分有（raw/小红书/*.md 有抓取说明），wiki/ 下多数缺失 | 应统一加（尤其索引版） |
| `resource` | 资源链接/来源 URL | ⚠️ raw/ 下完整（`url:`），wiki/ 下多数缺失 | wiki 索引版应加 `source:` 链接 |
| `tags` | 标签 | ✅ 完整 | 一致（格式：`["AI", "..."]`） |
| `timestamp` | 时间戳 | ✅ 完整（`captured:` + `created:`） | OKF 应支持 created/updated 双字段 |

**结论**：本 Wiki 6 个字段中**满足 3 个（title/tags/timestamp）**，**缺失 1 个（type）**，**部分满足 2 个（description/resource）**。**对齐 OKF 只需做小手术**。

---

## OKF 强调的 4 个核心约束

OKF 的"哲学三原则"映射到我们 GEB 协议：

| OKF 原则 | 本 Wiki (GEB) | 评估 |
|---|---|---|
| **vendor-neutral**（厂商中立） | ✅ Obsidian + 纯 md，无厂商绑定 | 完全对齐 |
| **agent-friendly**（agent 友好） | ✅ Claude Code / Codex / Catui 都能直接读 | 完全对齐 |
| **human-friendly**（人类可读） | ✅ Markdown 原生渲染 | 完全对齐 |
| **portable**（可移植） | ✅ Git 仓库，tarball 友好 | 完全对齐 |
| **interoperable**（互操作） | ⚠️ Obsidian wikilink 格式 `[[...]]` 不是通用 Markdown，外部工具不识别 | **唯一短板** |

---

## 与 GEB 协议的关系

GEB 协议是你的**项目级实施规范**（三层分形：根 CLAUDE.md / 模块 CLAUDE.md / 文件头注释），OKF 是**跨项目通用规范**。两者**完全正交、互补**：

```
GEB 协议 = "在这个项目里怎么组织文档"（垂直：项目内一致）
OKF 规范 = "跨项目文档怎么互通"（水平：跨项目一致）
```

如果你想把本 wiki 升级成 OKF 兼容，最小改动：

1. 在所有 frontmatter 加 `type: index / raw / note / guide / log`
2. wiki/ 索引版加 `description:` 字段（一句话摘要）
3. wikilink `[[...]]` 保留（Obsidian 渲染 OK），但同时**维护一个 markdown 链接备份**用于 OKF 消费

---

## 行动建议（基于 OKF 启发）

### 立即可做（5 分钟）

- [ ] 给 `wiki/Agent/*.md` 加 `type: index`
- [ ] 给 `wiki/guides/*.md` 加 `type: guide`
- [ ] 给 `wiki/speech/*.md` 加 `type: speech`
- [ ] 给 `wiki/design/*.md` 加 `type: index`

### 中期（30 分钟）

- [ ] 在 `wiki/_index.md`（如果有）做一次 OKF 兼容性扫描
- [ ] 写 `wiki/OKF-兼容性报告.md` 记录对齐进度

### 长期

- [ ] 把 OKF 规范纳入 `wiki/guides/`（跟 `小红书入库流程.md` 同级）
- [ ] 探索 OKF 与 GEB 协议的混合模式（obsidian wikilink for humans + markdown link for agents）

---

## 核心金句

> As foundation models continue to improve, the lack of relevant context often limits what they can do.

> OKF formalizes the LLM-wiki pattern into a portable, interoperable format.

> Just markdown. Just files. Just YAML frontmatter. That's it.

> If you've used Obsidian, Notion, Hugo, or any of the LLM wiki patterns that have emerged over the past year, the shape will feel familiar.

> A fragmented context landscape.

---

## 与本 Wiki 的关联

- [[谷歌发布的开放知识格式（OKF）]] — raw 笔记原文（1 张图，2,199 字 OCR）
- [[小红书入库流程]] — 你已经在用的 LLM-wiki pattern（YAML frontmatter + wikilink）
- [[Claude Code 系统提示词]] — 同样利用 LLM-wiki pattern 喂上下文
- [[Codex 系统提示词]] — 另一类 harness 里的 OKF-style context
- [[AI Agent 开发]] — Multi-Agent 协作的 context 标准

---

*版本：v1.0 · 抓取日期 2026-06-20 · 标签 `#OKF` `#LLM-wiki` `#上下文工程` `#Google Cloud`*