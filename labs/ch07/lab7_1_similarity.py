"""实验 7-1 声纹比一比：提取 7 段录音的声纹向量，两两算余弦相似度，画成热力图，找出同一个人，并判断“未知录音”是谁。

运行：在 labs/ch07 文件夹里  python lab7_1_similarity.py
需要模型：python models.py speaker
"""
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.append("..")
from voicelab import embed

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "WenQuanYi Zen Hei"]
files = ["volunteer_A_1", "volunteer_A_2", "volunteer_B_1", "volunteer_C_1",     # ← 改这里
         "volunteer_C_2", "volunteer_D_1", "unknown"]

# 1. 每段录音 → 一个 192 维的声纹向量（已经缩放成长度为 1）
vectors = np.array([embed(f"../data/voices/{name}.wav") for name in files])
print("声纹向量的形状：", vectors.shape)
print("A_1 的前 5 个数：", np.round(vectors[0, :5], 3))

# 2. 两两算余弦相似度：长度为 1 的向量，点积就是余弦相似度
sim = vectors @ vectors.T
labels = [n.replace("volunteer_", "") for n in files]
print("\n相似度矩阵：")
print("        " + "".join(f"{x:>8}" for x in labels))
for name, row in zip(labels, sim):
    print(f"{name:>8}" + "".join(f"{v:8.2f}" for v in row))

# 3. 画热力图
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(sim, cmap="viridis", vmin=-0.2, vmax=1)
ax.set_xticks(range(len(labels)), labels, rotation=45)
ax.set_yticks(range(len(labels)), labels)
for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, f"{sim[i, j]:.2f}", ha="center", va="center", color="w" if sim[i, j] < 0.6 else "k", fontsize=8)
fig.colorbar(im)
ax.set_title("声纹相似度")
fig.tight_layout()
fig.savefig("similarity.png", dpi=120)

# 4. 未知录音最像谁？
for name, s in sorted(zip(labels[:-1], sim[-1, :-1]), key=lambda x: -x[1]):
    print(f"unknown 和 {name} 的相似度：{s:.2f}")
