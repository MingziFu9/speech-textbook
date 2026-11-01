"""实验 3-3 算一算字错率：先验算 3 个手算例子，再批量识别 8 段来电，算总字错率和实时率。"""
import sys
import time

import pandas as pd

sys.path.append("..")
from voicelab import PUNCT, cer, duration, read_audio, transcribe

# ---------- 第一部分：验算手算的 3 个例子 ----------
examples = [("请尽快处理", "请景快处理"),
            ("楼道里的灯坏了", "楼道的灯坏了了"),
            ("电动车充电桩", "电动车充电装晚上")]
for ref, hyp in examples:
    rate, s, d, i = cer(ref, hyp)
    print(f"参考：{ref}  识别：{hyp}  替换 {s}、删除 {d}、插入 {i}，字错率 {rate:.0%}")

# 英文按“词”算，叫词错率（WER）：把句子按空格切成词的列表，再交给同一个函数
rate, s, d, i = cer("turn on the light please".split(), "turn of the light".split())
print(f"英文词错率：替换 {s}、删除 {d}、插入 {i}，词错率 {rate:.0%}")

# ---------- 第二部分：批量识别 8 段来电 ----------
DIGITS = str.maketrans("零一二三四五六七八九", "0123456789")


def normalize(text):
    """统一写法：把中文数字换成阿拉伯数字（参考答案和识别结果都换，写法就一致了）"""
    return text.translate(DIGITS)


truth = pd.read_csv("../data/calls/calls.csv")
model = "sensevoice"                          # ← 改这里：试试 "paraformer-zh"（第 4 章详细比较）
transcribe("../data/calls/call_01.wav", model=model)    # 先识别一次，把模型加载好，不算进用时

rows, total_err, total_err_norm, total_chars, total_audio, total_time = [], 0, 0, 0, 0.0, 0.0
for _, r in truth.iterrows():
    y, sr = read_audio(f"../data/calls/{r['文件']}")
    start = time.time()
    hyp = transcribe(y, sr, model=model)
    used = time.time() - start
    rate, s, d, i = cer(r["文字"], hyp)
    rate_n, s_n, d_n, i_n = cer(normalize(r["文字"]), normalize(hyp))
    n_chars = len([c for c in r["文字"] if c not in PUNCT])    # 参考文本的字数（不算标点）
    total_err += s + d + i
    total_err_norm += s_n + d_n + i_n
    total_chars += n_chars
    total_audio += duration(y, sr)
    total_time += used
    rows.append([r["文件"], n_chars, s, d, i, f"{rate:.0%}", f"{rate_n:.0%}", hyp])

table = pd.DataFrame(rows, columns=["文件", "字数", "替换", "删除", "插入", "字错率", "统一写法后", "识别结果"])
pd.set_option("display.width", 200)
print(table.to_string(index=False))
print(f"总字错率 = 错误总数 {total_err} ÷ 总字数 {total_chars} = {total_err / total_chars:.1%}")
print(f"统一写法后总字错率 = {total_err_norm} ÷ {total_chars} = {total_err_norm / total_chars:.1%}")
print(f"实时率 RTF = 识别用时 {total_time:.2f} 秒 ÷ 音频时长 {total_audio:.1f} 秒 = {total_time / total_audio:.3f}")
table.to_csv("cer_report.csv", index=False, encoding="utf-8-sig")
print("已保存 cer_report.csv")
