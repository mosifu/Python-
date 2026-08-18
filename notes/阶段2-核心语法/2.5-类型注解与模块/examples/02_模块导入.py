"""
02 - 模块导入（import / from...import / as 别名）
对应课程：第 73-76 集
生成时间: 2026-07-26
"""

# ===== 1. 导入标准库模块 =====
print("=== 1. 导入标准库 ===")

# 方式1：import 模块名 - 调用加前缀
import random
print(f"random.randint(1,100) = {random.randint(1, 100)}")

# 方式1变体：as 别名
import random as rd
print(f"rd.randint(1,100) = {rd.randint(1, 100)}")

# 方式2：from 模块 import 功能 - 直接用功能名
from random import randint
print(f"randint(1,100) = {randint(1, 100)}")

# 方式2变体：as 别名
from random import randint as rint
print(f"rint(1,100) = {rint(1, 100)}")

# 方式3：from 模块 import * - 导入全部（不推荐）
from random import *
print(f"randint(1,100) = {randint(1, 100)}")

# ===== 2. 导入自定义模块 =====
print("\n=== 2. 导入自定义模块 ===")

# 导入同目录下的 my_tools 模块
import my_tools as tools

print(f"tools.PI = {tools.PI}")
print(f"tools.NAME = {tools.NAME}")
tools.log_separator1()
tools.log_separator4()

# 导入模块的功能
from my_tools import PI, log_separator2
print(f"PI = {PI}")
log_separator2()

# ===== 3. __all__ 与 __name__ 演示 =====
print("\n=== 3. __all__ 与 __name__ ===")

# from module import * 受 __all__ 控制
from my_tools import *
print(f"import * 后能用 PI: {PI}")
log_separator1()
log_separator4()
# log_separator2()  # ❌ 不在 __all__ 里，import * 导入不了

# 模块名本身需要 import 才能用
import my_tools
print(f"\nmy_tools 模块名: {my_tools.__name__}")
print(f"当前模块名: {__name__}")
print("直接运行时 __name__ == '__main__'")

# ===== 4. 导入包中的模块 =====
print("\n=== 4. 导入包中模块 ===")

# 导入包中的模块
from mypackage import my_math
print(f"mypackage.my_math.add(2,3) = {my_math.add(2, 3)}")

# 导入包中模块的功能
from mypackage.my_math import multiply
print(f"multiply(4,5) = {multiply(4, 5)}")

# 导入包的变量
from mypackage import my_config
print(f"my_config.VERSION = {my_config.VERSION}")
