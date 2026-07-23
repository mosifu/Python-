"""
04 - set 集合（去重/交并差运算/集合推导式）
对应课程：第 49-51 集
生成时间: 2026-07-24
"""

# ===== 1. 定义与去重 =====
print("=== 1. 定义与去重 ===")

s1 = {1, 2, 3, 4, 5, 2, 4}
print(f"集合(自动去重): {s1}, 类型: {type(s1)}")

# ⚠️ {} 是 dict，不是 set！
empty_dict = {}
empty_set = set()
print(f"{{}}: {type(empty_dict)}, set(): {type(empty_set)}")

# ===== 2. 增删操作 =====
print("\n=== 2. 增删操作 ===")

s = {100, 200, 300, 400, 500}
print(f"原始: {s}")

s.add(800)
print(f"add(800)后: {s}")

s.remove(100)  # 元素不存在会报错
print(f"remove(100)后: {s}")

popped = s.pop()  # 随机删除
print(f"pop删除了: {popped}, 剩余: {s}")

s.clear()
print(f"clear后: {s}")

# ===== 3. 集合运算 =====
print("\n=== 3. 集合运算 ===")

s5 = {'A', 'B', 'C', 'D', 'E', 'F'}
s6 = {'B', 'C', 'G', 'H', 'I', 'J'}

# 交集：两者都有
print(f"交集 (&):  {s5 & s6}")
print(f"交集 (方法): {s5.intersection(s6)}")

# 并集：合并去重
print(f"并集 (|):  {s5 | s6}")
print(f"并集 (方法): {s5.union(s6)}")

# 差集：只在s5不在s6
print(f"差集 (-):  {s5 - s6}")
print(f"差集 (方法): {s5.difference(s6)}")

# ===== 4. 选课案例 =====
print("\n=== 4. 选课案例 ===")

football = {"王林", "普牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
basketball = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
french = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "普牛"}
art = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 1. 同时选法语和艺术
print(f"法语 ∩ 艺术: {french & art}")

# 2. 四门全选
all_four = football & basketball & french & art
print(f"四门全选: {all_four}")

# 3. 选足球但不选篮球
print(f"足球-篮球: {football - basketball}")

# 4. 统计每人选了几门
all_students = football | basketball | french | art
all_list = [*football, *basketball, *french, *art]  # 解包成list(允许重复)
print("\n每人选课数:")
for stu in sorted(all_students):
    print(f"  {stu}: {all_list.count(stu)}门")

# ===== 5. 集合推导式 =====
print("\n=== 5. 集合推导式 ===")

# {x for x in set if condition}
only_football = {s for s in football if s not in basketball}
print(f"只踢足球不踢篮球: {only_football}")
