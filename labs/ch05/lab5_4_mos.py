"""实验 5-4（选做）给合成打分：同一条通知用 5 种方式合成，打乱顺序编号，
生成小组 MOS 打分表；同时自动算出回识别字错率和实时率。"""
import csv
import random
import sys
import time

import numpy as np

sys.path.append("..")
from voicelab import cer, save_audio, speak, transcribe

text = "各位居民请注意，明天上午9点到11点小区停水，请提前储水，给您带来不便，敬请谅解。"   # ← 改这里
versions = [  # (说明, 模型, 说话人编号, 语速)
    ("Matcha 正常语速", "matcha-zh", 0, 1.0),
    ("Matcha 加快 1.4 倍", "matcha-zh", 0, 1.4),
    ("Kokoro 女声", "kokoro", 45, 1.0),
    ("Kokoro 男声", "kokoro", 65, 1.0),
    ("VITS AISHELL-3 第 10 号音色", "vits-aishell3", 10, 1.0),
]
random.seed(2026)
codes = random.sample(range(101, 200), len(versions))       # 随机编号，打分时不知道哪个是哪个（“盲听”）

rows = []
for (desc, model, sid, speed), code in zip(versions, codes):
    speak("预热", model=model, sid=sid)                     # 先合成一次，把模型加载好
    start = time.time()
    audio, sr = speak(text, model=model, sid=sid, speed=speed)
    used = time.time() - start
    save_audio(f"sample_{code}.wav", audio, sr)
    heard = transcribe(audio, sr)
    dur = len(audio) / sr
    rows.append([code, desc, sr, f"{dur:.2f}", f"{used / dur:.3f}", f"{cer(text, heard)[0]:.0%}", heard])
    print(f"sample_{code}.wav  {desc:<22} 采样率 {sr:>5}  时长 {dur:5.2f} 秒  实时率 {used / dur:.3f}  "
          f"字错率 {cer(text, heard)[0]:>4.0%}  {heard}")

with open("answer_key.csv", "w", newline="", encoding="utf-8-sig") as f:      # 答案（打完分再看）
    csv.writer(f).writerows([["编号", "版本", "采样率", "时长", "实时率", "回识别字错率", "回识别结果"]] + rows)
with open("mos_sheet.csv", "w", newline="", encoding="utf-8-sig") as f:       # 打分表（发给每个组员）
    w = csv.writer(f)
    w.writerow(["编号", "自然度（1—5 分）", "清晰度（1—5 分）", "备注"])
    for code in sorted(codes):
        w.writerow([code, "", "", ""])
print("已保存 sample_*.wav、mos_sheet.csv（打分表）和 answer_key.csv（答案，打完分再打开）")
