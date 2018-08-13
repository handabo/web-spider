import requests
import time

# 在代码中有没有一个东西和浏览器是一样的，能够保存cookie呢？下次发送的时候自动携带cookie

# 首先创建一个会话
s = requests.Session()

# 往下所有的请求，都是s里面的方法方法发送，那么就会自动保存cookie和携带cookie

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018741029602'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
formdata = {
	'email': '17701256561',
	'password': 'lizhibin666',
	'icode': '',
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVwDXbx3oN5RBHzVxzj2jwbsO3z8VmHcZ1HZQTdC3enq%26wd%3D%26eqid%3D834642bf0000b410000000055b6bac87',
}

r = s.post(post_url, data=formdata, headers=headers)

time.sleep(3)

get_url = 'http://www.renren.com/960481378/profile'

# r = s.get(url=get_url, headers=headers)

with open('renren.html', 'wb') as fp:
	fp.write(r.content)