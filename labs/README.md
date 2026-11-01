# 实验代码

按章存放，`chNN/` 对应第 NN 章，每章有一个 `README.md` 说明各个文件。文件名 `labN_M_英文短名.py` 是第 N 章实验 N-M，`demo_*.py` 是正文里的演示。公共数据放在 `data/`，见 `data/README.md`；公共工具是 `voicelab.py`（读写音频、识别、合成、声纹、克隆、字错率），模型下载脚本是 `models.py`。

## 安装（只需一次）

推荐 Python 3.12（3.10–3.12 都可以）。在 `labs` 文件夹里打开终端：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python models.py ch01        # 下载第 1 章要用的模型；第几章就写 ch 几，全部下载写 all（约 1.6 GB）
```

不会安装的同学先看附录 B。

## 运行

**先进入这一章的文件夹再运行**，例如：

```bash
cd labs/ch04
python lab4_1_compare_models.py
```

程序会读取 `../data/` 里的音频，结果（WAV、字幕、图片、表格）保存在当前文件夹。每个脚本也可以整段复制到 Notebook 的单元格里运行，在 Notebook 里还能直接点播放听结果。

## 说明

- 标 ★ 的实验给出完整代码：先读懂、运行，再按“改一改”改参数观察变化。标 ☆ 的是选做。
- 合成和识别的耗时与电脑有关，编者的数字是在 4 核 CPU、2 个线程上测的。
- 需要联网、显卡或额外安装的实验（6-4 云平台接口、7-4 语音转换、8-4 微调式克隆、9-1 的大模型选项），文件开头的注释写明了运行条件。
