import os

import streamlit as st
from openai import OpenAI

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 是环境变量的名字,值就是deepseek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 设置大模型系统提示词
sys_prompt = "你是一个非常专业的AI助理，叫小兰，每次回答的时候都用甜美的语调"

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 页面布局
    layout="wide",
    # 控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 设置大标题
st.title("AI智能伴侣")

# 设置log
st.logo("./resources/logo.png")

# 初始化对话信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 需要在每次对话的时候展示聊天信息
for message in st.session_state.messages: # ["role": user/ai, "content":prompt]
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("ai").write(message["content"])

    # 简化一下,既然st.chat_message需要的参数和判断的role一样,那么就可以直接输入message的key,即"role"
    st.chat_message(message["role"]).write(message["content"])
    
# 设置用户输入
prompt = st.chat_input("请输入您想询问的问题~")

# 信息展示
if prompt:
    st.chat_message(name='user').write(prompt)
    # 控制台记录一下用户输入
    print("--------->用户输入：",prompt)

    # 记录用户输入
    st.session_state.messages.append({"role":"user", "content":prompt})

    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 大模型返回
    print("<-----------大模型回答：",response.choices[0].message.content)

    # 大模型回答展示
    st.chat_message(name='ai').write(response.choices[0].message.content)

    # 记录大模型回答
    st.session_state.messages.append({"role":"ai", "content":response.choices[0].message.content})
