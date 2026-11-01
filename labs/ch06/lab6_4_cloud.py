"""实验 6-4 云平台合成接口（待实测）：用阿里云百炼的 CosyVoice 合成同一段文字，并用 SSML 控制停顿、语速和多音字。

编者说明：本实验需要注册阿里云账号、开通百炼服务、创建 API Key，并能联网；编者的写作环境不能访问该服务，
代码按阿里云官方文档（2026 年 11 月查阅）编写，**待实测**。接口和音色名称经常更新，运行前请对照附录 A 和官方文档。
安装：pip install -U dashscope
运行前设置环境变量（不要把 Key 写进代码）：
    Windows:  set DASHSCOPE_API_KEY=你的Key
    macOS/Linux:  export DASHSCOPE_API_KEY=你的Key
"""
import os

import dashscope

client = dashscope.Client(
    api_key=os.environ["DASHSCOPE_API_KEY"],         # 从环境变量读取 Key
    workspace=os.environ.get("DASHSCOPE_WORKSPACE"),  # 业务空间 ID，在百炼控制台查看  ← 改这里
    region="cn-beijing",                              # 中国内地（北京）地域；以官方文档为准
)
MODEL, VOICE = "cosyvoice-v3-flash", "longanyang"     # ← 改这里：模型和音色见官方“音色列表”

# 1. 普通文字
text = "各位居民请注意，下周六上午九点，社区在中心广场组织消防演练，欢迎大家参加。"
audio = client.audio.tts.synthesize(text, model=MODEL, voice=VOICE)
open("cloud_plain.mp3", "wb").write(audio)

# 2. SSML：语速加快一点、指定停顿、指定多音字读音、电话号码逐位读
ssml = ('<speak rate="1.1">各位居民请注意，<break time="500ms"/>'
        '请到<phoneme alphabet="py" ph="yin2 hang2">银行</phoneme>门口集合，'
        '咨询电话<say-as interpret-as="telephone">12345</say-as>。</speak>')
audio = client.audio.tts.synthesize(ssml, model=MODEL, voice=VOICE, enable_ssml=True)
open("cloud_ssml.mp3", "wb").write(audio)
print("已保存 cloud_plain.mp3 和 cloud_ssml.mp3，请和实验 6-1 的本地模型对比")
