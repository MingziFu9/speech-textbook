---
title: 附录 A sherpa-onnx 与音频处理速查
description: 本书用到的 voicelab 小工具、sherpa-onnx 各类模型、音频处理库、ffmpeg 命令和云平台接口的速查表
---

# 附录 A sherpa-onnx 与音频处理速查

这份速查表把全书实验里反复出现的写法集中在一起，做项目时可以直接照着改。每一段代码都摘自配套资源 `labs/` 里实测通过的程序（编者环境：sherpa-onnx 2.0.1，Python 3.12），并注明出处，想看完整的上下文就打开对应的文件。只有 A.6 节的云平台接口是**待实测**的。

## A.1 voicelab 小工具函数 { #a1 }

`labs/voicelab.py` 把常用的几行 sherpa-onnx 代码包装成了函数，第 1—3 章直接用，第 4、6、7、8 章逐个拆开讲。在某一章的文件夹里使用时，先写：

```python
import sys
sys.path.append("..")          # voicelab.py 在上一级的 labs 文件夹里
from voicelab import speak, transcribe, save_audio, read_audio
```

| 函数 | 作用 | 返回 | 第一次出现 |
|---|---|---|---|
| `read_audio(file, sr=16000)` | 读音频文件，变成单声道并转成指定采样率；`sr=None` 表示保持原采样率 | `(采样点数组, 采样率)` | 第 1 章 |
| `save_audio(file, samples, sr)` | 保存成 16 位 WAV 文件 | 文件名 | 第 1 章 |
| `play(samples, sr)` | 在 Notebook 里显示播放条；在命令行里什么也不做 | 无 | 第 1 章 |
| `duration(samples, sr)` | 音频时长 | 秒 | 第 2 章 |
| `speak(text, model="matcha-zh", sid=0, speed=1.0)` | 文字转语音；`model` 可选 `matcha-zh`、`vits-aishell3`、`melo-zh-en`、`kokoro` | `(采样点数组, 采样率)` | 第 1 章 |
| `transcribe(audio, sr=None, model="sensevoice")` | 语音转文字；`audio` 可以是文件名或采样点数组；`model` 可选 `sensevoice`、`paraformer-zh`、`whisper-tiny` | 文字 | 第 1 章 |
| `cer(ref, hyp)` | 字错率，先去掉标点和空格 | `(字错率, 替换, 删除, 插入)` | 第 3 章 |
| `embed(audio, sr=None)` | 提取声纹向量（192 个数，长度已缩放为 1） | 数组 | 第 7 章 |
| `similarity(a, b)` | 两段语音（或两个声纹向量）的余弦相似度，越接近 1 越像同一个人 | 小数 | 第 7 章 |
| `clone(text, ref_audio, ref_text, steps=4, speed=1.0)` | 零样本克隆：用参考音和它的文字，以参考音的音色朗读 `text` | `(采样点数组, 采样率)` | 第 8 章 |
| `model_path(name)` | 某个模型的文件夹；没下载会提示该运行哪条命令 | 路径 | 第 4 章 |

`voicelab.py` 开头的 `THREADS = 2` 是 CPU 线程数，电脑核多可以改成 4。

## A.2 sherpa-onnx 识别类模型 { #a2 }

sherpa-onnx 的用法都是同一个套路：**① 用配置建一个“工具”（识别器、合成器……）→ ② 建一个“流”（stream），把声音喂进去 → ③ 让工具处理这个流 → ④ 取结果**。下面的代码默认已经写了 `import sherpa_onnx as so`，`d` 是模型文件夹 `model_path("模型名")`。

### 整句识别（非流式） { #a2-1 }

一整段录音一次识别完，适合录音文件转写（第 4 章，`voicelab.py`）。

```python
rec = so.OfflineRecognizer.from_sense_voice(model=f"{d}/model.int8.onnx", tokens=f"{d}/tokens.txt",
                                            use_itn=True, num_threads=2)   # use_itn：数字写成阿拉伯数字
stream = rec.create_stream()
stream.accept_waveform(sr, samples)     # samples 是 16 kHz 单声道 float32 数组
rec.decode_stream(stream)
print(stream.result.text)
```

| 模型 | 建识别器的函数 | 主要参数 |
|---|---|---|
| SenseVoice | `from_sense_voice` | `model`、`tokens`、`use_itn` |
| Paraformer | `from_paraformer` | `paraformer`、`tokens` |
| Whisper | `from_whisper` | `encoder`、`decoder`、`tokens`、`language="zh"` |

### 流式识别和热词 { #a2-2 }

边说边出字，适合实时字幕（第 4 章，`ch04/demo4_streaming.py`、`lab4_4_noise_hotwords.py`）。

```python
rec = so.OnlineRecognizer.from_transducer(
    tokens=f"{d}/tokens.txt", encoder=f"{d}/encoder-epoch-99-avg-1.int8.onnx",
    decoder=f"{d}/decoder-epoch-99-avg-1.onnx", joiner=f"{d}/joiner-epoch-99-avg-1.int8.onnx",
    decoding_method="modified_beam_search",              # 用热词时必须是这个
    hotwords_file="my_hotwords.txt", hotwords_score=1.5, num_threads=2)
stream = rec.create_stream()
for start in range(0, len(samples), sr // 2):            # 每次喂 0.5 秒
    stream.accept_waveform(sr, samples[start:start + sr // 2])
    while rec.is_ready(stream):
        rec.decode_stream(stream)
    print(rec.get_result(stream))
```

热词文件每行一个词，**字和字之间用空格隔开**，例如 `幸 福 里`。

### 语音活动检测（VAD） { #a2-3 }

把长录音切成一句一句（第 4 章，`ch04/lab4_2_meeting_srt.py`）。

```python
cfg = so.VadModelConfig()
cfg.silero_vad.model = f"{d}/silero_vad.onnx"
cfg.silero_vad.threshold = 0.5               # 像人声的概率超过它才算有人说话
cfg.silero_vad.min_silence_duration = 0.5    # 静音超过 0.5 秒算一句结束
cfg.silero_vad.min_speech_duration = 0.25    # 太短的声音不算一句
cfg.sample_rate = sr
vad = so.VoiceActivityDetector(cfg, buffer_size_in_seconds=60)
window = cfg.silero_vad.window_size          # 每次喂 512 个采样点
for start in range(0, len(samples), window):
    vad.accept_waveform(samples[start:start + window])
    while not vad.empty():
        seg = vad.front                      # seg.start（采样点位置）、seg.samples（这句话）
        vad.pop()
```

### 唤醒词检测 { #a2-4 }

第 4 章 `ch04/lab4_3_wake_word.py`、第 9 章 `lab9_4_latency.py`。

```python
kws = so.KeywordSpotter(tokens=f"{d}/tokens.txt", encoder=..., decoder=..., joiner=...,
                        keywords_file="my_keywords.txt", keywords_threshold=0.25, num_threads=2)
stream = kws.create_stream()
stream.accept_waveform(sr, samples)
stream.input_finished()
while kws.is_ready(stream):
    kws.decode_stream(stream)
    if kws.get_result(stream):               # 听到唤醒词时返回唤醒词，否则返回空
        print("唤醒！", kws.get_result(stream))
        kws.reset_stream(stream)
```

唤醒词文件要写成带声调的拼音，用 `so.text2token(["你好小站"], tokens=..., tokens_type="ppinyin")` 自动转换，结果形如 `n ǐ h ǎo x iǎo zh àn @你好小站`。

## A.3 sherpa-onnx 合成与克隆 { #a3 }

### 语音合成 { #a3-1 }

四个合成模型的建法只差在“模型配置”这一层（第 6 章，`voicelab.py` 的 `load_tts`）：

```python
m = so.OfflineTtsModelConfig(matcha=so.OfflineTtsMatchaModelConfig(
        acoustic_model=f"{d}/model-steps-3.onnx", vocoder=f"{d}/vocos-22khz-univ.onnx",
        lexicon=f"{d}/lexicon.txt", tokens=f"{d}/tokens.txt", dict_dir=f"{d}/dict"),
    num_threads=2)
tts = so.OfflineTts(so.OfflineTtsConfig(model=m,
        rule_fsts=f"{d}/phone.fst,{d}/date.fst,{d}/number.fst",   # 电话、日期、数字的读法规则
        max_num_sentences=1))
audio = tts.generate("各位居民请注意。", sid=0, speed=1.0)
samples, sr = audio.samples, audio.sample_rate
```

| 模型 | 配置类 | 采样率 | 音色（`sid`） | 要点 |
|---|---|---|---|---|
| Matcha（标贝） | `OfflineTtsMatchaModelConfig` | 22.05 kHz | 1 种女声 | 中文最稳；不认识的字（如“〇”）会跳过，先替换成“零” |
| VITS AISHELL-3 | `OfflineTtsVitsModelConfig` | 8 kHz | 174 种（0—173） | 音色多，音质一般；10、100 号是男声 |
| MeloTTS 中英 | `OfflineTtsVitsModelConfig`（加 `dict_dir`） | 44.1 kHz | 1 种 | 中英混读最好 |
| Kokoro 多语种 | `OfflineTtsKokoroModelConfig` | 24 kHz | 103 种；3—57 中文女声，58—102 中文男声 | 英文缩写要改写（如“A P P”） |

`speed` 大于 1 变快，小于 1 变慢；Matcha 和 VITS 的语速也可以在配置里用 `length_scale` 调（数值越大越慢）。

### 零样本克隆 { #a3-2 }

第 8 章，`voicelab.py` 的 `load_cloner` 和 `clone`。**只能用虚拟授权人或已签授权书的本人录音。**

```python
m = so.OfflineTtsModelConfig(zipvoice=so.OfflineTtsZipvoiceModelConfig(
        tokens=f"{d}/tokens.txt", encoder=f"{d}/encoder.int8.onnx", decoder=f"{d}/decoder.int8.onnx",
        lexicon=f"{d}/lexicon.txt,{d}/lexicon-en-us.txt", vocoder=f"{d}/vocos_24khz.onnx"), num_threads=2)
tts = so.OfflineTts(so.OfflineTtsConfig(model=m))
g = so.GenerationConfig()
g.reference_audio = ref_samples            # 参考音（3—15 秒、干净、只有一个人）
g.reference_sample_rate = ref_sr
g.reference_text = "参考音里说的每一个字"     # 必须和参考音一字不差
g.num_steps = 4                            # 生成步数：1 步不能用，2—4 步性价比最高
g.speed = 1.0
audio = tts.generate("要克隆说的新内容。", g)
```

### 声纹与说话人日志 { #a3-3 }

第 7 章，`voicelab.py` 的 `embed`、`ch07/lab7_3_diarization.py`。

```python
ex = so.SpeakerEmbeddingExtractor(so.SpeakerEmbeddingExtractorConfig(model=f"{d}/3dspeaker_speech_campplus_sv_zh-cn_16k-common.onnx"))
stream = ex.create_stream()
stream.accept_waveform(sr, samples)
stream.input_finished()
v = np.array(ex.compute(stream))           # 192 个数
v = v / np.linalg.norm(v)                  # 缩放成长度 1，之后两个向量点乘就是余弦相似度
```

说话人日志把“分割模型 + 声纹模型 + 聚类”组合在一起：

```python
cfg = so.OfflineSpeakerDiarizationConfig(
    segmentation=so.OfflineSpeakerSegmentationModelConfig(
        pyannote=so.OfflineSpeakerSegmentationPyannoteModelConfig(model=".../model.onnx")),
    embedding=so.SpeakerEmbeddingExtractorConfig(model=".../campplus...onnx"),
    clustering=so.FastClusteringConfig(num_clusters=-1, threshold=0.5),   # 知道人数就写人数
    min_duration_on=0.3, min_duration_off=0.5)
sd = so.OfflineSpeakerDiarization(cfg)
for s in sd.process(samples).sort_by_start_time():
    print(s.start, s.end, s.speaker)       # 起止秒数、第几位发言人
```

## A.4 音频处理库速查 { #a4 }

第 2、3 章大量使用 soundfile、librosa、numpy。下表按“想做什么”排列。

| 想做什么 | 写法 | 说明 |
|---|---|---|
| 读 WAV / FLAC | `y, sr = sf.read("a.wav", dtype="float32")` | `import soundfile as sf`；多声道时 `y` 是二维的 |
| 读任意格式并重采样 | `y, sr = librosa.load("a.mp3", sr=16000)` | `sr=None` 保持原采样率 |
| 写 WAV | `sf.write("b.wav", y, sr, subtype="PCM_16")` | 16 位整数，体积小、兼容性最好 |
| 双声道变单声道 | `y = y.mean(axis=1)` | |
| 重采样 | `librosa.resample(y, orig_sr=44100, target_sr=16000)` | 识别和声纹模型都要 16 kHz |
| 截取一段 | `y[int(1.5 * sr):int(3 * sr)]` | 1.5 秒到 3 秒 |
| 调音量 | `y * 0.5`；归一化 `y / np.abs(y).max() * 0.9` | 乘大于 1 的数可能削波 |
| 拼接 | `np.concatenate([y1, np.zeros(int(0.3 * sr)), y2])` | 中间插 0.3 秒静音；采样率要相同 |
| 去掉首尾静音 | `y2, idx = librosa.effects.trim(y, top_db=30)` | |
| 音量（分贝） | `20 * np.log10(np.sqrt(np.mean(y ** 2)))` | 均方根值换算成 dBFS |
| 短时傅里叶变换 | `S = librosa.stft(y, n_fft=512, hop_length=160)` | 16 kHz 下帧长 32 ms、帧移 10 ms |
| 画语谱图 | `librosa.display.specshow(librosa.amplitude_to_db(abs(S)), sr=sr, hop_length=160, x_axis="time", y_axis="hz")` | 要 `import librosa.display` |
| 梅尔频谱 | `librosa.feature.melspectrogram(y=y, sr=sr, n_mels=80)` | 再用 `librosa.power_to_db` 取对数 |
| MFCC | `librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)` | 加 `librosa.feature.delta` 得到一阶差分 |
| 基频（音高） | `f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr)` | 不发声的帧是 `nan` |
| 动态时间规整 | `D, path = librosa.sequence.dtw(X=mfcc1, Y=mfcc2)` | 第 3 章模板匹配 |
| 降噪 | `noisereduce.reduce_noise(y=y, sr=sr)` | 第 2 章 |

## A.5 ffmpeg 常用命令 { #a5 }

ffmpeg 是处理音视频的命令行工具（安装见[附录 B](b-environment.md#b5)）。在命令行窗口里运行：

| 想做什么 | 命令 |
|---|---|
| 任意格式转成识别用的 WAV | `ffmpeg -i 录音.m4a -ar 16000 -ac 1 录音.wav` |
| WAV 转 MP3（64 kbps） | `ffmpeg -i a.wav -b:a 64k a.mp3` |
| 写入元数据（标题、注释） | `ffmpeg -i a.wav -b:a 64k -metadata title="冬季告居民书" -metadata comment="AI 合成" a.mp3` |
| 读出元数据 | `ffprobe -v error -show_entries format_tags -of default=nw=1 a.mp3` |
| 从视频里提取声音 | `ffmpeg -i 视频.mp4 -vn -ar 16000 -ac 1 声音.wav` |
| 截取第 10 秒开始的 30 秒 | `ffmpeg -i a.wav -ss 10 -t 30 b.wav` |

在 Python 里调用时，把命令拆成列表交给 `subprocess.run`（第 6 章 `lab6_3_audiobook.py`）：

```python
import subprocess
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "a.wav", "-b:a", "64k",
                "-metadata", "comment=本音频由人工智能合成", "a.mp3"], check=True)
```

## A.6 云平台语音接口的一般调用方法（待实测） { #a6 }

国内主要云平台都提供识别、合成、声音复刻服务（4.8 节、6.6 节有介绍）。编者的写作环境不能访问这些服务，本节按各平台官方文档（2026 年 11 月查阅）整理，**待实测**。各平台接口更新很快，使用前一定以官方文档为准。

### 通用步骤 { #a6-1 }

1. **注册并实名认证**：个人账号即可，一般有免费额度。
2. **开通服务**：在控制台找到“语音识别 / 语音合成 / 声音复刻”，点“开通”。
3. **拿到密钥**：创建应用或 API Key。讯飞是 AppID + APIKey + APISecret，阿里云百炼是一个 API Key，火山引擎是 AppID + Access Token。
4. **保存密钥**：放进环境变量，**不要写在代码里，不要上传到网上**。
5. **安装 SDK 或调用网络接口**：按平台文档安装官方的 Python 包；没有 Python 包的，就按文档用 `requests` 或 `websocket` 发请求。
6. **检查计费**：在控制台设置用量提醒，实验结束后关掉不用的服务。

设置环境变量（关掉命令行窗口就失效，适合上课时临时用）：

```bash
# Windows 命令提示符
set DASHSCOPE_API_KEY=你的Key
# macOS / Linux
export DASHSCOPE_API_KEY=你的Key
```

Python 里这样读：`os.environ["DASHSCOPE_API_KEY"]`。

### 各平台入口 { #a6-2 }

| 平台 | 识别 | 合成 | 声音复刻 | Python 调用方式 |
|---|---|---|---|---|
| 阿里云百炼 | Paraformer、Fun-ASR 等 | CosyVoice、Qwen-TTS 等 | CosyVoice 声音复刻 | `pip install dashscope`；大模型对话用 OpenAI 兼容接口 |
| 科大讯飞 讯飞开放平台 | 语音听写、录音文件转写 | 在线语音合成、超拟人合成 | 一句话复刻 | 官方示例多为 WebSocket 接口，按文档的示例代码改 |
| 腾讯云 | 一句话识别、实时识别 | 语音合成 | 声音复刻 | `pip install tencentcloud-sdk-python` |
| 火山引擎 豆包语音 | 流式识别、录音文件识别 | 豆包语音合成 | 声音复刻 | 按文档用 HTTP / WebSocket 接口 |

### 阿里云百炼的写法 { #a6-3 }

本书两个待实测实验都用阿里云百炼：

- **合成**（实验 6-4，`labs/ch06/lab6_4_cloud.py`）：用 `dashscope` 的 `Client` 指定地域和业务空间，调用 CosyVoice 模型，`enable_ssml=True` 时可以用 SSML 控制停顿、多音字和电话号码读法。
- **大模型回答**（实验 9-1 选做，`labs/ch09/llm_answer.py`）：用 `openai` 库连百炼的 OpenAI 兼容接口，地址 `https://dashscope.aliyuncs.com/compatible-mode/v1`，模型名如 `qwen-plus`。

```python
from openai import OpenAI
client = OpenAI(api_key=os.environ["DASHSCOPE_API_KEY"],
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
resp = client.chat.completions.create(model="qwen-plus", messages=[
    {"role": "system", "content": "你是社区语音助手，回答不超过 60 个字。"},
    {"role": "user", "content": "暖气片漏水了找谁修？"}])
print(resp.choices[0].message.content)
```

### 使用云平台的注意事项 { #a6-4 }

- **上传录音就是向第三方提供个人信息**。含居民姓名、电话、住址的录音，先征得同意，或者改用离线模型。
- **声音复刻要授权**。平台一般要求上传者承诺有权使用这段声音，有的还要求本人朗读指定文字验证。不要上传别人的声音（第 8 章）。
- **生成内容要标识**。平台生成的语音同样适用《人工智能生成合成内容标识办法》，发布前加上提示（6.7 节、8.6 节）。
- **记录版本**。在实验报告里写清平台、模型名、音色名和调用日期，结果才能复现。
