# 演讲准备计划：Design → Build

> 演讲标题：**从 Design 到 Build：Agent 时代体验设计的新边界**
> 场合：阿里 D20 全球设计院长峰会（对外分享）
> 时长：20min · 中文 · 无需 live demo
> 听众：设计师为主
> 演讲日期：7月11日 · PPT 初稿截止：6月25日
> QoderWork 身份：可以公开演讲 ✅

---

## 阶段总览

| 阶段 | 时间 | 产出 |
|------|------|------|
| ① 素材补齐 | 6/15 - 6/17（3天） | 调研文档、原文入库、大纲定稿 |
| ② 内容设计 | 6/18 - 6/19（2天） | content-doc 终版、PPT 模板骨架 |
| ③ PPT 制作 | 6/20 - 6/24（5天） | 精美 PPT 初稿（含动效） |
| ④ 交付 | 6/25 | 提交 PPT 初稿 |

> 💡 **硬件原型已降级**：PPT 里只用 1 页"软件 → 硬件延伸"概念图占位，不做实物。省下时间专注 PPT 内容打磨。

---

## 阶段 ① 素材补齐（6/15 - 6/17）

### Day 1 · 6月15日（周一）— 调研日

> 🔴 **今日必须完成：所有调研产出物落盘**
> ⏰ 下班前 checklist：5篇原文链接确认 ✓ / 3份调研文档 ✓ / outline-v1 review 意见 ✓

**上午（9:00-12:00）：原文链接确认 + 启动调研**

- [x] **确认演讲基本参数** ✅
  - 演讲时长 → 20min
  - 听众画像 → 设计师为主
  - 场合 → 阿里 D20 全球设计院长峰会（对外分享）
  - live demo → 暂不需要
  - 标题 → 从 Design 到 Build：Agent 时代体验设计的新边界
  - 日期 → 0711 演讲，0625 交初稿
  - QoderWork 身份 → 可以公开

- [x] **5 篇原文软链接** ✅（已联网拿到公开源）

  | # | 文章 | 软链接 | 备注 |
  |---|------|--------|------|
  | 1 | Claude Code 之父 Boris：「品味」不是人类护城河 | [知乎全文](https://zhuanlan.zhihu.com/p/2047009089100702659) | 中文整理稿 |
  | 1+ | 同上·Karpathy × Boris 对谈版（编程已死） | [36氪](https://m.36kr.com/p/3668658715829123) | 更长，金句更多 |
  | 2 | Claude 设计负责人 Jenny Wen：下一个 10 年 3 个能力 | [36氪](https://m.36kr.com/p/3705572553584769) | IDE 成新宠 |
  | 2+ | 同上·AI 会拥有审美吗 | [品玩](https://www.pingwest.com/a/311748) | 配套深度访谈 |
  | 3 | Anthropic 产品负责人 Cat Wu：面了上百个 PM | [搜狐](https://www.sohu.com/a/1018290724_122074763) | "品味越来越贵" |
  | 3+ | 同上·一个真正优秀的 AI 产品应该学会闭嘴 | [知乎](https://zhuanlan.zhihu.com/p/1920156813409629069) | Anthropic 产品哲学 |
  | 4 | AI in Design Report 2026 · 英文原版 | [stateofaidesign.com](https://stateofaidesign.com/) + [Designer Fund](https://designerfund.com/blog/ai-in-design-2026) | 周用 54%→91% |
  | 4+ | 同上·中文版（IXDC 联合出品） | [上篇](https://www.meia.me/article/1504?columnid=2620) · [下篇](https://ixdc.org/?p=28103) | 中文更适合演讲引用 |
  | 5 | 最恐怖的 AI 实验：没有法律的虚拟城镇 | [36氪全文](https://m.36kr.com/p/3841175573088513) | 《蝇王》× 西部世界 |

**下午（13:00-18:00）：三份调研并行**

- [ ] **调研 ①：QoderWork Agent 设计模式**
  - 研究 Agent 交互设计：怎么跟用户协作、怎么呈现状态、怎么处理反馈
  - 梳理 Agent 设计范式：自主程度、人机边界、错误恢复机制
  - 跟 Claude Code / Cursor / Codex 的 Agent 模式做横向对比
  - 📄 **产出**：`wiki/speech/qoderwork-agent-design.md`

- [ ] **调研 ②：Design Agent 生态**
  - 梳理市面上设计方向 Agent 产品：Galileo AI、Uizard、Figma AI、v0、Bolt 等
  - 每个产品：核心能力、交互模式、设计师角色变化、局限性
  - 📄 **产出**：`wiki/speech/design-agent-landscape.md`（含对比表）

- [ ] **调研 ③：Anthropic / Cursor / OpenAI 设计师工作模式**
  - 搜索三家公司设计师的公开分享（博客、播客、X/Twitter、会议演讲）
  - 特别关注 Ryo Lu (Cursor)、Ed Bayes (OpenAI)、Jenny Wen (Anthropic)
  - 📄 **产出**：整理成 sources.md 新增弹药条目

**晚间（19:00-21:00）：收尾**

- [ ] **review outline-v1.md**，根据确认的参数 + 今日调研发现，标注需要调整的地方
- [ ] 硬件概念图准备（AI 出图 / 找参考图，10 分钟搞定）

---

### Day 2 · 6月16日（周二）— 素材入库日

> 🔴 **今日必须完成：所有新素材入库 wiki + QoderWork 故事线定稿 + sources.md 更新**
> ⏰ 下班前 checklist：wiki 入库完成 ✓ / QoderWork 故事线 ✓ / sources.md 更新 ✓

**上午（9:00-12:00）：新素材批量入库**

- [ ] **新素材入库 wiki**（按 new-sources.md 的建议，逐篇入库）
  - Agentic Workflow → `AI实操与工具.md` + `AI Agent 开发.md`
  - 设计走查全自动 → `AI实操与工具.md` + `设计师成长.md`
  - OpenAI 大神榨干 Codex → `AI编程与Vibe Coding.md`
  - HTML版剪映 → `AI编程与Vibe Coding.md`
  - AI in Design Report 2026 → `AI设计工具.md`
  - 其他素材按建议入库
  - 📄 **产出**：new-sources.md 中所有素材入库完成

**下午（13:00-18:00）：QoderWork 素材整合**

- [ ] **QoderWork 素材整理 + 故事线定稿**
  - 把对谈文章（谢吉宝/唐三）核心观点提取到 `wiki/design/AI编程与Vibe Coding.md`
  - 把 Design Desk 抖音内容补充到 `wiki/design/抖音设计短视频.md`
  - 截 QoderWork 工作台/Design Desk 真实运行画面（你电脑上有）
  - 准备 1-2 段 Design Desk 录屏
  - 整理"5 人 7 天"故事线的具体时间节点
  - 将 Agent 设计模式分析融入演讲叙事
  - 📄 **产出**：`wiki/speech/qoderwork-case.md`

- [x] **QoderWork 公开信息盘点** ✅（已搜集）

  **官方入口：**
  - 官网（中国版）：https://qoder.com.cn/qoderwork
  - 产品总站：https://qoder.com/zh
  - 阿里云产品页：https://www.aliyun.com/product/lingma
  - 谢吉宝（唐三）2026 奇点智能技术大会演讲：**重塑桌面生产力，构建全场景驱动的桌面 Agent**

  **可引用的媒体报道：**
  - 知乎：[阿里 QoderWork 震撼上新](https://zhuanlan.zhihu.com/p/2040848366679156558) — "AI 办公从对话驱动走向领域驱动"
  - 品玩：[QoderWork 上线 AI Native 设计工作台](https://www.pingwest.com/w/313816) — 语音驱动"设计即代码"
  - IT 之家：[QoderWork 设计工作台](https://www.ithome.com/0/951/975.htm) — 语音描述就能交付专业设计
  - 品玩：[阿里发布 Qoder CLI](https://www.pingwest.com/w/308308) — 谢吉宝：未来开发界面是 IDE+CLI 组合

**晚间（19:00-21:00）：弹药库更新**

- [ ] **更新 sources.md**，补充所有新入库的观点弹药 + 调研发现

---

### Day 3 · 6月17日（周三）— 大纲定稿日

> 🔴 **今日必须完成：outline-final.md 定稿 + 4个个人案例素材可讲**
> ⏰ 下班前 checklist：outline-final.md ✓ / 4个案例叙事 ✓ / 截图录屏素材 ✓
> ⚠️ **今日是硬 deadline，大纲锁定后后续只改细节**

**上午（9:00-12:00）：大纲定稿**

- [ ] **大纲定稿 → `outline-final.md`**
  - 根据确认的参数精简/扩充（20min 约 15-18 页 PPT）
  - 确定每个论点的最终取舍
  - 确定金句清单的最终版本
  - 📄 **产出**：`wiki/speech/outline-final.md`（锁定版）

**下午（13:00-18:00）：个人案例整理**

- [ ] **4 个案例素材整理，每个案例必须有完整叙事**
  - 案例 ① QoderWork（核心案例）：5人7天、AI-native 协作、Design Desk
  - 案例 ② Agent Loop
  - 案例 ③ 前端开发
  - 案例 ④ 组件库 / DESIGN.md
  - 每个案例：背景 → 做了什么 → 为什么设计师适合做 → 效果/数据
  - 📄 **产出**：`wiki/speech/cases.md`

---

## 阶段 ② 内容设计（6/18 - 6/19）

> ⚠️ 内容设计压缩到 2 天，把时间让给 PPT 制作（PPT 要精美、动效足、干货足）

### Day 4 · 6月18日（周四）— 内容设计日

> 🔴 **今日必须完成：content-doc.md 产出（全部页面的内容方案）**
> ⏰ 下班前 checklist：逐页内容方案 ✓ / 视觉素材清单 ✓

**上午（9:00-12:00）：逐页内容设计（前半段）**

- [ ] **逐页内容设计：开场 + 第一部分 + 第二部分**
  - 每页 PPT 的标题、核心信息、视觉呈现方式
  - 标注哪些页需要动画/过渡效果
  - 规划金句页（全屏大字）

**下午（13:00-18:00）：逐页内容设计（后半段）+ 视觉素材**

- [ ] **逐页内容设计：第三部分 + 第四部分 + 收尾**
  - 优势矩阵表格页、工具链推荐页、三步走路径页、预言页
- [ ] **视觉素材收集**
  - 工具截图：Cursor、Claude Code、Codex 的工作界面
  - 流程图：传统流程 vs 新流程对比
  - 数据图：Figma 估值、DESIGN.md Star 数等
  - 个人案例截图/录屏
  - **硬件概念图**（1 页占位）

**晚间（19:00-21:00）：收尾**

- [ ] **输出 content-doc.md**
  - 📄 **产出**：`wiki/speech/content-doc.md`（全部页面的完整内容方案）

---

### Day 5 · 6月19日（周五）— 内容 Review + PPT 模板准备日

> 🔴 **今日必须完成：content-doc 终版确认 + PPT 视觉方向锁定**
> ⏰ 下班前 checklist：content-doc review ✓ / PPT 风格方向 ✓ / 模板骨架 ✓

**上午（9:00-12:00）：内容通盘 Review**

- [ ] **content-doc.md 通盘 review**
  - 检查叙事逻辑是否连贯、论据是否充分、时间分配是否合理
  - 📄 **产出**：content-doc.md 终版确认

**下午（13:00-18:00）：PPT 视觉方向锁定**

- [ ] **PPT 风格决策 + 模板搭建**
  - 确定模板/风格（深色？浅色？品牌色？）
  - 确定字体、配色、排版规范
  - 搭建所有页面骨架（标题 + 占位内容）
  - 📄 **产出**：`wiki/speech/ppt-design-spec.md` + PPT 模板文件

---

## 阶段 ③ PPT 制作（6/20 - 6/24）

> ⚠️ **5 天做 PPT，前 3 天逐段制作，后 2 天打磨动效 + 预演**
> 要求：设计精美、动效足够、干货十足。每天产出 6-8 页高质量页面。

### Day 6 · 6月20日（周六）— PPT 制作：开篇冲击力

> 🔴 **今日必须完成：封面 + 开场 + 第一部分（约 8 页）全部定稿**

- [ ] **封面**：视觉冲击力，一眼知道演讲主题
- [ ] **开场页（约 3 页）**：hook 观众——为什么今天要讲这个
- [ ] **第一部分（约 4-5 页）**：行业背景 + 核心论点引入
- 📄 **产出**：PPT 文件，前 8 页可交付状态

---

### Day 7 · 6月21日（周日）— PPT 制作：核心干货

> 🔴 **今日必须完成：第二部分（约 10-12 页）全部定稿**

- [ ] **设计工具变化**（2-3 页）
- [ ] **个人案例展示**（4 个案例，每个 1-2 页，共 6-8 页）
- [ ] **UX → AX → Ambient AX**（1-2 页）
- [ ] **设计系统变化**（1-2 页）
- 📄 **产出**：PPT 文件，前 20 页可交付状态

---

### Day 8 · 6月22日（周一）— PPT 制作：收尾段 + 金句页

> 🔴 **今日必须完成：第三部分 + 第四部分 + 收尾 + 金句/过渡页**

- [ ] **第三部分（约 4-5 页）**：优势矩阵、品味壁垒
- [ ] **第四部分（约 3-4 页）**：工具推荐、三步走路径
- [ ] **收尾（1-2 页）**：预言 + 结尾
- [ ] **金句页 + 过渡页**：全屏大字，视觉冲击
- 📄 **产出**：PPT 全部页面初版完成（约 15-18 页）

---

### Day 9 · 6月23日（周二）— PPT 精打磨：动效 + 视觉

> 🔴 **今日必须完成：所有页面动效上线 + 视觉质量达标**

- [ ] **动效打磨**：页面切换、关键内容出现动效、金句冲击力、数据动画
- [ ] **视觉质量检查**：截图高清、配色统一、字体层级清晰
- [ ] **文字精简**（PPT 不是文档，每页字要少要精）
- [ ] **演讲者备注**（每页的讲稿要点写好）
- 📄 **产出**：PPT 完整版（含动效 + 备注）

---

### Day 10 · 6月24日（周三）— 预演 + 最终打磨

> 🔴 **今日必须完成：内部预演通过 + PPT 终版锁定**

- [ ] **内部预演**：完整讲一遍，计时，记录每页耗时
- [ ] **根据预演反馈修复**：调整内容量、修复节奏问题
- [ ] **导出 PDF 备份**
- 📄 **产出**：PPT 终版 + PDF 备份

---

## 阶段 ④ 交付（6/25）

### Day 11 · 6月25日（周四）— 提交日

> 🔴 **今日必须完成：PPT 初稿提交**

- [ ] **最终检查**：文件格式、分辨率、不同设备预览、无错别字
- [ ] **提交 PPT 初稿** ✅

---

## 阶段 ⑤ 硬件占位（已降级 · 1 页 PPT）

> ❌ **不再做实物原型**。原方案 A/B/C/D 全部废弃。

**新方案：PPT 里加 1 页"软件 → 硬件延伸"概念页。**

- [ ] **准备一张概念图**（任选其一，10 分钟内完成）
  - AI 出图：MJ / FLUX / Recraft 出"桌面 Agent 设备"概念渲染图
  - 找现成参考图：Clawdmeter、qpaperOS、M5Stack StackChan

- [ ] **页面文案（建议）**
  - 主标：从屏幕到桌面 — Agent 的下一个边界
  - 副标：UX → AX → **Ambient AX**
  - 一句话："当 Agent 走出屏幕，谁来设计它和物理世界的交互？还是设计师。"

> 这一页放在第二部分"案例 4"位置，30 秒一带而过的概念延伸。

---

## 关键决策点

| # | 决策 | 状态 | 确认时间 |
|---|------|------|----------|
| 1 | 演讲时长 | 20min ✅ | 已确认 |
| 2 | 听众画像 | 设计师为主（D20 院长峰会）✅ | 已确认 |
| 3 | 是否需要 live demo | 不需要 ✅ | 已确认 |
| 4 | 是否用中文还是英文 | 中文 ✅ | 已确认 |
| 5 | 能否以 QoderWork 身份公开演讲 | 可以 ✅ | 已确认 |
| 6 | PPT 风格/模板 | 待定 | Day 5 前 |

---

## 风险 & 应对

| 风险 | 应对 |
|------|------|
| 5 篇原文抓取失败 | 已联网拿到公开软链接，备选用标题+摘要 |
| QoderWork 数据/截图涉密 | 用脱敏数据 + 公开报道里的口径 |
| **PPT 制作时间不够** | **已调整：内容设计压缩到 2 天，PPT 制作扩展到 5 天** |
| **PPT 动效/视觉不够精美** | **Day 9 留整天打磨动效；Day 10 预演后还有修复时间** |
| 大纲迟迟定不了 | Day 3 强制锁定，后续只改细节 |
| 硬件概念图找不到合适的 | AI 出图兜底，10 分钟解决 |

---

## 文件索引

| 文件 | 路径 | 产出日 | 状态 |
|------|------|--------|------|
| 演讲大纲 v1 | [`wiki/speech/outline-v1.md`](outline-v1.md) | 已有 | ✅ 待打磨 |
| 演讲大纲 v2 | [`wiki/speech/outline-v2.md`](outline-v2.md) | 已有 | ✅ 新增 |
| 弹药库 | [`wiki/speech/sources.md`](sources.md) | 已有 | ✅ 50 条 |
| 新素材分析 | [`wiki/speech/new-sources.md`](new-sources.md) | 已有 | ✅ 30 篇 |
| 灵感碎片 | [`wiki/speech/idea-fragments.md`](idea-fragments.md) | 已有 | ✅ 新增 |
| 本计划 | [`wiki/speech/plan.md`](plan.md) | 已有 | ✅ 本文件 |
| QoderWork Agent 设计模式 | `wiki/speech/qoderwork-agent-design.md` | Day 1 | ⏳ |
| Design Agent 生态对比 | `wiki/speech/design-agent-landscape.md` | Day 1 | ⏳ |
| QoderWork 案例素材 | `wiki/speech/qoderwork-case.md` | Day 2 | ⏳ |
| 定稿大纲 | `wiki/speech/outline-final.md` | Day 3 | ⏳ |
| 个人案例文档 | `wiki/speech/cases.md` | Day 3 | ⏳ |
| 内容文档 | `wiki/speech/content-doc.md` | Day 4 | ⏳ |
| PPT 设计规范 | `wiki/speech/ppt-design-spec.md` | Day 5 | ⏳ |
| PPT 初稿 | 待定 | Day 10 | ⏳ |

---
*计划随进展更新 · 最后更新：2026-06-15*
