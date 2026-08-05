#定义类 ---> 不推荐 动态的为对象添加属性
# class Car:
#     pass
#
# #创建对象
# c1 = Car()
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 50000
#
# print(c1)
# print(c1.brand)
# print(c1.__dict__)  #会将对象中的所有属性以字典形式输出出来


#定义类:类命名使用大驼峰命名法
# class Car:
#     # __init__ 方法是初始化的方法,会在创建对象时自动调用,可以在该方法中为对象设置对应的属性
#     #self:是第一个参数,表示当前所创建出来的示例对象
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已添加完毕")

# c1 = Car("蓝色", "BMW", "X5", 1000000)
# c2 = Car("黄色", "XIAOMI", "SU7", 1000000)
# print(c1.c_brand)
# print(c1.__dict__)
# print(c2.__dict__)



# -------------- 定义类:实例方法 -----------------
# class Car:
#     # __init__ 方法是初始化的方法,会在创建对象时自动调用,可以在该方法中为对象设置对应的属性
#     #self:是第一个参数,表示当前所创建出来的示例对象
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已添加完毕")
#
#     #定义实例方法
#     def running(self):
#         print(f"{self.c_brand}{self.c_name}正在高速行驶...")
#
#     def total_price(self, discount, rate):
#         """
#         计算提车的价格
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 提车总价
#         """
#         total_price = discount * self.c_price + rate * self.c_price
#         return total_price
# c1 = Car("蓝色", "BMW", "X5", 1000000)
#
# #调用对象中的方法
# c1.running()
# print(f"{c1.c_brand}{c1.c_name}的提车价格为:{c1.total_price(0.9,0.1)}")


# -------------------- 定义类: 魔法方法 ----------------------
# class Car:
#     # __init__ 方法是初始化的方法,会在创建对象时自动调用,可以在该方法中为对象设置对应的属性
#     #self:是第一个参数,表示当前所创建出来的示例对象
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已添加完毕")
#
#     #魔法方法:Python中提供的_xxx_形式的特殊方法,魔法方法无需手动调用,Python会在合适的时机自动调用
#     def __str__(self):
#         return f"{self.c_color} {self.c_brand} {self.c_name} {self.c_price}"
#
#     def __lt__(self, other):
#         return self.c_price < other.c_price
#
#     def __eq__(self, other):
#         return self.c_price == other.c_price and self.c_color == other.c_color and self.c_brand == other.c_brand and self.c_name == other.c_name
# c1 = Car("蓝色", "BMW", "X5", 1000000)
# c2 = Car("蓝色", "BMW", "X5", 1000000)
#
# print(c1)
# print(c2)
#
# print(c1 == c2)
# print(c1 > c2)


# ------------------实例属性与类属性------------------
class Car:
    #类属性(所有实例对象共享)
    wheel = 4   #车辆轮胎数量
    tax_rate = 0.1  #汽车购置税率
    # __init__ 方法是初始化的方法,会在创建对象时自动调用,可以在该方法中为对象设置对应的属性
    #self:是第一个参数,表示当前所创建出来的示例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        self.wheel = 2

c1 = Car("蓝色", "BMW", "X5", 1000000)
print(c1.wheel) #通过实例对象,查找属性时,会先查找实例属性;实例属性不存在,再查找类属性

#通过类名访问类属性
print(Car.wheel)
