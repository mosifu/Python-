"""
01 - 类型注解（变量/容器/Union/函数注解/类型推断）
对应课程：第 71-72 集
生成时间: 2026-07-26
"""

# ===== 1. 变量类型注解 =====
print("=== 1. 变量类型注解 ===")

# 无注解
a = 1
b = 2.4
c = "Hello World"
flag = True

# 有注解 - 变量名: 类型 = 值
a1: int = 2
b2: float = 2.5
hobby: str = "Python"
flag2: bool = True
d1: None = None

print(f"a1={a1}, b2={b2}, hobby={hobby}")

# ===== 2. 容器类型注解 =====
print("\n=== 2. 容器类型注解 ===")

# 列表 - list[元素类型]
names: list[str | int] = ["A", 23, "B"]
names.append("X")
print(f"names: {names}")

# 集合 - set[元素类型]
phones: set[str] = {"123", "234", "3535"}
print(f"phones: {phones}")

# 字典 - dict[key类型, value类型]
options: dict[str | int, int] = {"count": 2, 555: 10}
print(f"options: {options}")

# 元组 - tuple[类型1, 类型2, 类型3]
goods: tuple[str, int, float] = ("手机", 999, 1.3)
print(f"goods: {goods}")

# ===== 3. Union 联合类型 =====
print("\n=== 3. Union 联合类型 | ===")

# Python 3.10+ 用 | 表示"或"
x: int | str = 10
print(f"x 是 int: {x}")
x = "hello"           # 合法！注解不强制
print(f"x 变 str: {x}")

# ===== 4. 函数类型注解 =====
print("\n=== 4. 函数类型注解 ===")


def circle_area_len(r: float) -> tuple[float, float]:
    """返回 (面积, 周长)"""
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


area, length = circle_area_len(10)
print(f"圆 r=10: 面积={area}, 周长={length}")

# ===== 5. 实战：订单计算器（带注解）=====
print("\n=== 5. 订单计算器（带注解）===")


def calc_order_cost(
    *args: tuple[str, float, int],
    coupon: int = 0,
    score: int = 0,
    express: float = 0.0
) -> float:
    """计算订单总金额"""
    prices = [goods[1] * goods[2] for goods in args]
    total = sum(prices)
    print(f"  商品总额: {total}")

    if total >= 5000 and coupon <= total:
        total -= coupon
        print(f"  减优惠券 {coupon} -> {total}")

    if total >= 5000 and score // 100 <= total:
        discount = score // 100
        total -= discount
        print(f"  减积分({score}分={discount}元) -> {total}")

    total += express
    print(f"  加运费 {express} -> {total}")
    return total


result = calc_order_cost(
    ("手机", 4999, 2), ("茶叶", 78, 5),
    coupon=10, score=4000, express=9.9
)
print(f"  订单总金额: {result}")

# ===== 6. 类型推断 =====
print("\n=== 6. 类型推断 ===")
# 解释器自动推断，无需显式声明
y = 10          # 推断为 int
z = "hello"     # 推断为 str
print(f"y={y}(推断int), z={z}(推断str)")
print("注解主要给 IDE 和 mypy 用，运行时不强制")
