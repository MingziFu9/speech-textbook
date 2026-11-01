"""4.5 节示例：流式识别——把录音一小段一小段地喂给模型，看文字怎样“边说边出”。"""
import sys

import sherpa_onnx

sys.path.append("..")
from models import path as model_path
from voicelab import read_audio

d = model_path("streaming-zh")                             # 一个 14M 参数的中文流式模型（实验 4-4 也用它）
recognizer = sherpa_onnx.OnlineRecognizer.from_transducer(
    tokens=f"{d}/tokens.txt", encoder=f"{d}/encoder-epoch-99-avg-1.int8.onnx",
    decoder=f"{d}/decoder-epoch-99-avg-1.onnx", joiner=f"{d}/joiner-epoch-99-avg-1.int8.onnx", num_threads=2)

samples, sr = read_audio("../data/meeting/meeting.wav")
samples = samples[:int(9.5 * sr)]                       # 只取主持人的第一句话
stream = recognizer.create_stream()
last = ""
for start in range(0, len(samples), sr // 2):           # 每次喂 0.5 秒，模拟麦克风
    stream.accept_waveform(sr, samples[start:start + sr // 2])
    while recognizer.is_ready(stream):
        recognizer.decode_stream(stream)
    text = recognizer.get_result(stream)
    if text != last:
        print(f"{(start + sr // 2) / sr:4.1f} 秒：{text}")
        last = text
