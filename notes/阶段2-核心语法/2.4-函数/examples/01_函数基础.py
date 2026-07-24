"""
01 - 函数基础（定义/参数/返回值/多值返回/嵌套调用/docstring）
对应课程：第 57-63 集
生成时间: 2026-07-25
"""

# ===== 1. 函数定义与调用 =====
print("=== 1. 函数定义与调用 ===")


def out_line():
    print("hello world")
    print("------------")


out_line()

# ===== 2. 参数传递 =====
print("\n=== 2. 参数传递 ===")


def circle_area(r):
    """计算圆的面积"""
    return 3.14 * r ** 2


def rectangle_area(length, width):
    """计算长方形面积"""
    return length * width


print(f"圆面积(r=5): {circle_area(5)}")
print(f"长方形面积(4x3): {rectangle_area(4, 3)}")

# ===== 3. 多值返回 → 元组解包 =====
print("\n=== 3. 多值返回 ===")


def circle_info(r):
    """计算圆的面积和周长，返回多个值"""
    area = 3.14 * r ** 2
    perimeter = 2 * 3.14 * r
    return round(area, 1), round(perimeter, 1)


# 方式1：一个变量接收 → 元组
result = circle_info(5)
print(f"元组接收: {result}, 类型: {type(result)}")

# 方式2：解包接收（推荐）
area, perimeter = circle_info(5)
print(f"解包: 面积={area}, 周长={perimeter}")

# ===== 4. 函数嵌套调用 =====
print("\n=== 4. 函数嵌套调用 ===")


def outer():
    print("outer before")
    inner()
    print("outer after")


def inner():
    print("  inner")


outer()
print("调用完毕")

# ===== 5. docstring =====
print("\n=== 5. docstring ===")


def triangle_area(base, height):
    """
    根据传入的底和高计算三角形面积
    :param base:  底
    :param height: 高
    :return: 面积
    """
    return round(base * height / 2, 1)


print(f"三角形面积(底4,高3): {triangle_area(4, 3)}")

# ===== 6. 实战练习 =====
print("\n=== 6. 实战练习 ===")


# 统计元音字母
def count_vowels(s):
    """统计字符串中的元音字母个数"""
    total = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            total += 1
    return total


print(f"'Hello World' 元音数: {count_vowels('Hello World')}")


# 成绩统计
def score_stats(scores):
    """返回最高分、最低分、平均分"""
    return max(scores), min(scores), round(sum(scores) / len(scores), 1)


scores = [85, 92, 78, 90, 88]
high, low, avg = score_stats(scores)
print(f"成绩: 最高{high}, 最低{low}, 平均{avg}")
