"""
02 - 字符串字面量示例
对应课程：第 09 集
"""

# ===== 4 种字符串写法 =====

# 单引号 — Java 里是 char，Python 里是 str
name1 = '单引号字符串'

# 双引号 — 和 Java 一样
name2 = "双引号字符串"

# 三单引号 — 可跨行，Java 无直接对应
name3 = '''这是三单引号
跨行字符串
可以写多行内容'''

# 三双引号 — ≈ Java 13+ 文本块 Text Block
name4 = """这也是三双引号
跨行字符串
经常用作文档注释"""

print("=== 四种字符串写法 ===")
print(f"单引号: {name1}")
print(f"双引号: {name2}")
print(f"三单引号: {name3}")
print(f"三双引号: {name4}")

# ===== 引号嵌套技巧 =====
# 里面用双引号，外面用单引号 — 无需转义
s1 = '他说："Python 很简单！"'

# 里面用单引号，外面用双引号
s2 = "It's a beautiful day!"

print("\n=== 引号嵌套 ===")
print(s1)
print(s2)

# ===== Java 对比 =====
# Java:   char c = 'A';   ← 单引号是 char，占 2 字节
# Python: c = 'A'         ← 单引号也是 str，没有 char 类型！
char_demo = 'A'
print(f"\n单字符 'A' 的类型: {type(char_demo)}  ← 是 str，不是 char！")
