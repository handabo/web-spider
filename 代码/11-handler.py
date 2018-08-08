import urllib.request

url = 'http://www.baidu.com/'
# 创建handler
handler = urllib.request.HTTPHandler()
# 根据handler创建opener
opener = urllib.request.build_opener(handler)

# 发送请求的时候，不要使用urlopen发送，使用opener.open()
response = opener.open(url)

print(response.read().decode('utf8'))