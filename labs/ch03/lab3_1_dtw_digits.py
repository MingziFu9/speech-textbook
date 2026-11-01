"""实验 3-1 模板匹配认数字：用 DTW 比较 MFCC，识别英文数字 0—9 的录音。"""
import sys
import time

import librosa
import numpy as np

sys.path.append("..")
from voicelab import read_audio

DATA = "../data/fsdd"                       # Free Spoken Digit Dataset：4 个人，每人把 0—9 各读 10 遍


def mfcc_of(digit, speaker, rep):
    """读一段数字录音，返回它的 MFCC（13 行 × 帧数）"""
    y, sr = read_audio(f"{DATA}/{digit}_{speaker}_{rep}.wav", sr=8000)   # 这套数据是 8 kHz 电话音质
    y, _ = librosa.effects.trim(y, top_db=30)                            # 去掉首尾静音
    return librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=256, hop_length=80)   # 32 毫秒一帧，10 毫秒一步


def dtw_distance(a, b):
    """用 DTW 对齐两段 MFCC，返回对齐后的平均距离（越小越像）"""
    cost, path = librosa.sequence.dtw(X=a, Y=b, metric="euclidean")
    return cost[-1, -1] / len(path)


template_speakers = ["george"]             # ← 改这里：用谁的录音做模板，试试 ["george", "jackson", "lucas", "nicolas"]
templates = {(d, s): mfcc_of(d, s, 0) for d in range(10) for s in template_speakers}   # 每人每个数字存 1 个模板：第 0 遍
print(f"模板：{len(templates)} 个（{'、'.join(template_speakers)} 读的第 0 遍）")

start = time.time()
for speaker in ["george", "jackson", "lucas", "nicolas"]:
    reps = range(1, 10) if speaker in template_speakers else range(0, 10)   # 模板那一遍不拿来测
    right, wrong = 0, []
    for d in range(10):
        for rep in reps:
            test = mfcc_of(d, speaker, rep)
            scores = {k: dtw_distance(test, t) for k, t in templates.items()}
            guess = min(scores, key=scores.get)[0]      # 距离最小的模板是哪个数字，答案就是它
            if guess == d:
                right += 1
            else:
                wrong.append(f"{d}→{guess}")
    total = 10 * len(reps)
    tag = "（有模板）" if speaker in template_speakers else "（没有模板）"
    print(f"{speaker:<8}{tag:<8} 正确 {right:>3}/{total}，准确率 {right / total:.0%}  认错的例子：{' '.join(wrong[:6])}")
print(f"用时 {time.time() - start:.1f} 秒")

# 看一个对齐的例子：同一个人读两遍“1”，帧数不一样，DTW 怎样把它们对上
a, b = mfcc_of(1, "george", 0), mfcc_of(1, "george", 1)
cost, path = librosa.sequence.dtw(X=a, Y=b, metric="euclidean")
print(f"“1”第 0 遍 {a.shape[1]} 帧，第 1 遍 {b.shape[1]} 帧，对齐路径 {len(path)} 步")

import matplotlib.pyplot as plt                     # 把对齐路径画出来

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
plt.figure(figsize=(5, 4.5))
plt.imshow(cost.T, origin="lower", cmap="gray_r", aspect="auto")   # 底色：累计距离，越深越大
plt.plot(path[:, 0], path[:, 1], color="red", linewidth=2)          # 红线：DTW 找到的最佳对齐路径
plt.xlabel("第 0 遍的帧")
plt.ylabel("第 1 遍的帧")
plt.title("DTW 对齐路径：同一个人读两遍“1”")
plt.tight_layout()
plt.savefig("dtw_path.png", dpi=120)
print("已保存 dtw_path.png")
