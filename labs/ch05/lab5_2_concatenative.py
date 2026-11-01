"""实验 5-2 拼接合成听“机器腔”：先做一个“单字录音库”，用单字拼出一句话，再和神经网络整句合成的同一句对比。

真实的拼接合成系统要请播音员录几个小时、成千上万个字和词。这里用合成模型逐字朗读来代替“播音员录单字”，
只为体会拼接的原理和问题。
"""
import sys

import librosa
import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from voicelab import cer, save_audio, speak, transcribe

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.rcParams["axes.unicode_minus"] = False
sentence = "欢迎各位居民参加社区活动"            # ← 改这里：换一句话（不要标点）

# 第 1 步：建“单字录音库”——每个字单独读一遍，剪掉前后的静音
library = {}
for ch in sorted(set(sentence)):
    samples, sr = speak(ch)
    samples, _ = librosa.effects.trim(samples, top_db=30)
    library[ch] = samples
print(f"单字录音库：{len(library)} 个字，采样率 {sr} Hz")

# 第 2 步：拼接——按顺序把单字接起来，接缝处用 10 毫秒淡入淡出，减少“咔哒”声
fade = int(0.01 * sr)
pieces = []
for ch in sentence:
    piece = library[ch].copy()
    piece[:fade] *= np.linspace(0, 1, fade)
    piece[-fade:] *= np.linspace(1, 0, fade)
    pieces.append(piece)
concat = np.concatenate(pieces)
save_audio("concat.wav", concat, sr)

# 第 3 步：神经网络整句合成
whole, _ = speak(sentence)
save_audio("whole.wav", whole, sr)

# 第 4 步：比较
for name, audio in [("拼接合成", concat), ("整句合成", whole)]:
    heard = transcribe(audio, sr)
    f0, voiced, _ = librosa.pyin(audio, fmin=80, fmax=500, sr=sr)
    print(f"{name}：时长 {len(audio) / sr:.2f} 秒，回识别 {heard}（字错率 {cer(sentence, heard)[0]:.0%}），"
          f"音高 {np.nanmin(f0):.0f}—{np.nanmax(f0):.0f} Hz")

fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharey=True)
for ax, (name, audio) in zip(axes, [("拼接合成（每个字都是单独读的）", concat), ("整句合成", whole)]):
    f0, _, _ = librosa.pyin(audio, fmin=80, fmax=500, sr=sr)
    t = librosa.times_like(f0, sr=sr)
    ax.plot(t, f0, linewidth=2)
    ax.set_title(name + "：音高曲线")
    ax.set_ylabel("音高（Hz）")
axes[1].set_xlabel("时间（秒）")
plt.tight_layout()
plt.savefig("concat_pitch.png", dpi=110)
print("已保存 concat.wav、whole.wav、concat_pitch.png")
