"""
02 - match 模式匹配（match-case / 多值 | / if 守卫 / 通配符 _）
对应课程：第 26-27 集
需要 Python 3.10+
生成时间: 2026-07-16
"""

# ===== 1. 基本 match...case =====
print("=== 1. 基本 match...case ===")

day = "3"
match day:
    case "1":
        print("星期一，上班日")
    case "2":
        print("星期二，项目日")
    case "3":
        print("星期三，研发日")
    case "4":
        print("星期四，研讨日")
    case "5":
        print("星期五，摸鱼日")
    case "6" | "7":           # | = 匹配多个值
        print("周末，休息日")
    case _:                    # _ = default（通配符）
        print("输入日期不存在")

# ===== 2. case 守卫（if 条件）=====
print("\n=== 2. case 守卫 ===")

# 计算器 — 防止除零
a, b = 10, 0
operator = "/"

match operator:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/" if b != 0:     # ← 守卫：b不为0才匹配
        print(f"{a} / {b} = {a / b}")
    case "/":                # b == 0 走这里
        print("错误：除数不能为 0！")
    case _:
        print(f"未知运算符: {operator}")

# 正常除法演示
b = 2
match "/":
    case "/" if b != 0:
        print(f"正常除法: {a} / {b} = {a / b}")

# ===== 3. 综合案例：游戏角色控制 =====
print("\n=== 3. 游戏角色控制 ===")

def move_character(command):
    """根据指令控制角色移动"""
    match command:
        case "w" | "W" | "上":
            return "角色向上移动"
        case "s" | "S" | "下":
            return "角色向下移动"
        case "a" | "A" | "左":
            return "角色向左移动"
        case "d" | "D" | "右":
            return "角色向右移动"
        case " " | "跳":
            return "角色跳跃"
        case "j" | "J" | "攻击":
            return "角色发动攻击"
        case "esc" | "ESC" | "退出":
            return "退出游戏"
        case _:
            return f"无效指令: {command}"

# 测试各种指令
commands = ["w", "S", "左", "D", " ", "J", "esc", "x"]
for cmd in commands:
    print(f"  输入 '{cmd}' → {move_character(cmd)}")

# ===== 4. Python match vs Java switch =====
print("\n=== 4. match vs switch 速查 ===")
print(f"{'Python match':<35} {'Java switch':<35}")
print(f"{'不用 break，自动不穿透':<35} {'必须 break，否则穿透':<35}")
print(f"{'case _: (通配符)':<35} {'default:':<35}")
print(f"{'case \"6\" | \"7\":':<35} {'case \"6\": case \"7\":':<35}")
print(f"{'case \"/\" if b != 0:':<35} {'(不支持 guard)':<35}")
print(f"{'match 后面可以是任意表达式':<35} {'switch 只支持整数/字符串/枚举':<35}")
