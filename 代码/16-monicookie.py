import urllib.request
import urllib.parse
import http.cookiejar

# 模拟浏览器中的cookie

# 首先创建一个cookiejar对象，用来保存cookie
ck = http.cookiejar.CookieJar()
# 根据ck创建一个handler
handler = urllib.request.HTTPCookieProcessor(ck)
opener = urllib.request.build_opener(handler)

# 往下所有的请求，都是opener.open()方法发送，那么就会自动保存cookie和携带cookie

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018741029602'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/68.0.3440.84 Safari/537.36',
}
request = urllib.request.Request(url=post_url, headers=headers)
formdata = {
    'email': '179878979',
    'password': '7578678',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVwDXbx3\oN5RBHzVxzj2jwbsO3z8VmHcZ1HZQTdC3enq%26wd%3D%26eqid%3D834642bf0000b410000000055b6bac87',
}

formdata = urllib.parse.urlencode(formdata).encode('utf8')

r = opener.open(request, data=formdata)

# print(r.read().decode('utf8'))
# 假如登录成功

get_url = 'http://www.renren.com/960481378/profile'

request = urllib.request.Request(url=get_url, headers=headers)

r = opener.open(request)

with open('renren.html', 'wb') as fp:
    fp.write(r.read())