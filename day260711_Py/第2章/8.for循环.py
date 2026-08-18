# for循环遍历字符串，打印输出
# msg = input("请输入需要遍历的字符串：")
# for i in msg:
#     print(f"元素：{i}")
# else:
#     print("遍历结束~")

#for循环和while循环的应用场景---需补充

# for循环案例： 实现1-100之间，所有奇数之和
#range()生成指定的数字序列.range(end) -> 从0开始不包含end; range(start, end) -> 从start到end之前; range(start, end, step)
# num = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         num += i
# print(f"1-100之间奇数和为:{num}")
#简化
# num = 0
# for i in range(1, 101, 2):
#     num += i
# print(f"1-100之间奇数和为:{num}")


#for循环案例: 计算100-500之间,所有3的倍数的数字之和
# num = 0
# for i in range(100, 501):
#     if i % 3 == 0:
#         num += i
# print(f"300-500之间所有3的倍数的数字之和为:{num}")

