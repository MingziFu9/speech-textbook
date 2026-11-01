"""一个简单的中文文本前端：把文字变成合成模型能用的“发音说明书”（第 5 章实验 5-1、5-3 共用）。

三步：
    1. normalize(text)   文本正则化：数字、日期、金额、百分数、电话号码 → 汉字读法
    2. segment(text)     分词（jieba）
    3. to_pinyin(text)   注音：带声调的拼音（pypinyin），再修正多音字和“一”“不”的变调
"""
import re

import jieba
from pypinyin import Style, lazy_pinyin, load_phrases_dict

jieba.setLogLevel(60)
DIGIT = "零一二三四五六七八九"


# ---------------- 1. 文本正则化 ----------------
def read_digits(s, one="一"):
    """逐位读：2026 → 二零二六；电话号码里的 1 读“幺”"""
    return "".join(one if c == "1" else DIGIT[int(c)] for c in s)


def read_number(s):
    """按数值读整数（0—99999999）：305 → 三百零五，12 → 十二"""
    n = int(s)
    if n == 0:
        return "零"
    if n >= 10000:
        high, low = divmod(n, 10000)
        rest = read_number(str(low)) if low else ""
        return read_number(str(high)) + "万" + ("零" + rest if 0 < low < 1000 else rest)
    out, zero = "", False
    for unit, value in (("千", 1000), ("百", 100), ("十", 10), ("", 1)):
        d, n = divmod(n, value)
        if d:
            out += ("零" if zero else "") + DIGIT[d] + unit
            zero = False
        elif out:
            zero = True
    return out[1:] if out.startswith("一十") else out      # 12 读“十二”，不读“一十二”


def read_decimal(s):
    whole, _, frac = s.partition(".")
    return read_number(whole) + ("点" + read_digits(frac) if frac else "")


RULES = [  # (规则说明, 正则表达式, 怎么读)；按顺序替换，越具体的规则越靠前
    ("手机号", r"1\d{10}", lambda m: read_digits(m.group(), one="幺")),
    ("日期", r"(\d{4})[-/年](\d{1,2})[-/月](\d{1,2})日?",
     lambda m: f"{read_digits(m[1])}年{read_number(m[2])}月{read_number(m[3])}日"),
    ("年份", r"(\d{4})年", lambda m: read_digits(m[1]) + "年"),
    ("时刻", r"(\d{1,2}):(\d{2})", lambda m: read_number(m[1]) + "点" + (read_number(m[2]) + "分" if m[2] != "00" else "")),
    ("百分数", r"(\d+(?:\.\d+)?)%", lambda m: "百分之" + read_decimal(m[1])),
    ("人民币", r"[¥￥](\d+(?:\.\d+)?)", lambda m: read_decimal(m[1]) + "元"),
    ("几号楼", r"(\d+)(号|栋|单元|室|楼)", lambda m: (read_digits(m[1]) if len(m[1]) > 2 else read_number(m[1])) + m[2]),
    ("负数", r"(?<![\d\w])-(\d+(?:\.\d+)?)", lambda m: "负" + read_decimal(m[1])),
    ("小数和整数", r"\d+(?:\.\d+)?", lambda m: read_decimal(m.group())),
]


def normalize(text, verbose=False):
    for name, pattern, how in RULES:
        if verbose:
            for m in re.finditer(pattern, text):
                print(f"  [{name}] {m.group()} → {how(m)}")
        text = re.sub(pattern, how, text)
    return text


# ---------------- 2. 分词 ----------------
def segment(text):
    return jieba.lcut(text)


# ---------------- 3. 注音 ----------------
# pypinyin 自带的词典读错的词，在这里补上正确读音（← 改这里：发现读错的词就加进来）
load_phrases_dict({"大夫": [["dài"], ["fu"]], "单县": [["shàn"], ["xiàn"]],
                   "一样": [["yí"], ["yàng"]], "一天": [["yì"], ["tiān"]]})


def to_pinyin(text):
    """返回 [(字, 拼音), ...]，拼音用数字表示声调（轻声不带数字），标点原样保留"""
    pys = lazy_pinyin(text, style=Style.TONE3, tone_sandhi=True, errors=lambda s: list(s))
    pairs = list(zip(text, pys))
    # “一”“不”的变调：在第四声前读第二声；“一”在第一、二、三声前读第四声；“第一”“十一”和句末不变
    for i, (ch, py) in enumerate(pairs):
        if ch not in "一不" or i + 1 >= len(pairs) or not pairs[i + 1][1][-1:].isdigit():
            continue
        if i > 0 and pairs[i - 1][0] in "第十" + DIGIT:
            continue
        nxt = pairs[i + 1][1][-1]
        if nxt == "4":
            pairs[i] = (ch, py[:-1] + "2")
        elif ch == "一":
            pairs[i] = (ch, "yi4")
    return pairs


def frontend(text, verbose=True):
    """完整的前端：返回拼音列表（标点保留，合成模型用它控制停顿）"""
    if verbose:
        print("原文：", text)
    spoken = normalize(text, verbose)
    words = segment(spoken)
    pairs = to_pinyin(spoken)
    if verbose:
        print("分词：", " / ".join(words))
        print("拼音：", " ".join(p for _, p in pairs))
    return [p for _, p in pairs]
