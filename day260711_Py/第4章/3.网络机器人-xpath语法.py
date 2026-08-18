from lxml import html

# 测试解析本地的html文件
with open("resource/花卉一览表.html","r",encoding="utf-8") as f:
    content_text = f.read()

    # 解析html文本将其转换成文档对象
    doc = html.document_fromstring(content_text)

    # 解析表头-xpath语法
    # / 单斜杠标识从根节点开始
    # th_list = doc.xpath("/html/body/div/table/thead/tr/th/text()")
    # //双斜杠标识从当前位置开始匹配
    th_list = doc.xpath("//table/thead/tr/th/text()")
    # 输出表头
    print(th_list)

    # tr[1]获取tr第一个标签的内容.(从1开始)
    tr_list = doc.xpath("//table/tbody/tr[1]/td/text()")
    print(tr_list)

    # tr[last()]匹配tr最后一个标签的内容.  tr[last()-1]匹配倒数第二个
    tr_list_last = doc.xpath("//table/tbody/tr[last()-1]/td/text()")
    print(tr_list_last)

    # h1[@style]中@用来匹配属性,
    h1_list = doc.xpath("//h1[@style]/text()")
    print(h1_list)
    # h1[@style='color: #5a8a7a'] 还可以匹配属性的值
    h1_list1 = doc.xpath("//h1[@style='color: #5a8a7a']/text()")
    print(h1_list1)

    # *:表示匹配任意标签
    h_list = doc.xpath("//*/td[@class='col-en']/text()")
    print(h_list)

    # @*:表示获取匹配标签的属性值
    td_a_list = doc.xpath("//*/td/@*")
    print(td_a_list)
