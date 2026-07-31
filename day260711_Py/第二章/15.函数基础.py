# 函数定义 ： 必须先定义后调用；定义的时候不会执行
# def out_line():
#     print("hello world")
#     print("------------")
#
# #调用
# out_line()
import sys


#1.函数：传入一个参数的情况
#计算圆的面积-传入半径r
# def circle_area(r):
#     """
#     计算圆的面积
#     :param r:   半径
#     :return:    圆的面积
#     """
#     area = 3.14 * r ** 2
#     return area
# print(f"计算半径为5的圆的面积为:{circle_area(5)}")
#
# #2.传入多个参数 ->使用逗号隔开
# #计算长方形的面积 - 传入长宽
# def rectangle_area(l, w):
#     """
#     计算长方形面积
#     :param l:   长
#     :param w:   宽
#     :return:    长方形面积
#     """
#     area = l * w
#     return area
# print(f"计算长为4,宽为3的长方形面积为:{rectangle_area(4,3)}")    #传入的实参顺序必须和形参的一样
#
# #3.返回多个结果的情况 -> 逗号隔开
# #计算圆的面积和周长
# def circle_area(r):
#     """
#     计算圆的面积和周长
#     :param r:   圆的半径
#     :return:    圆的面积,周长
#     """
#     area = 3.14 * r ** 2
#     length = 2 * 3.14 * r
#     return round(area, 1), round(length, 1)    #设置精度可以用round(数字, 需要控制的精度)
# s = circle_area(5)  #可以用一个元素来接受, 会以元组的形式接受
# print(s)
# print(type(s))
# a, l = circle_area(5)   #或者以解包的形式接受
# print(f"计算半径为5的圆的面积为:{a},周长为:{l}")


# 函数嵌套调用
#函数的嵌套调用 ---- 函数执行会按照栈的方式进行,后进先出
# def function_a():
#     print("a...before")
#     function_b()
#     print("a...after")
#
# def function_b():
#     print("b...before")
#     function_c()
#     print("b...after")
#
# def function_c():
#     print("c...")
#
# function_a()
# print("函数调用完毕~")


# -------- 案例 ------------
#1.定义一个函数:根据传入的底和高计算三角形面积的函数(3三角形面积=底*高/2)。
# def tri_area(d, h):
#     """
#     根据传入的三角形底和高计算三角形面积
#     :param d: 底
#     :param h: 高
#     :return: 面积
#     """
#     s = d * h /2
#     return round(s, 1)
# d = float(input("请输入三角形的底:"))
# h = float(input("请输入三角形的高:"))
# print(f"三角形面积为:{tri_area(d, h)}")

#2.定义一个函数:计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)。
# def sum_vos(s):
#     """
#     计算传入的字符串中元音字母的个数(元音字母为aeiouAEIOU)
#     :param s: 传入的字符串
#     :return: 元音字母个数
#     """
#     sum = 0
#     for i in s:
#         if  i in 'aeiouAEIOU':
#             sum += 1
#     return sum
# s = input("请输入字符串:")
# print(f"字符串:{s}中元音字母个数为:{sum_vos(s)}")

#3.定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回。
# def deal_stu_scor(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
#     :param score_list: 分数列表
#     :return: 最高分,最低分,平均分
#     """
#     sumscore = sum(score_list)
#     minscore = min(score_list)
#     maxscore = max(score_list)
#     avgscore = round(sumscore / len(score_list), 1)
#     return maxscore, minscore, avgscore
# s = [float(x.strip()) for x in input("输入班级学生高考成绩(用逗号隔开):").split(',') if x.strip()]
# max_s, min_s, avg_s = deal_stu_scor(s)
# print(f"最高分为:{max_s},最低分为:{min_s},平均分为:{avg_s}")

# ------------- 练习 ----------------
"""
    1.定义一个函数,根据传入的分数,计算对应的分数等级并返回。
    分数>=90:A
    分数>=75:B
    分数>=60:C
    分数<60:D
"""
# def lev(score):
#     """
#     根据传入的分数,计算对应的分数等级并返回。
#     :param score: 传入分数
#     :return:    分数等级
#     """
#     if score >= 90:
#         lev_off = 'A'
#     elif score >= 75:
#         lev_off = 'B'
#     elif score >= 60:
#         lev_off = 'C'
#     else:
#         lev_off = 'D'
#     return lev_off
# s = float(input("请输入分数:"))
# print(f"{s}对应的等级为:{lev(s)}")

# 2.定义一个函数,用于判断一个字符串是否是回文串,返回bool值。
# 把字符串反转,如果和原字符串相同,就是回文串。(如:"level","radar","黄山落叶松叶落山黄")
# def palindrome(input_str):
#     """
#     判断一个字符串是否是回文串
#     :param input_str: 输入的字符串
#     :return:    返回是否是回文
#     """
#     #获取字符串一半长度
#     half_len = len(input_str) // 2   #整除
#     #后半段切片取反,与前半段比较
#     if input_str[0:half_len] == input_str[-1:-half_len-1:-1]:
#         print(f"{input_str}是回文字符串")
#     else:
#         print(f"{input_str}不是回文字符串")
# s = input("请输入字符串:")
# palindrome(s)


# 3.定义一个函数:完成时间转换功能,将传入的秒转换为小时、分钟、秒。
# def time_ex(func):
#     """
#     将将传入的秒转换为小时、分钟、秒。
#     :param func: 传入秒数
#     :return: 转换后的时间
#     """
#     if func < 60:
#         print(f"{func}秒转化后是:{func}秒")
#     elif 60 <= func < 60 * 60:
#         mint = func // 60    #分
#         second = func % 60 #秒
#         print(f"{func}秒转化后是:{mint}分,{second}秒")
#     else:
#         hour = func // (60 * 60) #时
#         mint = func % (60 * 60) // 60  #分
#         second = func % 60 #秒
#         print(f"{func}秒转化后是:{hour}时{mint}分,{second}秒")
#
# time = float(input("请输入秒数:"))
# time_ex(time)

# 4.定义一个函数:根据传入的三角形三个边的边长,判定三角形的类型(等边、等腰、普通,或者不能构成三角形)。
def jud_tri(s):
    a, b, c = [float(i.strip()) for i in s.split(',') if i.strip()]
    if a <= 0 or b <= 0 or c <= 0:
        print("输入三角形三条边必须大于0")
        return
    if a+b > c and a+c > b and b+c > a:
        if a == b and b == c:
            print(f"{a},{b},{c}组成的是等边三角形")
        elif a == b or b == c or c == a:
            print(f"{a},{b},{c}组成的是等腰三角形")
        else:
            print(f"{a},{b},{c}组成的是普通三角形")
    else:
        print(f"{a},{b},{c}不能组成三角形")

s = input("请输入三角形三条边(用逗号隔开):")
jud_tri(s)