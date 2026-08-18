"""
03 - while 循环（while / while-else / break / continue）
对应课程：第 28-30 集
生成时间: 2026-07-17
"""

# ===== 1. 基本 while =====
print("=== 1. 基本 while ===")

i = 0
while i < 10:
    i += 1
    print(f"第{i}遍：人生苦短，我用Python！")

# ===== 2. while...else =====
print("\n=== 2. while...else ===")

# 正常结束 — else 会执行
count = 0
while count < 3:
    count += 1
    print(f"正常循环: count={count}")
else:
    print("循环正常结束（else 执行）")

# break 跳出 — else 不执行
count = 0
while True:
    count += 1
    print(f"break 循环: count={count}")
    if count >= 3:
        break
else:
    print("这行永远不会执行")

print("break 跳出后继续...")

# ===== 3. 实战：1-100 偶数和 =====
print("\n=== 3. 1-100 偶数和 ===")

i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1-100 偶数和: {total}")

# ===== 4. 实战：登录系统（while True + break + continue）=====
print("\n=== 4. 登录系统演示 ===")

# 用硬编码模拟交互
test_users = [
    ("", ""),           # 空输入 → continue
    ("admin", "wrong"), # 错误密码 → 重试
    ("admin", "666888"),# 正确 → break
]

for username, pwd in test_users:
    if username == "" or pwd == "":
        print(f"'{username}'/'{pwd}' → 不能为空！(continue)")
        continue

    if username == "admin" and pwd == "666888":
        print(f"'{username}'/'{pwd}' → 登录成功！(break)")
        break

    print(f"'{username}'/'{pwd}' → 密码错误，重试...")
