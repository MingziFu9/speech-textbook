"""本书实验的公共小工具：读写音频、识别、合成、声纹、克隆、字错率。

每个函数背后都是几行 sherpa-onnx 代码，第 4、6、7、8 章会把它们一一拆开讲。
前几章先直接用，像用手机 App 一样：

    from voicelab import speak, transcribe, save_audio
    samples, sr = speak("你好，欢迎来到社区语音服务站。")
    save_audio("hello.wav", samples, sr)
    print(transcribe("hello.wav"))

模型要先下载：在 labs 文件夹里运行 python models.py ch01（第几章就写几）。
"""
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
import soundfile as sf

LABS = Path(__file__).resolve().parent
sys.path.insert(0, str(LABS))
from models import path as model_path  # noqa: E402

THREADS = 2        # CPU 线程数，电脑核多可以改大


# ---------------- 读写和播放音频 ----------------

def read_audio(file, sr=16000):
    """读一个音频文件，转成单声道、指定采样率（默认 16000），返回 (采样点数组, 采样率)"""
    samples, file_sr = sf.read(str(file), dtype="float32", always_2d=True)
    samples = samples.mean(axis=1)                    # 多声道取平均变成单声道
    if sr and file_sr != sr:
        import librosa
        samples = librosa.resample(samples, orig_sr=file_sr, target_sr=sr)
        file_sr = sr
    return samples.astype(np.float32), file_sr


def save_audio(file, samples, sr):
    """把采样点保存成 16 位 WAV 文件"""
    sf.write(str(file), np.asarray(samples, dtype=np.float32), sr, subtype="PCM_16")
    return file


def play(samples, sr):
    """在 Notebook 里显示一个播放条；在命令行里运行时什么也不做（请打开保存的 WAV 文件听）"""
    try:
        from IPython import get_ipython
        from IPython.display import Audio, display
        if get_ipython() is not None:
            display(Audio(np.asarray(samples), rate=sr))
    except ImportError:
        pass


def duration(samples, sr):
    """音频时长（秒）"""
    return len(samples) / sr


# ---------------- 语音合成 ----------------

@lru_cache(maxsize=None)
def load_tts(name="matcha-zh"):
    """加载一个合成模型：matcha-zh（中文女声）、vits-aishell3（174 种音色）、melo-zh-en（中英混读）、kokoro（多语种）"""
    import sherpa_onnx as so
    d = model_path(name)
    if name == "matcha-zh":
        m = so.OfflineTtsModelConfig(matcha=so.OfflineTtsMatchaModelConfig(
            acoustic_model=f"{d}/model-steps-3.onnx", vocoder=f"{d}/vocos-22khz-univ.onnx",
            lexicon=f"{d}/lexicon.txt", tokens=f"{d}/tokens.txt", dict_dir=f"{d}/dict"))
        fsts = f"{d}/phone.fst,{d}/date.fst,{d}/number.fst"
    elif name == "vits-aishell3":
        m = so.OfflineTtsModelConfig(vits=so.OfflineTtsVitsModelConfig(
            model=f"{d}/model.onnx", lexicon=f"{d}/lexicon.txt", tokens=f"{d}/tokens.txt"))
        fsts = f"{d}/phone.fst,{d}/date.fst,{d}/number.fst,{d}/new_heteronym.fst"
    elif name == "melo-zh-en":
        m = so.OfflineTtsModelConfig(vits=so.OfflineTtsVitsModelConfig(
            model=f"{d}/model.onnx", lexicon=f"{d}/lexicon.txt", tokens=f"{d}/tokens.txt",
            dict_dir=f"{d}/dict"))
        fsts = f"{d}/phone.fst,{d}/date.fst,{d}/number.fst,{d}/new_heteronym.fst"
    elif name == "kokoro":
        m = so.OfflineTtsModelConfig(kokoro=so.OfflineTtsKokoroModelConfig(
            model=f"{d}/model.int8.onnx", voices=f"{d}/voices.bin", tokens=f"{d}/tokens.txt",
            data_dir=f"{d}/espeak-ng-data", dict_dir=f"{d}/dict",
            lexicon=f"{d}/lexicon-us-en.txt,{d}/lexicon-zh.txt"))
        fsts = f"{d}/phone-zh.fst,{d}/date-zh.fst,{d}/number-zh.fst"
    else:
        raise ValueError(f"不认识的合成模型：{name}")
    m.num_threads = THREADS
    return so.OfflineTts(so.OfflineTtsConfig(model=m, rule_fsts=fsts, max_num_sentences=1))


def speak(text, model="matcha-zh", sid=0, speed=1.0):
    """把文字合成为语音，返回 (采样点, 采样率)。sid 是说话人编号，speed 是语速（1.0 为正常）"""
    audio = load_tts(model).generate(text, sid=sid, speed=speed)
    return np.array(audio.samples, dtype=np.float32), audio.sample_rate


# ---------------- 语音识别 ----------------

@lru_cache(maxsize=None)
def load_asr(name="sensevoice"):
    """加载一个识别模型：sensevoice（默认，带标点）、paraformer-zh、whisper-tiny"""
    import sherpa_onnx as so
    d = model_path(name)
    if name == "sensevoice":
        return so.OfflineRecognizer.from_sense_voice(model=f"{d}/model.int8.onnx", tokens=f"{d}/tokens.txt",
                                                     use_itn=True, num_threads=THREADS)
    if name == "paraformer-zh":
        return so.OfflineRecognizer.from_paraformer(paraformer=f"{d}/model.int8.onnx", tokens=f"{d}/tokens.txt",
                                                    num_threads=THREADS)
    if name == "whisper-tiny":
        return so.OfflineRecognizer.from_whisper(encoder=f"{d}/tiny-encoder.int8.onnx",
                                                 decoder=f"{d}/tiny-decoder.int8.onnx",
                                                 tokens=f"{d}/tiny-tokens.txt", language="zh", num_threads=THREADS)
    raise ValueError(f"不认识的识别模型：{name}")


def transcribe(audio, sr=None, model="sensevoice"):
    """把一段语音转成文字。audio 可以是文件名，也可以是采样点数组（这时要给 sr）"""
    if isinstance(audio, (str, Path)):
        audio, sr = read_audio(audio)
    rec = load_asr(model)
    stream = rec.create_stream()
    stream.accept_waveform(sr, np.asarray(audio, dtype=np.float32))
    rec.decode_stream(stream)
    return stream.result.text.strip()


# ---------------- 声纹 ----------------

@lru_cache(maxsize=None)
def load_speaker():
    import sherpa_onnx as so
    d = model_path("speaker")
    cfg = so.SpeakerEmbeddingExtractorConfig(model=f"{d}/3dspeaker_speech_campplus_sv_zh-cn_16k-common.onnx",
                                             num_threads=THREADS)
    return so.SpeakerEmbeddingExtractor(cfg)


def embed(audio, sr=None):
    """提取一段语音的声纹向量（192 个数，已经缩放成长度为 1）"""
    if isinstance(audio, (str, Path)):
        audio, sr = read_audio(audio)
    ex = load_speaker()
    stream = ex.create_stream()
    stream.accept_waveform(sr, np.asarray(audio, dtype=np.float32))
    stream.input_finished()
    v = np.array(ex.compute(stream))
    return v / np.linalg.norm(v)


def similarity(a, b):
    """两段语音（或两个声纹向量）的余弦相似度，越接近 1 越像同一个人"""
    va = a if isinstance(a, np.ndarray) and a.ndim == 1 and len(a) < 1000 else embed(a)
    vb = b if isinstance(b, np.ndarray) and b.ndim == 1 and len(b) < 1000 else embed(b)
    return float(va @ vb)


# ---------------- 零样本克隆 ----------------

@lru_cache(maxsize=None)
def load_cloner():
    import sherpa_onnx as so
    d = model_path("zipvoice")
    m = so.OfflineTtsModelConfig(zipvoice=so.OfflineTtsZipvoiceModelConfig(
        tokens=f"{d}/tokens.txt", encoder=f"{d}/encoder.int8.onnx", decoder=f"{d}/decoder.int8.onnx",
        lexicon=f"{d}/lexicon.txt,{d}/lexicon-en-us.txt", vocoder=f"{d}/vocos_24khz.onnx"), num_threads=THREADS)
    return so.OfflineTts(so.OfflineTtsConfig(model=m))


def clone(text, ref_audio, ref_text, ref_sr=None, steps=4, speed=1.0):
    """用参考音（ref_audio）和它对应的文字（ref_text）克隆音色，朗读 text。返回 (采样点, 采样率)"""
    import sherpa_onnx as so
    if isinstance(ref_audio, (str, Path)):
        ref_audio, ref_sr = read_audio(ref_audio, sr=None)
    g = so.GenerationConfig()
    g.reference_audio = np.asarray(ref_audio, dtype=np.float32)
    g.reference_sample_rate = ref_sr
    g.reference_text = ref_text
    g.num_steps = steps
    g.speed = speed
    g.extra["min_char_in_sentence"] = "30"
    audio = load_cloner().generate(text, g)
    return np.array(audio.samples, dtype=np.float32), audio.sample_rate


# ---------------- 字错率 ----------------

PUNCT = set("，。！？、；：,.!?;:“”\"'‘’（）() 　")


def cer(ref, hyp):
    """字错率 = (替换 + 删除 + 插入) / 参考文本字数；会先去掉标点和空格。返回 (字错率, 替换, 删除, 插入)"""
    r = [c for c in ref if c not in PUNCT]
    h = [c for c in hyp if c not in PUNCT]
    # d[i][j] = (总错误, 替换, 删除, 插入)：r 的前 i 个字变成 h 的前 j 个字最少要几步
    d = [[(j, 0, 0, j) for j in range(len(h) + 1)]]
    for i in range(1, len(r) + 1):
        row = [(i, 0, i, 0)]
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                row.append(d[i - 1][j - 1])
                continue
            s, dl, ins = d[i - 1][j - 1], d[i - 1][j], row[j - 1]
            row.append(min((s[0] + 1, s[1] + 1, s[2], s[3]), (dl[0] + 1, dl[1], dl[2] + 1, dl[3]),
                           (ins[0] + 1, ins[1], ins[2], ins[3] + 1)))
        d.append(row)
    total, sub, dele, ins = d[-1][-1]
    return (total / len(r) if r else 0.0), sub, dele, ins
