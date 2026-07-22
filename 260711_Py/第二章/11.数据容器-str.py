# str字符串 基本操作 ---> 不可变(无法修改),有序性,可迭代(能循环)
# str1 = "Hello-Python"
#
# #取值
# print(str1[0])
# print(str1[-1])
#
# #切片
# print(str1[0:5])
# print(str1[:5])
# print(str1[-1:-7])
# print(str1[::2])
# #可以设置步长为负数,但是要和前面的开始索引指向结束索引的方向一致.如[0:2:1];[-1:-7:-1]
# print("------------")
# print(str1[0:5:-1]) #错误示范,不显示值
# print(str1[0:5:1])
# print(str1[-8:-13:-1]) #步长是负的会从开始索引倒着数
# print(str1[0::-1]) #省略 stop 时，不是默认指向末尾，而是默认指向“路径终点：正步长路径终点在末尾右侧，负步长路径终点在开头左侧。

#------------------ str常用方法 -----------------
# str2 = "  Hello-Python-Hello-World  "
#
# #.find("Hello")查找指定字符串第一次出现的索引下标
# s1 = str2.find("Hello")
# print(s1)
#
# #.count("Hello")统计指定字符串出现的次数
# s2 = str2.count("Hello")
# print(s2)
#
# #.split()按照指定字符串进行切割,形成列表
# s3 = str2.split('-')
# print(s3)
#
# #.upper()字符串转大写
# s4 = str2.upper()
# print(s4)
#
# #.lower()字符串转小写
# s5 = str2.lower()
# print(s5)
#
# #.strip()去除字符串两边的空格
# s6 = str2.strip()
# print(s6)
#
# #.startswith()/.endswith("Python")判断字符串是否以某字符串开头或结尾,返回布尔值
# s7 = str2.startswith(" ")
# print(s7)
# s8 = str2.endswith("Python")
# print(s8)
#
# #.replace("-", "_") 字符串替换
# s9 = str2.replace("-", "_")
# print(s9)
# print("-----------------")
# print(str2) #原始字符串不变

# ------------------- 案例 ---------------
#1.邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.),如果输入正确,输出"邮箱格式正确",否则输出"邮箱格式错误"。
# email = input("请输入一个邮箱:")
# #for循环遍历邮箱
# num_a = 0
# num_b = 0
# for i in email:
#     if i == "@":
#         num_a += 1
#     elif i == ".":
#         num_b += 1
# if num_a == 1 and num_b >= 1:
#     print("邮箱格式正确~")
# else:
#     print("邮箱格式错误!")

# 方式2:使用count()统计出现次数.使用in判断是否存在
# email = input("请输入一个邮箱:")
# if email.count("@") == 1 and '.' in email:
#     print("邮箱格式正确~")
# else:
#     print("邮箱格式错误!")

#2.输入一个字符串,判断该字符串是否是回文(两边对称)。
"""黄山落叶松叶落山黄
上海自来水来自海上"""
# input_str = input("请输入需要判断的字符串:")
# len_str = len(input_str)    #获取字符串长度
# if input_str[0 : len_str % 2] == input_str[-1 : -(len_str % 2) -1 : -1]:   #len_str % 2取长度中间值,输出前半段的字符串,后半段通过切片取反得到
#     print(f"字符串:'{input_str}'回文~")
# else:
#     print(f"字符串:'{input_str}'不回文~")


#3.将用户输入的10个字符串,反转后全部转换为大写,然后记录是在列表中,最后将列表内容,遍历输出出来。
input_str =[]
for i in range(10):
    str_i = input(f"请输入第{i+1}个字符串:")
    re_str_i = str_i[::-1].upper()  #切片反转并大写
    input_str.append(re_str_i)      #记录在列表中
for item in input_str:
    print(item)