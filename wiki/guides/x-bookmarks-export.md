---
title: "X (Twitter) 书签导出指南"
description: "从 X 导出书签并转换为 wiki 格式的完整流程"
tags: [x-bookmarks, 导出, 工具, 教程]
date: 2026-06-14
type: guide
---

# X (Twitter) 书签导出指南

## 概述

从 X (Twitter) 导出书签到本地 wiki，包含文字、图片、视频的完整备份。

## 前置条件

- Chrome 浏览器
- 已登录 X 账号
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)（用于下载视频）
- Node.js

## 导出步骤

### 1. 导出书签数据

1. 打开 https://x.com/i/bookmarks
2. 按 `F12` 打开开发者工具
3. 切换到 **Console** 标签
4. 输入 `allow pasting` 并回车（Chrome 安全机制）
5. 粘贴以下脚本并运行：

```javascript
(async function exportBookmarks() {
  const bookmarks = [];
  let lastHeight = 0;
  let noNewContentCount = 0;
  const MAX_NO_NEW_CONTENT = 5;

  console.log('开始导出 X 书签...');

  function extractTweets() {
    const articles = document.querySelectorAll('article[data-testid="tweet"]');
    const newTweets = [];

    articles.forEach(article => {
      try {
        const tweetTextEl = article.querySelector('[data-testid="tweetText"]');
        const text = tweetTextEl ? tweetTextEl.innerText : '';

        const links = [];
        if (tweetTextEl) {
          tweetTextEl.querySelectorAll('a').forEach(a => {
            if (a.href && !a.href.includes('x.com') && !a.href.includes('twitter.com')) {
              links.push(a.href);
            }
          });
        }

        const userLinkEl = article.querySelector('a[role="link"][href*="/"]');
        const username = userLinkEl ? userLinkEl.href.split('/').pop() : '';
        const displayNameEl = article.querySelector('[data-testid="User-Name"]');
        const displayName = displayNameEl ? displayNameEl.innerText.split('\n')[0] : '';

        const timeEl = article.querySelector('time');
        const timestamp = timeEl ? timeEl.getAttribute('datetime') : '';
        const timeText = timeEl ? timeEl.innerText : '';

        const tweetLinkEl = article.querySelector('a[href*="/status/"]');
        const tweetUrl = tweetLinkEl ? tweetLinkEl.href : '';

        const images = [];
        article.querySelectorAll('img[src*="pbs.twimg.com/media"]').forEach(img => {
          images.push(img.src);
        });

        const videos = [];
        article.querySelectorAll('video').forEach(video => {
          videos.push(video.src || 'video detected');
        });

        const id = tweetUrl.split('/status/')[1] || `${username}-${timestamp}`;

        if (text || images.length > 0) {
          newTweets.push({
            id, username, displayName, text, links, tweetUrl, timestamp, timeText, images,
            videos: videos.length > 0 ? true : false
          });
        }
      } catch (e) {
        console.warn('提取推文时出错:', e);
      }
    });

    return newTweets;
  }

  function addUniqueTweets(newTweets) {
    const existingIds = new Set(bookmarks.map(t => t.id));
    let added = 0;
    newTweets.forEach(tweet => {
      if (!existingIds.has(tweet.id)) {
        bookmarks.push(tweet);
        existingIds.add(tweet.id);
        added++;
      }
    });
    return added;
  }

  while (noNewContentCount < MAX_NO_NEW_CONTENT) {
    const newTweets = extractTweets();
    const added = addUniqueTweets(newTweets);
    console.log(`当前已收集 ${bookmarks.length} 条书签 (本次新增 ${added})`);

    window.scrollTo(0, document.body.scrollHeight);
    await new Promise(resolve => setTimeout(resolve, 2000));

    const newHeight = document.body.scrollHeight;
    if (newHeight === lastHeight) {
      noNewContentCount++;
    } else {
      noNewContentCount = 0;
    }
    lastHeight = newHeight;
  }

  console.log(`\n导出完成！共 ${bookmarks.length} 条书签`);

  const blob = new Blob([JSON.stringify(bookmarks, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `x-bookmarks-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  return bookmarks;
})();
```

6. 等待滚动完成，自动下载 JSON 文件

### 2. 保存原始数据

将下载的 JSON 文件放到 `raw/` 目录：

```bash
mv ~/Downloads/x-bookmarks-*.json raw/
```

### 3. 导出 Cookies（下载视频需要）

1. 安装 Chrome 扩展 [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
2. 在 X 页面点击扩展图标
3. 导出 cookies.txt 文件
4. 保存到 `~/Downloads/x.com_cookies.txt`

### 4. 下载视频

```bash
node scripts/download-x-videos.js
```

视频会下载到 `raw/x-videos/` 目录。

### 5. 转换为 Wiki 格式

```bash
node scripts/convert-x-bookmarks.js
```

会在 `wiki/x-bookmarks/` 生成分类的 markdown 文件。

## 脚本说明

| 脚本 | 用途 |
|------|------|
| `scripts/x-bookmarks-export.js` | 浏览器控制台脚本，提取书签数据 |
| `scripts/download-x-videos.js` | 使用 yt-dlp 批量下载视频 |
| `scripts/convert-x-bookmarks.js` | 将 JSON 转换为 wiki markdown |

## 分类规则

书签按内容自动分类：

- **AI 工具** — 通用 AI 工具
- **AI 设计工具** — AI 图像/设计相关
- **AI 编程工具** — AI IDE/编程助手
- **AI 视频与动画** — AI 视频生成
- **设计工具** — Framer、Figma 等
- **UI 组件库** — shadcn、Base UI 等
- **开发工具** — IDE、效率工具
- **设计灵感** — Hero section、动画示例
- **硬件与 IoT** — 硬件项目
- **其他** — 未分类

## 注意事项

- X 书签 API 有 rate limit，脚本会自动限速
- 视频下载需要 cookies 认证
- 导出的 JSON 包含：文字、链接、图片 URL、视频标记、时间戳
- 图片只保存 URL，未下载原图

## 相关文件

- `raw/x-bookmarks-*.json` — 原始数据
- `raw/x-videos/` — 下载的视频
- `wiki/x-bookmarks/` — 转换后的 wiki 页面
