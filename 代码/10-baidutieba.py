import urllib.request
import urllib.parse
import os
import time


def main():
    baming = input('请输入要爬取的贴吧的名字:')
    start_page = int(input('请输入要爬取的起始页码:'))
    end_page = int(input('请输入要爬取的结束页码:'))
    url = 'https://tieba.baidu.com/f?'

    for page in range(start_page, end_page + 1):
        print('正在爬取第%s页......' % page)
        # 根据url和page拼接指定页码的url
        request = handle_request(page, baming, url)
        # 根据请求对象发送请求得到响应写入到指定的文件中
        down_load(request, baming, page)
        print('结束爬取第%s页' % page)
        time.sleep(3)

def down_load(request, baming, page):
    response = urllib.request.urlopen(request)
    # 通过代码创建指定的文件夹
    dirname = baming
    # 判断不存在的时候创建
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    # 文件的名字
    filename = '第%s页.html' % page
    # 得到文件的路径
    filepath = os.path.join(dirname, filename)
    # 将内容直接写入到filepath中
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def handle_request(page, baming, url):
    pn = (page-1) * 50
    # 拼接url
    data = {
        'kw': baming,
        'ie': 'utf8',
        'pn': pn
    }
    url += urllib.parse.urlencode(data)
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 构建请求对象
    request = urllib.request.Request(url, headers=headers)
    return request


if __name__ == '__main__':
    main()