"""实验 7-3 谁在说话：对三人议事会录音做说话人日志（谁在什么时候说话），再配合第 4 章的识别，输出“发言人：内容”格式的纪要。

运行：在 labs/ch07 文件夹里  python lab7_3_diarization.py
需要模型：python models.py segmentation speaker sensevoice
"""
import csv
import sys

import numpy as np
import sherpa_onnx as so

sys.path.append("..")
from voicelab import embed, model_path, read_audio, transcribe

# 1. 建说话人日志工具：分割模型找“换人的地方”，声纹模型提取每一段的声纹，再把声纹相近的段聚成一类
config = so.OfflineSpeakerDiarizationConfig(
    segmentation=so.OfflineSpeakerSegmentationModelConfig(
        pyannote=so.OfflineSpeakerSegmentationPyannoteModelConfig(model=f"{model_path('segmentation')}/model.onnx")),
    embedding=so.SpeakerEmbeddingExtractorConfig(
        model=f"{model_path('speaker')}/3dspeaker_speech_campplus_sv_zh-cn_16k-common.onnx"),
    clustering=so.FastClusteringConfig(num_clusters=-1, threshold=0.5),   # ← 改这里：不知道几个人时用 -1 和门槛
    min_duration_on=0.3, min_duration_off=0.5)
sd = so.OfflineSpeakerDiarization(config)

# 2. 处理整段录音
audio, sr = read_audio("../data/meeting/meeting.wav", sd.sample_rate)
segments = sd.process(audio).sort_by_start_time()
print(f"录音 {len(audio) / sr:.1f} 秒，找到 {len(segments)} 段，{len({s.speaker for s in segments})} 位发言人")

# 3. 每一段交给识别模型转文字
minutes = []
for s in segments:
    piece = audio[int(s.start * sr):int(s.end * sr)]
    minutes.append((s.start, s.end, s.speaker, transcribe(piece, sr)))
    print(f"{s.start:6.2f}—{s.end:6.2f}  说话人{s.speaker}  {minutes[-1][3]}")

# 4. 把“说话人0、1、2”对上真名：和注册过的声纹比一比（这里用标准答案里每人第一句话当注册录音）
truth = list(csv.DictReader(open("../data/meeting/meeting_truth.csv", encoding="utf-8-sig")))
names = {}
for t in truth:
    if t["发言人"] not in names:
        names[t["发言人"]] = embed(audio[int(float(t["开始秒"]) * sr):int(float(t["结束秒"]) * sr)], sr)
who = {}
for spk in sorted({s.speaker for s in segments}):
    pieces = np.concatenate([audio[int(a * sr):int(b * sr)] for a, b, k, _ in minutes if k == spk])
    v = embed(pieces, sr)
    who[spk] = max(names, key=lambda n: v @ names[n])

print("\n========== 议事会纪要 ==========")
for start, end, spk, text in minutes:
    print(f"[{int(start // 60):02d}:{start % 60:04.1f}] {who[spk]}：{text}")

# 5. 和标准答案对比：每一句话的中点落在哪个人的段里
right = 0
for t in truth:
    mid = (float(t["开始秒"]) + float(t["结束秒"])) / 2
    got = [who[s.speaker] for s in segments if s.start <= mid <= s.end]
    right += bool(got) and got[0] == t["发言人"]
print(f"\n{len(truth)} 句话中，{right} 句的发言人判断正确")

# 6. 另一种做法：事先注册过每个人的声纹，就不用聚类，直接逐段“辨认”最像谁
right = 0
for t in truth:
    mid = (float(t["开始秒"]) + float(t["结束秒"])) / 2
    for start, end, spk, text in minutes:
        if start <= mid <= end:
            v = embed(audio[int(start * sr):int(end * sr)], sr)
            right += max(names, key=lambda n: v @ names[n]) == t["发言人"]
print(f"逐段辨认：{len(truth)} 句话中，{right} 句的发言人判断正确")
