"""实验 1-2 让电脑听写：把几段录音转成文字。
运行前：python models.py ch01；先运行实验 1-1 得到 notice.wav。"""
import sys
import time

sys.path.append("..")
from voicelab import transcribe

files = [
    "notice.wav",                                   # 实验 1-1 合成的通知
    "../models/sensevoice/test_wavs/zh.wav",        # 模型自带的普通话录音
    "../models/sensevoice/test_wavs/yue.wav",       # 粤语
    "../models/sensevoice/test_wavs/en.wav",        # 英语
    # "my_voice.wav",                               # ← 改这里：放进你自己用手机录的一句话
]

for f in files:
    start = time.time()
    text = transcribe(f)                            # 识别：声音 → 文字
    print(f"{f.split('/')[-1]:<12} 用时 {time.time() - start:.2f} 秒：{text}")
