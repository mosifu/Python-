# 变量作用域
#全局变量
# num = 100
# def cir_area(r):
#     pi = 3.14   #局部变量
#     area = pi * (r ** 2)
#     #可以使用global声明使用的是全局变量
#     global num
#     num = 10000 #如果在函数内定义一个和全局变量一样的值,不会影响函数外的局部变量,这里输出 10000
#     print(num)  #可以在函数内使用全局变量
#     #但是在函数内定义的变量只能是局部变量函数外无法使用
#     return area
#
# print(cir_area(10))
# print(num)  #10000
#global主要用在程序的状态、配置和计数器等场景中


# ------------ 传参方式 ----------------
#定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# #1.位置传参 --> 实参顺序和形参顺序一致
# s1 = reg_stu("mosifu", 23, "男", "贵阳")
# print(s1)
#
# #2.关键字传参 -->顺序不做要求,关键字对上就行
# s2 = reg_stu(name="lan",gender="女", city="贵阳", age=23)
# print(s2)
#
# #3.混合传参 --> 必须位置传参在前(否则报错)
# s3 = reg_stu("jian", 23, city="贵阳", gender="女")
# print(s3)


# ------------------- 默认参数 ---------------
# def reg_stu1(name, age, gender = "男", city = "东莞"): #默认参数必须放在非默认参数后面
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# s4 = reg_stu1("mo", 23)
# print(s4)
#
# s5 = reg_stu1("jianlan" , 24, "女")
# print(s5)
#
# s6 = reg_stu1("momo", 25,city="贵阳")
# print(s6)


# --------------------- 不定长参数(位置传参 *args ---> 元组类型) -------------
#根据输入的数据,求最大值,最小值,平均值
# def cacl_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     sum_data = sum(args)
#     avg_data = sum_data / len(args)
#     return min_data, max_data, round(avg_data, 2)
#
# #调用函数
# m,a,v = cacl_data(1,3,2,45,5,2,4)
# print(f"最大值:{a},最小值:{m},平均值:{v}")


# --------------------- 不定长参数(关键字传参 **kwargs ---> 字典类型) -------------
#根据输入的数据,求最大值,最小值,平均值
# def cacl_data(*args, **kwargs):
#     min_data = min(args)
#     max_data = max(args)
#     sum_data = sum(args)
#     avg_data = sum_data / len(args)
#     if kwargs.get("round") is not None:
#         avg_data = round(avg_data, kwargs["round"])
#     if kwargs.get("print") :
#         print(f"最大值:{max_data},最小值:{min_data},平均值:{avg_data}")
#     return min_data, max_data, avg_data
#
# #调用函数
# print(cacl_data(1,3,2,45,5,2,4,round = 2, print= True))
# print(cacl_data(13,23,42,45,25,42,4))


# ---------------- 函数参数类型 -----------------
#参数类型可以是int,float,list,str,tuple,set,dict也可以是其他函数
#函数的参数类型
#加
# def add(x, y):
#     return x + y
#
# #减
# def subtract(x, y):
#     return x - y
#
# #乘
# def multiply(x, y):
#     return x * y
#
# #除
# def divide(x, y):
#     return x / y
#
# def cacl(x, y, oper):
#     return oper(x, y)
# print(cacl(2,3,add))
# print(cacl(2,3,subtract))
# print(cacl(2,3,multiply))
# print(cacl(2,3,divide))


# -------------------- 匿名函数 -------------------------
#1.打印一个分割线
#命名函数实现
# def out_line():
#     print("命名函数实现---------------------")
# #使用
# out_line()
#
# #匿名函数实现
# out_line1 = lambda : print("匿名函数实现---------------")
# out_line1()
#
# #2.计算两数之和
# def add_xy(a, b):
#     print(a+b)
#
# add_xy(20,20)
#
# add_xy1 = lambda a,b: a+b
# print(add_xy1(10,20))
#
# #需求3:完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序;
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# #使用官方方法来排序sort,可以指定按照什么来排序
# data_list.sort(key = lambda item : len(item))   #官方文档给出可以自定义sort的排序方式,用key来定义
# print(data_list)


# ------------ 案例 -------------
#1.计算n的阶乘
#递归调用(先层层递进,再逐层回归):在函数中自己调用自己 --->一定要有终结点
"""
jc(4) = 4 * jc(3)   --> 4 * 6 =24
jc(3) = 3 * jc(2)   --> 3 * 2 =6
jc(2) = 2 * jc(1)   --> 2 * 1 =2
jc(1) = 1
"""
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n-1)
# result = jc(4)
# print(result)


#2.电商订单计算器
"""
    定义一个函数,用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信
    息计算订单的总金额。
    具体规则如下:
    优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
    积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。
"""
def calc_order_cost(*args, coupon = 0, score =0, express = 0.0):
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