# Audit Report: wiki/design

**Audit ID**: 2026-06-06T00:00:00Z
**Scope**: Full wiki audit (37 files)
**Provenance state**: partial (no session events, file timestamps + frontmatter only)

---

## Summary

| Metric | Value |
|--------|-------|
| Wiki files scanned | 37 |
| Critical findings | 3 |
| Warning findings | 3 |
| Suggestion findings | 2 |
| Files with See Also | 8 / 37 |
| Files with frontmatter | 0 / 37 |
| Files using relative paths | 16 / 37 |
| Largest file | 行业案例与趋势.md (697KB) |

---

## Critical

### C1: No `_index.md` entry point

The wiki has 37 files but no `_index.md` table of contents. `设计资源.md` is a well-structured MOC but only covers the 18 Moonvy-based articles — it misses 17 files including 品牌与视觉, AI设计工具, AI编程与Vibe Coding, 动效与动画, 设计师成长, 行业案例与趋势, LLM与大模型, UX与交互研究, UI设计与组件, AI实操与工具, AI Agent 开发, 设计系统, 前端实现, 设计方法论, 作品集, 其他资源, 硬件项目.

**Recommendation**: Create `_index.md` listing all 37 files organized by category with one-line descriptions. Or expand `设计资源.md` to be the true entry point.

### C2: No YAML frontmatter on any file

None of the 37 files have structured YAML frontmatter (`title`, `category`, `created`, `updated`, `tags`, `summary`). This blocks:
- Machine-readable indexing
- Automated freshness tracking
- Tag-based filtering in Obsidian

**Recommendation**: Add frontmatter to all 37 files. Can be batch-generated from file content.

### C3: Corrupted line in 行业案例与趋势.md

Line 3: `> 42 moonvy 设计素材周刊条目## Sources` — the `## Sources` heading is fused onto the end of the blockquote. Should be two separate lines.

**Fix**: Split into `> 42 moonvy 设计素材周刊条目` + blank line + `## Sources`.

---

## Warning

### W1: 9 files still use relative path links

717+ occurrences of `../../raw/` relative path links across 16 files:
- 行业案例与趋势.md (273), AI编程与Vibe Coding.md (96), AI Agent 开发.md (51), AI设计工具.md (43), 前端实现.md (43), LLM与大模型.md (40), UI设计与组件.md (31), UX与交互研究.md (28), 品牌与视觉.md (23), 抖音设计短视频.md (17), 设计系统.md (15), 动效与动画.md (13), 设计师成长.md (11), AI实操与工具.md (28), 作品集.md (4), 设计方法论.md (1)

Obsidian supports markdown links, but `../../` paths can cause "folder exist" errors. Wikilink format `[[filename|text]]` is more reliable.

**Recommendation**: Convert remaining relative path links to wikilinks.

### W2: 29/37 files lack See Also sections

Only 8 files have `## See Also` for cross-referencing. The wiki lacks interconnection — readers can't navigate between related topics.

**Recommendation**: Add See Also sections linking to related wiki files.

### W3: 3 oversized files

| File | Size | Risk |
|------|------|------|
| 行业案例与趋势.md | 697KB | Slow rendering, scroll fatigue |
| AI设计工具.md | 405KB | Slow rendering |
| 抖音设计短视频.md | 365KB | Index file, acceptable |

**Recommendation**: Consider splitting 行业案例与趋势.md into sub-topics (企业案例, 产品分析, 行业报告, etc.).

---

## Suggestion

### S1: Inconsistent Sources section format

Some files use blockquote stats (`> N moonvy 设计素材周刊条目`), others use plain list under `## Sources`. Both work but visual inconsistency.

### S2: Minor image URL params

Some images retain `&from=appmsg`, `&tp=wxpic`, `&watermark=1` params. These are harmless but add noise.

---

## File-by-file notes

| File | Issues |
|------|--------|
| 行业案例与趋势.md | C3 corrupted line (fixed), W1 relative paths, W3 oversized |
| AI设计工具.md | W1 relative paths, W3 oversized |
| 品牌与视觉.md | W1 relative paths |
| 动效与动画.md | W1 relative paths |
| 前端实现.md | W1 relative paths |
| UI设计与组件.md | W1 relative paths |
| 设计师成长.md | W1 relative paths |
| AI编程与Vibe Coding.md | W1 relative paths |
| UX与交互研究.md | W1 relative paths |
| 设计系统.md | W1 relative paths |
| AI实操与工具.md | W1 relative paths |
| AI Agent 开发.md | W1 relative paths |
| 作品集.md | W1 relative paths |
| 设计方法论.md | W1 relative paths |
| LLM与大模型.md | W1 relative paths |
| All 37 files | C2 no frontmatter |
| 29/37 files | W2 no See Also |
