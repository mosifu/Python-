import json

# 写入json数据文件
# user = {
#     "name": "mosifu",
#     "age": 18,
#     "gender": "男",
#     "hobbies": ["游泳", "跑步"]
# }
#
# with open("./resources/user.json", "w", encoding="utf-8") as f:
#     # ensure_ascii:默认为True,确保所有的数据输出的都是ASCII编码(非ASCII码会进行转义);False,非ASCII码保留原样输出
#     # indent:会在输出的json数据中添加缩进(格式化)
#     json.dump(user, f, ensure_ascii=False, indent=2)

# 读取json数据文件
with open("./resources/user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))