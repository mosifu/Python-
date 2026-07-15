"""
06 - 字符串操作（拼接、格式化、转义字符）
对应课程：第 16-17 集
生成时间: 2026-07-15
"""

# ===== 1. 字符串拼接 =====
print("=== 字符串拼接 ===")

name = "mo_sifu"
age = 23
job = "AI"
hobby = "run"

# + 拼接 — 非 str 类型需要 str() 转换
print("我是" + name + "，今年" + str(age) + "岁")
# print("我是" + name + age)  # TypeError: 不能 int + str

# 隐式拼接 — 相邻字符串字面量自动合并（Java 没有！）
msg = "气温二十一度" '刚好又是花季' """适合出去玩"""
print(f"隐式拼接: {msg}")

# join — 用分隔符连接
words = ["Hello", "Python", "World"]
print(f"空格连接: {' '.join(words)}")
print(f"逗号连接: {', '.join(words)}")

# ===== 2. 字符串格式化 =====
print("\n=== 字符串格式化 ===")

# 方式1: %s 占位（老式）
print("(%%s) 我是%s，今年%s岁，专业%s，爱好%s" % (name, age, job, hobby))

# 方式2: f-string（推荐！）
print(f"(f-string) 我是{name}，今年{age}岁，专业{job}，爱好{hobby}")

# f-string 里写表达式
print(f"明年我就{age + 1}岁了")
print(f"名字大写: {name.upper()}")
print(f"名字长度: {len(name)} 个字符")

# f-string 格式化数字
pi = 3.14159
print(f"pi ≈ {pi:.2f}")           # 保留 2 位小数
print(f"百分比: {0.856:.1%}")       # 百分比格式
print(f"大数千分位: {1000000:,}")    # 1,000,000

# 方式3: .format()
print("(format) 我是{}，今年{}岁".format(name, age))

# ===== 3. 转义字符 =====
print("\n=== 转义字符 ===")

# 同引号用 \ 转义
print('It\'s a good day')

# \n 换行
print("你好世界，\n欢迎来到Python的世界")

# \t 制表符（对齐列）
print("姓名\t年龄\t城市")
print("张三\t25\t北京")
print("李四\t30\t上海")

# 防转义：用 r 前缀（raw string）— 常用于正则和路径
print(r"C:\Users\mosifu\Desktop")  # 不需要 \\ 转义
