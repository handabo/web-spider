import requests

'''
url = 'https://www.baidu.com/s?'
data = {
    'ie': 'utf8',
    'wd': '王力宏'
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

r = requests.get(url, params=data, headers=headers)
'''
# print(r)

# print(r.text)
# print(r.content)       # 字节格式内容
# print(r.url)           # 获取发送请求的url
# print(r.status_code)   # 获取响应状态码
# print(r.headers)       # 获取响应头
# r.encoding = 'gbk'
# print(r.encoding)

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r = requests.get(url=url, headers=headers)
# print(r.text)
print(type(r.json()))