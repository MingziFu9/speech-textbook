"""实验 3-4（选做）语言模型来纠错：用社区通知训练一个“二元语言模型”，给读音相同的候选句打分，选出最通顺的一句。

二元语言模型只统计一件事：在训练文字里，每个字后面跟着哪个字、出现了多少次。
“充电”后面常跟“桩”，很少跟“装”，所以“充电桩”得分高。
"""
import math
from collections import Counter

from pypinyin import lazy_pinyin

# ---------- 第 1 步：训练。数一数每个字、每两个相邻的字各出现几次 ----------
text = open("../data/corpus/community.txt", encoding="utf-8").read()    # 47 句社区通知和服务用语
extra = []          # ← 改这里：加几句别的文字再训练，如 ["下周举行期中考试，请同学们认真复习。"]
lines = ["^" + line.strip() + "$" for line in text.splitlines() + extra if line.strip()]   # ^ 和 $ 表示句首、句尾
one = Counter(c for line in lines for c in line)                                  # 单个字的次数
two = Counter(line[i:i + 2] for line in lines for i in range(len(line) - 1))      # 相邻两个字的次数
V = len(one)                                                                      # 一共见过多少种字
print(f"训练文字 {len(lines)} 句、{sum(one.values()) - 2 * len(lines)} 个字，{V} 种字，{len(two)} 种相邻字对")


def lm_score(sentence):
    """句子得分 = 每个字“跟在前一个字后面”的对数概率之和，越大（越接近 0）越通顺"""
    s = "^" + sentence + "$"
    score = 0.0
    for a, b in zip(s, s[1:]):
        p = (two[a + b] + 1) / (one[a] + V)          # 加 1 平滑：没见过的字对也给一点点概率，不至于是 0
        score += math.log(p)
    return score


# ---------- 第 2 步：给候选句打分 ----------
groups = [  # 每组候选句读音相同（声调可以不同），模拟识别模型“听”到的几种可能
    ["电动车充电桩晚上总是排队", "电动车充电装晚上总是排队", "电动车冲点桩晚上总是排队"],
    ["七号楼门口的快递柜坏了请尽快处理", "七号楼门口的快递柜坏了请景快处理", "七号楼门口的快递贵坏了请尽快处理"],
    ["请问社区卫生服务站周日开门吗", "请问社区医生服务站周日开门吗"],        # 读音不同，看语言模型能不能帮上忙
    ["我想报名参加志愿服务", "我想报名参加自愿服务", "我想报名参加志愿伏乌"],
    ["下周举行期中考试", "下周举行期终考试", "下周举行其中考试"],           # ← 改这里：自己加一组
]

for group in groups:
    print("读音：", " ".join(lazy_pinyin(group[0])))
    for rank, (score, s) in enumerate(sorted(((lm_score(s), s) for s in group), reverse=True), 1):
        print(f"  {score:7.1f}  {s}{'  ← 选它' if rank == 1 else ''}")
