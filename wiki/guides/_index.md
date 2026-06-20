---
type: index
description: "项目操作指南、工具配置、流程文档"
timestamp: 2026-06-20
---
# 指南索引

> 项目操作指南、工具配置、流程文档

## 工具配置

| 指南 | 说明 |
|------|------|
| [X API 调通指南](x-api-setup.md) | ClashX Pro 代理 + Cookie 导出 + twitter-cli 配置 |
| [X 书签导出指南](x-bookmarks-export.md) | 从 X (Twitter) 导出书签并转换为 wiki 格式 |

## 数据流程

| 指南 | 说明 |
|------|------|
| [抖音视频下载指南](抖音视频下载指南.md) | Cookie 提取 + 收藏列表 API + 批量下载 |
| [抖音视频入库流程](抖音视频入库流程.md) | 视频转文字稿 + 分类入库 wiki |
| [YouTube 视频入库流程](YouTube视频入库流程.md) | YouTube 链接 → 字幕抓取 → 段级合并 → 信达雅翻译 → 软链到 wiki/speech/yt-talks/ → 收录金句 |
| [小红书入库流程](小红书入库流程.md) | 未登录抓取 + __INITIAL_STATE__ 解析 + macOS Vision API OCR → raw/小红书/imgs/ + wiki/<主题>/ 索引 |
| [Cubox 入库流程](Cubox入库流程.md) | cubox-cli 抓收藏 + 微信/小红书文章分类归档 → raw/文章汇总/ + wiki/<主题>/ 索引 |
| [音频转写通用流程](音频转写通用流程.md) | 任意 mp3/m4a → ffmpeg 标准化 → Groq Whisper API → 带时间戳 .md（Groq 凭据已就绪）|
| [x-transcripts-x-audio 流程](x-transcripts-x-audio流程.md) | tweet 嵌入视频（YouTube）+ Twitter Spaces 音频 → 文字稿 |

---
*最后更新：2026-06-20*
