"""实验 2-3 整理居民来电：批量统一成单声道 16 kHz、去掉首尾静音、音量归一化，输出检查表，并比较整理前后的识别结果。"""
import sys
from pathlib import Path

import librosa
import numpy as np
import pandas as pd
import soundfile as sf

sys.path.append("..")
from voicelab import cer, read_audio, save_audio, transcribe

src = Path("../data/calls")
out = Path("calls_clean")
out.mkdir(exist_ok=True)
truth = pd.read_csv(src / "calls.csv")                     # 标准答案（每段来电的文字）

rows = []
for _, r in truth.iterrows():
    info = sf.info(src / r["文件"])                         # 先看原始格式
    raw, raw_sr = read_audio(src / r["文件"], sr=None)       # 原样读入（多声道已取平均）
    peak = np.abs(raw).max()
    clipped = np.mean(np.abs(raw) > 0.99)                    # 削波：贴着最大值的采样点比例

    y, sr = read_audio(src / r["文件"], sr=16000)            # ① 单声道 ② 16 kHz
    y, _ = librosa.effects.trim(y, top_db=35)                # ③ 去掉首尾比最响处低 35 分贝以上的部分
    y = y / np.abs(y).max() * 0.9                            # ④ 音量归一化：最响处调到 0.9
    save_audio(out / r["文件"], y, sr)

    before, after = transcribe(raw, raw_sr), transcribe(y, sr)
    rows.append({"文件": r["文件"], "问题": r["录音问题"], "声道": info.channels, "采样率": info.samplerate,
                 "原时长": round(info.duration, 2), "新时长": round(len(y) / sr, 2), "峰值": round(float(peak), 3),
                 "削波比例": f"{clipped:.1%}", "整理前字错率": f"{cer(r['文字'], before)[0]:.0%}",
                 "整理后字错率": f"{cer(r['文字'], after)[0]:.0%}", "整理后识别": after})

table = pd.DataFrame(rows)
table.to_csv("calls_check.csv", index=False, encoding="utf-8-sig")
pd.set_option("display.width", 200)
print(table.drop(columns="整理后识别").to_string(index=False))
for f in ["call_03.wav", "call_06.wav"]:
    print(f, "整理后识别：", table.set_index("文件").loc[f, "整理后识别"])
print("已保存 calls_clean/ 和 calls_check.csv")
