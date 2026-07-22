#常见数据类型,使用type()来获取指定字面量和变量对应值的数据类型
# print("Hello World")
# print(type("Hello World")) #str
# print(type(100)) #int
# print(type(3.14)) #float
# print(type(True)) #bool
# print(type(False)) #bool
#定义一个变量
# num = "Hello World"
# print(type(num)) #str

#常见数据类型,使用isinstance()来判断数据是否是指定的数据类型;是->True, 否->False
# print(isinstance(num, str)) #True
# print(isinstance(num, int)) #False
# print(isinstance(num, float)) #False
#
# s1 = 'hello'
# s2 = "Python"
# s3 = """
# Hello World:
#     this is Python World
# """
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))


# \' \" \n \t 都是转义字符
# msg1 = 'It\'s a good day.'
# print(msg1)
# msg2 = 'Hello的意思是:"你好"'
# print(msg2)
# print("你好世界,\n\t欢迎来到Python的世界") #\n 换行,  \t制表符,缩进

# 字符串拼接(变量拼接用 + 号, 只能拼接字符串)
m1 = "气温二十一度" '刚好又是花季' """适合出去玩"""
print(m1)
m2 = "你要出去吗?"
print("今天星期二 , " + m1 +" , " + m2)

name = "mo_sifu"
age = 23
professional = "AI"
hobby = "run"
print("大家好, 我是" + name +", 今年" + str(age) + "岁, 学习的专业是" + professional + ", 爱好是" + hobby)
#字符串格式化,用%s占位符来替代 ----方式一
print("大家好, 我是%s, 今年%s岁, 学习的专业是%s, 爱好是%s" % (name, age, professional, hobby))
#方式二 ---f"...{变量名/表达式}..."
print(f"大家好, 我是{name}, 今年{age}岁, 学习的专业是{professional}, 爱好是{hobby}")
