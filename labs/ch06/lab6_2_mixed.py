"""实验 6-2 中英混读：同样几句中英文混在一起的话，比较三个合成模型读得怎么样。

运行：在 labs/ch06 文件夹里  python lab6_2_mixed.py
需要模型：python models.py matcha-zh melo-zh-en kokoro sensevoice
"""
import sys
import time

sys.path.append("..")
from voicelab import save_audio, speak, transcribe

sentences = [                                                        # ← 改这里：换成你自己的句子
    "请在WiFi设置里选择Community-5G，密码写在服务站门口。",
    "下载社区App以后，扫一扫二维码就能预约。",
    "今天的线上会议用Zoom开，晚上八点准时开始。",
    "我们的AI助手支持中文和English两种语言。",
]
models = [("matcha-zh", 0), ("melo-zh-en", 0), ("kokoro", 45)]      # (模型, 说话人编号)

for model, sid in models:
    speak("预热", model=model, sid=sid)                             # 先加载模型，不计时间
    print(f"========== {model} ==========")
    for k, text in enumerate(sentences, 1):
        start = time.time()
        audio, sr = speak(text, model=model, sid=sid)
        used = time.time() - start
        save_audio(f"mixed_{model}_{k}.wav", audio, sr)
        print(f"第 {k} 句  时长 {len(audio) / sr:4.1f} 秒  实时率 {used / (len(audio) / sr):.2f}  听写：{transcribe(audio, sr)}")

print("========== 改写文字再试 ==========")
rewritten = [                                       # 英文单词换一种写法：加连字符、字母和数字之间加空格
    "请在Wi-Fi设置里选择Community 5 G，密码写在服务站门口。",
    "下载社区A P P以后，扫一扫二维码就能预约。",
    "我们的A I助手支持中文和English两种语言。",
]
for model, sid in models[1:]:
    for text in rewritten:
        audio, sr = speak(text, model=model, sid=sid)
        print(f"{model:<10}  {text}  →  听写：{transcribe(audio, sr)}")
