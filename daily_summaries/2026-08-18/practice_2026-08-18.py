# 每日练习 - 2026-08-18
# 主题：网络爬虫入门（requests + lxml + xpath，第120-126集）
# 说明：纯注释练习文件，请在每题的"我的回答"后填写

# ============================================================
# 第一部分：巩固练习
# ============================================================

# -------- 练习 1：发送请求与解析 --------
#
# 涉及知识点：requests.get、html.fromstring、response.text
#
# 题目描述：
#   补全下面的代码：请求 https://www.tiobe.com/tiobe-index/ ，
#   把响应解析成 lxml 文档对象，并取出页面 <title> 标签的文本。
#
#   import requests
#   from lxml import html
#
#   url = "https://www.tiobe.com/tiobe-index/"
#   # 1. 发送请求
#   response = ____
#   # 2. 解析成文档对象
#   doc = ____
#   # 3. 取 title 文本（注意 xpath 返回的是列表）
#   title = ____
#   print(title)
#
# 我的回答：


# -------- 练习 2：xpath 路径与索引 --------
#
# 涉及知识点：/、//、索引从1开始、last()
#
# 题目描述：
#   针对一个表格 HTML，写出下列需求的 xpath（只写 xpath 字符串）：
#   1. 取所有表头单元格（th）的文本
#   2. 取 tbody 第 1 行的所有 td 文本
#   3. 取 tbody 最后一行的所有 td 文本
#   4. 取 tbody 倒数第 2 行的所有 td 文本
#
#   <table id="data">
#     <thead><tr><th>名称</th><th>评分</th></tr></thead>
#     <tbody>
#       <tr><td>电影A</td><td>9.0</td></tr>
#       <tr><td>电影B</td><td>8.5</td></tr>
#       <tr><td>电影C</td><td>7.2</td></tr>
#     </tbody>
#   </table>
#
# 我的回答：
# 1.
# 2.
# 3.
# 4.


# -------- 练习 3：属性匹配与多值 class --------
#
# 涉及知识点：@属性、contains()、多值 class
#
# 题目描述：
#   针对下面的 HTML，写出 xpath 取出"当前激活按钮"的文本。
#   并说明为什么不能写 //button[@class="work"]。
#
#   <div class="modes">
#     <button class="mode-btn work active" data-mode="work">工作</button>
#     <button class="mode-btn short" data-mode="short">短休息</button>
#     <button class="mode-btn long" data-mode="long">长休息</button>
#   </div>
#
# 我的回答：


# -------- 练习 4：取文本 vs 取属性 --------
#
# 涉及知识点：/text()、/@属性、@*
#
# 题目描述：
#   针对下面的 HTML，分别写出 xpath：
#   1. 取"Python教程"这个文本
#   2. 取 a 标签的 href 属性值
#   3. 取 div 下所有标签的所有属性值
#
#   <div class="card">
#     <a href="https://xxx.com/python" class="link">Python教程</a>
#     <img src="logo.png" alt="logo">
#   </div>
#
# 我的回答：
# 1.
# 2.
# 3.


# -------- 练习 5：表格两步法爬取 --------
#
# 涉及知识点：先取行集合，再循环取单元格
#
# 题目描述：
#   补全代码：用"两步法"爬取表格所有行的数据，每行打印一个 td 文本列表。
#
#   # 1. 取出 tbody 下所有 tr（行集合）
#   tr_list = doc.xpath("____")
#   # 2. 循环每行，取该行下所有 td 的文本
#   for tr in tr_list:
#       row = tr.xpath("____")
#       print(row)
#
# 我的回答：


# ============================================================
# 第二部分：自测题（共 5 题）
# ============================================================

# ---------- 第 1 题 ----------
# xpath 中 tr[1] 表示什么？
# A. 第 0 行（和 Python 列表一样从 0 开始）
# B. 第 1 行（xpath 索引从 1 开始）
# C. 最后 1 行
# D. 随机一行
#
# 我的回答：


# ---------- 第 2 题 ----------
# doc.xpath("//div[@class='box']/text()") 的返回类型是？
# A. 字符串  B. 列表  C. 字典  D. 元素对象
#
# 我的回答：


# ---------- 第 3 题 ----------
# HTML 中 <button class="mode-btn work active">，要匹配这个按钮，正确写法是？
# A. //button[@class="work"]
# B. //button[@class="mode-btn work active"]
# C. //button[contains(@class, "work")]
# D. B 和 C 都可以
#
# 我的回答：


# ---------- 第 4 题 ----------
# xpath 中 / 和 // 的区别是？
# A. 没区别
# B. / 是直接子节点，// 是任意后代节点
# C. / 是任意后代，// 是直接子节点
# D. / 是属性，// 是文本
#
# 我的回答：


# ---------- 第 5 题 ----------
# requests 抓不到网页数据，最可能的原因是（多选）？
# A. 该网页数据是 JS 动态加载的，HTML 源码里没有
# B. 没加 User-Agent 被反爬拒绝
# C. xpath 写错了
# D. 网络不通
#
# 我的回答：


# ============================================================
# 自测答案（写完后对照检查）
# ============================================================
# 第1题：B（xpath 索引从 1 开始，和 Python/Java 数组不同）
# 第2题：B（xpath() 永远返回列表，即使只匹配一个）
# 第3题：D（完整匹配用 =，部分匹配用 contains）
# 第4题：B（/ 直接子节点，// 任意后代）
# 第5题：A/B/C/D 都可能（动态加载、反爬、xpath 错、网络问题都会导致抓不到）
# ============================================================
