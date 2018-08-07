import urllib.request

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1533639915215&di=1bbd3901c9991b363ac0211dc861a909&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F225a5f3f75d1d4c59532704782eebd25d323fd801e57a-VlY5c4_fw658'

# 第一种方式，发送请求，获取响应
# response = urllib.request.urlopen(url)

# with open('meinv.jpg', 'wb') as fp:
# 	fp.write(response.read())

# 第二种方式，
urllib.request.urlretrieve(url, 'meinv2.png')