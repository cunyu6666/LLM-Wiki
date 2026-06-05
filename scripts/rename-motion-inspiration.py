#!/usr/bin/env python3
"""P1: Rename 动效与加载 → 动效灵感, move inspiration-site entries to 灵感网站."""

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki" / "design"

INSPIRATION_PATTERNS = [
    r"灵感网站", r"灵感、细节", r"APP 灵感", r"APP 设计灵感",
    r"设计灵感", r"inspiration", r"60fps", r"designspells",
    r"spottedinprod", r"交互 Demo 欣赏",
]


def parse_sections(content: str):
    parts = re.split(r"(?=^### )", content, flags=re.MULTILINE)
    header = parts[0]
    sections = []
    for part in parts[1:]:
        m = re.match(r"^### (.+?)\n", part)
        if m:
            sections.append((m.group(1).strip(), part))
    return header, sections


def is_inspiration(title: str, body: str) -> bool:
    combined = title + body[:300]
    return any(re.search(p, combined, re.IGNORECASE) for p in INSPIRATION_PATTERNS)


def main():
    src = WIKI / "动效与加载.md"
    content = src.read_text(encoding="utf-8")
    header, sections = parse_sections(content)

    keep, move = [], []
    for title, section in sections:
        if is_inspiration(title, section):
            move.append(section)
        else:
            keep.append(section)

    # Rename file content
    new_header = header.replace("# 动效与加载", "# 动效灵感")
    new_header = new_header.replace("「动效与加载」", "「动效灵感」")
    new_header = re.sub(r"> \d+ moonvy", f"> {len(keep)} moonvy", new_header, count=1)
    new_header = re.sub(r"共 \d+ 个", f"共 {len(keep)} 个", new_header)

    new_path = WIKI / "动效灵感.md"
    new_path.write_text(new_header + "\n".join(keep), encoding="utf-8")
    if src.exists() and src != new_path:
        src.unlink()

    # Append to 灵感网站
    if move:
        insp = WIKI / "灵感网站.md"
        icontent = insp.read_text(encoding="utf-8")
        iheader, isections = parse_sections(icontent)
        old = len(isections)
        new_count = old + len(move)
        iheader = re.sub(r"> \d+ moonvy", f"> {new_count} moonvy", iheader, count=1)
        iheader = re.sub(r"共 \d+ 个", f"共 {new_count} 个", iheader)
        insp.write_text(iheader + "".join(s for _, s in isections) + "".join(move), encoding="utf-8")

    print(f"动效灵感: {len(keep)} kept, {len(move)} moved to 灵感网站")
    print(f"Renamed: 动效与加载.md → 动效灵感.md")


if __name__ == "__main__":
    main()
