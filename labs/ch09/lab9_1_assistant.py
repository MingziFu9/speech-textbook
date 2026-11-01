"""实验 9-1 语音问答小助手：8 段居民提问 → 识别 → 按关键词找答案 → 合成回答，统计答对几题、每一步花多少时间。

运行：在 labs/ch09 文件夹里  python lab9_1_assistant.py
需要模型：python models.py sensevoice matcha-zh
"""
import csv
import sys

sys.path.append("..")
from assistant import ask
from voicelab import read_audio, save_audio, speak, transcribe

speak("预热")                                                     # 先把识别和合成模型加载好，不计入耗时
transcribe(read_audio("../data/questions/q_1.wav")[0], 16000)

right = 0
rows = list(csv.DictReader(open("../data/questions/questions.csv", encoding="utf-8-sig")))
for r in rows:
    audio, sr = read_audio(f"../data/questions/{r['文件']}")
    result = ask(audio, sr)
    save_audio(f"reply_{r['文件']}", result["audio"], result["sr"])
    ok = result["faq"] == r["应匹配的问答编号"]
    right += ok
    t = result["time"]
    print(f"【{r['文件']}】听到：{result['heard']}")
    print(f"   匹配问答 {result['faq']}（应为 {r['应匹配的问答编号']}）{'✓' if ok else '✗'}  回答：{result['reply'][:24]}……")
    print(f"   耗时：识别 {t['识别']:.2f} 秒，理解 {t['理解'] * 1000:.1f} 毫秒，首句合成 {t['首句合成']:.2f} 秒，全部合成 {t['全部合成']:.2f} 秒")
print(f"\n{len(rows)} 个问题，答对 {right} 个")

# 第 2 步：关键词匹配的弱点——直接用文字测几句“刁钻”的问题
from assistant import understand                                  # noqa: E402

print("\n========== 关键词匹配测一测 ==========")
for q in ["厨房水龙头坏了怎么办", "暖气片漏水了找谁修", "食堂的饭菜能不能少放点盐", "我要提个建议"]:   # ← 改这里
    item = understand(q)
    print(f"{q}  →  {item['编号'] + ' ' + item['主题'] if item else '没有匹配'}")
