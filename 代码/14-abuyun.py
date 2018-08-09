import urllib.request
import base64

user = 'HCQ4X00T441PYI5D'
pwd = 'E8C159C7668242ED'

# 将用户名和密码拼接后再转化
string = user + ':' + pwd
# 进行base64编码
ret = 'Basic ' + base64.b64encode(string.encode('utf8')).decode('utf8')
# print(ret)

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'Proxy-Authorization': ret
}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

#
handler = urllib.request.ProxyHandler(proxies={'http': 'http-dyn.abuyun.com:9020'})
opener = urllib.request.build_opener(handler)

r = opener.open(request)

with open('ip.html', 'wb') as fp:
    fp.write(r.read())