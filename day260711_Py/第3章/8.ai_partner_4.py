import json
import os
from datetime import datetime

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

# 定义保存会话函数
def save_session():
    # 构建会话对象
    session_data = {
        "nick_name": st.session_state.nick_name,
        "nature": st.session_state.nature,
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages,
    }

    # 创建sessions文件夹,用于保存会话信息
    if not os.path.exists('./resources/sessions'):
        os.mkdir('./resources/sessions')

    # 保存会话信息
    with open(f'./resources/sessions/{st.session_state.current_session}.json', 'w', encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

# 定义会话标识生成函数
def load_current_session():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 加载所有会话列表信息
def load_sessions():
    session_data = []
    # sessions会话信息文件存在才加载
    if os.path.exists('./resources/sessions'):
        files = os.listdir('./resources/sessions')  # 按list收集所有文件信息
        for file in files:
            if file.endswith(".json"):
                session_data.append(file[:-5])
    # 倒序输出
    # session_data.sort(reverse=True)
    # return session_data
    #切片反转
    return session_data[::-1]

# 加载指定会话信息
def load_session(session_name):
    try:
        # 先判断会话文件是否存在
        if os.path.exists(f'./resources/sessions/{session_name}.json'):
            # 读取会话文件
            with open(f'./resources/sessions/{session_name}.json', 'r', encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
                st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("会话加载失败!")

# 删除会话信息
def delete_session(session_name):
    try:
        # 先判断会话文件是否存在
        if os.path.exists(f'./resources/sessions/{session_name}.json'):
            os.remove(f'./resources/sessions/{session_name}.json')  # 删除文件

            # 如果删除的是当前会话,则需要清除消息列表
            if st.session_state.current_session == session_name:
                st.session_state.messages = []
                st.session_state.current_session = load_current_session()
    except Exception:
        st.error("删除会话失败!")

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

# 设置会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = load_current_session()

# 展示会话名称
st.text(f"当前会话信息:{st.session_state.current_session}")

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

    # 设置侧边栏标题
    st.header("AI控制面板")

    # 设置新建会话按钮
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 1.保存会话信息
        save_session()

        # 2.创建新会话,需要考虑当前会话信息是否存在,不存在不继续创建
        if st.session_state.messages:
            st.session_state.messages = []  # 重置一下会话信息
            st.session_state.current_session = load_current_session()   # 会话标识
            save_session()
            st.rerun()  # 重新运行当前页面

    # 会话历史
    st.text("会话历史")

    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1]) # st.columns把一行的内容按输入比例分配
        with col1:
            # 加载会话信息
            if st.button(session, icon="📝", key=f"load_{session}", type="primary" if st.session_state.current_session == session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            # 删除会话信息-按钮
            if st.button("", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 设置分割线
    st.divider()

    # 伴侣信息
    st.subheader("伴侣信息")

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

    # 大模型每次回答都要保存信息
    save_session()