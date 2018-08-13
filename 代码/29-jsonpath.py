import json
import jsonpath

fp = open('book.json', 'r', encoding='utf8')
string = fp.read()
fp.close()

obj = json.loads(string)

# 得到所有book的author
ret = jsonpath.jsonpath(obj, '$.store.book[*].author')
# 直接找到所有的author
# ret = jsonpath.jsonpath(obj, '$..author')
# # 得到store下面的所有的price
# ret = jsonpath.jsonpath(obj, '$.store..price')
# # 得到第3本书
# ret = jsonpath.jsonpath(obj, '$..book[2]')
# # 得到最后一本书
# ret = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
# #
print(ret)