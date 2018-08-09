import urllib.request
import random
import time

url = 'http://www.baidu.com/#ie=UTF-8&wd=ip'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)

# 读取文件
fp = open('pool.txt', 'r')
string = fp.read()
fp.close()

# print(string)
# 将字符串按照换行符切割，得到一个列表，列表里面就是一个一个的代理服务器
lt = string.splitlines()

# print(lt)
while True:
	# 从列表中随机抽取一个代理
	daili = random.choice(lt)
	# 发送请求
	proxy = {'http': daili}
	# 创建handler
	handler = urllib.request.ProxyHandler(proxies=proxy)
	# 创建opener
	opener = urllib.request.build_opener(handler)

	try:
		response = opener.open(request)
		print('使用代理%s成功' % daili)

		with open('ip.html', 'wb') as fp:
			fp.write(response.read())
		break
	except Exception as e:
		# 将这个代理从你的列表移除
		lt.remove(daili)
		print('使用代理%s失败' % daili)
	time.sleep(2)
