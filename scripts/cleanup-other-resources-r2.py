#!/usr/bin/env python3
"""P2 round 2: Further cleanup of 其他资源.md."""

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki" / "design"

DELETE_PATTERNS = [
    r"^---$", r"Notion 1亿", r"Notion 支持",
    r"^推荐关注$", r"^文章封面", r"^文章头图",
]

# (title_regex, body_regex_or_None, target) — first match wins
ROUTES = [
    # noise / dup
    (r"2025 年主流设计交付工具", None, "DELETE_DUP"),
    # industry
    (r"(挖掘 Shopify|设计交付工具|小道消息.*Figma|Figma (Config|数据库|博客|收购)|Sidebar 宣布|人工智能 \+ 设计|UI 界面设计中的思考|无标签设计|谷歌产品墓碑|CMA 搁置|前端开发者.*调研|Frame 和 Group)", None, "行业案例与趋势.md"),
    (r"(歸藏.*AI|Trae 上线|Gpt-4o)", None, "行业案例与趋势.md"),
    # inspiration
    (r"(设计欣赏|设计案例分享|网店设计|网页设计欣赏|GLEEC|在线体验|Infinite Mac|诺基亚.*怀旧|手绘小鱼|桌面风格|复古风|集体创作|工程师个人网站|1000个鼓舞|设计师社区|用户体验文章|艺术家作品|摄影博客|卢浮宫|陈幼坚|Shyrism|创作者社区|Muse Art|日本网站设计|极简风格交互|有趣的按钮收集|特斯拉中控|游戏数字化|摩托罗拉概念|探索宝丽来|网店设计|手绘漫画风|复古风门户|可交互的网站，爱尔兰)", None, "灵感网站.md"),
    (r"(可交互概率论|可交互的文字游戏|陌生人闹钟|手绘小鱼的在线鱼缸|美好的.时间|画正方形)", None, "灵感网站.md"),
    # ui template
    (r"(Edicus|音乐类应用设计概念|移动设备导航栏|UI UX 资源|微软新发布两个设计资源|Windowkill|小部件设计组件|徽章设计|APP 设计 UI|B端.*组件|Figma.*鼠标指针|Figma 按钮合集|流程图素材|iOS 键盘|Switch Button|干净简洁的移动端原型|深色色系.*便当|黑色风格.*便当|UI 卡片设计|原型组件包|租赁应用|地铁出行 APP|健身类型 UI|宠物网站设计|科技感网站设计文件|优秀网页设计，数据分析)", None, "UI模板与设计系统.md"),
    (r"(4 月份 Figma|Figma 仿长虹玻璃|Figma 绘制幽灵猫|Figma 原型小游戏|Figma 最新原型|Figma 文本变换|Figma 彩色胶条|Figma 2022.*中断|Figma 键盘快捷键)", None, "UI模板与设计系统.md"),
    # ai tools
    (r"(即梦 AI|倒置 AI 图像|Stable Diffusion|Midjourney 网页版|AI 评论生成|AI 吐槽|CommentFast|嘴替|海绵音乐|AI\.com)", None, "AI应用.md"),
    # illustration / assets
    (r"(包装图形|万圣节素材|抽象图形|抽象泡泡|1785 个 Memoji|一组高清图片|使用文字拼成|水彩风格.*封面|以前旧版本.*印刷)", None, "插画.md"),
    (r"(移动设备导航栏|导航栏样式)", None, "UI模板与设计系统.md"),
    (r"(构建颜色系统|Tweakcn)", None, "图库与配色.md"),
    (r"(Framer 基础知识|Framer 汉化|Framer Meetups|每个交互设计师都应该观看)", None, "教程与复刻.md"),
    (r"(她的数字化物品|数字化物品)", None, "灵感网站.md"),
    (r"(火狐浏览器吉祥物|柴猫表情包|Emoji 大全|Emoji 运算)", None, "图标.md"),
    (r"(一款颜值很高的相机|StrongMe|BananaBin|MyKeymap|site2pdf|Pixcall|MuseDAM|竹白百科|休闲娱乐文案)", None, "DELETE"),
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


def classify(title: str, body: str) -> str | None:
    for pat in DELETE_PATTERNS:
        if re.search(pat, title + body[:200], re.IGNORECASE):
            return "DELETE"
    for title_pat, body_pat, target in ROUTES:
        if re.search(title_pat, title, re.IGNORECASE):
            return target
        if body_pat and re.search(body_pat, body[:500], re.IGNORECASE):
            return target
    return None


def update_header(header: str, count: int, name: str) -> str:
    header = re.sub(r"> \d+ moonvy", f"> {count} moonvy", header, count=1)
    header = re.sub(r"共 \d+ 个", f"共 {count} 个", header)
    return header


def main():
    src = WIKI / "其他资源.md"
    header, sections = parse_sections(src.read_text(encoding="utf-8"))
    kept, deleted, moved = [], [], {}

    seen_titles = set()
    for title, section in sections:
        if title in seen_titles:
            deleted.append(title)
            continue
        seen_titles.add(title)

        target = classify(title, section)
        if target == "DELETE" or target == "DELETE_DUP":
            if target == "DELETE_DUP" and title in seen_titles:
                pass
            deleted.append(title)
        elif target:
            moved.setdefault(target, []).append(section)
        else:
            kept.append(section)

    # Handle DELETE_DUP: only delete second occurrence of 2025设计交付工具
    # Re-parse with smarter dup handling
    kept, deleted, moved = [], [], {}
    seen = {}
    for title, section in sections:
        target = classify(title, section)
        if target == "DELETE_DUP":
            seen[title] = seen.get(title, 0) + 1
            if seen[title] > 1:
                deleted.append(title)
                continue
            target = "行业案例与趋势.md"
        if target == "DELETE":
            deleted.append(title)
            continue
        if target:
            moved.setdefault(target, []).append(section)
        else:
            kept.append(section)

    new_header = update_header(header, len(kept), "其他资源")
    src.write_text(new_header + "\n".join(kept) if kept else new_header + "\n\n## 条目\n\n_剩余未归类实验性条目。_\n", encoding="utf-8")

    for target, secs in moved.items():
        tpath = WIKI / target
        tcontent = tpath.read_text(encoding="utf-8")
        theader, tsections = parse_sections(tcontent)
        existing = {t for t, _ in tsections}
        new_secs = []
        for s in secs:
            m = re.match(r"^### (.+?)\n", s)
            if m and m.group(1).strip() not in existing:
                new_secs.append(s)
                existing.add(m.group(1).strip())
        if not new_secs:
            continue
        new_count = len(tsections) + len(new_secs)
        theader = update_header(theader, new_count, target)
        tpath.write_text(theader + "".join(s for _, s in tsections) + "".join(new_secs), encoding="utf-8")

    print(f"R2: {len(sections)} → kept {len(kept)}, moved {sum(len(v) for v in moved.values())}, deleted {len(deleted)}")
    for t, s in sorted(moved.items()):
        print(f"  → {t}: +{len(s)}")


if __name__ == "__main__":
    main()
