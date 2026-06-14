// X (Twitter) Bookmarks Export Script
// 使用方法：
// 1. 打开 https://x.com/i/bookmarks
// 2. 按 F12 打开开发者工具
// 3. 切换到 Console 标签
// 4. 粘贴这个脚本并回车运行
// 5. 等待滚动完成，会自动下载 JSON 文件

(async function exportBookmarks() {
  const bookmarks = [];
  let lastHeight = 0;
  let noNewContentCount = 0;
  const MAX_NO_NEW_CONTENT = 5; // 连续5次没有新内容就停止

  console.log('开始导出 X 书签...');
  console.log('脚本会自动滚动页面，请耐心等待。');

  function extractTweets() {
    // X 的推文文章元素
    const articles = document.querySelectorAll('article[data-testid="tweet"]');
    const newTweets = [];

    articles.forEach(article => {
      try {
        // 提取推文文本
        const tweetTextEl = article.querySelector('[data-testid="tweetText"]');
        const text = tweetTextEl ? tweetTextEl.innerText : '';

        // 提取链接
        const links = [];
        if (tweetTextEl) {
          tweetTextEl.querySelectorAll('a').forEach(a => {
            if (a.href && !a.href.includes('x.com') && !a.href.includes('twitter.com')) {
              links.push(a.href);
            }
          });
        }

        // 提取用户信息
        const userLinkEl = article.querySelector('a[role="link"][href*="/"]');
        const username = userLinkEl ? userLinkEl.href.split('/').pop() : '';
        const displayNameEl = article.querySelector('[data-testid="User-Name"]');
        const displayName = displayNameEl ? displayNameEl.innerText.split('\n')[0] : '';

        // 提取时间
        const timeEl = article.querySelector('time');
        const timestamp = timeEl ? timeEl.getAttribute('datetime') : '';
        const timeText = timeEl ? timeEl.innerText : '';

        // 提取推文链接
        const tweetLinkEl = article.querySelector('a[href*="/status/"]');
        const tweetUrl = tweetLinkEl ? tweetLinkEl.href : '';

        // 提取媒体
        const images = [];
        article.querySelectorAll('img[src*="pbs.twimg.com/media"]').forEach(img => {
          images.push(img.src);
        });

        const videos = [];
        article.querySelectorAll('video').forEach(video => {
          videos.push(video.src || 'video detected');
        });

        // 生成唯一ID
        const id = tweetUrl.split('/status/')[1] || `${username}-${timestamp}`;

        if (text || images.length > 0) {
          newTweets.push({
            id,
            username,
            displayName,
            text,
            links,
            tweetUrl,
            timestamp,
            timeText,
            images,
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

  // 主滚动循环
  while (noNewContentCount < MAX_NO_NEW_CONTENT) {
    const newTweets = extractTweets();
    const added = addUniqueTweets(newTweets);

    console.log(`当前已收集 ${bookmarks.length} 条书签 (本次新增 ${added})`);

    // 滚动到底部
    window.scrollTo(0, document.body.scrollHeight);
    await new Promise(resolve => setTimeout(resolve, 2000)); // 等待加载

    const newHeight = document.body.scrollHeight;
    if (newHeight === lastHeight) {
      noNewContentCount++;
      console.log(`页面高度未变化 (${noNewContentCount}/${MAX_NO_NEW_CONTENT})`);
    } else {
      noNewContentCount = 0;
    }
    lastHeight = newHeight;
  }

  console.log(`\n导出完成！共 ${bookmarks.length} 条书签`);

  // 下载 JSON 文件
  const blob = new Blob([JSON.stringify(bookmarks, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `x-bookmarks-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  console.log('JSON 文件已下载！');

  // 也在控制台输出，方便复制
  console.log('\n书签数据:');
  console.log(JSON.stringify(bookmarks, null, 2));

  return bookmarks;
})();
