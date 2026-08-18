"""
01 - 智能伴侣核心逻辑（会话记忆 + 流式输出）
对应课程：第 103-110 集
生成时间: 2026-08-13

说明：本文件展示 Streamlit 应用的核心逻辑片段，
完整项目是 ai_partner_3.py（运行方式：streamlit run xxx.py）
"""

import os
import streamlit as st
from openai import OpenAI

# ===== 1. 创建客户端 =====
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# ===== 2. 系统提示词（用 % 格式化动态注入昵称/性格）=====
def build_sys_prompt(nick_name, nature):
    """构建系统提示词"""
    sys_prompt = """
你叫%s,现在是用户的真实伴侣,请完全代入伴侣角色。
规则:
1.每次只回1条消息
2.禁止任何场景或状态描述性文字
3.匹配用户的语言
4.回复简短,像微信聊天一样
5.有需要的话可以用😜🥰😝等emoji表情
6.用符合伴侣性格的方式对话

伴侣性格:
-%s
你必须严格遵守上述规则来回复用户。
"""
    return sys_prompt % (nick_name, nature)

# ===== 3. 会话记忆 =====
def init_session():
    """初始化会话状态（key 必须一致！）"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "nick_name" not in st.session_state:
        st.session_state.nick_name = "小兰"
    if "nature" not in st.session_state:
        st.session_state.nature = "含蓄内敛的南方姑娘"

def display_history():
    """展示历史消息"""
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

def build_history_for_api():
    """把 session_state 的 messages 转成 API 识别的格式"""
    history = []
    for msg in st.session_state.messages:
        # 存储用 "ai"，API 要求 "assistant"，三目转换
        role = "assistant" if msg["role"] == "ai" else msg["role"]
        history.append({"role": role, "content": msg["content"]})
    return history

# ===== 4. 流式输出（含存储）=====
def stream_chat(prompt):
    """调用 API 并流式输出，最后把回复存回历史"""
    # 记录用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 API（展开 history）
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": build_sys_prompt(
                st.session_state.nick_name, st.session_state.nature)},
            *build_history_for_api(),
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 流式输出容器
    response_msg = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_msg.chat_message("ai").write(full_response)

    # ⚠️ 关键：流式结束后存回历史
    st.session_state.messages.append({"role": "ai", "content": full_response})

    return full_response


# ===== 5. 侧边栏个性化 =====
def render_sidebar():
    """侧边栏：昵称/性格设置"""
    with st.sidebar:
        nick_name = st.text_input("昵称", placeholder="请输入昵称",
                                  value=st.session_state.nick_name)
        if nick_name:
            st.session_state.nick_name = nick_name

        nature = st.text_input("性格", placeholder="请定义性格",
                               value=st.session_state.nature)
        if nature:
            st.session_state.nature = nature


# ===== 主流程（实际运行时取消注释）=====
if __name__ == "__main__":
    st.set_page_config(page_title="AI智能伴侣", page_icon="🤖", layout="wide")
    st.title("AI智能伴侣")

    init_session()
    render_sidebar()
    display_history()

    prompt = st.chat_input("请输入您想询问的问题~")
    if prompt:
        st.chat_message('user').write(prompt)
        stream_chat(prompt)
