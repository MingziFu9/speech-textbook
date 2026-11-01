---
title: 附录 C 术语表
description: 本书主要术语的中英文名称、简明定义和例子，按章节顺序排列
---

# 附录 C 术语表

本表按章节顺序列出本书的主要术语，每个术语给出英文名称、简明定义和例子。正文中带虚线下划线的术语，把鼠标停在上面就能看到定义，点击可以跳到本表。

通用术语（如“过拟合”“精确率”）的译名和定义以本系列教材共用的《系列公共术语表》为准，各书保持一致。

## 第 1 章 走进语音技术

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-语音识别"></span>语音识别 | Automatic Speech Recognition, ASR | 让计算机把人说的话转换成文字的技术，也叫语音转文字（STT） | 微信语音转文字、会议实时字幕 |
| <span id="g-语音合成"></span>语音合成 | Text to Speech, TTS | 让计算机把文字转换成自然语音的技术，也叫文语转换 | 导航播报路况、有声书 |
| <span id="g-语音克隆"></span>语音克隆 | Voice Cloning | 用某个人的少量录音，让机器用这个人的音色说出任意内容的技术 | 用 10 秒参考录音，让合成语音带上志愿者的嗓音 |
| <span id="g-声纹识别"></span>声纹识别 | Speaker Recognition | 根据声音判断说话人是谁或是不是某个人的技术，也叫说话人识别 | 银行电话客服用声纹核验身份 |
| <span id="g-语音唤醒"></span>语音唤醒 | Wake-up Word Detection | 设备持续监听，只在听到特定唤醒词时才开始工作的技术，也叫关键词检测 | 说“小爱同学”唤醒智能音箱 |
| <span id="g-语音交互"></span>语音交互 | Voice Interaction | 人和机器之间用说话和听声音来交流的方式，通常由唤醒、识别、理解、回答、合成几个环节组成 | 车载语音助手导航 |
| <span id="g-语音大模型"></span>语音大模型 | Speech Large Model | 能直接听懂语音并直接用语音回答的大模型，不必先转成文字 | 能实时对话、可以随时打断的语音助手 |
| <span id="g-离线模型"></span>离线模型 | Offline Model | 下载到本机运行、不需要联网调用云端服务的模型 | 本书用 sherpa-onnx 在笔记本电脑上运行的识别和合成模型 |
| <span id="g-sherpa-onnx"></span>sherpa-onnx | sherpa-onnx | 新一代 Kaldi 团队开源的语音工具包，能在电脑和手机上离线运行识别、合成、唤醒、声纹等模型 | 本书全部实验的主力工具 |

## 第 2 章 声音的数字化与音频处理

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-声波"></span>声波 | Sound Wave | 物体振动带动空气一疏一密地传播开去形成的波，传到耳朵就是声音 | 说话时声带振动产生声波 |
| <span id="g-频率"></span>频率 | Frequency | 每秒振动的次数，单位赫兹（Hz），频率越高听起来音越高 | 女声基频约 200 Hz，口哨约 2000 Hz |
| <span id="g-振幅"></span>振幅 | Amplitude | 振动偏离平衡位置的大小，振幅越大声音越响 | 波形图上纵向的高低 |
| <span id="g-基频"></span>基频 | Fundamental Frequency, F0 | 浊音中声带振动的频率，决定听到的音高 | 实验 2-1 中元音的基频约 214 Hz |
| <span id="g-音色"></span>音色 | Timbre | 让音高、响度相同的两个声音听起来仍然不同的特性，主要由谐波和共振峰决定 | 钢琴和小提琴弹同一个音，一听就能分出来 |
| <span id="g-共振峰"></span>共振峰 | Formant | 口腔、鼻腔像共鸣箱一样放大的几个频率区域，决定发的是哪个元音 | “啊”的前两个共振峰约 800、1200 Hz |
| <span id="g-采样"></span>采样 | Sampling | 每隔相同的时间记下一次声波的高度，把连续的声音变成一串数字 | 16 kHz 采样即每秒记 16000 次 |
| <span id="g-采样率"></span>采样率 | Sample Rate | 每秒采样的次数，单位 Hz | 语音识别常用 16000 Hz，CD 用 44100 Hz |
| <span id="g-采样定理"></span>采样定理 | Sampling Theorem | 采样率至少是声音最高频率的 2 倍，才能把声音完整记录下来 | 8 kHz 采样最多记录到 4000 Hz |
| <span id="g-混叠"></span>混叠 | Aliasing | 声音频率超过采样率一半时，被错误地记成一个更低的频率 | 用 8 kHz 采样 6000 Hz 的声音，会变成 2000 Hz |
| <span id="g-量化"></span>量化 | Quantization | 把每个采样点的高度四舍五入到有限个台阶上，变成整数保存 | 16 位量化有 65536 个台阶 |
| <span id="g-位深"></span>位深 | Bit Depth | 每个采样点用多少位二进制数保存，位数越多越精细 | WAV 常用 16 位 |
| <span id="g-声道"></span>声道 | Channel | 同时录下的独立声音路数，单声道 1 路，立体声 2 路 | 语音识别通常只要单声道 |
| <span id="g-波形图"></span>波形图 | Waveform | 横轴是时间、纵轴是振幅的图，直接画出采样点 | 看哪里有声音、哪里静音、有没有削波 |
| <span id="g-频谱"></span>频谱 | Spectrum | 一小段声音里各个频率成分各有多强的图，横轴是频率 | 口哨的频谱只有一个高峰 |
| <span id="g-语谱图"></span>语谱图 | Spectrogram | 横轴时间、纵轴频率、颜色深浅表示能量强弱的图，把一段段频谱排起来得到 | 在语谱图上能看到元音的共振峰横条 |
| <span id="g-梅尔频谱"></span>梅尔频谱 | Mel Spectrogram | 按人耳对高低频敏感程度不同（梅尔刻度）重新划分频带的语谱图，语音模型最常用的输入 | 80 个梅尔频带、每 10 毫秒一帧 |
| <span id="g-MFCC"></span>MFCC | Mel-Frequency Cepstral Coefficients | 在梅尔频谱基础上再压缩得到的十几个数，概括一帧声音的音色，传统语音识别的标准特征 | 每帧 13 个 MFCC 系数 |
| <span id="g-帧"></span>帧 | Frame | 把声音切成的一小段（通常 20—30 毫秒），在一帧里认为声音基本不变 | 25 毫秒一帧、每 10 毫秒移动一次 |
| <span id="g-重采样"></span>重采样 | Resampling | 把音频从一种采样率转换成另一种采样率 | 把 44.1 kHz 的录音转成 16 kHz 再识别 |
| <span id="g-音量归一化"></span>音量归一化 | Loudness Normalization | 把音频整体放大或缩小到统一的音量水平 | 把最响处调到 0.9 |
| <span id="g-削波"></span>削波 | Clipping | 声音太大超过能记录的最大值，波峰被“削平”，听起来破音 | 离话筒太近大喊造成的破音 |
| <span id="g-信噪比"></span>信噪比 | Signal-to-Noise Ratio, SNR | 有用声音和噪声的能量之比，常用分贝表示，越大越干净 | 0 dB 表示人声和噪声一样强 |
| <span id="g-降噪"></span>降噪 | Noise Reduction | 估计并减去录音中的背景噪声，让人声更清楚 | 用 noisereduce 去掉稳定的嘶嘶声 |

## 第 3 章 语音识别原理：从模板匹配到深度学习

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-声学模型"></span>声学模型 | Acoustic Model | 识别系统中判断“这一小段声音像哪个音”的部分 | 给每一帧打分：像“sh”的可能性 0.8，像“s”的 0.15 |
| <span id="g-语言模型"></span>语言模型 | Language Model | 判断一串文字通不通顺、出现的可能性有多大的模型 | 同音的“期中考试”和“其中考试”，靠语言模型选出前者 |
| <span id="g-解码器"></span>解码器 | Decoder | 结合声学模型和语言模型的打分，在所有可能的文字中搜索最好的一句的部分 | 从几千条候选路径里找出总分最高的一句 |
| <span id="g-词图"></span>词图 | Word Lattice | 解码时把各种可能的词连成的网状图，每条从头到尾的路径是一种候选句子 | “充电桩/充电装/冲点桩”是词图里的几条分支 |
| <span id="g-模板匹配"></span>模板匹配 | Template Matching | 事先存好每个词的录音特征当模板，识别时和每个模板比较，最像的就是结果 | 早期的数字识别器 |
| <span id="g-动态时间规整"></span>动态时间规整 | Dynamic Time Warping, DTW | 允许一帧对多帧，自动对齐两段快慢不同的语音并算出距离的方法 | 实验 3-1 用 DTW 比较数字录音的 MFCC |
| <span id="g-隐马尔可夫模型"></span>隐马尔可夫模型 | Hidden Markov Model, HMM | 用看不见的“状态”一步步转移、每个状态发出可观察的声音来描述语音的统计模型 | 实验 3-2 给每个数字训练一个 5 状态 HMM |
| <span id="g-高斯混合模型"></span>高斯混合模型 | Gaussian Mixture Model, GMM | 用几个“钟形曲线”叠加来描述一个状态会发出什么样的声音特征 | 传统识别中 HMM 每个状态配一个 GMM |
| <span id="g-音素"></span>音素 | Phoneme | 语言中能区分意思的最小语音单位 | “bā”和“pā”的区别在音素 b 和 p |
| <span id="g-声韵母"></span>声韵母 | Initial and Final | 汉语音节的声母和韵母，中文识别常用的建模单位 | “中”= 声母 zh + 韵母 ong |
| <span id="g-混淆矩阵"></span>混淆矩阵 | Confusion Matrix | 行是真实类别、列是识别结果的表格，对角线是认对的，其他格子显示谁被认成了谁 | 实验 3-2 中 2 有 1 次被认成 0 |
| <span id="g-端到端模型"></span>端到端模型 | End-to-End Model | 一个神经网络直接把声音变成文字，不再分成声学模型、发音词典、语言模型几个部件 | Whisper、Paraformer、SenseVoice |
| <span id="g-CTC"></span>CTC | Connectionist Temporal Classification | 让模型逐帧输出字或空白，再合并重复、删掉空白得到文字的训练和解码方法 | “__你你_好好_”折叠成“你好” |
| <span id="g-编码器—解码器"></span>编码器—解码器 | Encoder-Decoder | 先由编码器把整段声音“读懂”，再由解码器一个字一个字地写出文字的模型结构 | Whisper |
| <span id="g-非自回归模型"></span>非自回归模型 | Non-autoregressive Model | 一次同时输出所有字，而不是一个接一个地输出，因此速度快 | Paraformer |
| <span id="g-N-元语言模型"></span>N 元语言模型 | N-gram Language Model | 只看前面 N−1 个字（或词）来估计下一个字概率的语言模型 | 实验 3-4 的二元（2 元）语言模型 |
| <span id="g-字错率"></span>字错率 | Character Error Rate, CER | (替换 + 删除 + 插入) ÷ 参考文本字数，中文识别的主要评价指标 | 7 个字错 2 个，字错率约 29% |
| <span id="g-词错率"></span>词错率 | Word Error Rate, WER | 按词计算的错误率，英文等用空格分词的语言常用 | 5 个词错 2 个，词错率 40% |
| <span id="g-实时率"></span>实时率 | Real-Time Factor, RTF | 处理用时 ÷ 音频时长，小于 1 表示比说话还快 | 61.8 秒录音用 3.3 秒识别完，RTF 约 0.05 |

## 第 4 章 语音识别实战：转写、字幕与唤醒

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-识别器"></span>识别器 | Recognizer | sherpa-onnx 中加载了识别模型、负责识别的对象，一个程序通常只建一次 | `OfflineRecognizer.from_sense_voice(...)` |
| <span id="g-数据流"></span>数据流 | Stream | sherpa-onnx 中装一段待识别音频的“容器”，每段录音建一个 | `stream = recognizer.create_stream()` |
| <span id="g-语音活动检测"></span>语音活动检测 | Voice Activity Detection, VAD | 判断一段声音里哪些时间有人在说话、哪些是静音或噪声的技术 | 把 51 秒的会议录音切成 7 句 |
| <span id="g-时间戳"></span>时间戳 | Timestamp | 每句话（或每个字）在录音中开始和结束的时间 | 第 2 句 10.18—17.10 秒 |
| <span id="g-SRT-字幕"></span>SRT 字幕 | SubRip Subtitle | 最常见的字幕文件格式，每条字幕由序号、起止时间和文字组成 | `00:00:10,182 --> 00:00:17,100` |
| <span id="g-文本逆正则化"></span>文本逆正则化 | Inverse Text Normalization, ITN | 把识别出的口语化写法转换成书面写法，如数字、日期、金额 | “二零二六年五月一号”→“2026年5月1日” |
| <span id="g-标点恢复"></span>标点恢复 | Punctuation Restoration | 给没有标点的识别结果加上逗号、句号、问号 | Paraformer 的结果没有标点，SenseVoice 自带 |
| <span id="g-非流式识别"></span>非流式识别 | Non-streaming ASR | 一段话说完、录音完整以后再整体识别 | 录音文件转写 |
| <span id="g-流式识别"></span>流式识别 | Streaming ASR | 一边接收声音一边输出文字，不用等说完 | 会议实时字幕、语音输入法 |
| <span id="g-唤醒词"></span>唤醒词 | Wake Word | 让设备从待机状态开始工作的特定词语 | “你好小站” |
| <span id="g-误唤醒"></span>误唤醒 | False Alarm | 没有说唤醒词，设备却被唤醒 | 说“你好小张”时服务站亮了 |
| <span id="g-漏唤醒"></span>漏唤醒 | False Rejection | 说了唤醒词，设备却没有反应 | 阈值太高时“小站小站”叫不醒 |
| <span id="g-热词"></span>热词 | Hotword | 预先告诉识别系统、让它在识别时优先考虑的词，常用于人名、地名、专业术语 | 把“樟树苑”“韦嘉怡”设为热词 |

## 第 5 章 语音合成原理：从文字到声音

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-文本前端"></span>文本前端 | Text Front-end | 语音合成中把文字转换成发音信息（读法、拼音、停顿）的部分 | 把“3号楼”变成“san1 hao4 lou2” |
| <span id="g-文本正则化"></span>文本正则化 | Text Normalization, TN | 把数字、日期、符号等非汉字写法转换成实际的读法 | “¥1500”→“一千五百元” |
| <span id="g-分词"></span>分词 | Word Segmentation | 把连续的汉字句子切分成一个个词 | “银行/的/工作人员” |
| <span id="g-多音字"></span>多音字 | Polyphonic Character | 有两个或更多读音、要根据词语和上下文确定读音的字 | “行”在“银行”里读 háng，在“行走”里读 xíng |
| <span id="g-变调"></span>变调 | Tone Sandhi | 字的声调在连读时发生变化的现象 | “一个”的“一”读 yí，“你好”的“你”读 ní |
| <span id="g-韵律"></span>韵律 | Prosody | 说话时的停顿、轻重、快慢和语调，决定听起来自然不自然 | 逗号处停顿、疑问句句末上扬 |
| <span id="g-声码器"></span>声码器 | Vocoder | 把梅尔频谱等声学特征转换成声音波形的模块 | HiFi-GAN、Vocos |
| <span id="g-拼接合成"></span>拼接合成 | Concatenative Synthesis | 事先录好大量语音片段，合成时挑选合适的片段拼接起来的方法 | 早期的火车站报站系统 |
| <span id="g-统计参数合成"></span>统计参数合成 | Statistical Parametric Synthesis | 用 HMM 等统计模型预测声音参数，再用程序生成声音的方法 | 2000 年代的手机朗读功能 |
| <span id="g-神经网络语音合成"></span>神经网络语音合成 | Neural TTS | 用神经网络预测梅尔频谱并生成波形的合成方法 | Tacotron 2、FastSpeech 2、VITS、Matcha-TTS |
| <span id="g-平均意见分"></span>平均意见分 | Mean Opinion Score, MOS | 请多人给语音按 1—5 分打分后取平均，评价合成语音自然度的主观指标 | 小组 6 人给 5 个版本打分 |
| <span id="g-回识别字错率"></span>回识别字错率 | ASR-based CER | 把合成的语音交给识别模型，看识别结果和原文的字错率，用来检查读得对不对 | “请提前储水”回识别成“请提前出水” |

## 第 6 章 语音合成实战：多音色与有声书

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-多说话人合成"></span>多说话人合成 | Multi-speaker TTS | 用很多人的录音训练一个合成模型，用说话人编号选择用谁的声音说话 | VITS AISHELL-3 模型有 174 种声音，编号 0—173 |
| <span id="g-说话人编号"></span>说话人编号 | Speaker ID, sid | 多说话人合成模型里代表某一种声音的整数，换编号就换声音 | Kokoro 的 3—57 号是中文女声，58—102 号是中文男声 |
| <span id="g-语速"></span>语速 | Speaking Rate | 说话的快慢；合成模型里通常用一个倍数控制，1.0 是正常速度 | 语速 1.3 时同一句话从 4.45 秒缩短到 3.68 秒 |
| <span id="g-中英混读"></span>中英混读 | Code-switching TTS | 一句话里既有中文又有英文时，两种语言都能读对的合成能力 | “请连接 Community 5 G 的 Wi-Fi” |
| <span id="g-有声书"></span>有声书 | Audiobook | 把一篇较长的文字朗读成可以连续收听的音频作品，通常带片头、章节和停顿 | 把 1500 字的告居民书做成 5 分半钟的 MP3 |
| <span id="g-SSML"></span>SSML | Speech Synthesis Markup Language | 语音合成标记语言，用类似网页标签的写法告诉合成服务在哪停顿、怎么读、读多快 | `<break time="500ms"/>` 停半秒 |
| <span id="g-显式标识"></span>显式标识 | Explicit Label | 在生成合成的内容里用人能直接看到或听到的方式标明“由人工智能生成”，如音频开头的语音提示 | 有声书开头的“本音频由人工智能语音合成” |
| <span id="g-隐式标识"></span>隐式标识 | Implicit Label | 写在文件元数据等处、人不容易直接感知但机器能读出的“人工智能生成”标记 | MP3 注释字段里写“AI生成” |

## 第 7 章 声纹识别与语音转换

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-声纹"></span>声纹 | Voiceprint | 一个人嗓音的独特特征，像指纹一样可以用来区分不同的人；在计算机里用一串数字（声纹向量）表示 | CAM++ 模型把一段话变成 192 个数 |
| <span id="g-声纹向量"></span>声纹向量 | Speaker Embedding | 声纹模型把一段语音转换成的固定长度的一串数字，同一个人的向量相近，不同人的相远 | 志愿者 A 两段录音的向量相似度 0.94 |
| <span id="g-余弦相似度"></span>余弦相似度 | Cosine Similarity | 两个向量夹角的余弦值，范围 -1 到 1，越接近 1 方向越一致、越像 | 未知录音和 C 的相似度 0.91 |
| <span id="g-说话人确认"></span>说话人确认 | Speaker Verification | 判断一段语音“是不是某个人说的”，回答是或否 | 声纹登录：你说你是 A，系统核验 |
| <span id="g-说话人辨认"></span>说话人辨认 | Speaker Identification | 判断一段语音“是已注册的哪个人说的”，从多人中选一个 | 未知录音最像 A、B、C、D 中的谁 |
| <span id="g-说话人日志"></span>说话人日志 | Speaker Diarization | 把一段多人录音切成小段，标出“谁在什么时候说话” | 议事会录音分出主持人、老王、李阿姨 |
| <span id="g-误接受率"></span>误接受率 | False Acceptance Rate, FAR | 冒充者被错误放行的次数占冒充测试总次数的比例 | 门槛 0.5 时 112 次冒充有 15 次被放行，FAR 13.4% |
| <span id="g-误拒绝率"></span>误拒绝率 | False Rejection Rate, FRR | 本人被错误拒绝的次数占本人测试总次数的比例 | 门槛 0.9 时 16 次本人测试有 10 次被拒，FRR 62.5% |
| <span id="g-等错误率"></span>等错误率 | Equal Error Rate, EER | 调节门槛使误接受率等于误拒绝率时的错误率，越低说明系统越好 | EER 1% 表示两种错误都在 1% 左右 |
| <span id="g-语音转换"></span>语音转换 | Voice Conversion, VC | 保留一段语音“说了什么”，把“谁在说”换成另一个人的音色的技术，俗称变声 | 把 A 说的话换成 C 的声音 |

## 第 8 章 语音克隆：技术、伦理与授权

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-零样本克隆"></span>零样本克隆 | Zero-shot Voice Cloning | 不用重新训练模型，只给几秒到十几秒的参考音和它的文字，就能用这个音色朗读新内容的克隆方法 | ZipVoice 用 3 秒参考音克隆，相似度 0.70 |
| <span id="g-微调式克隆"></span>微调式克隆 | Fine-tuning Voice Cloning | 准备几分钟到一小时某人的录音，在预训练模型上再训练一会儿，得到专属这个人的合成模型 | 用 GPT-SoVITS 训练自己的声音模型 |
| <span id="g-参考音"></span>参考音 | Reference Audio | 克隆时提供给模型、代表目标音色的一段录音，通常要求安静、单人、几秒到十几秒，并附上准确的文字 | 志愿者 B 的 9 秒自我介绍 |
| <span id="g-声音权益"></span>声音权益 | Voice Rights | 自然人对自己声音享有的人格权益，《民法典》规定参照肖像权保护，未经许可不得使用 | 配音演员的声音被 AI 化出售，法院判侵权 |
| <span id="g-深度合成"></span>深度合成 | Deep Synthesis | 利用深度学习等生成合成类算法制作文本、图像、音频、视频等网络信息的技术，包括合成人声、仿声 | 语音克隆、AI 换脸 |
| <span id="g-单独同意"></span>单独同意 | Separate Consent | 针对某一项个人信息处理活动专门、单独取得的同意，不能和其他条款捆绑一次勾选 | 采集声纹前单独弹窗征求同意 |
| <span id="g-声音授权书"></span>声音授权书 | Voice Authorization | 声音所有人书面同意他人在约定用途、范围、期限内采集和使用其声音的文件 | 附录 D 的《声音使用授权书》 |
| <span id="g-音频水印"></span>音频水印 | Audio Watermark | 嵌入在声音里、人耳几乎听不出、但用密钥可以检测出来的标记，用来证明来源或标明 AI 生成 | 实验 8-3 的水印比声音低 34 dB，转成 MP3 后仍能检测 |

## 第 9 章 语音交互应用与综合项目

| 术语 | 英文 | 定义 | 例子 |
|---|---|---|---|
| <span id="g-端到端延迟"></span>端到端延迟 | End-to-end Latency | 从用户说完话到听到系统回答的总等待时间，是各环节耗时之和 | 本书小助手实测约 1.4 秒 |
| <span id="g-首包延迟"></span>首包延迟 | First-packet Latency | 合成或回答开始后，到发出第一段声音所用的时间；先合成第一句就播放可以缩短它 | 首句合成 0.49 秒，整段合成 1.15 秒 |
| <span id="g-意图理解"></span>意图理解 | Intent Understanding | 判断用户这句话想做什么、要问什么，是语音助手“懂”的那一步 | “暖气不热怎么办”→ 供暖问题 |
| <span id="g-兜底回复"></span>兜底回复 | Fallback Response | 系统听不懂或答不了时给出的礼貌回复，引导用户换说法或转人工 | “这个问题我还不会回答，请拨打服务热线” |
| <span id="g-打断"></span>打断 | Barge-in | 系统正在说话时，用户插话，系统能停下来听用户说 | 小助手读通知时用户说“停” |
| <span id="g-模型量化"></span>模型量化 | Model Quantization | 把模型参数从 32 位小数换成 8 位整数等更短的表示，让模型更小更快，精度略有损失 | 唤醒词模型从 12.5 MB 降到 4.8 MB |
| <span id="g-端侧部署"></span>端侧部署 | On-device Deployment | 把模型放在手机、音箱、车机等用户自己的设备上运行，不依赖网络 | 离线语音输入法 |
