"""
04 - 变量与标识符
对应课程：第 13–14 集
"""

# ===== 1. 变量：无需声明类型 =====
# 对比 Java: String name = "张三";
name = "张三"
age = 20
score = 98.5
is_passed = True

print("=== 变量赋值 ===")
print(f"name = {name}, 类型: {type(name)}")
print(f"age = {age}, 类型: {type(age)}")
print(f"score = {score}, 类型: {type(score)}")
print(f"is_passed = {is_passed}, 类型: {type(is_passed)}")

# ===== 2. 标识符命名规则 =====
print("\n=== 命名规则 ===")

# ✅ 正确命名
user_name = "李四"              # snake_case — Python 推荐风格
_private = "以下划线开头"        # 约定私有
normal2 = "可以包含数字"         # 但不能数字开头

print(f"snake_case 风格: {user_name}")
print(f"下划线开头: {_private}")
print(f"包含数字: {normal2}")

# ❌ 错误命名（取消注释会报错）
# 2user = "错误"    # SyntaxError: 不能数字开头
# class = "错误"    # SyntaxError: class 是保留字

# ===== 3. 多重赋值（Python 独有！）=====
print("\n=== 多重赋值 ===")

# 一行给多个变量赋值
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# 一行交换两个变量的值 — 不需要临时变量！
a, b = "苹果", "香蕉"
print(f"交换前: a={a}, b={b}")
a, b = b, a
print(f"交换后: a={a}, b={b}")

# 链式赋值
p = q = r = 0
print(f"链式赋值: p={p}, q={q}, r={r}")

# ===== 4. 变量可以重新指向不同类型的值 =====
print("\n=== 动态类型演示 ===")
data = 100
print(f"data = {data}, 类型: {type(data)}")   # int

data = "现在变成字符串了"
print(f"data = {data}, 类型: {type(data)}")   # str

data = [1, 2, 3]
print(f"data = {data}, 类型: {type(data)}")   # list
print("（不推荐频繁换类型，但 Python 允许这样做）")

# ===== 5. 删除变量 =====
temp = "用完就删"
print(f"\n删除前: temp = {temp}")
del temp
# print(temp)  # NameError: name 'temp' is not defined
print("del temp 后，temp 已被删除")
