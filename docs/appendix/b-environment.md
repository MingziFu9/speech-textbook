---
title: 附录 B 实验环境、模型与数据说明
description: 安装 Python 和本书的库、下载模型、安装 ffmpeg、使用云端 Notebook、实验数据说明、编者实测环境和待实测实验清单
---

# 附录 B 实验环境、模型与数据说明

本书的实验**全部只用 CPU**，一台 4 核、8 GB 内存的普通笔记本电脑就够了；需要显卡的两个拓展实验（7-4、8-4）写明了用云端 GPU。下面按“装软件 → 下模型 → 跑起来”的顺序说明。

## B.1 编者的实测环境 { #b1 }

书中所有“运行结果”都是编者在下面的环境里实际运行得到的：

| 项目 | 版本或配置 |
|---|---|
| 处理器 | 4 核 CPU（Intel Xeon 2.1 GHz），没有显卡 |
| 系统 | Linux（学生在 Windows、macOS 上同样可以运行） |
| Python | 3.12.3 |
| sherpa-onnx | 2.0.1 |
| 其他库 | numpy 2.5.4、librosa 1.0.0、soundfile 0.14.0、matplotlib 3.11.2、gradio 6.31.0 等，见 `labs/requirements.txt` |
| 时间 | 2026 年 11 月 |

你的电脑运行结果和书上的数字可能有小差别：耗时、实时率和电脑快慢有关；合成和克隆每次都带一点随机性，相似度、字错率会在小数位上波动。**只要大致相同就说明做对了。**

## B.2 在自己电脑上安装 { #b2 }

### 第 1 步：安装 Python { #b2-1 }

1. 打开 Python 官网 <https://www.python.org/downloads/>，下载 3.12 版本（3.10—3.12 都可以；更新的版本个别库可能还没跟上）。
2. Windows 上运行安装程序时，**一定勾选最下面的“Add Python to PATH”**，再点“Install Now”。
3. 装好后打开“命令提示符”（按 Win 键，输入 `cmd`），输入 `python --version`，看到 `Python 3.12.x` 就成功了。

macOS 可以用官网的安装包；Linux 一般自带 Python，用 `python3` 代替下文的 `python`。

### 第 2 步：取得配套资源 { #b2-2 }

从老师处或本书仓库下载配套资源，解压到一个**路径里没有中文和空格**的文件夹，例如 `D:\speech\labs`。路径里的中文偶尔会让模型加载出错。

### 第 3 步：建一个虚拟环境（推荐） { #b2-3 }

虚拟环境像一个独立的“工具箱”，本课程装的库不会和别的课程打架：

```bash
cd D:\speech\labs
python -m venv venv
venv\Scripts\activate          # macOS / Linux：source venv/bin/activate
```

命令行前面出现 `(venv)` 就说明进入了虚拟环境。以后每次打开命令行窗口做实验，都要先运行 `activate` 这一行。

### 第 4 步：安装本书用到的库 { #b2-4 }

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

`-i` 后面是清华大学的镜像，国内下载快。装完运行第 1 章的环境检查程序：

```bash
cd ch01
python lab1_4_check_env.py
```

## B.3 下载模型 { #b3 }

模型文件很大，不放在配套资源里，用 `models.py` 从 sherpa-onnx 官方 GitHub 发布页下载，保存在 `labs/models/<模型名>/`。在 `labs` 文件夹里运行：

| 命令 | 作用 |
|---|---|
| `python models.py` | 列出全部模型、大小、哪几章用、是否已下载 |
| `python models.py ch04` | 下载第 4 章用到的模型（第几章就写 `ch` 几，两位数字） |
| `python models.py all` | 下载全部模型（约 1.6 GB，请留出 2 GB 磁盘空间） |
| `python models.py zipvoice` | 只下载某一个模型 |

| 模型名 | 内容 | 大约大小 | 用到的章 |
|---|---|---|---|
| `matcha-zh` | 中文合成 Matcha-TTS（标贝女声）+ Vocos 声码器 | 125 MB | 1—6、8、9 |
| `hifigan` | HiFi-GAN 声码器 | 4 MB | 5 |
| `vits-aishell3` | 中文多说话人合成 VITS（174 种音色） | 30 MB | 4、6、7、8 |
| `melo-zh-en` | 中英混读合成 MeloTTS | 175 MB | 6 |
| `kokoro` | 多语种合成 Kokoro（int8） | 140 MB | 6 |
| `zipvoice` | 零样本克隆 ZipVoice（int8）+ Vocos 24 kHz 声码器 | 160 MB | 8、9 |
| `sensevoice` | 多语种识别 SenseVoice（int8） | 155 MB | 1、4—9 |
| `paraformer-zh` | 中文识别 Paraformer（small） | 75 MB | 4 |
| `whisper-tiny` | 多语种识别 Whisper tiny | 110 MB | 4 |
| `streaming-zh` | 中文流式识别 Zipformer（支持热词） | 74 MB | 4 |
| `vad` | 语音活动检测 Silero VAD | 1 MB | 4、7、9 |
| `kws` | 关键词唤醒 Zipformer | 31 MB | 4、9 |
| `speaker` | 声纹模型 3D-Speaker CAM++ | 27 MB | 7、8 |
| `segmentation` | 说话人分割 pyannote 3.0 | 7 MB | 7 |

!!! warning "ZipVoice 模型包里的示例音频不要用"
    `labs/models/zipvoice/test_wavs/` 文件夹是模型作者自带的示例，其中有真实公众人物的录音。**本书的所有实验都不使用它们**，只用 `labs/data/voices/` 里的虚拟授权人或你自己签了授权书的录音（第 8 章）。

!!! note "两个下载时的小坑"
    - **ZipVoice 要用 int8 包**。`models.py` 下载的是 `sherpa-onnx-zipvoice-distill-int8-zh-en-emilia`。如果你从别处下载了旧版的非 int8 包，克隆出来会是乱码一样的声音。
    - **MeloTTS 用原始模型**。MeloTTS 发布页的压缩包里虽然有一个 `model.int8.onnx`，但编者下载时它只是一个 133 字节的占位文件，不能用，所以本书只用 `model.onnx`；第 9 章比较 int8 量化时改用唤醒词模型。

### 模型下载不了怎么办 { #b3-1 }

GitHub 在国内有时很慢甚至中断，按顺序试：

1. **多试几次**。`models.py` 断了会接着已经下载的部分继续，最多重试 20 次；再运行一遍同样的命令也会接着下。
2. **换个时间或网络**。夜里或用手机热点往往更快。
3. **找老师要离线包**。老师可以提前把 `labs/models/` 整个文件夹打包放到校内网盘，学生下载后解压到 `labs/models/`。
4. **从镜像下载**。魔搭社区（modelscope.cn）有 sherpa-onnx 模型的镜像，搜索压缩包的名字（见 `models.py` 里的下载地址）即可。下载后解压，**把压缩包里那一层文件夹里的文件**放进 `labs/models/<模型名>/`，再在这个文件夹里新建一个名为 `.done` 的空文件，`models.py` 就会认为已经下载好了。

放好以后可以运行 `python models.py` 检查，“状态”一栏显示“已下载”就对了。

## B.4 使用云端 Notebook { #b4 }

不想在自己电脑上装软件，可以用免费的云端 Notebook：魔搭社区、飞桨 AI Studio、阿里云 PAI-DSW 等平台都提供。平台的界面经常改版，大体步骤是：

1. 注册并登录平台，新建一个 Notebook（选 CPU 环境就够了，Python 3.10 以上）。
2. 把配套资源的压缩包上传，在 Notebook 的一个格子里解压并安装：

    ```python
    !unzip -q labs.zip
    %cd labs
    !pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    !python models.py ch01
    ```

3. 运行实验：`%cd ch01` 进入某一章的文件夹，再 `%run lab1_1_first_voice.py`。
4. 听声音：`voicelab` 的 `play(samples, sr)` 在 Notebook 里会显示一个播放条；也可以在左边的文件列表里下载 WAV 文件。
5. 用自己的录音：手机录好后用页面的“上传”按钮传上去。

注意：免费环境一般有时长限制，**关掉以后下载的模型可能会被清空**，下次要重新下载；含个人信息的录音不要上传到云端。

## B.5 安装 ffmpeg { #b5 }

第 6、8 章把 WAV 转成 MP3、写入元数据要用 ffmpeg。它是一个独立的软件，不是 Python 库，`pip` 装不了。

- **Windows**：打开 <https://ffmpeg.org/download.html>，在 Windows 一栏选一个提供编译好版本的网站，下载“release essentials”压缩包，解压到 `C:\ffmpeg`。然后把 `C:\ffmpeg\bin` 加到系统环境变量 PATH：按 Win 键搜索“编辑系统环境变量” → “环境变量” → 选中“Path” → “编辑” → “新建”，填入 `C:\ffmpeg\bin`，一路确定。
- **macOS**：装了 Homebrew 的，运行 `brew install ffmpeg`。
- **Linux**：`sudo apt install ffmpeg`。
- **用 conda 的**：`conda install -c conda-forge ffmpeg`。

装好后**重新打开**命令行窗口，输入 `ffmpeg -version`，能看到版本号就成功了。暂时装不上也不影响其他实验，只用 WAV 文件就行。

## B.6 实验数据 { #b6 }

全书的数据都在 `labs/data/` 里，详细说明见该文件夹的 `README.md`：

| 文件夹 | 内容 | 用在 |
|---|---|---|
| `fsdd/` | 英文数字 0—9 录音 400 段（公开数据集 FSDD 的子集，CC BY-SA 4.0） | 第 3 章 |
| `corpus/` | 47 句社区通知和服务用语，训练二元语言模型 | 第 3 章 |
| `sounds/` | 元音、口哨、噪声、敲门声、一段 44.1 kHz 讲话 | 第 2 章 |
| `calls/` | 8 段格式不统一的“居民来电” | 第 2、4 章 |
| `meeting/` | 约 52 秒的三人议事会录音和标准答案 | 第 4、7 章 |
| `hotwords/`、`kws/` | 热词测试录音、唤醒词测试录音 | 第 4 章 |
| `texts/` | 1469 字的《冬季告居民书》 | 第 6 章 |
| `voices/` | 4 位虚拟授权人 A—D 的录音和 B 的三种长度参考音 | 第 7、8 章 |
| `speaker_test/` | 声纹登录测试录音 32 段 | 第 7 章 |
| `faq/`、`questions/` | 社区问答表 10 条、居民提问录音 8 段 | 第 9 章 |

**书中所有“居民”“志愿者”“虚拟授权人”的声音都是用 Kokoro 内置音色合成的，不是真人录音**，人名、地名也都是虚构的。在 `labs` 文件夹里运行 `python data/make_audio.py`（先下载 `kokoro` 模型）可以重新生成这些录音。

## B.7 待实测的实验 { #b7 }

下面几个实验需要 GPU、国外网站或付费的云服务，编者的写作环境无法运行。书中给出了按官方文档编写的代码和步骤，但**没有运行结果**，标注为“待实测”。请你运行后把结果填进下表，交实验报告时一并提交。

| 实验 | 内容 | 需要 | 编者没能运行的原因 |
|---|---|---|---|
| 实验 6-4 | 阿里云百炼 CosyVoice 合成与 SSML | 阿里云账号、API Key、联网 | 写作环境不能访问该服务 |
| 实验 7-4 | kNN-VC 语音转换 | PyTorch（约 1 GB）、模型约 1.3 GB；有 GPU 更快 | 写作环境不能下载 PyTorch |
| 实验 8-4 | GPT-SoVITS 微调式克隆 | 云端 GPU（显存 8 GB 以上） | 写作环境没有 GPU |
| 实验 9-1 选做 | 用国产大模型回答居民提问 | 阿里云账号、API Key、联网 | 写作环境不能访问该服务 |

**待实测记录表**

| 实验 | 运行日期 | 平台 / 软件版本 | 是否运行成功 | 主要结果（数字或听感） | 遇到的问题和解决办法 |
|---|---|---|---|---|---|
| 6-4 | | | | | |
| 7-4 | | | | | |
| 8-4 | | | | | |
| 9-1 选做 | | | | | |

## B.8 常见安装问题 { #b8 }

| 现象 | 原因 | 解决 |
|---|---|---|
| `'python' 不是内部或外部命令` | 安装时没勾选“Add Python to PATH” | 重新运行安装程序，选“Modify”，勾选“Add Python to environment variables” |
| `pip install` 很慢或超时 | 默认从国外下载 | 命令末尾加 `-i https://pypi.tuna.tsinghua.edu.cn/simple` |
| `ModuleNotFoundError: No module named 'sherpa_onnx'` | 没装库，或者没进虚拟环境 | 先运行 `venv\Scripts\activate`，再 `pip install -r requirements.txt` |
| `ModuleNotFoundError: No module named 'voicelab'` | 没有在某一章的文件夹里运行 | 先 `cd ch04` 这样进入章文件夹，再运行实验 |
| `FileNotFoundError: 模型 xxx 还没下载` | 模型没下载 | 按提示运行 `python models.py xxx` |
| `FileNotFoundError: ../data/...` | 运行时不在章文件夹里 | 同上，先进入章文件夹 |
| 图上的中文是方框 | 电脑缺少中文字体 | Windows 一般自带“微软雅黑”“黑体”，不会出现；Linux 运行 `sudo apt install fonts-wqy-microhei` 安装文泉驿字体；macOS 自带“苹方” |
| `FileNotFoundError: [WinError 2]`（出在 `subprocess.run`） | 没装 ffmpeg | 按 B.5 节安装 |
| 合成或识别特别慢 | 电脑太旧，或同时开了很多程序 | 把 `voicelab.py` 开头的 `THREADS` 改成 4；关掉其他程序 |
