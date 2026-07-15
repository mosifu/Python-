"""
08 - 运算符（算术、赋值、比较、逻辑）
对应课程：第 20-21 集
生成时间: 2026-07-15
"""

# ===== 1. 算术运算符 =====
print("=== 1. 算术运算符 ===")

a, b = 10, 4
print(f"{a} + {b} = {a + b}")    # 加法 14
print(f"{a} - {b} = {a - b}")    # 减法 6
print(f"{a} * {b} = {a * b}")    # 乘法 40
print(f"{a} / {b} = {a / b}")    # 除法 2.5（Java 中 int/int=2！）
print(f"{a} % {b} = {a % b}")    # 取余 2
print(f"{a} // {b} = {a // b}")  # 整除 2（等同 Java int/int）
print(f"{a} ** {b} = {a ** b}")  # 指数 10000

# ===== 2. 优先级 =====
print("\n=== 2. 运算符优先级 ===")

# ** > * / % // > + -
print(f"0.1 + 10 / 4 ** 2 = {0.1 + 10 / 4 ** 2}")
# 解析: 4**2=16, 10/16=0.625, 0.1+0.625=0.725

print(f"(0.1 + 10) / 4 = {(0.1 + 10) / 4}")
# 括号最高: 0.1+10=10.1, 10.1/4=2.525

# ===== 3. 浮点精度问题 =====
print("\n=== 3. 浮点精度问题 ===")

print(f"0.5 - 0.4 = {0.5 - 0.4}")
# 结果: 0.09999999999999998 ← 不是 0.1！
# 原因: 二进制无法精确表示 0.1，所有语言都一样（Java 也是）

# 解决方案：用 round() 或 decimal
print(f"round(0.5 - 0.4, 2) = {round(0.5 - 0.4, 2)}")

# ===== 4. 赋值运算符 =====
print("\n=== 4. 赋值运算符 ===")

num = 85
print(f"初始: num = {num}")

num += 10               # num = num + 10
print(f"num += 10 → {num}")

num -= 10               # num = num - 10
print(f"num -= 10 → {num}")

num *= 10               # num = num * 10
print(f"num *= 10 → {num}")

num /= 10               # num = num / 10
print(f"num /= 10 → {num}")

num = int(num)          # 恢复为 int
num //= 10              # num = num // 10
print(f"num //= 10 → {num}")

num %= 3                # num = num % 3
print(f"num %= 3 → {num}")

num = 2
num **= 3               # num = num ** 3
print(f"num **= 3 → {num}")

# ===== 5. 比较运算符 =====
print("\n=== 5. 比较运算符 ===")
# 和 Java 完全一样，无记忆负担

print(f"100 == 100 ? {100 == 100}")    # True
print(f"100 != 100 ? {100 != 100}")    # False
print(f"100 > 100  ? {100 > 100}")     # False
print(f"100 < 100  ? {100 < 100}")     # False
print(f"100 >= 100 ? {100 >= 100}")    # True
print(f"100 <= 100 ? {100 <= 100}")    # True

# 字符串也可以比较（按字典序）
print(f'"abc" == "abc" ? {"abc" == "abc"}')    # True
print(f'"abc" < "abd"  ? {"abc" < "abd"}')     # True

# ===== 6. 逻辑运算符 =====
print("\n=== 6. 逻辑运算符 ===")
# ⚠️ 最大坑：Python 用 and/or/not，不是 &&/||/!

print(f"True and True  = {True and True}")     # True
print(f"True and False = {True and False}")    # False
print(f"True or False  = {True or False}")     # True
print(f"False or False = {False or False}")    # False
print(f"not True       = {not True}")          # False
print(f"not False      = {not False}")         # True

# 综合案例1：判断数字在 10-20 之间
num = 15
print(f"\n{num} 在 10-20 之间吗？ {num >= 10 and num <= 20}")

# 综合案例2：判断数字不在 10-20 之间
print(f"{num} 不在 10-20 之间吗？ {num < 10 or num > 20}")

# info 演示不同情况的判断
nums = [5, 15, 25]
for n in nums:
    in_range = n >= 10 and n <= 20
    print(f"  {n:>3} → {'在 10-20 之间' if in_range else '不在 10-20 之间'}")

# ===== 7. Python vs Java 运算符速查 =====
print("\n=== Python vs Java 运算符速查 ===")
compare = [
    ("算术", "+ - * %", "一样", ""),
    ("除法", "10 / 4 = 2.5", "10 / 4 = 2", "Python / 总返回float"),
    ("整除", "10 // 4 = 2", "(无)", "Python 独有 //"),
    ("指数", "10 ** 4", "Math.pow(10,4)", "Python 内置幂运算符"),
    ("赋值", "+= -= *= /= %= //= **=", "+= -= *= /= %=", "多了 //= 和 **="),
    ("比较", "== != > < >= <=", "一样", "完全兼容"),
    ("逻辑", "and or not", "&& || !", "最易写错！"),
]
for cat, py, java, note in compare:
    print(f"  {cat:<6}  Python: {py:<25}  Java: {java:<25}  {note}")
