---
title: 在线模拟卷
description: 按期末开卷考试的题型和分值，从各章课后练习中组成的两套在线模拟卷，可以直接作答并查看解析
---

# 在线模拟卷

本课程期末为开卷考试，题目侧重理解和应用。下面两套模拟卷按期末考试的题型和分值，从各章课后练习中抽题组成，覆盖全书 9 章：

| 题型 | 题数 | 每题分值 | 合计 |
|---|---|---|---|
| 单项选择题 | 20 | 2 | 40 |
| 多项选择题 | 5 | 4 | 20 |
| 判断题 | 10 | 1 | 10 |
| 简答题 | 2 | 10 | 20 |
| 实操题 | 1 | 10 | 10 |

建议限时 90 分钟，先独立做完一整套，再展开“答案与解析”核对。简答题和实操题按参考答案的要点自评。实操题要在电脑上运行代码完成。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。

## 模拟卷一

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="B" markdown>

**1.** 把会议录音自动变成文字纪要，主要用到的是（　　）。

- A. 语音合成
- B. 语音识别
- C. 语音克隆
- D. 语音唤醒

</div>

??? tip "答案与解析"
    **答案：B**

    声音 → 文字是语音识别。语音合成方向相反（文字 → 声音）。

    考查：五类语音任务 · 认知层次：理解 · [回看 1.1.2](chapters/01-overview/index.md#112)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**2.** 电话银行让客户说一句话来确认“是不是本人”，用到的是（　　）。

- A. 语音识别
- B. 语音合成
- C. 声纹识别
- D. 语音唤醒

</div>

??? tip "答案与解析"
    **答案：C**

    判断“是不是某个人”是声纹识别（说话人确认）。语音识别只关心说了什么，不关心是谁说的。

    考查：声纹识别与语音识别的区别 · 认知层次：理解 · [回看 1.1.2](chapters/01-overview/index.md#112)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**3.** 男声和女声说同一个“啊”，听起来女声更高，主要是因为女声的（　　）更高。

- A. 振幅
- B. 采样率
- C. 基频
- D. 位深

</div>

??? tip "答案与解析"
    **答案：C**

    音高由基频决定，女声基频约 200—250 Hz，男声约 100—150 Hz。振幅决定响度；采样率和位深是录音设备的参数，与说话人无关。

    考查：音高与基频 · 认知层次：理解 · [回看 2.1.2](chapters/02-audio/index.md#212)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**4.** 同一个人用同样的音高先说“啊”再说“衣”，两段声音的主要区别在于（　　）。

- A. 基频不同
- B. 共振峰位置不同
- C. 采样率不同
- D. 声道数不同

</div>

??? tip "答案与解析"
    **答案：B**

    元音由口腔形状决定，口腔形状决定共振峰。实验 2-1 中三个元音的音高都是 214 Hz，区别在共振峰和频谱重心。

    考查：共振峰 · 认知层次：理解 · [回看 2.1.2](chapters/02-audio/index.md#212)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**5.** 在识别系统的四块积木中，负责判断“这串文字通不通顺”的是（　　）。

- A. 特征提取
- B. 语言模型
- C. 声学模型
- D. 声码器

</div>

??? tip "答案与解析"
    **答案：B**

    声学模型管“声音像哪个音”，语言模型管“文字通不通顺”。声码器是语音合成里的部件（第 5 章）。

    考查：识别系统的组成 · 认知层次：记忆 · [回看 3.2](chapters/03-asr-principles/index.md#32)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**6.** DTW 主要解决的问题是（　　）。

- A. 录音里有噪声
- B. 同音字太多
- C. 同一个词说得快慢不同，帧数不一样
- D. 录音的采样率不同

</div>

??? tip "答案与解析"
    **答案：C**

    DTW 允许一帧对多帧，把快慢不同的两段语音对齐后再算距离。

    考查：DTW · 认知层次：理解 · [回看 3.3.2](chapters/03-asr-principles/index.md#332)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**7.** 社区来电以普通话为主，偶尔有粤语和英语，根据实验 4-1，最合适的识别模型是（　　）。

- A. Whisper tiny
- B. Paraformer
- C. SenseVoice
- D. 唤醒模型

</div>

??? tip "答案与解析"
    **答案：C**

    实验 4-1 中只有 SenseVoice 把普通话、粤语、英语都识别对了，来电的字错率也最低。

    考查：按场景选模型 · 认知层次：评价 · [回看 4.1](chapters/04-asr-practice/index.md#41)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**8.** 用 sherpa-onnx 识别时，把一段 44.1 kHz 的录音谎报成 16000 Hz 喂给模型，会出现（　　）。

- A. 识别结果完全一样
- B. 声音被当成慢放，识别结果完全不对
- C. 识别速度变快，结果更准
- D. 自动报错并提示正确的采样率

</div>

??? tip "答案与解析"
    **答案：B**

    `accept_waveform` 的采样率必须如实填写，模型才能正确转换。谎报后每秒的采样点被当成近 3 秒，相当于慢放。

    考查：采样率的坑 · 认知层次：理解 · [回看 4.2](chapters/04-asr-practice/index.md#42)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**9.** 在语音合成系统中，把梅尔频谱转换成声音波形的是（　　）。

- A. 文本前端
- B. 声码器
- C. 语言模型
- D. 分词器

</div>

??? tip "答案与解析"
    **答案：B**

    文本前端把文字变成发音说明书，声学模型画出梅尔频谱，声码器把梅尔频谱变成声音。

    考查：合成系统的组成 · 认知层次：记忆 · [回看 5.2](chapters/05-tts-principles/index.md#52)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**10.** 把“¥1500”转换成“一千五百元”，属于文本前端中的（　　）。

- A. 分词
- B. 变调
- C. 文本正则化
- D. 韵律预测

</div>

??? tip "答案与解析"
    **答案：C**

    把数字、符号等写法转换成读法，是文本正则化。

    考查：文本正则化 · 认知层次：理解 · [回看 5.3.1](chapters/05-tts-principles/index.md#531)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**11.** 在多说话人合成模型中，要换一种声音，应该修改（　　）。

- A. 语速 `speed`
- B. 采样率
- C. 说话人编号 `sid`
- D. 模型文件

</div>

??? tip "答案与解析"
    **答案：C**

    多说话人模型用说话人编号选择声音；语速只改快慢。

    考查：说话人编号 · 认知层次：记忆 · [回看 6.2.1](chapters/06-tts-practice/index.md#621)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**12.** 一段合成语音的平均音高是 135 Hz，它最可能是（　　）。

- A. 女声
- B. 男声
- C. 儿童的声音
- D. 无法判断，平均音高和男女无关

</div>

??? tip "答案与解析"
    **答案：B**

    成年男性说话的平均基频一般在 90—160 Hz，女性一般在 180—300 Hz。

    考查：用平均音高判断男女 · 认知层次：应用 · [回看 6.2.1](chapters/06-tts-practice/index.md#621)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**13.** 声纹模型 CAM++ 对一段 2 秒的录音和一段 20 秒的录音，输出的声纹向量（　　）。

- A. 长度分别是 2 和 20
- B. 长度都是 192
- C. 长度和采样率有关
- D. 没有固定长度

</div>

??? tip "答案与解析"
    **答案：B**

    声纹模型不管录音多长，都输出固定长度的向量，CAM++ 是 192 个数。

    考查：声纹向量 · 认知层次：记忆 · [回看 7.1](chapters/07-speaker/index.md#71)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**14.** 向量 $a = (1, 0)$ 和 $b = (0, 2)$ 的余弦相似度是（　　）。

- A. 1
- B. 2
- C. 0
- D. -1

</div>

??? tip "答案与解析"
    **答案：C**

    点积 $1 \times 0 + 0 \times 2 = 0$，所以余弦相似度为 0，两个向量互相垂直。

    考查：余弦相似度计算 · 认知层次：应用 · [回看 7.2](chapters/07-speaker/index.md#72)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**15.** 零样本克隆和微调式克隆最主要的区别是（　　）。

- A. 零样本克隆效果一定更好
- B. 零样本克隆只需几秒参考音、不用重新训练
- C. 微调式克隆不需要任何录音
- D. 零样本克隆只能克隆男声

</div>

??? tip "答案与解析"
    **答案：B**

    零样本克隆直接用几秒到十几秒的参考音；微调式克隆要几分钟以上的录音并重新训练。

    考查：两条技术路线 · 认知层次：理解 · [回看 8.2.1](chapters/08-voice-cloning/index.md#821)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**16.** 下面哪一段最适合作为克隆的参考音？（　　）

- A. 在食堂录的 30 秒聊天，有好几个人说话
- B. 对着麦克风大喊的 10 秒口号，有破音
- C. 安静房间里的 2 秒“你好”
- D. 安静房间里平稳朗读的 10 秒，文字和录音完全对应

</div>

??? tip "答案与解析"
    **答案：D**

    参考音要安静、单人、5—15 秒、不削波、文字完全对应。

    考查：参考音要求 · 认知层次：应用 · [回看 8.3](chapters/08-voice-cloning/index.md#83)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**17.** 语音助手的端到端延迟指的是（　　）。

- A. 识别模型的实时率
- B. 合成一整段回答的时间
- C. 用户说完话到听到回答的总等待时间
- D. 唤醒词检测的时间

</div>

??? tip "答案与解析"
    **答案：C**

    端到端延迟是各环节耗时之和，是用户实际感受到的等待时间。

    考查：端到端延迟 · 认知层次：记忆 · [回看 9.1](chapters/09-applications/index.md#91)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**18.** 实验 9-4 中，“先合成第一句就播放”比“整段合成完再播放”少等约 0.7 秒，这缩短的是（　　）。

- A. 首包延迟
- B. 识别耗时
- C. VAD 静音等待
- D. 网络传输

</div>

??? tip "答案与解析"
    **答案：A**

    首包延迟是从开始合成到发出第一段声音的时间，只合成第一小句就能更快开口。

    考查：首包延迟 · 认知层次：理解 · [回看 9.1](chapters/09-applications/index.md#91)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**19.** 《民法典》第一千零二十三条规定，对自然人声音的保护（　　）。

- A. 参照适用肖像权保护的有关规定
- B. 参照适用著作权保护的有关规定
- C. 只保护公众人物的声音
- D. 不受法律保护

</div>

??? tip "答案与解析"
    **答案：A**

    第一千零二十三条第二款：对自然人声音的保护，参照适用肖像权保护的有关规定。

    考查：声音权益 · 认知层次：记忆 · [回看 8.6.1](chapters/08-voice-cloning/index.md#861)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**20.** 用户问“厨房水龙头坏了怎么办”，关键词匹配却回答了停水通知，最可能的原因是（　　）。

- A. 识别模型听错了
- B. 合成模型读错了
- C. 问答库里没有任何关键词
- D. 关键词匹配不懂意思，“水”命中了停水的关键词

</div>

??? tip "答案与解析"
    **答案：D**

    “水”和“坏了”各命中一条问答的关键词，程序选了排在前面的“停水”。

    考查：关键词匹配的局限 · 认知层次：分析 · [回看 9.4](chapters/09-applications/index.md#94)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**1.** “社区语音服务站”用退休播音员林老师的声音念通知，下列做法正确的有（　　）。

- A. 先请林老师签署书面授权，写清用途和期限
- B. 在发布的音频里标明“本音频由 AI 合成”
- C. 林老师是熟人，口头说一声就可以用在任何地方
- D. 林老师以后不想用了，应当可以撤回授权

</div>

??? tip "答案与解析"
    **答案：ABD**

    克隆声音要取得本人的单独同意，最好书面写清用途、范围、期限和撤回方式；AI 合成的内容要加标识。C 错在“口头”和“任何地方”。第 8 章详细讲。

    考查：声音的个人信息保护 · 认知层次：评价 · [回看 1.6](chapters/01-overview/index.md#16)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**2.** 下列属于端到端识别模型的有（　　）。

- A. Whisper
- B. Paraformer
- C. 实验 3-1 的 DTW 模板匹配
- D. SenseVoice

</div>

??? tip "答案与解析"
    **答案：ABD**

    三者都是一个神经网络直接从声音到文字。DTW 模板匹配是第一代方法。

    考查：端到端模型 · 认知层次：记忆 · [回看 3.5.2](chapters/03-asr-principles/index.md#352)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**3.** 下列属于文本前端工作的有（　　）。

- A. 确定“银行”中“行”的读音
- B. 把“9:30”转换成“九点三十分”
- C. 把梅尔频谱转换成声音
- D. 标出逗号处的停顿

</div>

??? tip "答案与解析"
    **答案：ABD**

    C 是声码器的工作。

    考查：文本前端 · 认知层次：理解 · [回看 5.3](chapters/05-tts-principles/index.md#53)
    { .quiz-meta }

<div class="quiz" data-answer="ABC" data-multi="true" markdown>

**4.** 下面哪些情况会让本人的声纹验证分数明显下降？（　　）

- A. 注册时用手机录音，验证时通过电话线路说话
- B. 验证时只说了 1 秒
- C. 验证时环境很吵
- D. 验证时说的内容和注册时不一样

</div>

??? tip "答案与解析"
    **答案：ABC**

    声纹模型忽略说话的内容，所以内容不同影响不大；但录音条件、时长、噪声变化会让分数大幅下降（实验 7-2 中电话音质平均分从 0.89 降到 0.59）。

    考查：影响声纹的因素 · 认知层次：分析 · [回看 7.3.3](chapters/07-speaker/index.md#733)
    { .quiz-meta }

<div class="quiz" data-answer="ABCD" data-multi="true" markdown>

**5.** 一份合格的声音授权书应当写清（　　）。

- A. 用途和发布范围
- B. 授权期限
- C. 是否商用、有无报酬
- D. 撤回方式和数据删除

</div>

??? tip "答案与解析"
    **答案：ABCD**

    还包括授权双方、授权内容、标识要求等，共 8 项要素。

    考查：声音授权书 · 认知层次：记忆 · [回看 8.7.1](chapters/08-voice-cloning/index.md#871)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** 语音识别和声纹识别是同一种技术的两种叫法。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    语音识别认“说了什么”，声纹识别认“是谁说的”，关注点正好相反。

    考查：语音识别与声纹识别 · 认知层次：理解 · [回看 1.4](chapters/01-overview/index.md#14)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** 采样率越高越好，所以语音识别应该用 48 kHz 的录音。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    人说话的主要信息在 8000 Hz 以下，16 kHz 已经够用；识别模型一般也按 16 kHz 训练，更高的采样率只会让文件更大。

    考查：采样率选择 · 认知层次：评价 · [回看 2.2.1](chapters/02-audio/index.md#221)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**3.** 在 HMM 中，说话快慢不同可以用“每个状态停留的帧数不同”来自然地表示。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    说得慢，每个发音阶段停留的帧数多；说得快，停留的帧数少，不需要另做 DTW。

    考查：HMM · 认知层次：理解 · [回看 3.4.1](chapters/03-asr-principles/index.md#341)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** sherpa-onnx 中的 `OfflineRecognizer` 表示这个识别器不能联网。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    这里的 Offline 指“非流式”（录音完整后整体识别），流式识别器叫 `OnlineRecognizer`。两者都在本机运行。

    考查：sherpa-onnx 识别器 · 认知层次：理解 · [回看 4.2](chapters/04-asr-practice/index.md#42)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**5.** 文本正则化规则的顺序很重要，手机号规则应该放在普通数字规则之前。（　　）

</div>

??? tip "答案与解析"
    **答案：√**

    否则手机号会先被普通数字规则按数值读出来。

    考查：文本正则化 · 认知层次：理解 · [回看 5.3.1](chapters/05-tts-principles/index.md#531)
    { .quiz-meta }

<div class="quiz" data-answer="B" data-type="tf" markdown>

**6.** 实时率大于 1 的合成模型没有任何用处。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：错误**

    有声书、广播等提前生成的场合可以使用；只有实时对话要求实时率远小于 1。

    考查：实时率 · 认知层次：理解 · [回看 6.1](chapters/06-tts-practice/index.md#61)
    { .quiz-meta }

<div class="quiz" data-answer="A" data-type="tf" markdown>

**7.** 同一个人说两句内容完全不同的话，声纹相似度仍然可以很高。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：正确**

    声纹模型故意忽略说话内容，实验 7-1 中 A 的两句不同的话相似度为 0.94。

    考查：声纹与内容无关 · 认知层次：理解 · [回看 7.1](chapters/07-speaker/index.md#71)
    { .quiz-meta }

<div class="quiz" data-answer="B" data-type="tf" markdown>

**8.** 公众人物的声音已经公开，所以可以随意克隆使用。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：错误**

    公众人物同样享有声音权益，未经授权一律不克隆。

    考查：声音权益 · 认知层次：评价 · [回看 8.7.2](chapters/08-voice-cloning/index.md#872)
    { .quiz-meta }

<div class="quiz" data-answer="A" data-type="tf" markdown>

**9.** 关键词匹配对识别中的个别错字不太敏感，只要关键词还在就能答对。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：正确**

    实验 9-1 中，“老年时，唐中午几点开饭”仍因“开饭”答对。

    考查：关键词匹配的长处 · 认知层次：理解 · [回看 9.4](chapters/09-applications/index.md#94)
    { .quiz-meta }

<div class="quiz" data-answer="A" data-type="tf" markdown>

**10.** 参考音的文字必须和录音内容完全对应，否则克隆结果容易读错。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：正确**

    零样本模型靠参考音的文字和声音对齐，再“续写”新内容。

    考查：零样本克隆原理 · 认知层次：理解 · [回看 8.2.2](chapters/08-voice-cloning/index.md#822)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 用自己的话说明模板匹配、HMM、端到端模型三代识别方法各自的基本思路，以及后一代解决了前一代的什么问题。

??? tip "答案与解析"
    **参考答案**：模板匹配为每个词存一个录音模板，用 DTW 对齐后比较距离，最像的就是结果，但只认特定人的读法、词多了无法录模板。HMM 用概率描述“看不见的发音阶段”和“听得到的声音特征”，用很多人的录音训练，能适应不同的人；以声韵母为单位，配合发音词典和语言模型，可以识别任意句子，但系统部件多、搭建复杂。端到端模型用一个神经网络直接从声音到文字，只要“录音 + 文字”就能训练，借助海量数据大幅提高了准确率，也简化了系统。

    考查：识别方法的发展 · 认知层次：理解 · [回看 3.3](chapters/03-asr-principles/index.md#33)
    { .quiz-meta }

**2.** 请比较微调式克隆和零样本克隆，并说明为什么零样本克隆的风险更大。

??? tip "答案与解析"
    **参考答案**：微调式克隆需要几分钟到一小时的录音，要在 GPU 上训练，效果更像；零样本克隆只要 3—15 秒参考音，不用训练，CPU 就能运行。零样本克隆风险更大，因为一条语音消息、一段短视频就足以克隆，本人可能完全不知道自己的声音被采集，门槛低、隐蔽性强。

    考查：两条技术路线 · 认知层次：分析 · [回看 8.2.1](chapters/08-voice-cloning/index.md#821)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 修改 `lab6_3_audiobook.py`：（1）正文改用 Kokoro 20 号音色、语速 0.9；（2）结尾也加一句“本音频由人工智能语音合成”；（3）把 MP3 比特率改成 32 kbps。运行后记录合成用时、总时长和 MP3 大小，并说明 32 kbps 是否适合发到业主群。

??? tip "答案与解析"
    **参考做法**：（1）`BODY = ("kokoro", 20, 0.9)`；（2）在 `parts += [chime(), silence(0.5)]` 前加 `parts += [label, silence(0.6)]`；（3）把 `"-b:a", "64k"` 改成 `"32k"`。正文换成 Kokoro 后实时率约 1.3，合成用时会从不到 1 分钟增加到 7 分钟以上；语速 0.9 使总时长变长；32 kbps 的 MP3 大小约为 64 kbps 的一半。语音以人声为主，32 kbps 一般仍能听清，适合手机流量有限的老人，但要自己听一遍确认音质。

    考查：有声书流水线 · 认知层次：应用 · [回看实验 6-3](chapters/06-tts-practice/index.md#6-3)
    { .quiz-meta }

## 模拟卷二

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="D" markdown>

**1.** 智能音箱平时一直在听，但只有听到“小爱同学”才开始工作。这样设计的主要原因不包括（　　）。

- A. 省电
- B. 避免把家里的闲聊都上传，保护隐私
- C. 避免误把电视里的话当成指令
- D. 唤醒词能提高合成语音的音质

</div>

??? tip "答案与解析"
    **答案：D**

    唤醒和合成音质没有关系。唤醒的作用是省电、保护隐私、减少误操作。

    考查：语音唤醒 · 认知层次：理解 · [回看 1.2](chapters/01-overview/index.md#12)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**2.** 在一次语音问答中，“从识别出的文字里判断用户想问活动时间”属于哪个环节？（　　）

- A. 唤醒
- B. 理解
- C. 识别
- D. 合成

</div>

??? tip "答案与解析"
    **答案：B**

    识别只负责把声音变成文字，判断“想干什么”是理解。实验 1-3 用关键词做了这一步。

    考查：语音对话流水线 · 认知层次：理解 · [回看 1.2](chapters/01-overview/index.md#12)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**3.** 一段 2 分钟、单声道、8 kHz、16 位的 WAV 电话录音，大小约为（　　）。

- A. 0.23 MB
- B. 0.92 MB
- C. 3.66 MB
- D. 1.83 MB

</div>

??? tip "答案与解析"
    **答案：D**

    8000 × 16 ÷ 8 × 1 × 120 = 1 920 000 字节 ≈ 1.83 MB。和 16 kHz 1 分钟的大小正好一样：采样率减半、时长加倍。

    考查：文件大小计算 · 认知层次：应用 · [回看 2.2.3](chapters/02-audio/index.md#223)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**4.** 在语谱图上，一条从下到上贯穿的竖直亮线，最可能是（　　）。

- A. 口哨声
- B. 持续的元音
- C. 敲门声这样短促的敲击
- D. 静音

</div>

??? tip "答案与解析"
    **答案：C**

    短促的敲击在极短时间内包含各种频率，在语谱图上是竖线。口哨是细横线，元音是一排横线和共振峰横带，静音是暗的。

    考查：读语谱图 · 认知层次：理解 · [回看 2.4.3](chapters/02-audio/index.md#243)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**5.** 在“隔墙听骰子”的比喻中，对应语音识别里“每一帧录到的 MFCC”的是（　　）。

- A. 用的是哪颗骰子
- B. 换不换骰子的规律
- C. 每颗骰子的形状
- D. 听到的点数

</div>

??? tip "答案与解析"
    **答案：D**

    听得到的点数是观察，对应每帧的 MFCC；用哪颗骰子是隐状态，对应看不见的发音阶段。

    考查：HMM 的基本概念 · 认知层次：理解 · [回看 3.4.1](chapters/03-asr-principles/index.md#341)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**6.** CTC 逐帧输出“\_好好\_\_好\_的的\_”（\_ 表示空白），折叠后的结果是（　　）。

- A. 好的
- B. 好好的
- C. 好好好的的
- D. 好\_好\_的

</div>

??? tip "答案与解析"
    **答案：B**

    先合并连续重复：\_ 好 \_ 好 \_ 的 \_；再删掉空白：好好的。两个“好”之间有空白隔开，所以保留两个。

    考查：CTC 折叠规则 · 认知层次：应用 · [回看 3.5.2](chapters/03-asr-principles/index.md#352)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**7.** 用 VAD 切分会议录音，发现一句话经常被切成两三截，应该（　　）。

- A. 调小最短静音
- B. 调大最短语音
- C. 降低阈值
- D. 调大最短静音

</div>

??? tip "答案与解析"
    **答案：D**

    一句话被切断，说明句中的短停顿被当成了句子结束，要把“最短静音”调大，静音更长才算结束。

    考查：VAD 参数 · 认知层次：应用 · [回看 4.3.1](chapters/04-asr-practice/index.md#431)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**8.** 把识别结果“百分之十五”转换成“15%”，叫（　　）。

- A. 标点恢复
- B. 文本正则化
- C. 文本逆正则化
- D. 热词

</div>

??? tip "答案与解析"
    **答案：C**

    把口语说法变成书面写法是逆正则化（ITN）；反过来把写法变成说法是正则化，用在语音合成中。

    考查：文本逆正则化 · 认知层次：理解 · [回看 4.4](chapters/04-asr-practice/index.md#44)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**9.** “一个”的“一”读 yí，依据的是（　　）。

- A. 两个第三声连读
- B. “一”在第一声前读第四声
- C. “一”在词尾读原调
- D. “一”在第四声前读第二声

</div>

??? tip "答案与解析"
    **答案：D**

    “个”是第四声，“一”在第四声前变为第二声。

    考查：变调 · 认知层次：应用 · [回看 5.3.3](chapters/05-tts-principles/index.md#533)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**10.** 实验 5-2 中，拼接合成听起来“一字一顿”，主要原因是（　　）。

- A. 采样率太低
- B. 每个字都是单独读的，带着完整的声调，没有整句的语调
- C. 声码器太慢
- D. 识别模型识别错了

</div>

??? tip "答案与解析"
    **答案：B**

    拼接版的音高曲线每个字都“从头来一遍”，没有整句话从高到低的语调。

    考查：拼接合成 · 认知层次：分析 · [回看 5.4.1](chapters/05-tts-principles/index.md#541)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**11.** VITS AISHELL-3 模型输出 8000 Hz 的声音，因此（　　）。

- A. 4000 Hz 以上的声音成分全部丢失，听起来像电话
- B. 音质比 24000 Hz 的模型更好
- C. 只能合成男声
- D. 不能调语速

</div>

??? tip "答案与解析"
    **答案：A**

    按采样定理，8000 Hz 的采样率最高只能记录 4000 Hz 的频率。

    考查：采样率与音质 · 认知层次：应用 · [回看 6.1](chapters/06-tts-practice/index.md#61)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**12.** 一家公司要做可以商用的多音色语音播报产品，本书的四个模型中最合适的是（　　）。

- A. Matcha 中文
- B. 都不能商用
- C. Kokoro
- D. 只能用 Matcha，因为它最快

</div>

??? tip "答案与解析"
    **答案：C**

    Kokoro 采用 Apache-2.0 许可，可以商用，有 100 多种音色；Matcha 的训练数据只允许非商业使用。

    考查：模型选择与许可 · 认知层次：评价 · [回看 6.1](chapters/06-tts-practice/index.md#61)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**13.** “这段会议录音里，谁在什么时候说话？”属于（　　）。

- A. 说话人确认
- B. 说话人辨认
- C. 语音转换
- D. 说话人日志

</div>

??? tip "答案与解析"
    **答案：D**

    说话人日志要把录音切成段，并标出每段是谁说的。

    考查：三种任务 · 认知层次：理解 · [回看 7.4](chapters/07-speaker/index.md#74)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**14.** 声纹验证中把门槛从 0.6 调高到 0.9，通常会（　　）。

- A. 误接受率上升，误拒绝率下降
- B. 误接受率下降，误拒绝率上升
- C. 两种错误都下降
- D. 两种错误都不变

</div>

??? tip "答案与解析"
    **答案：B**

    门槛越高越难通过：冒充者更难进来，本人也更容易被拒。

    考查：门槛与两种错误 · 认知层次：理解 · [回看 7.3.2](chapters/07-speaker/index.md#732)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**15.** 在 2024 年北京互联网法院 AI 声音侵权案中，法院认为（　　）。

- A. 公司拥有录音制品著作权，就可以把声音做成 AI 音色出售
- B. AI 生成的声音不受任何保护
- C. 录音制品的著作权不等于把声音 AI 化使用的授权
- D. 只要不收费就不构成侵权

</div>

??? tip "答案与解析"
    **答案：C**

    法院认定，在具备可识别性的前提下，声音权益可及于 AI 生成声音；拥有录音的著作权不等于获得 AI 化授权。

    考查：AI 声音侵权案 · 认知层次：理解 · [回看 8.6.1](chapters/08-voice-cloning/index.md#861)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**16.** 《互联网信息服务深度合成管理规定》要求，提供人声等生物识别信息编辑功能的，应当提示使用者依法告知被编辑的个人，并取得其（　　）。

- A. 口头同意
- B. 单独同意
- C. 家属同意
- D. 平台同意

</div>

??? tip "答案与解析"
    **答案：B**

    第十四条第二款要求取得被编辑个人的单独同意。

    考查：深度合成规定 · 认知层次：记忆 · [回看 8.6.3](chapters/08-voice-cloning/index.md#863)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**17.** 语音助手听不懂用户的问题时，最好的做法是（　　）。

- A. 随便选一个最接近的答案回答
- B. 给出兜底回复，请用户换个说法或转人工
- C. 不回答，保持沉默
- D. 让用户重启设备

</div>

??? tip "答案与解析"
    **答案：B**

    听不懂要老实说，并给用户出口。

    考查：兜底回复 · 认知层次：应用 · [回看 9.4](chapters/09-applications/index.md#94)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**18.** 把模型参数从 32 位小数换成 8 位整数，叫做（　　）。

- A. 端侧部署
- B. 重采样
- C. 模型量化
- D. 音量归一化

</div>

??? tip "答案与解析"
    **答案：C**

    量化让模型更小更快，模型文件名中的 int8 就是量化版本。

    考查：模型量化 · 认知层次：记忆 · [回看 9.6.1](chapters/09-applications/index.md#961)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**19.** 下列场景中，必须使用流式识别的是（　　）。

- A. 把一年的来电录音转成文字存档
- B. 线上讲座的实时字幕
- C. 给一部已经剪好的视频配字幕
- D. 统计一批录音的字错率

</div>

??? tip "答案与解析"
    **答案：B**

    实时字幕要边说边出字，只能用流式识别；其他场景录音是完整的，用非流式识别更准。

    考查：流式与非流式 · 认知层次：应用 · [回看 4.5](chapters/04-asr-practice/index.md#45)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**20.** 某系统 112 次冒充测试中有 15 次被放行，误接受率约为（　　）。

- A. 15%
- B. 1.5%
- C. 13.4%
- D. 86.6%

</div>

??? tip "答案与解析"
    **答案：C**

    误接受率 = 15 ÷ 112 ≈ 13.4%。

    考查：误接受率计算 · 认知层次：应用 · [回看 7.3.2](chapters/07-speaker/index.md#732)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="BD" markdown>

**1.** 下列录音毛病中，事后用程序**很难**补救的有（　　）。

- A. 前后有几秒静音
- B. 声音太大造成的削波
- C. 双声道、44.1 kHz，和其他录音格式不统一
- D. 8 kHz 采样丢掉的 4000 Hz 以上的高频

</div>

??? tip "答案与解析"
    **答案：BD**

    静音可以剪，格式可以转；削波和采样时丢掉的高频，信息已经没有记录，补不回来。

    考查：音频处理的能力边界 · 认知层次：评价 · [回看 2.6](chapters/02-audio/index.md#26)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ACD" markdown>

**2.** 社区服务站处理居民来电录音时，符合个人信息保护要求的做法有（　　）。

- A. 通话开始时告知“本次通话将被录音”
- B. 把录音发到志愿者群里，方便大家一起听写
- C. 不再需要的原始录音按规定期限删除
- D. 含敏感信息的录音优先用离线模型识别

</div>

??? tip "答案与解析"
    **答案：ACD**

    录音含个人信息，要告知、最少、安全，发到群里会造成泄露。

    考查：录音隐私 · 认知层次：评价 · [回看 4.7.2](chapters/04-asr-practice/index.md#472)
    { .quiz-meta }

<div class="quiz" data-answer="ACD" data-multi="true" markdown>

**3.** 下面哪些方法可以提高中英混读的效果？（　　）

- A. 选择支持中英混读的模型，如 MeloTTS
- B. 把英文全部改成大写
- C. 要逐个字母读的缩写，字母之间加空格
- D. 实在读不好时，换成中文说法

</div>

??? tip "答案与解析"
    **答案：ACD**

    实验 6-2 中，“App”“AI”这样的大写缩写反而容易读错；字母之间加空格、换中文说法都有效。

    考查：中英混读 · 认知层次：应用 · [回看 6.4.4](chapters/06-tts-practice/index.md#644)
    { .quiz-meta }

<div class="quiz" data-answer="ACD" data-multi="true" markdown>

**4.** 下面哪些属于语音克隆的正当用途（前提是本人授权）？（　　）

- A. 为渐冻症患者保存声音，以后用来和家人交流
- B. 用明星的声音为网店带货
- C. 主播授权后用克隆声音录制新有声书，并标明 AI 合成
- D. 外语教师用自己的声音生成听力材料

</div>

??? tip "答案与解析"
    **答案：ACD**

    未经许可用明星声音带货侵犯声音权益。

    考查：正当用途与风险 · 认知层次：评价 · [回看 8.5](chapters/08-voice-cloning/index.md#85)
    { .quiz-meta }

<div class="quiz" data-answer="ABD" data-multi="true" markdown>

**5.** 智能客服系统通常用到哪些语音模块？（　　）

- A. 语音识别
- B. 语音合成
- C. 语音克隆客户的声音
- D. 声纹核验身份

</div>

??? tip "答案与解析"
    **答案：ABD**

    智能客服识别客户的话、合成回答，有的用声纹核验身份；克隆客户声音既无必要也不合规。

    考查：行业案例 · 认知层次：分析 · [回看 9.3](chapters/09-applications/index.md#93)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** 有了能直接听、直接说的语音大模型，专门的语音识别和语音合成模型已经没有用处了。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    批量转写、字幕、有声书、端侧设备、唤醒等场景仍然依靠专门的小模型，它们更快、更便宜、更容易控制。

    考查：语音大模型 · 认知层次：评价 · [回看 1.7](chapters/01-overview/index.md#17)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** 降噪总能提高语音识别的准确率。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    实验 2-4 中，5 dB 时降噪反而让字错率从 5% 升到 10%；只有 0 dB 左右时降噪明显有帮助，−5 dB 时也救不回来。

    考查：降噪的效果 · 认知层次：评价 · [回看实验 2-4](chapters/02-audio/index.md#2-4)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**3.** CTC 中的“空白”只表示静音，没有其他作用。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    空白还用来隔开两个相同的字，否则“谢谢”会被合并成“谢”。

    考查：CTC · 认知层次：理解 · [回看 3.5.2](chapters/03-asr-principles/index.md#352)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** 使用 Whisper 时，把语种设置成中文去识别英文录音，模型会自动发现并改用英文识别。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    实验 4-1 中，语种固定为中文的 Whisper tiny 识别英文录音输出了乱码。要告诉模型正确的语种，或者让它自动检测。

    考查：实验结果分析 · 认知层次：分析 · [回看实验 4-1](chapters/04-asr-practice/index.md#4-1)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**5.** 只要模型代码是开源的，就可以把它用在商业产品里。（　　）

</div>

??? tip "答案与解析"
    **答案：×**

    还要看训练数据的许可。本书的 Matcha 中文模型训练数据只允许非商业使用。

    考查：模型许可 · 认知层次：评价 · [回看本章实验](chapters/05-tts-principles/index.md#5-4)
    { .quiz-meta }

<div class="quiz" data-answer="B" data-type="tf" markdown>

**6.** 使用 sherpa-onnx 时，应该在循环里每合成一句话就重新建一次合成器。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：错误**

    建合成器要读入上百 MB 的模型，很慢，应该只建一次，在循环里只调用 `generate`。

    考查：sherpa-onnx 合成步骤 · 认知层次：应用 · [回看 6.3](chapters/06-tts-practice/index.md#63)
    { .quiz-meta }

<div class="quiz" data-answer="A" data-type="tf" markdown>

**7.** 等错误率越低，说明声纹模型把本人和冒充者分得越开。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：正确**

    等错误率是误接受率等于误拒绝率时的错误率，是比较声纹模型的常用指标。

    考查：等错误率 · 认知层次：理解 · [回看 7.3.2](chapters/07-speaker/index.md#732)
    { .quiz-meta }

<div class="quiz" data-answer="B" data-type="tf" markdown>

**8.** 用书里的虚拟授权人生成的声音发布到网上时，因为不是真人，可以不加 AI 标识。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：错误**

    标识办法要求所有生成合成内容都要标识，不得恶意删除标识，虚拟声音也不例外。

    考查：标识办法 · 认知层次：应用 · [回看 8.6.5](chapters/08-voice-cloning/index.md#865)
    { .quiz-meta }

<div class="quiz" data-answer="A" data-type="tf" markdown>

**9.** 实验 9-4 中，唤醒词模型量化成 int8 后，体积变小、速度变快，判断正确的段数没有变化。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：正确**

    12.5 MB 降到 4.8 MB，实时率 0.025 降到 0.020，都是 17/18 正确。

    考查：模型量化 · 认知层次：理解 · [回看 9.6.1](chapters/09-applications/index.md#961)
    { .quiz-meta }

<div class="quiz" data-answer="B" data-type="tf" markdown>

**10.** 有了语音大模型，传统的“识别 + 理解 + 合成”流水线已经完全没有用了。（　　）

- A. 正确
- B. 错误

</div>

??? tip "答案与解析"
    **答案：错误**

    流水线可控、可离线、回答来源可审核，在社区、医院、政务等场合仍然常用。

    考查：流水线与语音大模型 · 认知层次：评价 · [回看 9.2](chapters/09-applications/index.md#92)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 以“请到3号楼找王大夫，电话13912345678”为例，说明文本前端要做哪些处理，每一步的结果是什么。

??? tip "答案与解析"
    **参考答案**：① 文本正则化：“3号楼”→“三号楼”，“13912345678”→“幺三九幺二三四五六七八”；② 分词：请 / 到 / 三号 / 楼 / 找 / 王大夫 / ， / 电话 / ……；③ 注音：qing3 dao4 san1 hao4 lou2 zhao3 wang2 dai4 fu ……，其中“大夫”是多音字，要读 dài fu；④ 韵律：在逗号处加停顿（#3），句末加长停顿（#4）。

    考查：文本前端 · 认知层次：应用 · [回看 5.3](chapters/05-tts-principles/index.md#53)
    { .quiz-meta }

**2.** 请列出语音问答小助手的各个环节，并说明怎样把用户的等待时间缩短到 1 秒左右。

??? tip "答案与解析"
    **参考答案**：环节：唤醒 → VAD 等说完 → 识别 → 理解 → 回答 → 合成 → 播放。缩短等待时间的方法：VAD 静音等待取 0.3—0.5 秒；用流式识别边说边识别，说完时识别也基本完成；常见问题用关键词匹配，只把难题交给大模型，并让大模型流式输出；合成只合成第一小句就开始播放；模型尽量放在本地或近处服务器，减少网络传输；使用量化模型加快计算。

    考查：延迟优化 · 认知层次：应用 · [回看 9.1](chapters/09-applications/index.md#91)
    { .quiz-meta }

**五、实操题**（每题 10 分）

**1.** 把实验 4-2 改造成一个“录音转文字小工具”：给定任意一个 WAV 文件路径，自动 VAD 切句、逐句识别，输出同名的 `.srt` 字幕和 `.txt` 文字稿（每行一句，前面加上 `[开始秒]`）。用你自己录的一段 1 分钟左右的录音测试。

??? tip "答案与解析"
    **参考做法**：把实验 4-2 中切句和识别的部分写成一个函数，文件名作为参数：

    ```python
    def to_subtitles(wav_file):
        samples, sr = read_audio(wav_file)
        # ……这里放实验 4-2 第 1 步的 VAD 代码，得到 segments……
        srt, txt = [], []
        for k, (begin, seg) in enumerate(segments, 1):
            end = begin + len(seg) / sr
            text = transcribe(seg, sr)
            srt.append(f"{k}\n{srt_time(begin)} --> {srt_time(end)}\n{text}\n")
            txt.append(f"[{begin:.1f}] {text}")
        base = wav_file.rsplit(".", 1)[0]
        open(base + ".srt", "w", encoding="utf-8").write("\n".join(srt))
        open(base + ".txt", "w", encoding="utf-8").write("\n".join(txt))

    to_subtitles("my_talk.wav")      # 手机录音先转成 WAV
    ```

    注意每次调用都要新建一个 VAD（或调用 `vad.reset()`），否则上一个文件的内容会残留。自己的录音如果有较长的思考停顿，可以适当调大最短静音。

    考查：VAD 与字幕的综合应用 · 认知层次：应用 · [回看实验 4-2](chapters/04-asr-practice/index.md#4-2)
    { .quiz-meta }
