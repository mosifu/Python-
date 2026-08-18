# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 是环境变量的名字,值就是deepseek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 与AI大模型进行交互(参数)
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": "你是一个非常专业的AI助理，叫小兰，每次回答的时候都用甜美的语调"},
        {"role": "user", "content": "你是谁，你能帮我做什么"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出返回的结果
print(response.choices[0].message.content)