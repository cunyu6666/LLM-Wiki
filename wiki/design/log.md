# Design Wiki Log

## [2026-06-06] compile | 动效与动画专题编译（96 个抖音视频）
- Source: 抖音"动效与动画"分类 96 条视频文字稿
- Compiled: 动效与动画.md 新增 8 个子主题
  - 品牌/Logo动态设计 (21) / UI动效与微交互 (24) / AE技巧与工具链 (15)
  - C4D与3D动画 (13) / MG动画实战 (9) / 动效作品与灵感 (7)
  - 建筑/空间动画 (5) / 动效设计原理与原则 (2)
- Tools: Groq Whisper API（whisper-large-v3-turbo），遇到 429 限流后完成

## [2026-06-06] ingest | 抖音视频 GIF 预览生成
- Source: 559 个抖音 .mp4 视频
- Output: 521 个 GIF 预览（38 个失败，主要是无声/纯黑视频）
- Location: raw/来自抖音/gifs/，总计 74MB
- Parameters: 240px 宽，1.5fps，前 8 秒，单通道 ffmpeg
- Tools: /tmp/make_gifs.py（使用 static-ffmpeg，系统 ffmpeg 不可用）

## [2026-06-06] fix | GIF 嵌入到 raw .md 文件
- Action: 559 个 raw .md 文件添加 GIF 预览嵌入
- Format: `![[filename.gif]]` 放在 `## 文字稿` 之前
- 修复: 视频嵌入从 `![](file.mp4)` 转为 `![[file.mp4]]`（Obsidian wikilink）
- 修复: 链接从 `[text](file.mp4)` 转为 `[[file.mp4|text]]`

## [2026-06-06] fix | GIF 重复显示问题
- Problem: wiki 中同时出现 2 个（后变 4 个）相同 GIF
- Root cause: `[[filename|text]]` 无扩展名时 Obsidian 解析到 .gif 而非 .md
- Fix: 所有链接加显式扩展名 `[[filename.md|text]]`
- 抖音设计短视频.md 特殊处理：删除冗余第二链接，清理 `·` 分隔符

## [2026-06-06] fix | 断链与格式问题
- 修复 35 个 `%20` 编码断链（文件名空格 URL 编码）
- 修复 26 个 `&valid=true` / `&valid=false` 失效图片参数
- 修复 8 个 `> N sources## Sources` 合并行（blockquote 与 heading 融合）
- 移除所有文件的 Raw Sources 区（文章摘要过长，最长达 777 行）
- 清理 Sources 区（只保留统计行，移除链接列表）

## [2026-06-06] format | /tmp/fix_wiki_format.py 批量格式规范化
- 37 个 wiki 文件批量修复
- 修复项：Raw Sources 移除、Sources 清理、空占位符删除、`####` → `###` 升级、`&valid=` 参数移除、`||` blockquote 修复、See Also 移至末尾、多余空行压缩
- 33/37 文件有改动

## [2026-06-06] doc | 抖音视频入库流程文档
- Created: 抖音视频入库流程.md（项目根目录）
- Content: 7 步流水线（下载 → .md 生成 → 转写 → GIF → 编译 → 链接规范化 → 格式修复）
- 含脚本清单、注意事项、新数据源入库 Checklist

## [2026-06-06] audit | oh-my-mind wiki 审计
- Tool: /wiki:audit（oh-my-mind skill）
- Scope: wiki/design 全部 37 个文件
- Findings: 3 Critical, 3 Warning, 2 Suggestion
- Critical: 无 _index.md、无 YAML frontmatter、行业案例与趋势.md 腐蚀行
- Report: .audit/REPORT.md, .audit/scan-results.json

## [2026-06-06] fix | 创建 _index.md 入口索引
- Created: wiki/design/_index.md
- Coverage: 37 个文件全部覆盖，按「综合主题 / 素材资产 / 其他」分类
- 每个文件含条目数和一句话描述

## [2026-06-06] fix | 37 个文件添加 YAML frontmatter
- Fields: title, summary, tags, created, updated, sources
- 37/37 文件全部添加
- Tools: /tmp/add_frontmatter.py

## [2026-06-06] fix | 696 个链接转为双链接格式
- Pattern: `[text](../../raw/path)` → `[[file.md|text]] ([text](../../raw/path))`
- 15 个文件，696 个链接
- 符合 oh-my-mind 原则 4：Obsidian wikilink + Claude markdown link 同行
- Tools: /tmp/convert_dual_links.py
