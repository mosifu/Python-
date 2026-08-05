#__all__ 指定的是 from ... import * 导入的是哪些功能
__all__ = ['PI', 'log_separator1', 'log_separator4']

#常量: 不会发生变化的数据;通常为全部大写
PI = 3.14159
NAME = "mosifu"

#函数
def log_separator1():
    print("- " * 30)

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

#测试函数
#log_separator1()
# __name__:Python内置变量,表示当前模块的名字(若直接运行当前模块,__name__的值为"__main__";当该模块被导入时,__name__的值是模块名"my_fun")
#如果直接执行当前文件,则执行如下代码;如果是被导入则不执行
if __name__ == '__main__':
    log_separator1()