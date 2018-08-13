import json

lt = [
    {'name': '王静', 'age': '7', 'height': 130},
    {'name': '闫晓红', 'age': 13, 'height': 160},
    {'name': '刘惠芬', 'age': 16, 'height': 158},
    {'name': '赵铁柱', 'age': 20, 'height': 170}
]

string = json.dumps(lt, ensure_ascii=False)

# print(string)
obj = json.loads(string)

print(type(obj))