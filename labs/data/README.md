# 实验数据说明

| 文件夹 | 内容 | 用在 | 来源与许可 |
|---|---|---|---|
| `fsdd/` | 英文数字 0–9 录音 400 段（4 位说话人 × 10 个数字 × 每个 10 遍，8 kHz） | 第 3 章 | Free Spoken Digit Dataset 的子集（george、jackson、lucas、nicolas 四人前 10 遍），CC BY-SA 4.0，<https://github.com/Jakobovski/free-spoken-digit-dataset> |
| `corpus/community.txt` | 47 句社区通知和服务用语（约 1200 字），训练第 3 章的二元语言模型 | 第 3 章 | 编者编写 |
| `sounds/` | 元音“啊、衣、乌”、口哨、噪声、敲门声、一段 44.1 kHz 讲话 | 第 2 章 | 编者生成：元音用“声源—滤波器”方法按共振峰合成，讲话用 Kokoro 合成，口哨、噪声、敲门声用 numpy 生成 |
| `calls/` | 8 段“居民来电”，故意做成格式不统一（双声道、8 kHz、声音太小、削波、带噪声、长静音），`calls.csv` 是标准文字 | 第 2、4 章 | 编者用 Kokoro 合成后加工 |
| `meeting/` | 一段约 52 秒的三人议事会录音，`meeting_truth.csv` 是每句话的起止时间、发言人和文字 | 第 4、7 章 | 编者用 Kokoro 三种音色合成 |
| `kws/` | 唤醒词测试录音 18 段（6 句话 × 3 种音色），`kws.csv` 标明是否含“你好小站 / 小站小站” | 第 4 章 | 编者用 Kokoro 合成 |
| `voices/` | 4 位“虚拟授权人”A、B、C、D 各 3 段录音，加一段身份未知的录音 `unknown.wav`，`voices.csv` 是文字 | 第 7、8 章 | 编者用 Kokoro 内置音色合成，不是真人录音 |

- **书中所有“居民”“志愿者”的声音都是合成的。** Kokoro 模型（Apache-2.0）的内置音色不对应任何公众人物。第 8 章把它们当作“虚拟授权人”练习语音克隆；克隆真人的声音必须先取得本人的书面授权，见第 8 章和附录 D 的授权书模板。
- 重新生成：在 `labs` 文件夹里运行 `python data/make_audio.py`（要先 `python models.py kokoro`）。合成结果和编者的文件可能有细微差别，正文的运行结果以仓库里的文件为准。
- 模型不放在仓库里，用 `python models.py` 下载到 `labs/models/`，见附录 B。
