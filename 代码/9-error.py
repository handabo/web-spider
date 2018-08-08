import urllib.request
import urllib.error

'''
url = 'http://www.maodan.com/'
# response = urllib.request.urlopen(url)
try:
    response = urllib.request.urlopen(url)
# except Exception as e:
except urllib.error.URLError as e:
# except NameError as e:   这个不能捕获
    print(e)

print('不影响这一句代码的运行')
'''
# Exception > URLError > HTTPError
url = 'https://www.cnblogs.com/fh-fendou/p/7479811.html'

try:
    response = urllib.request.urlopen(url)
# except urllib.error.HTTPError as e:
except (urllib.error.URLError, urllib.error.HTTPError) as e:
    print(e)
    print('httperror')
# except urllib.error.URLError as e:
# 	print(e)
# 	print('urlerror')

print('正常运行')
