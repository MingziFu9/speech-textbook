# TTS、SST 与语音克隆的理论与应用

**面向成人教育人工智能技术应用专业（专科）的《课程名称》教材**

<!-- 书名、课程信息框和“目录与实验”表由 python tools/course.py sync 根据 course.yml 生成；全书概览表由 python tools/book_stats.py 生成 -->

<!-- course:start -->
!!! abstract "课程信息"
    4 学分 · 72 学时（理论 36 学时 + 实验 36 学时） · 第 4 学期 · 9 章 · 36 个实验 · 期末开卷
<!-- course:end -->

## 这本书讲什么

两三段话：这门课研究什么、学生身边哪里用得到、全书从哪里讲到哪里。

## 本书的特点

- **通俗易懂**：用生活中的例子和“算一算”小计算讲清原理，公式只保留最必要的部分；
- **每章动手实验**：★ 为基础实验，☆ 为拓展实验，教师可按课时选做，其余作为课后练习；
- **结果真实**：书中的运行结果都是编者实际运行得到的；编写环境无法运行的部分标为“待实测”，并提供记录表；
- **在线练习**：每章课后的单选、多选和判断题可以在网页上直接作答，并查看解析；
- **贴近岗位**：实验按智能客服、会议转写、有声书、语音助手等岗位任务设计，本课程不对应职业证书。

## 全书概览

<!-- stats:start -->

| 章 | 正文字数 | 实验 | 课后练习<br>（可在线作答） | 术语 | 参考文献 | 交互动画 |
|---|---|---|---|---|---|---|
| [第 1 章](chapters/01-overview/index.md) | 0.8 万 | 4 | 20（16） | 9 | 8 | 1 |
| [第 2 章](chapters/02-audio/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 3 章](chapters/03-asr-principles/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 4 章](chapters/04-asr-practice/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 5 章](chapters/05-tts-principles/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 6 章](chapters/06-tts-practice/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 7 章](chapters/07-speaker/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 8 章](chapters/08-voice-cloning/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| [第 9 章](chapters/09-applications/index.md) | 0.1 万 | 4 | 5（3） | 0 | 1 | 0 |
| **合计** | **1.4 万** | **36** | **60（40）** | **9** | **16** | **1** |

正文字数只统计汉字，不含代码和课后练习；单选、多选和判断题可以在网页上直接作答。配套学习资源：[交互动画](sims/index.md) 1 个 · [学习图谱](learning-graph/index.md) 2 个概念 · [常见问题](faq/index.md) 2 问 · [术语表](appendix/glossary.md) 9 条。

<!-- stats:end -->

## 目录与实验

<!-- toc:start -->
| 章节 | 实验 |
|---|---|
| [第 1 章 走进语音技术](chapters/01-overview/index.md) | 实验 1-1 ★ 让电脑说第一句话<br>实验 1-2 ★ 让电脑听写<br>实验 1-3 ★ 一来一回<br>实验 1-4 ☆ 在自己的电脑上安装环境 |
| [第 2 章 声音的数字化与音频处理](chapters/02-audio/index.md) | 实验 2-1 ★ 看见声音<br>实验 2-2 ★ 采样率听一听<br>实验 2-3 ★ 整理居民来电<br>实验 2-4 ☆ 梅尔频谱、MFCC 与降噪 { #2-4 } |
| [第 3 章 语音识别原理：从模板匹配到深度学习](chapters/03-asr-principles/index.md) | 实验 3-1 ★ 模板匹配认数字<br>实验 3-2 ★ HMM 数字识别器 { #3-2 }<br>实验 3-3 ★ 算一算字错率<br>实验 3-4 ☆ 语言模型来纠错 |
| [第 4 章 语音识别实战：转写、字幕与唤醒](chapters/04-asr-practice/index.md) | 实验 4-1 ★ 三个模型比一比<br>实验 4-2 ★ 议事会录音做字幕<br>实验 4-3 ★ 自定义唤醒词<br>实验 4-4 ☆ 噪声和热词 |
| [第 5 章 语音合成原理：从文字到声音](chapters/05-tts-principles/index.md) | 实验 5-1 ★ 做一个文本前端<br>实验 5-2 ★ 拼接合成听“机器腔”<br>实验 5-3 ★ 拆开看声学模型和声码器<br>实验 5-4 ☆ 给合成打分 |
| [第 6 章 语音合成实战：多音色与有声书](chapters/06-tts-practice/index.md) | 实验 6-1 ★ 一个模型多种声音<br>实验 6-2 ★ 中英混读<br>实验 6-3 ★ 社区有声广播<br>实验 6-4 ☆ 云平台合成接口（待实测） |
| [第 7 章 声纹识别与语音转换](chapters/07-speaker/index.md) | 实验 7-1 ★ 声纹比一比<br>实验 7-2 ★ 声纹登录<br>实验 7-3 ★ 谁在说话<br>实验 7-4 ☆ 语音转换体验（待实测） |
| [第 8 章 语音克隆：技术、伦理与授权](chapters/08-voice-cloning/index.md) | 实验 8-1 ★ 签授权书，录参考音<br>实验 8-2 ★ 零样本克隆<br>实验 8-3 ★ 克隆像不像，并贴上标签<br>实验 8-4 ☆ 微调式克隆（待实测） |
| [第 9 章 语音交互应用与综合项目](chapters/09-applications/index.md) | 实验 9-1 ★ 语音问答小助手<br>实验 9-2 ★ 做成网页<br>实验 9-3 ★ 综合项目<br>实验 9-4 ☆ 测一测快不快 |

附录：[A sherpa-onnx 与音频处理速查](appendix/a-libraries.md) · [B 实验环境、模型与数据说明](appendix/b-environment.md) · [C 术语表](appendix/glossary.md) · [D 实验报告、声音授权书与项目模板](appendix/d-templates.md)
<!-- toc:end -->

## 配套资源

- [交互动画](sims/index.md)、[学习图谱](learning-graph/index.md)、[常见问题](faq/index.md)
- 实验代码与数据：仓库中的 `labs/` 目录
- 课件、教案和 Word/PDF 版教材：见仓库的 Releases 页面
