# Wiki 配置

> oh-my-mind 兼容配置

## 基本信息

| 字段 | 值 |
|------|-----|
| Wiki 名称 | cunyu-llm-wiki |
| 主题 | 设计师知识库 · AI 时代的设计与构建 |
| 创建时间 | 2026-06-07 |
| 最后更新 | 2026-06-14 |

## 数据源

| 来源 | 路径 | 说明 |
|------|------|------|
| Cubox | `Cubox/` | 微信公众号、网页收藏 |
| 抖音 | `raw/来自抖音/` | 抖音视频文字稿 |
| X 书签 | `raw/x-bookmarks/` | Twitter 书签 |
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

## 当前主题

| 主题 | 路径 | 文章数 |
|------|------|--------|
| design | `wiki/design/` | 37 篇 |
| speech | `wiki/speech/` | 4 篇 |
| x-bookmarks | `raw/x-bookmarks/` | 10 个分类文件 |
