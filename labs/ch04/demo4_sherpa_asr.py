"""4.2 节示例：不用 voicelab，直接用 sherpa-onnx 识别一段录音（四步：建识别器 → 建数据流 → 喂音频 → 取结果）。"""
import sys

import soundfile as sf
import sherpa_onnx

sys.path.append("..")
from models import path as model_path

d = model_path("sensevoice")

# 第 1 步：建识别器（告诉它模型文件在哪里）。整个程序只需要建一次
recognizer = sherpa_onnx.OfflineRecognizer.from_sense_voice(
    model=str(d / "model.int8.onnx"),
    tokens=str(d / "tokens.txt"),
    use_itn=True,              # ← 改这里：False 关掉逆正则化，试试有什么不同。逆正则化：“五号楼”写成“5号楼”，并加标点
    num_threads=2,
)

# 读录音：sherpa-onnx 要的是 float32 的单声道采样点，数值在 -1 到 1 之间
samples, sr = sf.read("../data/calls/call_02.wav", dtype="float32")
print("原始形状：", samples.shape, "采样率：", sr)
if samples.ndim == 2:          # 双声道：每一行是一个时刻的左右两个值，取平均变成单声道
    samples = samples.mean(axis=1)

stream = recognizer.create_stream()          # 第 2 步：建一个数据流（每段录音一个）
stream.accept_waveform(sr, samples)          # 第 3 步：把采样点和采样率喂进去（采样率不是 16000 会自动转换）
recognizer.decode_stream(stream)             # 识别
print(stream.result.text)                    # 第 4 步：取结果
print(stream.result.lang, stream.result.emotion, stream.result.event)   # SenseVoice 还能给出语种、情绪、声音事件
