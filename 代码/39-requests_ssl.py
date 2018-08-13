import requests
# 忽略警告
from requests.packages import urllib3
urllib3.disable_warnings()

url = 'https://www.12306.cn/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 取消证书验证
r = requests.get(url=url, headers=headers, verify=False)