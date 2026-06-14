const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// 读取书签数据
const bookmarksPath = path.join(__dirname, '..', 'raw', 'x-bookmarks-2026-06-14.json');
const bookmarks = JSON.parse(fs.readFileSync(bookmarksPath, 'utf8'));

// 筛选有视频的书签
const videoBookmarks = bookmarks.filter(b => b.videos === true && b.tweetUrl);
console.log(`共 ${bookmarks.length} 条书签，其中 ${videoBookmarks.length} 条有视频\n`);

// 创建下载目录
const downloadDir = path.join(__dirname, '..', 'raw', 'x-videos');
if (!fs.existsSync(downloadDir)) {
  fs.mkdirSync(downloadDir, { recursive: true });
}

// Cookies 文件路径
const cookiesPath = '/Users/cunyu666/Downloads/x.com_cookies.txt';

// 下载视频的函数
function downloadVideo(tweetUrl, filename) {
  try {
    const outputTemplate = path.join(downloadDir, `${filename}.%(ext)s`);
    const cmd = `yt-dlp --cookies "${cookiesPath}" --no-check-certificates -o "${outputTemplate}" "${tweetUrl}"`;

    console.log(`下载中: ${filename}`);
    execSync(cmd, { stdio: 'pipe' });
    return true;
  } catch (error) {
    console.error(`下载失败: ${filename} - ${error.message}`);
    return false;
  }
}

// 批量下载
let successCount = 0;
let failCount = 0;

for (const bookmark of videoBookmarks) {
  const id = bookmark.id;
  const username = bookmark.username;
  const filename = `${username}-${id}`;

  // 检查是否已下载
  const existingFiles = fs.readdirSync(downloadDir).filter(f => f.startsWith(filename));
  if (existingFiles.length > 0) {
    console.log(`跳过已下载: ${filename}`);
    successCount++;
    continue;
  }

  if (downloadVideo(bookmark.tweetUrl, filename)) {
    successCount++;
  } else {
    failCount++;
  }

  // 限速，避免被封
  if (videoBookmarks.indexOf(bookmark) < videoBookmarks.length - 1) {
    execSync('sleep 2');
  }
}

console.log(`\n下载完成: 成功 ${successCount}，失败 ${failCount}`);
console.log(`视频保存在: ${downloadDir}`);
