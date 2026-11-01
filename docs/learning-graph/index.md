---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **110 个概念、142 条先修关系**，概念按章排列，颜色表示 6 个类别（声音与音频、语音识别、语音合成、声纹与克隆、系统与应用、伦理与合规）。概念的定义都来自[附录 C 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 语音技术概览（9 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [语音识别](../appendix/glossary.md#g-语音识别) | 语音识别 | — |
    | [语音合成](../appendix/glossary.md#g-语音合成) | 语音合成 | — |
    | [语音克隆](../appendix/glossary.md#g-语音克隆) | 声纹与克隆 | [语音合成](../appendix/glossary.md#g-语音合成) |
    | [声纹识别](../appendix/glossary.md#g-声纹识别) | 声纹与克隆 | — |
    | [语音唤醒](../appendix/glossary.md#g-语音唤醒) | 语音识别 | — |
    | [语音交互](../appendix/glossary.md#g-语音交互) | 系统与应用 | [语音识别](../appendix/glossary.md#g-语音识别)、[语音合成](../appendix/glossary.md#g-语音合成)、[语音唤醒](../appendix/glossary.md#g-语音唤醒) |
    | [语音大模型](../appendix/glossary.md#g-语音大模型) | 系统与应用 | [语音交互](../appendix/glossary.md#g-语音交互) |
    | [离线模型](../appendix/glossary.md#g-离线模型) | 系统与应用 | — |
    | [sherpa-onnx](../appendix/glossary.md#g-sherpa-onnx) | 系统与应用 | [离线模型](../appendix/glossary.md#g-离线模型) |

??? note "第 2 章 声音与音频处理（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [声波](../appendix/glossary.md#g-声波) | 声音与音频 | — |
    | [频率](../appendix/glossary.md#g-频率) | 声音与音频 | [声波](../appendix/glossary.md#g-声波) |
    | [振幅](../appendix/glossary.md#g-振幅) | 声音与音频 | [声波](../appendix/glossary.md#g-声波) |
    | [基频](../appendix/glossary.md#g-基频) | 声音与音频 | [频率](../appendix/glossary.md#g-频率) |
    | [音色](../appendix/glossary.md#g-音色) | 声音与音频 | [共振峰](../appendix/glossary.md#g-共振峰)、[基频](../appendix/glossary.md#g-基频) |
    | [共振峰](../appendix/glossary.md#g-共振峰) | 声音与音频 | [频率](../appendix/glossary.md#g-频率) |
    | [采样](../appendix/glossary.md#g-采样) | 声音与音频 | [声波](../appendix/glossary.md#g-声波) |
    | [采样率](../appendix/glossary.md#g-采样率) | 声音与音频 | [采样](../appendix/glossary.md#g-采样) |
    | [采样定理](../appendix/glossary.md#g-采样定理) | 声音与音频 | [采样率](../appendix/glossary.md#g-采样率) |
    | [混叠](../appendix/glossary.md#g-混叠) | 声音与音频 | [采样定理](../appendix/glossary.md#g-采样定理) |
    | [量化](../appendix/glossary.md#g-量化) | 声音与音频 | [采样](../appendix/glossary.md#g-采样) |
    | [位深](../appendix/glossary.md#g-位深) | 声音与音频 | [量化](../appendix/glossary.md#g-量化) |
    | [声道](../appendix/glossary.md#g-声道) | 声音与音频 | [采样](../appendix/glossary.md#g-采样) |
    | [波形图](../appendix/glossary.md#g-波形图) | 声音与音频 | [振幅](../appendix/glossary.md#g-振幅) |
    | [频谱](../appendix/glossary.md#g-频谱) | 声音与音频 | [频率](../appendix/glossary.md#g-频率) |
    | [语谱图](../appendix/glossary.md#g-语谱图) | 声音与音频 | [帧](../appendix/glossary.md#g-帧)、[频谱](../appendix/glossary.md#g-频谱) |
    | [梅尔频谱](../appendix/glossary.md#g-梅尔频谱) | 声音与音频 | [语谱图](../appendix/glossary.md#g-语谱图) |
    | [MFCC](../appendix/glossary.md#g-MFCC) | 声音与音频 | [梅尔频谱](../appendix/glossary.md#g-梅尔频谱) |
    | [帧](../appendix/glossary.md#g-帧) | 声音与音频 | [采样率](../appendix/glossary.md#g-采样率) |
    | [重采样](../appendix/glossary.md#g-重采样) | 声音与音频 | [采样率](../appendix/glossary.md#g-采样率) |
    | [音量归一化](../appendix/glossary.md#g-音量归一化) | 声音与音频 | [振幅](../appendix/glossary.md#g-振幅) |
    | [削波](../appendix/glossary.md#g-削波) | 声音与音频 | [位深](../appendix/glossary.md#g-位深)、[振幅](../appendix/glossary.md#g-振幅) |
    | [信噪比](../appendix/glossary.md#g-信噪比) | 声音与音频 | [振幅](../appendix/glossary.md#g-振幅) |
    | [降噪](../appendix/glossary.md#g-降噪) | 声音与音频 | [信噪比](../appendix/glossary.md#g-信噪比) |

??? note "第 3 章 识别原理（19 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [声学模型](../appendix/glossary.md#g-声学模型) | 语音识别 | [语音识别](../appendix/glossary.md#g-语音识别) |
    | [语言模型](../appendix/glossary.md#g-语言模型) | 语音识别 | [语音识别](../appendix/glossary.md#g-语音识别) |
    | [解码器](../appendix/glossary.md#g-解码器) | 语音识别 | [声学模型](../appendix/glossary.md#g-声学模型)、[语言模型](../appendix/glossary.md#g-语言模型) |
    | [词图](../appendix/glossary.md#g-词图) | 语音识别 | [解码器](../appendix/glossary.md#g-解码器) |
    | [模板匹配](../appendix/glossary.md#g-模板匹配) | 语音识别 | [MFCC](../appendix/glossary.md#g-MFCC) |
    | [动态时间规整](../appendix/glossary.md#g-动态时间规整) | 语音识别 | [模板匹配](../appendix/glossary.md#g-模板匹配)、[帧](../appendix/glossary.md#g-帧) |
    | [隐马尔可夫模型](../appendix/glossary.md#g-隐马尔可夫模型) | 语音识别 | [帧](../appendix/glossary.md#g-帧)、[音素](../appendix/glossary.md#g-音素) |
    | [高斯混合模型](../appendix/glossary.md#g-高斯混合模型) | 语音识别 | [隐马尔可夫模型](../appendix/glossary.md#g-隐马尔可夫模型) |
    | [音素](../appendix/glossary.md#g-音素) | 语音识别 | — |
    | [声韵母](../appendix/glossary.md#g-声韵母) | 语音识别 | [音素](../appendix/glossary.md#g-音素) |
    | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) | 语音识别 | [模板匹配](../appendix/glossary.md#g-模板匹配) |
    | [端到端模型](../appendix/glossary.md#g-端到端模型) | 语音识别 | [声学模型](../appendix/glossary.md#g-声学模型) |
    | [CTC](../appendix/glossary.md#g-CTC) | 语音识别 | [端到端模型](../appendix/glossary.md#g-端到端模型) |
    | [编码器—解码器](../appendix/glossary.md#g-编码器—解码器) | 语音识别 | [端到端模型](../appendix/glossary.md#g-端到端模型) |
    | [非自回归模型](../appendix/glossary.md#g-非自回归模型) | 语音识别 | [端到端模型](../appendix/glossary.md#g-端到端模型) |
    | [N 元语言模型](../appendix/glossary.md#g-N-元语言模型) | 语音识别 | [语言模型](../appendix/glossary.md#g-语言模型) |
    | [字错率](../appendix/glossary.md#g-字错率) | 语音识别 | [语音识别](../appendix/glossary.md#g-语音识别) |
    | [词错率](../appendix/glossary.md#g-词错率) | 语音识别 | [字错率](../appendix/glossary.md#g-字错率) |
    | [实时率](../appendix/glossary.md#g-实时率) | 语音识别 | [语音识别](../appendix/glossary.md#g-语音识别) |

??? note "第 4 章 识别实战（13 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [识别器](../appendix/glossary.md#g-识别器) | 语音识别 | [sherpa-onnx](../appendix/glossary.md#g-sherpa-onnx) |
    | [数据流](../appendix/glossary.md#g-数据流) | 语音识别 | [识别器](../appendix/glossary.md#g-识别器) |
    | [语音活动检测](../appendix/glossary.md#g-语音活动检测) | 语音识别 | [帧](../appendix/glossary.md#g-帧)、[振幅](../appendix/glossary.md#g-振幅) |
    | [时间戳](../appendix/glossary.md#g-时间戳) | 语音识别 | [语音活动检测](../appendix/glossary.md#g-语音活动检测) |
    | [SRT 字幕](../appendix/glossary.md#g-SRT-字幕) | 语音识别 | [时间戳](../appendix/glossary.md#g-时间戳) |
    | [文本逆正则化](../appendix/glossary.md#g-文本逆正则化) | 语音识别 | [识别器](../appendix/glossary.md#g-识别器) |
    | [标点恢复](../appendix/glossary.md#g-标点恢复) | 语音识别 | [识别器](../appendix/glossary.md#g-识别器) |
    | [非流式识别](../appendix/glossary.md#g-非流式识别) | 语音识别 | [数据流](../appendix/glossary.md#g-数据流) |
    | [流式识别](../appendix/glossary.md#g-流式识别) | 语音识别 | [数据流](../appendix/glossary.md#g-数据流)、[实时率](../appendix/glossary.md#g-实时率) |
    | [唤醒词](../appendix/glossary.md#g-唤醒词) | 语音识别 | [语音唤醒](../appendix/glossary.md#g-语音唤醒)、[流式识别](../appendix/glossary.md#g-流式识别) |
    | [误唤醒](../appendix/glossary.md#g-误唤醒) | 语音识别 | [唤醒词](../appendix/glossary.md#g-唤醒词)、[混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [漏唤醒](../appendix/glossary.md#g-漏唤醒) | 语音识别 | [唤醒词](../appendix/glossary.md#g-唤醒词) |
    | [热词](../appendix/glossary.md#g-热词) | 语音识别 | [流式识别](../appendix/glossary.md#g-流式识别)、[解码器](../appendix/glossary.md#g-解码器) |

??? note "第 5 章 合成原理（12 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [文本前端](../appendix/glossary.md#g-文本前端) | 语音合成 | [语音合成](../appendix/glossary.md#g-语音合成) |
    | [文本正则化](../appendix/glossary.md#g-文本正则化) | 语音合成 | [文本前端](../appendix/glossary.md#g-文本前端)、[文本逆正则化](../appendix/glossary.md#g-文本逆正则化) |
    | [分词](../appendix/glossary.md#g-分词) | 语音合成 | [文本前端](../appendix/glossary.md#g-文本前端) |
    | [多音字](../appendix/glossary.md#g-多音字) | 语音合成 | [分词](../appendix/glossary.md#g-分词)、[声韵母](../appendix/glossary.md#g-声韵母) |
    | [变调](../appendix/glossary.md#g-变调) | 语音合成 | [声韵母](../appendix/glossary.md#g-声韵母) |
    | [韵律](../appendix/glossary.md#g-韵律) | 语音合成 | [基频](../appendix/glossary.md#g-基频)、[文本前端](../appendix/glossary.md#g-文本前端) |
    | [声码器](../appendix/glossary.md#g-声码器) | 语音合成 | [梅尔频谱](../appendix/glossary.md#g-梅尔频谱) |
    | [拼接合成](../appendix/glossary.md#g-拼接合成) | 语音合成 | [语音合成](../appendix/glossary.md#g-语音合成) |
    | [统计参数合成](../appendix/glossary.md#g-统计参数合成) | 语音合成 | [拼接合成](../appendix/glossary.md#g-拼接合成)、[隐马尔可夫模型](../appendix/glossary.md#g-隐马尔可夫模型) |
    | [神经网络语音合成](../appendix/glossary.md#g-神经网络语音合成) | 语音合成 | [统计参数合成](../appendix/glossary.md#g-统计参数合成)、[声码器](../appendix/glossary.md#g-声码器) |
    | [平均意见分](../appendix/glossary.md#g-平均意见分) | 语音合成 | [语音合成](../appendix/glossary.md#g-语音合成) |
    | [回识别字错率](../appendix/glossary.md#g-回识别字错率) | 语音合成 | [字错率](../appendix/glossary.md#g-字错率)、[语音合成](../appendix/glossary.md#g-语音合成) |

??? note "第 6 章 合成实战（8 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [多说话人合成](../appendix/glossary.md#g-多说话人合成) | 语音合成 | [神经网络语音合成](../appendix/glossary.md#g-神经网络语音合成)、[音色](../appendix/glossary.md#g-音色) |
    | [说话人编号](../appendix/glossary.md#g-说话人编号) | 语音合成 | [多说话人合成](../appendix/glossary.md#g-多说话人合成) |
    | [语速](../appendix/glossary.md#g-语速) | 语音合成 | [韵律](../appendix/glossary.md#g-韵律) |
    | [中英混读](../appendix/glossary.md#g-中英混读) | 语音合成 | [文本正则化](../appendix/glossary.md#g-文本正则化)、[文本前端](../appendix/glossary.md#g-文本前端) |
    | [有声书](../appendix/glossary.md#g-有声书) | 语音合成 | [语速](../appendix/glossary.md#g-语速)、[文本正则化](../appendix/glossary.md#g-文本正则化)、[实时率](../appendix/glossary.md#g-实时率) |
    | [SSML](../appendix/glossary.md#g-SSML) | 语音合成 | [韵律](../appendix/glossary.md#g-韵律)、[多音字](../appendix/glossary.md#g-多音字) |
    | [显式标识](../appendix/glossary.md#g-显式标识) | 伦理与合规 | [语音合成](../appendix/glossary.md#g-语音合成) |
    | [隐式标识](../appendix/glossary.md#g-隐式标识) | 伦理与合规 | [显式标识](../appendix/glossary.md#g-显式标识) |

??? note "第 7 章 声纹与变声（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [声纹](../appendix/glossary.md#g-声纹) | 声纹与克隆 | [声纹识别](../appendix/glossary.md#g-声纹识别)、[音色](../appendix/glossary.md#g-音色) |
    | [声纹向量](../appendix/glossary.md#g-声纹向量) | 声纹与克隆 | [声纹](../appendix/glossary.md#g-声纹) |
    | [余弦相似度](../appendix/glossary.md#g-余弦相似度) | 声纹与克隆 | [声纹向量](../appendix/glossary.md#g-声纹向量) |
    | [说话人确认](../appendix/glossary.md#g-说话人确认) | 声纹与克隆 | [余弦相似度](../appendix/glossary.md#g-余弦相似度) |
    | [说话人辨认](../appendix/glossary.md#g-说话人辨认) | 声纹与克隆 | [余弦相似度](../appendix/glossary.md#g-余弦相似度) |
    | [说话人日志](../appendix/glossary.md#g-说话人日志) | 声纹与克隆 | [说话人辨认](../appendix/glossary.md#g-说话人辨认)、[语音活动检测](../appendix/glossary.md#g-语音活动检测) |
    | [误接受率](../appendix/glossary.md#g-误接受率) | 声纹与克隆 | [说话人确认](../appendix/glossary.md#g-说话人确认) |
    | [误拒绝率](../appendix/glossary.md#g-误拒绝率) | 声纹与克隆 | [说话人确认](../appendix/glossary.md#g-说话人确认) |
    | [等错误率](../appendix/glossary.md#g-等错误率) | 声纹与克隆 | [误接受率](../appendix/glossary.md#g-误接受率)、[误拒绝率](../appendix/glossary.md#g-误拒绝率) |
    | [语音转换](../appendix/glossary.md#g-语音转换) | 声纹与克隆 | [声纹向量](../appendix/glossary.md#g-声纹向量)、[音色](../appendix/glossary.md#g-音色) |

??? note "第 8 章 语音克隆（8 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [零样本克隆](../appendix/glossary.md#g-零样本克隆) | 声纹与克隆 | [参考音](../appendix/glossary.md#g-参考音)、[多说话人合成](../appendix/glossary.md#g-多说话人合成)、[声纹向量](../appendix/glossary.md#g-声纹向量) |
    | [微调式克隆](../appendix/glossary.md#g-微调式克隆) | 声纹与克隆 | [语音克隆](../appendix/glossary.md#g-语音克隆)、[神经网络语音合成](../appendix/glossary.md#g-神经网络语音合成) |
    | [参考音](../appendix/glossary.md#g-参考音) | 声纹与克隆 | [语音克隆](../appendix/glossary.md#g-语音克隆)、[信噪比](../appendix/glossary.md#g-信噪比) |
    | [声音权益](../appendix/glossary.md#g-声音权益) | 伦理与合规 | [语音克隆](../appendix/glossary.md#g-语音克隆) |
    | [深度合成](../appendix/glossary.md#g-深度合成) | 伦理与合规 | [语音克隆](../appendix/glossary.md#g-语音克隆)、[显式标识](../appendix/glossary.md#g-显式标识) |
    | [单独同意](../appendix/glossary.md#g-单独同意) | 伦理与合规 | [声纹](../appendix/glossary.md#g-声纹) |
    | [声音授权书](../appendix/glossary.md#g-声音授权书) | 伦理与合规 | [声音权益](../appendix/glossary.md#g-声音权益)、[单独同意](../appendix/glossary.md#g-单独同意) |
    | [音频水印](../appendix/glossary.md#g-音频水印) | 伦理与合规 | [隐式标识](../appendix/glossary.md#g-隐式标识) |

??? note "第 9 章 应用与项目（7 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [端到端延迟](../appendix/glossary.md#g-端到端延迟) | 系统与应用 | [语音交互](../appendix/glossary.md#g-语音交互)、[实时率](../appendix/glossary.md#g-实时率) |
    | [首包延迟](../appendix/glossary.md#g-首包延迟) | 系统与应用 | [端到端延迟](../appendix/glossary.md#g-端到端延迟) |
    | [意图理解](../appendix/glossary.md#g-意图理解) | 系统与应用 | [语音交互](../appendix/glossary.md#g-语音交互)、[语音识别](../appendix/glossary.md#g-语音识别) |
    | [兜底回复](../appendix/glossary.md#g-兜底回复) | 系统与应用 | [意图理解](../appendix/glossary.md#g-意图理解) |
    | [打断](../appendix/glossary.md#g-打断) | 系统与应用 | [语音大模型](../appendix/glossary.md#g-语音大模型)、[语音活动检测](../appendix/glossary.md#g-语音活动检测) |
    | [模型量化](../appendix/glossary.md#g-模型量化) | 系统与应用 | [离线模型](../appendix/glossary.md#g-离线模型)、[位深](../appendix/glossary.md#g-位深) |
    | [端侧部署](../appendix/glossary.md#g-端侧部署) | 系统与应用 | [模型量化](../appendix/glossary.md#g-模型量化)、[语音唤醒](../appendix/glossary.md#g-语音唤醒) |

<!-- graph:end -->
