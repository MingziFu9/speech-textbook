"""实验 6-1 一个模型多种声音：用 174 个说话人的 VITS 模型挑音色、调语速，并和 Kokoro 对比。

运行：在 labs/ch06 文件夹里  python lab6_1_voices.py
需要模型：python models.py vits-aishell3 kokoro
"""
import sys

import librosa
import numpy as np

sys.path.append("..")
from voicelab import save_audio, speak

text = "各位居民请注意，下周六上午九点，社区在中心广场组织消防演练，欢迎大家参加。"   # ← 改这里


def pitch(audio, sr):
    """平均音高（基频，Hz）：女声一般在 180—300，男声一般在 90—160"""
    f0, voiced, _ = librosa.pyin(audio, fmin=60, fmax=500, sr=sr)
    return np.nanmean(f0[voiced])


print("== 第 1 步：VITS AISHELL-3，同一句话换 8 个说话人 ==")
for sid in [0, 10, 30, 50, 70, 100, 130, 160]:              # ← 改这里：0—173 任选
    audio, sr = speak(text, model="vits-aishell3", sid=sid)
    save_audio(f"aishell3_{sid}.wav", audio, sr)
    print(f"说话人 {sid:>3}  时长 {len(audio) / sr:5.2f} 秒  平均音高 {pitch(audio, sr):5.0f} Hz  采样率 {sr}")

print("\n== 第 2 步：调语速（第 10 号说话人）==")
for speed in [0.8, 1.0, 1.2, 1.5]:                          # ← 改这里
    audio, sr = speak(text, model="vits-aishell3", sid=10, speed=speed)
    save_audio(f"speed_{speed}.wav", audio, sr)
    print(f"语速 {speed}  时长 {len(audio) / sr:5.2f} 秒  平均音高 {pitch(audio, sr):5.0f} Hz")

print("\n== 第 3 步：Kokoro 的中文音色（3—57 女声，58—102 男声）==")
for sid in [20, 45, 65, 85]:
    audio, sr = speak(text, model="kokoro", sid=sid)
    save_audio(f"kokoro_{sid}.wav", audio, sr)
    print(f"音色 {sid:>3}  时长 {len(audio) / sr:5.2f} 秒  平均音高 {pitch(audio, sr):5.0f} Hz  采样率 {sr}")
