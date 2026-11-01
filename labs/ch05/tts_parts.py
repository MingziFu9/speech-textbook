"""把 Matcha 合成拆成两半，分别调用（第 5 章实验 5-3、5-4 用）：
    声学模型 acoustic_model(拼音列表) → 梅尔频谱
    声码器   vocoder(梅尔频谱, "vocos" 或 "hifigan") → 声音
sherpa-onnx 的 speak() 内部做的也是这两步，这里直接用 onnxruntime 运行两个模型文件，方便看中间结果。
"""
import sys
from functools import lru_cache

import librosa
import numpy as np
import onnxruntime as ort

sys.path.append("..")
from models import path as model_path

SR = 22050                                   # Matcha 中文模型和两个声码器的采样率


@lru_cache(maxsize=None)
def _session(file):
    return ort.InferenceSession(str(file), providers=["CPUExecutionProvider"])


@lru_cache(maxsize=None)
def _tokens():
    table = {}
    for line in open(model_path("matcha-zh") / "tokens.txt", encoding="utf-8"):
        sym, idx = line.rstrip("\n").rsplit(" ", 1)
        table[sym] = int(idx)
    return table


def acoustic_model(pinyin, speed=1.0, noise=0.667):
    """拼音列表 → 梅尔频谱（80 行 × 帧数，每帧约 11.6 毫秒）。标点控制停顿，认不出的符号跳过"""
    table, ids = _tokens(), []
    for p in pinyin:
        p = {"，": ",", "、": ",", "；": ",", "：": ",", "。": ".", "！": "!", "？": "?"}.get(p, p)
        if p in table:
            ids += [table[p], 1]                 # 每个音后面插一个“间隔”符号（编号 1），这个模型训练时就是这样
    ids = [1] + ids
    mel = _session(model_path("matcha-zh") / "model-steps-3.onnx").run(None, {
        "x": np.array([ids], dtype=np.int64), "x_length": np.array([len(ids)], dtype=np.int64),
        "noise_scale": np.array([noise], dtype=np.float32),       # 随机程度：越大每次越不一样
        "length_scale": np.array([1 / speed], dtype=np.float32)})[0]
    return mel[0]


def vocoder(mel, name="vocos"):
    """梅尔频谱 → 声音采样点。name 可选 "vocos"、"hifigan"（神经网络声码器）或 "griffinlim"（传统算法，不用模型）"""
    if name == "griffinlim":                     # Griffin-Lim：反复猜测相位，迭代 32 次
        return librosa.feature.inverse.mel_to_audio(np.exp(mel), sr=SR, n_fft=1024, hop_length=256,
                                                    power=1.0, n_iter=32, fmin=0, fmax=8000)
    if name == "hifigan":                        # HiFi-GAN：直接输出波形
        return _session(model_path("hifigan") / "hifigan_v2.onnx").run(None, {"mel": mel[None]})[0][0]
    mag, x, y = _session(model_path("matcha-zh") / "vocos-22khz-univ.onnx").run(None, {"mels": mel[None]})
    spec = mag[0] * (x[0] + 1j * y[0])           # Vocos：输出每一帧的频谱，再用逆傅里叶变换变回波形
    return librosa.istft(spec, hop_length=256, win_length=1024, n_fft=1024, window="hann", center=True)
