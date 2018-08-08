import urllib.request
import ssl

# 解决访问Https时不受信任SSL证书问题
# ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com/'

# 如何定制UA
# 在这个头部不仅可以定制ua，还可以定制其他的请求头部，一般只需要定制ua
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

# 发送请求，直接打开这个请求对象即可
response = urllib.request.urlopen(request)