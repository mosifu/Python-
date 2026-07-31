"""
自定义模块 - my_tools
演示 __all__ 和 __name__ 的用法
"""

# __all__ 控制 from my_tools import * 能导入哪些
__all__ = ['PI', 'NAME', 'log_separator1', 'log_separator4']

# 常量（全大写命名约定）
PI = 3.14159
NAME = "mosifu"


# 函数
def log_separator1():
    print("- " * 30)


def log_separator2():
    print("+ " * 30)


def log_separator3():
    print("# " * 30)


def log_separator4():
    print("* " * 30)


# __name__：直接运行时为 '__main__'，被导入时为模块名 'my_tools'
# 只有直接运行才执行测试代码，被导入不执行
if __name__ == '__main__':
    print(f"模块名: {__name__}")
    log_separator1()
    print("这是 my_tools 模块的测试代码")
