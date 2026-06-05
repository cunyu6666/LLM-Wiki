#!/usr/bin/env python3
"""Fix 灵感网站.md: restore + append moved entries from 其他资源 and 动效与加载."""

import re
import subprocess
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki" / "design"
ROOT = WIKI.parent.parent

INSPIRATION_FROM_MOTION = [
    r"灵感网站", r"灵感、细节", r"APP 灵感", r"APP 设计灵感",
    r"交互 Demo 欣赏",
]

ROUTE_TO_LINGGAN = [
    r"个人网站", r"网页设计", r"网站欣赏", r"网站设计", r"1000个鼓舞",
    r"设计师社区", r"导航站", r"在线体验.*mac", r"博物馆", r"考古", r"博客$",
]


def git_show(path: str) -> str:
    return subprocess.check_output(["git", "show", f"HEAD:{path}"], cwd=ROOT, text=True)


def parse_sections(content: str):
    parts = re.split(r"(?=^### )", content, flags=re.MULTILINE)
    header = parts[0]
    sections = []
    for part in parts[1:]:
        m = re.match(r"^### (.+?)\n", part)
        if m:
            sections.append((m.group(1).strip(), part))
    return header, sections


def should_move_from_other(title: str, body: str) -> bool:
    combined = title + " " + body[:500]
    for pat in ROUTE_TO_LINGGAN:
        if re.search(pat, title, re.IGNORECASE) or re.search(pat, combined, re.IGNORECASE):
            return True
    return False


def should_move_from_motion(title: str, body: str) -> bool:
    combined = title + body[:300]
    return any(re.search(p, combined, re.IGNORECASE) for p in INSPIRATION_FROM_MOTION)


def main():
    # Current 灵感网站 (restored, 81 entries)
    insp_path = WIKI / "灵感网站.md"
    iheader, isections = parse_sections(insp_path.read_text(encoding="utf-8"))
    existing = {t for t, _ in isections}

    to_append = []

    # From git 其他资源
    _, osections = parse_sections(git_show("wiki/design/其他资源.md"))
    for title, section in osections:
        if title in existing:
            continue
        if should_move_from_other(title, section):
            to_append.append(section)
            existing.add(title)

    # From git 动效与加载
    _, msections = parse_sections(git_show("wiki/design/动效与加载.md"))
    for title, section in msections:
        if title in existing:
            continue
        if should_move_from_motion(title, section):
            to_append.append(section)
            existing.add(title)

    new_count = len(isections) + len(to_append)
    iheader = iheader.replace("# 作品集-灵感网站", "# 灵感网站")
    iheader = re.sub(r"> \d+ moonvy", f"> {new_count} moonvy", iheader, count=1)
    iheader = re.sub(r"共 \d+ 个", f"共 {new_count} 个", iheader)

    insp_path.write_text(iheader + "".join(s for _, s in isections) + "".join(to_append), encoding="utf-8")
    print(f"灵感网站: {len(isections)} + {len(to_append)} = {new_count}")


if __name__ == "__main__":
    main()
