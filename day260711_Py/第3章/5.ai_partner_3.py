import os

import streamlit as st
from openai import OpenAI

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 是环境变量的名字,值就是deepseek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 设置大模型系统提示词
sys_prompt = """
你叫%s,现在是用户的真实伴侣,请完全代入伴侣角色。 
    规则:
    1.每次只回1条消息
    2.禁止任何场景或状态描述性文字
    3.匹配用户的语言
    4.回复简短,像微信聊天一样
    5.有需要的话可以用😜🥰😝等emoji表情
    6.用符合伴侣性格的方式对话
    7.回复的内容,要充分体现伴侣的性格特征
    伴侣性格:
    -%s
    你必须严格遵守上述规则来回复用户。
"""


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

# 初始化昵称,性格
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小兰"
if "nature" not in st.session_state:
    st.session_state.nature = "含蓄内敛的南方姑娘"

# 需要在每次对话的时候展示聊天信息
for message in st.session_state.messages: # ["role": user/ai, "content":prompt]
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("ai").write(message["content"])

    # 简化一下,既然st.chat_message需要的参数和判断的role一样,那么就可以直接输入message的key,即"role"
    st.chat_message(message["role"]).write(message["content"])

# 设置侧边栏
with st.sidebar:
    # 昵称输入框,并设置默认值
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    # 性格输入框,并设置默认值
    nature = st.text_input("性格", placeholder="请定义性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# 设置用户输入
prompt = st.chat_input("请输入您想询问的问题~")

# 信息展示
if prompt:
    st.chat_message(name='user').write(prompt)
    # 控制台记录一下用户输入
    print("--------->用户输入：",prompt)

    # 记录用户输入
    st.session_state.messages.append({"role":"user", "content":prompt})

    # 设置会话历史
    history = []
    # 因为接口要求role = assistant,所以需要把ai转成assistant
    for msg in st.session_state.messages:
        # 三目运算,若role = ai 则赋值assistant 否则是user
        role = "assistant" if msg["role"] == "ai" else msg["role"]
        #添加回history
        history.append({"role":role, "content":msg["content"]})

    # 控制台输出看一下情况
    print("-=-=-=-=-=-",history)

    #调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": sys_prompt % (st.session_state.nick_name, st.session_state.nature)},  # 字符串格式化
            # 解包history列表,包含前面会话内容而且和deepseek接口要求一样
            *history,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 大模型回答展示(非流式输出)
    #st.chat_message(name='ai').write(response.choices[0].message.content)

    # 设置流式输出容器
    response_msg = st.empty()  # 用于展示大模型返回结果

    # 大模型回答展示(使用流式输出)
    full_response = ""  # 每次流式输出收集的信息
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            # 把上面收集到的信息利用response_msg写出来
            response_msg.chat_message("ai").write(full_response)


    # 记录大模型回答
    st.session_state.messages.append({"role":"ai", "content":full_response})
