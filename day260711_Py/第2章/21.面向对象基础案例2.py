"""
采用面向对象的编程思想,开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据,通过控制台菜单与用户交互。具体功能如下:
    1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
    2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入
    完成后修改该商品信息。
    3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
    4.查询购物车:将购物车中的商品信息展示出来,格式为:"商品名称:xxx,商品价格:xxx,商
    品数量:xxx"。
    5.退出购物车
"""

#创建商品类
class goods:
    #初始化商品信息
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    #设置商品信息输出格式
    def __str__(self):
        return f"商品名称:{self.name}, 商品价格:{self.price}, 商品数量:{self.num}"

    #修改商品信息
    def update_goods(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


#创建购物车系统类
class ShoppingCart():
    system_version = "1.0.1"
    system_name = "购物车管理系统"

    def __init__(self):
        #初始化购物车列表信息,用来装商品
        self.shopping_cart_list = []

    #添加购物车-键盘录入
    def add_shopping_care(self):
        name = input("请输入商品名称:")
        #判断当前商品是否在购物车
        for good in self.shopping_cart_list:
            if good.name == name:
                print("当前商品已存在,添加失败!")
                return

        price = float(input("请输入商品价格:"))
        num = int(input("请输入商品数量:"))
        good = goods(name, price, num)
        self.shopping_cart_list.append(good)
        print("商品添加成功~")

    #修改购物车
    def update_shopping_cart(self):
        name = input("请输入商品名称:")
        # 判断当前商品是否在购物车
        for good in self.shopping_cart_list:
            if good.name == name:
                print(good)
                #修改信息
                price = float(input("请输入商品价格:"))
                num = int(input("请输入商品数量:"))
                good.update_goods(price, num)
                print("修改商品信息成功~")
                print(f"修改后信息:{good}")
                return

        print("商品信息不存在,修改失败!")

    #删除购物车
    def delete_shopping_cart(self):
        name = input("请输入商品名称:")
        # 判断当前商品是否在购物车
        for good in self.shopping_cart_list:
            if good.name == name:
                self.shopping_cart_list.remove(good)
                print("删除商品信息成功~")
                return
        print("商品信息不存在,删除失败!")

    #查询购物车
    def print_shopping_cart(self):
        for good in self.shopping_cart_list:
            print(good)

    #运行系统
    def run(self):
        print(f"进入购物车系统 V{ShoppingCart.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加购物车    2.修改购物车    3.删除购物车    4.查询购物车    5.退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

            choice = input("\n请输入要执行的操作(1-5):")

            #异常处理
            try:
                match choice:
                    case "1":  # 添加购物车
                        self.add_shopping_care()
                    case "2":  # 修改购物车
                        self.update_shopping_cart()
                    case "3":  # 删除购物车
                        self.delete_shopping_cart()
                    case "4":  # 查询购物车
                        self.print_shopping_cart()
                    case "5":  # 退出系统
                        print("退出系统成功!bye~")
                        break
                    case _:  # 其他情况
                        print("输入数字不在范围内,请重新输入!")
            except ValueError:
                print("输入数值有误,请重新输入!!!")
            except Exception:
                print("操作有误,请重新输入!!!")


if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()