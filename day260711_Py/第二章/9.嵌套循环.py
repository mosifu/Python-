#嵌套循环: 打印输入长度为m,宽度为n的长方形
#print("*"):输出自带换行效果,每次输出都是新的一行*
#print("*", end = ""):end表示每一次输出以什么结束,默认是\n(换行符)
# m = int(input("输入长度为m:"))
# n = int(input("输入宽度为n:"))
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print("*", end="")
#     print()


#嵌套循环案例: 打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{i}×{j}={i*j}", end="\t")
#     print()


#嵌套循环练习: 根据输入的直角边的边长,打印等腰直角三角形
# i = int(input("请输入直角边的边长:"))
# for a in range(1,i+1):
#     for b in range(1,a+1):
#         print("*",end=" ")
#     print()

#嵌套循环练习: 根据输入的数字,打印对应的数字金字塔
# i = int(input("请输入数字:"))
# for a in range(1,i+1):
#     for b in range(1,a+1):
#         print(f"{b}",end=" ")
#     print()

#嵌套循环练习: 打印黑白格的国际象棋棋盘
# i = int(input("请输入需要打印的棋盘边长:"))
# for c in range(1,i+1):
#     for b in range(1,i+1):
#         if c % 2 ==1:
#             if b % 2 ==1:
#                 print("⬛",end="")
#             else:
#                 print("⬜", end="")
#         else:
#             if b % 2 ==0:
#                 print("⬛", end="")
#             else:
#                 print("⬜",end="")
#     print()


"""
    需求:根据输入的用户名密码执行登录操作,具体要求如下:
    1.正确的用户名和密码为admin/6668888、zhangsan/123456taoge/8886666
    2.输入用户名和密码进行登录,直到登录成功,程序结束运行;如果登录失败,则继续输入用户名和密码进行登录
    3.输入的用户名和密码不能为空!
    4.登录成功:输出"登录成功,进入B站首页~"
    5.登录失败:输出"用户名或密码错误,请重新输入!"

    关键字:
        break:跳出循环,while后面的else语句不会被执行
        continue:中断本次循环,进入下一次循环

"""
# while True:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#
#     if username == "" or password == "":
#         print("输入的用户名和密码不能为空,请重新输入!")
#         continue
#
#     if username == "admin" and password == "666888":
#         print("登录成功,进入B站首页~")
#         break
#     if username == "zhangsan" and password == "123456":
#         print("登录成功,进入B站首页~")
#         break
#     if username == "taoge" and password == "886666":
#         print("登录成功,进入B站首页~")
#         break
#
#     print("用户名或密码错误,请重新输入!")


"""
    1.系统随机生成一个随机数
    2.用户根据提示猜数字,并将所猜的数字输入系统
    3.如果猜错,系统给出提示是猜大了,还是猜小了,然后继续输入猜的数字
    4.如果猜对,系统自动退出,游戏结束
"""
# import random
#
# random_number = random.randint(1,100)
# while True:
#     num = int(input("请输入预测的数字:"))
#     if num > random_number:
#         print("数字猜大了!")
#     elif num < random_number:
#         print("数字猜小了!")
#     else:
#         print("猜对了~")
#         break
# print(f"随机数字为:{random_number}")


# 将1-1000之间所有5的倍数的数字累加起来
# num = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#        num += i
# print(f"1-1000之间所有5的倍数的数字和为{num}")

#统计随机输入的字符串中有多少个a和k
input_str = input("请输入随机的字符串:")
num_a = num_k = 0
for i in input_str:
    if i == 'a':
        num_a += 1
    elif i == 'k':
        num_k += 1
print(f"输入字符串{input_str}中,有{num_a}个'a',{num_k}个'k'")
