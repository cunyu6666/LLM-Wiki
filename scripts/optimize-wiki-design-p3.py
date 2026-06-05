#!/usr/bin/env python3
"""P3 wiki/design optimization: dedupe, format, fix links, sync counts."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / "wiki" / "design"

MOONVY_CATALOGS = [
    "图标.md", "插画.md", "3D模型.md", "字体.md", "背景与渐变.md",
    "SVG素材.md", "材质与拟物.md", "UI模板与设计系统.md",
    "Figma技巧与插件.md", "图库与配色.md", "免费资源.md",
    "灵感网站.md", "动效灵感.md", "数据与可视化.md", "教程与复刻.md",
    "作品集.md", "AI应用.md", "硬件项目.md", "其他资源.md",
]

SEE_ALSO_OLD = "./作品集与灵感.md"
SEE_ALSO_NEW = "./作品集.md"


def fix_see_also_links():
    fixed = []
    for path in DESIGN.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if SEE_ALSO_OLD not in text:
            continue
        new_text = text.replace(
            f"- [作品集与灵感]({SEE_ALSO_OLD})",
            f"- [作品集]({SEE_ALSO_NEW})",
        )
        path.write_text(new_text, encoding="utf-8")
        fixed.append(path.name)
    return fixed


def extract_week(title_block: str) -> str:
    m = re.search(r"周刊\s*#(\d+)", title_block)
    return m.group(1) if m else ""


def primary_url(body: str) -> str:
    for m in re.finditer(r"\[https?://[^\]]+\]\((https?://[^)]+)\)", body):
        return m.group(1).split("?")[0].rstrip("/")
    for m in re.finditer(r"(?<![(\[])(https?://[^\s)]+)", body):
        return m.group(1).split("?")[0].rstrip("/")
    return ""


def parse_entries(content: str) -> tuple[str, list[dict], str]:
    idx = content.find("\n## 条目\n")
    if idx == -1:
        return content, [], ""
    header = content[: idx + len("\n## 条目\n")]
    body = content[idx + len("\n## 条目\n") :]
    see_idx = body.find("\n## See Also")
    tail = body[see_idx:] if see_idx != -1 else ""
    if see_idx != -1:
        body = body[:see_idx]
    parts = re.split(r"(?=^### )", body, flags=re.MULTILINE)
    entries = []
    for part in parts:
        part = part.strip("\n")
        if not part.startswith("### "):
            continue
        lines = part.split("\n", 1)
        title = lines[0][4:].strip()
        rest = lines[1] if len(lines) > 1 else ""
        entries.append({"title": title, "body": rest.strip()})
    return header, entries, tail


def dedupe_moonvy_file(path: Path) -> int:
    content = path.read_text(encoding="utf-8")
    if "\n## 条目\n" not in content:
        text = normalize_whitespace(content)
        if text != content:
            path.write_text(text, encoding="utf-8")
        return 0

    prefix_end = content.index("\n## 条目\n") + len("\n## 条目\n")
    prefix = content[:prefix_end]
    header, entries, tail = parse_entries(content)
    if not entries:
        normalize_moonvy_formatting(path)
        return 0

    seen_url: set[str] = set()
    seen_title_url: set[tuple[str, str]] = set()
    seen_titles: set[str] = set()
    out = []
    removed = 0

    for e in entries:
        url = primary_url(e["body"])
        plugin_m = re.search(r"figma\.com/community/plugin/\d+", e["body"])
        product_key = plugin_m.group(0) if plugin_m else url
        key = (e["title"], product_key or url)

        if e["title"] in seen_titles:
            removed += 1
            continue
        if product_key and key in seen_title_url:
            removed += 1
            continue
        if url and key in seen_title_url:
            removed += 1
            continue

        if product_key:
            seen_title_url.add(key)
        elif url:
            seen_title_url.add((e["title"], url))
            seen_url.add(url)

        seen_titles.add(e["title"])

        title = e["title"]
        week = extract_week(e["body"][:200])
        generic = {
            "免费图标库", "免费的 3D 素材", "优秀网站欣赏", "网页设计欣赏",
            "关于封面", "背景图案素材", "矢量插画", "Midjourney 样式分享",
        }
        if title in generic and week and f"#{week}" not in title:
            title = f"{title}（周刊 #{week}）"

        out.append({"title": title, "body": e["body"]})

    new_content = rebuild_catalog(header, out, tail)
    path.write_text(new_content, encoding="utf-8")
    update_entry_count(path, len(out))
    return removed


def rebuild_catalog(header: str, entries: list, tail: str) -> str:
    blocks = [f"### {e['title']}\n\n{e['body']}".strip() for e in entries]
    body = "\n\n".join(blocks)
    result = header + body
    if tail.strip():
        result += "\n\n" + tail.strip() + "\n"
    return normalize_whitespace(result)


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"\n---\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def update_entry_count(path: Path, count: int):
    text = path.read_text(encoding="utf-8")
    name = path.stem
    # update blockquote count line
    if name == "3D模型":
        # preserve compiled section count
        text = re.sub(
            r"^> \d+ moonvy.*$",
            f"> {count} moonvy 设计素材周刊条目 + 7 抖音编译",
            text,
            count=1,
            flags=re.M,
        )
        text = re.sub(
            r"共 \d+ 个「3D模型」",
            f"共 {count} 个「3D模型」",
            text,
            count=1,
        )
    else:
        text = re.sub(
            r"^> \d+ moonvy.*$",
            f"> {count} moonvy 设计素材周刊条目",
            text,
            count=1,
            flags=re.M,
        )
        cat = name
        text = re.sub(
            rf"共 \d+ 个「{re.escape(cat)}」",
            f"共 {count} 个「{cat}」",
            text,
            count=1,
        )
    path.write_text(text, encoding="utf-8")


def normalize_moonvy_formatting(path: Path):
    text = path.read_text(encoding="utf-8")
    new_text = normalize_whitespace(text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")


def dedupe_industry_raw_blocks(path: Path) -> int:
    """Remove duplicate raw source blocks (same ../../raw/ path) keeping first."""
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(- \[[^\]]+\]\(\.\./\.\./raw/[^)]+\)\n\n(?:> .+\n)*(?:!\[[^\]]*\]\([^)]+\)\n?)*)",
        re.MULTILINE,
    )
    seen: set[str] = set()
    removed = 0

    def repl(m):
        nonlocal removed
        block = m.group(1)
        url_m = re.search(r"\(\.\./\.\./raw/[^)]+\)", block)
        if not url_m:
            return block
        key = url_m.group(0)
        if key in seen:
            removed += 1
            return ""
        seen.add(key)
        return block

    new_text = pattern.sub(repl, text)
    new_text = normalize_whitespace(new_text)
    if removed:
        path.write_text(new_text, encoding="utf-8")
    return removed


def count_headings(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if path.name == "作品集.md":
        paths = set(re.findall(r"\(\.\./\.\./raw/[^)]+\)", text))
        return len(paths)
    if path.name == "3D模型.md":
        # count only moonvy 条目 section
        m = re.search(r"## 条目\n(.*)", text, re.DOTALL)
        if m:
            section = m.group(1).split("## See Also")[0]
            return len(re.findall(r"^### ", section, re.M))
    if path.name == "抖音设计短视频.md":
        return len(re.findall(r"^### ", text, re.M))
    m = re.search(r"## 条目\n(.*)", text, re.DOTALL)
    if m:
        return len(re.findall(r"^### ", m.group(1).split("## See Also")[0], re.M))
    return len(re.findall(r"^### ", text, re.M))


def sync_index_tables():
    index_path = ROOT / "wiki" / "index.md"
    resource_path = DESIGN / "设计资源.md"
    counts = {}
    for fn in MOONVY_CATALOGS + ["抖音设计短视频.md"]:
        p = DESIGN / fn
        if p.exists():
            counts[fn.replace(".md", "")] = count_headings(p)

    # update 设计资源.md table rows
    res_text = resource_path.read_text(encoding="utf-8")

    def replace_count(text, article, n):
        return re.sub(
            rf"(\[{re.escape(article)}\]\({re.escape(article)}\.md\) \| )\d+",
            rf"\g<1>{n}",
            text,
        )

    mapping = {
        "图标": counts.get("图标"),
        "插画": counts.get("插画"),
        "3D模型": counts.get("3D模型"),
        "字体": counts.get("字体"),
        "背景与渐变": counts.get("背景与渐变"),
        "SVG素材": counts.get("SVG素材"),
        "材质与拟物": counts.get("材质与拟物"),
        "UI模板与设计系统": counts.get("UI模板与设计系统"),
        "Figma技巧与插件": counts.get("Figma技巧与插件"),
        "图库与配色": counts.get("图库与配色"),
        "免费资源": counts.get("免费资源"),
        "灵感网站": counts.get("灵感网站"),
        "动效灵感": counts.get("动效灵感"),
        "数据与可视化": counts.get("数据与可视化"),
        "教程与复刻": counts.get("教程与复刻"),
        "作品集": counts.get("作品集"),
        "AI应用": counts.get("AI应用"),
        "硬件项目": counts.get("硬件项目"),
        "其他资源": counts.get("其他资源"),
        "抖音设计短视频": counts.get("抖音设计短视频"),
    }
    for art, n in mapping.items():
        if n is not None:
            res_text = replace_count(res_text, art, n)

    resource_path.write_text(res_text, encoding="utf-8")

    idx = index_path.read_text(encoding="utf-8")
    for art, n in mapping.items():
        if n is None or art == "3D模型":
            continue
        pat = rf"(\[{re.escape(art)}\]\(design/{re.escape(art)}\.md\) \| [^|]+ \| )\d+"
        idx = re.sub(pat, rf"\g<1>{n}", idx, count=1)
    # fix 3D model knowledge row separately
    n3d = counts.get("3D模型", 87)
    idx = re.sub(
        r"(\[3D模型\]\(design/3D模型\.md\) \| \*\*Spline 轻量 3D 工具编译\*\* \+ Moonvy 3D 素材目录 \| )[\d+\+]+",
        rf"\g<1>{n3d}+7",
        idx,
    )
    index_path.write_text(idx, encoding="utf-8")
    return counts


def main():
    see_fixed = fix_see_also_links()
    print(f"Fixed See Also links in: {see_fixed}")

    total_removed = 0
    for fn in MOONVY_CATALOGS:
        p = DESIGN / fn
        if not p.exists():
            continue
        normalize_moonvy_formatting(p)
        r = dedupe_moonvy_file(p)
        if r:
            print(f"  {fn}: removed {r} duplicate entries")
            total_removed += r

    industry_removed = dedupe_industry_raw_blocks(DESIGN / "行业案例与趋势.md")
    print(f"行业案例与趋势: removed {industry_removed} duplicate raw blocks")

    counts = sync_index_tables()
    print(f"Synced counts: {counts}")
    print(f"Total moonvy duplicates removed: {total_removed}")


if __name__ == "__main__":
    main()
