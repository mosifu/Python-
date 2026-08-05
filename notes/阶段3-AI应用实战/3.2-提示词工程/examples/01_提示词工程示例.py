"""
01 - 提示词工程示例（优化前 vs 优化后对比）
对应课程：第 99 集
生成时间: 2026-07-29
"""

import os
from openai import OpenAI

# 创建客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY', ''),
    base_url="https://api.deepseek.com"
)


def ask(prompt, model="deepseek-chat"):
    """调用大模型"""
    if not os.environ.get('DEEPSEEK_API_KEY'):
        return "[未设置 DEEPSEEK_API_KEY，跳过实际调用]"

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1024
    )
    return response.choices[0].message.content


# ===== 1. 优化前 vs 优化后：学习助手 =====
print("=" * 60)
print("示例1：学习助手")
print("=" * 60)

# ❌ 优化前
bad_prompt = "帮我讲一下 Python 的装饰器"
print(f"\n❌ 优化前：{bad_prompt}")
# print(f"回答：{ask(bad_prompt)}")

# ✅ 优化后
good_prompt = """【角色】
你是一位有10年经验的 Python 技术讲师，擅长用生活化类比解释抽象概念。
你的学员有 Java 基础，正在学习 Python 进阶。

【任务】
讲解 Python 装饰器（decorator），包括：
1. 装饰器是什么（用一个生活类比）
2. 为什么需要装饰器（解决什么问题）
3. 基本语法和执行流程
4. 一个实际应用场景（如计时器）

【要求】
- 每个概念用 Java 对比
- 代码可直接运行，附中文注释
- 分4个小节，每节有标题
- 不超过800字，不讲带参数的装饰器
"""
print(f"\n✅ 优化后（提示词已展示，取消注释可调用）")
# print(f"回答：{ask(good_prompt)}")


# ===== 2. 代码审查提示词 =====
print("\n" + "=" * 60)
print("示例2：代码审查")
print("=" * 60)

code_review_prompt = """【角色】你是严谨的 Python 代码审查员。

【任务】审查以下代码：语法/逻辑/规范/性能

【要求】
- 格式：✅/❌ 问题 -> 修正建议
- 按严重程度排序：致命 > 警告 > 建议
- 只指出问题，不重写整段代码

【约束】不引入高级特性

【代码】
def calc(a, b):
    return a / b

print(calc(10, 0))
"""
print(f"提示词已构建，取消注释可调用")
# print(ask(code_review_prompt))


# ===== 3. 格式化输出提示词 =====
print("\n" + "=" * 60)
print("示例3：格式化输出")
print("=" * 60)

format_prompt = """【角色】你是 AI 技术分析师。

【任务】对比 DeepSeek 和 ChatGPT。

【要求】按以下表格输出，不加其他文字：

| 对比维度 | DeepSeek | ChatGPT |
|---------|----------|---------|
| 开发公司 | | |
| 上下文长度 | | |
| 中文能力 | | |
| API 价格 | | |
| 开源情况 | | |

【约束】不确定的填"待确认"，不编造
"""
print(f"提示词已构建，取消注释可调用")
# print(ask(format_prompt))


# ===== 4. 思维链提示词 =====
print("\n" + "=" * 60)
print("示例4：思维链（先想后答）")
print("=" * 60)

cot_prompt = """【角色】你是 Python 后端架构师。

【背景】购物车系统：shop = {"商品名": {"price": 单价, "num": 数量}}

【任务】添加满减优惠功能，按以下步骤思考：

第一步：分析需求（满减规则、作用范围）
第二步：设计方案（列2种方案，对比优劣）
第三步：给出推荐方案代码（附注释，考虑边界）

【要求】每步先输出思考过程，再输出结论
"""
print(f"提示词已构建，取消注释可调用")
# print(ask(cot_prompt))


# ===== 5. 提示词工程速查表 =====
print("\n" + "=" * 60)
print("提示词工程速查表")
print("=" * 60)

tips = [
    ("角色设定", "你是XX专家", "每次都写"),
    ("背景信息", "用户是Java背景", "需要个性化时"),
    ("任务拆解", "分3步完成", "复杂任务"),
    ("输出格式", "用表格输出", "需要结构化时"),
    ("Few-shot", "参考这个例子", "需要特定风格时"),
    ("约束限制", "不超过200字", "需要控制输出时"),
    ("思维链", "先分析再回答", "推理/分析类任务"),
    ("否定指令", "不要用XX", "防止不良输出"),
    ("迭代反馈", "不确定就问我", "需求模糊时"),
]

for i, (name, desc, when) in enumerate(tips, 1):
    print(f"  {i}. {name:<8} {desc:<16} -> {when}")

print("\n💡 使用方法：取消上方注释，设置 DEEPSEEK_API_KEY 后运行")
