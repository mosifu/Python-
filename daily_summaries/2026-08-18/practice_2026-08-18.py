"""
每日练习 — 2026-08-18
对应课程：阶段 4 网络爬虫，第 120-126 集
今日主题：requests 发送请求 + lxml 解析 + XPath 语法 + 前端三剑客基础

使用说明：
- 本文件为纯注释练习，不含可执行代码。
- 在每处 `# 我的回答：` 后面写你的答案（注释形式即可）。
- 巩固练习可另建 .py 文件实际编码验证。
"""


# ============================================================
# 巩固练习 1：防御性爬虫重写
# 涉及知识点：requests 请求头/超时/异常处理、response.encoding、
#             相对路径 xpath、if __name__ 守卫、类型标注
# 简要描述：今日 01_发送请求与解析.py 是裸请求（无 headers、无 timeout、
#           无 try/except、用绝对路径 xpath）。请重写为"生产可用"版本：
#           1. 加 User-Agent 请求头
#           2. 加 timeout=10
#           3. 用 try/except requests.RequestException 包裹请求
#           4. 设置 response.encoding = "utf-8"
#           5. 把绝对路径 xpath 改为相对路径 //table[@id='top20']//th
#           6. 加 if __name__ == '__main__': 守卫
#           7. 给所有变量/函数加类型标注
# 预计耗时：30-40 分钟
# ============================================================

# 我的回答：
# （在此写出你的重写方案，可直接写成可执行代码贴到单独 .py 文件中运行验证）




# ============================================================
# 巩固练习 2：表格结构化函数 + contains() 实操
# 涉及知识点：xpath 两步法、多值 class contains()、string() vs text()、
#             函数封装、返回 list[dict] 结构化数据
# 简要描述：写一个函数 parse_table(html_text: str, table_id: str) -> list[dict]，
#           功能：
#           1. 用 html.fromstring 解析 HTML 文本
#           2. 用 //table[@id='...']//th/text() 取表头作为字典 key
#           3. 用两步法（//tr 取行 → ./td 取格）取每行数据
#           4. 将每行组装为 {表头: 值} 的字典，返回列表
#           5. 额外：若某 <td> 内有嵌套 <span>（如 <td><span>A</span>B</td>），
#              用 string() 而非 /text() 取完整文本 "AB"，并思考为何 /text() 会漏
#           6. 额外：构造一个含多值 class 的 HTML 片段
#              （如 <div class="item active hot">），分别用 @class="active"
#              和 contains(@class, "active") 测试，记录哪个匹配成功
# 预计耗时：40-50 分钟
# ============================================================

# 我的回答：
# （在此写出函数实现思路与关键代码）




# ============================================================
# 自测题（共 6 题）
# ============================================================

# 题 1：XPath 索引
# 对于 HTML 表格的第 1、2、3 行，以下哪个 xpath 取的是"第 2 行"？
# A. //tr[0]/td/text()
# B. //tr[1]/td/text()
# C. //tr[2]/td/text()
# D. //tr[last()-2]/td/text()
# 我的回答：


# 题 2：多值 class 匹配
# HTML: <button class="mode-btn work active">工作</button>
# 以下哪个 xpath 能成功匹配该 button？（多选）
# A. //button[@class="work"]
# B. //button[@class="mode-btn work active"]
# C. //button[contains(@class, "work")]
# D. //button[contains(@class, "mode-btn")]
# 我的回答：


# 题 3：/text() 与 //text() 的区别（简答）
# 给定 HTML：<div class="box"><span>你好</span>世界</div>
# - doc.xpath('//div[@class="box"]/text()') 返回什么？
# - doc.xpath('//div[@class="box"]//text()') 返回什么？
# - 若想得到完整的 "你好世界" 一个字符串，应该用哪个 xpath 函数？
# 我的回答：


# 题 4：静态网页 vs 动态网页判断（简答）
# 你要用 requests 抓某电商商品价格，requests.get() 拿到的 HTML 源码里搜不到价格数据，
# 但浏览器页面上能看见价格。请判断这是静态还是动态网页，并说明接下来该怎么抓。
# 我的回答：


# 题 5：requests 响应属性
# 以下哪个不是 requests.Response 对象的常用属性？
# A. response.text
# B. response.content
# C. response.html
# D. response.status_code
# 我的回答：


# 题 6：为什么用 contains(@class, ...) 而不是 @class="..."？（简答）
# 请用自己的话解释：为什么 HTML 的 class 是多值时，
# xpath 用 @class="某值" 会匹配失败，而 contains(@class, "某值") 能成功？
# 提示：从"class 属性的值到底是什么字符串"角度思考。
# 我的回答：


# ============================================================
# 练习完成自检（做完后对照）
# ============================================================

# [ ] 巩固练习 1：是否 7 项防御性改进全部落实？
# [ ] 巩固练习 2：函数是否返回 list[dict]？contains() 实操是否完成？
# [ ] 自测题 1：xpath 索引从 1 开始，你答对了吗？
# [ ] 自测题 2：多值 class 的 @class="..." 只有完整匹配才成功，你选对了吗？
# [ ] 自测题 3：/text() 只取直接子文本，//text() 取所有后代文本，string() 拼接——记住了吗？
# [ ] 自测题 4：动态网页需找 XHR 接口或用 Selenium，你说清楚了吗？
# [ ] 自测题 5：requests 没有 .html 属性（那是 BeautifulSoup 的思路），你避开了吗？
# [ ] 自测题 6：class 的值是完整字符串 "mode-btn work active"，= 要求完全相等——你解释对了吗？
