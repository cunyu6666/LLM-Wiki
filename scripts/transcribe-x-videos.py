#!/usr/bin/env python3
"""
从 X 视频中提取音频并转录为文字
使用 ffmpeg 提取音频，使用 Google Speech Recognition 转录
"""

import os
import json
import subprocess
from pathlib import Path

# 路径配置
BASE_DIR = Path(__file__).parent.parent
RAW_DIR = BASE_DIR / "raw"
VIDEOS_DIR = RAW_DIR / "x-videos"
AUDIO_DIR = RAW_DIR / "x-audio"
TRANSCRIPTS_DIR = RAW_DIR / "x-transcripts"

# 创建目录
AUDIO_DIR.mkdir(exist_ok=True)
TRANSCRIPTS_DIR.mkdir(exist_ok=True)

def extract_audio(video_path, audio_path):
    """使用 ffmpeg 提取音频（轻量模式）"""
    try:
        cmd = [
            "ffmpeg", "-i", str(video_path),
            "-vn",  # 不要视频
            "-acodec", "pcm_s16le",
            "-ar", "8000",  # 降低采样率到 8kHz
            "-ac", "1",  # 单声道
            "-y",
            str(audio_path)
        ]
        subprocess.run(cmd, capture_output=True, check=True, timeout=30)
        return True
    except subprocess.TimeoutExpired:
        print(f"提取超时: {video_path.name}")
        return False
    except subprocess.CalledProcessError as e:
        print(f"提取失败: {video_path.name}")
        return False

def transcribe_audio(audio_path):
    """使用 Google Speech Recognition 转录音频"""
    try:
        import speech_recognition as sr

        recognizer = sr.Recognizer()
        with sr.AudioFile(str(audio_path)) as source:
            audio = recognizer.record(source)

        # 使用 Google 免费 API
        text = recognizer.recognize_google(audio, language="zh-CN")
        return text
    except sr.UnknownValueError:
        return "[无法识别音频内容]"
    except sr.RequestError as e:
        return f"[语音识别服务错误: {e}]"
    except ImportError:
        return "[需要安装 speech_recognition: pip3 install SpeechRecognition]"

def process_video(video_file):
    """处理单个视频"""
    video_path = VIDEOS_DIR / video_file
    stem = video_path.stem

    # 检查是否已转录
    transcript_path = TRANSCRIPTS_DIR / f"{stem}.txt"
    if transcript_path.exists():
        print(f"跳过已转录: {stem}")
        return True

    # 提取音频
    audio_path = AUDIO_DIR / f"{stem}.wav"
    if not audio_path.exists():
        print(f"提取音频: {stem}")
        if not extract_audio(video_path, audio_path):
            return False

    # 转录
    print(f"转录中: {stem}")
    text = transcribe_audio(audio_path)

    # 保存转录结果
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"完成: {stem}")
    return True

def main():
    # 检查是否安装了 speech_recognition
    try:
        import speech_recognition
    except ImportError:
        print("需要安装 SpeechRecognition:")
        print("pip3 install SpeechRecognition")
        return

    # 获取所有视频文件
    video_files = [f for f in os.listdir(VIDEOS_DIR) if f.endswith(('.mp4', '.mov', '.avi', '.mkv'))]
    print(f"找到 {len(video_files)} 个视频文件\n")

    success_count = 0
    fail_count = 0

    for video_file in video_files:
        if process_video(video_file):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n转录完成: 成功 {success_count}，失败 {fail_count}")
    print(f"转录文件保存在: {TRANSCRIPTS_DIR}")

if __name__ == "__main__":
    main()
