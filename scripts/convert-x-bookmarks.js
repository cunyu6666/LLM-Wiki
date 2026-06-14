const fs = require('fs');
const path = require('path');

// 读取书签数据
const bookmarksPath = path.join(__dirname, '..', 'x-bookmarks-2026-06-14.json');
const bookmarks = JSON.parse(fs.readFileSync(bookmarksPath, 'utf8'));

console.log(`共读取 ${bookmarks.length} 条书签`);

// 分类函数
function categorize(text) {
  const lower = text.toLowerCase();

  // AI 工具
  if (lower.match(/gemini|claude|gpt|llm|ai|nano banana|magnific|elevenlabs|kling|wan|odyssey|hunyuan|openclaw|pippit/i)) {
    if (lower.match(/video|motion|animation|3d|upscale/i)) return 'AI 视频与动画';
    if (lower.match(/image|photo|design|ui|ux|logo/i)) return 'AI 设计工具';
    if (lower.match(/code|coding|ide|cursor|antigravity|lovable|trae|vibe/i)) return 'AI 编程工具';
    return 'AI 工具';
  }

  // 设计工具
  if (lower.match(/framer|figma|shadcn|base ui|component|ui library|tailwind|unicorn|shader/i)) {
    if (lower.match(/component|library|ui kit/i)) return 'UI 组件库';
    return '设计工具';
  }

  // 开发工具
  if (lower.match(/cursor|ide|vscode|linear|tldraw|obsidian|mermaid|raycast|glaze/i)) {
    return '开发工具';
  }

  // 硬件/IoT
  if (lower.match(/m5stack|esp|hardware|iot/i)) return '硬件与 IoT';

  // 设计灵感
  if (lower.match(/hero section|landing page|card|animation|motion|color/i)) return '设计灵感';

  return '其他';
}

// 按分类整理
const categorized = {};
bookmarks.forEach(b => {
  const category = b.text ? categorize(b.text) : '其他';
  if (!categorized[category]) categorized[category] = [];
  categorized[category].push(b);
});

console.log('\n分类统计:');
Object.entries(categorized).forEach(([cat, items]) => {
  console.log(`  ${cat}: ${items.length} 条`);
});

// 生成 markdown
function generateMarkdown(category, items) {
  let md = `---\ntitle: "${category}"\ndescription: "X 书签 - ${category}"\ntags: [x-bookmarks, ${category.toLowerCase().replace(/\s+/g, '-')}]\ndate: ${new Date().toISOString().slice(0, 10)}\n---\n\n# ${category}\n\n> 从 X (Twitter) 书签导入\n\n`;

  items.forEach(item => {
    const date = item.timeText || item.timestamp?.slice(0, 10) || '';
    const author = item.displayName || item.username;
    const text = item.text || '(无文字)';
    const url = item.tweetUrl;

    md += `## ${author} (${date})\n\n`;
    md += `${text}\n\n`;

    if (item.links && item.links.length > 0) {
      md += `**链接:** ${item.links.join(', ')}\n\n`;
    }

    if (item.images && item.images.length > 0) {
      md += `**图片:** ${item.images.length} 张\n\n`;
    }

    if (item.videos) {
      md += `**视频:** 是\n\n`;
    }

    md += `[查看原文](${url})\n\n---\n\n`;
  });

  return md;
}

// 写入文件
const outputDir = path.join(__dirname, '..', 'wiki', 'x-bookmarks');
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// 写入索引文件
let indexMd = `---\ntitle: "X 书签"\ndescription: "从 X (Twitter) 导入的书签合集"\ntags: [x-bookmarks, index]\ndate: ${new Date().toISOString().slice(0, 10)}\n---\n\n# X 书签\n\n> 共 ${bookmarks.length} 条书签，按主题分类\n\n`;

Object.entries(categorized).forEach(([category, items]) => {
  const filename = category.replace(/\s+/g, '-').toLowerCase() + '.md';
  indexMd += `- [[${filename}|${category}]] (${items.length} 条)\n`;

  // 写入分类文件
  const filePath = path.join(outputDir, filename);
  fs.writeFileSync(filePath, generateMarkdown(category, items), 'utf8');
  console.log(`已创建: ${filename}`);
});

// 写入索引
fs.writeFileSync(path.join(outputDir, '_index.md'), indexMd, 'utf8');
console.log('已创建: _index.md (索引文件)');

console.log(`\n完成！文件保存在: ${outputDir}`);
