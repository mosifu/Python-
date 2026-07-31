"""
01 - 面向对象基础（类/对象/__init__/self/实例方法/魔法方法/类属性）
对应课程：第 77-81 集
生成时间: 2026-07-27
"""

# ===== 1. 定义类与创建对象 =====
print("=== 1. 类与对象 ===")


class Car:
    def __init__(self, color, brand, name, price):
        """__init__ 在创建对象时自动调用，self 是当前对象"""
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price
        print(f"{brand}{name} 对象初始化完毕")


c1 = Car("蓝色", "BMW", "X5", 1000000)
c2 = Car("黄色", "XIAOMI", "SU7", 1000000)
print(f"c1.brand = {c1.brand}")
print(f"c2 的所有属性: {c2.__dict__}")

# ===== 2. 实例方法 =====
print("\n=== 2. 实例方法 ===")


class Car2:
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        """实例方法 - 第一个参数永远是 self"""
        print(f"{self.brand}{self.name}正在高速行驶...")

    def total_price(self, discount, rate):
        """计算提车价 = 折扣价 + 税"""
        return discount * self.price + rate * self.price


c = Car2("蓝色", "BMW", "X5", 1000000)
c.running()
print(f"提车价: {c.total_price(0.9, 0.1)}")

# ===== 3. 魔法方法 =====
print("\n=== 3. 魔法方法 ===")


class Car3:
    def __init__(self, color, brand, name, price):
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price

    def __str__(self):
        """print(对象) 时自动调用"""
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __lt__(self, other):
        """obj1 < obj2 时自动调用"""
        return self.price < other.price

    def __eq__(self, other):
        """obj1 == obj2 时自动调用"""
        return (self.price == other.price and
                self.color == other.color and
                self.brand == other.brand and
                self.name == other.name)


a = Car3("蓝色", "BMW", "X5", 1000000)
b = Car3("蓝色", "BMW", "X5", 1000000)
d = Car3("红色", "Audi", "A6", 800000)

print(f"print(a): {a}")           # 触发 __str__
print(f"a == b: {a == b}")        # 触发 __eq__ -> True
print(f"a > d: {a > d}")          # 触发 __lt__ -> False（100万 > 80万）
print(f"d < a: {d < a}")          # 触发 __lt__ -> True

# ===== 4. 实例属性与类属性 =====
print("\n=== 4. 实例属性与类属性 ===")


class Car4:
    wheel = 4         # 类属性 - 所有实例共享
    tax_rate = 0.1    # 类属性

    def __init__(self, color, brand, name, price):
        self.color = color    # 实例属性 - 各对象独有
        self.brand = brand
        self.name = name
        self.price = price


e = Car4("蓝色", "BMW", "X5", 1000000)
f = Car4("红色", "Audi", "A6", 800000)

print(f"e.wheel = {e.wheel}")       # 4（类属性）
print(f"f.wheel = {f.wheel}")       # 4（类属性）
print(f"Car4.wheel = {Car4.wheel}") # 4（通过类名访问）

# 修改类属性 - 所有实例都受影响
Car4.wheel = 6
print(f"修改类属性后 e.wheel = {e.wheel}")   # 6
print(f"修改类属性后 f.wheel = {f.wheel}")   # 6

# 实例属性遮蔽类属性
e.wheel = 2   # 创建实例属性，不影响类属性和其他实例
print(f"e.wheel = {e.wheel}")       # 2（实例属性优先）
print(f"f.wheel = {f.wheel}")       # 6（类属性）
print(f"Car4.wheel = {Car4.wheel}") # 6（类属性不变）
