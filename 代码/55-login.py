import requests
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
import pytesseract
import time

def shibie(image_path):
    img = Image.open(image_path)
    # 转化为灰度图片
    img = img.convert('L')
    # 二值化处理
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = img.point(table, '1')

    # out.show()
    # 识别图片
    img = img.convert('RGB')

    return pytesseract.image_to_string(img)

# 创建一个会话
s = requests.Session()

i = 1

while 1:
    login_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }
    r_log = s.get(url=login_url, headers=headers)

    # 将验证码图片下载到本地
    soup = BeautifulSoup(r_log.text, 'lxml')
    image_src = 'https://so.gushiwen.org' + soup.find('img', id="imgCode")['src']
    # urllib.request.urlretrieve(image_src, 'code.png')
    r_image = s.get(image_src, headers=headers)
    with open('code.png', 'wb') as fp:
        fp.write(r_image.content)

    # 获取表单隐藏框中的值
    views = soup.find('input', id="__VIEWSTATE")['value']
    viewg = soup.find('input', id="__VIEWSTATEGENERATOR")['value']

    # 发送post请求
    # code = input('请输入验证码------')
    code = shibie('code.png')

    post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    formdata = {
        '__VIEWSTATE': views,
        '__VIEWSTATEGENERATOR': viewg,
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'email': '1090509990@qq.com',
        'pwd': '123456',
        'code': code,
        'denglu': '登录',
    }
    r_post = s.post(url=post_url, headers=headers, data=formdata)

    # with open('gushi.html', 'wb') as fp:
    #     fp.write(r_post.content)
    # 判断是否登录成功
    if '修改昵称' in r_post.text:
        print('亲，第%s次登录成功------' % i)
        break
    print('不好意思，第%s次登录失败' % i)
    i += 1
    time.sleep(2)