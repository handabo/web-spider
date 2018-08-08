import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
city = input('请输入要搜索的城市:')
data = {
    'cname': city,
    'pid': '',
    'pageIndex': '1',
    'pageSize': '10'
}
data = urllib.parse.urlencode(data).encode('utf8')
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request, data=data)

print(response.read().decode('utf8'))