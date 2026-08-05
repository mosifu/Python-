"""
采用面向对象的编程思想,完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息,通过控制台菜单与用户交互立,具体的功能如下:
    1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩,记录在系统中
        1.1输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2检查学生姓名是否已存在,如果学生不存在,再添加(存在则)不添加)
        1.3验证成绩范围(0-100分)
        1.4创建学生对象并添加到系统
    2.修改学生成绩:根据输入的学生姓名,修改对应的学生成绩
        2.1输入要修改的学生姓名
        2.2根据姓名查找该学生,显示该生当前成绩信息
        2.3输入新的语文、数学、英语成绩
        2.4更新学生成绩数据
    3.删除学生成绩:根据输入的学生姓名,删除对应的学生成绩童
    4.查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输出
        4.1输出格式为:"姓名:张三|语文:85|数学:90|英语:88|总分:263"
    5.展示全部学生成绩:展示出系统中所有学生的成绩
"""

#定义学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    #按姓名:张三|语文:85|数学:90|英语:88|总分:263 格式输出
    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分:{self.english+self.math+self.chinese}"

    #修改学生成绩方法
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#定义教务系统类
class EduManagement:
    system_version = "1.0.1"
    system_name = "教务管理系统"

    #初始化学生列表
    def __init__(self):
        self.stu_list = []  #学生列表记录学生信息

    #添加学生的方法
    def add_stu(self):
        name = input("请输入学生姓名:")
        #判断学生姓名是否存在,若存在则添加失败
        for stu in self.stu_list:
            if stu.name == name:
                print(f"学生{name}已存在,添加失败!")
                return

        chinese = float(input("请输入学生语文成绩:"))
        math = float(input("请输入学生数学成绩:"))
        english = float(input("请输入学生英语成绩:"))
        #判断成绩是否在1-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            s1 = Student(name, chinese, math, english)
            self.stu_list.append(s1)
            print("学生信息添加成功~")
        else:
            print("各科成绩必须在1-100之间")

    #修改学生信息
    def update_stu(self):
        name = input("请输入学生姓名:")

        #根据学生姓名查找学生的信息
        for stu in self.stu_list:
            if stu.name == name:
                print(f"当前成绩:{stu}")

                chinese = float(input("请输入修改后的语文成绩:"))
                math = float(input("请输入修改后的数学成绩:"))
                english = float(input("请输入修改后的英语成绩:"))

                # 判断成绩是否在1-100之间
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    stu.update_score(chinese, math, english)
                    print("学生成绩修改成功~")
                    print(f"修改后的成绩:{stu}")
                    return
                else:
                    print("各科成绩必须在1-100之间")

        print("未查到该学生信息,修改失败!")

    #删除学生信息
    def delete_stu(self):
        name = input("请输入学生姓名:")

        for stu in self.stu_list:
            if stu.name == name:
                self.stu_list.remove(stu)
                print("学生信息删除成功~")
                return

        print("未查到该学生信息,删除失败!")

    #查找指定学生成绩
    def query_stu(self):
        name = input("请输入学生姓名:")

        for stu in self.stu_list:
            if stu.name == name:
                print(f"学生信息:{stu}")
                return

        print("未查到该学生信息!")

    #展示全部学生成绩
    def list_stu(self):
        for stu in self.stu_list:
            print(stu)


    #系统运行
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

            choice = input("\n请输入要执行的操作(1-6):")
            #异常处理
            try:
                match choice:
                    case "1":   #添加学生
                        self.add_stu()
                    case "2":   #修改学生
                        self.update_stu()
                    case "3":   #删除学生
                        self.delete_stu()
                    case "4":   #查询指定学生
                        self.query_stu()
                    case "5":   #查询全部学生
                        self.list_stu()
                    case "6":   #退出系统
                        print("退出系统成功!bye~")
                        break
                    case _:     #其他情况
                        print("输入数字不在范围内,请重新输入!")
            except ValueError:
                print("输入的数据有误,请检查,然后重新输入!!!")
            except Exception:
                print("输入有误,重新选择!!!")



#测试
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()