#1.导入模块 --> import ...  调用方式：模块名.功能名 / 别名.功能名
import random
import random as rd

for i in range(100):
    print(random.randint(1, 100))    #包含1和100
    