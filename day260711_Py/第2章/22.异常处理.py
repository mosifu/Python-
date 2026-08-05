#捕获异常
# try:
#     print("------------------------------")
#     print(my_name)
#     print("------------------------------")
# except NameError:
#     print("系统出现异常,请联系管理人员")

try:
    print("------------------------------")
    # print(my_name)
    # print(1/0)
    # print('ABC'[9])
    print('ABC'.hello)
    print("------------------------------")
except NameError as e:
    print("名字不存在,请检查变量或函数名字,异常信息:",e)
except ZeroDivisionError as e:
    print("0不能做被除数,异常信息:",e)
except IndexError as e:
    print("索引错误,异常信息:",e)
except Exception as e:
    print("程序出错,异常信息:",e)
finally:    #无论程序是否正常运行,finally代码块中的代码都会运行
    print("释放资源~")



# ------------ 异常的传递 ---------------
def fun1():
    print("fun1...running...")
    fun2()

def fun2():
    print("fun2...running...")
    fun3()

def fun3():
    print("fun3...running...")
    print(my_color)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序出错,请联系管理人员,错误信息:",e)