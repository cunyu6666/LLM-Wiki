#!/usr/bin/env bash
set -euo pipefail

# Grub harness 启动脚本（get-bearings 协议）。
# 该脚本只做"项目还活着吗"的最小校验，不修改任何目标文件。

echo "=== grub bearings ==="
cd "$(dirname "$0")/../.."
pwd
echo "--- recent commits ---"
git log --oneline -n 20 2>/dev/null || true
echo "--- working tree ---"
git status --short 2>/dev/null || true
echo "--- progress tail ---"
tail -n 40 "/Users/cunyu666/Projects/cunyu-llm-wiki/.grub/b84a4fd5/progress-log.md" 2>/dev/null || true
echo "--- feature progress ---"
node -e "try{const l=require('/Users/cunyu666/Projects/cunyu-llm-wiki/.grub/b84a4fd5/feature-list.json');const p=l.features.filter(f=>f.passes).length;console.log(p+'/'+l.features.length+' passing');}catch(e){console.log('feature-list.json unavailable');}" 2>/dev/null || true

echo "--- project smoke (override below) ---"
# 项目专属烟测：speech/ 下应有 .md 链接分类产物（若已生成）
SMOKE_DIR="/Users/cunyu666/Projects/cunyu-llm-wiki/.grub/b84a4fd5"
if [ -f "$SMOKE_DIR/link-classification.md" ]; then
  echo "link-classification.md exists:"
  head -n 20 "$SMOKE_DIR/link-classification.md"
else
  echo "link-classification.md not generated yet (expected on first runs)"
fi
if [ -f "$SMOKE_DIR/broken-links.json" ]; then
  echo "broken-links.json exists, total entries: $(node -e "try{const a=require('$SMOKE_DIR/broken-links.json');console.log(Array.isArray(a)?a.length:Object.keys(a).length);}catch(e){console.log('parse-error');}")"
else
  echo "broken-links.json not generated yet"
fi
