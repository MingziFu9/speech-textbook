"""实验 8-3 克隆像不像，并贴上标签：给克隆结果加开头语音提示（显式标识）、写入元数据（隐式标识）、嵌入并检测一个简单水印。

运行：先完成实验 8-2（要用到 clone_volunteer_B_1.wav），再在 labs/ch08 文件夹里  python lab8_3_label.py
需要模型：python models.py matcha-zh；需要 ffmpeg
"""
import json
import subprocess
import sys

import librosa
import numpy as np

sys.path.append("..")
from voicelab import read_audio, save_audio, speak
from watermark import detect_watermark, embed_watermark

KEY = 2026                                                     # 水印密钥，只有知道密钥的人能检测  ← 改这里
cloned, sr = read_audio("clone_volunteer_B_1.wav", sr=None)

# 1. 显式标识：开头加一句语音提示，用另一个声音（Matcha）说，和克隆的声音区分开
notice, nsr = speak("以下内容由人工智能合成。", model="matcha-zh")
notice = librosa.resample(notice, orig_sr=nsr, target_sr=sr)
labeled = np.concatenate([notice, np.zeros(int(0.5 * sr)), cloned]).astype(np.float32)

# 2. 水印：把密钥生成的微弱噪声铺进整段声音
marked = embed_watermark(labeled, sr, KEY)
save_audio("labeled.wav", marked, sr)

# 3. 隐式标识：用 ffmpeg 转成 MP3，元数据里写上生成合成属性、制作者、内容编号
meta = {"AIGC": "AI生成", "Producer": "某某学院-语音课程作业-学号20260001", "ContentID": "ch08-lab3-0001",
        "Model": "ZipVoice", "Voice": "虚拟授权人B（已授权）"}
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "labeled.wav", "-b:a", "64k",
                "-metadata", "comment=" + json.dumps(meta, ensure_ascii=False), "labeled.mp3"], check=True)
probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format_tags=comment", "-of", "default=nw=1:nk=1",
                        "labeled.mp3"], capture_output=True, text=True).stdout.strip()
print("MP3 里读出的隐式标识：", probe)

# 4. 检测水印：有水印、没水印、转成 MP3 后、用错密钥、B 的真实录音
mp3, msr = librosa.load("labeled.mp3", sr=sr)
real, rsr = read_audio("../data/voices/volunteer_B_3.wav", sr=None)
tests = [("加了水印的 WAV", marked, KEY), ("没加水印的克隆", labeled, KEY), ("转成 MP3 以后", mp3, KEY),
         ("用错误的密钥检测", marked, 1234), ("B 的真实录音", real, KEY)]
print("\n检测对象            得分    结论（得分 > 5 判为有水印）")
for name, audio, key in tests:
    score = detect_watermark(audio, sr, key)
    print(f"{name:<14}  {score:6.1f}    {'有水印' if score > 5 else '没有检测到'}")

# 5. 水印会不会影响听感？算一算水印比声音小多少分贝
noise = marked - labeled
print(f"\n水印能量比声音低 {10 * np.log10(np.mean(labeled ** 2) / np.mean(noise ** 2)):.0f} dB")
