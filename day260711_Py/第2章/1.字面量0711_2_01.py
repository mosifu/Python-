#字面量
print(100) #整型(int)
print(3.14) #浮点型(float)
print(True) #布尔型(True)
print(False) #布尔型(False)
print("Hello World") #字符型(Str)
print(None) #空值(None)

#布尔型本质也是整型,与整型计算时(True->1, False->0)
print(True + 1) #->1 + 1
print(False - 1) #->0 - 1

#变量
#现有一个视频播放量为45.8万的视频,每个月的新增播放量为30万,那么未来两个月的播放量是多少
base , incr = 45.8 , 30 #可以一次性定义多个变量,用逗号(,)隔开
print("未来第一个月的视频播放量", base+incr)
print("未来第二个月的视频播放量", base+incr+incr)