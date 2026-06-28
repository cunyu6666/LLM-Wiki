---
type: log
description: "## ingest | xhs mega batch #1 (10 articles, 47 images)"
timestamp: 2026-06-20
---
# Wiki Log

## [2026-06-20] compile | 5 篇 Youtube raw 编译入 wiki
- AI Agent 开发.md：新增「Claude Architect 多智能体编排」章节（层级式任务分解 + 异构子 Agent + 沙箱隔离）
- AI设计工具.md：新增「Claude Code 作为设计工具」章节（Griffin Wooldridge 设计工作流）+ 「Framer Agents 与协作式 AI 设计」章节（Canvas Agent、分支、上下文感知编辑）
- 设计师成长.md：新增「Ryo Lu 谈设计师与开发者的融合」章节（a16z 播客：角色融合、品味本质、设计师变为开发者）
- Raw sources: Claude-Architect多智能体编排、把Claude-Code变成设计天才、Framer发布会介绍Agents与分支、Cursor的Ryo-Lu谈设计活工具与编程未来、Ryo-Lu谈AI将设计师变为开发者

## [2026-06-20] ingest | xhs mega batch #2 (19 URLs, 18 success, 85 images)
- Source: 用户一次提供 19 条小红书 URL
- Failure: `6a1e5af4...` (23KB，被反爬，仅 18 条成功)
- Method: 复用 mega batch #1 流程（curl 并发抓 + Vision API 并发 OCR）
- 18 条笔记（按主题）:
  - **AI Agent 开发 (4)**: Continual Harness / SkillOpt / ECC / Anthropic设计负责人 / 孙立超团队 Agent 自进化
  - **AI 编程 (5)**: AI Coding Agent / /teach / Claude Code 首席设计师 / OpenSpec / 野生AI产品
  - **AI 设计工具 (5)**: 设计跟开发不用打架 / Claude设计负责人播客 / AI in Design Report / 资讯简报×2
  - **AI 应用 (3)**: AnySearch / 硅谷脑电波 / (空标题)
  - **亮点**: SkillOpt (13k字) — Agent Skills 自进化；Continual Harness (5k字) — Agent 自进化；ECC (1.2k字) — everything-claude-code
- Files:
  - `raw/小红书/<title>_<note_id>.md` × 18
  - `raw/小红书/imgs/<note_id>/{1..N}.jpg` × 85
  - `wiki/design/<title>.md` × 18 索引版（OKF frontmatter）
- Stats: 总 OCR 字数 50,150（自适应分位数阈值修复后提升 10×）
- **关键修复**：OCR 重建阈值从 `h * 1.3` 改为基于 y 间距分布的 30% 分位数（自适应密度）
- **可读性后处理**：批量正则替换 Vision API 常见误识（Al→AI / Github→GitHub / scndle→schedule / Lollm→LLM 等）；按 zh_ratio 分 4 级（good/mixed/english/multicol），每条加可读性说明 frontmatter
- **空标题处理**：`6a16bc57...` 标题为空但 desc 完整，自动用 desc 替换 OCR 主体
- **失败处理**：`6a1e5af4...` xsec_source 是 `pc_search` 而非 `pc_collect`，触发反爬；以后仅保留 `pc_collect` 来源

## [2026-06-20] ingest | xhs mega batch #1 (10 articles, 47 images)
- Source: 用户一次提供 10 条小红书 URL 批量入库
- Method: xargs + curl 并发抓 HTML（避开 Python urllib SSL 限制）→ 批量 JSON 解析 → curl 批量下载图 → Vision API 并发 OCR → 按 y 降序 + x 升序重建阅读顺序（自适应行高阈值）
- 10 条笔记:
  1. AI没有护城河_这是Anthropic最不想承认的事 (5图) → AI编程与Vibe Coding
  2. Cursor工程师说了大实话_全栈通才是伪命题 (6图) → AI编程与Vibe Coding
  3. figma设计负责人对AI coding的看法 (2图) → AI设计工具
  4. Anthropic Deep Research_ 多智能体架构 (7图) → AI Agent 开发
  5. webclaw将html清洗成AI友好的数据格式 (1图) → AI应用
  6. Loop Engineering 是什么｜8 张图讲透 (8图) → AI Agent 开发
  7. Claude Code 30万行代码的核心 (4图) → AI Agent 开发
  8. 我理解的 AI 设计工作台_三层就够了 (5图) → AI Agent 开发
  9. Shopify内部AI必须全员公开_让私聊变群聊 (8图) → AI应用
  10. 谷歌发布的开放知识格式（OKF） (1图) → AI应用
- Files:
  - `raw/小红书/<title>_<note_id>.md` × 10
  - `raw/小红书/imgs/<note_id>/{1..N}.jpg` × 47
  - `wiki/design/<title>.md` × 10 索引版
- Stats: 总 OCR 字数 20,746
- **关键修复**：OCR 重建阈值改用自适应行高（`h*1.3`），原固定 0.012 导致小字段落全被判为换段 → 标题以外全部丢失
- **最关键笔记**：`谷歌发布的开放知识格式（OKF）` — 跟本 wiki 架构（Obsidian wikilink + frontmatter）直接相关，OKF v0.1 就是 LLM-wiki pattern 的形式化规范

## [2026-06-20] ingest | xhs third batch (1 article, 12 images)
- Source: 小红书 `https://www.xiaohongshu.com/explore/6a31046d0000000011010e16`
- Title: Zynga 创始人：先抄对，再创新
- Author: 小红书号「奇点日记」转载自 Lenny 播客 · Mark Pincus
- Method: 复用 xhs first batch 流程
- Files:
  - `raw/小红书/Zynga 创始人先抄对再创新_6a31046d0000000011010e16.md`
  - `raw/小红书/imgs/6a31046d0000000011010e16/{1..12}.jpg`（已按 note_id 命名空间隔离）
  - `wiki/speech/Zynga 创始人先抄对再创新.md`
- Back-links: `wiki/speech/0620 计划与进展.md` 已收录
- Stats: 181 赞 / 253 收藏 / 1 评论 / ~4625 字 OCR
- Core: Proven-Better-New 三段框架 + 6 大洞察

## [2026-06-20] ingest | xhs user-pasted image (1 article, IDE OCR)
- Source: 用户在 Claude Code IDE 内贴入的 PNG 截图（非真实小红书笔记）
- Title: High-Performance Teams in the Age of AI: Learnings from Lovable
- Author: Felix Haas (Lovable 创始人, designplusai.com)
- Method: IDE 内置 OCR → 人工归档（无 curl/无 imgs/，纯文本）
- Files:
  - `raw/小红书/High-Performance Teams in the Age of AI_ felix-haas-ai-teams.md` — 含 note 字段注明非真实 xhs
  - `wiki/design/High-Performance Teams in the Age of AI.md` — 7 条原则速查表
- Back-links: `wiki/design/AI Agent 开发.md` See Also 区追加
- 用途：Lovable / AI Teams / Leadership 主题入库；与 `Dan Koe 人生就四件事` 互为镜像（DanKoe 强调"Build in Public"，Felix 强调"Ship then improve"）

## [2026-06-20] ingest | xhs second batch (1 article, 11 images)
- Source: 小红书 `https://www.xiaohongshu.com/explore/6a17099700000000070210da`
- Title: Dan Koe：人生就四件事，其余全是噪音
- Author: 小红书号 `DanKoe行动指南`（从图片 OCR 识别）
- Method: 复用 xhs first batch 流程（见 `wiki/guides/小红书入库流程.md`）
- Files:
  - `raw/小红书/Dan Koe 人生就四件事_6a17099700000000070210da.md`
  - `raw/小红书/imgs/6a17099700000000070210da/{1..11}.jpg`
  - `wiki/speech/Dan Koe 人生就四件事.md` — 演讲素材落点
- Back-links: `wiki/speech/0620 计划与进展.md` 已收录
- Stats: 1,271 赞 / 1,610 收藏 / 10 评论 / ~2394 字 OCR
- **Bug 修复 + 流程补强**：
  - 第 1 轮 `imgs/1.jpg` 被第 2 轮覆盖 → 立即从 `/tmp/xhs/imgs/` 恢复 A 的图 1-9
  - 改用 `imgs/<note_id>/N.jpg` 命名空间隔离（已写入 `wiki/guides/小红书入库流程.md` 强制约定）

## [2026-06-20] ingest | xhs first batch (1 article, 9 images)
- Source: 小红书 `https://www.xiaohongshu.com/explore/6a2bf71e000000002100a7d2`
- Title: 一文读懂 Agent、harness、Loop 等概念：AI 的边界在哪？
- Method: `curl` + iPhone UA + Referer 抓 HTML → `__INITIAL_STATE__` JSON 解析 → urllib 下载 9 张原图 → macOS Vision API (`VNRecognizeTextRequest`) OCR → 视觉坐标重建阅读顺序
- Files:
  - `raw/小红书/一文读懂 Agent、harness、Loop 等概念_6a2bf71e000000002100a7d2.md` — 主文档 + 完整 OCR 文字稿
  - `raw/小红书/imgs/1-9.jpg` — 9 张原图（按抖音 `gifs/` 约定对齐，命名用 `imgs/`）
  - `wiki/Agent/一文读懂 Agent、harness、Loop 等概念.md` — 索引版，含摘要 / 三段大纲 / 核心金句 / 关联链接
- Back-links: `wiki/design/AI Agent 开发.md` See Also 区追加反向链接
- Stats: 719 赞 / 717 收藏 / 10 评论 / ~3442 字 OCR 全文
- Note: 首次接入小红书数据源；建立 `raw/小红书/` 目录；未登录态下作者昵称无法解析（仅 author_id）

## [2026-06-05] ingest | design full build (386 articles with full text)
- Source: Cubox CLI batch fetch — 386 design-related articles with full Markdown content
- Compiled: 11 wiki articles from 386 raw sources (~78KB)
- Topics:
  - AI设计工具 (110 sources → 1 article)
  - 设计资源与周刊 (76 sources → 1 article)
  - 设计趋势与行业 (43 sources → 1 article)
  - UX与交互设计 (37 sources → 1 article)
  - 品牌与视觉设计 (26 sources → 1 article)
  - 前端与设计开发 (23 sources → 1 article)
  - 设计系统与规范 (12 sources → 1 article)
  - 产品与创业 (8 sources → 1 article)
  - AI产品设计 (7 sources → 1 article)
  - 设计师成长 (6 sources → 1 article)
  - 杂项 (37 sources → 1 article)
- Tools used: Cubox CLI for full-text fetch, 7 parallel agents for compilation
- Note: This is the first full-text build. Previous build used Cubox sync (title+description only) and was replaced.

## [2026-06-05] recompile | design granular rebuild (386 articles → 16 wiki pages)
- Action: Replaced 11 consolidated articles with 16 granular, topic-specific articles
- New articles:
  - Claude Design (8 sources)
  - Figma与MCP (19 sources)
  - Cursor与AI编程设计 (17 sources)
  - AI设计工具综合 (32 sources)
  - UX方法论与研究 (28 sources)
  - 设计资源与周刊 (66 sources)
  - 品牌与视觉设计 (31 sources)
  - 前端与设计开发 (20 sources)
  - 设计系统与DESIGN.md (12 sources)
  - 设计师职业发展 (13 sources)
  - Lovart与AI设计Agent (5 sources)
  - AI产品设计模式 (5 sources)
  - 产品设计与创业 (5 sources)
  - AI产品与界面 (13 sources)
  - 设计工具与资源 (8 sources)
  - 设计杂谈 (11 sources)
- Tools used: 14 parallel compilation agents
- Note: Google Stitch (1 source) merged into AI设计工具综合. 124 uncategorized articles split into 3 thematic articles (AI产品与界面, 设计工具与资源, 设计杂谈).

## [2026-06-05] ingest | moonvy 设计素材周刊 213 期 → 8 个 Design 分类
- Source: Moonvy 月维「设计素材周刊」213 期（2022-02 至 2026-05），3000 个条目已按主题分桶
- Routed:
  - 行业案例与趋势 +743
  - 作品集与灵感 +1531
  - AI设计工具 +629
  - 设计方法论 +44
  - UX与交互研究 +38
  - UI设计与组件 +8
  - 设计系统 +5
  - 品牌与视觉 +2
- Method: section 头机械分桶为主，AI/方法论/UX 类条目做关键词二次路由
- Format: 原文 + 外部图片链接保留；按周报期数倒序排列；图片采用 moonvy.com 外部 URL
- Tools: Python 抽取脚本（按 ##/### 切片 + 关键词路由）

## [2026-06-05] ingest | moonvy 设计素材周刊 213 期 → 14 个 Design 分类（精修重排）
- Source: Moonvy 月维「设计素材周刊」213 期（2022-02 至 2026-05），3000 个条目已按主题分桶
- Initial route: section 头机械分桶为主，AI/方法论/UX 类条目做关键词二次路由
- Refinement: 对散落在 industry_trends/portfolio/ai_tools 中具备强信号（body 内 ≥ 2 关键词）的 97 个条目做精修 re-route
- Re-routes:
  - 动效与动画 +37（来自 industry_trends 18、ai_tools 13、portfolio 5、ux_research 1）
  - 前端实现 +33（来自 portfolio 19、industry_trends 8、ai_tools 6）
  - LLM与大模型 +10（来自 ai_tools 5、portfolio 4、industry_trends 1）
  - AI Agent 开发 +6（来自 industry_trends 4、portfolio 1、ai_tools 1）
  - 设计师成长 +6（来自 industry_trends 3、portfolio 3）
  - AI编程与Vibe Coding +5（来自 portfolio 3、industry_trends 2）
- Final distribution (12/15 categories):
  - 作品集与灵感 1496 / 行业案例与趋势 707 / AI设计工具 604
  - 设计方法论 44 / UX与交互研究 37 / 动效与动画 37
  - 前端实现 33 / UI设计与组件 8 / AI Agent 开发 6
  - 设计师成长 6 / 设计系统 5 / AI编程与Vibe Coding 5
  - LLM与大模型 10 / 品牌与视觉 2 / AI实操与工具 0
- Format: 原文 + 外部图片链接保留（moonvy.com 外链 3249 处）；按周报期数倒序排列
- Tools: Python 抽取脚本（按 ##/### 切片 + 关键词路由 + 精修 re-route）

## [2026-06-05] restructure | 作品集与灵感 拆分为 MOC hub + 18 个子文章
- 拆分依据：原 作品集与灵感.md moonvy 节 1496 条目过密，按资源类型细分到 18 个子文章
- 跳过：18 条「我们是谁？」类 moonvy 自宣
- 子文章（按资源类型）:
  - 作品集-图标 (272) / 作品集-插画 (126) / 作品集-3D模型 (87)
  - 作品集-字体 (97) / 作品集-背景与渐变 (67) / 作品集-UI模板与设计系统 (185)
  - 作品集-动效与加载 (63) / 作品集-灵感网站 (81) / 作品集-免费资源 (58)
  - 作品集-图库与配色 (15) / 作品集-SVG素材 (48) / 作品集-数据与可视化 (16)
  - 作品集-Figma技巧与插件 (18) / 作品集-AI应用 (23) / 作品集-硬件项目 (3)
  - 作品集-教程与复刻 (19) / 作品集-材质与拟物 (15) / 作品集-其他资源 (285)
- MOC hub: 作品集与灵感.md moonvy 节改为导航表，含 18 个子文章链接 + 拆分规则
- 路由规则：标题/正文关键词优先匹配，按桶顺序第一个匹配归类

## [2026-06-05] restructure | 18 个作品集子文章去前缀，作品集回退为纯项目目录
- 动作：
  - 18 个 `作品集-*.md` 子文章统一去掉 `作品集-` 前缀，升级为 wiki/design/ 同级独立资源文章
  - `作品集与灵感.md` 重命名为 `作品集.md`，移除 moonvy MOC 段，回归顶级设计师作品集项目主题
- 命名映射：
  - 作品集-图标 → 图标.md / 作品集-插画 → 插画.md / 作品集-3D模型 → 3D模型.md
  - 作品集-字体 → 字体.md / 作品集-背景与渐变 → 背景与渐变.md
  - 作品集-UI模板与设计系统 → UI模板与设计系统.md / 作品集-动效与加载 → 动效与加载.md
  - 作品集-灵感网站 → 灵感网站.md / 作品集-免费资源 → 免费资源.md
  - 作品集-图库与配色 → 图库与配色.md / 作品集-SVG素材 → SVG素材.md
  - 作品集-数据与可视化 → 数据与可视化.md / 作品集-Figma技巧与插件 → Figma技巧与插件.md
  - 作品集-AI应用 → AI应用.md / 作品集-硬件项目 → 硬件项目.md
  - 作品集-教程与复刻 → 教程与复刻.md / 作品集-材质与拟物 → 材质与拟物.md
  - 作品集-其他资源 → 其他资源.md
- 原则：「作品集」目录只放顶级设计师作品集项目（Behance/Dribbble 等），其他资源类（图标/字体/UI 套件等）作为独立 design 主题存在

## [2026-06-05] cleanup | 全局移除 moonvy 品牌/自宣图 165 张
- 目标：去除周报中无意义的设计师自宣图（"我们是谁" 类 section-end promo）
- 移除的 3 个图片 hash：
  - bc408645a23b4c7e.png（88 张，#024+ 期刊使用）
  - d65850e1cc6d69eb.jpg（48 张，#001-#023 早期期刊使用）
  - fdaba363e3b35e0d.png（29 张，#160+ 期刊使用）
- 总计：23 篇 wiki 文章移除 165 张品牌图
- 校验：剩余 moonvy.com 图片 3066 张（3231 - 165），无残留品牌图

## [2026-06-05] fix | 墨水屏手表从 3D模型.md 移到 硬件项目.md
- 问题：原 qpaperOS（ESP32 智能手表固件 DIY）被错分到 3D模型.md，本质是硬件项目（开源固件 + 3D 打印外壳）
- 原则：3D模型.md 定位为"现成 3D 资产库"，DIY 硬件项目的 3D 文件归硬件项目.md
- 验证 3D模型.md 其他条目：剩余 86 条均为现成 3D 资源（图标/场景/角色/样机），无类似错分
- 顺手修复：硬件项目.md 内部标题 `# 作品集-硬件项目` → `# 硬件项目`（去前缀遗漏）
- index.md 计数：3D模型 87→86，硬件项目 3→4

## [2026-06-05] restructure | 样机资源改 MOC 索引模式（Level 1+2 混用）
- 思路转变：单一归属太刚，改用 Obsidian 原生 hub-and-spoke + 内联标签
- 动作：
  - 30 条样机相关条目**原地不动**（保留在 4 个原文件中：UI模板与设计系统 25 / 3D模型 2 / 图标 1 / 背景与渐变 2）
  - 每条加内联标签 `> 标签：#样机`（双标签 2 条额外加 `#3D模型`）
  - 新建 [样机.md] 作为 MOC 索引页：30 条用 `[file#heading]` wikilink 串起
- 优势：
  - 维护成本零（改 1 处即所有引用同步）
  - karpathy-llm-wiki skill 兼容（canonical 唯一，lint 不破）
  - Obsidian 反向链自动聚合
  - 双归属天然支持（如"3D 手指 - 手表 UI 样机"在 3D模型.md 是 #3D模型 #样机，browsing 任何一维都能找到）
- index.md 计数：30 条样机资源（MOC 页）

## [2026-06-06] cleanup | design 分类优化与元数据修复
- 修复 18 篇文章 H1 标题与文件名不同步（`作品集-*` 前缀残留）
- 修复 `作品集.md` 标题：`作品集与灵感` → `作品集`
- 重写 `index.md`：删除 18 条幽灵重复项（`作品集-*` 已不存在），拆分为「知识洞察」+「设计资源」两组
- 修正 `作品集` 来源计数：1517 → 21（拆分后旧计数未更新）
- 新建 [设计资源.md](design/设计资源.md) 作为 Moonvy 素材总 MOC 索引页
- 样机.md 添加 See Also 指向设计资源 MOC

## [2026-06-06] cleanup | P0/P1 分类优化 + 抖音 ingest
- P0 其他资源清理：285 → 156 条（删除 12 条噪音，搬迁 117 条到目标分类）
  - → UI模板与设计系统 +40 / 灵感网站 +30 / AI应用 +21 / 图标 +9 / 插画 +5 / Figma技巧 +5 / 行业案例 +5 等
- P1 动效与加载 → 动效灵感（63 → 62 条，4 条灵感站迁入灵感网站）
- ingest | 抖音设计短视频：425 条设计类抖音文字稿（raw/来自抖音/）
- 修复灵感网站恢复后条目丢失问题（81 + 30 = 111）
- index.md / 设计资源.md 更新计数与分组

## [2026-06-06] compile | P2 深度编译 + 其他资源 R2 清理
- R2 其他资源：156 → 81（搬迁 64，删除 11）
  - → 灵感网站 +26 / 行业案例与趋势 +16 / UI模板 +10 / 插画 +5 / 教程 +3 等
- compile | 3D模型.md：新增「Spline 轻量 3D 工具」编译章节（7 条抖音 + 交叉引用）
- compile | 前端实现.md：新增「CSS 文字方向属性」章节（writing-mode / inline-size / block-size）
- refactor | AI应用 ↔ AI设计工具：明确分工（工具链 vs 产品案例），双向 See Also
- index.md / 设计资源.md 同步更新

## [2026-06-06] lint | P3 去重 + 排版 + 抖音编译
- 修复 10 篇 See Also 断链：`作品集与灵感` → `作品集`
- Moonvy 目录去重：3D模型 −3（Vector to 3D 促销重复）、图标 −2、免费资源 −2；泛化标题加「周刊 #N」后缀
- 行业案例与趋势：删除 134 个重复 raw 块；作品集：删除 16 个重复 raw 块
- 排版：资源文章去除多余 `---`、压缩空行；抖音设计短视频改为短 ### + 完整标题 blockquote
- compile | UI设计与组件 / 动效与动画 / 品牌与视觉：各新增「抖音短视频补充」5 条洞察
- index.md：3D模型 知识/资源分工说明；同步条目计数（图标 280、3D 84、字体 101、免费 58 等）
- 新增脚本 `scripts/optimize-wiki-design-p3.py`；更新 `ingest-douyin-design.py` 标题格式

## [2026-06-09] ingest | Cubox API sync (31 new articles)
- Source: Cubox API direct fetch via `cubox-cli` API endpoints
- New articles saved to `Cubox/` directory (2026-05-20 to 2026-06-08)
- Key topics:
  - Anthropic Skill 方法论、上下文工程（Context Engineering）
  - Agentic Workflow、设计走查 AI 全自动
  - Cursor Composer 2.5、Codex Annotation、MiniMax M3
  - DeepSeek DeliAutoResearch SKILL、Reasonix 缓存优化
  - HTML 版剪映、Quarkdown、Presenton、Lovart、Tolaria
  - 2026 科技中的设计报告（UX→AX）、Vercel 设计团队、Claude Design
  - 8 个 AI 时代产品设计模式、Agent 时代 UI 设计
- Wiki pages updated: AI实操与工具, AI编程与Vibe Coding, 设计师成长, 设计方法论, 行业案例与趋势, AI Agent 开发, LLM与大模型
- Tools used: Cubox API (curl), Python batch script

## [2026-06-09 → 2026-06-14] 拉取远端增量
- 提交 a1bd9a7：原始素材入仓（raw/x-audio/、raw/x-transcripts/、raw/x-bookmarks/gifs/）
- 提交 965cce7：Agent 系统提示词合集（Claude Code / Claude Design / Codex / Catui / Open Design）→ wiki/Agent/
- 提交 81eaf32：演讲素材与计划更新
- 抖音下载/入库流程从根目录并入 wiki/guides/

## [2026-06-17] cleanup | P0 显性错误与索引归一
- 删除 3dmax.md（0 字节空文件，6-10 残留）
- 删除 raw/xiaohongshu_favorites.json（空数组）
- 同步 config.md：design 37→40、speech 4→6、新增 x-bookmarks/Agent/guides 三个模块
- 在 config.md 增补"Skill 配置"小节，注明 .agents/skills/ 与 skills/ 双份关系
- wiki/index.md：合并 3D模型 知识/资源双条目（84+7 与 84），补 speech 和 Agent 板块，扩 guides 至 4 条
- wiki/design/_index.md 改为重定向页（指向 wiki/index.md#design），保留 67 行历史快照供回溯
- wiki/scan_progress.md（531 行 6-08 停止）归档为 wiki/guides/lint-history.md；wiki/ 根留重定向
- inventory/_index.md 增"重审"批注，标记 10 条待抓取 Cubox 链接已 8 天未处理

## [2026-06-17] 待办
- inventory 10 条 Cubox 待抓取未处理，建议逐条确认后清理
- 3 条"待入库素材"的 raw 来源路径缺失，需要补
- skills/ 与 .agents/skills/ 内容仍漂移（前者 392 行扩展版，后者 187 行上游版），建议下次 Lint 时统一
- moonvy.com 3066 张外链未做存活率验证

## [2026-06-29] ingest | Vercel product-design 三件套
- Source: https://vercel.com/blog/teaching-agents-product-design-at-vercel (2026-06-25)
- Raw: `raw/design/2026-06-29-Teaching-Agents-Product-Design-at-Vercel.md` (25KB, 含 SKILL.md 模板与 ESLint rule 代码块)
- 新建: `wiki/design/用 Skill 与 Lint 教 Agent 做产品设计.md`
  - 概念:把产品设计决策编码成 SKILL.md + Lint + Eval 三件套,让 coding agent 继承 reasoning 而非只复制模式
  - 关键数据:Vercel 内部 Next.js evals 显示 56% 情况下 agent 未 invoke 可用 skill
- Cascade:
  - `wiki/design/AI Agent 开发.md`:在「Agent Skills 与工具构建」章节末插入 Vercel product-design 子节作为标杆范例
  - `wiki/design/AI编程与Vibe Coding.md`:See Also 增加新文章链接
- Index: `wiki/index.md` design 段新增条目,`Sources` 计数 1

## [2026-06-29] compile | speech 整理稿副本
- 在 `wiki/speech/Vercel-用-Skill-与-Lint-教-Agent-做产品设计-整理稿.md` 放了一份独立可传播的整理稿(7KB)
- 与 `wiki/design/用 Skill 与 Lint 教 Agent 做产品设计.md` 互链,前者是完整中文编译版,后者是可独立分享的短稿

## [2026-06-29] organize | wiki/speech 目录重整
**A. 整理稿重命名(顶层,5 篇)**
- 旧:`Dan Koe 人生就四件事.md` → 新:`2026-06-20-Dan-Koe-人生就四件事-整理稿.md`
- 旧:`Dan-Carey-Claude-Design-整理稿.md` → 新:`2026-06-20-Dan-Carey-Claude-Design-整理稿.md`
- 旧:`Ryo-Lu-Closer-to-the-Material-Compile-2026-整理稿.md` → 新:`2026-06-20-Ryo-Lu-Closer-to-the-Material-Compile-2026-整理稿.md`
- 旧:`Zynga 创始人先抄对再创新.md` → 新:`2026-06-20-Zynga-创始人先抄对再创新-整理稿.md`
- 旧:`Vercel-用-Skill-与-Lint-教-Agent-做产品设计-整理稿.md` → 新:`2026-06-29-Vercel-用-Skill-与-Lint-教-Agent-做产品设计-整理稿.md`

**B. 过程笔记移入新建的 `notes/` 子目录(12 篇)**
- 0620 计划与进展.md → notes/2026-06-20-计划与进展.md
- idea-fragments.md → notes/想法碎片.md
- new-sources.md → notes/新来源.md
- sources.md → notes/来源清单.md
- plan.md → notes/计划.md
- 证据表.md → notes/证据表.md
- ⭐️ Key Sentense.md → notes/关键句索引.md
- outline-0620-catui.md → notes/2026-06-20-Catui-演讲大纲.md
- outline-v1.md → notes/演讲大纲-v1.md
- outline-v2.md → notes/演讲大纲-v2.md
- speech-0620-catui.md → notes/2026-06-20-Catui-演讲稿.md
- design-to-build-agent-era-speech-20min.md → notes/2026-06-设计到构建Agent时代-20分钟演讲稿.md

**C. Cascade 引用更新**
- wiki/index.md: 6 条 speech 子条目路径 + 标题改中文
- wiki/speech/CLAUDE.md: 顶层 Ryo Lu 旧名 → 完整 5 篇整理稿清单
- wiki/speech/yt-talks/CLAUDE.md: 2 条 cross-dir 引用(sources / outline-v1/v2 → notes/)
- wiki/guides/YouTube视频入库流程.md: 2 条 sources.md 引用
- wiki/design/OKF 兼容性报告.md: 1 条 [[0620 计划与进展]] wikilink
- wiki/design/High-Performance Teams in the Age of AI.md: 1 条 [[Dan Koe 人生就四件事]] wikilink
- wiki/design/设计素材周刊-014.md: 1 条 [[idea-fragments]] wikilink
- wiki/speech/2026-06-20-Zynga-创始人先抄对再创新-整理稿.md: 2 条 wikilink
- wiki/speech/2026-06-20-Dan-Koe-人生就四件事-整理稿.md: 2 条 wikilink
- wiki/speech/notes/计划.md: 6 条 markdown 表格路径

**D. 不动的部分**
- wiki/log.md 历史条目保留旧文件名(append-only 日志不该改写历史)
- yt-talks/ 子目录未触碰(10 个视频整理稿命名规范不动)
