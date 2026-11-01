"""实验 7-2 声纹登录：注册 4 位志愿者的声纹，用新录音和“冒充者”录音测试，调门槛，记录误接受和误拒绝。

运行：在 labs/ch07 文件夹里  python lab7_2_login.py
需要模型：python models.py speaker
"""
import csv
import sys

import matplotlib.pyplot as plt
import librosa
import numpy as np

sys.path.append("..")
from voicelab import embed, read_audio

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "WenQuanYi Zen Hei"]

# 1. 注册：每人用 2 段录音的声纹向量取平均，作为这个人的“声纹模板”
enrolled = {}
for code in "ABCD":
    v = embed(f"../data/voices/volunteer_{code}_1.wav") + embed(f"../data/voices/volunteer_{code}_2.wav")
    enrolled[code] = v / np.linalg.norm(v)
print("已注册：", list(enrolled))

# 2. 测试：每段测试录音都分别“声称”自己是 A、B、C、D，算和模板的相似度
genuine, impostor = [], []                     # 真本人的分数、冒充者的分数
rows = list(csv.DictReader(open("../data/speaker_test/speaker_test.csv", encoding="utf-8-sig")))
for r in rows:
    v = embed(f"../data/speaker_test/{r['文件']}")
    for code, t in enrolled.items():
        (genuine if r["真实身份"] == code else impostor).append(float(v @ t))
genuine, impostor = np.array(genuine), np.array(impostor)
print(f"真本人测试 {len(genuine)} 次，分数 {genuine.min():.2f}—{genuine.max():.2f}，平均 {genuine.mean():.2f}")
print(f"冒充测试 {len(impostor)} 次，分数 {impostor.min():.2f}—{impostor.max():.2f}，平均 {impostor.mean():.2f}")

# 3. 调门槛：分数 ≥ 门槛就“放行”
print("\n门槛   误接受率 FAR   误拒绝率 FRR")
for th in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:          # ← 改这里
    far = np.mean(impostor >= th)                        # 冒充者被放行的比例
    frr = np.mean(genuine < th)                          # 本人被拒绝的比例
    print(f"{th:.2f}   {far:8.1%}      {frr:8.1%}")

# 4. 找等错误率 EER：FAR 和 FRR 相等的那个门槛
ths = np.linspace(0, 1, 1001)
fars = np.array([np.mean(impostor >= t) for t in ths])
frrs = np.array([np.mean(genuine < t) for t in ths])
k = np.argmin(np.abs(fars - frrs))
print(f"\n等错误率 EER ≈ {(fars[k] + frrs[k]) / 2:.1%}，此时门槛 ≈ {ths[k]:.2f}")
ok = ths[(fars == 0) & (frrs == 0)]
if len(ok):
    print(f"门槛在 {ok.min():.2f}—{ok.max():.2f} 之间时，两种错误都是 0")

# 5. 画两种分数的分布
plt.figure(figsize=(7, 3.5))
plt.hist(impostor, bins=30, range=(-0.2, 1), alpha=0.6, label="冒充者")
plt.hist(genuine, bins=30, range=(-0.2, 1), alpha=0.6, label="本人")
plt.axvline(ths[k], color="r", linestyle="--", label=f"EER 门槛 {ths[k]:.2f}")
plt.xlabel("和声纹模板的相似度")
plt.ylabel("次数")
plt.legend()
plt.tight_layout()
plt.savefig("login_scores.png", dpi=120)

# 6. 换个条件再测：本人用电话打进来（8 kHz）、或者只说 1 秒，门槛还用 0.75
TH = 0.75                                                # ← 改这里
phone, short = [], []
for r in rows:
    if r["真实身份"] in enrolled:
        a, sr = read_audio(f"../data/speaker_test/{r['文件']}")
        tel = librosa.resample(librosa.resample(a, orig_sr=sr, target_sr=8000), orig_sr=8000, target_sr=sr)
        phone.append(float(embed(tel, sr) @ enrolled[r["真实身份"]]))
        short.append(float(embed(a[int(0.2 * sr):int(1.2 * sr)], sr) @ enrolled[r["真实身份"]]))
print(f"\n门槛 {TH}：")
print(f"正常录音  本人平均分 {genuine.mean():.2f}，误拒绝率 {np.mean(genuine < TH):.0%}")
print(f"电话音质  本人平均分 {np.mean(phone):.2f}，误拒绝率 {np.mean(np.array(phone) < TH):.0%}")
print(f"只说 1 秒 本人平均分 {np.mean(short):.2f}，误拒绝率 {np.mean(np.array(short) < TH):.0%}")
