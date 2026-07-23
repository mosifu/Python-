# tuple元组：元素可以重复；有序；不可修改
# t1  = (1, 234, 2, 43, 23, '456', 2)
#
# print(t1)
# #类型
# print(type(t1))
#
# #索引访问
# print(t1[1])
#
# #切片
# print(t1[1::2])
#
# #.count(2)统计元素出现的次数
# print(t1.count(2))
#
# #.index(2)输出元素第一次出现的索引下标
# print(t1.index(2))
#
# #
# t2 = ()
# print(t2)
# print(type(t2))
# # 注意点：定义单个元素元组的时候,需要在单个元素后加逗号,不然相当于一个普通括号包裹住那个元素
# t3 = (100,)  #(100) --> type: int    (100,) --> type:tuple
# print(t3)
# print(type(t3))
#
# #-------- 元组的组包与解包 ------------
# #组包
# t_1 = (12, 213, 321, 124, 124, 12)
# t_2 = 12, 213, 321, 124, 124, 52, 123, 6
#
# print(t_1)
# print(t_2)
#
# #解包
# #基础解包:元素数量与容器元素数量一致,一对一赋值
# a, b ,c, d, e, f = t_1
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# #扩展解包(使用*收集剩余元素,组成list列表)
# first, second, *other = t_1
# print(first)
# print(second)
# print(other)
# *first_1, other_2 = t_2
# print(first_1)
# print(other_2)


# ----------------- 案例 ------------
#1.现有两个变量,分别为:a=10,b=20,现需要将这两个变量值交换,然后输出到控制台。
# a = 10; b = 20
# a, b = b, a #--> 使用元组组包操作 t = b,a; 然后在使用元组解包操作 a, b = t; --> 合并一下就是a, b = b, a
# print(a)
# print(b)
#
# #2.现有三个变量,分别为:a=100,b=200,c=300,现需要将这三个变量值进行交换,将a,b,c的值分别赋值给c,a,b,并将其输出到控制台。
# a = 100
# b = 200
# c = 300
# c, a, b = a, b, c
# print(a)
# print(b)
# print(c)

#-------------------- 练习 ---------------------
"""
根据提供的学生成绩单,完成如下需求:
1.计算每个学生的总分、三个科目平均分,然后一并输出出来。
2.统计各科成绩的最低分、最高分、平均分,并输出。
3.查找成绩优秀(平均分大于90)的学生,并输出。
"""
student_list = (
    ("S001", "王林", 85, 78, 92),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 82, 85),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

#1.计算每个学生的总分、三个科目平均分,然后一并输出出来。 ---->avg:.1f 保留一位小数
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方式一:
# for student in student_list:    #("S001", "王林", 85, 78, 92)
#     total = student[2] + student[3] + student[4]
#     avg = total / 3
#     print(f"{student[0]} \t {student[1]} \t {student[2]} \t {student[3]} \t {student[4]} \t {total} \t {avg:.1f}")
#方式二:用解包的形式来简化代码
for id, name, chinese, math, english in student_list:    #("S001", "王林", 85, 78, 92)
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")

#2.统计各科成绩的最低分、最高分、平均分,并输出。
chinese_score = [s[2] for s in student_list]
math_score = [s[3] for s in student_list]
english_score = [s[4] for s in student_list]
print(f"各科成绩最低分:\t {min(chinese_score)} \t {min(math_score)} \t {min(english_score)}")
print(f"各科成绩最高分:\t {max(chinese_score)} \t {max(math_score)} \t {max(english_score)}")
print(f"各科成绩平均分:\t {sum(chinese_score)/10:.1f} \t {sum(math_score)/10:.1f} \t {sum(english_score)/10:.1f}")

#3.查找成绩优秀(平均分大于90)的学生,并输出。
a_student =[]
for student in student_list:
    if (student[2] + student[3] +student[4]) / 3 > 90:
        a_student.append(student[1])
print("成绩优秀的学生(平均分大于90)有:", '\t'.join(a_student))