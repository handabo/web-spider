import urllib.request


url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
handler = urllib.request.ProxyHandler(proxies={'http': '218.60.8.98:3129'})
opener = urllib.request.build_opener(handler)

r = opener.open(url)

with open('代理.html', 'wb') as fp:
    fp.write(r.read())