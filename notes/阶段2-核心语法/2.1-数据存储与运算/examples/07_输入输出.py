"""
07 - 输入输出（input 和 print）
对应课程：第 18-19 集
生成时间: 2026-07-15
"""

# ===== 1. input() — 获取用户输入 =====
print("=== input() 示例 ===")

# 基本用法：提示语 + 等待输入
# name = input("请输入您的姓名: ")
# age = input("请输入您的年龄: ")
# print(f"您的姓名为{name}, 年龄为{age}")

# ===== 2. 关键坑：input() 返回 str！=====
print("\n=== 关键坑：input 返回 str ===")

# 取消注释来测试（这里用硬编码演示）
a_str = "10"    # 模拟 input 返回
b_str = "20"    # 模拟 input 返回

# ❌ 错误：字符串 + 字符串 = 拼接
print(f'未转换: "10" + "20" = "{a_str + b_str}"  ← 字符串拼接！')

# ✅ 正确：先转换为 int
a = int(a_str)
b = int(b_str)
print(f'转换后: {a} + {b} = {a + b}  ← 数值加法')

# ===== 3. print() 进阶用法 =====
print("\n=== print() 进阶 ===")

# end 参数：控制结尾字符（默认换行 \n）
print("第一行", end=" → ")
print("第二行")  # 输出在一行

# sep 参数：控制分隔符（默认空格）
print("a", "b", "c", sep=" | ")  # a | b | c

# ===== 4. 综合案例：计算两个数字之和 =====
print("\n=== 综合案例 ===")

# 取消注释来交互式体验：
# x = int(input("请输入一个数: "))
# y = int(input("请输入另一个数: "))
# print(f"{x} + {y} = {x + y}")

# 演示用硬编码代替 input
x, y = 25, 38
print(f"(演示) {x} + {y} = {x + y}")
print(f"(演示) {x} - {y} = {x - y}")
print(f"(演示) {x} * {y} = {x * y}")
print(f"(演示) {x} / {y} = {x / y}")

# ===== 5. 实战：模拟 ATM 取款 =====
print("\n=== 模拟 ATM 取款 ===")

balance = 10000
# password = input("请输入密码: ")
# if password == "123456":
#     amount = int(input("请输入取款金额: "))
#     balance -= amount
#     print(f"取款成功！取款{amount}元，余额{balance}元")
# else:
#     print("密码错误！")

# 硬编码演示
password = "123456"
amount = 2000
if password == "123456":
    balance -= amount
    print(f"取款成功！取款{amount}元，余额{balance}元")
