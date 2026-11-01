"""社区语音问答小助手（第 9 章实验 9-1、9-2、9-4 共用）：听 → 懂 → 答 → 说。

    ask(audio, sr)  输入一段居民的语音，返回识别文字、匹配到的问答、回答文字、回答语音和各环节耗时
"""
import csv
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from voicelab import speak, transcribe  # noqa: E402

FAQ_FILE = Path(__file__).resolve().parent.parent / "data/faq/community_faq.csv"
FALLBACK = "抱歉，这个问题我还不会回答。您可以换个说法再问一次，或者拨打社区服务热线找工作人员。"


def load_faq(file=FAQ_FILE):
    with open(file, encoding="utf-8-sig") as f:
        return [dict(r, 关键词=r["关键词"].split()) for r in csv.DictReader(f)]


FAQ = load_faq()


def understand(text):
    """“理解”：数一数问题里出现了每条问答的几个关键词，选出现最多的；一个都没有就返回 None"""
    best, score = None, 0
    for item in FAQ:
        hits = sum(1 for w in item["关键词"] if w in text)
        if hits > score:
            best, score = item, hits
    return best


def ask(audio, sr, voice="matcha-zh"):
    t = {}
    start = time.time()
    heard = transcribe(audio, sr)                                       # 1. 听：语音识别
    t["识别"] = time.time() - start

    start = time.time()
    item = understand(heard)                                            # 2. 懂：关键词匹配
    reply = item["回答"] if item else FALLBACK
    t["理解"] = time.time() - start

    start = time.time()
    first = reply.split("，")[0] + "。"                                 # 先合成第一小句，尽快开口
    speak(first, model=voice)
    t["首句合成"] = time.time() - start
    reply_audio, reply_sr = speak(reply, model=voice)                   # 3. 说：合成整段回答
    t["全部合成"] = time.time() - start
    return {"heard": heard, "faq": item["编号"] if item else "0", "reply": reply,
            "audio": reply_audio, "sr": reply_sr, "time": t}
