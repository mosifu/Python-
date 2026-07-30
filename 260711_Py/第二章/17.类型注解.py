# 1. 变量定义：未定义类型注解
a = 1
b = 2.4
c = "Hello World"
flag = True
d = None
names = ['A', 'B', 'C']
phone = {'123123123', '342342351231', '22222'}
options = {"count":2, "total":10}
goods = ("手机", 999, 1)

names.append("X")
print(names)


# 2. 变量定义：指定类型注解 --- 添加类型注解也只是提示一下，不会改变python是动态类型语言的事实，强制执行的话也会改变
a1: int = 2
b2: float = 2.5
hobby: str = "Python"
flag2: bool = True
d1: None = None

names: list[str | int] = ["A", 23, "B"]
phones: set[str] = {"123", "234", "3535"}
options1:dict[str | int, int] = {"count":2, 555:10}
goods1: tuple[str, int, float] = ("nihao", 12, 1.3)

#类型推断： python解释器自动推断出变量，表达式或函数返回值的数据类型的能力，无需开发者显式声明

#函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(al)


# 为前面订单计算器函数设置类型注解
def calc_order_cost(*args: tuple[str, float, int], coupon: int = 0, score: int =0, express: float = 0.0) -> float:
    #订单的总金额=商品总金额-优惠券-积分抵扣运费
    #1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    #2.扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    #3.扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    #4.添加运费
    total_cost += express
    return total_cost

total = calc_order_cost(("手机", 4999, 2),("茶叶", 78, 5),coupon = 10, score = 4000, express = 9.9)
print(total)
