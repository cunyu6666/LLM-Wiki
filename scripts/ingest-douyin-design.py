#!/usr/bin/env python3
"""Ingest design-related 抖音 raw files into wiki/design/抖音设计短视频.md."""

import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "来自抖音"
WIKI = ROOT / "wiki" / "design" / "抖音设计短视频.md"

CATEGORIES = [
    ("3D与建模", [r"3d", r"spline", r"c4d", r"blender", r"建模", r"渲染", r"ue5", r"虚幻"]),
    ("UI与交互", [r"ui设计", r"ux", r"交互", r"组件", r"b端", r"表单", r"步骤条", r"导航"]),
    ("动效与动画", [r"动效", r"动画", r"ae", r"motion", r"mg动画", r"微交互"]),
    ("品牌与平面", [r"logo", r"品牌", r"包装", r"平面", r"海报", r"字体设计", r"排版", r"酸性"]),
    ("AI设计", [r"\bai\b", r"midjourney", r"stable", r"aigc", r"gpt", r"生图", r"即梦"]),
    ("前端与代码", [r"css", r"前端", r"程序员", r"代码", r"html", r"react", r"tailwind"]),
    ("工具与教程", [r"figma", r"教程", r"技巧", r"工具", r"插件", r"设计师必"]),
    ("其他设计", [r"设计"]),
]


def categorize(text: str) -> str:
    lower = text.lower()
    for cat, patterns in CATEGORIES:
        if any(re.search(p, lower) for p in patterns):
            return cat
    return "其他设计"


def short_title(title: str, max_len: int = 48) -> str:
    """Strip hashtags/noise; keep readable ### heading."""
    t = re.sub(r"[@#][^\s#@]+", "", title)
    t = re.sub(r"\s+", " ", t).strip(" ·，,")
    if len(t) <= max_len:
        return t or title[:max_len]
    return t[: max_len - 1].rstrip() + "…"


def extract_transcript(content: str) -> str:
    m = re.search(r"## 文字稿\n\n(.+?)(?:\n\n\[原始视频\]|\Z)", content, re.DOTALL)
    if m:
        t = m.group(1).strip()
        return t[:200] + ("…" if len(t) > 200 else "")
    return ""


def main():
    entries = defaultdict(list)
    for f in sorted(RAW.glob("*.md")):
        content = f.read_text(encoding="utf-8", errors="ignore")
        # Parse metadata
        author_m = re.search(r'author: "(.+?)"', content)
        url_m = re.search(r'url: (.+)', content)
        title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
        if not title_m:
            continue
        title = title_m.group(1).strip()
        tags_m = re.search(r'tags: \[(.+?)\]', content)
        tag_str = tags_m.group(1) if tags_m else ""
        if "设计" not in tag_str and not any(
            kw in title.lower() for kw in ["设计", "ui", "ux", "figma", "3d", "动效", "logo", "品牌"]
        ):
            continue
        cat = categorize(title + " " + content[:200])
        transcript = extract_transcript(content)
        author = author_m.group(1) if author_m else "未知"
        url = url_m.group(1).strip() if url_m else ""
        rel = f"../../raw/来自抖音/{f.name}"
        entries[cat].append((title, author, url, rel, transcript))

    lines = [
        "# 抖音设计短视频",
        "",
        f"> {sum(len(v) for v in entries.values())} sources",
        "",
        "## Sources",
        "- 抖音设计类短视频文字稿 (2022-2026)",
        "",
        "## Raw Sources",
        f"- [来自抖音目录](../../raw/来自抖音/)",
        "",
        "## Overview",
        "",
        "设计相关抖音短视频的文字稿索引，按主题分类。视频文件保留在 raw/来自抖音/ 目录。",
        "",
    ]

    for cat, _ in CATEGORIES:
        if cat not in entries:
            continue
        lines.append(f"## {cat}")
        lines.append("")
        for title, author, url, rel, transcript in entries[cat]:
            lines.append(f"### {short_title(title)}")
            lines.append("")
            lines.append(f"> **{title}**")
            lines.append(f"> 作者：{author}")
            if url:
                lines.append(f"> 来源：[抖音]({url}) · [{rel}]({rel})")
            if transcript:
                lines.append("")
                lines.append(transcript)
            lines.append("")

    WIKI.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for v in entries.values())
    print(f"Created 抖音设计短视频.md: {total} entries")
    for cat, _ in CATEGORIES:
        if cat in entries:
            print(f"  {cat}: {len(entries[cat])}")


if __name__ == "__main__":
    main()
