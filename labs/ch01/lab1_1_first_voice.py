"""实验 1-1 让电脑说第一句话：用中文合成模型朗读一条社区通知。
运行前：在 labs 文件夹里运行 python models.py ch01 下载模型；然后 cd ch01 再运行本文件。"""
import sys
import time

sys.path.append("..")                       # 让 Python 找到 labs 文件夹里的 voicelab.py
from voicelab import duration, play, save_audio, speak

text = "社区通知：本周六上午9点，在3号楼前举行垃圾分类宣传活动，欢迎居民参加。"   # ← 改这里：换成你想说的话
speed = 1.0                                 # ← 改这里：语速，0.8 慢一些，1.2 快一些

start = time.time()
samples, sr = speak(text, speed=speed)      # 合成：文字 → 声音（采样点 + 采样率）
used = time.time() - start

save_audio("notice.wav", samples, sr)       # 保存成 WAV 文件，双击就能听
play(samples, sr)                           # 在 Notebook 里会出现播放条
print(f"采样率：{sr} Hz，采样点：{len(samples)} 个")
print(f"语音时长：{duration(samples, sr):.2f} 秒，合成用时：{used:.2f} 秒")
print("已保存 notice.wav")
