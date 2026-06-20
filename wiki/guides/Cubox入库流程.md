---
type: guide
description: "Cubox 收藏的文章/小红书/公众号批量入库到 LLM Wiki"
timestamp: 2026-06-20
---
# Cubox 入库流程

> 完整流水线：从 Cubox 收藏到 LLM Wiki 知识库
> 适用：Cubox 收藏的微信公众号、小红书、网页文章批量入库
> 现状（2026-06-20）：`raw/文章汇总/` 已有 2024-08 月文章；`cubox-cli` 未安装，需手动处理

---

## 流程总览

```
Cubox 收藏 → 导出/抓取 → raw/文章汇总/ → 主题分类 → wiki/<主题>/ 索引 → 反向链接
```

## 1. 数据采集（两条路线）

### 路线 A：cubox-cli（推荐，自动化）

**前置**：
```bash
# 安装 cubox-cli（Go 工具，OLCUBO 维护）
go install github.com/OLCUBO/cubox-cli@latest
# 配置 API key（从 https://cubox.pro/settings/api 获取）
export CUBOX_API_KEY="..."
```

**完整脚本**：`/Users/cunyu666/Design/01_设计项目/skills/skills/oh-my-mind/scripts/cubox-to-wiki.py`

```bash
# 同步过去 1 天到 daily 主题
python3 cubox-to-wiki.py daily 1
# 同步星标文章
python3 cubox-to-wiki.py --starred
# 自定义主题 + 天数
python3 cubox-to-wiki.py 设计方法论 7
```

**输出目录**：`topics/<主题>/raw/articles/cubox-<id>-<safe-title>.md`

**已知问题**：
- `cubox-cli` Go 包名变更（`OLCUBO/cubox-cli` 仓库可能迁移）
- API key 需要 Cubox Pro 订阅

### 路线 B：手动导出（兜底）

1. 浏览器打开 https://cubox.pro
2. 收藏列表 → 选中 → 导出 Markdown
3. 或单篇 → 复制 Markdown → 粘贴到 `raw/文章汇总/<日期>-<标题>.md`

## 2. 历史文章模式（2024-08 实战）

`raw/文章汇总/` 已有 100+ 篇 2024-08 月文章，格式：

```markdown
---
id: "7227971752813398370"
cubox_url: 
url: <原 URL（公众号/小红书/网页）>
author: "<作者>"
collected: 2024-08-27
tags: [哲学, ...]
---

# <标题>

# <标题>（重复标题，原始 Cubox 导出的瑕疵）

[<原 URL>](url) <作者>

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=...)  ← Cubox 代理的图片 URL

## 抓取说明
...
```

**目录命名**：`YYYY-MM-DD-<标题>.md`（按收藏日期）

**常见来源**：
- 微信公众号（`mp.weixin.qq.com`）
- 小红书（`xiaohongshu.com`）
- 网页文章（`media.*.com`）

## 3. 文件名清洗

参考 [小红书入库流程.md §11](小红书入库流程.md)：

| 原标题 | 清洗后 |
|--------|--------|
| `黄铮：大部分知识是没用的，遇到问题再解决` | `2024-08-27-黄铮大部分知识是没用的遇到问题再解决.md` |
| `通达未来，智领革新  \|  2024通义品牌视觉系统升级` | `2024-08-29-通达未来智领革新-2024通义品牌视觉系统升级.md` |

**清洗函数**（同小红书）：
```python
import re
def clean_title(s):
    s = re.sub(r'[，。：；？、（）！""《》｜—…·,.;:?!()\[\]"\'/\\*?<>|&$#@!+]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s
```

## 4. 主题分类（建立索引）

**当前 wiki 主题映射**：

| 文章类型 | wiki 目标 |
|----------|-----------|
| 设计方法论/设计思维 | `wiki/design/设计方法论.md` |
| AI 编程/Agent | `wiki/design/AI编程与Vibe Coding.md` |
| AI 设计工具 | `wiki/design/AI设计工具.md` |
| 设计系统/品牌 | `wiki/design/设计系统.md` |
| UX/交互 | `wiki/design/UX与交互研究.md` |
| 设计师成长 | `wiki/design/设计师成长.md` |
| 大模型/LLM | `wiki/design/LLM与大模型.md` |
| AI 实操 | `wiki/design/AI实操与工具.md` |
| 通用（无法分类）| `wiki/Agent/资料/` 或 `wiki/Uncategorized/` |

**分类标准**：
- 看标题关键词 + tags
- 看内容第一段（前 200 字）
- 看 url 来源（公众号/小红书/网页）

## 5. 索引页格式

每个主题下建立 `Cubox归档.md` 索引（参考 `wiki/speech/yt-talks/CLAUDE.md` 模式）：

```markdown
# Cubox 归档：<主题>

> Cubox 收藏中与<主题>相关的文章
> 最后更新：2026-06-20

## 文章列表

| 日期 | 标题 | 作者 | tags | 软链 |
|------|------|------|------|------|
| 2024-08-27 | 黄铮：大部分知识是没用的 | 悟道图书馆 | 哲学 | [[../../raw/文章汇总/...]] |
| 2024-08-29 | 2024通义品牌视觉系统升级 | 阿里云设计中心 | 品牌 | [[../../raw/文章汇总/...]] |
```

## 6. 反向链接到主题

在主题 wiki 页面的 `## See Also` 区追加：

```markdown
## See Also

- [[Cubox归档_设计方法论]] — Cubox 收藏中与设计方法论相关的文章
- [[Cubox归档_AI编程与Vibe Coding]] — AI 编程相关
```

## 7. 与 Obsidian cubox-sync 插件协同

`/Users/cunyu666/Design/03_材料/LLM-Wiki/.obsidian/plugins/cubox-sync/` 已装。

**配置位置**：
- `data.json` - 包含 `domain/apiKey/folderFilter/typeFilter/statusFilter`
- 可在 Obsidian 设置 → Cubox Sync 配置

**两种工作流**：

| 路线 | 优点 | 缺点 |
|------|------|------|
| Obsidian 插件 | 实时同步，UI 友好 | 需 Cubox Pro；插件维护活跃度未知 |
| cubox-cli + 脚本 | 自动化，CI/CD 友好 | 需 Go 环境；脚本需自己维护 |

**推荐**：平时用 Obsidian 插件（实时），批量迁移用 cubox-cli。

## 8. 实战经验 & 已知坑

### 重复标题

Cubox 原始导出有"# 标题"+"# 标题"重复，**入库时删一个**。

```python
# 删重复标题
import re
text = re.sub(r'^(# .+)\n+\1', r'\1', content, flags=re.MULTILINE)
```

### 图片 URL 代理

`https://cubox.pro/c/filters:no_upscale()?imageUrl=...` 是 Cubox 代理 CDN，**直接引用会失效**（Cubox 关闭代理后图片全挂）。

**修复**：
- 解析出原始 URL（`imageUrl` 参数）
- 重新下载到 `raw/文章汇总/imgs/<id>/N.jpg`
- markdown 替换为本地路径

### URL 参数冗长

微信文章 url 包含 `__biz/mid/idx/sn/chksm/mpshare/scene/srcid/sharer_shareinfo...` 一大堆参数，**保留完整 url**（其他参数可能含分享追踪）。

### 跨平台作者

微信公众号没有作者字段，`author` 经常是空。**从内容里抓"作者：xxx"或署名**。

## 9. 注意事项

1. **采集速度**：避免一次性拉太多（Cubox API 有限流）
2. **去重**：Cubox 同一篇文章可能在多个收藏夹，按 ID 去重
3. **分类粗略**：宁可多归到宽泛主题也不要漏掉
4. **保留原文**：不要修改正文，只补充分类标签
5. **软链 vs 复制**：推荐软链（raw 是唯一源，wiki 端只做索引）

## 10. Checklist（新文章复用）

- [ ] 文章已存到 `raw/文章汇总/<日期>-<标题>.md`
- [ ] frontmatter 完整（id/author/url/collected/tags）
- [ ] 删除重复标题
- [ ] 解析图片 URL 到本地（`imgs/<id>/N.jpg`）
- [ ] 主题分类确定
- [ ] 在主题 `wiki/design/<主题>.md` See Also 加引用
- [ ] 建立/更新 `Cubox归档_<主题>.md` 索引
- [ ] `wiki/log.md` 头部加 ingest 记录
- [ ] Obsidian 中验证：链接可跳转、图片可显示

## 与其他 SOP 的关系

- **文件清洗规范**：[小红书入库流程.md §11](小红书入库流程.md)
- **音频转写**：[音频转写通用流程.md](音频转写通用流程.md) — 视频/播客走音频转写
- **微博/Twitter**：[x-bookmarks-export.md](x-bookmarks-export.md)
- **YouTube**：[YouTube视频入库流程.md](YouTube视频入库流程.md)

## 参考案例

- `raw/文章汇总/2024-08-27-黄铮大部分知识是没用的遇到问题再解决.md`
- `raw/文章汇总/2024-08-29-通达未来智领革新-2024通义品牌视觉系统升级.md`
- `/Users/cunyu666/Design/01_设计项目/skills/skills/oh-my-mind/scripts/cubox-to-wiki.py` (现成脚本)
