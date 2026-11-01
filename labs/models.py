"""下载本书用到的离线语音模型（全部来自 sherpa-onnx 官方 GitHub 发布页）。

用法（在 labs 文件夹里运行）：
    python models.py              # 列出全部模型、大小、哪几章用、是否已下载
    python models.py ch01         # 下载第 1 章用到的模型
    python models.py all          # 下载全部模型（约 1.6 GB）
    python models.py matcha-zh    # 只下载某一个模型

模型保存在 labs/models/ 下，每个模型一个文件夹。下载慢或下载失败，见附录 B“模型下载不了怎么办”。
"""
import sys
import tarfile
import urllib.request
from pathlib import Path

BASE = "https://github.com/k2-fsa/sherpa-onnx/releases/download"
MODELS_DIR = Path(__file__).resolve().parent / "models"

# 名称: (说明, 大约大小 MB, 用到的章, [下载地址（相对 BASE）……])
MODELS = {
    "matcha-zh": ("中文语音合成 Matcha-TTS（标贝女声）+ Vocos 声码器", 125, [1, 2, 3, 4, 5, 6, 9],
                  ["tts-models/matcha-icefall-zh-baker.tar.bz2", "vocoder-models/vocos-22khz-univ.onnx"]),
    "hifigan": ("HiFi-GAN 声码器（第 5 章和 Vocos 对比）", 4, [5], ["vocoder-models/hifigan_v2.onnx"]),
    "vits-aishell3": ("中文多说话人合成 VITS（AISHELL-3，174 种音色）", 30, [4, 6, 7, 8],
                      ["tts-models/vits-icefall-zh-aishell3.tar.bz2"]),
    "melo-zh-en": ("中英混读合成 MeloTTS", 175, [6], ["tts-models/vits-melo-tts-zh_en.tar.bz2"]),
    "kokoro": ("多语种合成 Kokoro（int8）", 140, [6], ["tts-models/kokoro-int8-multi-lang-v1_1.tar.bz2"]),
    "zipvoice": ("零样本语音克隆 ZipVoice（int8）+ Vocos 24 kHz 声码器", 160, [8, 9],
                 ["tts-models/sherpa-onnx-zipvoice-distill-int8-zh-en-emilia.tar.bz2",
                  "vocoder-models/vocos_24khz.onnx", "tts-models/lexicon-en-us.txt"]),
    "sensevoice": ("多语种语音识别 SenseVoice（int8，带标点和逆正则化）", 155, [1, 4, 5, 6, 7, 8, 9],
                   ["asr-models/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17.tar.bz2"]),
    "paraformer-zh": ("中文语音识别 Paraformer（small）", 75, [4],
                      ["asr-models/sherpa-onnx-paraformer-zh-small-2024-03-09.tar.bz2"]),
    "whisper-tiny": ("多语种语音识别 Whisper tiny", 110, [4], ["asr-models/sherpa-onnx-whisper-tiny.tar.bz2"]),
    "streaming-zh": ("中文流式识别 Zipformer（14M，边说边出字，支持热词）", 74, [4],
                     ["asr-models/sherpa-onnx-streaming-zipformer-zh-14M-2023-02-23.tar.bz2"]),
    "vad": ("语音活动检测 Silero VAD", 1, [4, 7, 9], ["asr-models/silero_vad.onnx"]),
    "kws": ("关键词唤醒 Zipformer（WenetSpeech，3.3M）", 31, [4, 9],
            ["kws-models/sherpa-onnx-kws-zipformer-wenetspeech-3.3M-2024-01-01.tar.bz2"]),
    "speaker": ("声纹模型 3D-Speaker CAM++（中文）", 27, [7, 8],
                ["speaker-recongition-models/3dspeaker_speech_campplus_sv_zh-cn_16k-common.onnx"]),
    "segmentation": ("说话人分割模型 pyannote 3.0（说话人日志用）", 7, [7],
                     ["speaker-segmentation-models/sherpa-onnx-pyannote-segmentation-3-0.tar.bz2"]),
}


def path(name):
    """返回模型文件夹，没下载就报一句看得懂的错"""
    p = MODELS_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"模型 {name} 还没下载。请在 labs 文件夹里运行：python models.py {name}")
    return p


def _fetch(url, file, retries=20):
    """下载一个文件；网络断了会接着已下载的部分继续下（最多重试 20 次）"""
    for attempt in range(1, retries + 1):
        have = file.stat().st_size if file.exists() else 0
        req = urllib.request.Request(url, headers={"Range": f"bytes={have}-"} if have else {})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                if have and r.status != 206:          # 服务器不支持续传，从头下
                    have = 0
                total = have + int(r.headers.get("Content-Length", 0))
                shown = -1
                with open(file, "ab" if have else "wb") as f:
                    while chunk := r.read(1 << 20):
                        f.write(chunk)
                        have += len(chunk)
                        pct = int(have * 10 / total) if total else 0
                        if pct != shown:
                            print(f"\r    {have / 1048576:6.1f} / {total / 1048576:.1f} MB", end="", flush=True)
                            shown = pct
            if total and have < total:                  # 连接被悄悄断开，接着下
                raise OSError("连接提前关闭")
            print()
            return
        except OSError as e:
            if getattr(e, "code", None) == 416:        # 已经下完了
                print()
                return
            print(f"\n    网络中断（{e}），第 {attempt} 次重试……")
    raise RuntimeError(f"下载失败：{url}，请检查网络或见附录 B")


def download(name):
    desc, mb, _, urls = MODELS[name]
    target = MODELS_DIR / name
    if (target / ".done").exists():
        print(f"[已有] {name}")
        return
    target.mkdir(parents=True, exist_ok=True)
    print(f"[下载] {name}：{desc}，约 {mb} MB")
    for url in urls:
        file = target / url.split("/")[-1]
        _fetch(f"{BASE}/{url}", file)
        if file.name.endswith(".tar.bz2"):
            with tarfile.open(file) as tar:
                for m in tar.getmembers():          # 去掉压缩包里的顶层文件夹，文件直接放进 models/<名称>/
                    parts = Path(m.name).parts
                    if len(parts) > 1:
                        m.name = str(Path(*parts[1:]))
                        tar.extract(m, target, filter="data")
            file.unlink()
    (target / ".done").write_text("ok")


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if not arg:
        print(f"{'名称':<15}{'大小':>7}  {'章':<14}{'状态':<6}说明")
        for name, (desc, mb, chs, _) in MODELS.items():
            ok = "已下载" if (MODELS_DIR / name / ".done").exists() else "-"
            print(f"{name:<15}{mb:>5} MB  {','.join(map(str, chs)):<14}{ok:<6}{desc}")
        return
    if arg == "all":
        names = list(MODELS)
    elif arg.startswith("ch"):
        names = [n for n, v in MODELS.items() if int(arg[2:]) in v[2]]
    else:
        names = [arg]
    for name in names:
        download(name)


if __name__ == "__main__":
    main()
