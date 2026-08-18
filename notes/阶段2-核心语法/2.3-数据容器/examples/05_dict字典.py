"""
05 - dict 字典（键值对/增删改查/嵌套/遍历/综合案例）
对应课程：第 52-55 集
生成时间: 2026-07-24
"""

# ===== 1. 定义与基本操作 =====
print("=== 1. 定义与基本操作 ===")

d = {"mosifu": 688, "jianl": 334, "mo": 666}
print(f"字典: {d}, 类型: {type(d)}")

# key 必须是不可变类型
d2 = {0: 123, 1.3: 444, (1, 2): 666, ('A', 'B'): 777}
print(f"各种key类型: {d2}")

# 访问
print(f"d['mosifu'] = {d['mosifu']}")
print(f"d.get('mosifu') = {d.get('mosifu')}")
print(f"d.get('不存在', '默认') = {d.get('不存在', '无此key')}")

# ===== 2. 增删改查 =====
print("\n=== 2. 增删改查 ===")

d3 = {"莫": 444, "简": 888, "兰": 777}
print(f"原始: {d3}")

# 增 — key不存在
d3["你好"] = 350
print(f"添加: {d3}")

# 改 — key存在
d3["你好"] = 600
print(f"修改: {d3}")

# 删
popped = d3.pop("简")
print(f"pop('简') = {popped}, 剩余: {d3}")

del d3["兰"]
print(f"del后: {d3}")

# ===== 3. keys/values/items =====
print("\n=== 3. keys/values/items ===")

d4 = {"莫": 444, "简": 888, "兰": 777, "爱": 666}
print(f"keys:   {d4.keys()}")
print(f"values: {d4.values()}")
print(f"items:  {d4.items()}")

# 遍历方式1：遍历 key
print("\n遍历key:")
for k in d4.keys():
    print(f"  {k}: {d4[k]}")

# 遍历方式2：遍历 key+value（推荐）
print("\n遍历key+value:")
for k, v in d4.items():
    print(f"  {k}: {v}")

# ===== 4. 嵌套字典 =====
print("\n=== 4. 嵌套字典 ===")

shop = {
    "苹果": {'price': 5.5, 'num': 10},
    "香蕉": {'price': 3.0, 'num': 20},
    "橘子": {'price': 4.2, 'num': 15},
}

print("购物车商品:")
for name, info in shop.items():
    # ⚠️ 嵌套dict的f-string: 外层用双引号，内层key用单引号
    print(f"  {name}: 单价{info['price']}元, 数量{info['num']}个")

# ===== 5. 购物车系统（模拟）=====
print("\n=== 5. 购物车系统演示 ===")

cart = {}

# 模拟添加
cart["苹果"] = {'price': 5.5, 'num': 3}
cart["香蕉"] = {'price': 3.0, 'num': 5}
print("添加后:", cart)

# 模拟修改
cart["苹果"] = {'price': 5.5, 'num': 6}  # 数量改为6
print("修改后:", cart)

# 模拟查询
print("查询结果:")
for k, v in cart.items():
    print(f"  商品:{k}, 价格:{v['price']}元, 数量:{v['num']}")

# 模拟删除
cart.pop("香蕉")
print("删除后:", cart)

# ===== 6. 教务管理系统演示 =====
print("\n=== 6. 教务管理系统演示 ===")

students = {
    "王林":   {'chinese': 85, 'math': 78, 'english': 92},
    "李慕婉": {'chinese': 92, 'math': 88, 'english': 95},
    "十三":   {'chinese': 78, 'math': 82, 'english': 85},
    "曾牛":   {'chinese': 88, 'math': 79, 'english': 91},
}

# 列出所有学生
print(f"{'姓名':<8}{'语文':<6}{'数学':<6}{'英语':<6}")
for name, scores in students.items():
    print(f"{name:<8}{scores['chinese']:<6}{scores['math']:<6}{scores['english']:<6}")

# 统计班级成绩
chinese_scores = [students[n]['chinese'] for n in students]
math_scores    = [students[n]['math'] for n in students]
english_scores = [students[n]['english'] for n in students]

print(f"\n{'':<8}{'语文':<8}{'数学':<8}{'英语':<8}")
print(f"{'最高分':<8}{max(chinese_scores):<8}{max(math_scores):<8}{max(english_scores):<8}")
print(f"{'最低分':<8}{min(chinese_scores):<8}{min(math_scores):<8}{min(english_scores):<8}")
print(f"{'平均分':<8}{sum(chinese_scores)/len(chinese_scores):.1f}   {sum(math_scores)/len(math_scores):.1f}   {sum(english_scores)/len(english_scores):.1f}")

# 找最高分对应学生
max_student = students[list(students.keys())[0]]  # 仅作结构展示
print("\n语文最高分的同学:")
for name in students:
    if students[name]['chinese'] == max(chinese_scores):
        print(f"  {name}")
