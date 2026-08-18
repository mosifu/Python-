"""
03 - 布尔与 None 字面量 + type() 用法
对应课程：第 09–10 集
生成时间: 2026-07-14
"""

# ===== 布尔值（bool）=====
# ⚠️ Java 程序员注意：首字母大写！
is_student = True    # ✅ 不是 true
is_teacher = False   # ✅ 不是 false

print("=== 布尔值 ===")
print(f"is_student = {is_student}, 类型: {type(is_student)}")
print(f"is_teacher = {is_teacher}, 类型: {type(is_teacher)}")

# 常见错误示范（取消注释会让程序报错）：
# is_admin = true   # ❌ NameError: name 'true' is not defined

# ===== None =====
# Python 的空值 = Java 的 null
# 判断时用 "is None"，不是 "== null"
result = None

print("\n=== None ===")
print(f"result = {result}, 类型: {type(result)}")

if result is None:       # ✅ 推荐写法
    print("result 是 None（用 is None 判断）")

if result == None:       # ⚠️ 能用但不推荐
    print("result 是 None（用 == None 判断）")

# ===== type() — 查看任何值的类型 =====
print("\n=== type() 查看所有字面量类型 ===")
print(f"100        → {type(100)}")
print(f"3.14       → {type(3.14)}")
print(f"1+2j       → {type(1+2j)}")
print(f"'hello'    → {type('hello')}")
print(f"True       → {type(True)}")
print(f"None       → {type(None)}")

# ===== 快速对比 Java 差异 =====
print("\n=== Java vs Python 速查 ===")
java_vs_python = [
    ("Java", "Python"),
    ("true/false (小写)", "True/False (大写)"),
    ("null", "None"),
    ('char c = \'A\';', 'c = \'A\' (也是str)'),
    ("int(4B) / long(8B)", "int (无限大)"),
    ("float(4B) / double(8B)", "float (=double 8B)"),
]
for java, python in java_vs_python:
    print(f"  {java:<30} → {python:<30}")
