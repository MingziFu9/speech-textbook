"""实验 2-2 采样率听一听：把一段 44.1 kHz 的讲话降到 16、8、4 kHz，比较文件大小、语谱图和识别结果。"""
import os
import sys

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from voicelab import read_audio, save_audio, transcribe

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]

original, sr0 = read_audio("../data/sounds/speech_44k.wav", sr=None)   # sr=None：保持原来的采样率
rates = [44100, 16000, 8000, 4000, 2000]                                # ← 改这里：试试 1000、22050

fig, axes = plt.subplots(1, len(rates), figsize=(18, 3.5), sharey=True)
for ax, sr in zip(axes, rates):
    y = librosa.resample(original, orig_sr=sr0, target_sr=sr) if sr != sr0 else original
    file = f"speech_{sr // 1000}k.wav"
    save_audio(file, y, sr)
    kb = os.path.getsize(file) / 1024
    print(f"{sr:>6} Hz：{len(y):>7} 个采样点，文件 {kb:6.1f} KB，最高能表示 {sr // 2:>5} Hz 识别：{transcribe(y, sr)}")
    spec = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=1024)), ref=np.max)
    librosa.display.specshow(spec, sr=sr, x_axis="time", y_axis="hz", ax=ax)
    ax.set_ylim(0, 22050)
    ax.set_title(f"{sr} Hz")
plt.tight_layout()
plt.savefig("sample_rates.png", dpi=120)
print("已保存 sample_rates.png")
