#!/usr/bin/env node
// 从 speech/ 下所有 .md 抽取 wikilink 与 markdown 内部链接。
// 输出：all-links.tsv，列：source_file<TAB>kind<TAB>raw<TAB>target
//   kind: wiki | md | absolute
//   target: 对 md 链接为原始 path；对 wiki 为页面名；absolute 留空由后续分类

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const SPEECH = path.join(ROOT, 'wiki', 'speech');
const OUT = path.join(__dirname, 'all-links.tsv');

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(p, out);
    else if (entry.isFile() && p.endsWith('.md')) out.push(p);
  }
  return out;
}

const WIKI_RE = /\[\[([^\]\r\n]+)\]\]/g;
const MD_LINK_RE = /\[([^\]\r\n]*)\]\(([^)\r\n]+)\)/g;
const CODE_FENCE = /```/g;

const files = walk(SPEECH);
const rows = [];
for (const abs of files) {
  const rel = path.relative(ROOT, abs);
  const text = fs.readFileSync(abs, 'utf8');
  // 跳过代码块内部
  const cleaned = text.replace(/```[\s\S]*?```/g, (m) => ' '.repeat(m.length));

  // wikilink
  let m;
  WIKI_RE.lastIndex = 0;
  while ((m = WIKI_RE.exec(cleaned)) !== null) {
    const raw = m[1];
    const target = raw.split('|')[0].split('#')[0].trim();
    rows.push([rel, 'wiki', `[[${raw}]]`, target]);
  }
  // markdown 链接
  MD_LINK_RE.lastIndex = 0;
  while ((m = MD_LINK_RE.exec(cleaned)) !== null) {
    const txt = m[1];
    const href = m[2].trim();
    if (/^https?:\/\//i.test(href)) continue; // 跳过外链
    if (/^mailto:/i.test(href)) continue;
    if (/^#/.test(href)) continue; // 页内锚
    if (href.startsWith('file://')) continue;
    let kind = 'md';
    if (/^\//.test(href)) kind = 'absolute';
    rows.push([rel, kind, `[${txt}](${href})`, href]);
  }
}

const header = 'source_file\tkind\traw\ttarget\n';
const body = rows.map((r) => r.join('\t')).join('\n');
fs.writeFileSync(OUT, header + body + (body ? '\n' : ''));
console.log(`extracted ${rows.length} links from ${files.length} files -> ${path.relative(ROOT, OUT)}`);
