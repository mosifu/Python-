# 字典 --- key不能重复(如果重复,后面的值会覆盖前面的值)
#定义
# dict1 = {"mosifu":688, "jianl":334, "mo":666}
#
# print(dict1)
# print(type(dict1))
#
# #字典key必须是不可变类型(int, str, float, tuple), 不能是list, set, dict
# dict2 = {0:123, 1.3:444, (1,2):666, ('A','B'):777}
# print(dict2)
# print(type(dict2))
#
# #访问
# print(dict1["mosifu"])  #获取
# dict1["jianl"] = 888    #修改
# print(dict1)
#
# # ------------ dict常用方法
# dict3 = {"莫":444, "简":888, "兰":777, "爱":666}
# print(dict3)
#
# #字典中不存在的话就是添加操作
# dict3["你好"] = 350
# print(dict3)
#
# #字典中存在就是修改操作
# dict3["你好"] = 600
# print(dict3)
#
# #查询
# print(dict3["简"])   #根据key获取value
# print(dict3.get("简"))   #根据key获取value
#
# print(dict3.keys())     #获取字典里所有key  ---dict_keys(['莫', '简', '兰', '爱', '你好'])
# print(dict3.values())   #获取字典里所有value ---dict_values([444, 888, 777, 666, 600])
# print(dict3.items())    #获取字典里所有键值对 ---dict_items([('莫', 444), ('简', 888), ('兰', 777), ('爱', 666), ('你好', 600)])
#
# #删除
# e = dict3.pop("简")
# print(e)
# print(dict3)
#
# del dict3["兰"]
# print(dict3)
#
# #遍历
# #方式一
# for k in dict3.keys():
#     print(f"{k}:{dict3[k]}")
#
# #方式二:
# for k,v in dict3.items():
#     print(f"{k}:{v}")


# ------------------------- 案例 ------------------
"""
    开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据,
    通过控制台菜单与用户交互。具体功能如下:
    1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
    2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
    3.删除购物车:要求用户输入要删除的购物车名称,根据名名称删除购物车中的商品。
    4.查询购物车:将购物车中的商品信息展示出来,格式为:"商品名称:xxx,商品价格:xxx,商品数量:xxx"。
    5.退出购物车
    存储结构 = {'name' : {'price' : ... ,'num' : ...}, }

"""

#制作一个菜单
# str1 = """
# ######## 欢迎来到购物车系统 ###########
# #           1.添加购物车            #
# #           2.修改购物车            #
# #           3.删除购物车            #
# #           4.查询购物车            #
# #           5.退出购物车            #
# ###################################
# """
# print(str1)
# shop_dict = dict()
# while True:
#     s = input("请输入需要执行的操作数字(1-5):")
#     match s:
#         case '1':   #添加购物车操作
#             name = input("请输入需要录入的商品名称:")
#             # 判断商品是否存在
#             if name in shop_dict.keys():
#                 print(f"{name}该商品已存在!,请选择其他操作")
#                 continue
#             price = float(input("请输入需要录入的商品价格:"))
#             num = int(input("请输入需要录入的商品数量:"))
#             shop_dict[name] = {"price" : price, "num" : num}
#             print(f"添加商品成功:{name},价格:{price},数量:{num}")
#         case '2':
#             name = input("请输入需要修改的商品名称:")
#             #判断需要修改的商品是否存在
#             if name not in shop_dict.keys():
#                 print(f"{name}该商品不存在!请选择其他操作")
#                 continue
#             price = input("请输入需要修改的商品价格:")
#             num = input("请输入需要修改的商品数量:")
#             shop_dict[name] = {"price": price, "num": num}
#             print(f"修改商品成功:{name},价格:{price},数量:{num}")
#         case '3':
#             name = input("请输入需要删除的商品名称:")
#             #判断商品是否存在
#             if name not in shop_dict.keys():
#                 print(f"{name}该商品不存在!请选择其他操作")
#             else:
#                 e = shop_dict.pop(name)
#                 print(f"删除{name}商品成功")
#         case '4':
#             print("当前购物车中商品信息为:")
#             for k, v in shop_dict.items():
#                 print(f"商品名称:{k},商品价格:{v["price"]}商品数量:{v["num"]}")
#         case '5':
#             break
#         case _:
#             print("未知操作,请重试")



"""
    开发一个教务管理系统,在该系统中可以维护和管理学员的成线债息,具体需求如下:
    1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩,录入完成保存到系统中。
    2.修改学生信息:要求输入要修改的学生姓名,然后再提示输入语文、数学、英语成绩,输入完成后修改学员信息。
    3.删除学生信息:要求输入要删除的学生姓名,根据姓名删除学生信息。
    4.查询学生信息:要求输入要查询的学生姓名,根据姓名查查询学生信息并输出。
    5.列出所有学生:遍历所有学生信息并输出。
    6.统计班级成绩:统计班级语文、数学、英语成绩的最高分分、最低分、平均分,以及语文、数学、英语最高分和最低分的学
    员姓名。
    7.退出系统。
"""
#先设置菜单
menu = """
# # # # # # # # # # # # # # # # # # # # #[菜单]# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 1.添加学生信息  2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有信息    6.统计班级成绩    7.退出系统 #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
"""
stu_mes = dict()
while True:
    print(menu)
    s = input("请输入需要进行的操作(1-7):")
    match s:
        case '1':   #1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩,录入完成保存到系统中。
            print("添加学生信息:")
            stu_name = input("请输入学生姓名:")
            #判断学生是否存在
            if stu_name in stu_mes.keys():
                print(f"{stu_name}该学生已存在!请选择其他操作")
                continue
            chinese_sc = float(input("请输入学生语文成绩:"))
            math_sc = float(input("请输入学生数学成绩:"))
            english_sc = float(input("请输入学生英语成绩:"))

            stu_mes[stu_name] = {"chinese":chinese_sc, "math":math_sc, "english":english_sc}
            print(f"添加{stu_name}学生信息成功!语文{chinese_sc}分,数学{math_sc}分,英语{english_sc}分")

        case '2':   #2.修改学生信息:要求输入要修改的学生姓名,然后再提示输入语文、数学、英语成绩,输入完成后修改学员信息。
            print("修改学生信息:")
            stu_name = input("请输入需要修改信息的学生姓名:")
            # 判断学生是否存在
            if stu_name not in stu_mes.keys():
                print(f"{stu_name}该学生不存在!请选择其他操作")
                continue
            chinese_sc = float(input("需要修改的语文成绩:"))
            math_sc = float(input("需要修改的数学成绩:"))
            english_sc = float(input("需要修改的英语成绩:"))

            stu_mes[stu_name] = {"chinese": chinese_sc, "math": math_sc, "english": english_sc}
            print(f"修改{stu_name}学生信息成功!语文{chinese_sc}分,数学{math_sc}分,英语{english_sc}分")
        case '3':   #3.删除学生信息:要求输入要删除的学生姓名,根据姓名删除学生信息。
            print("删除学生信息:")
            stu_name = input("请输入需要删除信息的学生姓名:")
            # 判断学生是否存在
            if stu_name not in stu_mes.keys():
                print(f"{stu_name}该学生不存在!请选择其他操作")
                continue
            del stu_mes[stu_name]
            print(f"删除{stu_name}学生的信息成功")

        case '4':   #4.查询学生信息:要求输入要查询的学生姓名,根据姓名查查询学生信息并输出。
            print("查询学生信息:")
            stu_name = input("请输入需要查询的学生姓名:")
            # 判断学生是否存在
            if stu_name not in stu_mes.keys():
                print(f"{stu_name}该学生不存在!请选择其他操作")
                continue
            print(f"查询{stu_name}学生信息成功!语文{stu_mes[stu_name]['chinese']}分,数学{stu_mes[stu_name]['math']}分,英语{stu_mes[stu_name]['english']}分")

        case '5':   #5.列出所有学生:遍历所有学生信息并输出。
            print("查询所有学生信息:")
            for k,v in stu_mes.items():
                print(f"学生{k}的成绩为:语文:{v['chinese']},数学:{v['math']},英语:{v['english']}")

        case '6':   #6.统计班级成绩:统计班级语文、数学、英语成绩的最高分分、最低分、平均分,以及语文、数学、英语最高分和最低分的学员姓名。
            print("统计全班信息:")
            chinese_all = sum(stu_mes[k]["chinese"] for k in stu_mes.keys())  #语文总分
            chinese_avg = chinese_all / len(stu_mes.keys())
            chinese_min = min(stu_mes[k]["chinese"] for k in stu_mes.keys())  #语文最低分
            chinese_max = max(stu_mes[k]["chinese"] for k in stu_mes.keys())  #语文最高分
            ch_min_stu = [name for name in stu_mes if stu_mes[name]["chinese"] == chinese_min]  #语文成绩最低的学生
            ch_max_stu = [name for name in stu_mes if stu_mes[name]["chinese"] == chinese_max]  #语文成绩最高的学生
            print(f"该班级语文平均分为:{chinese_avg:.1f};最高分为:{chinese_max},对应学生为:{ch_max_stu};最低分为:{chinese_min},对应学生为:{ch_min_stu}")

            math_all = sum(stu_mes[k]["math"] for k in stu_mes.keys())  #数学总分
            math_avg = math_all / len(stu_mes.keys())                   #数学平均分
            math_min = min(stu_mes[k]["math"] for k in stu_mes.keys())  #数学最低分
            math_max = max(stu_mes[k]["math"] for k in stu_mes.keys())  #数学最高分
            math_min_stu = [name for name in stu_mes if stu_mes[name]["math"] == math_min]  #数学成绩最低的学生
            math_max_stu = [name for name in stu_mes if stu_mes[name]["math"] == math_max]  #数学成绩最高的学生
            print(f"该班级数学平均分为:{math_avg:.1f};最高分为:{math_max},对应学生为:{math_max_stu};最低分为:{math_min},对应学生为:{math_min_stu}")

            english_all = sum(stu_mes[k]["english"] for k in stu_mes.keys())  #语文总分
            english_avg = english_all / len(stu_mes.keys())
            english_min = min(stu_mes[k]["english"] for k in stu_mes.keys())  #英语最低分
            english_max = max(stu_mes[k]["english"] for k in stu_mes.keys())  #英语最高分
            eng_min_stu = [name for name in stu_mes if stu_mes[name]["english"] == english_min]  #英语成绩最低的学生
            eng_max_stu = [name for name in stu_mes if stu_mes[name]["english"] == english_max]  #英语成绩最高的学生
            print(f"该班级英语平均分为:{english_avg:.1f};最高分为:{english_max},对应学生为:{eng_max_stu};最低分为:{english_min},对应学生为:{eng_min_stu}")

        case '7':   #7.退出系统
            break

        case _:
            print("非法操作!")