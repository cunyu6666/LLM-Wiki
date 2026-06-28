# CLAUDE.md - wiki/speech 模块

## 模块定位

`wiki/speech/` 存放**演讲 / talk 的整理稿与过程笔记**。结构：
- 顶层：对外的**整理稿成品**（按 `YYYY-MM-DD-标题-整理稿.md` 命名）
- `notes/`：过程性笔记（演讲大纲、计划、证据表、想法碎片等）
- `yt-talks/`：YouTube 演讲整理稿（含视频抽帧，CLAUDE.md 单独维护）
- `assets/`：所有演讲的配图集中目录

每篇对外整理稿一个 `.md` 文件，配套：
- 原始素材：`raw/来自<平台>/` 下同名 `.transcript.md` + 视频源
- 配图：`assets/<talk-slug>/`（视频抽帧，jpg）

当前收录（按日期排序，最新在前）：
- `2026-06-29-Vercel-用-Skill-与-Lint-教-Agent-做产品设计-整理稿.md` — Vercel 官方 blog 整理稿（中文编译版）
- `2026-06-20-Ryo-Lu-Closer-to-the-Material-Compile-2026-整理稿.md` — Ryo Lu @ Compile 2026（含 10 张配图）
- `2026-06-20-Dan-Carey-Claude-Design-整理稿.md` — Dan Carey @ Anthropic Labs · Claude Design
- `2026-06-20-Dan-Koe-人生就四件事-整理稿.md` — Dan Koe "人生就四件事"
- `2026-06-20-Zynga-创始人先抄对再创新-整理稿.md` — Mark Pincus · Lenny's Podcast

过程笔记见 `notes/` 子目录（计划、大纲 v1/v2、证据表、想法碎片等）。

## 整理稿写作约定

- 标题：`<演讲者角色>：<原标题>`
- 章节结构：分章整理 + 末尾完整原文（无时间戳）
- 引文：使用 `> 「…」（中文）` 格式
- 表格：用 markdown 表格，不引入 HTML
- 金句索引：每条带原始时间码（如 `— 04:44`）
- 末尾"相关"区：链接原始 transcript、主笔记、整理流程文档

## 视频抽帧配图流程（GEB_PROTOCOL 同步）

> **核心经验**：**绝对不能凭直觉抽帧**——必须密集采样 → 拼图比对 → 精确定位。

### 步骤

1. **建索引**：用 `ffmpeg -i video.mp4 -vf "fps=1/10,scale=480:-1" -q:v 5` 每 10 秒采一帧
2. **拼总览**：用 PIL（不要用 `montage` 命令，本机 ImageMagick 对 JPEG 输入有 bug）把索引帧拼成 3 列总览图，肉眼读整段时间轴
3. **细找目标**：围绕候选时间点 ±15s 密集抽 4 帧，PIL 拼成 4 联图，确认精确时间点
4. **正式抽帧**：`ffmpeg -ss <sec> -i video.mp4 -frames:v 1 -q:v 2 output.jpg`
5. **逐张校验**：每一张都 Read 一次，眼见为实——**不能相信参数就放过**

### 命名约定

`<序号>-<画面主题短描述>.jpg`，例如：
- `01-ryo-os-messages.jpg` — 第一张，主题是 Ryo OS Messages
- `04-more-mediocre.jpg` — 第 4 张，画面核心金句

主题短描述用英文短语（小写 + 连字符），便于跨工具引用。

### 存放路径

`assets/<演讲者-场合-年份>/` 同模块子文件夹，**绝不放在 raw/ 下**（raw 是只读档案）。

### frontmatter 同步

每次新增图片必须更新演讲整理稿 frontmatter 的 `attachments` 字段，列全部图片相对路径。

## 链接写作规范

- 内链到图片：`![alt](assets/...)`（标准 markdown）+ 图注用 `*<small>...</small>*`
- 内链到同模块其他演讲：相对路径 `../<其他演讲>.md`
- 内链到 raw 素材：相对路径 `../../../raw/来自<平台>/<文件>.md`

## 错误学习

### ❌ 单点抽帧 + 直觉选时间（2026-06-28 Ryo Lu 案例）
第一次直接用 `ffmpeg -ss 00:02:30` 等孤立时间点抽帧，结果 9 张中 5 张错位。原因：
- 前 02:30 一直是 Ryo OS 桌面演示而非 PPT，导致后续 PPT 时间码整体偏早 ~1 分钟
- 离散抽样容易抽到过渡帧 / 动画帧 / 介绍页

**正确做法**：见上面的"视频抽帧配图流程"。

### ❌ 用 `magick montage` 拼图（2026-06-28）
本机 ImageMagick 7 在 montage 多 JPEG 输入时报 "no decode delegate"，但单文件转换正常。绕过方法：全部用 Python + PIL 拼图。