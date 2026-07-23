"""
03 - tuple 元组（不可变/组包解包/单元素逗号）
对应课程：第 47-48 集
生成时间: 2026-07-24
"""

# ===== 1. 定义与基本操作 =====
print("=== 1. 定义与操作 ===")

t1 = (1, 234, 2, 43, 23, '456', 2)
print(f"元组: {t1}, 类型: {type(t1)}")

# 索引和切片 — 和 list 一样
print(f"t1[1]    = {t1[1]}")
print(f"t1[1::2] = {t1[1::2]}")

# 只有 count 和 index 两个方法
print(f"2 出现次数: {t1.count(2)}")
print(f"2 首次位置: {t1.index(2)}")

# 空元组和单元素
t2 = ()
t3 = (100,)    # ⚠️ 必须加逗号！(100) 只是带括号的 int
print(f"空元组: {t2}, 类型: {type(t2)}")
print(f"单元素元组: {t3}, 类型: {type(t3)}")
print(f"(100)不加逗号: {(100)}, 类型: {type((100))}")

# ===== 2. 组包与解包 =====
print("\n=== 2. 组包与解包 ===")

# 组包 — 多个值自动打包
t = 12, 213, 321, 124, 52
print(f"组包: {t}")

# 基础解包 — 数量必须匹配
a, b, c, d, e = t
print(f"解包: a={a}, b={b}, c={c}")

# 扩展解包 — * 收集剩余
first, second, *others = t
print(f"*解包: first={first}, others={others}(类型:{type(others)})")

*head, last = t
print(f"*解包: head={head}, last={last}")

# 经典应用：一行交换变量
x, y = 10, 20
print(f"交换前: x={x}, y={y}")
x, y = y, x
print(f"交换后: x={x}, y={y}")

# 三变量轮转
p, q, r = 100, 200, 300
c_old = r
c_new, a_new, b_new = p, q, r
print(f"轮转: a={p}, b={q}, c={r}")
p, q, r = q, r, p  # 更简洁的轮转
print(f"再轮转: a={p}, b={q}, c={r}")

# ===== 3. 遍历嵌套元组 =====
print("\n=== 3. 学生成绩单 ===")

students = (
    ("S001", "王林", 85, 78, 92),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 82, 85),
    ("S004", "曾牛", 88, 79, 91),
)

print(f"{'学号':<8}{'姓名':<8}{'语文':<6}{'数学':<6}{'英语':<6}{'总分':<6}{'均分'}")
for sid, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{sid:<8}{name:<8}{chinese:<6}{math:<6}{english:<6}{total:<6}{avg:.1f}")

# 统计各科
chinese_scores = [s[2] for s in students]
print(f"\n语文: 最高{max(chinese_scores)} 最低{min(chinese_scores)} 均分{sum(chinese_scores)/len(chinese_scores):.1f}")

# 均分 > 90 的学生
a_students = [s[1] for s in students if (s[2]+s[3]+s[4])/3 > 90]
print(f"均分>90的学生: {'、'.join(a_students)}")
