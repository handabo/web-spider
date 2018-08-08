import urllib.request

# 下载网页
url = 'http://www.baidu.com/'
# 模拟浏览器发送请求
response = urllib.request.urlopen(url)

# print(response.read().decode('utf8'))  # 字符串格式-->字节格式
# print(response.read().decode('gbk'))  # 字节格式-->字符串格式
# print(response.url)  # 获取请求url
# print(response.headers)  # 响应头部
# print(response.status)  # 状态码

# 第一种
# with open('baidu1.html', 'w', encoding='utf8') as fp:
#     fp.write(response.read().decode('utf8'))

# 第二种
# with open('baidu2.html', 'wb') as fp:
#     fp.write(response.read())

# 第三种
# 向url发送请求，直接将响应写入到filepath中
urllib.request.urlretrieve(url, 'baidu3.html')


'''
# 下载图片
url = 'https://timgsa.baidu.com/timg?image&quality=' \
      '80&size=b9999_10000&sec=1533639915215&di=' \
      '1bbd3901c9991b363ac0211dc861a909&imgtype=0&src=' \
      'http%3A%2F%2Fhbimg.b0.upaiyun.com%2F225a5f3f75' \
      'd1d4c59532704782eebd25d323fd801e57a-VlY5c4_fw658'

# 第一种方式，发送请求，获取响应
response = urllib.request.urlopen(url)

with open('meinv2.jpg', 'wb') as fp:
    fp.write(response.read())

# 第二种方式，
urllib.request.urlretrieve(url, 'meinv1.png')
'''