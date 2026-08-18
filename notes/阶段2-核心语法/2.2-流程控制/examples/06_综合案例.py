"""
06 - 综合案例（猜数字游戏 / for筛选 / 遍历计数）
对应课程：第 35 集综合练习
生成时间: 2026-07-17
"""

# ===== 案例1：猜数字游戏 =====
# 综合：random + while True + if/elif/else + break + input + int()
print("=== 案例1：猜数字游戏 ===")

import random

# 用固定种子模拟演示（实战中去掉 seed 用真正的随机数）
target = random.randint(1, 100)

# 模拟用户输入序列演示（实战中用 input()）
test_guesses = [50, 75, 62, 68, 65]  # target 假设为 65
for guess in test_guesses:
    if guess > target:
        hint = "猜大了！"
    elif guess < target:
        hint = "猜小了！"
    else:
        hint = "猜对了~"
    print(f"  猜 {guess:>3} → {hint}")
    if guess == target:
        break

print(f"随机数字为: {target}")

# ===== 案例2：1-1000 中 5 的倍数之和 =====
print("\n=== 案例2：1-1000 中 5 的倍数之和 ===")

total = 0
for i in range(1, 1001):
    if i % 5 == 0:
        total += i

print(f"结果: {total}")
# 验证：等差数列求和 = 5 * (1+2+...+200) = 5 * 200*201/2 = 100500
expected = 5 * 200 * 201 // 2
print(f"验证: {total} == {expected}? {total == expected}")

# ===== 案例3：统计字符串中 a 和 k 的个数 =====
print("\n=== 案例3：统计字符出现次数 ===")

# 用硬编码演示（实战中用 input()）
text = "a quick brown fox jumps over a lazy dog and keeps jumping"
count_a = count_k = 0

for ch in text:
    if ch == 'a':
        count_a += 1
    elif ch == 'k':
        count_k += 1

print(f"字符串: '{text}'")
print(f"  'a' 出现 {count_a} 次")
print(f"  'k' 出现 {count_k} 次")

# ===== 技巧：链式赋值 =====
print("\n=== 技巧：链式赋值 ===")
x = y = z = 0
print(f"x={x}, y={y}, z={z}  ← 一行初始化三个变量")
