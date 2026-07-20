"""
04 - for 循环 & range()
对应课程：第 31-33 集
生成时间: 2026-07-17
"""

# ===== 1. for 遍历字符串 =====
print("=== 1. for 遍历字符串 ===")

msg = "Python"
for ch in msg:
    print(f"字符: {ch}")
else:
    print("遍历结束~")

# ===== 2. range() 三种用法 =====
print("\n=== 2. range() 三种用法 ===")

# range(end): 0 到 end-1
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(start, end): start 到 end-1
print("range(3, 7):", end=" ")
for i in range(3, 7):
    print(i, end=" ")
print()

# range(start, end, step): 带步长
print("range(1, 10, 2):", end=" ")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# ===== 3. 实战：1-100 奇数和 =====
print("\n=== 3. 1-100 奇数和 ===")

# 方法1：步长为2（直接跳过偶数）
total = 0
for i in range(1, 101, 2):
    total += i
print(f"方法1（步长2）: {total}")

# 方法2：条件判断
total = 0
for i in range(1, 101):
    if i % 2 == 1:
        total += i
print(f"方法2（if判断）: {total}")

# ===== 4. 实战：100-500 中 3 的倍数和 =====
print("\n=== 4. 100-500 中 3 的倍数和 ===")

total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print(f"100-500 3的倍数和: {total}")

# 更高效：从 3 的倍数起始 + 步长
total = 0
start = 102  # 100 之后第一个 3 的倍数
for i in range(start, 501, 3):
    total += i
print(f"(高效版) 结果相同: {total}")

# ===== 5. for...else =====
print("\n=== 5. for...else ===")

# break 后 else 不执行
for i in range(10):
    if i == 5:
        print(f"找到 i={i}，break！")
        break
else:
    print("遍历完成")  # 不会输出

# 未找到时 else 执行
for i in range(10):
    if i == 999:
        break
else:
    print("未找到 999，else 执行")

# ===== 6. while vs for 演示 =====
print("\n=== 6. while vs for ===")
print(f"{'while':<20} {'for':<20}")
print(f"{'while i <= 100:':<20} {'for i in range(1, 101):':<20}")
print(f"{'需要手动 i += 1':<20} {'自动递增':<20}")
