"""实验 4-1 三个模型比一比：SenseVoice、Paraformer、Whisper 识别同一批来电，比较字错率和速度；再试试方言和外语。"""
import sys
import time

import pandas as pd
import zhconv                                                     # 繁体字转简体字

sys.path.append("..")
from voicelab import PUNCT, cer, duration, read_audio, transcribe

DIGITS = str.maketrans("零一二三四五六七八九", "0123456789")


def normalize(text):
    """统一写法：繁体转简体，中文数字转阿拉伯数字（第 3 章实验 3-3）"""
    return zhconv.convert(text, "zh-cn").translate(DIGITS)


models = ["sensevoice", "paraformer-zh", "whisper-tiny"]           # ← 改这里：可以只比其中两个
truth = pd.read_csv("../data/calls/calls.csv")
audios = {r["文件"]: read_audio(f"../data/calls/{r['文件']}") for _, r in truth.iterrows()}
total_audio = sum(duration(y, sr) for y, sr in audios.values())

summary = []
for model in models:
    transcribe(*audios["call_01.wav"], model=model)                  # 先识别一次，把模型加载好
    errors = chars = 0
    used = 0.0
    for _, r in truth.iterrows():
        start = time.time()
        hyp = transcribe(*audios[r["文件"]], model=model)
        used += time.time() - start
        rate, s, d, i = cer(normalize(r["文字"]), normalize(hyp))
        errors += s + d + i
        chars += len([c for c in r["文字"] if c not in PUNCT])
        if r["文件"] in ("call_03.wav", "call_07.wav"):                # 打印两段看看
            print(f"{model:<14}{r['文件']}  {hyp}")
    summary.append([model, f"{errors / chars:.1%}", f"{used:.2f}", f"{used / total_audio:.3f}"])

print(pd.DataFrame(summary, columns=["模型", "总字错率", "识别用时（秒）", "实时率"]).to_string(index=False))

# 方言和外语：模型自带的测试录音（没有标准答案，听一听再判断对不对）
tests = {"四川话": "../models/paraformer-zh/test_wavs/3-sichuan.wav",
         "天津话": "../models/paraformer-zh/test_wavs/4-tianjin.wav",
         "河南话": "../models/paraformer-zh/test_wavs/5-henan.wav",
         "粤语": "../models/sensevoice/test_wavs/yue.wav",
         "英语": "../models/sensevoice/test_wavs/en.wav"}
for name, file in tests.items():
    y, sr = read_audio(file)
    print(f"【{name}】{duration(y, sr):.1f} 秒")
    for model in models:
        print(f"  {model:<14}{transcribe(y, sr, model=model)}")
