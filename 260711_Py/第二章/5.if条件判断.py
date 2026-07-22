# if条件判断： 如果分数超过680，我就去读清华
# score = 689
# if score > 680:
#     print("我去读清华")
#     print("超过680的都来读清华")
# print("-------------")

#案例： 使用if判断完成B站登录功能（正确账号密码：188888888/6666666）
# #定义正确账号密码
# right_account = "188888888"
# right_password = "6666666"
# #接受输入
# account = input("请输入B站账户:")
# password = input("请输入密码:")
# if account == right_account and password == right_password:
#     print("账户密码正确!!")
#     print("欢迎登录!!")
# if account != right_account or password != right_password:
#     print("账户或密码错误!!")
#     print("无法登录!!")

#案例进阶: 通过if...else...来判断登录
#定义正确账号密码
# right_account = "188888888"
# right_password = "6666666"
# #接受输入
# account = input("请输入B站账户:")
# password = input("请输入密码:")
# if account == right_account and password == right_password:
#     print("账户密码正确!!")
#     print("欢迎登录!!")
# else:
#     print("账户或密码错误!!")
#     print("无法登录!!")


#案例: 根据用户输入的年份,判断这一年是闰年还是平年(非正白年,且能被4整除的年份是闰年;整百年必须能被400整除才是闰年|)
# year = int(input("请输入一个年份:"))
# if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

#练习1: 根据用户输入的数字,判断数字是奇数还是偶数
# nub = int(input("请输入需要判断的数字:"))
# if nub % 2 == 0:
#     print(f"{nub}是偶数!")
# else:
#     print(f"{nub}是奇数")

#练习2: 根据用户输入的年龄,判断该用户是否已经成年(>=18,成年;否则,未成年)
# age = int(input("请输入年龄:"))
# if age >= 18:
#     print("该用户已成年")
# else:
#     print("该用户未成年")

#练习3: 根据用户输入的数字,判断该数字是正数还是负数(不考虑0)
# nub = int(input("请输入需要判断的数字:"))
# if nub > 0:
#     print(f"{nub}是正数")
# else:
#     print(f"{nub}是负数")

#练习3(考虑0)
# nub = int(input("请输入需要判断的数字:"))
# if nub > 0:
#     print(f"{nub}是正数")
# elif nub <0:
#     print(f"{nub}是负数")
# else:
#     print(f"{nub}既不是正数也不是负数")

#练习4: 根据用户输入的考试分数,判断是否及格(大于等于60就是及格)
# score = int(input("请输入考试分数:"))
# if score >= 60:
#     print("考试及格!!")
# else:
#     print("考试不及格!")

#案例: 根据用户输入用户名,密码进行登录(用户名/密码为:admin/666888或root/12345或mosifu/666)
# account = input("请输入用户名:")
# password = input("请输入密码:")
# if account == "admin" and password == "666888":
#     print("登录成功!")
# elif account == "root" and password == "12345":
#     print("登录成功!")
# elif account == "mosifu" and password == "666":
#     print("登录成功!")
# else:
#     print("用户名或密码错误")


#练习: 根据成绩输入,判断成绩等级(大于等于85分为优秀;60-85分为及格;否则就是不及格)
# score = int(input("请输入考试成绩:"))
# if score >= 85:
#     print("成绩为优秀!")
# elif 60 <=score < 80:
#     print("成绩为及格!")
# else:
#     print("成绩不及格")

#练习: 根据输入购物车的商品总额,以及如下折扣规则,计算实际应付的金额(金额 >= 500:8折;300<=金额<500:9折;100<=金额<300:95折;金额<100:无折扣)
# money = int(input("请输入商品总额:"))
# if money >= 500:
#     print(f"实付金额为:{money*0.8}")
# elif 300<= money < 500:
#     print(f"实付金额为:{money*0.9}")
# elif 100<= money < 300:
#     print(f"实付金额为:{money*0.95}")
# else:
#     print(f"实付金额为:{money}")

#案例: 三角形类型判断:根据输入的三条边的边长(正整数),判断是等边三角形,等腰三角形,普通三角形,还是不能构成三角形
#三角形构成条件:两边之和大于等于第三边
# nums = input("请输入三角形的三条边(用空格隔开):").strip()
# a, b, c = map(int, nums.split())
# # pass 表示空语句
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print(f"{a},{b},{c}该三角形是等边三角形")
#     elif a == b or b == c or a == c:
#         print(f"{a},{b},{c}该三角形是等腰三角形")
#     else:
#         print(f"{a},{b},{c}该三角形是普通三角形")
# else:
#     print(f"{a},{b},{c}不能组成三角形")

#练习: 根据输入的用电数,计算阶梯电费(2880度一下,电费单价0.4883元/度;2880-4800度,电费单价0.5383元/度;4800度以上,电费单价0.7883元/度)
total = int(input("请输入用电数:"))
if total < 2880:
    print(f"{total}度电,电费为{total*0.4883}")
elif 2880 <= total <= 4800:
    print(f"{total}度电,电费为{2880*0.4883+(total-2880)*0.5383}")
elif 4800 < total:
    print(f"{total}度电,电费为{2880*0.4883+(4800-2880)*0.5383+(total-4800)*0.7883}")