"""
02 - 异常处理（try/except/finally/多异常/异常传递）
对应课程：第 86-87 集
生成时间: 2026-07-27
"""

# ===== 1. 基本 try/except =====
print("=== 1. 基本 try/except ===")

try:
    print("------------------------------")
    # print(my_name)   # NameError: 变量未定义
    print("正常运行")
    print("------------------------------")
except NameError:
    print("系统出现异常,请联系管理人员")

# ===== 2. 多异常捕获 + as e =====
print("\n=== 2. 多异常捕获 ===")

errors = [
    # lambda: print(my_name),           # NameError
    lambda: print(1 / 0),               # ZeroDivisionError
    lambda: print('ABC'[9]),            # IndexError
    lambda: print('ABC'.hello),         # AttributeError
]

for i, test in enumerate(errors, 1):
    try:
        test()
    except NameError as e:
        print(f"  测试{i}: 名字不存在, 异常信息: {e}")
    except ZeroDivisionError as e:
        print(f"  测试{i}: 0不能做被除数, 异常信息: {e}")
    except IndexError as e:
        print(f"  测试{i}: 索引错误, 异常信息: {e}")
    except Exception as e:
        print(f"  测试{i}: 程序出错, 异常信息: {e}")
    finally:
        print(f"  测试{i}: 释放资源~")

# ===== 3. finally 总会执行 =====
print("\n=== 3. finally ===")

try:
    print("try 块执行")
except Exception:
    print("except 块（不会执行）")
finally:
    print("finally 块（总会执行）")

# ===== 4. 异常的传递 =====
print("\n=== 4. 异常传递 ===")


def fun1():
    print("fun1...running...")
    fun2()


def fun2():
    print("fun2...running...")
    fun3()


def fun3():
    print("fun3...running...")
    print(undefined_var)   # NameError 在这里发生


# 异常从 fun3 -> fun2 -> fun1 传递到最外层
if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print(f"在最外层捕获异常: {e}")

# ===== 5. 异常处理实战：保护用户输入 =====
print("\n=== 5. 保护用户输入 ===")

# 模拟用户输入（实战中用 input()）
test_inputs = ["abc", "3.14", "100"]

for user_input in test_inputs:
    try:
        num = float(user_input)
        print(f"  输入 '{user_input}' -> 数字 {num}")
    except ValueError as e:
        print(f"  输入 '{user_input}' -> ValueError: {e}")
    except Exception as e:
        print(f"  输入 '{user_input}' -> 未知错误: {e}")

# ===== 6. 常见异常类型速查 =====
print("\n=== 6. 常见异常类型 ===")

exceptions = [
    ("NameError", "变量未定义"),
    ("ValueError", "类型对但值非法，如 int('abc')"),
    ("TypeError", "类型不对，如 'a' + 1"),
    ("IndexError", "索引越界，如 [1,2][9]"),
    ("KeyError", "字典key不存在"),
    ("ZeroDivisionError", "除以零"),
    ("AttributeError", "属性/方法不存在"),
    ("Exception", "所有异常的父类（兜底）"),
]

for name, desc in exceptions:
    print(f"  {name:<20} {desc}")
