import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
print('每页显示10条数据')
page = int(input('请输入页码:'))
# 根据page计算出来start和limit
start = (page-1) * 10
limit = 10
data = {
    'start': start,
    'limit': limit,
}
url += urllib.parse.urlencode(data)

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))