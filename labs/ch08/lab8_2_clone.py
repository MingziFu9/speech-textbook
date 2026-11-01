"""实验 8-2 零样本克隆：用虚拟授权人 B 的参考音克隆音色，朗读一句新的话；改参考时长和生成步数，看效果和速度。

运行：在 labs/ch08 文件夹里  python lab8_2_clone.py
需要模型：python models.py zipvoice speaker sensevoice
参考音只用书里的虚拟授权人或已签授权书的你自己。不要用模型包 test_wavs 里的任何示例音（其中有真实公众人物的声音）。
"""
import csv
import sys
import time

sys.path.append("..")
from voicelab import cer, clone, embed, save_audio, transcribe

text = "各位居民请注意，本周六上午九点，社区卫生服务站提供免费量血压服务。"      # ← 改这里：要克隆声音说的话
refs = {row["文件"]: row["文字"] for row in csv.DictReader(open("../data/voices/ref_lengths.csv", encoding="utf-8-sig"))}
refs["volunteer_B_1.wav"] = "大家好，我是社区志愿者，平时负责每周的社区广播和活动通知，很高兴为大家服务。"
order = ["ref_B_3s.wav", "ref_B_6s.wav", "volunteer_B_1.wav", "ref_B_15s.wav"]

# 用 B 没参与克隆的一段录音当“真身”，看克隆结果像不像 B；再和 A、C、D 比，看是否“不像别人”
real = {c: embed(f"../data/voices/volunteer_{c}_3.wav") for c in "ABCD"}
clone("预热", "../data/voices/ref_B_3s.wav", refs["ref_B_3s.wav"])   # 先加载模型


def evaluate(audio, sr, used):
    v = embed(audio, sr)
    others = max(v @ real[c] for c in "ACD")
    heard = transcribe(audio, sr)
    return f"像 B {v @ real['B']:.2f}  像别人(最高) {others:.2f}  字错率 {cer(text, heard)[0]:4.0%}  实时率 {used / (len(audio) / sr):.2f}"


print("== 第 1 步：参考音长短不同（生成步数 4）==")
for name in order:
    start = time.time()
    audio, sr = clone(text, f"../data/voices/{name}", refs[name], steps=4)
    used = time.time() - start
    save_audio(f"clone_{name}", audio, sr)
    print(f"{name:<18} {evaluate(audio, sr, used)}")

print("\n== 第 2 步：生成步数不同（参考音 volunteer_B_1，约 9 秒）==")
for steps in [1, 2, 4, 8, 16]:                                   # ← 改这里
    start = time.time()
    audio, sr = clone(text, "../data/voices/volunteer_B_1.wav", refs["volunteer_B_1.wav"], steps=steps)
    used = time.time() - start
    save_audio(f"clone_steps{steps}.wav", audio, sr)
    print(f"步数 {steps:>2}  {evaluate(audio, sr, used)}")
