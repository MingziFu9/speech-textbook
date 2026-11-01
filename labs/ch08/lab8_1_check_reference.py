"""实验 8-1 录参考音并检查质量：克隆前先给参考音“体检”，时长、音量、削波、静音、噪声、文字是否对应，逐项打勾。

运行：在 labs/ch08 文件夹里  python lab8_1_check_reference.py
需要模型：python models.py sensevoice
用自己的声音之前，先填好附录 D 的《声音使用授权书》（授权给自己的课程作业）。
"""
import sys

import librosa
import numpy as np
import soundfile as sf

sys.path.append("..")
from voicelab import cer, save_audio, transcribe


def check(file, text):
    """检查一段参考音，返回不合格的项目列表"""
    info = sf.info(file)
    audio, sr = librosa.load(file, sr=None, mono=True)
    dur = len(audio) / sr
    problems = []
    if not 5 <= dur <= 15:
        problems.append(f"时长 {dur:.1f} 秒，建议 5—15 秒")
    if info.channels > 1:
        problems.append("双声道，建议录成单声道")
    if sr < 16000:
        problems.append(f"采样率 {sr} Hz 太低，至少 16000 Hz")
    if np.mean(np.abs(audio) > 0.99) > 0.001:
        problems.append("有削波（声音太大被“削顶”），离麦克风远一点")
    if np.abs(audio).max() < 0.1:
        problems.append("声音太小，靠近一点或调大录音音量")
    frames = librosa.feature.rms(y=audio, frame_length=1024, hop_length=256)[0]
    loud = frames > 0.1 * frames.max()                          # 有声音的帧
    lead, tail = np.argmax(loud) * 256 / sr, np.argmax(loud[::-1]) * 256 / sr
    if lead > 1 or tail > 1:
        problems.append(f"开头静音 {lead:.1f} 秒、结尾静音 {tail:.1f} 秒，剪到 0.5 秒以内")
    snr = 20 * np.log10(np.percentile(frames, 90) / (np.percentile(frames, 10) + 1e-9))
    if snr < 25:
        problems.append(f"背景噪声偏大（信噪比约 {snr:.0f} dB），换个安静的地方")
    heard = transcribe(audio, sr)
    if cer(text, heard)[0] > 0.1:
        problems.append(f"文字对不上：识别结果是“{heard}”")
    return problems


# 1. 准备几段“有问题”的参考音（用虚拟授权人 B 的录音故意做坏）
good = "../data/voices/volunteer_B_1.wav"
text = "大家好，我是社区志愿者，平时负责每周的社区广播和活动通知，很高兴为大家服务。"
audio, sr = librosa.load(good, sr=None)
rng = np.random.default_rng(0)
save_audio("bad_noisy.wav", audio + 0.03 * rng.standard_normal(len(audio)), sr)
save_audio("bad_clipped.wav", np.clip(audio * 5, -1, 1), sr)
save_audio("bad_silence.wav", np.concatenate([np.zeros(3 * sr), audio, np.zeros(3 * sr)]), sr)
cases = [("合格的参考音", good, text),
         ("太短", "../data/voices/ref_B_3s.wav", "大家好，我是社区志愿者。"),
         ("有噪声", "bad_noisy.wav", text),
         ("削波", "bad_clipped.wav", text),
         ("首尾静音太长", "bad_silence.wav", text),
         ("文字写错了", good, "大家好，我是物业的工作人员，负责小区的保洁和绿化。")]

# 2. 逐个检查
for name, file, t in cases:                                      # ← 改这里：换成你自己的录音和文字
    problems = check(file, t)
    print(f"【{name}】", "✓ 合格" if not problems else "✗ " + "；".join(problems))
