"""生成本书实验用的示例音频（编者已经运行过，生成的文件就在 data/ 里，学生不用运行）。

用法：在 labs 文件夹里运行  python data/make_audio.py
需要先下载模型：python models.py kokoro && python models.py matcha-zh && python models.py vits-aishell3

说明：
- 书里所有“居民”“志愿者”“议事会成员”的声音都是用开源合成模型 Kokoro（Apache-2.0）的内置音色生成的，
  不是任何真实人物的录音。第 8 章把这些音色当作“虚拟授权人”，用来练习语音克隆。
- 文字内容是编者编写的“社区语音服务站”场景，人名、楼号都是虚构的。
"""
import csv
import sys
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf

LABS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(LABS))
from voicelab import save_audio, speak  # noqa: E402

DATA = LABS / "data"
rng = np.random.default_rng(42)


def say(text, sid, sr=16000, speed=1.0):
    s, r = speak(text, model="kokoro", sid=sid, speed=speed)
    return librosa.resample(s, orig_sr=r, target_sr=sr) if sr != r else s


def silence(sec, sr=16000):
    return np.zeros(int(sec * sr), np.float32)


def write_csv(file, rows, header):
    with open(file, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ---------- 第 2 章：几种声音 ----------
def make_sounds():
    out = DATA / "sounds"
    out.mkdir(exist_ok=True)
    sr = 16000
    for name, text in [("vowel_a", "啊"), ("vowel_i", "衣"), ("vowel_u", "乌")]:
        s = say(text, sid=20, speed=0.4)
        save_audio(out / f"{name}.wav", s, sr)
    t = np.arange(int(1.5 * sr)) / sr
    whistle = 0.3 * np.sin(2 * np.pi * (1800 + 200 * np.sin(2 * np.pi * 2 * t)) * t)  # 口哨：一个上下滑动的高音
    save_audio(out / "whistle.wav", whistle * np.hanning(len(t)), sr)
    save_audio(out / "noise.wav", 0.1 * rng.standard_normal(len(t)).astype(np.float32), sr)
    knock = np.zeros(len(t), np.float32)
    for start in (0.2, 0.6, 1.0):                                  # 敲三下门
        i = int(start * sr)
        n = int(0.05 * sr)
        knock[i:i + n] = 0.8 * rng.standard_normal(n) * np.exp(-np.arange(n) / (0.008 * sr))
    save_audio(out / "knock.wav", knock, sr)
    s = say("同学们好，欢迎来到社区语音服务站。今天我们一起看看，声音在电脑里是什么样子。", sid=20, sr=44100)
    save_audio(out / "speech_44k.wav", s, 44100)


# ---------- 第 2、4 章：居民来电（故意做成格式不统一、有问题的录音） ----------
CALLS = [
    # 编号, 音色, 文字, 问题
    (1, 10, "你好，我想问一下，这周六的垃圾分类宣传活动是几点开始？", "正常"),
    (2, 65, "我是五号楼的住户，楼道里的灯坏了好几天了，麻烦物业来修一下。", "双声道 44.1 kHz"),
    (3, 30, "请问社区卫生服务站周日上午开门吗？我想带孩子去打疫苗。", "声音太小"),
    (4, 80, "电动车充电桩晚上总是排队，能不能再多装几个？", "前后有 3 秒静音"),
    (5, 45, "我家老人不会用手机挂号，社区有没有人可以帮忙？", "有背景噪声"),
    (6, 90, "七号楼门口的快递柜坏了，取不出包裹，请尽快处理。", "声音太大、削波"),
    (7, 15, "你好，社区的老年食堂中午几点开饭？一份套餐多少钱？", "8 kHz 电话录音"),
    (8, 70, "下周的议事会我想提一个建议，能不能在小区里多装几个休息的长椅。", "正常"),
]


def make_calls():
    out = DATA / "calls"
    out.mkdir(exist_ok=True)
    rows = []
    for n, sid, text, problem in CALLS:
        sr = 16000
        s = say(text, sid)
        s = np.concatenate([silence(0.3), s, silence(0.3)])
        if problem == "双声道 44.1 kHz":
            sr = 44100
            s = librosa.resample(s, orig_sr=16000, target_sr=sr)
            s = np.stack([s, 0.9 * s], axis=1)
        elif problem == "声音太小":
            s = s * 0.05
        elif problem == "前后有 3 秒静音":
            s = np.concatenate([silence(3), s, silence(3)])
        elif problem == "有背景噪声":
            s = s + 0.03 * rng.standard_normal(len(s)).astype(np.float32)
        elif problem == "声音太大、削波":
            s = np.clip(s * 4, -1, 1)
        elif problem == "8 kHz 电话录音":
            sr = 8000
            s = librosa.resample(s, orig_sr=16000, target_sr=sr)
        file = out / f"call_{n:02d}.wav"
        sf.write(file, s, sr, subtype="PCM_16")
        rows.append([file.name, text, problem])
    write_csv(out / "calls.csv", rows, ["文件", "文字", "录音问题"])


# ---------- 第 4、7 章：议事会录音（三个人轮流发言） ----------
MEETING = [
    ("主持人", 5, "大家晚上好，今天议事会讨论两件事，第一是电动车充电桩，第二是垃圾分类。"),
    ("老王", 70, "我先说充电桩，楼下现在只有四个桩，晚上经常排队。"),
    ("李阿姨", 30, "我同意多装几个，不过要注意消防安全，不能在楼道里充电。"),
    ("主持人", 5, "好的，那我们下周请物业来现场看一看。"),
    ("老王", 70, "垃圾分类这边，我建议在每栋楼前增加一个厨余垃圾桶。"),
    ("李阿姨", 30, "还要安排志愿者在早上七点到九点值班，提醒大家分好类再扔。"),
    ("主持人", 5, "这两个建议我都记下了，会后整理成纪要发到业主群。"),
]


def make_meeting():
    out = DATA / "meeting"
    out.mkdir(exist_ok=True)
    parts, rows, t = [silence(0.5)], [], 0.5
    for who, sid, text in MEETING:
        s = say(text, sid)
        rows.append([f"{t:.2f}", f"{t + len(s) / 16000:.2f}", who, text])
        parts += [s, silence(0.8)]
        t += len(s) / 16000 + 0.8
    save_audio(out / "meeting.wav", np.concatenate(parts), 16000)
    write_csv(out / "meeting_truth.csv", rows, ["开始秒", "结束秒", "发言人", "文字"])


# ---------- 第 4 章：唤醒词测试 ----------
KWS = [("你好小站，帮我查一下垃圾分类时间。", True), ("你好小站，明天会下雨吗？", True),
       ("小站小站，播放社区通知。", True), ("你好小张，今天天气不错。", False),
       ("你好，小朋友们在站台等车。", False), ("今天去超市买菜。", False)]


def make_kws():
    out = DATA / "kws"
    out.mkdir(exist_ok=True)
    rows = []
    for i, (text, positive) in enumerate(KWS, 1):
        for sid in (20, 60, 90):
            file = out / f"kws_{i}_{sid}.wav"
            save_audio(file, say(text, sid), 16000)
            rows.append([file.name, text, "是" if positive else "否"])
    write_csv(out / "kws.csv", rows, ["文件", "文字", "含唤醒词"])


# ---------- 第 7、8 章：虚拟授权人（声纹、克隆用） ----------
VOICES = [  # 代号, 音色, 性别
    ("A", 20, "女"), ("B", 45, "女"), ("C", 65, "男"), ("D", 85, "男")]
VOICE_TEXTS = [
    "大家好，我是社区志愿者，平时负责每周的社区广播和活动通知，很高兴为大家服务。",
    "今天天气不错，我们组织了几位老人去公园散步，大家都很开心。",
    "请各位居民注意，明天上午九点到十一点小区停水，请提前储水。",
]


def make_voices():
    out = DATA / "voices"
    out.mkdir(exist_ok=True)
    rows = []
    for code, sid, gender in VOICES:
        for k, text in enumerate(VOICE_TEXTS, 1):
            file = out / f"volunteer_{code}_{k}.wav"
            s, sr = speak(text, model="kokoro", sid=sid)
            save_audio(file, s, sr)                      # 保留 24 kHz 原始采样率，克隆时用
            rows.append([file.name, code, gender, sid, text])
    # 一段“不知道是谁”的录音，第 7 章让学生用声纹判断是 A、B、C、D 里的哪一位
    s, sr = speak("你好，我想报名参加下周的社区义诊志愿服务。", model="kokoro", sid=65)
    save_audio(out / "unknown.wav", s, sr)
    rows.append(["unknown.wav", "?", "?", 65, "你好，我想报名参加下周的社区义诊志愿服务。"])
    write_csv(out / "voices.csv", rows, ["文件", "代号", "性别", "Kokoro 音色编号", "文字"])


if __name__ == "__main__":
    for f in (make_sounds, make_calls, make_meeting, make_kws, make_voices):
        print("生成", f.__name__)
        f()
    print("完成")
