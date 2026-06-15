#!/usr/bin/env python3
"""Replace external moonvy.com source URLs with local Obsidian wikilinks."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / "wiki" / "design"

# Pattern: > 来源：周刊 #NNN · YYYY/MM/DD · [display](https://moonvy.com/...)
SOURCE_PATTERN = re.compile(
    r"(> 来源：周刊 #(\d+) · (\d{4}/\d{2}/\d{2}) · )"
    r"\[[^\]]*\]\(https?://moonvy\.com/blog/post/[^)]+\)"
)


def replace_source(match: re.Match) -> str:
    prefix = match.group(1)  # "> 来源：周刊 #071 · 2023/07/02 · "
    week_num = match.group(2)  # "071"
    # Build wikilink: [[设计素材周刊-071]]
    wikilink = f"[[设计素材周刊-{week_num.zfill(3)}]]"
    return prefix + wikilink


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    new_text, count = SOURCE_PATTERN.subn(replace_source, text)
    if count > 0:
        path.write_text(new_text, encoding="utf-8")
    return count


def main():
    total = 0
    for md in sorted(DESIGN.glob("*.md")):
        count = process_file(md)
        if count:
            print(f"  {md.name}: {count} 处")
            total += count
    print(f"\n总计替换: {total} 处")


if __name__ == "__main__":
    main()
