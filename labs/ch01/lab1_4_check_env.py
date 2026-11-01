"""实验 1-4 检查实验环境：看看需要的库装好没有、模型下载了哪些。"""
import importlib
import platform
import sys

sys.path.append("..")
print("Python", platform.python_version(), "|", platform.system())
for name in ["sherpa_onnx", "numpy", "soundfile", "librosa", "matplotlib", "pandas", "jieba", "pypinyin"]:
    try:
        m = importlib.import_module(name)
        print(f"  [好] {name:<12} {getattr(m, '__version__', '')}")
    except ImportError:
        print(f"  [缺] {name:<12} 请运行 pip install -r requirements.txt")

from models import MODELS, MODELS_DIR       # noqa: E402
ready = [n for n in MODELS if (MODELS_DIR / n / ".done").exists()]
print(f"已下载模型 {len(ready)} / {len(MODELS)} 个：{'、'.join(ready) or '还没有'}")
