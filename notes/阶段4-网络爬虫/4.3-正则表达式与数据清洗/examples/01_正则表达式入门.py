# 生成时间: 2026-08-23
# 来源：学习者跟练代码（第4章/7.正则表达式入门.py）
# 知识点：re.match / re.search / re.findall 三大函数、r 原始字符串
# 说明：纯本地练习，无需联网

import re

s1 = "18809090000是我的手机号,你记住了吗?我的的另一个手机号是1880008888,两个QQ号分别是1559998992 和 18809091293821 你记住了吗?"
s2 = "我的手机号是18809090000,你记住了吗?我的另一个下手机号是18800008888,两个Q号分别是155998992和18809091293821你记住了吗?"

# ----------------------
# 1. re.match 只匹配字符串开头（s1开头刚好是手机号，s2开头不是）
# ----------------------
pattern_phone = r"1[3-9]\d{9}"  # r用来表示字符串里面的转义字符\无效,仅作为普通字符串

print("===== re.match 测试 s1 =====")
result = re.match(pattern_phone, s1)
if result:
    print("匹配内容：", result.group())
    print("索引区间：", result.span())
    print("起始索引：", result.start())
    print("结束索引：", result.end())
else:
    print("match未匹配到")

print("\n===== re.match 测试 s2 =====")
result2 = re.match(pattern_phone, s2)
if result2:
    print("匹配内容：", result2.group())
else:
    print("match未匹配到（s2开头不是手机号）")

# ----------------------
# 2. re.search：查找字符串里第一个符合的手机号（不限开头）
# ----------------------
print("\n===== re.search 查找第一个手机号 =====")
res_search = re.search(pattern_phone, s2)
if res_search:
    print("s2第一个手机号：", res_search.group())
    print(res_search.span())

# ----------------------
# 3. re.findall：提取全部手机号
# ----------------------
print("\n===== findall 提取全部手机号 =====")
all_phone_s1 = re.findall(pattern_phone, s1)
all_phone_s2 = re.findall(pattern_phone, s2)
print("s1所有手机号：", all_phone_s1)
print("s2所有手机号：", all_phone_s2)

# ----------------------
# 4. 提取QQ号示例
# ----------------------
pattern_qq = r"\d{5,11}"
all_qq_s1 = re.findall(pattern_qq, s1)
print("\ns1提取到数字(包含QQ)：", all_qq_s1)
