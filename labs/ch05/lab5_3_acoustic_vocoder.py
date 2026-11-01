"""实验 5-3 拆开看声学模型和声码器：前端 → 声学模型画出梅尔频谱 → 两种声码器把同一张频谱变成声音，比较速度和效果。"""
import sys
import time

import librosa.display
import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from frontend import frontend
from tts_parts import SR, acoustic_model, vocoder
from voicelab import cer, save_audio, transcribe

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
text = "社区通知：本周六上午9:30，在3号楼前举行垃圾分类宣传活动，欢迎居民参加。"    # ← 改这里

# 第 1 步：文本前端（实验 5-1）
pinyin = frontend(text)
answer = "社区通知：本周六上午9点30分，在3号楼前举行垃圾分类宣传活动，欢迎居民参加。"   # 回识别的标准答案（按识别模型的写法）

# 第 2 步：声学模型 → 梅尔频谱
acoustic_model(pinyin)                                   # 先运行一次，把模型加载好
start = time.time()
mel = acoustic_model(pinyin)
t_am = time.time() - start
print(f"\n梅尔频谱：{mel.shape}（80 个频带 × {mel.shape[1]} 帧），声学模型用时 {t_am:.2f} 秒")

# 第 3 步：同一张频谱交给三个声码器
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
librosa.display.specshow(mel, sr=SR, hop_length=256, x_axis="time", ax=axes[0])
axes[0].set_title("声学模型输出的梅尔频谱")
axes[0].set_xlabel("时间（秒）")
for k, name in enumerate(["vocos", "hifigan", "griffinlim"], 1):
    vocoder(mel, name)                                   # 先运行一次，把模型加载好
    start = time.time()
    audio = vocoder(mel, name)
    used = time.time() - start
    audio = audio / np.abs(audio).max() * 0.9            # 统一音量，方便比较
    save_audio(f"notice_{name}.wav", audio, SR)
    dur = len(audio) / SR
    heard = transcribe(audio, SR)
    print(f"{name:<8} 时长 {dur:.2f} 秒，声码器用时 {used:.3f} 秒（实时率 {used / dur:.3f}），"
          f"回识别字错率 {cer(answer, heard)[0]:.0%}：{heard}")
    S = librosa.amplitude_to_db(np.abs(librosa.stft(audio, n_fft=1024, hop_length=256)), ref=np.max)
    librosa.display.specshow(S, sr=SR, hop_length=256, x_axis="time", y_axis="hz", ax=axes[k])
    axes[k].set_title(f"{name} 生成的声音的语谱图")
    axes[k].set_xlabel("时间（秒）")
plt.tight_layout()
plt.savefig("mel_vocoder.png", dpi=110)
print("已保存 mel_vocoder.png 和三个 notice_*.wav")
