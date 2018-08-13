import requests

url = 'http://www.baidu.com/#ie=UTF-8&wd=ip'
proxies = {
    'http': "http://121.43.170.207:3128",
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r = requests.get(url=url, headers=headers)
with open('ip.html', 'wb') as fp:
    fp.write(r.content)