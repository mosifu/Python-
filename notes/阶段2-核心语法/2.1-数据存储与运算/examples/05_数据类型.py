"""
05 - 数据类型
对应课程：第 15 集
"""

# ===== 1. Python 的常见数据类型 =====
print("=== Python 数据类型一览 ===\n")

# 数字类型
age = 20
price = 9.99
cnum = 1 + 2j

# 文本类型
message = "Hello, Python!"

# 布尔类型
is_ok = True

# 空类型
nothing = None

# 打印所有类型
variables = [
    ("age", age),
    ("price", price),
    ("cnum", cnum),
    ("message", message),
    ("is_ok", is_ok),
    ("nothing", nothing),
]

for name, value in variables:
    print(f"  {name:10} = {str(value):20} → 类型: {type(value).__name__}")

# ===== 2. 动态类型 vs 静态类型 =====
print("\n=== 动态类型演示 ===")
print("Python 是动态类型：变量运行时才确定类型")
print("Java 是静态类型：变量编译时已确定类型\n")

# Python：同一变量可以换类型
data = 42
print(f"data = {data}  → {type(data).__name__}")

data = "四十二"
print(f"data = {data}  → {type(data).__name__}")

data = 3.14
print(f"data = {data}  → {type(data).__name__}")

print("\n[!] 虽然可以换类型，但实际项目中不推荐频繁换类型！")

# ===== 3. type() vs isinstance() =====
print("\n=== type() 和 isinstance() ===")

value = 100

# type() — 精确判断
print(f"type(value) == int:  {type(value) == int}")     # True
print(f"type(value) == str:  {type(value) == str}")     # False

# isinstance() — 考虑继承（推荐用法）
print(f"isinstance(value, int):        {isinstance(value, int)}")        # True
print(f"isinstance(value, str):        {isinstance(value, str)}")        # False
print(f"isinstance(value, (int, float)): {isinstance(value, (int, float))}")  # True — 可多类型

# ===== 4. 类型转换 =====
print("\n=== 类型转换 ===")

# str() — 转字符串（= Java String.valueOf()）
s1 = str(100)
s2 = str(3.14)
s3 = str(True)
print(f"str(100) = {repr(s1)}, type: {type(s1).__name__}")
print(f"str(3.14) = {repr(s2)}, type: {type(s2).__name__}")
print(f"str(True) = {repr(s3)}, type: {type(s3).__name__}")

# int() — 转整数（= Java Integer.parseInt()）
print(f"\nint(3.14) = {int(3.14)}       # 截断，不是四舍五入")
print(f'int("100") = {int("100")}')

# float() — 转浮点
print(f"\nfloat(10) = {float(10)}")
print(f'float("3.14") = {float("3.14")}')

# bool() — 转布尔
print(f"\nbool(1) = {bool(1)}          # 非0为True")
print(f"bool(0) = {bool(0)}           # 0为False")
print(f'bool(\"\") = {bool("")}        # 空字符串为False')
print(f'bool(\"hello\") = {bool("hello")} # 非空字符串为True')
print(f"bool([]) = {bool([])}         # 空列表为False")
print(f"bool(None) = {bool(None)}     # None为False")

# ===== 5. Python vs Java 类型对照表 =====
print("\n=== Python vs Java 类型对照 ===")
table = [
    ("int", "int/long/BigInteger", "无限精度，自动扩容"),
    ("float", "double", "64位双精度，无 float/double 之分"),
    ("complex", "(无原生支持)", "内置 1+2j 语法"),
    ("str", "String", "无 char 类型；单双引号等价"),
    ("bool", "boolean", "True/False 首字母大写"),
    ("NoneType", "null", "None 是单例对象"),
]
for py, java, note in table:
    print(f"  {py:<10} vs {java:<25} → {note}")

print("\n[*] 核心记忆：Python 动态类型但强类型，写法省了声明但逻辑一样严谨")
