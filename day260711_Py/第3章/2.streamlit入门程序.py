import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit 入门",
    page_icon="💪",
    # 页面布局
    layout="wide",
    # 控制侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={}
)

st.title("这里是一级标题")
st.header("这里是二级标题")
st.subheader("这是三级标题")

#运行的话要在终端输入 streamlit run xxx.py

# 添加图片
st.image("./resources/Yidao.jpg")

# 添加音频
st.audio("./resources/陈粒 - 虚拟.mp3")

# 添加视频
st.video("./resources/羔 子 - Aruarian Dance（8bit）.mp4")

# 设置logo
st.logo("./resources/logo.png", size="large")

# 设置表格
student_data = {
    "姓名":["王林","李慕婉","贝罗","莫厉海","石萧"],
    "学号":["20260001","20260002","20260003","20260004","20260005"],
    "语文":[98,90,59,29,80],
    "数学":[88,78,65,70,39],
    "英语":[99,89,87,59,62],
    "总分":[285,257,211,158,181]
}

st.table(student_data)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为:{name}")

# 密码输入框
password = st.text_input("请输入密码", type="password")
st.write(f"您输入的密码为:{password}")

# 单选按钮
gender = st.radio("请输入您的性别", ["男", "女", "未知"], index=2)
st.write(f"您的性别为:{gender}")