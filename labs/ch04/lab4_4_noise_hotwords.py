"""实验 4-4（选做）噪声和热词：
第一部分：给 8 段来电加上不同强度的噪声，看两个模型的字错率怎样变化；
第二部分：本地地名、人名总是认错，试两种办法：识别模型的“热词”功能，和识别后按拼音纠错。"""
import sys

import numpy as np
import pandas as pd
import sherpa_onnx
from pypinyin import lazy_pinyin

sys.path.append("..")
from models import path as model_path
from voicelab import PUNCT, cer, read_audio, transcribe

# ================= 第一部分：噪声 =================
DIGITS = str.maketrans("零一二三四五六七八九", "0123456789")
truth = pd.read_csv("../data/calls/calls.csv")
audios = [read_audio(f"../data/calls/{f}") for f in truth["文件"]]
rng = np.random.default_rng(0)
rows = []
for snr in [30, 20, 10, 5, 0, -5]:                      # ← 改这里：信噪比（分贝）
    row = [f"{snr} dB"]
    for model in ["sensevoice", "paraformer-zh"]:
        errors = chars = 0
        for (y, sr), ref in zip(audios, truth["文字"]):
            noise = rng.standard_normal(len(y)).astype(np.float32)
            noise *= np.sqrt(np.mean(y ** 2) / np.mean(noise ** 2) / 10 ** (snr / 10))
            hyp = transcribe(y + noise, sr, model=model)
            rate, s, d, i = cer(ref.translate(DIGITS), hyp.translate(DIGITS))
            errors += s + d + i
            chars += len([c for c in ref if c not in PUNCT])
        row.append(f"{errors / chars:.1%}")
    rows.append(row)
print(pd.DataFrame(rows, columns=["信噪比", "sensevoice", "paraformer-zh"]).to_string(index=False))

# ================= 第二部分：热词 =================
hotwords = ["幸福里", "邻里汇", "韦嘉怡", "鲁班路", "樟树苑", "栖霞书屋"]     # ← 改这里：本社区的地名、人名
tests = pd.read_csv("../data/hotwords/hotwords.csv")

# 办法一：识别模型自带的热词功能（只有一部分模型支持，这里用一个支持热词的小型流式模型）
d = model_path("streaming-zh")
with open("my_hotwords.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(" ".join(w) for w in hotwords))        # 每行一个热词，字和字之间用空格隔开


def make_recognizer(use_hotwords):
    extra = dict(hotwords_file="my_hotwords.txt", hotwords_score=1.5) if use_hotwords else {}
    return sherpa_onnx.OnlineRecognizer.from_transducer(
        tokens=f"{d}/tokens.txt", encoder=f"{d}/encoder-epoch-99-avg-1.int8.onnx",
        decoder=f"{d}/decoder-epoch-99-avg-1.onnx", joiner=f"{d}/joiner-epoch-99-avg-1.int8.onnx",
        decoding_method="modified_beam_search", max_active_paths=10, num_threads=2, **extra)


def run(recognizer, y, sr):
    stream = recognizer.create_stream()
    stream.accept_waveform(sr, y)
    stream.accept_waveform(sr, np.zeros(sr // 2, dtype=np.float32))   # 结尾补 0.5 秒静音，让最后几个字出来
    stream.input_finished()
    while recognizer.is_ready(stream):
        recognizer.decode_stream(stream)
    return recognizer.get_result(stream)


# 办法二：识别后按拼音纠错——在识别结果里找“读音和热词一样”的几个字，换成热词
def pinyin_fix(text):
    for word in hotwords:
        target, n = lazy_pinyin(word), len(word)
        for i in range(len(text) - n + 1):
            if lazy_pinyin(text[i:i + n]) == target:
                text = text[:i] + word + text[i + n:]
    return text


plain, boosted = make_recognizer(False), make_recognizer(True)
for _, r in tests.iterrows():
    y, sr = read_audio(f"../data/hotwords/{r['文件']}")
    sv = transcribe(y, sr)
    results = {"小模型": run(plain, y, sr), "小模型+热词": run(boosted, y, sr),
               "SenseVoice": sv, "SenseVoice+拼音纠错": pinyin_fix(sv)}
    print(f"\n标准答案：{r['文字']}")
    for name, text in results.items():
        print(f"  {name:<16}{cer(r['文字'], text)[0]:>5.0%}  {text}")
