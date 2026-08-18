"""
01 - 文件操作示例（读/写/追加/with语句/JSON）
对应课程：第 111 集
生成时间: 2026-08-13
"""

import json

# ===== 1. 读文件（三步走）=====
print("=== 1. 读文件 ===")

# 方式1：手动 open + close
f = open("./resources/古诗.txt", "r", encoding="utf-8")
content = f.read()           # 读取所有内容
print(f"read() 读出的内容:\n{content}")
f.close()

# 方式2：readlines 按行读 + 遍历
f = open("./resources/古诗.txt", "r", encoding="utf-8")
for line in f.readlines():
    print(f"行: {line.strip()}")   # strip 去换行
f.close()

# ===== 2. 写文件（覆盖模式 "w"）=====
print("\n=== 2. 写文件 (w 覆盖) ===")

with open("./resources/静夜诗.txt", "w", encoding="utf-8") as f:
    f.write("静夜诗(李白)\n\n")     # 注意：write 不会自动换行，要手动加 \n
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
print("已写入 静夜诗.txt")

# ===== 3. 追加模式 "a" =====
print("\n=== 3. 追加 (a) ===")

with open("./resources/静夜诗.txt", "a", encoding="utf-8") as f:
    f.write("\n—— 李白 追加的一行\n")
print("已追加内容")

# 验证追加结果
with open("./resources/静夜诗.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ===== 4. with 语句（推荐）=====
print("\n=== 4. with 语句 ===")

# with 自动关闭文件，无需手动 close
with open("./resources/古诗.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"with 读取的内容长度: {len(content)} 字符")
print("with 块结束，文件已自动关闭")

# ===== 5. JSON 文件操作（智能伴侣持久化准备）=====
print("\n=== 5. JSON 持久化 ===")

# 模拟对话历史
messages = [
    {"role": "user", "content": "你好"},
    {"role": "ai", "content": "你好呀，今天过得怎么样？"},
    {"role": "user", "content": "陪我聊聊天吧"},
]

# 保存到 JSON 文件
with open("./resources/history.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)
print("已保存 history.json")

# 读取 JSON 文件
with open("./resources/history.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"读回的历史（{len(loaded)} 条消息）:")
for msg in loaded:
    print(f"  {msg['role']}: {msg['content']}")

# ===== 6. 文件打开模式速查 =====
print("\n=== 6. 打开模式 ===")
modes = [
    ("r", "只读", "文件不存在报错"),
    ("w", "只写(覆盖)", "不存在自动创建"),
    ("a", "追加", "不存在自动创建"),
    ("r+", "读写", "文件不存在报错"),
    ("w+", "读写(覆盖)", "不存在自动创建"),
    ("a+", "读写(追加)", "不存在自动创建"),
]
for mode, desc, note in modes:
    print(f"  {mode:<3} {desc:<10} {note}")

print("\n✅ 示例运行完毕。提示：读不存在的文件会报 FileNotFoundError")
