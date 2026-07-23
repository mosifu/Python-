# set集合: 无序,不可重复,可修改
#定义
# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4}
# print(s1)
# print(type(s1))
# #定义空集合要使用set();单纯使用{}是定义字典
# s2 = {}
# print(type(s2))
#
# s3 = set()
# print(type(s3))

#----------- 集合常用方法 -------------
# s4 = {100, 200, 300, 400, 500}
# print(s4)
#
# #.add(800):添加元素到集合
# s4.add(800)
# print(s4)
#
# #.remove(100):移除集合中的指定元素(指定元素不存在将报错)
# s4.remove(100)
# print(s4)
#
# #.pop():随机删除集合中的元素,并返回
# e = s4.pop()
# print(e)
# print(s4)
#
# #.clear():清空集合
# s4.clear()
# print(s4)
#
# s5 = {'A', 'B', 'C', 'D', 'E', 'F'}
# s6 = {'B', 'C', 'G', 'H', 'I', 'J'}
#
# #.difference(s6):两个集合的差集(存在于前面一个集合,但不存在后面那个集合中的)
# print(s5.difference(s6))
# print(s6.difference(s5))
#
# #.union(s6):两个集合的并集
# print(s5.union(s6))
# print(s6.union(s5))
#
# #.intersection(s6):两个集合的交集
# print(s5.intersection(s6))
# print(s6.intersection(s5))


# ---------------- set案例 -----------------
"""
根据提供的班级学生的选课情况,完成如下需求:
1.找出同时选修了法语和艺术的学生
2.找出同时选修了所有四门课程的学生
3.找出选修了足球,但是没有选修篮球的学生
4.统计每一个学生选修的课程数量
"""
#选修足球学生名单
football_set={"王林","普牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","普牛"}
#选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#1.找出同时选修了法语和艺术的学生
french_art_set= french_set.intersection(art_set)
print("同时选修了法语和艺术的学生:",'\t'.join(french_art_set))
#方式二:使用&进行交集运算
french_art_set2= french_set & art_set
print("同时选修了法语和艺术的学生:",'\t'.join(french_art_set2))

#2.找出同时选修了所有四门课程的学生
all_set = football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)
print(f"同时选修所有四门课程的学生有:{all_set}")
#方式二: &
all_set2= football_set & basketball_set & french_set & art_set
print(f"同时选修所有四门课程的学生有:{all_set2}")

#3.找出选修了足球,但是没有选修篮球的学生
foot_ex_bask_set = football_set.difference(basketball_set)
print(f"选修了足球,但是没有选修篮球的学生:{foot_ex_bask_set}")
#方式二: -  利用减号运算符来求差集
foot_ex_basket_set2 = football_set - basketball_set
print(f"选修了足球,但是没有选修篮球的学生:{foot_ex_basket_set2}")
#方式三:集合推导式 -->集合 = {要存入集合的元素 for 元素 in 集合 if 条件判断}
foot_ex_basket_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球,但是没有选修篮球的学生:{foot_ex_basket_set3}")

#4.统计每一个学生选修的课程数量
#先统计学生名单    可以使用并集或者是 | 竖线符号代替  会去重
all_stu_set = football_set | basketball_set | french_set | art_set

#统计每个学生的选修课程
all_list = [*football_set, *basketball_set, *french_set, *art_set]  #使用*解包操作,并放入list列表中允许重复
for stu in all_stu_set:
    print(f"{stu}选修的课程数量为:{all_list.count(stu)}")