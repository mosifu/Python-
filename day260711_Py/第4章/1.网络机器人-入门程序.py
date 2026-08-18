import requests
from lxml import html

# 目标网页
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求
response = requests.get(target_url)

# 转换成html文档
doc = html.fromstring(response.text)

# 获取表头数据
# th_list = doc.xpath("//table[@id='top20']//th/text()")
# 可以从浏览器直接查找xpath路径
th_list = doc.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()")
print(th_list)


# 获取表格数据
td_list = doc.xpath("//table[@id='top20']//tbody/tr")
for tds in td_list:
    td = tds.xpath("./td/text()")
    print(td)
