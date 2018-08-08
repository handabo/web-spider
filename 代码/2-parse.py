import urllib.parse

# url = 'https://www.baidu.com/s?ie=UTF-8&wd=周杰伦'

# string = urllib.parse.quote(url)

# string1 = urllib.parse.unquote(string)

# print(string)
# print(string1)

# urlencode
url = 'https://www.baidu.com/s?'
# 将get参数写到这里
data = {
    'ie': 'utf8',
    'wd': '周杰伦'
}

query_string = urllib.parse.urlencode(data)
url += query_string
print(url)

'''
# 将data拼接到url的后面，组成完整的url
# 遍历这个字典，拼接为指定格式
lt = []
for k, v in data.items():
    value = k + '=' + v
    lt.append(value)
# 将lt用&符号拼接起来即可
query_string = '&'.join(lt)
url += query_string

print(url)
'''
