"""实验 9-1 选做：把“理解”这一步换成国产大模型（待实测）。

编者说明：需要注册阿里云百炼并创建 API Key，联网使用，按调用量计费。编者的写作环境不能访问该服务，
代码按阿里云百炼“OpenAI 兼容接口”的官方说明编写，**待实测**；模型名称请以官方文档为准。
安装：pip install -U openai      设置环境变量 DASHSCOPE_API_KEY（见第 6 章实验 6-4）
用法：在 assistant.py 里把 understand 的结果为空时，改成调用 llm_answer(heard)
"""
import os

from openai import OpenAI

from assistant import FAQ

client = OpenAI(api_key=os.environ["DASHSCOPE_API_KEY"],
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
SYSTEM = ("你是幸福里社区的语音助手，回答要简短（不超过 60 个字），口语化，适合朗读。"
          "只根据下面的社区信息回答；信息里没有的，就说“这个问题请咨询社区工作人员”，不要编造。\n"
          + "\n".join(f"- {item['回答']}" for item in FAQ))


def llm_answer(question, model="qwen-plus"):                    # ← 改这里：换成官方文档里的模型名
    resp = client.chat.completions.create(model=model, messages=[
        {"role": "system", "content": SYSTEM}, {"role": "user", "content": question}])
    return resp.choices[0].message.content


if __name__ == "__main__":
    print(llm_answer("暖气片漏水了找谁修？"))
