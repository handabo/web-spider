import urllib.request
import urllib.parse

url = 'http://fanyi.baidu.com/sug'
# 将表单数据写成一个字典
formdata = {
	'kw': 'baby'
}
# 将formdata单独处理一下
formdata = urllib.parse.urlencode(formdata).encode('utf8')

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, data=formdata)

print(response.read().decode('utf8'))