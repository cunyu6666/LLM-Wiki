---
type: guide
description: "从 Twitter/X 抓视频/音频、转写为 .txt 入库到 x-transcripts；x-audio 是 Twitter Spaces 音频"
timestamp: 2026-06-20
---
# x-transcripts / x-audio 转写流程

> 完整流水线：从 tweet 嵌入的 YouTube 视频、Twitter Spaces 音频，转写为带时间戳的文字稿
> 适用：tweet 里分享的视频、Twitter Spaces、长播客
> 现状：`raw/x-transcripts/` 25 个 .txt（YouTube 转录）；`raw/x-audio/` 1 个 mp3（Twitter Spaces）

---

## 流程总览

```
Tweet URL → 提取嵌入视频 URL → 走 [YouTube SOP] → raw/x-transcripts/<handle>-<tweet_id>.txt
                                                                                ↓
                                                                  [音频转写通用流程] → .md
```

或 Twitter Spaces：

```
Tweet URL (含音频) → 抓 mp3 → raw/x-audio/<handle>-<tweet_id>.mp3 → Groq Whisper → .md
```

## 1. x-transcripts：tweet 嵌入视频的文字稿

**目录**：`raw/x-transcripts/<handle>-<tweet_id>.txt`

**已存在 25 个文件**，命名规范：
- `blurrhaus-1963513003086655900.txt` (handle-tweet_id)
- 来源：tweet 内嵌 YouTube 视频 + 用 youtube-transcript-api 转录

### 处理流程

#### 1.1 解析 tweet 提取视频 URL

```bash
# 用 twitter-cli 或直接抓 tweet HTML
tweet fetch "https://x.com/<handle>/status/<tweet_id>" -o json
# 或用 x-api-setup.md 配置的 twitter-cli
```

提取 `entities.urls[].expanded_url` → 如果是 `https://youtu.be/xxx` 或 `https://youtube.com/watch?v=xxx`，是嵌入 YouTube 视频。

#### 1.2 走 YouTube SOP

拿到 YouTube URL 后按 [YouTube视频入库流程.md](YouTube视频入库流程.md)：
- 优先 `youtube-transcript-api`（双语）
- 降级 `yt-dlp` VTT
- 兜底 STT 路线

#### 1.3 写入 x-transcripts

```python
import json
segs = [{'text': s.text, 'start': s.start, 'duration': s.duration} for s in yt_data]
with open(f'/tmp/{handle}-{tweet_id}.json', 'w') as f:
    json.dump(segs, f, ensure_ascii=False, indent=2)

# 写入 x-transcripts（纯文本格式）
out_path = f'/Users/cunyu666/Design/03_材料/LLM-Wiki/raw/x-transcripts/{handle}-{tweet_id}.txt'
with open(out_path, 'w') as f:
    f.write(f'# {handle} - {tweet_id}\n')
    f.write(f'# 来源: {youtube_url}\n\n')
    for s in segs:
        f.write(f'[{s["start"]:.1f}s] {s["text"]}\n')
```

### 历史文件格式（2024-06 实战）

```text
# blurrhaus - 1963513003086655900
# 来源: https://www.youtube.com/watch?v=xxx

[0.0s] 在这个视频中...
[3.5s] 我们要讨论的主题是...
...
```

**没有 frontmatter**，纯时间戳文本。**简化版** — 如果要写 wiki 索引再补 frontmatter。

## 2. x-audio：Twitter Spaces 音频转写

**目录**：`raw/x-audio/<handle>-<tweet_id>.mp3` (源音频) + `...md` (转录)

**已有文件**：`viktoroddy-1994405408128287146.mp3` (17MB mp3)

### 2.1 抓 Twitter Spaces 音频

Twitter Spaces 音频在 tweet 详情里以 mp3/m4a 形式提供。两种方式：

#### 方式 A：twitter-cli

```bash
# 用 x-api-setup.md 配置的 twitter-cli
tweet audio "https://x.com/<handle>/status/<tweet_id>" \
  -o "/Users/cunyu666/Design/03_材料/LLM-Wiki/raw/x-audio/<handle>-<tweet_id>.mp3"
```

#### 方式 B：手动从浏览器抓

1. 浏览器打开 tweet，DevTools → Network
2. 找 `audio/mp4` 或 `audio/mpeg` 响应
3. 复制 cURL 命令下载

### 2.2 转写（走音频转写通用流程）

```python
# 完整脚本：[音频转写通用流程.md §4](音频转写通用流程.md)
import os
from groq import Groq
client = Groq(api_key=os.environ["GROQ_API_KEY"])

with open("/Users/cunyu666/Design/03_材料/LLM-Wiki/raw/x-audio/viktoroddy-1994405408128287146.mp3", "rb") as f:
    t = client.audio.transcriptions.create(
        file=("audio.mp3", f.read()),
        model="whisper-large-v3-turbo",
        response_format="verbose_json",
        timestamp_granularities=["segment"],
    )

# 写入 .md
import json
segs = [{'start': round(s['start'],2), 'end': round(s['end'],2), 'text': s['text'].strip()} for s in t.segments]
# 合并段 + 写入
...
```

### 2.3 文件结构

```markdown
---
source: x-audio
handle: viktoroddy
tweet_id: "1994405408128287146"
tweet_url: https://x.com/viktoroddy/status/1994405408128287146
duration: 1800
language: en
captured: 2026-06-20
model: whisper-large-v3-turbo
---

# viktoroddy Twitter Spaces: <标题>

> **原始音频**：raw/x-audio/viktoroddy-1994405408128287146.mp3
> **转写引擎**：Groq Whisper API
> **总时长**：1800s

## 完整文字稿
**[00:00:00.000]** ...
...
```

## 3. 实战经验

### 3.1 viktoroddy 文件分析

- **来源**：viktoroddy 是 AI 设计/产品领域 Twitter 用户
- **文件大小**：17MB（mp3, 64kbps stereo, 44.1kHz）
- **预估时长**：约 35-40 分钟
- **建议处理**：直接走 [音频转写通用流程.md](音频转写通用流程.md)，Groq 12s 转完

### 3.2 x-transcripts 25 个文件分类

观察命名规律：
- `<handle>-<tweet_id>.txt` — 模板
- handle 例：`blurrhaus / DataChaz / DilumSanjaya / EHuanglu / ElevenLabs / fal / Fateen_Anam / flowstated / hasantoxr / krea_ai`
- **全是 AI/设计领域 KOL** 的 tweet → 内嵌 YouTube 视频 → 转录

**未来批量处理**：
- 解析 25 个文件的 `tweet_id`
- 用 twitter-cli 拉 tweet 详情
- 提取 YouTube URL
- 检查是否已转录（按 tweet_id 去重）
- 新增的走 YouTube SOP

### 3.3 与 x-bookmarks 区分

| 目录 | 内容 | 来源 |
|------|------|------|
| `x-bookmarks/` | 书签（链接+作者+简介）| 用户收藏的 tweet |
| `x-transcripts/` | tweet 嵌入视频的文字稿 | tweet 内嵌 YouTube 视频 |
| `x-audio/` | tweet 嵌入音频的源文件 + 转录 | Twitter Spaces / 语音推 |

**关系**：x-bookmarks 是 tweet 元数据，x-transcripts/x-audio 是 tweet 内容的深度转录。

## 4. 实战案例

### 4.1 待处理：`viktoroddy-1994405408128287146.mp3`

```bash
# 1. 转写
python3 -c "
import os
from groq import Groq
client = Groq(api_key=os.environ['GROQ_API_KEY'])
with open('/Users/cunyu666/Design/03_材料/LLM-Wiki/raw/x-audio/viktoroddy-1994405408128287146.mp3', 'rb') as f:
    t = client.audio.transcriptions.create(
        file=('audio.mp3', f.read()),
        model='whisper-large-v3-turbo',
        response_format='verbose_json',
        timestamp_granularities=['segment'],
    )
import json
with open('/tmp/viktoroddy-segs.json','w') as f:
    json.dump([{'start':s['start'],'end':s['end'],'text':s['text']} for s in t.segments], f, indent=2)
print(f'Segments: {len(t.segments)}')
"

# 2. 合并段 + 写入 .md
# 3. 删除源 mp3 节省空间（如需）
```

### 4.2 已有 x-transcripts 案例

`raw/x-transcripts/ElevenLabs-1994120106310287793.txt` — ElevenLabs 创始人 tweet 嵌入的 YouTube 视频。

## 5. 错误处理速查

| 错误 | 原因 | 解决 |
|------|------|------|
| tweet 没有视频/音频 | 纯文字 tweet | 跳过，记录到 log |
| 音频 >25MB | 长 Spaces (>60min) | ffmpeg 切 16kHz mono m4a |
| Groq 429 | 短时间请求过多 | 等待 60s 重试 |
| YouTube 视频已删 | 推主删除原视频 | 保留转录 + 标记"原视频已删" |

## 6. Checklist

- [ ] 解析 tweet 拿到视频/音频 URL
- [ ] YouTube 走 SOP
- [ ] Spaces 走音频转写流程
- [ ] 写入 x-transcripts/<handle>-<tweet_id>.txt 或 x-audio/<handle>-<tweet_id>.md
- [ ] 在 wiki 主题 See So 添加引用（如相关）
- [ ] `wiki/log.md` 头部追加记录
- [ ] 删除大源文件（>10MB）节省空间

## 与其他 SOP 的关系

- **YouTube 转录**：[YouTube视频入库流程.md](YouTube视频入库流程.md)
- **音频转写**：[音频转写通用流程.md](音频转写通用流程.md)
- **Twitter CLI 配置**：[x-api-setup.md](x-api-setup.md)
- **书签导出**：[x-bookmarks-export.md](x-bookmarks-export.md)
