"""实验 5-1 做一个文本前端：把一条社区通知变成带声调的拼音，看正则化、分词、多音字和变调各做了什么。"""
from frontend import frontend, normalize, to_pinyin

notice = ("社区通知：2026-11-08（周六）9:30，在3号楼前举行垃圾分类宣传活动，预计参加约120人。"
          "报名电话13912345678，活动经费¥1500，比去年增加12.5%。"
          "请到一楼大厅找王大夫领取材料，银行的工作人员也会到场，介绍重新办理社保卡的流程。")  # ← 改这里

print("========== 完整的前端 ==========")
pinyin = frontend(notice)

print("\n========== 逐项检查 ==========")
cases = ["2026-11-08", "9:30", "3号楼", "120人", "13912345678", "¥1500", "12.5%", "-3度",   # 数字
         "银行", "行走", "重庆", "重新", "大夫", "单县",                                     # 多音字
         "一个", "一天", "第一", "一楼", "不对", "不好", "你好"]                              # 变调
for c in cases:
    spoken = normalize(c)
    print(f"{c:<12}→ {spoken:<14} {' '.join(p for _, p in to_pinyin(spoken))}")

with open("notice_pinyin.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(pinyin))
print("\n已保存 notice_pinyin.txt（实验 5-3 会把它交给声学模型）")
