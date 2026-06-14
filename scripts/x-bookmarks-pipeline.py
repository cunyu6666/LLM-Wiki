#!/usr/bin/env python3
"""
X (Twitter) 书签入库完整流程
参照抖音视频入库流程，适配 X 书签数据

流程：原始 JSON → .md 生成 → 音频转文字 → GIF 预览 → Wiki 编译
"""

import os
import json
import subprocess
import time
from pathlib import Path

# 路径配置
BASE_DIR = Path(__file__).parent.parent
RAW_DIR = BASE_DIR / "raw"
VIDEOS_DIR = RAW_DIR / "x-videos"
X_BOOKMARKS_DIR = RAW_DIR / "x-bookmarks"
GIFS_DIR = RAW_DIR / "x-bookmarks" / "gifs"
TRANSCRIPTS_DIR = RAW_DIR / "x-transcripts"

# Groq API 配置
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "whisper-large-v3-turbo"

def get_static_ffmpeg():
    """获取 static-ffmpeg 的 ffmpeg 路径"""
    try:
        import static_ffmpeg
        static_ffmpeg.add_paths()
        # ffmpeg 现在已经在 PATH 中了
        return "ffmpeg"
    except Exception as e:
        print(f"static-ffmpeg 初始化失败: {e}")
        return None

def load_bookmarks():
    """加载书签数据"""
    json_path = RAW_DIR / "x-bookmarks-2026-06-14.json"
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_md_files(bookmarks):
    """为每个书签生成 .md 文件"""
    X_BOOKMARKS_DIR.mkdir(exist_ok=True)

    for bookmark in bookmarks:
        tweet_id = bookmark.get("id", "")
        username = bookmark.get("username", "unknown")
        filename = f"{username}-{tweet_id}.md"
        filepath = X_BOOKMARKS_DIR / filename

        if filepath.exists():
            print(f"跳过已存在: {filename}")
            continue

        # 构建 frontmatter
        display_name = bookmark.get("displayName", username)
        text = bookmark.get("text", "").replace('"', '\\"')
        tweet_url = bookmark.get("tweetUrl", "")
        timestamp = bookmark.get("timestamp", "")
        time_text = bookmark.get("timeText", "")
        links = bookmark.get("links", [])
        images = bookmark.get("images", [])
        has_video = bookmark.get("videos", False)

        # 标签提取
        tags = ["x-bookmark"]
        if has_video:
            tags.append("video")

        # 生成 md 内容
        content = f"""---
id: "{tweet_id}"
source: "X (Twitter)"
author: "{display_name}"
username: "{username}"
url: {tweet_url}
date: "{timestamp}"
tags: {json.dumps(tags, ensure_ascii=False)}
---

# {display_name}

{text}

"""

        # 添加链接
        if links:
            content += "**链接：**\n"
            for link in links:
                content += f"- {link}\n"
            content += "\n"

        # 添加图片
        if images:
            content += f"**图片：** {len(images)} 张\n\n"

        # 添加视频嵌入
        video_file = VIDEOS_DIR / f"{username}-{tweet_id}.mp4"
        if video_file.exists():
            content += f"![[../../x-videos/{username}-{tweet_id}.mp4]]\n\n"
            content += f"[原始视频](../../x-videos/{username}-{tweet_id}.mp4) | [X 链接]({tweet_url})\n"
        elif has_video:
            content += f"[X 链接（含视频）]({tweet_url})\n"

        # 写入文件
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"已生成: {filename}")

def extract_audio(video_path, audio_path, ffmpeg_path):
    """使用 static-ffmpeg 提取音频"""
    try:
        cmd = [
            ffmpeg_path, "-i", str(video_path),
            "-vn",
            "-acodec", "libmp3lame",
            "-q:a", "4",
            "-y",
            str(audio_path)
        ]
        result = subprocess.run(cmd, capture_output=True, timeout=60)
        return result.returncode == 0
    except Exception as e:
        print(f"提取音频失败: {video_path.name} - {e}")
        return False

def transcribe_audio(audio_path):
    """使用 Groq Whisper API 转录音频"""
    if not GROQ_API_KEY:
        return "[需要设置 GROQ_API_KEY 环境变量]"

    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)

        with open(audio_path, "rb") as f:
            result = client.audio.transcriptions.create(
                file=(audio_path.name, f.read()),
                model=GROQ_MODEL,
                language="zh"
            )

        return result.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            print(f"Groq API 限流，等待 30 秒...")
            time.sleep(30)
            return transcribe_audio(audio_path)  # 重试
        return f"[转录失败: {error_msg}]"

def process_transcripts(bookmarks, ffmpeg_path):
    """处理所有视频的音频转录"""
    TRANSCRIPTS_DIR.mkdir(exist_ok=True)
    audio_dir = RAW_DIR / "x-audio"
    audio_dir.mkdir(exist_ok=True)

    for bookmark in bookmarks:
        tweet_id = bookmark.get("id", "")
        username = bookmark.get("username", "unknown")
        has_video = bookmark.get("videos", False)

        if not has_video:
            continue

        video_file = VIDEOS_DIR / f"{username}-{tweet_id}.mp4"
        if not video_file.exists():
            continue

        # 检查是否已转录
        transcript_file = TRANSCRIPTS_DIR / f"{username}-{tweet_id}.txt"
        if transcript_file.exists():
            print(f"跳过已转录: {username}-{tweet_id}")
            continue

        # 提取音频
        audio_file = audio_dir / f"{username}-{tweet_id}.mp3"
        if not audio_file.exists():
            print(f"提取音频: {username}-{tweet_id}")
            if not extract_audio(video_file, audio_file, ffmpeg_path):
                continue

        # 转录
        print(f"转录中: {username}-{tweet_id}")
        text = transcribe_audio(audio_file)

        # 保存转录
        with open(transcript_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"完成: {username}-{tweet_id}")

        # 更新 .md 文件，添加文字稿
        md_file = X_BOOKMARKS_DIR / f"{username}-{tweet_id}.md"
        if md_file.exists() and text and not text.startswith("["):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            if "## 文字稿" not in content:
                content += f"\n## 文字稿\n\n{text}\n"
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(content)

        # 清理音频文件节省空间
        if audio_file.exists():
            audio_file.unlink()

        # 限速
        time.sleep(2)

def generate_gifs(bookmarks, ffmpeg_path):
    """为视频生成 GIF 预览"""
    GIFS_DIR.mkdir(exist_ok=True)

    for bookmark in bookmarks:
        tweet_id = bookmark.get("id", "")
        username = bookmark.get("username", "unknown")
        has_video = bookmark.get("videos", False)

        if not has_video:
            continue

        video_file = VIDEOS_DIR / f"{username}-{tweet_id}.mp4"
        if not video_file.exists():
            continue

        gif_file = GIFS_DIR / f"{username}-{tweet_id}.gif"
        if gif_file.exists():
            print(f"跳过已有 GIF: {username}-{tweet_id}")
            continue

        print(f"生成 GIF: {username}-{tweet_id}")
        try:
            cmd = [
                ffmpeg_path, "-y", "-v", "warning",
                "-i", str(video_file),
                "-t", "8",
                "-vf", "fps=1.5,scale=240:-1:flags=lanczos",
                "-loop", "0",
                str(gif_file)
            ]
            subprocess.run(cmd, capture_output=True, timeout=30)
        except Exception as e:
            print(f"GIF 生成失败: {username}-{tweet_id} - {e}")

def update_md_with_gif(bookmarks):
    """更新 .md 文件，添加 GIF 预览"""
    for bookmark in bookmarks:
        tweet_id = bookmark.get("id", "")
        username = bookmark.get("username", "unknown")
        has_video = bookmark.get("videos", False)

        if not has_video:
            continue

        md_file = X_BOOKMARKS_DIR / f"{username}-{tweet_id}.md"
        gif_file = GIFS_DIR / f"{username}-{tweet_id}.gif"

        if not md_file.exists() or not gif_file.exists():
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        if "![" + f"[{username}-{tweet_id}.gif]" in content:
            continue

        # 在视频嵌入前添加 GIF 预览
        gif_embed = f"![{username}-{tweet_id}.gif](gifs/{username}-{tweet_id}.gif)\n\n"
        content = content.replace(
            f"![[{username}-{tweet_id}.mp4]]",
            f"{gif_embed}![[{username}-{tweet_id}.mp4]]"
        )

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"已更新 GIF: {username}-{tweet_id}")

def main():
    print("=" * 50)
    print("X 书签入库流程")
    print("=" * 50)

    # 检查依赖
    ffmpeg_path = get_static_ffmpeg()
    if not ffmpeg_path:
        print("错误: static-ffmpeg 未安装")
        return

    print(f"ffmpeg 路径: {ffmpeg_path}")

    # 加载书签
    bookmarks = load_bookmarks()
    print(f"共 {len(bookmarks)} 条书签")

    # 步骤 1: 生成 .md 文件
    print("\n[1/4] 生成 .md 文件...")
    generate_md_files(bookmarks)

    # 步骤 2: 音频转文字
    print("\n[2/4] 音频转文字...")
    if GROQ_API_KEY:
        process_transcripts(bookmarks, ffmpeg_path)
    else:
        print("跳过（未设置 GROQ_API_KEY）")

    # 步骤 3: 生成 GIF 预览
    print("\n[3/4] 生成 GIF 预览...")
    generate_gifs(bookmarks, ffmpeg_path)

    # 步骤 4: 更新 .md 文件
    print("\n[4/4] 更新 .md 文件...")
    update_md_with_gif(bookmarks)

    print("\n" + "=" * 50)
    print("完成！")
    print(f"文件位置: {X_BOOKMARKS_DIR}")
    print("=" * 50)

if __name__ == "__main__":
    main()
