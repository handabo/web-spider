import urllib.request
import urllib.parse
import re
import time
import os


def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    url = 'https://www.qiushibaike.com/pic/page/{}/'
    for page in range(start_page, end_page + 1):
        print('正在下载第%s页......' % page)
        # 拼接url，构建请求对象
        request = handle_request(url, page)
        # 发送请求，获取响应
        content = urllib.request.urlopen(request).read().decode('utf8')
        # 正则解析内容
        parse_content(content)
        print('结束下载第%s页' % page)
        # 休眠时间
        time.sleep(2)


# 请求函数
def handle_request(url, page):
    # 拼接url
    url = url.format(page)
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 正则解析函数
def parse_content(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt="(.*?)" />.*?</div>', re.S)
    ret = pattern.findall(content)
    # print(ret)
    # print(len(ret))
    # 遍历这个列表，依次下载每一个图片
    for tp in ret:
        # 取出图片的链接
        image_src = 'https:' + tp[0]
        # 取出图片的名字
        name = tp[1]
        # 保存图片
        dirname = 'qiutu'
        filename = name + '.' + image_src.split('.')[-1]
        filepath = os.path.join(dirname, filename)
        print('正在下载%s..' % filename)
        urllib.request.urlretrieve(image_src, filepath)
        print('结束下载%s' % filename)
        time.sleep(2)


if __name__ == '__main__':
    main()