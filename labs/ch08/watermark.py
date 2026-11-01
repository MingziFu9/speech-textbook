"""一个教学用的简单音频水印（第 8 章实验 8-3）：用“密钥”生成一段人耳几乎听不到的伪随机噪声，叠加到声音里；
检测时用同一个密钥生成同样的噪声，和声音做相关，相关得分明显高于随机水平就说明有水印。
注意：这只是演示原理，强度很弱、容易被去掉，正式产品要按 GB 45438—2025 等标准使用专业方案。
"""
import numpy as np
from scipy.signal import butter, sosfilt

BLOCK = 4096                                            # 水印图案的长度（采样点）


def _pattern(key, sr):
    """用密钥生成一段固定的伪随机噪声，并只保留 1—4 kHz（压缩成 MP3 后也不容易丢）"""
    rng = np.random.default_rng(key)
    p = rng.standard_normal(BLOCK)
    p = sosfilt(butter(4, [1000, 4000], btype="band", fs=sr, output="sos"), p)
    return p / np.sqrt(np.mean(p ** 2))


def embed_watermark(audio, sr, key, strength=0.02):
    """把水印图案一遍遍铺满整段声音。strength 是水印相对于声音音量的比例"""
    p = _pattern(key, sr)
    tiled = np.resize(p, len(audio))
    rms = np.sqrt(np.mean(audio ** 2))
    return (audio + strength * rms * tiled).astype(np.float32)


def detect_watermark(audio, sr, key):
    """返回检测得分：把声音切成和图案一样长的块，叠加平均后和图案做相关。没有水印时得分一般在 -3 到 3 之间，有水印时大于 5（声音越长越明显）"""
    p = _pattern(key, sr)
    n = len(audio) // BLOCK
    if n == 0:
        return 0.0
    avg = audio[:n * BLOCK].reshape(n, BLOCK).mean(axis=0)        # 叠加平均：声音互相抵消，水印越叠越强
    avg = sosfilt(butter(4, [1000, 4000], btype="band", fs=sr, output="sos"), avg)
    corr = np.dot(avg, p) / (np.linalg.norm(avg) * np.linalg.norm(p) + 1e-12)
    return float(corr * np.sqrt(BLOCK))                           # 换算成“比随机水平高几倍”
