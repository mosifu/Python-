# 1.导入模块
# from 第二章.module_18.module2 import my_fun
# my_fun.log_separator1()
# my_fun.log_separator2()


# import module_18.module2.my_fun
# module_18.module2.my_fun.log_separator4()
# module_18.module2.my_fun.log_separator1()


#注意:如果要通过from ... import * 导入包下的所有模块,需要在 __init__.py文件中添加__all__ = []
# from module_18.module2 import *
#
# print(my_var.PI)
# print(my_var.NAME)
# my_fun.log_separator4()


#2.导入模块中的功能
#相对路径
from module_18.module2.my_fun import log_separator4, log_separator2

#绝对路径
from day260711_Py.第二章.module_18.module2.my_fun import log_separator2, log_separator3
log_separator4()
log_separator4()
log_separator2()