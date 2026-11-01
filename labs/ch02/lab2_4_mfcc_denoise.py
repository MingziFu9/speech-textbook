"""实验 2-4（选做）提取 MFCC 并降噪：画出梅尔频谱和 MFCC，用 noisereduce 给带噪声的来电降噪。"""
import sys

import librosa
import librosa.display
import matplotlib.pyplot as plt
import noisereduce as nr
import numpy as np
import pandas as pd

sys.path.append("..")
from voicelab import cer, read_audio, save_audio, transcribe

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]

y, sr = read_audio("../data/calls/call_05.wav")             # 有背景噪声的那段
truth = pd.read_csv("../data/calls/calls.csv").set_index("文件").loc["call_05.wav", "文字"]
snr = 0  # ← 改这里：信噪比（分贝），越小噪声越大，试试 10、5、-5
rng = np.random.default_rng(0)
noise = rng.standard_normal(len(y)).astype(np.float32)
noise *= np.sqrt(np.mean(y ** 2) / np.mean(noise ** 2) / 10 ** (snr / 10))   # 按信噪比调整噪声的大小
y = y + noise                                               # 再加一层更大的噪声
save_audio("call_05_noisy.wav", y, sr)

mel = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=400, hop_length=160, n_mels=80)   # 25 毫秒一帧，10 毫秒一步
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=400, hop_length=160)
print("梅尔频谱：", mel.shape, "（80 个频带 × 帧数）")
print("MFCC：    ", mfcc.shape, "（13 个系数 × 帧数）")

clean = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.9)     # ← 改这里：0.5 降一半噪声，1.0 尽量全降
save_audio("call_05_denoised.wav", clean, sr)
for name, x in [("降噪前", y), ("降噪后", clean)]:
    text = transcribe(x, sr)
    print(f"{name}：字错率 {cer(truth, text)[0]:.0%}  {text}")

fig, axes = plt.subplots(1, 4, figsize=(18, 3.5))
for ax, data, title in [(axes[0], librosa.power_to_db(mel, ref=np.max), "梅尔频谱"), (axes[1], mfcc, "MFCC")]:
    librosa.display.specshow(data, sr=sr, hop_length=160, x_axis="time", ax=ax)
    ax.set_title(title)
for ax, x, title in [(axes[2], y, "降噪前语谱图"), (axes[3], clean, "降噪后语谱图")]:
    librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(x)), ref=np.max), sr=sr,
                             x_axis="time", y_axis="hz", ax=ax)
    ax.set_title(title)
plt.tight_layout()
plt.savefig("mfcc_denoise.png", dpi=120)
print("已保存 mfcc_denoise.png")
