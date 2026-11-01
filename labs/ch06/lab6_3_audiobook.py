"""实验 6-3 社区有声广播：把一篇约 1500 字的告居民书做成带片头、句间停顿和 AI 标识的 MP3 有声书。

运行：在 labs/ch06 文件夹里  python lab6_3_audiobook.py
需要模型：python models.py matcha-zh kokoro sensevoice；需要 ffmpeg（见附录 B）
"""
import os
import re
import subprocess
import sys
import time

import librosa
import numpy as np
import soundfile as sf

sys.path.append("..")
from voicelab import speak, transcribe

SR = 24000                                              # 整本有声书统一用 24 kHz
BODY = ("matcha-zh", 0, 1.0)                            # 正文：(模型, 说话人, 语速)  ← 改这里
HEAD = ("kokoro", 58, 1.0)                              # 标题和 AI 提示：换一个声音，听得出层次
PAUSE = {"句": 0.35, "段": 0.8, "标题": 1.0}             # 停顿秒数  ← 改这里


def tts(text, voice):
    """合成一句话，统一采样率，并把音量调到差不多大（不同模型的音量不一样）"""
    model, sid, speed = voice
    text = text.replace("〇", "零")                     # Matcha 的词典里没有“〇”，会被跳过（编者运行时看到了警告）
    audio, sr = speak(text, model=model, sid=sid, speed=speed)
    audio = librosa.resample(audio, orig_sr=sr, target_sr=SR)
    return 0.1 * audio / (np.sqrt(np.mean(audio ** 2)) + 1e-9)


def silence(sec):
    return np.zeros(int(sec * SR), np.float32)


def chime():
    """片头提示音：三个渐弱的音（do、mi、sol），用 numpy 生成，没有版权问题"""
    notes = []
    for f in (523, 659, 784):
        t = np.arange(int(0.35 * SR)) / SR
        notes.append(0.25 * np.sin(2 * np.pi * f * t) * np.exp(-t * 6))
    return np.concatenate(notes).astype(np.float32)


def split_sentences(paragraph):
    """按句号、问号、感叹号、分号切句，标点留在句子末尾"""
    return [s for s in re.split(r"(?<=[。！？；])", paragraph) if s.strip()]


# 1. 读文章，分出标题、小标题和段落
lines = [x.strip() for x in open("../data/texts/winter_notice.txt", encoding="utf-8") if x.strip()]
title = lines[0].lstrip("# ")

# 2. 片头：提示音 + AI 合成提示（显式标识）+ 标题
start = time.time()
label = tts("本音频由人工智能语音合成。", HEAD)
print("AI 提示回识别：", transcribe(label, SR))             # 标识必须听得清，先用识别模型检查一遍
parts = [chime(), silence(0.5), label, silence(0.6),
         tts(title, HEAD), silence(PAUSE["标题"])]
chapters, n_sent = [], 0                                # chapters 记下每个小标题从第几秒开始

# 3. 逐段、逐句合成，加上停顿
for line in lines[1:]:
    if line.startswith("## "):
        chapters.append((sum(len(p) for p in parts) / SR, line[3:]))
        parts += [tts(line[3:], HEAD), silence(PAUSE["标题"])]
        continue
    for s in split_sentences(line):
        parts += [tts(s, BODY), silence(PAUSE["句"])]
        n_sent += 1
    parts.append(silence(PAUSE["段"]))
    print(f"已合成 {n_sent} 句，用时 {time.time() - start:.0f} 秒")
parts += [chime(), silence(0.5)]                         # 片尾再响一次提示音
book = np.concatenate(parts)
used = time.time() - start

# 4. 保存 WAV，再用 ffmpeg 转成 MP3；MP3 的“注释”里写上 AI 生成说明（隐式标识）
book = 0.9 * book / np.abs(book).max()                  # 整体归一化，防止削波
sf.write("winter_notice.wav", book, SR, subtype="PCM_16")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "winter_notice.wav", "-b:a", "64k",
                "-metadata", f"title={title}", "-metadata", "artist=幸福里社区居民委员会",
                "-metadata", "comment=AI生成：本音频由人工智能语音合成（Matcha-TTS、Kokoro）",
                "winter_notice.mp3"], check=True)

# 5. 写一份“目录”，方便居民跳到想听的部分
with open("winter_notice_目录.txt", "w", encoding="utf-8") as f:
    for sec, name in chapters:
        f.write(f"{int(sec // 60):02d}:{int(sec % 60):02d}  {name}\n")

dur = len(book) / SR
print(f"\n共 {n_sent} 句，时长 {int(dur // 60)} 分 {dur % 60:.0f} 秒，合成用时 {used:.0f} 秒，实时率 {used / dur:.2f}")
for name in ("winter_notice.wav", "winter_notice.mp3"):
    print(f"{name:<20} {sf.info(name).frames / SR:6.1f} 秒  {os.path.getsize(name) / 1024 / 1024:5.2f} MB")
print(open("winter_notice_目录.txt", encoding="utf-8").read())
