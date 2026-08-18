"""
02 - 函数进阶（作用域/传参方式/不定长参数/高阶函数/lambda/递归）
对应课程：第 64-70 集
生成时间: 2026-07-25
"""

# ===== 1. 变量作用域 =====
print("=== 1. 变量作用域 ===")

num = 100  # 全局变量


def calc(r):
    global num       # 声明修改全局变量（PEP 8：放函数顶部）
    pi = 3.14        # 局部变量
    num = 10000      # 修改全局 num
    return pi * r ** 2


print(f"calc(10) = {calc(10)}")
print(f"全局 num = {num}（已被函数修改）")

# ===== 2. 传参方式 =====
print("\n=== 2. 传参方式 ===")


def register(name, age, gender, city):
    return {"name": name, "age": age, "gender": gender, "city": city}


# 位置传参 — 按顺序
r1 = register("mosifu", 23, "男", "贵阳")
print(f"位置传参: {r1}")

# 关键字传参 — 顺序随意
r2 = register(name="lan", gender="女", city="贵阳", age=23)
print(f"关键字传参: {r2}")

# 混合传参 — 位置必须在关键字前
r3 = register("jian", 23, city="贵阳", gender="女")
print(f"混合传参: {r3}")

# ===== 3. 默认参数 =====
print("\n=== 3. 默认参数 ===")


def register2(name, age, gender="男", city="东莞"):
    """默认参数必须放在非默认参数后面"""
    return {"name": name, "age": age, "gender": gender, "city": city}


print(f"全默认: {register2('mo', 23)}")
print(f"覆盖gender: {register2('lan', 24, '女')}")
print(f"关键字覆盖: {register2('momo', 25, city='贵阳')}")

# ===== 4. 不定长参数 *args =====
print("\n=== 4. *args（元组）===")


def calc_data(*args):
    """任意个数字，求最大/最小/平均"""
    return min(args), max(args), round(sum(args) / len(args), 2)


mn, mx, avg = calc_data(1, 3, 2, 45, 5, 2, 4)
print(f"最大值:{mx}, 最小值:{mn}, 平均值:{avg}")

# ===== 5. **kwargs（字典）=====
print("\n=== 5. **kwargs（字典）===")


def calc_data2(*args, **kwargs):
    """*args = 数据, **kwargs = 可选控制参数"""
    min_val = min(args)
    max_val = max(args)
    avg_val = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_val = round(avg_val, kwargs["round"])
    if kwargs.get("print"):
        print(f"  最大值:{max_val}, 最小值:{min_val}, 平均值:{avg_val}")

    return min_val, max_val, avg_val


print("带选项:")
calc_data2(1, 3, 2, 45, 5, 2, 4, round=2, print=True)
print("不带选项:")
calc_data2(13, 23, 42, 45, 25, 42, 4)

# ===== 6. 函数作为参数（高阶函数）=====
print("\n=== 6. 高阶函数 ===")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def calculate(x, y, operation):
    """operation 是一个函数"""
    return operation(x, y)


print(f"calc(2,3,add) = {calculate(2, 3, add)}")
print(f"calc(2,3,subtract) = {calculate(2, 3, subtract)}")

# ===== 7. lambda 匿名函数 =====
print("\n=== 7. lambda ===")

# 简化写法
add_lambda = lambda a, b: a + b
print(f"lambda 加法: {add_lambda(10, 20)}")

# 经典应用：sort 自定义排序
data = ["C++", "C", "Python", "Java", "Go", "JavaScript", "Rust"]
data.sort(key=lambda item: len(item))  # 按字符串长度排序
print(f"按长度排序: {data}")

# ===== 8. 递归：阶乘 =====
print("\n=== 8. 递归 ===")


def factorial(n):
    """计算 n!  -- 必须有终结点"""
    if n == 1:          # 终结点
        return 1
    return n * factorial(n - 1)


print(f"4! = {factorial(4)}")  # 4*3*2*1 = 24
print(f"5! = {factorial(5)}")  # 120

# ===== 9. 综合：电商订单计算器 =====
print("\n=== 9. 电商订单计算器 ===")


def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    """
    计算电商订单总金额
    :param args: 商品元组 (商品名, 单价, 数量)
    :param coupon: 优惠券（满5000可用）
    :param score: 积分（满5000可用，100积分=1元）
    :param express: 运费
    """
    prices = [goods[1] * goods[2] for goods in args]
    total = sum(prices)
    print(f"  商品总额: {total}")

    if total >= 5000 and coupon <= total:
        total -= coupon
        print(f"  减优惠券: {coupon} → {total}")

    if total >= 5000 and score // 100 <= total:
        discount = score // 100
        total -= discount
        print(f"  减积分({score}分={discount}元) → {total}")

    total += express
    print(f"  加运费: {express}")
    return total


result = calc_order_cost(
    ("手机", 4999, 2), ("茶叶", 78, 5),
    coupon=10, score=4000, express=9.9
)
print(f"  订单总金额: {result}")
