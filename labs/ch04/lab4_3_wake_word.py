"""实验 4-3 自定义唤醒词：把“你好小站”“小站小站”设为唤醒词，测试 18 段录音，统计漏唤醒和误唤醒。"""
import sys

import pandas as pd
import sherpa_onnx

sys.path.append("..")
from models import path as model_path
from voicelab import read_audio

d = model_path("kws")
wake_words = ["你好小站", "小站小站"]          # ← 改这里：换成你自己的唤醒词（建议 4 个字左右、不常见的组合）
threshold = 0.25                              # ← 改这里：越大越“严格”，误唤醒少、漏唤醒多；试试 0.1、0.4

# 第 1 步：唤醒词 → 拼音声韵母，写成模型认识的关键词文件（每行“声韵母 @原文”）
tokens = sherpa_onnx.text2token(wake_words, tokens=str(d / "tokens.txt"), tokens_type="ppinyin")
with open("my_keywords.txt", "w", encoding="utf-8") as f:
    for word, tok in zip(wake_words, tokens):
        f.write(" ".join(tok) + " @" + word + "\n")
print(open("my_keywords.txt", encoding="utf-8").read())

# 第 2 步：建关键词检测器
kws = sherpa_onnx.KeywordSpotter(
    tokens=str(d / "tokens.txt"),
    encoder=str(d / "encoder-epoch-12-avg-2-chunk-16-left-64.int8.onnx"),
    decoder=str(d / "decoder-epoch-12-avg-2-chunk-16-left-64.int8.onnx"),
    joiner=str(d / "joiner-epoch-12-avg-2-chunk-16-left-64.int8.onnx"),
    keywords_file="my_keywords.txt",
    keywords_threshold=threshold,
    num_threads=2,
)


def detect(file):
    """把一段录音一点一点“喂”给检测器（模拟麦克风），返回检测到的唤醒词列表"""
    samples, sr = read_audio(file)
    stream = kws.create_stream()
    found = []
    for start in range(0, len(samples), 1600):                  # 每次喂 0.1 秒
        stream.accept_waveform(sr, samples[start:start + 1600])
        while kws.is_ready(stream):
            kws.decode_stream(stream)
            word = kws.get_result(stream)
            if word:
                found.append(word)
                kws.reset_stream(stream)                        # 检测到以后重新开始听
    return found


# 第 3 步：测试 18 段录音（6 句话 × 3 种音色），统计
table = pd.read_csv("../data/kws/kws.csv")
rows = []
for _, r in table.iterrows():
    found = detect(f"../data/kws/{r['文件']}")
    should = r["含唤醒词"] == "是"
    result = ("唤醒正确" if found else "漏唤醒") if should else ("误唤醒" if found else "正确不响应")
    rows.append([r["文件"], r["文字"], r["含唤醒词"], "、".join(found) or "-", result])
out = pd.DataFrame(rows, columns=["文件", "文字", "含唤醒词", "检测到", "结果"])
pd.set_option("display.width", 200)
print(out.to_string(index=False))
n_pos, n_neg = (table["含唤醒词"] == "是").sum(), (table["含唤醒词"] == "否").sum()
miss, false = (out["结果"] == "漏唤醒").sum(), (out["结果"] == "误唤醒").sum()
print(f"阈值 {threshold}：漏唤醒 {miss}/{n_pos}，误唤醒 {false}/{n_neg}")
