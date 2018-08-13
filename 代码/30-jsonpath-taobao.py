import json
import jsonpath
import urllib.request

url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=562099309982&spuId=893336129&sellerId=2616970884&order=3&currentPage=2'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
content = urllib.request.urlopen(request).read().decode('gbk')
content = '{' + content + '}'
# print(content)
fp = open('taobao.txt', 'w', encoding='utf8')
obj = json.loads(content)
# print(type(obj))
# 找到所有的评论列表
comments_list = obj['rateDetail']['rateList']
# 遍历列表，依次获取每一个评论内容
for com_obj in comments_list:
    # 评论内容
    comment = com_obj['rateContent']
    # 用户名
    name = jsonpath.jsonpath(com_obj, '$..displayUserNick')[0]
    # 上传照片
    images = jsonpath.jsonpath(com_obj, '$..pics')[0]
    # 评论时间
    tt = jsonpath.jsonpath(com_obj, '$..rateDate')[0]
    # print(images)
    # print('*' * 50)
    item = {
        '评论内容': comment,
        '用户名': name,
        '照片': images,
        '评论时间': tt
    }
    fp.write(str(item) + '\n')

fp.close()

