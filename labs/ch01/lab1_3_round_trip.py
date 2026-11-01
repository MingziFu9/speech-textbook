"""实验 1-3 一来一回：识别一段居民来电 → 按关键词写一句回复 → 合成出来 → 再识别一遍检查。
运行前：python models.py ch01"""
import sys

sys.path.append("..")
from voicelab import save_audio, speak, transcribe

heard = transcribe("../data/calls/call_01.wav")          # 第 1 步：听写居民来电
print("居民说：", heard)

if "垃圾分类" in heard:                                   # 第 2 步：看看问的是什么（第 9 章会做得更聪明）
    reply = "您好，本周六的垃圾分类宣传活动上午9点开始，地点在3号楼前，欢迎参加。"
else:
    reply = "您好，您的问题我们已经记下了，工作人员会尽快回复您。"
print("回复：", reply)

samples, sr = speak(reply)                                # 第 3 步：把回复合成出来
save_audio("reply.wav", samples, sr)

check = transcribe("reply.wav")                           # 第 4 步：再识别一遍，看合成得清不清楚
print("回听：", check)
