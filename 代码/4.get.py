import urllib.request
import urllib.parse

# 让用户输入搜索关键字
keyword = input('请输入要搜索的关键字:')
url = 'https://www.baidu.com/s?'
# get参数
data = {
	'ie': 'utf8',
	'wd': keyword,
}
query_string = urllib.parse.urlencode(data)

url += query_string

# 向url发送请求，得到响应
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request)

# 拼接文件名字
filename = keyword + '.html'
# 写入到文件中

with open(filename, 'wb') as fp:
	fp.write(response.read())
