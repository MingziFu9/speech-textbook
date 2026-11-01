"""实验 3-2 HMM 数字识别器：每个数字训练一个隐马尔可夫模型，测试准确率，画混淆矩阵。"""
import sys
import time
import warnings

import librosa
import matplotlib.pyplot as plt
import numpy as np
from hmmlearn import hmm
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

sys.path.append("..")
from voicelab import read_audio

warnings.filterwarnings("ignore")              # hmmlearn 训练时会打印一些收敛提示，先关掉
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Zen Hei", "Noto Sans CJK SC"]
DATA = "../data/fsdd"
SPEAKERS = ["george", "jackson", "lucas", "nicolas"]


def features(digit, speaker, rep):
    """MFCC 再加上它的变化量（一阶差分），每帧 26 个数；转置成“帧数 × 26”，hmmlearn 要求每行一帧"""
    y, sr = read_audio(f"{DATA}/{digit}_{speaker}_{rep}.wav", sr=8000)
    y, _ = librosa.effects.trim(y, top_db=30)
    m = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, n_fft=256, hop_length=80)
    return np.vstack([m, librosa.feature.delta(m)]).T


n_states = 5                                    # ← 改这里：每个数字的隐状态个数，试试 2、3、8
train_reps, test_reps = range(5, 10), range(0, 5)   # 每人每个数字：后 5 遍训练，前 5 遍测试

start = time.time()
models = {}
for d in range(10):
    X = [features(d, s, r) for s in SPEAKERS for r in train_reps]      # 这个数字的 20 段训练录音
    model = hmm.GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=20, random_state=0)
    model.fit(np.vstack(X), lengths=[len(x) for x in X])                # 多段录音拼在一起，lengths 告诉它每段多长
    models[d] = model
print(f"训练完成：10 个 HMM，每个 {n_states} 个状态，用时 {time.time() - start:.1f} 秒")

truth, guess = [], []
for s in SPEAKERS:
    for d in range(10):
        for r in test_reps:
            x = features(d, s, r)
            scores = {k: m.score(x) for k, m in models.items()}     # 每个模型给出“这段声音由我产生”的对数概率
            truth.append(d)
            guess.append(max(scores, key=scores.get))               # 概率最大的那个数字就是答案
truth, guess = np.array(truth), np.array(guess)
print(f"测试 {len(truth)} 段，准确率 {np.mean(truth == guess):.1%}")
for s, i in zip(SPEAKERS, range(0, len(truth), 50)):
    print(f"  {s:<8} {np.mean(truth[i:i + 50] == guess[i:i + 50]):.0%}")

cm = confusion_matrix(truth, guess)
ConfusionMatrixDisplay(cm, display_labels=range(10)).plot(cmap="Blues", colorbar=False)
plt.xlabel("识别结果")
plt.ylabel("真实数字")
plt.title(f"HMM 数字识别混淆矩阵（{n_states} 个状态）")
plt.tight_layout()
plt.savefig("hmm_confusion.png", dpi=120)
print("已保存 hmm_confusion.png")
