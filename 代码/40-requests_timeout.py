import requests
from requests.exceptions import Timeout

url = 'http://www.baidu.com/'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

try:
    r = requests.get(url=url, headers=headers, timeout=0.01)
except Timeout as e:
    print(e)
    print('请求超时')
