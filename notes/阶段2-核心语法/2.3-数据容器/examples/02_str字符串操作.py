"""
02 - str 字符串操作（索引/切片/常用方法/不可变性）
对应课程：第 43-46 集
生成时间: 2026-07-21
"""

# ===== 1. str 不可变 + 索引 =====
print("=== 1. 索引与不可变性 ===")

s = "Hello-Python"
print(f"s[0]  = {s[0]}")        # H
print(f"s[-1] = {s[-1]}")       # n

# s[0] = "h"  # TypeError: 'str' object does not support item assignment
s = "h" + s[1:]  # 正确方式：造新字符串
print(f"修改后: {s}")

# ===== 2. 切片 =====
print("\n=== 2. 切片 ===")

str1 = "Hello-Python"
print(f"str1[0:5]  = '{str1[0:5]}'")      # Hello
print(f"str1[:5]   = '{str1[:5]}'")       # Hello
print(f"str1[::2]  = '{str1[::2]}'")      # HloPto
print(f"str1[::-1] = '{str1[::-1]}'")     # 反转！

# 负步长 — 方向必须一致
print(f"str1[0:5:1]   = '{str1[0:5:1]}'")    # Hello（正步长）
print(f"str1[0:5:-1]  = '{str1[0:5:-1]}'")    # ''（空！方向不对）
print(f"str1[-8:-13:-1] = '{str1[-8:-13:-1]}'")  # oP-oll（正确方向）

# ===== 3. 常用方法 =====
print("\n=== 3. 常用方法 ===")

str2 = "  Hello-Python-Hello-World  "

print(f"原字符串:    '{str2}'")
print(f"find('Hello'): {str2.find('Hello')}")      # 2
print(f"count('Hello'): {str2.count('Hello')}")    # 2
print(f"split('-'):    {str2.split('-')}")         # ['  Hello', 'Python', ...]
print(f"upper():       '{str2.upper()}'")
print(f"lower():       '{str2.lower()}'")
print(f"strip():       '{str2.strip()}'")
print(f"startswith(' '): {str2.startswith(' ')}")   # True
print(f"endswith('d'):   {str2.endswith('d')}")    # True
print(f"replace('-','_'): '{str2.replace('-', '_')}'")
print(f"原字符串未变:   '{str2}'")  # 不可变性！

# ===== 4. 邮箱验证 =====
print("\n=== 4. 邮箱验证 ===")

def validate_email(email):
    """验证邮箱格式：恰好1个@ + 至少1个."""
    return email.count("@") == 1 and "." in email

# 测试
for email in ["test@example.com", "testexample.com", "a@b@c.com", "user@mail"]:
    status = "正确" if validate_email(email) else "错误"
    print(f"  {email:<25} → {status}")

# ===== 5. 回文判断 =====
print("\n=== 5. 回文判断 ===")

def is_palindrome(text):
    """判断字符串是否回文（两边对称）"""
    half = len(text) // 2           # 整除取一半
    return text[:half] == text[-1:-half-1:-1]

# 测试
cases = ["上海自来水来自海上", "黄山落叶松叶落山黄", "hello", "abba"]
for text in cases:
    result = "是回文" if is_palindrome(text) else "不是回文"
    print(f"  '{text}' → {result}")

# ===== 6. 反转大写 =====
print("\n=== 6. 反转+大写 ===")

inputs = ["hello", "python", "world"]
for word in inputs:
    reversed_upper = word[::-1].upper()
    print(f"  '{word}' → '{reversed_upper}'")
