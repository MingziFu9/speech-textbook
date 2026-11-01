"""实验 9-2 做成网页：用 Gradio 把转写、合成和问答小助手做成三个标签页，在浏览器里直接录音、上传、播放。

运行：在 labs/ch09 文件夹里  python lab9_2_web.py   然后用浏览器打开命令行里显示的地址（一般是 http://127.0.0.1:7860）
需要：pip install gradio；模型 python models.py sensevoice matcha-zh kokoro
"""
import sys

import gradio as gr
import numpy as np

sys.path.append("..")
from assistant import ask
from voicelab import speak, transcribe


def to_float(audio):
    """Gradio 给的录音是 (采样率, 整数数组)，可能是双声道，转成单声道小数"""
    sr, data = audio
    data = data.astype(np.float32) / (32768 if data.dtype == np.int16 else 1)
    return (data.mean(axis=1) if data.ndim == 2 else data), sr


def do_transcribe(audio):
    if audio is None:
        return "请先录音或上传一个音频文件"
    data, sr = to_float(audio)
    return transcribe(data, sr)


def do_speak(text, voice, speed):
    model, sid = {"Matcha 女声（快）": ("matcha-zh", 0), "Kokoro 女声": ("kokoro", 20),
                  "Kokoro 男声": ("kokoro", 58)}[voice]
    audio, sr = speak(text, model=model, sid=sid, speed=speed)
    return (sr, audio), "提示：本音频由人工智能语音合成"


def do_ask(audio):
    if audio is None:
        return "请先录音", "", None
    data, sr = to_float(audio)
    r = ask(data, sr)
    cost = "，".join(f"{k} {v:.2f} 秒" for k, v in r["time"].items())
    return r["heard"], f"{r['reply']}\n\n（耗时：{cost}）", (r["sr"], r["audio"])


with gr.Blocks(title="社区语音服务站") as demo:
    gr.Markdown("# 社区语音服务站\n本页面的语音由人工智能合成；录音只在本机处理，不会上传或保存。")
    with gr.Tab("语音转文字"):
        mic = gr.Audio(sources=["microphone", "upload"], type="numpy", label="录音或上传")
        out = gr.Textbox(label="识别结果")
        gr.Button("开始识别", variant="primary").click(do_transcribe, mic, out)
    with gr.Tab("文字转语音"):
        text = gr.Textbox(label="要朗读的文字", value="各位居民请注意，下周六上午九点，社区组织消防演练。")
        voice = gr.Radio(["Matcha 女声（快）", "Kokoro 女声", "Kokoro 男声"], value="Matcha 女声（快）", label="声音")
        speed = gr.Slider(0.6, 1.6, value=1.0, step=0.1, label="语速")
        player = gr.Audio(label="合成结果")
        note = gr.Markdown()
        gr.Button("开始合成", variant="primary").click(do_speak, [text, voice, speed], [player, note])
    with gr.Tab("问答小助手"):
        q = gr.Audio(sources=["microphone", "upload"], type="numpy", label="问一个社区的问题")
        heard = gr.Textbox(label="我听到的是")
        reply = gr.Textbox(label="回答")
        reply_audio = gr.Audio(label="语音回答", autoplay=True)
        gr.Button("提问", variant="primary").click(do_ask, q, [heard, reply, reply_audio])

if __name__ == "__main__":
    demo.launch()                                                  # 加 share=True 可以生成临时公网链接（会经过外部服务器，注意隐私）
