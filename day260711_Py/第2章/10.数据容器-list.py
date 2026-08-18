#列表操作
#定义列表 - list

# s = [1, 3, 4.5, 'hello', True]
#
# #获取类型
# print(type(s))
#
# #获取元素
# print(s[0])     #正向索引， 从0开始
# print(s[-5])    #反向索引， 从-1开始
#
# print(s[2])
# print(s[-3])
#
# #修改
# s[3] = "world"
# print(s)
#
# #如果修改的索引超出范围，将会报错IndexError: list assignment index out of range
# # s[10] = "hello, world"
# # print(s)
#
# #删除 - del关键字
# del s[2]
# print(s)
#
# #遍历
# for item in s:
#     print(item)
#
# #------------------- 列表操作 -----------------
# # 切片操作 h[开始索引:结束索引:步长]
# h = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# print(h[0:6:1])
# print(h[0:-4:1])
# print(h[:-4])
# print(h[1:-1:2])
#
# g = [56, 234, 634, 23, 63, 74, 211, 5]
#
# #.append()在列表后面添加元素
# g.append(78)
# print(g)
#
# #.insert(1, 78)在指定索引前加入该元素
# g.insert(1, 78)
# print(g)
#
# #.remove(78)移除第一个匹配到的元素
# g.remove(78)
# print(g)
#
# #.pop(1)删除指定索引的元素,如果未指定索引则删除列表最后一个元素
# g.pop(1)
# print(g)
# g.pop()
# print(g)
#
# #.sort()对列表进行排序(需要列表元素类型相同才可以)
# g.sort()
# print(g)
#
# #.reverse()反转列表元素
# g.reverse()
# print(g)

# ----------------- list案例 ---------------
# 1.将用户输入的10个数字,存储到一个列表中,并将其进行排序,输出其中最小值,最大值和平均值
# num_list = []
# #接受输入的数字
# for i in range(10):
#     num_list.append(int(input(f"请输入第{i+1}个数字:")))
#
# print(f"数字列表为:{num_list}")
# num_list.sort()
# print(f"排序后的列表:{num_list}")
# #输出数字
# print(f"列表最小值为:{num_list[0]};列表最大值为:{num_list[-1]}")
# #计算平均值 可以用sum()获取列表之和,用len()获取元素个数/列表长度
# """total = 0
# for num in num_list:
#     total += num
# print(f"列表平均值为:{total/num_list.__len__()}")"""
# print(f"列表平均值为:{sum(num_list)/len(num_list)}")

#2.合并两个列表中的元素,并对合并的结果进行去重处理
# num_list1 = [12, 24, 35, 12, 535, 125, 3]
# num_list2 = [121, 24, 25, 121, 55, 125, 3]
# #通过for循环添加
# for item in num_list2:
#     num_list1.append(item)
# print(f"合并之后的列表:{num_list1}")
# #列表去重
# num_list = []
# for i in num_list1:
#     if i not in num_list:
#         num_list.append(i)
# print(f"去重后的列表为:{num_list}")

#简化版本----利用Python的解包方式或者使用符号"+"
# num_list1 = [12, 24, 35, 12, 535, 125, 3]
# num_list2 = [121, 24, 25, 121, 55, 125, 3]
# #解包:将列表这一类容器解开成一个一个独立的元素
# #组包:将多个值合并到一个容器
# new_list = [*num_list1, *num_list2]
# # new_list = num_list1 + num_list2  #直接使用 + 号连接
# print(new_list)
# print(f"合并之后的列表:{new_list}")
# #列表去重
# num_list = []
# for i in new_list:
#     if i not in num_list:
#         num_list.append(i)
# print(f"去重后的列表为:{num_list}")
#
#
# #3.生成1-20的平方列表
# #方式一:传统方式
# nub_list = []
# for i in range(1, 21):
#     nub_list.append(i**2)
# print(f"1-20的平方列表为:{nub_list}")
# #方式二:列表推导式: 按照一定规则快速生成一个列表的方法 --> 语法格式1: [要插入的值 for i in 序列/列表]
# nub_list2 = [i**2 for i in range(1, 21)]
# print(f"采用列表推导式生成的平方列表:{nub_list2}")

#4.从输入的数字列表中提取所有偶数,并计算其平方,组成一个新的列表
# in_nub_list = list(map(int, input("请输入列表数字,使用逗号隔开:").split(",")))
# nub2list =[]
# nub2list_2 = []
# for item in in_nub_list:
#     if item % 2 == 0:
#         nub2list.append(item)
#         nub2list_2.append(item**2)
# print(f"组成的新偶数列表为:{nub2list}")
# print(f"组成的新偶数列表平方为:{nub2list_2}")

#使用列表推导式来实现
# in_nub_list = list(map(int, input("请输入列表数字,使用逗号隔开:").split(",")))
# #方式二:列表推导式: 按照一定规则快速生成一个列表的方法 --> 语法格式2: [要插入的值 for i in 序列/列表 if 条件]
# print(f"组成的偶数列为:{[i for i in in_nub_list if i % 2 == 0]}")
# nub2list_2 =[i**2 for i in in_nub_list if i % 2 == 0]
# print(f"组成的新偶数列表平方为:{nub2list_2}")

# -------------------- list练习 --------------
#1.将下列多个列表合并为一个列表,并去除重复元素,按升序排好后输出到控制台
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'O']
# list2 = ['Q', 'M', 'A', 'S', 'Y', 'Z', 'P']
# list3 = ['W', 'X', 'N', 'D']
# new_list = list1 + list2 + list3
# list = []
# for i in new_list:
#     if i not in list:
#         list.append(i)
# print(f"合并去重排序后的列表为:{sorted(list)}")

#2.将如下列表中能被3或5整除的元素提取出来,并获取这些数字对应的平方,组成一个新的列表
# list1 = list(range(1,31))
# new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(f"提取出能被3或5整除的元素,并获取数字对应的平方组成的新列表为:{new_list}")

#3.将如下列表中的正数提取出来,封装为一个新的列表
list2 = [11, 21, -11, 1231, -34, 10, 35, -111, -2134]
new_list = [i for i in list2 if i > 0]
print(f"提取出正数组成的新列表为:{new_list}")