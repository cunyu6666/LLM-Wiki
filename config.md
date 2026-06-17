# Wiki 配置

> oh-my-mind 兼容配置

## 基本信息

| 字段 | 值 |
|------|-----|
| Wiki 名称 | cunyu-llm-wiki |
| 主题 | 设计师知识库 · AI 时代的设计与构建 |
| 创建时间 | 2026-06-07 |
| 最后更新 | 2026-06-17 |

## 数据源

| 来源 | 路径 | 说明 |
|------|------|------|
| Cubox | `Cubox/` (gitignored) | 微信公众号、网页收藏 |
| 抖音 | `raw/来自抖音/` | 抖音视频文字稿 |
| X 书签 | `raw/x-bookmarks/` + `raw/x-audio/` + `raw/x-transcripts/` | Twitter 书签 + 视频 + 转录 |
| Moonvy 周刊 | `raw/moonvy-weekly/` | 设计素材周刊 |
| 手动笔记 | `raw/design/` 等 | 分类后的原始素材 |

## 编译规则

- **raw/** 不可变，只增不改
- **wiki/** 从多源编译而来，可迭代更新
- 文章使用 `[[wikilink]]` 双链
- 每个引用必须标注来源路径

## Obsidian 集成

- 双链接：`[[wikilink]]` + `[markdown](path)` 同行
- 图谱视图：按 tags 分组

## Skill 配置

两份并存的 Karpathy LLM Wiki skill，职责明确：

| 路径 | 角色 | 来源 |
|------|------|------|
| `.agents/skills/karpathy-llm-wiki/` | 上游装版本，**被 Agent Skills 标准工具加载** | `skills-lock.json` 锁定 hash |
| `skills/karpathy-llm-wiki/` | 项目扩展版：MCP/Setup/Quick Build/Full Build/Farmer agents | 项目内部扩展 |

`skills-lock.json` 锁的是 `.agents/skills/` 的 hash，跟 `skills/` 无关。修改扩展版后建议把变化同步到 `.agents/skills/SKILL.md` 的 `description` 字段，否则两者会持续漂移。

## 当前主题

| 主题 | 路径 | 文章数 |
|------|------|--------|
| design | `wiki/design/` | 40 篇（含 .audit 报告） |
| speech | `wiki/speech/` | 6 篇 |
| x-bookmarks | `wiki/x-bookmarks/` | 10 个分类文件 + 1 _index |
| Agent | `wiki/Agent/` | 5 个系统提示词（Claude/Codex/Catui/Open Design/Claude Design） |
| guides | `wiki/guides/` | 4 篇（X 书签导出、X API 调通、抖音下载、抖音入库） |
