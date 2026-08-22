# csv文件操作 - 方式一：原始的文件操作方式
# 写入
# with open("csv_data/01.csv",'w', encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")    # 写入表头
#     f.write("小王,18,男,'football,Java'\n")   # 写入数据
#     f.write("小李,23,女,Python\n")
#     f.write("小兰,22,女,唱歌\n")
#     f.write("小王,32,男,踢足球\n")
#
# # 读
# with open("csv_data/01.csv",'r', encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# csv文件操作 - 方式二:csv库(推荐)
import csv

# 写
with open('csv_data/02.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    writer.writeheader()    # 写入表头
    writer.writerow({"姓名":"mo", "年龄":"23", "性别":"男", "爱好":"Java"})  #写入数据
    writer.writerow({"姓名":"lan", "年龄":"22", "性别":"女", "爱好":"化妆"})
    writer.writerow({"姓名":"gong", "年龄":"26", "性别":"女", "爱好":"追星"})
    writer.writerow({"姓名":"he", "年龄":"22", "性别":"女", "爱好":"听音乐"})

# 读
with open('csv_data/02.csv', 'r', newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
