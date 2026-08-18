"""
01 - if 条件判断（if / if-else / if-elif-else / 嵌套if）
对应课程：第 22-25 集
生成时间: 2026-07-16
"""

# ===== 1. 基本 if（单分支）=====
print("=== 1. 基本 if ===")

score = 689
if score > 680:
    print("我去读清华")
    print("超过680的都来读")
print("----------")  # 这行不在 if 里

# ===== 2. if...else（双分支）=====
print("\n=== 2. if...else ===")

age = 17
if age >= 18:
    print("已成年")
else:
    print("未成年")

# ===== 3. if...elif...else（多分支）=====
print("\n=== 3. if...elif...else ===")

# 登录验证
right_account = "188888888"
right_password = "6666666"

# 用硬编码演示（实际使用 input()）
account = "188888888"
password = "6666666"

if account == right_account and password == right_password:
    print("登录成功！")
else:
    print("账号或密码错误！")

# 闰年判断
year = 2024
if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 是平年")

# ===== 4. 多用户登录（多 elif）=====
print("\n=== 4. 多分支登录 ===")

user = "mosifu"
pwd = "666"

if user == "admin" and pwd == "666888":
    print("admin 登录成功")
elif user == "root" and pwd == "12345":
    print("root 登录成功")
elif user == "mosifu" and pwd == "666":
    print("mosifu 登录成功")
else:
    print("用户名或密码错误")

# ===== 5. 嵌套 if：三角形判断 =====
print("\n=== 5. 嵌套 if ===")

a, b, c = 3, 3, 5
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print(f"{a},{b},{c} 等边三角形")
    elif a == b or b == c or a == c:
        print(f"{a},{b},{c} 等腰三角形")
    else:
        print(f"{a},{b},{c} 普通三角形")
else:
    print(f"{a},{b},{c} 不能构成三角形")

# ===== 6. 综合练习 =====
print("\n=== 6. 综合练习 ===")

# 成绩等级评定
score = 83
if score >= 85:
    grade = "优秀"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"成绩 {score} → {grade}")

# 购物折扣计算
money = 350
if money >= 500:
    pay = money * 0.8
elif money >= 300:
    pay = money * 0.9
elif money >= 100:
    pay = money * 0.95
else:
    pay = money
print(f"原价 {money} → 实付 {pay}")

# 阶梯电费（2880以下: 0.4883, 2880-4800: 0.5383, 4800以上: 0.7883）
total = 5000
if total < 2880:
    fee = total * 0.4883
elif total <= 4800:
    fee = 2880 * 0.4883 + (total - 2880) * 0.5383
else:
    fee = 2880 * 0.4883 + (4800 - 2880) * 0.5383 + (total - 4800) * 0.7883
print(f"用电 {total} 度 → 电费 {fee:.2f} 元")

# ===== 7. pass 占位符 =====
print("\n=== 7. pass 占位符 ===")

x = 10
if x > 0:
    pass  # TODO: 待实现，先占位
else:
    print("x 不是正数")
print("程序继续运行...")
