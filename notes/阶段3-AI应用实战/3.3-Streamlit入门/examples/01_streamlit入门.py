"""
01 - Streamlit 入门示例
对应课程：第 101-102 集
生成时间: 2026-08-13
运行方式: streamlit run 01_streamlit入门.py
"""

import streamlit as st

# 页面配置（必须是第一个 Streamlit 命令）
st.set_page_config(
    page_title="Streamlit 入门",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# ===== 1. 文本元素 =====
st.title("这里是一级标题")
st.header("这里是二级标题")
st.subheader("这是三级标题")

# ===== 2. 数据元素 =====
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)

# ===== 3. 表单控件 =====
st.subheader("表单控件演示")

# 普通输入框
name = st.text_input("请输入姓名")
if name:
    st.write(f"您输入的姓名为: {name}")

# 密码输入框
password = st.text_input("请输入密码", type="password")
if password:
    st.write(f"您输入的密码为: {password}")

# 单选按钮
gender = st.radio("请输入您的性别", ["男", "女", "未知"], index=2)
st.write(f"您的性别为: {gender}")

# 下拉选择框
city = st.selectbox("请选择城市", ["北京", "上海", "广州", "深圳"])
st.write(f"您选择的城市为: {city}")

# 按钮
if st.button("点击我"):
    st.write("按钮被点击了！🎉")

# 滑块
age = st.slider("选择年龄", 0, 100, 25)
st.write(f"您的年龄为: {age}")

# ===== 4. 侧边栏 =====
with st.sidebar:
    st.header("侧边栏设置")
    st.write("这里可以放一些配置项")

# ===== 5. session_state 演示 =====
st.subheader("session_state 演示")

# 普通变量：每次重跑都是新值
normal_count = 0

# session_state：跨重跑保留
if "st_count" not in st.session_state:
    st.session_state.st_count = 0
st.session_state.st_count += 1

st.write(f"普通变量 count = {normal_count}（每次重跑归零）")
st.write(f"session_state count = {st.session_state.st_count}（跨重跑累加）")

st.info("💡 每次交互（点击按钮/输入文字），整个脚本会重跑一遍。普通变量不保留，session_state 才保留。")
