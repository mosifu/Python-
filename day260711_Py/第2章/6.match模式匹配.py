#match...case 模式匹配
# day = input("请输入星期几(1-7):")
# match day:
#     case "1":
#         print("星期一,上班日")
#     case "2":
#         print("星期二,项目日")
#     case "3":
#         print("星期三,研发日")
#     case "4":
#         print("星期四,研讨日")
#     case "5":
#         print("星期五,摸鱼日")
#     case "6" | "7":
#         print("周末,休息日")
#     case _:
#         print("输入日期不存在")

#基于match...case实现一个计算器,实现+ - * / 运算,用户输入要运算的两个数以及运算符之后进行运算
# a = int(input("请输入计算的第一个数字:"))
# b = int(input("请输入计算的第二个数字:"))
# c = input("请输入需要实现的计算(+-*/):")
# match c:
#     case "+":
#         print(f"实现加法运算:{a} + {b} = {a+b}")
#     case "-":
#         print(f"实现减法运算:{a} - {b} = {a-b}")
#     case "*":
#         print(f"实现乘法运算:{a} * {b} = {a*b}")
#     case "/" if b != 0: #0 不能做除数,需条件成立才会匹配(if... |  _Python3.10的新语法)
#         print(f"实现除法运算:{a} / {b} = {a/b}")
#     case _:
#         print(f"无符合的运算符{c}")

"""
请你编写一个游戏角色移动控制系统,根据玩家输入的不同指令,控制游戏角色执行相应的动作(输出控制台)。
具体规则:
玩家输入                    对应动作
上/w/W                    角色向上移动
下/s/S                    角色向下移动
左/a/A                    角色向左移动
右/d/D                    角色向右移动
跳/" "(空格)               角色跳跃
攻击/j/J                  角色发动攻击
退出/esc/ESC              角色退出游戏
"""
move = input("请输入指令操控角色移动:")
match move:
    case "w" | "上" | "w":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左" | "a" | "A":
        print("角色向左移动")
    case "右" | "d" | "D":
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "j" | "J":
        print("角色发动攻击")
    case "退出" | "esc" | "ESC":
        print("角色退出游戏")
    case _:
        print("错误指令")
