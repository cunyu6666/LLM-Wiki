#!/usr/bin/env python3
"""
Polish Douyin video transcripts for readability.

Uses LLM to add punctuation, paragraph breaks, and fix ASR errors
while preserving the original oral/conversational style.

Usage:
    python3 scripts/polish-transcripts.py                    # dry run, show stats
    python3 scripts/polish-transcripts.py --apply             # actually process
    python3 scripts/polish-transcripts.py --apply --limit 10  # process first 10 only
    python3 scripts/polish-transcripts.py --force             # reprocess already done
"""

import re
import os
import sys
import json
import time
import argparse
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────
RAW_DIR = Path(__file__).resolve().parent.parent / "raw" / "来自抖音"
PROGRESS_FILE = Path(__file__).resolve().parent.parent / ".transcript-polish-progress.json"

# LLM config — defaults to Anthropic Claude, override with env vars
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "anthropic")  # "anthropic" or "openai"
ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o")
MAX_TOKENS = 1024

# ── Prompt ──────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """你是一个中文文字稿整理助手。你的任务是优化抖音视频的语音转文字稿，使其更易读。

规则：
1. 添加正确的中文标点符号（，。！？、：；——……等）
2. 按话题/段落自然分段，每段3-5句话
3. 修正明显的语音识别错误（只改你有把握的，不确定就保留原文）
4. 去除无意义的语气词和重复（如"对吧对吧"、"那个那个"）
5. 保留原始口语风格和说话人的语气，不要书面化重写
6. 不要添加原文中没有的内容
7. 不要改变原意

输出格式：
- 只输出整理后的文字稿正文
- 不要加标题、编号、markdown格式
- 不要加任何说明或注释"""


def get_transcript(content: str) -> str | None:
    """Extract transcript section from a raw .md file."""
    m = re.search(r"## 文字稿\n\n(.+?)(?:\n\n\[\[原始视频\]|\Z)", content, re.DOTALL)
    if not m:
        return None
    text = m.group(1).strip()
    # Filter out garbage transcripts
    if len(text) < 20:
        return None
    if text.startswith("字幕志愿者"):
        return None
    if "优优独播剧场" in text:
        return None
    return text


def replace_transcript(content: str, new_text: str) -> str:
    """Replace the transcript section in the raw .md file."""
    pattern = r"(## 文字稿\n\n).+?(\n\n\[\[原始视频\])"
    replacement = f"\\g<1>{new_text}\\2"
    return re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)


def call_anthropic(text: str) -> str:
    """Call Anthropic Claude API."""
    import anthropic
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def call_openai(text: str) -> str:
    """Call OpenAI API."""
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def polish_transcript(text: str) -> str:
    """Send transcript to LLM for polishing."""
    if LLM_PROVIDER == "anthropic":
        return call_anthropic(text)
    elif LLM_PROVIDER == "openai":
        return call_openai(text)
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {LLM_PROVIDER}")


def load_progress() -> dict:
    """Load processing progress from disk."""
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {}


def save_progress(progress: dict):
    """Save processing progress to disk."""
    PROGRESS_FILE.write_text(json.dumps(progress, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Polish Douyin transcripts")
    parser.add_argument("--apply", action="store_true", help="Actually process files (default: dry run)")
    parser.add_argument("--limit", type=int, default=0, help="Max files to process (0=all)")
    parser.add_argument("--force", action="store_true", help="Reprocess already-done files")
    parser.add_argument("--provider", default=None, help="Override LLM provider (anthropic/openai)")
    args = parser.parse_args()

    global LLM_PROVIDER
    if args.provider:
        LLM_PROVIDER = args.provider

    progress = load_progress()
    files = sorted(RAW_DIR.glob("*.md"))
    print(f"Found {len(files)} raw .md files")

    # Scan all files for valid transcripts
    candidates = []
    skipped_empty = 0
    skipped_garbage = 0
    skipped_done = 0

    for f in files:
        content = f.read_text(encoding="utf-8", errors="ignore")
        transcript = get_transcript(content)
        if transcript is None:
            skipped_empty += 1
            continue
        if f.name in progress and not args.force:
            skipped_done += 1
            continue
        candidates.append((f, transcript, content))

    print(f"\nScan results:")
    print(f"  Valid transcripts: {len(candidates)}")
    print(f"  Empty/garbage:     {skipped_empty}")
    print(f"  Already processed: {skipped_done}")

    if not candidates:
        print("\nNothing to process.")
        return

    if args.limit > 0:
        candidates = candidates[:args.limit]

    print(f"\n{'[DRY RUN] ' if not args.apply else ''}Will process {len(candidates)} files")
    print(f"Provider: {LLM_PROVIDER} | Model: {ANTHROPIC_MODEL if LLM_PROVIDER == 'anthropic' else OPENAI_MODEL}")

    if not args.apply:
        # Show a sample
        sample_file, sample_text, _ = candidates[0]
        print(f"\n--- Sample (first 500 chars of {sample_file.name}) ---")
        print(sample_text[:500])
        print(f"\nRun with --apply to actually process files.")
        return

    # Process files
    success = 0
    errors = 0
    for i, (f, transcript, content) in enumerate(candidates):
        print(f"\n[{i+1}/{len(candidates)}] {f.name[:60]}...")
        try:
            polished = polish_transcript(transcript)
            new_content = replace_transcript(content, polished)
            f.write_text(new_content, encoding="utf-8")
            progress[f.name] = {
                "status": "done",
                "original_len": len(transcript),
                "polished_len": len(polished),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            save_progress(progress)
            success += 1
            print(f"  ✅ {len(transcript)} → {len(polished)} chars")
            # Rate limit: 1 req/sec
            time.sleep(1)
        except Exception as e:
            errors += 1
            progress[f.name] = {"status": "error", "error": str(e)}
            save_progress(progress)
            print(f"  ❌ {e}")

    print(f"\n{'='*50}")
    print(f"Done! Success: {success} | Errors: {errors}")
    print(f"Progress saved to {PROGRESS_FILE}")


if __name__ == "__main__":
    main()
