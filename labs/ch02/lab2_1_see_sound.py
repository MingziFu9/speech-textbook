"""实验 2-1 看见声音：画出几种声音的波形图和语谱图。"""
import sys

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from voicelab import read_audio

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]  # 中文字体
plt.rcParams["axes.unicode_minus"] = False

names = {"vowel_a": "元音“啊”", "vowel_i": "元音“衣”", "vowel_u": "元音“乌”",
         "whistle": "口哨", "noise": "噪声", "knock": "敲门声"}

fig, axes = plt.subplots(2, len(names), figsize=(18, 6))
for col, (name, title) in enumerate(names.items()):
    samples, sr = read_audio(f"../data/sounds/{name}.wav")
    t = np.arange(len(samples)) / sr                          # 每个采样点对应的时间（秒）
    axes[0, col].plot(t, samples, linewidth=0.5)              # 上排：波形图
    axes[0, col].set_title(title)
    axes[0, col].set_xlabel("时间（秒）")
    spec = librosa.amplitude_to_db(np.abs(librosa.stft(samples, n_fft=512)), ref=np.max)
    librosa.display.specshow(spec, sr=sr, hop_length=128, x_axis="time", y_axis="hz", ax=axes[1, col])  # 下排：语谱图
    axes[1, col].set_xlabel("时间（秒）")
    axes[1, col].set_ylabel("")
    f0, voiced, _ = librosa.pyin(samples, fmin=60, fmax=2500, sr=sr)       # 估计音高（基频）
    pitch = f"{np.nanmedian(f0):.0f} Hz" if voiced.mean() > 0.3 else "没有明确音高"
    centroid = librosa.feature.spectral_centroid(y=samples, sr=sr).mean()   # 频谱重心：能量“平均”在多高的频率
    print(f"{title:<6} 时长 {len(samples) / sr:.2f} 秒，最大振幅 {np.abs(samples).max():.2f}，"
          f"音高 {pitch}，频谱重心 {centroid:.0f} Hz")
axes[0, 0].set_ylabel("振幅")
axes[1, 0].set_ylabel("频率（Hz）")
plt.tight_layout()
plt.savefig("see_sound.png", dpi=120)
print("已保存 see_sound.png")
