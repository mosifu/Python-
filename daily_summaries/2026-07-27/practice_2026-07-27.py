"""
======================================
 复盘练习 — 阶段2收官日（第71-87集）
 2.5 类型注解与模块 / 2.6 面向对象 / 2.7 异常处理
 日期：2026-07-27
 说明：纯注释文件，思考每个练习的实现思路
======================================
"""

# =====================================================================
# 练习 1：带类型注解的计算器 — 变量/参数/返回值注解 + Union
# =====================================================================
# 目标：给三个函数补充完整的类型注解：
#   1. add(a, b)           -> 两数相加（int 参数，int 返回）
#   2. parse_num(text)     -> 把字符串解析为数字（可能是 int 或 float，
#                             提示：float(text) 或 int(text) 均可，
#                             返回值用 Union 联合类型）
#   3. analyze(items)      -> 接收 list[int | float]，返回 (总和, 平均值)
#                             平均值用 round 保留 2 位
#
# 示例调用：
#   add(3, 5)              -> 8
#   parse_num("3.14")      -> 3.14（float）
#   analyze([90, 85.5, 100]) -> (275.5, 91.83)
#
# 思路提示：
#   1. def add(a: int, b: int) -> int: ...
#   2. def parse_num(text: str) -> int | float: ...
#   3. def analyze(items: list[int | float]) -> tuple[int | float, float]:
#        total = sum(items)
#        return total, round(total / len(items), 2)
#   4. 再定义一个变量并注解：scores: list[int] = [90, 85, 100]
#
# 考察点：变量注解、容器注解 list[...]、Union |、函数参数/返回值注解
# =====================================================================


# =====================================================================
# 练习 2：订单计算器加注解 — *args 容器注解 + 默认参数注解
# =====================================================================
# 目标：仿照课程中的 calc_order_cost，给下面的函数写类型注解：
#   输入：*args 是多个 (商品名, 单价, 数量) 元组
#         vip_level: 0=无 1=9.5折 2=9折 3=8折（默认0）
#         coupon: 优惠券金额（默认0）
#   逻辑：商品总额 = 每件 单价*数量 之和
#         满 2000 减 100，满 5000 减 300（与优惠券不叠加，取较大者）
#         然后按 vip_level 打折，最后返回总价
#
# 示例调用：
#   calc_order(("手机", 4999, 2), ("茶叶", 78, 5), vip_level=2, coupon=10)
#
# 思路提示：
#   1. def calc_order(*args: tuple[str, float, int],
#                     vip_level: int = 0, coupon: int = 0) -> float
#   2. prices = [p * n for _, p, n in args]   # 列表推导式解包元组
#   3. total = sum(prices)
#   4. 满减：full_cut = 100 if total >= 2000 else 300 if total >= 5000 else 0
#      total -= max(full_cut, coupon)          # 取较大者
#   5. 折扣：total *= [1, 0.95, 0.9, 0.8][vip_level]
#   6. return round(total, 2)
#
# 考察点：*args 容器注解、默认参数注解、Union、列表推导式、业务逻辑
# =====================================================================


# =====================================================================
# 练习 3：自定义模块设计 — __all__ / __name__ / 导入方式
# =====================================================================
# 目标：设计一个 string_utils.py 模块（只写设计，不用真建文件）：
#   函数：
#     reverse_str(s)      -> 反转字符串
#     count_words(text)   -> 统计单词数（按空格 split）
#     to_upper(s)         -> 转大写
#     _private_helper(s)  -> 私有约定函数（下划线前缀，不放进 __all__）
#   __all__ = ['reverse_str', 'count_words', 'to_upper']
#   if __name__ == '__main__': 里放测试代码
#
# 再写出在其他文件中导入该模块的 4 种方式：
#   1. import string_utils -> string_utils.reverse_str("abc")
#   2. import string_utils as su -> su.reverse_str("abc")
#   3. from string_utils import reverse_str, count_words
#   4. from string_utils import *（思考：_private_helper 会被导入吗？）
#
# 思路提示：
#   1. __all__ 控制 from string_utils import * 的可见名单
#   2. 下划线开头是"约定私有"，import * 默认也不导入
#   3. __name__ == '__main__' 守卫保证被导入时不执行测试代码
#   4. 思考题：为什么 from module import * 在生产代码中不推荐？
#
# 考察点：自定义模块、__all__、__name__ 入口守卫、四种导入方式
# =====================================================================


# =====================================================================
# 练习 4：包结构设计 — __init__.py / 点号路径导入
# =====================================================================
# 目标：设计一个 calculator/ 包（只写设计）：
#
#   calculator/
#   ├── __init__.py        # __all__ = ['basic', 'advanced']
#   │                      # __version__ = "1.0.0"
#   ├── basic.py           # add / sub / mul / div 四个函数
#   └── advanced.py        # power / sqrt / factorial
#
# 写出三种导入方式及调用：
#   1. from calculator import basic
#      basic.add(2, 3)
#   2. from calculator.basic import add, div
#      add(2, 3)
#   3. from calculator import *        # 受 __init__.py 的 __all__ 控制
#      basic.add(2, 3); advanced.power(2, 10)
#
# 思路提示：
#   1. 包 = 文件夹 + __init__.py
#   2. __init__.py 里的 __all__ 控制 from calculator import * 能导入哪些模块
#   3. 点号路径 = 包名.模块名（不能直接用 import calculator 后 calculator.add()，
#      因为 add 不在包命名空间里，除非在 __init__.py 中显式导入）
#   4. 思考题：如果没有 __init__.py，from calculator import * 会怎样？
#
# 考察点：package 包结构、__init__.py、__all__、点号导入路径
# =====================================================================


# =====================================================================
# 练习 5：BankAccount 银行账户类 — class / __init__ / self / 实例方法
# =====================================================================
# 目标：设计 BankAccount 类：
#   属性：owner（户主名）、balance（余额，默认 0.0）
#   方法：
#     deposit(amount)  存款，余额增加，打印 "存了X元，余额Y元"
#     withdraw(amount) 取款，余额不足时打印提示且不扣款
#     show()           打印 "户主:xxx 余额:xxx"
#
# 示例：
#   acc = BankAccount("mosifu", 1000)
#   acc.deposit(500)     # 余额 1500
#   acc.withdraw(2000)   # 提示余额不足，余额不变
#   acc.show()
#
# 思路提示：
#   1. class BankAccount:
#   2. def __init__(self, owner: str, balance: float = 0.0):
#        self.owner = owner
#        self.balance = balance
#   3. deposit 里 self.balance += amount（注意 amount 类型注解）
#   4. withdraw 里 if amount > self.balance: print("余额不足") else 扣款
#   5. 创建两个账户，互不影响（实例属性独有性的验证）
#   6. 给全部方法加上类型注解（呼应今日 2.5 的内容）
#
# 考察点：类定义、__init__ 初始化、self、实例方法、实例属性独立性
# =====================================================================


# =====================================================================
# 练习 6：Book 类 + 魔法方法 — __str__ / __lt__ / __eq__
# =====================================================================
# 目标：设计 Book 类（title 书名 / author 作者 / price 价格）：
#   __str__：返回 f"《{title}》 {author} ¥{price}"
#   __lt__ ：按价格比较（自选：价格相同再比书名字母序）
#   __eq__ ：书名相同即视为同一本书（作者也相同更好）
#
# 要求：创建 3-4 本书放进列表 books，然后：
#   books.sort()            # 依赖 __lt__ 按价格升序
#   for b in books: print(b)   # 依赖 __str__ 友好输出
#   检查两本同名的书 books[0] == books[1] 是否为 True（依赖 __eq__）
#
# 思路提示：
#   1. def __str__(self) -> str: return f"《{self.title}》{self.author} ¥{self.price}"
#   2. def __lt__(self, other) -> bool:
#        if self.price != other.price: return self.price < other.price
#        return self.title < other.title
#   3. def __eq__(self, other) -> bool:
#        return self.title == other.title and self.author == other.author
#   4. sort() 内部比较 "<" 时自动调用 __lt__，无需手动调用
#   5. 思考题：不写 __lt__ 时 books.sort() 会报什么错？（TypeError）
#
# 考察点：魔法方法触发时机、对象比较、sort 联动、__str__ 返回类型
# =====================================================================


# =====================================================================
# 练习 7：类属性 vs 实例属性 — 实例计数器 + 遮蔽现象
# =====================================================================
# 目标：设计 Counter 类：
#   类属性 count = 0
#   __init__(self, name)：给实例属性 self.name 赋值，并让类属性 count + 1
#   类方法 count_instances()：返回当前已创建对象个数
#
# 示例：
#   a = Counter("a"); b = Counter("b"); c = Counter("c")
#   Counter.count_instances()   # 3
#   print(Counter.count)        # 3
#
# 附加思考（写出你的判断）：
#   1. 若在 __init__ 里写 self.count = 1，会发生什么？
#      -> 创建了实例属性，遮蔽类属性；a.count 是 1，Counter.count 仍是 0
#   2. 若 Counter.count = 100，会影响已创建的 a/b/c 吗？
#      -> 会：类属性共享，所有实例读取到的都是 100
#   3. 查找规则：实例.属性 先找实例属性，没有才找类属性
#
# 思路提示：
#   1. class Counter:
#        count = 0            # 类属性（所有实例共享）
#        def __init__(self, name):
#            self.name = name # 实例属性（各对象独有）
#            Counter.count += 1
#   2. 类方法（或直接用 Counter.count 访问）
#   3. 用 print(a.__dict__) 观察实例属性字典里有没有 count
#
# 考察点：类属性共享性、实例属性独有性、遮蔽、__dict__
# =====================================================================


# =====================================================================
# 练习 8：安全计算器 — 多异常捕获 / as e / finally / 异常传递
# =====================================================================
# 目标：
#   1. safe_div(a, b)：除数为 0 时捕获 ZeroDivisionError，返回 None 并打印提示
#   2. parse_score(text)：把字符串转 float，捕获 ValueError，非法返回 None
#   3. 异常传递：outer() -> inner() -> deep() 三层函数，
#      在 deep 里故意 1/0，在最外层 outer 调用处用 try 捕获
#      （体验：只要最外层捕获即可，不用每层都写）
#   4. finally：无论 safe_div 成功还是失败，都打印 "操作完成"
#
# 示例调用：
#   safe_div(10, 0)        # 捕获 ZeroDivisionError，返回 None
#   parse_score("abc")     # 捕获 ValueError，返回 None
#   parse_score("85.5")    # 返回 85.5
#
# 思路提示：
#   1. try/except ZeroDivisionError as e / finally
#   2. try/except ValueError as e：float(text) 失败时触发
#   3. def outer(): inner()  ->  def inner(): deep()  ->  def deep(): 1/0
#      在 outer() 调用处包 try/except Exception as e
#   4. 注意 except 顺序：具体异常在前，Exception 兜底在后
#   5. 思考题：如果 deep 内部自己 try 捕获了，还会传到 outer 吗？
#      -> 不会：被吞掉后就中断传递了
#
# 考察点：try/except/finally、as e、多异常、Exception 兜底、异常传递链
# =====================================================================


# =====================================================================
# 练习 9：综合实战 — OOP 图书管理系统（收官大作业）
# =====================================================================
# 目标：把今天三大主题（OOP + 异常处理 + 模块化入口）融会贯通，
#       设计一个图书管理系统：
#
#   Book 类（数据层）：
#     __init__(self, title, author, price)
#     __str__()  -> f"《{title}》{author} ¥{price}"
#     update_price(new_price)  # None 模式可选参数可以不加，直接传新价
#
#   Library 类（业务层）：
#     __init__(self)：self.books = []  # 实例属性承载状态
#     add_book()      # input 输入书名/作者/价格；价格 float(input()) 需 try
#     remove_book()   # 按书名查找并移除（找不到打印提示）
#     search_book()   # 按书名查找并打印（触发 __str__）
#     list_books()    # 全部打印；空列表时提示"图书馆是空的"
#     run()           # 主循环：menu 1.添加 2.删除 3.查询 4.全部 5.排序 6.退出
#                     # match/case 分发 + except ValueError 保护输入
#
#   入口：if __name__ == '__main__':  Library().run()
#
# 思路提示：
#   1. 类属性：system_version = "1.0.0"，run() 里打印版本号
#   2. 排序功能：sorted(self.books) 依赖 Book.__lt__（按价格）
#   3. 异常处理：try: price = float(input(...))
#                except ValueError: print("价格必须是数字"); return
#   4. 删除用列表推导式或循环 + remove
#   5. 这个系统的骨架就是 2.6 购物车/教务系统的复用——
#      "增删改查 + 菜单循环 + 输入防护"是管理系统的通用模式
#
# 考察点：OOP 完整设计、魔法方法、类属性、异常处理、match/case、
#         模块化入口、综合业务逻辑（阶段2能力总验收）
# =====================================================================
