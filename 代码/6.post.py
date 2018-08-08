import urllib.request
import urllib.parse

# 加密的接口, 需要破解
url = 'http://fanyi.baidu.com/v2transapi'

word = 'wolf'
# 表单数据
formdata = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '275695.55262',
    'token': 'a5e2996f38e1aaa937a84e81019023b1'
}
# 处理表单数据
formdata = urllib.parse.urlencode(formdata).encode('utf8')

headers = {
    'Accept': '*/*',
    # 将其注释掉，索要完整的格式
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 将其注释掉，让其自动计算即可
    # 'Content-Length': '121',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=AA77479082B11BA72802648B0AD3B1C2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=4C8031C00E37DFD83E8E4A6E5F7BF1DC:FG=1; PSTM=1533539730; PSINO=3; H_PS_PSSID=1451_26911_26431_21126_20928; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'Host': 'fanyi.baidu.com',
    'Origin': 'http://fanyi.baidu.com',
    'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# 构件请求对象
request = urllib.request.Request(url=url, headers=headers)

# 发送请求
response = urllib.request.urlopen(request, data=formdata)
print(response.read().decode('utf8'))
