import urllib.request

url = 'http://www.baidu.com/'

# 模拟发送请求
# response = urllib.request.urlopen(url)

# 要的是字符串格式的内容
# print(response.read().decode('utf8'))
# print(response.url)
# print(response.headers)
# print(response.status)

# 将获取的响应内容保存到文件中
# r w a  r+  w+  a+  rb  wb  ab

# 写入方式第一种
# with open('baidu1.html', 'w', encoding='utf8') as fp:
# 	fp.write(response.read().decode('utf8'))

# 写入方式第二种
# with open('baidu2.html', 'wb') as fp:
# 	fp.write(response.read())

# 发送请求，将内容写到文件中
urllib.request.urlretrieve(url, 'baidu3.html')
