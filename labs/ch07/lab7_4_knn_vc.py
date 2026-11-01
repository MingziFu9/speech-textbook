"""实验 7-4 语音转换体验（待实测）：用 kNN-VC 把志愿者 A 说的一句话，换成志愿者 C 的音色，再用声纹检查“像谁”。

编者说明：kNN-VC 基于 PyTorch，首次运行要从 GitHub 下载约 1.3 GB 的模型（WavLM-Large 和声码器）。编者的写作环境
无法下载 PyTorch 安装包，本实验代码按 kNN-VC 官方说明编写，**待实测**。CPU 上转换一句话约需几十秒到几分钟。
安装：pip install torch torchaudio （按 https://pytorch.org 选择 CPU 版本）
参考音只用书里的虚拟授权人（A—D），不要用任何真实人物的声音。
"""
import sys

import torch
import torchaudio

sys.path.append("..")
from voicelab import embed, read_audio, save_audio

# 1. 加载 kNN-VC（第一次会自动下载模型，放在用户目录的 .cache/torch/hub 里）
knn_vc = torch.hub.load("bshall/knn-vc", "knn_vc", prematched=True, trust_repo=True, pretrained=True, device="cpu")   # 没有显卡时一定要写 device="cpu"

# 2. 源语音（说什么）：A 的一句话；目标音色（谁在说）：C 的全部录音
#    kNN-VC 要求 16 kHz，书里的志愿者录音是 24 kHz，先转一份 16 kHz 的
def to16k(name):
    audio, sr = read_audio(f"../data/voices/{name}.wav", 16000)
    save_audio(f"{name}_16k.wav", audio, sr)
    return f"{name}_16k.wav"


source = to16k("volunteer_A_1")
targets = [to16k(f"volunteer_C_{k}") for k in (1, 2, 3)]       # ← 改这里：换成 B 或 D；目标录音越长效果越好

query = knn_vc.get_features(source)               # 把源语音变成一帧一帧的“内容特征”
matching_set = knn_vc.get_matching_set(targets)   # 把目标人的录音也变成特征，组成“素材库”
out = knn_vc.match(query, matching_set, topk=4)   # 每一帧换成素材库里最像的 4 帧的平均，再变回声音
torchaudio.save("A_to_C.wav", out[None], 16000)

# 3. 用声纹检查：转换后的声音更像 A 还是更像 C？
converted, sr = read_audio("A_to_C.wav")
for code in "AC":
    print(f"转换结果和 {code} 的声纹相似度：{embed(converted, sr) @ embed(f'../data/voices/volunteer_{code}_2.wav'):.2f}")
