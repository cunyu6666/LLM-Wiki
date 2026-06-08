# Wiki Log

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
  - 新建 [样机.md](/Users/cunyu666/Projects/cunyu-llm-wiki/wiki/design/样机.md) 作为 MOC 索引页：30 条用 `[[file#heading]]` wikilink 串起
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
