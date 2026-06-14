const fs = require('fs');
const path = require('path');

// 路径配置
const RAW_DIR = path.join(__dirname, '..', 'raw', 'x-bookmarks');
const WIKI_DIR = path.join(__dirname, '..', 'wiki', 'x-bookmarks');
const JSON_PATH = path.join(__dirname, '..', 'raw', 'x-bookmarks-2026-06-14.json');

// 分类函数
function categorize(text) {
  const lower = (text || '').toLowerCase();
  if (lower.match(/gemini|claude|gpt|llm|ai|nano banana|magnific|elevenlabs|kling|wan|odyssey|hunyuan|openclaw|pippit/i)) {
    if (lower.match(/video|motion|animation|3d|upscale/i)) return 'ai-视频与动画';
    if (lower.match(/image|photo|design|ui|ux|logo/i)) return 'ai-设计工具';
    if (lower.match(/code|coding|ide|cursor|antigravity|lovable|trae|vibe/i)) return 'ai-编程工具';
    return 'ai-工具';
  }
  if (lower.match(/framer|figma|shadcn|base ui|component|ui library|tailwind|unicorn|shader/i)) {
    if (lower.match(/component|library|ui kit/i)) return 'ui-组件库';
    return '设计工具';
  }
  if (lower.match(/cursor|ide|vscode|linear|tldraw|obsidian|mermaid|raycast|glaze/i)) return '开发工具';
  if (lower.match(/m5stack|esp|hardware|iot/i)) return '硬件与-iot';
  if (lower.match(/hero section|landing page|card|animation|motion|color/i)) return '设计灵感';
  return '其他';
}

// 读取书签数据
const bookmarks = JSON.parse(fs.readFileSync(JSON_PATH, 'utf8'));

// 按分类整理
const categorized = {};
bookmarks.forEach(b => {
  const category = b.text ? categorize(b.text) : '其他';
  if (!categorized[category]) categorized[category] = [];
  categorized[category].push(b);
});

// 确保目录存在
if (!fs.existsSync(WIKI_DIR)) {
  fs.mkdirSync(WIKI_DIR, { recursive: true });
}

// 生成分类文章
function generateCategoryArticle(category, items) {
  const categoryNames = {
    'ai-工具': 'AI 工具',
    'ai-设计工具': 'AI 设计工具',
    'ai-编程工具': 'AI 编程工具',
    'ai-视频与动画': 'AI 视频与动画',
    '设计工具': '设计工具',
    'ui-组件库': 'UI 组件库',
    '开发工具': '开发工具',
    '设计灵感': '设计灵感',
    '硬件与-iot': '硬件与 IoT',
    '其他': '其他'
  };

  const categoryName = categoryNames[category] || category;
  const today = new Date().toISOString().slice(0, 10);

  // 提取关键洞察
  const insights = [];
  const tools = new Set();
  const people = new Set();

  items.forEach(item => {
    // 提取工具名称
    const text = (item.text || '').toLowerCase();
    const toolMatches = text.match(/\b(cursor|framer|figma|shadcn|lovable|v0|raycast|glaze|tldraw|linear|obsidian|elevenlabs|magnific|kling|wan|gemini|claude|gpt)\b/gi);
    if (toolMatches) {
      toolMatches.forEach(t => tools.add(t));
    }

    // 提取人名
    if (item.displayName && item.displayName.length > 2) {
      people.add(item.displayName);
    }
  });

  // 生成文章内容
  let content = `---
title: "${categoryName}"
description: "X 书签精选 - ${categoryName}"
tags: [x-bookmarks, ${category}]
date: ${today}
sources: ${items.length}
---

# ${categoryName}

> 从 X (Twitter) 书签中精选的${categoryName}相关内容，共 ${items.length} 条。

`;

  // 添加关键工具
  if (tools.size > 0) {
    content += `## 涉及工具\n\n${Array.from(tools).join('、')}\n\n`;
  }

  // 添加关键人物
  if (people.size > 0 && people.size <= 10) {
    content += `## 关注人物\n\n${Array.from(people).join('、')}\n\n`;
  }

  // 添加内容列表
  content += `## 精选内容\n\n`;

  // 按时间排序
  items.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

  items.forEach(item => {
    const date = item.timeText || item.timestamp?.slice(0, 10) || '';
    const author = item.displayName || item.username;
    const text = (item.text || '').split('\n')[0].slice(0, 100);
    const url = item.tweetUrl;
    const hasVideo = item.videos;
    const hasImages = item.images && item.images.length > 0;

    content += `### ${author} (${date})\n\n`;
    content += `${text}${(item.text || '').length > 100 ? '...' : ''}\n\n`;

    // 媒体标记
    const media = [];
    if (hasVideo) media.push('视频');
    if (hasImages) media.push(`${item.images.length} 张图片`);
    if (media.length > 0) {
      content += `**媒体：** ${media.join('、')}\n\n`;
    }

    // 链接
    content += `[查看原文](${url})\n\n`;

    // 如果有对应的 raw 文件，添加引用
    const rawFile = `${item.username}-${item.id}.md`;
    if (fs.existsSync(path.join(RAW_DIR, rawFile))) {
      content += `**详细内容：** [[../../raw/x-bookmarks/${rawFile}|${rawFile}]]\n\n`;
    }

    content += `---\n\n`;
  });

  // 添加 See Also
  content += `## See Also\n\n`;
  content += `- [[../guides/x-bookmarks-export|X 书签导出指南]]\n`;
  content += `- [[../index|知识库首页]]\n`;

  return content;
}

// 生成索引文件
function generateIndex() {
  const today = new Date().toISOString().slice(0, 10);

  let content = `---
title: "X 书签"
description: "从 X (Twitter) 导入的书签合集"
tags: [x-bookmarks, index]
date: ${today}
---

# X 书签

> 从 X (Twitter) 书签导入的精选内容，按主题分类整理。
> 共 ${bookmarks.length} 条书签，${Object.keys(categorized).length} 个分类。

## 分类索引

| 分类 | 数量 | 描述 |
|------|------|------|
`;

  const categoryDescriptions = {
    'ai-工具': '通用 AI 工具和平台',
    'ai-设计工具': 'AI 图像生成、设计辅助',
    'ai-编程工具': 'AI IDE、编程助手',
    'ai-视频与动画': 'AI 视频生成、动画工具',
    '设计工具': 'Framer、Figma 等设计工具',
    'ui-组件库': 'shadcn、Base UI 等组件库',
    '开发工具': 'IDE、效率工具、协作平台',
    '设计灵感': 'Hero section、动画示例',
    '硬件与-iot': '硬件项目、IoT 设备',
    '其他': '未分类内容'
  };

  Object.entries(categorized)
    .sort((a, b) => b[1].length - a[1].length)
    .forEach(([category, items]) => {
      const categoryNames = {
        'ai-工具': 'AI 工具',
        'ai-设计工具': 'AI 设计工具',
        'ai-编程工具': 'AI 编程工具',
        'ai-视频与动画': 'AI 视频与动画',
        '设计工具': '设计工具',
        'ui-组件库': 'UI 组件库',
        '开发工具': '开发工具',
        '设计灵感': '设计灵感',
        '硬件与-iot': '硬件与 IoT',
        '其他': '其他'
      };
      const name = categoryNames[category] || category;
      const desc = categoryDescriptions[category] || '';
      content += `| [[${category}|${name}]] | ${items.length} | ${desc} |\n`;
    });

  content += `\n## 数据来源\n\n`;
  content += `- **导出时间：** 2026-06-14\n`;
  content += `- **原始数据：** [[../../raw/x-bookmarks-2026-06-14.json|x-bookmarks-2026-06-14.json]]\n`;
  content += `- **视频文件：** [[../../raw/x-videos|raw/x-videos/]]\n`;
  content += `- **书签页面：** [[../../raw/x-bookmarks|raw/x-bookmarks/]]\n\n`;

  content += `## See Also\n\n`;
  content += `- [[../guides/x-bookmarks-export|X 书签导出指南]]\n`;
  content += `- [[../index|知识库首页]]\n`;

  return content;
}

// 写入文件
console.log('开始编译 X 书签到 Wiki...\n');

// 生成分类文章
Object.entries(categorized).forEach(([category, items]) => {
  const filename = `${category}.md`;
  const filepath = path.join(WIKI_DIR, filename);
  const content = generateCategoryArticle(category, items);

  fs.writeFileSync(filepath, content, 'utf8');
  console.log(`已生成: ${filename} (${items.length} 条)`);
});

// 生成索引
const indexContent = generateIndex();
fs.writeFileSync(path.join(WIKI_DIR, '_index.md'), indexContent, 'utf8');
console.log('\n已生成: _index.md');

console.log(`\n编译完成！文件保存在: ${WIKI_DIR}`);
