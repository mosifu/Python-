# 每日练习 - 2026-08-13
# 主题：Streamlit 入门 + 智能伴侣项目 + 文件操作（第101-111集）
# 说明：纯注释练习文件，请在每题的"我的回答"后填写

# ============================================================
# 第一部分：巩固练习
# ============================================================

# -------- 练习 1：Streamlit session_state 机制 --------
#
# 涉及知识点：st.session_state、脚本重跑机制
#
# 题目描述：
#   解释为什么 Streamlit 里普通变量 count 每次交互都会归零，
#   而 st.session_state.count 能跨重跑累加？
#
# 提示：回忆"每次交互整个脚本从头重跑一遍"的机制
#
# 我的回答：


# -------- 练习 2：会话记忆 key 陷阱 --------
#
# 涉及知识点：session_state key 一致性
#
# 题目描述：
#   下面这段代码有个 bug，会导致聊天历史每次重跑都丢失，
#   请指出问题在哪一行，并写出正确写法。
#
#   if "message" not in st.session_state:
#       st.session_state.messages = []
#
#   st.session_state.messages.append({"role": "user", "content": prompt})
#
# 我的回答：


# -------- 练习 3：流式输出完整闭环 --------
#
# 涉及知识点：流式输出、full_response 拼接、会话记忆
#
# 题目描述：
#   补全下面的流式输出代码，让 AI 回复能正确存入历史。
#   （在正确位置补上存历史的一行）
#
#   response = client.chat.completions.create(..., stream=True)
#   response_msg = st.empty()
#   full_response = ""
#   for chunk in response:
#       if chunk.choices[0].delta.content is not None:
#           full_response += chunk.choices[0].delta.content
#           response_msg.chat_message("ai").write(full_response)
#   # 这里应该补什么？为什么？
#
# 我的回答：


# -------- 练习 4：文件读写模式 --------
#
# 涉及知识点：open 模式 r/w/a、write 换行、编码
#
# 题目描述：
#   1. "w" 和 "a" 模式的区别是什么？
#   2. 下面这段代码会怎样？为什么？
#      f = open("笔记.txt", "w", encoding="utf-8")
#      f.write("第一行")   # 没有 \n
#      f.write("第二行")
#      f.close()
#   3. 用 with 语句重写上面代码
#
# 我的回答：


# -------- 练习 5：JSON 持久化 --------
#
# 涉及知识点：json.dump / json.load、智能伴侣会话保存
#
# 题目描述：
#   写代码：把 st.session_state.messages 保存到 history.json，
#   下次启动时读回恢复。（提示：json.dump + ensure_ascii=False + indent=2）
#
# 我的回答：


# ============================================================
# 第二部分：自测题（共 5 题）
# ============================================================

# ---------- 第 1 题 ----------
# Streamlit 中，跨重跑保存数据的唯一方式是什么？
# A. 全局变量  B. st.session_state  C. 局部变量  D. 文件变量
#
# 我的回答：


# ---------- 第 2 题 ----------
# 下面哪个 session_state key 的用法会导致历史每次重跑丢失？
# A. if "messages" not in ...: st.session_state.messages = []
# B. if "message" not in ...: st.session_state.messages = []
# C. if "messages" not in ...: st.session_state.messages = []
# D. 以上都不会丢
#
# 我的回答：


# ---------- 第 3 题 ----------
# 流式输出后，为什么必须把 full_response 存回 st.session_state.messages？
# A. 不存会报错  B. 不存AI下次对话就"失忆"  C. 不存无法显示  D. 必须存才能结束
#
# 我的回答：


# ---------- 第 4 题 ----------
# 用 "w" 模式打开一个已存在的文件并写入，会发生什么？
# A. 追加到末尾  B. 报错  C. 清空原有内容后写入  D. 无法写入
#
# 我的回答：


# ---------- 第 5 题 ----------
# Windows 下读写中文文件，不写 encoding="utf-8" 可能遇到什么问题？
# A. 正常运行  B. 乱码或编码错误  C. 文件自动删除  D. 只能读不能写
#
# 我的回答：


# ============================================================
# 自测答案（写完后对照检查）
# ============================================================
# 第1题：B
# 第2题：B（"message" 和 "messages" 不一致）
# 第3题：B（AI 无状态，记忆靠客户端保存历史）
# 第4题：C（"w" 覆盖写入）
# 第5题：B（中文编码问题）
# ============================================================
