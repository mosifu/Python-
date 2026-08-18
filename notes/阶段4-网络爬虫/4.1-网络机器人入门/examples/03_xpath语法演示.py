# 生成时间: 2026-08-18
# 来源：学习者跟练代码（第4章/3.网络机器人-xpath语法.py）
# 知识点：xpath 常用语法（/、//、索引、属性匹配、*、@*）
# 说明：需准备 resource/花卉一览表.html 文件

from lxml import html

# 测试解析本地的html文件
with open("resource/花卉一览表.html","r",encoding="utf-8") as f:
    content_text = f.read()

    # 解析html文本将其转换成文档对象
    doc = html.document_fromstring(content_text)

    # 解析表头-xpath语法
    th_list = doc.xpath("//table/thead/tr/th/text()")

    # 输出表头
    print(th_list)

    # 解析表格内的数据，先把表格标签的统一获取
    body_tr_list = doc.xpath("//table/tbody/tr")
    for td in body_tr_list:
        # 获取表格里面每行td内容
        td_list = td.xpath("./td/text()")
        print(td_list)
