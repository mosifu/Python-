"""
01 - 数字字面量示例
对应课程：第 09 集
生成时间: 2026-07-14
"""

# ===== 整数（int）=====
# Python 的 int 不限大小，自动处理大整数
age = 25
big_number = 14_0000_0000  # 下划线分隔，更易读（Java 7+ 也支持）
negative = -10

print("=== 整数 ===")
print(f"年龄: {age}, 类型: {type(age)}")
print(f"大数: {big_number}, 类型: {type(big_number)}")
print(f"负数: {negative}")

# ===== 浮点数（float）=====
# Python 的 float = Java 的 double（64位双精度）
pi = 3.14159
price = -0.5
sci = 1.5e-3  # 科学计数法 = 0.0015

print("\n=== 浮点数 ===")
print(f"π: {pi}")
print(f"价格: {price}")
print(f"科学计数法 1.5e-3 = {sci}")

# ===== 复数（complex）=====
# Python 内置支持，Java 无此特性
c = 1 + 2j
print("\n=== 复数 ===")
print(f"复数: {c}")
print(f"实部: {c.real}, 虚部: {c.imag}")
