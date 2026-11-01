"""实验 9-4 测一测快不快：（1）一次问答各环节的耗时，算出“用户要等多久”；（2）比较 int8 量化模型和原始模型的大小和速度。

运行：在 labs/ch09 文件夹里  python lab9_4_latency.py
需要模型：python models.py sensevoice matcha-zh kws
"""
import csv
import os
import sys
import time

import numpy as np
import sherpa_onnx as so

sys.path.append("..")
from assistant import ask
from voicelab import model_path, read_audio, speak

# 1. 一次问答的“等待时间”：用户说完 → 系统发现说完了（静音等待）→ 识别 → 理解 → 合成出第一句
VAD_WAIT = 0.5                                     # VAD 要听到 0.5 秒静音才认为“说完了”（第 4 章）  ← 改这里
speak("预热")
audio, sr = read_audio("../data/questions/q_2.wav")
ask(audio, sr)                                     # 预热一次
times = [ask(audio, sr)["time"] for _ in range(5)]  # 测 5 次取平均
avg = {k: np.mean([t[k] for t in times]) for k in times[0]}
print("== 一次问答各环节平均耗时（5 次）==")
for k, v in avg.items():
    print(f"{k:<6} {v:6.3f} 秒")
wait_first = VAD_WAIT + avg["识别"] + avg["理解"] + avg["首句合成"]
wait_all = VAD_WAIT + avg["识别"] + avg["理解"] + avg["全部合成"]
print(f"用户说完到听到回答：先合成第一句就播放 {wait_first:.2f} 秒；整段合成完再播放 {wait_all:.2f} 秒")


# 2. int8 量化模型 vs 原始模型：用第 4 章的唤醒词检测器，同样 18 段录音各跑一遍

d = model_path("kws")
rows = list(csv.DictReader(open("../data/kws/kws.csv", encoding="utf-8-sig")))
print("\n== int8 量化模型 vs 原始模型（唤醒词检测）==")
for tag in ["", ".int8"]:                                       # "" 是原始的 32 位小数模型，".int8" 是 8 位整数模型
    files = {p: f"{d}/{p}-epoch-12-avg-2-chunk-16-left-64{tag}.onnx" for p in ("encoder", "decoder", "joiner")}
    size = sum(os.path.getsize(x) for x in files.values()) / 1024 / 1024
    kws = so.KeywordSpotter(tokens=f"{d}/tokens.txt", **files, keywords_file="../ch04/my_keywords.txt",
                            keywords_threshold=0.25, num_threads=2)
    start, total, right = time.time(), 0.0, 0
    for r in rows:
        samples, sr = read_audio(f"../data/kws/{r['文件']}")
        total += len(samples) / sr
        stream, found = kws.create_stream(), False
        stream.accept_waveform(sr, samples)
        stream.input_finished()
        while kws.is_ready(stream):
            kws.decode_stream(stream)
            if kws.get_result(stream):
                found = True
                kws.reset_stream(stream)
        right += found == (r["含唤醒词"] == "是")
    used = time.time() - start
    print(f"{'int8' if tag else '原始 float32':<12} 大小 {size:5.1f} MB  处理 {total:.0f} 秒录音用 {used:.2f} 秒  "
          f"实时率 {used / total:.3f}  判断正确 {right}/{len(rows)}")
