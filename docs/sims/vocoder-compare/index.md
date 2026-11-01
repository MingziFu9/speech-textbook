---
title: 从频谱到声音
description: 同一张梅尔频谱分别交给 Vocos、HiFi-GAN 和 Griffin-Lim 三种声码器，播放、看语谱图、比较速度（第 5 章）
---

# 从频谱到声音

<iframe class="sim-frame" src="main.html" height="620" loading="lazy" title="从频谱到声音"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[5.5 声码器：把频谱“演奏”成声音](../../chapters/05-tts-principles/index.md#55)

## 教学说明

**学习目标**

1. 能说出声码器的作用（记忆）；
2. 能从听感、语谱图和速度三方面比较神经网络声码器和传统算法（分析）。

**画面与操作**

- 三张卡片分别是三种声码器的结果：标题、语谱图和播放条；播放一个时其他自动暂停。
- 下方条形图是生成 8.9 秒语音的用时。

**数据来源**：梅尔频谱由 Matcha-TTS 声学模型生成，三段声音和用时均来自实验 5-3 在编者笔记本电脑 CPU 上的实测，声音转成了 64 kbps 的 MP3。

**课堂用法建议**

1. 先不告诉学生哪个是哪个，请他们按音质排序，再揭晓答案。
2. 对比 Griffin-Lim 和 Vocos 的语谱图，引导学生发现高频部分的差别。
