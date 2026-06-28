# OKF 兼容性报告

> Google Cloud · Open Knowledge Format v0.1 · 2026-06-12
> 报告日期：2026-06-20 · v1.0

---

## TL;DR

本 Wiki **已 100% 拥有 frontmatter**，但有**两套字段规范共存**（旧 `summary/tags/created/updated` vs OKF `description/tags/timestamp`）。OKF 兼容性 = **3 步可达成**：① 字段映射（`summary` ↔ `description`），② `timestamp` 替换 `created/updated` 双字段，③ 增加 `type` 枚举（已自动完成）。

---

## OKF v0.1 规范字段（Google Cloud · 2026-06-12）

OKF 定义了 6 个核心 YAML frontmatter 字段：

| 字段 | 含义 | 是否必填 |
|---|---|---|
| `type` | 文档类型（vendor-neutral enum） | 推荐 |
| `title` | 文档标题 | 必填 |
| `description` | 文档摘要（agent 消费） | 推荐 |
| `resource` | 资源链接/来源 URL | 可选 |
| `tags` | 标签数组 | 推荐 |
| `timestamp` | 时间戳 | 推荐 |

OKF 哲学三原则：**vendor-neutral / agent-friendly / human-friendly / portable / interoperable**。

---

## 本 Wiki 当前状态（2026-06-20 扫描）

### 覆盖度

```
总文件: 100
有 frontmatter: 100 / 100 (100%)
有 type 字段: 100 / 100 (100%)
```

### 双规范并存

| 规范 | 文件数 | 字段示例 |
|---|---|---|
| **旧规范** | 51 | `title / summary / tags / created / updated / type` |
| **OKF 新规范** | 49 | `type / description / timestamp` |

### type 字段分布

```
  15  index              ← 主索引页
  11  note               ← 笔记/转载
   6  guide              ← 流程指南
   6  speech-meta        ← 演讲元数据
   5  agent-prompt       ← Agent 系统提示词
   3  speech             ← 演讲素材
   2  log                ← 日志
   1  scan-progress      ← 扫描进度
```

---

## 字段映射方案（OKF 对齐）

### 一步映射（语义相同）

| 旧字段 | OKF 字段 | 动作 |
|---|---|---|
| `title` | `title` | 保留不动 |
| `tags` | `tags` | 保留不动 |

### 合并映射

| 旧字段 | OKF 字段 | 动作 |
|---|---|---|
| `summary` | `description` | 重命名 |
| `created` + `updated` | `timestamp` | 用 `updated` 为主，`created` 移到 metadata |

### 新增字段

| 字段 | 动作 |
|---|---|
| `type` | **已全部补齐**（2026-06-20 批量脚本完成） |
| `resource` | 可选，多数文件不需要 |
| `timestamp` | 旧文件用 `updated` 值填充 |

---

## 实施步骤（30 分钟内可完成）

### Step 1: 批量字段映射脚本（推荐）

```python
import re
from pathlib import Path

WIKI = Path('/Users/cunyu666/Design/03_材料/LLM-Wiki/wiki')

for p in sorted(WIKI.rglob('*.md')):
    text = p.read_text()
    if not text.startswith('---\n'): continue
    
    # 只处理旧规范（有 summary 字段的）
    if 'summary:' not in text: continue
    
    # summary → description
    text = re.sub(r'^summary:\s*(.*?)$', r'description: \1', text, flags=re.M)
    
    # created/updated → timestamp (用 updated)
    m_updated = re.search(r'^updated:\s*(\S+)', text, re.M)
    if m_updated:
        text = text + f'\ntimestamp: {m_updated.group(1)}'
    
    p.write_text(text)
    print(f"✓ {p.name}")
```

### Step 2: 验证（grep 检查）

```bash
# 确认没有 summary 字段残留
grep -r '^summary:' wiki/ --include='*.md' | wc -l
# 期望: 0

# 确认 description 已普及
grep -r '^description:' wiki/ --include='*.md' | wc -l
# 期望: ≥ 100
```

### Step 3: 在 raw/ 下同步（小红书笔记已有 OKF 字段）

raw/ 小红书笔记的 frontmatter 已经是 OKF 兼容（`source / author_id / url / tags / captured`），可作为模板反向同步到 raw/ 其它平台。

---

## 当前可被 agent 消费的程度

| 维度 | 评估 |
|---|---|
| **结构化字段** | ✅ 100% 文件有 frontmatter |
| **类型可识别** | ✅ 100% 文件有 type 字段 |
| **摘要可读** | ⚠️ 51/100 用 `summary`，49/100 用 `description`（合并后即 100%） |
| **时间可索引** | ⚠️ 51/100 用 `created/updated`，49/100 用 `timestamp`（合并后即 100%） |
| **可移植性** | ✅ 纯 Markdown，无锁 |
| **Wikilink 互操作** | ⚠️ `[...]` 格式外部工具不识别（Obsidian 专属） |

---

## OKF 与 GEB 协议的关系

| 维度 | OKF | GEB |
|---|---|---|
| 作用域 | 跨项目 / 跨厂商 | 项目内 / 文件级 |
| 抽象层级 | 数据格式 | 文档组织 + 工作流 |
| 主要受众 | 任意 AI Agent | 项目内 Claude / Codex / Catui |
| 互操作粒度 | 文件 | 文件 + 章节 + 模块 |

**两者完全正交、互补**：
- OKF 解决"**agent 怎么找到并消费**"本 wiki 的知识
- GEB 解决"**人类 + 项目内 AI 怎么组织**"本 wiki 的知识

---

## Wikilink 兼容性策略

OKF 要求 portable，但 Obsidian `[...]` 格式外部工具不识别。**两种方案**：

### 方案 A：保留 wikilink + 自动生成 markdown 链接备份

适合 wiki/ 内部链接。写一个 `tools/wikilink_to_md.py`：
- 读所有 wiki/*.md
- 把 `[[xxx|yyy]]` 转成 `[yyy]`
- 输出 `wiki_md/` 镜像目录供 agent 消费

### 方案 B：用 markdown 链接写 wiki（放弃 Obsidian 体验）

不推荐：丢失了 Obsidian 的图谱、反向链接、Daily Notes 等核心能力。

**推荐 A**——wikilink 给人类，markdown 镜像给 agent。

---

## 行动清单（按优先级）

### P0（已完成）

- [x] 100/100 wiki 文件补 frontmatter
- [x] 100/100 wiki 文件补 type 字段
- [x] OKF 兼容性报告落地（本文）

### P1（30 分钟）

- [ ] 批量 `summary` → `description` 重命名（51 个文件）
- [ ] 批量 `created/updated` → `timestamp` 合并（51 个文件）
- [ ] grep 验证 0 个 `summary` 残留

### P2（长期）

- [ ] raw/ 各平台 frontmatter 对齐 OKF（已有小红书作模板）
- [ ] 写 `tools/wikilink_to_md.py` 生成 markdown 镜像
- [ ] 在 Obsidian 之外（如 VS Code + Claude Code）验证 agent 可消费
- [ ] 把 OKF 规范纳入 GEB 协议 v2.0

---

## 关联文件

- [[OKF 与本 Wiki 对照分析]] — 概念层对照
- [小红书入库流程] — OKF 实战样本（raw/小红书/*.md 已用 OKF 字段）
- [0620 计划与进展] — 演讲素材
- [[AI Agent 开发]] — Multi-Agent 协作与 context 标准
- [Claude Code 系统提示词] — Agent 消费本 wiki 的实际案例

---

*报告日期：2026-06-20 · 标签 `#OKF` `#兼容性` `#frontmatter` `#LLM-wiki`*
*下次扫描建议：P1 步骤完成后立即重跑，验证 OKF 100% 兼容*