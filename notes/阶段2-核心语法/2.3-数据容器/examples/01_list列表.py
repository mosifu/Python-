"""
01 - list 列表（定义/索引/切片/增删改查/推导式）
对应课程：第 36-42 集
生成时间: 2026-07-21
"""

# ===== 1. 定义与索引 =====
print("=== 1. 定义与索引 ===")

s = [1, 3, 4.5, 'hello', True]  # 混合类型 OK
print(f"列表: {s}, 类型: {type(s)}")

print(f"s[0] = {s[0]}")      # 正向索引
print(f"s[-5] = {s[-5]}")    # 反向索引（倒数第5个）
print(f"s[-1] = {s[-1]}")    # 最后一个

# 修改
s[3] = "world"
print(f"修改后: {s}")

# ===== 2. 切片 =====
print("\n=== 2. 切片 ===")

h = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(f"h[0:6]    = {h[0:6]}")      # 索引 0-5
print(f"h[:4]     = {h[:4]}")       # 从头到索引3
print(f"h[1:-1:2] = {h[1:-1:2]}")   # 索引1到-1，步长2
print(f"h[::-1]   = {h[::-1]}")     # 反转！

# ===== 3. 增删改查 =====
print("\n=== 3. 增删改查 ===")

g = [56, 234, 634, 23, 63, 74, 211, 5]
print(f"原始: {g}")

g.append(78)
print(f"append(78):   {g}")

g.insert(1, 99)
print(f"insert(1,99): {g}")

g.remove(78)
print(f"remove(78):   {g}")

g.pop(1)
print(f"pop(1):       {g}")

g.pop()
print(f"pop():         {g}")

g.sort()
print(f"sort():        {g}")

g.reverse()
print(f"reverse():     {g}")

# ===== 4. 合并与去重 =====
print("\n=== 4. 合并与去重 ===")

list1 = [12, 24, 35, 12, 535]
list2 = [121, 24, 25, 121, 55]

# 合并 — 三种方式
merged = list1 + list2                           # +
merged = [*list1, *list2]                         # 解包
print(f"合并: {merged}")

# 去重
unique = []
for item in merged:
    if item not in unique:
        unique.append(item)
print(f"去重: {unique}")

# ===== 5. 列表推导式 =====
print("\n=== 5. 列表推导式 ===")

# 语法1：[表达式 for i in 序列]
squares = [i**2 for i in range(1, 21)]
print(f"1-20平方: {squares[:5]}...{squares[-3:]}")

# 语法2：[表达式 for i in 序列 if 条件]
evens = [i for i in range(1, 31) if i % 2 == 0]
print(f"偶数({len(evens)}个): {evens[:5]}...")

# 综合：能被3或5整除的数的平方
result = [i**2 for i in range(1, 31) if i % 3 == 0 or i % 5 == 0]
print(f"3或5倍数的平方: {result}")

# 提取正数
nums = [11, 21, -11, 1231, -34, 10, 35, -111, -2134]
positives = [i for i in nums if i > 0]
print(f"正数: {positives}")

# ===== 6. 综合案例：10个数字统计 =====
print("\n=== 6. 综合案例 ===")

# 用固定数据演示（实战中 input()）
data = [45, 12, 89, 33, 67, 21, 94, 8, 56, 72]
data.sort()
print(f"排序: {data}")
print(f"最小: {data[0]}, 最大: {data[-1]}")
print(f"平均: {sum(data)/len(data):.2f}")
