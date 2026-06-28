---
type: guide
description: "完整流水线：从 YouTube 链接到 Wiki 知识库的端到端流程。"
timestamp: 2026-06-20
---
# YouTube 视频文字稿入库流程

> 完整流水线：从 YouTube 链接到 Wiki 知识库的端到端流程。
> 适用于后续所有 YouTube 视频文字稿入库时复用。
> 配套：[抖音视频入库流程](抖音视频入库流程.md)

---

## 流程总览

```
YouTube 链接 → 抓元数据 → 抓英文字幕 → 段级合并 → 写入 raw/来自Youtube/ → 信达雅中文翻译 → 软链到 wiki/speech/yt-talks/ → 收录金句到 sources.md
```

## 1. 数据采集

### 抓取元数据

```bash
yt-dlp --dump-json "https://www.youtube.com/watch?v=VIDEO_ID"
```

提取字段：

| 字段 | 用途 |
|------|------|
| `title` | 文档标题 |
| `channel` / `uploader` | 演讲者/频道 |
| `uploader_id` | 频道 handle |
| `duration` | 时长（秒） |
| `upload_date` (YYYYMMDD) | 发布日期 |
| `view_count` / `like_count` | 统计 |
| `description` | 简介（前 1500 字） |
| `tags` | 标签 |

### 抓取英文字幕

**优先方案：`youtube-transcript-api`**

```python
from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
data = api.fetch('VIDEO_ID', languages=['en'])
segs = [{'text': s.text, 'start': s.start, 'duration': s.duration} for s in data]
```

**优势**：
- 段级已切分（每段是 YouTube 后端识别的一整句）
- 无 VTT 滚动字幕的重复问题
- 547 段 → 合并后约 100-150 段

**降级方案：`yt-dlp` 拉 VTT**

```bash
yt-dlp --write-auto-sub --sub-lang "en,en-orig" --convert-subs vtt \
       --skip-download -o "/tmp/VIDEO_ID" "URL"
```

VTT 需自行解析 word-level cue（`<ts><c>word</c>` 内联时间戳），用增量算法去重。

**注意事项**：
- `youtube-transcript-api` 直接 fetch 中文 → 失败（仅 en 翻译存在）
- `en.translate('zh-Hant').fetch()` → 易被 IP 限流（HTTP 429）
- 第三方服务（downsub、youtubetotranscript）→ 被 Cloudflare 拦截

**中文获取兜底（按推荐顺序）**：

1. **浏览器复制**：YouTube 网页 → 设置 → 字幕 → 中文(简体) → 复制粘贴
2. **yt-dlp + cookies**：
   ```bash
   yt-dlp --cookies-from-browser chrome --write-auto-sub --sub-lang "zh-Hans" \
          --convert-subs vtt --skip-download "URL"
   ```
3. **本地 LLM 翻译**：把英文段喂给 Ollama qwen2.5 翻译（推荐本地大模型，质量可控）

## 2. 段级合并

`youtube-transcript-api` 返回的 segments 每 3-4 秒一段（一句话被切 2-3 次）。需合并：

```python
def merge_segments(segs, gap_threshold=0.4):
    merged = []
    for s in segs:
        text = s['text'].strip()
        if not text or text in ('[music]', '[applause]'):
            continue
        if (merged and (s['start'] - merged[-1]['end']) < gap_threshold
            and not merged[-1]['text'].rstrip().endswith(('.', '?', '!'))):
            merged[-1]['end'] = s['start'] + s['duration']
            merged[-1]['text'] = (merged[-1]['text'] + ' ' + text).strip()
        else:
            merged.append({
                'start': s['start'],
                'end': s['start'] + s['duration'],
                'text': text,
                'is_sfx': False
            })
    return merged
```

**效果**：547 段 → 约 120 段（典型 18 分钟演讲）

清理：
- 移除行首 `>> `（VTT 标记）
- `[music]` / `[applause]` 标记为 `is_sfx` 单独保留

### 段间重叠检测（2026-06-20 新发现）

YouTube 现代 auto 字幕特性：每段约 2-4s 短句，**段间有 1-2s 重叠**（音频边界检测副作用）。

**判断方法**：

```python
# 合并后检查段间隔
gaps = [merged[i]['start'] - merged[i-1]['end'] for i in range(1, len(merged))]
negative_gaps = sum(1 for g in gaps if g < 0)
if negative_gaps > len(gaps) * 0.3:
    print("段间重叠，改用 0.2s 宽松阈值")
```

**两种合并策略**：
- **严格模式**（默认）：`gap=0.4s`，适合人工字幕
- **宽松模式**：`gap=0.2s`，适合 auto 字幕（避免错误合并）

**案例对比**（GOtHFZnagO0, 16:43 视频）：
- 严格模式 → 34 段（句意断裂）
- 宽松模式 → 34 段（同样 34，但段间不重叠）

**注意**：如果合并后段数 < 原始段数 × 20%，说明源数据已按静音/句子切分好，**不要硬合并**——直接保留原段（34 段对 16 分钟视频，约 30s/段，已是合理阅读粒度）。

## 3. 写入 raw/来自Youtube/

**目标文件**：`raw/来自Youtube/{video_id}_{slug-title}_{speaker}.md`

**slug 化标题**：移除引号、特殊字符、空格换 `-`

**Markdown 结构**：

```markdown
# "{原标题}" — {演讲者}

> **频道**：{channel} ({uploader_id})
> **链接**：[{url}]
> **时长**：{H} 分 {M} 秒
> **发布日期**：{YYYY-MM-DD}
> **观看/点赞**：{N:,} / {M:,}
> **字幕抓取日期**：{YYYY-MM-DD}
> **字幕来源**：YouTube auto-generated (en)
> **段落数**：{N} | **总字数**：约 {N} 词 / {N} 字符

---

## 简介
{description}

**标签**：`t1`, `t2`, ...

---

## 完整文字稿

> 段落格式：`[时:分:秒] 文字内容`

*[00:00:07.205] [music]*
**[00:00:14.640]** {text}

---

## 关键节点索引

| 时戳 | 内容摘要 |
|------|----------|
| `00:00:14.640` | {首句 80 字} |

---

## 信达雅中文翻译

> **演讲者**：{speaker}
> **原始语言**：英文 · **翻译**：Claude（手工译校）
> **风格**：信、达、雅。技术名词保留英文原貌
> 已修复 ASR 误识别（Clojure Code → Claude Code、John Osterhout → John Ousterhout 等）
> 本节为人类易读版本，移除时间戳，按演讲逻辑分章整理

### 一、开场：{章节名}
{段级译文，按演讲节奏合并}

### 二、{失败模式 N：描述}
...

### 七、收束：{核心金句}
...
```

## 4. 信达雅中文翻译

### 翻译规范

| 规则 | 例子 |
|------|------|
| 技术名词保留英文 | TDD, DDD, vibe coding, ubiquitous language, plan mode |
| ASR 误识别必须修正 | "Clojure Code" → "Claude Code" |
| 形象化短语意译 | outrunning your headlights → "跑出车灯照亮的范围" |
| 演讲体保留 | "嗯""对吧""懂吧""好,谢谢" |
| 短反应句合并 | "Cool. Okay." → 上下文自然衔接 |
| 音效标记 | [music] → 「音乐」, [applause] → 「掌声」 |

### ASR 误识别清单（演讲常见）

| 误识别 | 修正 | 出处 |
|--------|------|------|
| Clojure Code | Claude Code | Anthropic 产品 |
| John Osterhout | John Ousterhout | 《A Philosophy of Software Design》作者 |
| John Ousterhout | John Ousterhout | 同上 |
| AFK agent | AI agent | 通用术语 |
| macpocockskills | mattpocock/skills | GitHub 仓库 |

### 章节切分

按演讲逻辑硬切为 5-10 个章节。常见模式：

1. **开场**：钩子 + 核心论点
2. **失败模式 N**：（按演讲中提到的 1, 2, 3, 6 等）
3. **建议/技能**：每条独立章节
4. **收束**：核心金句 + 行动号召

每个章节的命名格式：`{N}、{标题}：{核心观点}（建议：{对应方案}）`

## 5. Wiki 软链入口

**目标位置**：`wiki/speech/yt-talks/{filename}.md`

```bash
mkdir -p wiki/speech/yt-talks
ln -sf "/abs/path/to/raw/来自Youtube/{filename}.md" \
       "wiki/speech/yt-talks/{filename}.md"
```

**创建模块级 CLAUDE.md**：`wiki/speech/yt-talks/CLAUDE.md`

```markdown
# yt-talks/CLAUDE.md

> L2 模块文档 — YouTube 演讲文字稿的 wiki 入口
> 所有文件为软链 → raw/来自Youtube/ 下原文

## 文件清单
| 文件 | 演讲者 | 主题 | 软链目标 |
|------|--------|------|----------|
| [{name}.md] | {speaker} | {topic} | `raw/来自Youtube/...` |

## 软链约定
- 绝对路径，便于跨目录访问
- 写操作统一改 raw 源文件，wiki 端自动同步
- 新增文件时同步更新本 CLAUDE.md
```

## 6. 收录金句到 sources.md

**目标位置**：`wiki/speech/sources.md`（D20 演讲弹药库）

**金句选取标准**：
- 强反直觉观点
- 可在演讲中作为钩子
- 与 D20 主题（设计 × AI）相关
- 一句完整，可独立引用

**格式**：

```markdown
{N+1}. **"{金句原文}"**
    — {演讲者}，{频道/场合}（[yt-talks/{filename}]）
    → 用法：{在 D20 演讲哪个段落使用，传递什么效果}
```

## 7. 错误处理速查

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| yt-dlp "n challenge solving failed" | JS challenge 失败 | 装 `yt-dlp-ejs` + bun runtime + 用最新 yt-dlp binary |
| timedtext API 返回 0 字节 | 签名过期或 IP 限流 | 等待 30 分钟重试，或换 cookie |
| 第三方服务被 Cloudflare 拦截 | 普遍情况 | 改用 API 直连 |
| API 返回 "No transcripts found" | 语言不可用 | 查 available languages，en 翻译列表 |
| "IpBlocked" from youtube-transcript-api | 短时间请求过多 | 等待 60+ 秒后单次重试 |
| "TranslationLanguageNotAvailable" | 不支持的目标语言 | 改用其他语言或本地 LLM 翻译 |
| **`TranscriptsDisabled` + `automatic_captions: []`** | 作者禁用字幕+无 auto | 走 **STT 兜底路线**（见下） |

## 8. STT 兜底路线（2026-06-20 实战验证）

**适用场景**：作者禁用 YouTube 官方字幕+无 auto-generated 字幕。

**前置依赖**：
```bash
# 装 ejs 解决 yt-dlp 的 SABR 验证
pip3 install yt-dlp-ejs
# 装 bun runtime（macOS 通常已有 ~/.bun/bin/bun，1.2.11-1.3.14 兼容）
# 装 groq SDK
pip3 install groq
# 需要 Groq API key（免费 1 小时/天 whisper-large-v3-turbo）
export GROQ_API_KEY="gsk_..."
```

**步骤**：

```bash
# 1. 拉最新 yt-dlp binary（pip 装的是 stable 2025.12.8，不支持新 player JS）
curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /tmp/yt-dlp-nightly
chmod +x /tmp/yt-dlp-nightly

# 2. 抓最低码率音频（itag 91，49kbps AAC，14MB/28min）
/tmp/yt-dlp-nightly --js-runtimes "bun:$HOME/.bun/bin/bun" \
  --cookies /tmp/yt-cookies.txt -f "91" \
  -o "/tmp/VIDEO_ID.mp4" "URL"

# 3. Groq Whisper API 转写
python3 -c "
import os, json
from groq import Groq
client = Groq(api_key=os.environ['GROQ_API_KEY'])
with open('/tmp/VIDEO_ID.mp4', 'rb') as f:
    t = client.audio.transcriptions.create(
        file=('video.mp4', f.read()),
        model='whisper-large-v3-turbo',
        language='en',
        response_format='verbose_json',
        timestamp_granularities=['segment']
    )
segs = [{'start': round(s['start'],2), 'end': round(s['end'],2), 'text': s['text'].strip()}
        for s in t.segments]
with open('/tmp/VIDEO_ID.groq.json','w') as f:
    json.dump(segs, f, ensure_ascii=False, indent=2)
"
```

**耗时**：28 分钟视频 → 抓音频 30s + STT 12s = **总 < 1 分钟**。

**案例**：[Uvl-tRga98g_Designing-with-Claude-from-Prompt-to-Production.md] — Dan Carey @ Anthropic 官方产品介绍。

## 脚本清单

| 脚本 | 用途 |
|------|------|
| `yt-dlp --dump-json URL` | 抓元数据 |
| `python3 -c "from youtube_transcript_api import..."` | 抓分段字幕 |
| 合并函数 `merge_segments()` | 段级合并 |
| 章节切分（按演讲节奏） | 人工或启发式 |
| `ln -sf` | 建立软链 |
| Edit sources.md | 追加金句 |

## 注意事项

1. **字幕语言优先级**：en auto-generated > en-orig（原始英文）> 翻译列表
2. **段级合并阈值**：0.4s 间隔，保留以 `. ? !` 结尾的短句独立
3. **时间戳格式**：统一用 `HH:MM:SS.mmm`（6 位毫秒）
4. **文件名安全化**：slug 标题只用 `-`、字母、数字；中文标题可在 slug 中保留 Pinyin 或纯 ASCII
5. **软链用绝对路径**：避免目录切换导致链接断开
6. **金句选取 3-5 条**：太多则稀释弹药库密度
7. **中文翻译章节数**：5-10 章为佳（太少显粗陋，太多读者迷失）
8. **ASR 修正必须**：原视频若有误识别，译者必须修——这是"信"的基本要求

## 新 YouTube 链接入库 Checklist

- [ ] 抓元数据：title / channel / duration / upload_date / view+like
- [ ] 抓英文字幕（youtube-transcript-api，en）
- [ ] 段级合并：547 → ~120 段
- [ ] 写入 `raw/来自Youtube/{video_id}_{slug}_{speaker}.md`
- [ ] 包含元信息、简介、英文带时间戳文字稿、关键节点索引
- [ ] 信达雅中文翻译：修复 ASR、技术名词保留英文、按章节切分
- [ ] 软链到 `wiki/speech/yt-talks/`
- [ ] 创建/更新 `wiki/speech/yt-talks/CLAUDE.md` 文件清单
- [ ] 收录 3-5 条金句到 `wiki/speech/sources.md`
- [ ] 验证软链可访问、wikilink 跳转正常

---

## 参考案例

- [v4F1gFy-hqg_Software-Fundamentals-Matter-More-Than-Ever_Matt-Pocock.md](../speech/yt-talks/软件基础比以往更重要_Software-Fundamentals-Matter-More-Than-Ever-Matt-Pocock_v4F1gFy-hqg.md) — Matt Pocock 在 AI Engineer 大会的演讲（18:26，2026-04-23，896K 播放）
- [ttkd0t5qTD4_Yao-Shunyu-Training-Models-at-Anthropic-Gemini.md](../speech/yt-talks/姚顺宇在Anthropic和Gemini训练模型_Yao-Shunyu-Training-Models-at-Anthropic-Gemini_ttkd0t5qTD4.md) — 姚顺宇访谈（3:48:01，2026-05-11，161K 播放）— 罕见地同时有 zh-Hans + en-GB 人工字幕，无需翻译
- [GOtHFZnagO0_How-to-Use-Codex-as-a-Designer.md](../speech/yt-talks/设计师如何使用Codex_How-to-Use-Codex-as-a-Designer_GOtHFZnagO0.md) — Griffin Wooldridge 实操指南（16:43，2026-06-08，34K 播放）— 段间重叠案例

可作为后续 YouTube 视频的参考模板。
