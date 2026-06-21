#!/usr/bin/env node
// 分类器：对 all-links.tsv 逐条判 ok/broken
//   md   → 相对源文件解析，存在→ok，缺→broken
//   wiki → 在 wiki/ 全树按页面名（去 .md/.md 后缀）查 .md，存在→ok，缺→broken
//   absolute → 仅检查 raw 显示文本是否含 /Users/... 这种绝对路径，是→broken
// 输出：
//   broken-links.json: [{source, kind, raw, target, reason}]
//   link-classification.md: 人类可读汇总

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const LINKS = path.join(__dirname, 'all-links.tsv');
const WIKI_ROOT = path.join(ROOT, 'wiki');
const OUT_JSON = path.join(__dirname, 'broken-links.json');
const OUT_MD = path.join(__dirname, 'link-classification.md');

// 预扫描 vault：所有 wiki 子树下的文件名（去 .md）→ 相对路径
function indexVault() {
  const map = new Map(); // basename(去 .md) -> [absPath]
  function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      if (entry.name.startsWith('.')) continue;
      const p = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(p);
      else if (entry.isFile() && p.endsWith('.md')) {
        const base = entry.name.replace(/\.md$/, '');
        if (!map.has(base)) map.set(base, []);
        map.get(base).push(p);
      }
    }
  }
  walk(WIKI_ROOT);
  return map;
}

function readRawText(abs) {
  return fs.readFileSync(abs, 'utf8');
}

function classifyOne(row, vault) {
  const [source, kind, raw, target] = row;
  if (kind === 'md') {
    const srcDir = path.dirname(path.join(ROOT, source));
    const tryPaths = [
      path.resolve(srcDir, target),
      path.resolve(srcDir, decodeURIComponent(target)),
      path.resolve(ROOT, target),
      path.resolve(ROOT, decodeURIComponent(target)),
    ];
    for (const p of tryPaths) {
      if (fs.existsSync(p)) return { status: 'ok', reason: `resolved: ${path.relative(ROOT, p)}` };
    }
    return { status: 'broken', reason: `target not found: ${path.relative(ROOT, tryPaths[0])}` };
  }
  if (kind === 'wiki') {
    const base = target.trim();
    const hits = vault.get(base);
    if (hits && hits.length) return { status: 'ok', reason: `vault hit: ${path.relative(ROOT, hits[0])}` };
    return { status: 'broken', reason: `wikilink target missing in vault: [[${base}]]` };
  }
  if (kind === 'absolute') {
    const srcAbs = path.join(ROOT, source);
    const text = readRawText(srcAbs);
    // 在 raw 显示文本里找匹配 url 的中括号 [...]，判断内容是否是绝对路径
    const re = /\[([^\]\r\n]*)\]\(([^)\r\n]+)\)/g;
    let m;
    while ((m = re.exec(text)) !== null) {
      if (m[2] === target) {
        if (/^\/Users\//.test(m[1]) || /^\/Users\//.test(m[2])) {
          return { status: 'broken', reason: `display text / href is absolute macOS path: "${m[1]}" -> "${m[2]}"` };
        }
        const srcDir = path.dirname(srcAbs);
        const resolved = path.resolve(srcDir, m[2]);
        if (fs.existsSync(resolved)) return { status: 'ok', reason: 'resolved (non-absolute text)' };
        return { status: 'broken', reason: `href missing: ${m[2]}` };
      }
    }
    return { status: 'broken', reason: 'absolute display not matched' };
  }
  return { status: 'unknown', reason: `unknown kind ${kind}` };
}

const lines = fs.readFileSync(LINKS, 'utf8').split('\n').filter(Boolean);
const header = lines.shift();
const rows = lines.map((l) => l.split('\t'));
const vault = indexVault();

const results = rows.map((r) => ({ row: r, ...classifyOne(r, vault) }));
const broken = results.filter((x) => x.status === 'broken');
const ok = results.filter((x) => x.status === 'ok');

// 写 JSON
fs.writeFileSync(
  OUT_JSON,
  JSON.stringify(
    broken.map((x) => ({ source: x.row[0], kind: x.row[1], raw: x.row[2], target: x.row[3], reason: x.reason })),
    null,
    2
  )
);

// 写 markdown
const md = [];
md.push(`# speech/ 链接分类（自动）`);
md.push('');
md.push(`- 生成时间：${new Date().toISOString()}`);
md.push(`- 总数：${results.length}（ok: ${ok.length}, broken: ${broken.length}）`);
md.push(`- 数据源：all-links.tsv（54 条 = 11 wiki + 43 md）`);
md.push('');
md.push('## Broken 链接');
if (broken.length === 0) {
  md.push('无。');
} else {
  broken.forEach((x) => {
    md.push(`- **${x.row[0]}**`);
    md.push(`  - 类型：${x.row[1]}`);
    md.push(`  - 原文：\`${x.row[2]}\``);
    md.push(`  - 原因：${x.reason}`);
  });
}
md.push('');
md.push('## OK 链接');
md.push('');
md.push(`共 ${ok.length} 条，按源文件分组：`);
const bySrc = new Map();
ok.forEach((x) => {
  if (!bySrc.has(x.row[0])) bySrc.set(x.row[0], []);
  bySrc.get(x.row[0]).push(x);
});
for (const [src, items] of [...bySrc.entries()].sort()) {
  md.push(`### ${src} (${items.length})`);
  items.forEach((x) => md.push(`- \`${x.row[2]}\` — ${x.reason}`));
}
fs.writeFileSync(OUT_MD, md.join('\n') + '\n');

console.log(`total ${results.length} | ok ${ok.length} | broken ${broken.length}`);
console.log(`-> ${path.relative(ROOT, OUT_JSON)}`);
console.log(`-> ${path.relative(ROOT, OUT_MD)}`);