"""实验 4-2 议事会录音做字幕：用 VAD 把长录音切成一句一句，逐句识别，生成 SRT 字幕文件，并和标准答案对比。"""
import sys

import numpy as np
import pandas as pd
import sherpa_onnx

sys.path.append("..")
from models import path as model_path
from voicelab import cer, read_audio, transcribe

samples, sr = read_audio("../data/meeting/meeting.wav")          # 约 51 秒、三个人轮流发言
print(f"录音时长 {len(samples) / sr:.2f} 秒")

# ---------- 第 1 步：VAD 找出“哪里有人在说话” ----------
config = sherpa_onnx.VadModelConfig()
config.silero_vad.model = str(model_path("vad") / "silero_vad.onnx")
config.silero_vad.threshold = 0.5             # 每一小段“像人声”的概率超过它，就算有人说话
config.silero_vad.min_silence_duration = 0.5  # ← 改这里：静音超过这么多秒才算一句话结束，试试 0.2、1.0
config.silero_vad.min_speech_duration = 0.25  # 短于这么多秒的声音不算一句（过滤咳嗽、敲桌子）
config.sample_rate = sr
vad = sherpa_onnx.VoiceActivityDetector(config, buffer_size_in_seconds=60)

window = config.silero_vad.window_size        # VAD 每次看 512 个采样点（32 毫秒）
segments = []
for start in range(0, len(samples), window):
    vad.accept_waveform(samples[start:start + window])
    while not vad.empty():                    # 每检测到一句完整的话，就取出来
        seg = vad.front
        segments.append((seg.start / sr, np.array(seg.samples)))
        vad.pop()
vad.flush()                                   # 录音结束，把最后一句也取出来
while not vad.empty():
    segments.append((vad.front.start / sr, np.array(vad.front.samples)))
    vad.pop()
print(f"VAD 切出 {len(segments)} 句")


# ---------- 第 2 步：逐句识别，写成 SRT 字幕 ----------
def srt_time(t):
    """秒 → SRT 的时间格式 时:分:秒,毫秒"""
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


lines = []
for k, (begin, seg) in enumerate(segments, 1):
    end = begin + len(seg) / sr
    text = transcribe(seg, sr)
    lines.append(f"{k}\n{srt_time(begin)} --> {srt_time(end)}\n{text}\n")
    print(f"{k:>2}  {begin:6.2f}–{end:6.2f} 秒  {text}")
with open("meeting.srt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("已保存 meeting.srt")

# ---------- 第 3 步：和标准答案对比 ----------
truth = pd.read_csv("../data/meeting/meeting_truth.csv")
ref = "".join(truth["文字"])
hyp = "".join(transcribe(seg, sr) for _, seg in segments)
rate, s, d, i = cer(ref, hyp)
print(f"标准答案 {len(truth)} 句；整场字错率 {rate:.1%}（替换 {s}、删除 {d}、插入 {i}）")
