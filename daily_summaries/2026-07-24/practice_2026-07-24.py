"""
practice_2026-07-24.py
今日练习：tuple / set / dict + 综合案例
课程：阶段2.3 第47-55集
生成时间：2026-07-24

使用方式：在 Python 交互式环境或 IDE 中逐段解开注释运行
"""

# ============================================================
# 练习1：tuple 元组 —— 组包与解包
# ============================================================
"""
题目：有两个列表 china 和 usa 分别存储两组成绩，
请将两组数据交错合并成一个元组列表。

要求：
1. 用 zip() 组包成 (china_score, usa_score) 的元组
2. 用 * 扩展解包输出每次对比结果
3. 至少使用一次一行交换变量

目标输出格式：
第1轮: 中国 85 vs 美国 82
第2轮: 中国 92 vs 美国 88
...

思路提示：
- zip(china, usa) 返回元组迭代器
- for i, (c, u) in enumerate(zip(...), 1): 可拿到轮次
- 一行交换示例：a, b = b, a
"""

# china = [85, 92, 78, 90, 88]
# usa   = [82, 88, 85, 91, 79]

# === 你的代码写在这里 ===
# for i, (c_score, u_score) in enumerate(zip(china, usa), 1):
#     print(f"第{i}轮: 中国 {c_score} vs 美国 {u_score}")


# ============================================================
# 练习2：tuple 元组 —— 学生成绩排名
# ============================================================
"""
题目：以下元组存储了5名学生的 (姓名, 总分)，
请按总分从高到低排序输出。

要求：
1. 使用 sorted() + key 参数排序
2. 用 *head, last 解包获取前三名和最后一名
3. 遍历输出排名结果

思路提示：
- sorted(students, key=lambda x: x[1], reverse=True)
- *top3, bottom = sorted_students
"""

# students = (
#     ("王林", 255),
#     ("李慕婉", 275),
#     ("十三", 245),
#     ("曾牛", 258),
#     ("韩立", 268),
# )

# === 你的代码写在这里 ===
# ranked = sorted(students, key=lambda s: s[1], reverse=True)
# print("=== 成绩排名 ===")
# for rank, (name, total) in enumerate(ranked, 1):
#     print(f"第{rank}名: {name} 总分{total}")


# ============================================================
# 练习3：set 集合 —— 多条件筛选
# ============================================================
"""
题目：有三个集合表示不同兴趣小组的成员，
请找出满足以下条件的学生。

条件：
1. 同时参加 Python 和 AI 小组的学生
2. 参加 Python 但不去 AI 小组的学生
3. 至少参加两个小组的学生（用交集思路）
4. 只参加一个小组的学生

思路提示：
- 交集 &、并集 |、差集 -
- "至少参加两个" = (python & ai) | (python & web) | (ai & web)
"""

# python = {"王林", "韩立", "厉飞雨", "紫灵", "张铁"}
# ai     = {"韩立", "紫灵", "曾牛", "天运子", "王蝉"}
# web    = {"厉飞雨", "张铁", "曾牛", "王林", "十三"}

# === 你的代码写在这里 ===
# print(f"Python & AI: {python & ai}")
# print(f"Python - AI: {python - ai}")
# at_least_two = (python & ai) | (python & web) | (ai & web)
# print(f"至少参加两个小组: {at_least_two}")
# print(f"只参加一个小组: {python ^ ai ^ web - at_least_two}")


# ============================================================
# 练习4：set 集合 —— 数据去重 + 交集应用
# ============================================================
"""
题目：两个班级的选课列表如下（有重复选课记录），
请找出同时选了"数据结构"和"算法设计"两门课的学生。

要求：
1. 先用 set 对两个列表分别去重
2. 再用交集找出同时选两门课的学生
3. 输出格式："同时选两门的学生有：XXX、XXX"

思路提示：
- set(data_structure) & set(algorithm_design)
- "、".join(result) 美化输出
"""

# data_structure = ["王林", "韩立", "王林", "紫灵", "张铁", "曾牛", "韩立"]
# algorithm_design = ["曾牛", "厉飞雨", "紫灵", "天运子", "王林", "张铁", "张铁"]

# === 你的代码写在这里 ===
# both = set(data_structure) & set(algorithm_design)
# print(f"同时选两门的学生有：{'、'.join(both)}")


# ============================================================
# 练习5：dict 字典 —— 词频统计
# ============================================================
"""
题目：统计以下英文句子中每个单词出现的次数。

要求：
1. 用 split() 分词
2. 用 dict 存储 {单词: 次数}
3. 用 d.get(word, 0) + 1 实现计数
4. 输出按出现次数从高到低排序

思路提示：
- words = sentence.lower().split()
- count[word] = count.get(word, 0) + 1
- sorted(count.items(), key=lambda x: x[1], reverse=True)
"""

# sentence = "Python is great and Python is fun and learning Python is amazing"

# === 你的代码写在这里 ===
# words = sentence.lower().split()
# count = {}
# for word in words:
#     count[word] = count.get(word, 0) + 1
# print("=== 词频统计 ===")
# for word, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
#     print(f"  {word}: {freq}次")


# ============================================================
# 练习6：dict 字典 —— 商品库存管理
# ============================================================
"""
题目：模拟一个简单的商品库存管理。

原始库存：
    "苹果": {"price": 5.5, "num": 100}
    "香蕉": {"price": 3.0, "num": 150}
    "橘子": {"price": 4.2, "num": 80}

操作步骤：
1. 卖出 20 个苹果 → 更新库存
2. 香蕉进货 50 个 → 更新库存
3. 新增商品 "草莓" 价格 15.0 库存 30
4. 查询苹果的单价和库存
5. 删除库存为 0 的商品（如果有）
6. 打印所有商品的总价值（单价 * 数量 求和）

要求：全程用 dict 操作，至少用到 get/pop/items
"""

# inventory = {
#     "苹果": {"price": 5.5, "num": 100},
#     "香蕉": {"price": 3.0, "num": 150},
#     "橘子": {"price": 4.2, "num": 80},
# }

# === 你的代码写在这里 ===
# inventory["苹果"]["num"] -= 20               # 卖出20个
# inventory["香蕉"]["num"] += 50               # 进货50个
# inventory["草莓"] = {"price": 15.0, "num": 30}  # 新增商品

# # 查询
# apple = inventory.get("苹果")
# print(f"苹果: 单价{apple['price']}元, 库存{apple['num']}个")

# # 计算总价值
# total_value = sum(info["price"] * info["num"] for info in inventory.values())
# print(f"库存总价值: {total_value:.2f}元")


# ============================================================
# 练习7：dict 嵌套 —— 模拟教务系统统计
# ============================================================
"""
题目：完善以下教务系统的统计功能。

已有数据：students = {姓名: {语数英成绩}}

要求：
1. 计算每个学生的总分和平均分
2. 找出总分最高的学生（可能并列）
3. 找出某单科（如数学）成绩低于60分的学生（如果全部>=60，输出无）
4. 按总分从高到低输出排名表

输出格式：
排名  姓名    语文  数学  英语  总分  平均分
 1   李慕婉   92   88   95   275   91.7
 2   韩立     85   92   88   265   88.3
...
"""

# students = {
#     "王林":   {"chinese": 85, "math": 78, "english": 92},
#     "李慕婉": {"chinese": 92, "math": 88, "english": 95},
#     "十三":   {"chinese": 78, "math": 82, "english": 85},
#     "曾牛":   {"chinese": 88, "math": 79, "english": 91},
#     "韩立":   {"chinese": 85, "math": 92, "english": 88},
# }

# === 你的代码写在这里 ===
# # 计算总分和排名
# rankings = []
# for name, scores in students.items():
#     total = sum(scores.values())
#     rankings.append((name, scores["chinese"], scores["math"], scores["english"], total))

# rankings.sort(key=lambda x: x[4], reverse=True)

# print(f"{'排名':<6}{'姓名':<8}{'语文':<6}{'数学':<6}{'英语':<6}{'总分':<6}{'平均分'}")
# for rank, (name, ch, ma, en, total) in enumerate(rankings, 1):
#     print(f"{rank:<6}{name:<8}{ch:<6}{ma:<6}{en:<6}{total:<6}{total/3:.1f}")

# # 找最高分（支持并列）
# max_total = max(r[4] for r in rankings)
# top_students = [r[0] for r in rankings if r[4] == max_total]
# print(f"\n总分最高: {'、'.join(top_students)} ({max_total}分)")


# ============================================================
# 练习8：综合挑战 —— 购物车金额统计
# ============================================================
"""
题目：实现一个简易的收银台系统，计算购物车中所有商品的总价。

要求：
1. 购物车结构：{商品名: {"price": 单价, "num": 数量}}
2. 计算每种商品的小计 (price * num)
3. 计算所有商品的总价
4. 如果有满减优惠（满100减10），计算优惠后总价
5. 输出购物小票

思路提示：
- sum(商品["price"] * 商品["num"] for 商品 in cart.values())
- 条件判断是否满减
"""

# cart = {
#     "苹果": {"price": 5.5, "num": 5},
#     "香蕉": {"price": 3.0, "num": 3},
#     "牛奶": {"price": 12.0, "num": 2},
#     "面包": {"price": 8.5, "num": 4},
# }

# === 你的代码写在这里 ===
# print("=== 购物小票 ===")
# for name, info in cart.items():
#     subtotal = info["price"] * info["num"]
#     print(f"{name}: {info['price']}元 x {info['num']} = {subtotal:.2f}元")

# total = sum(info["price"] * info["num"] for info in cart.values())
# print(f"\n原价合计: {total:.2f}元")

# if total >= 100:
#     discount = 10
#     final_price = total - discount
#     print(f"满100减{discount}元优惠已生效！")
#     print(f"优惠后总价: {final_price:.2f}元")
# else:
#     print(f"再买{100 - total:.1f}元可享受满减优惠")


# ============================================================
# 练习9：综合挑战 —— 通讯录管理系统
# ============================================================
"""
题目：仿照购物车系统的架构，实现一个通讯录管理系统。

菜单选项：
1. 添加联系人（姓名 + 电话 + 分组）
2. 查询联系人（按姓名查询）
3. 修改联系人电话
4. 删除联系人
5. 列出所有联系人
6. 按分组查看联系人
7. 退出

存储结构：
contacts = {
    "张三": {"phone": "13800138000", "group": "家人"},
    "李四": {"phone": "13900139000", "group": "同事"},
}

要求：
- match-case 做菜单分发
- while 循环
- 存在性判断用 key in dict
- 按分组查看用 dict 推导式
"""

# contacts = {}  # 初始为空，通过菜单添加

# === 你的代码写在这里 ===
# menu = """
# === 通讯录管理系统 ===
# 1.添加联系人  2.查询联系人  3.修改电话
# 4.删除联系人  5.列出全部  6.按分组查看  7.退出
# """
# while True:
#     print(menu)
#     op = input("请选择操作(1-7): ")
#     match op:
#         case '1':
#             name = input("姓名: ")
#             if name in contacts:
#                 print(f"{name}已存在！")
#                 continue
#             phone = input("电话: ")
#             group = input("分组: ")
#             contacts[name] = {"phone": phone, "group": group}
#             print(f"添加{name}成功")
#         case '2':
#             name = input("请输入查询姓名: ")
#             info = contacts.get(name)
#             if info:
#                 print(f"姓名:{name} 电话:{info['phone']} 分组:{info['group']}")
#             else:
#                 print(f"未找到{name}")
#         case '3':
#             name = input("请输入需要修改联系人的姓名: ")
#             if name not in contacts:
#                 print(f"未找到{name}")
#                 continue
#             new_phone = input("请输入新电话: ")
#             contacts[name]["phone"] = new_phone
#             print(f"修改{name}电话成功")
#         case '4':
#             name = input("请输入需要删除的联系人姓名: ")
#             if name not in contacts:
#                 print(f"未找到{name}")
#                 continue
#             contacts.pop(name)
#             print(f"删除{name}成功")
#         case '5':
#             print(f"{'姓名':<8}{'电话':<15}{'分组':<8}")
#             for name, info in contacts.items():
#                 print(f"{name:<8}{info['phone']:<15}{info['group']:<8}")
#         case '6':
#             group = input("请输入分组名称: ")
#             result = {n: info for n, info in contacts.items() if info["group"] == group}
#             if result:
#                 print(f"分组【{group}】的联系人:")
#                 for name, info in result.items():
#                     print(f"  {name}: {info['phone']}")
#             else:
#                 print(f"分组【{group}】下无联系人")
#         case '7':
#             print("已退出通讯录")
#             break
#         case _:
#             print("无效操作，请重试")


# ============================================================
# 练习10：终极挑战 —— 数据容器混合使用
# ============================================================
"""
题目：有一份学生选课数据，需要完成以下统计。

原始数据：两个 dict 分别存储学生信息和课程信息。
student_info = {"S001": "王林", "S002": "李慕婉", "S003": "十三", "S004": "曾牛"}
courses = {"Python": ["S001", "S002"], "AI": ["S002", "S003", "S004"], "Web": ["S001", "S003"]}

要求：
1. 输出每门课的学生姓名（用学号查姓名）
2. 找出选了 Python 但没选 AI 的学生
3. 找出选了至少两门课的学生
4. 统计每门课的人数，按人数从多到少排序

思路提示：
- 用 set 做集合运算（学号集合）
- 用 dict 做 {课程名: 学生名列表} 的映射
- 用 sorted() 按人数排序
"""

# student_info = {"S001": "王林", "S002": "李慕婉", "S003": "十三", "S004": "曾牛"}
# courses = {
#     "Python": {"S001", "S002"},
#     "AI":     {"S002", "S003", "S004"},
#     "Web":    {"S001", "S003"},
# }

# === 你的代码写在这里 ===
# # 1. 每门课的学生姓名
# print("=== 课程-学生列表 ===")
# for course, students_set in courses.items():
#     names = [student_info[sid] for sid in students_set]
#     print(f"{course}: {'、'.join(names)}")

# # 2. Python 但没选 AI
# python_only = courses["Python"] - courses["AI"]
# names = [student_info[sid] for sid in python_only]
# print(f"\n选Python不选AI: {'、'.join(names)}")

# # 3. 选至少两门课
# from collections import Counter
# all_students = []
# for s in courses.values():
#     all_students.extend(s)
# course_count = Counter(all_students)
# multi = {sid for sid, cnt in course_count.items() if cnt >= 2}
# names = [student_info[sid] for sid in multi]
# print(f"选课>=2门: {'、'.join(names)}")

# # 4. 按人数排序
# print("\n=== 课程人数排名 ===")
# for course, students_set in sorted(courses.items(),
#                                     key=lambda x: len(x[1]), reverse=True):
#     print(f"{course}: {len(students_set)}人")
