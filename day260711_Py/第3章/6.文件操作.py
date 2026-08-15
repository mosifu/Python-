# 读文件
# 1.打开文件
# f = open("./resources/古诗.txt","r", encoding="utf-8")
#
# # 2.读取内容
# # content = f.read()  # 读取所有内容
# # print(content)
#
# content_list = f.readlines()
# for i in content_list:
#     print(i.strip())
#
# # 3.关闭文件
# f.close()

# 写文件  文件不存在会直接创建,文件存在会覆盖
# 1.打开文件
# f = open("./resources/静夜诗.txt","w", encoding="utf-8")
#
# # 2.写入内容
# f.write("静夜诗(李白)\n\n")
# f.write("床前明月光\n")
# f.write("疑是地上霜\n")
# f.write("举头望明月\n")
# f.write("低头思故乡\n")

# 3.关闭文件
# f.close()

# ----------------------资源释放方式一---------------------
# 1.打开文件
f = open("./resources/静夜诗.txt","w", encoding="utf-8")

# 2.写入内容
try:
    f.write("静夜诗(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
finally:
    # 3.关闭文件
    f.close()


# ----------------------资源释放方式二（项目最推荐使用）---------------------
"""
    相对路径:从当前文件所在目录开始查找(推荐)
        ./可以省略
        .:当前目录---->./resources/望庐山瀑布.txt
        ..:上一级目录----->../第2章/file/寻隐者不遇.txt---->.../../第2章/file/寻隐者不遇.txt
    绝对路径:从文件系统根目录开始查找,文件位置的完整路径(注意:反斜杠在字符串中表示的是转义字符,\n\t)
        方式一:D:\\Python-Project\\py_project01\\第3章\\'resources\\望庐山瀑布.txt
        方式二:D:/Python-Project/py_project01/第3章/resources/望庐山瀑布.txt
"""

# 1.打开文件    with上下文管理器，使得资源总能正确释放
##写文件
#a:append,追加内容;w:write,覆盖内容;------>文件不存在,则创建文件;
with open("./resources/静夜诗.txt","a", encoding="utf-8") as f:
    # 2.写入内容
    f.write("静夜诗(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
