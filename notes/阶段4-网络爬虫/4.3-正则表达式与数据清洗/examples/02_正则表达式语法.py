# 生成时间: 2026-08-23
# 来源：学习者跟练代码（第4章/8.正则表达式语法.py）
# 知识点：量词 * ? +、\d{n}、字符集 [38]、^$、\w、分组 ()
# 说明：纯本地练习，无需联网

import re
s1 = "18809090000是我的手机号,188开头的,以00结尾的;我的另一个手机号是15500008888,两个Q号分别是1259989092和138099091293821,邮箱为python666@163.com"
#正则表达式
# print(re.findall(r"188.*", s1)) # * 匹配任意个
# print(re.findall(r"188.?", s1)) # ? 匹配0个或1个(最多出现一次)
# print(re.findall(r"188.+", s1)) # + 匹配1个或者多个(最少出现一次)

# print(re.findall(r"188\d{8}", s1))  # \d{8} 后面有8位数字
# print(re.findall(r"155\d{6,10}", s1))   # \d{6,10} 后面有6到10位数字
# print(re.findall(r"155\d{6,}", s1)) # \d{6,} 至少有6位数字

# print(re.findall(r"1[38]\d{8}", s1))    # [38] 匹配的第二位是3或8
# print(re.findall(r"1[^38]\d{8}", s1))   # [^38] 匹配的第二位是非 3或8
# print(re.findall(r"1[3-9]\d{8}", s1))   # [3-9] 匹配范围为3到9
# print(re.findall(r"^1[3-9]\d{9}", s1))  # ^ 从字符串开头开始匹配
# print(re.findall(r"^1[3-9]\d{9}$", s1)) # $ 字符串结尾匹配

# print(re.findall(r"\w+@\w+\.\w+", s1))  # \w 表示匹配任意单词字符[a-zA-Z0-9_以及中文等]
# print(re.findall(r"\w+@\w+\.\w+", s1, re.ASCII))  # re.ASCII 只匹配ASCII码表中的单词字符(a-zA-Z0-9_)


s2="现在的时间是2026年-02月-06日 10h:05m:25s,今天的天气还可以,气温是28度"
print(re.findall(r"\d{4}-\d{2}-\d{2}", s2))
print(re.findall(r"(\d+)h:(\d+)m:(\d+)s",s2))    # ()将捕获的分组组合成元组放在返回的列表中
print(re.search(r"(\d+)h:(\d+)m:(\d+)s",s2).group(3))
