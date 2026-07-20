"""
05 - 嵌套循环（九九乘法表、图形打印、棋盘）
对应课程：第 34-35 集
生成时间: 2026-07-17
"""

# ===== 1. 打印长方形 =====
print("=== 1. 长方形 (5x3) ===")

m, n = 5, 3
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()

# ===== 2. 九九乘法表 =====
print("\n=== 2. 九九乘法表 ===")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i*j}", end="\t")
    print()

# ===== 3. 直角三角形 =====
print("\n=== 3. 直角三角星 ===")

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# ===== 4. 数字金字塔 =====
print("\n=== 4. 数字金字塔 ===")

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ===== 5. 国际象棋棋盘 =====
print("\n=== 5. 国际象棋棋盘 (8x8) ===")

n = 8
for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print("[]", end="")   # 黑格
        else:
            print("  ", end="")   # 白格（空格）
    print()

# ===== 6. 倒三角 =====
print("\n=== 6. 倒三角 ===")

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ===== 7. 登录系统（综合练习）=====
print("\n=== 7. 登录系统（break + continue）===")

# 模拟多次登录尝试（硬编码演示）
test_attempts = [
    ("", ""),                      # 空输入
    ("admin", "wrong"),            # 密码错误
    ("admin", "666888"),           # 登录成功
]

users = {
    "admin": "666888",
    "zhangsan": "123456",
    "taoge": "886666",
}

for username, password in test_attempts:
    # continue: 空输入跳过
    if username == "" or password == "":
        print(f"空输入 -> 请重新输入 (continue)")
        continue

    # break: 登录成功跳出
    if username in users and users[username] == password:
        print(f"{username} -> 登录成功！ (break)")
        break

    print(f"{username} -> 密码错误，重试...")
