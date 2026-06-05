#!/usr/bin/env python3
"""P0: Clean up wiki/design/其他资源.md — remove noise, reclassify entries."""

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki" / "design"

NOISE_PATTERNS = [
    r"中奖", r"抽奖", r"特惠", r"招聘", r"推荐关注",
    r"文章封面来源", r"文章头图来源", r"愿你有走出困境",
    r"^---$",  # empty separators only
]

# (title_pattern, body_pattern, target_file) — first match wins
ROUTE_RULES = [
    (r"figma.*(按钮|组件|原型|源文件|规范|ui|贴纸|键盘|小游戏|计算器|钨丝|长虹玻璃|光标|文本变换|彩色胶条|幽灵猫|绘制)", None, "UI模板与设计系统.md"),
    (r"(按钮|组件|原型|ui文件|设计文件|小组件|widget|便当|bento|卡片设计|流程图|徽章|贴纸|ui规范|ui工具包|应用程序ui)", None, "UI模板与设计系统.md"),
    (r"(emoji|memoji|符号|glyphs|表情包|表情生成)", None, "图标.md"),
    (r"(插图|空状态|抽象图形|万圣节素材|泡泡.*素材|png素材)", None, "插画.md"),
    (r"(艺术字|文字效果|text effect)", None, "字体.md"),
    (r"(3d模型|抽象模型|小胖手模型)", None, "3D模型.md"),
    (r"(个人网站|网页设计|网站欣赏|网站设计|1000个鼓舞|设计师社区|导航站|在线体验.*mac|博物馆|考古|博客$|作品集)", None, "灵感网站.md"),
    (r"(配色|颜色系统|色板|构建颜色)", None, "图库与配色.md"),
    (r"(figma.*(插件|技巧|shortcut)|pie menu|sketch.*快捷)", None, "Figma技巧与插件.md"),
    (r"(midjourney|stable diffusion|ai.*工具|grok|runway|chatgpt|海绵音乐|commentfast|嘴替|niji)", None, "AI应用.md"),
    (r"(课程|培训|手册|framer.*课程|基础知识)", None, "教程与复刻.md"),
    (r"(加载动画|加载|动效|交互效果|可交互.*效果|滚动条|按钮交互|有声音交互)", None, "动效灵感.md"),
    (r"(数据可视化|年终报告|白皮书|figma config|收购案|权限 dsl)", None, "行业案例与趋势.md"),
    (r"(材质|长虹玻璃|投影)", None, "材质与拟物.md"),
    (r"(免费|开源)", None, "免费资源.md"),
    (r"(硬件|esp32|arduino|树莓)", None, "硬件项目.md"),
    (r"(数据大屏|可视化大屏)", None, "数据与可视化.md"),
]


def parse_sections(content: str) -> list[tuple[str, str]]:
    """Split article into (title, full_section) tuples."""
    parts = re.split(r"(?=^### )", content, flags=re.MULTILINE)
    header = parts[0]
    sections = []
    for part in parts[1:]:
        m = re.match(r"^### (.+?)\n", part)
        if m:
            sections.append((m.group(1).strip(), part))
    return header, sections


def is_noise(title: str, body: str) -> bool:
    combined = title + body
    for pat in NOISE_PATTERNS:
        if re.search(pat, combined, re.IGNORECASE):
            return True
    # Very short / empty body
    lines = [l for l in body.split("\n") if l.strip() and not l.startswith("> 来源")]
    if len(lines) <= 2:
        return True
    return False


def route_entry(title: str, body: str) -> str | None:
    combined = (title + " " + body[:500]).lower()
    for title_pat, body_pat, target in ROUTE_RULES:
        if re.search(title_pat, title, re.IGNORECASE) or (body_pat and re.search(body_pat, combined, re.IGNORECASE)):
            return target
    return None


def update_count(header: str, new_count: int, label: str) -> str:
    return re.sub(
        r"> \d+ moonvy 设计素材周刊条目",
        f"> {new_count} moonvy 设计素材周刊条目",
        header,
    ).replace(
        "共 285 个「其他资源」",
        f"共 {new_count} 个「其他资源」",
    ).replace(
        "共 63 个「动效与加载」",
        f"共 {new_count} 个「动效与加载」",
    )


def main():
    src_path = WIKI / "其他资源.md"
    content = src_path.read_text(encoding="utf-8")
    header, sections = parse_sections(content)

    kept = []
    deleted = []
    moved: dict[str, list[str]] = {}

    for title, section in sections:
        if is_noise(title, section):
            deleted.append(title)
            continue
        target = route_entry(title, section)
        if target:
            moved.setdefault(target, []).append(section)
        else:
            kept.append(section)

    # Write cleaned 其他资源
    new_header = update_count(header, len(kept), "其他资源")
    new_content = new_header + "\n".join(kept)
    if not kept:
        new_content = new_header.rstrip() + "\n\n## 条目\n\n_暂无条目，已全部重新归类或清理。_\n"
    src_path.write_text(new_content, encoding="utf-8")

    # Append moved sections to targets
    for target, secs in moved.items():
        tpath = WIKI / target
        if not tpath.exists():
            print(f"WARN: {target} not found, skipping {len(secs)} entries")
            continue
        tcontent = tpath.read_text(encoding="utf-8")
        theader, tsections = parse_sections(tcontent)
        existing_titles = {t for t, _ in tsections}
        new_secs = [s for s in secs if re.match(r"^### (.+?)\n", s).group(1).strip() not in existing_titles]
        if not new_secs:
            continue
        # Update count in header
        old_count_m = re.search(r"> (\d+)", theader)
        old_count = int(old_count_m.group(1)) if old_count_m else len(tsections)
        new_count = old_count + len(new_secs)
        theader = re.sub(r"> \d+.*", f"> {new_count} moonvy 设计素材周刊条目", theader, count=1)
        theader = re.sub(r"共 \d+ 个", f"共 {new_count} 个", theader)
        tpath.write_text(theader + "".join(s for _, s in tsections) + "".join(new_secs), encoding="utf-8")

    print(f"其他资源: {len(sections)} → kept {len(kept)}, moved {sum(len(v) for v in moved.values())}, deleted {len(deleted)}")
    for target, secs in sorted(moved.items()):
        print(f"  → {target}: +{len(secs)}")
    print(f"  deleted: {len(deleted)}")
    if deleted[:10]:
        print(f"  deleted samples: {deleted[:10]}")


if __name__ == "__main__":
    main()
