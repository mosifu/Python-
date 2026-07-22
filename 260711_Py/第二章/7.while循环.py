# 使用while循环，打印十遍：“人生苦短，我用python”
i = 0
while i<10:
    i +=1
    print("人生苦短，我用Python！")
else:
    print("循环结束")

# while案例：计算1-100所有偶数的和
i = 1
num = 0
while i <= 100:
    if i % 2 == 0:
       num += i
    i += 1
print(f"计算1-100之间所有偶数和为:{num}")