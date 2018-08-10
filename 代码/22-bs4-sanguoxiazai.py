import urllib.request
import time
from bs4 import BeautifulSoup


def parse_first():
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    request = handle_request(url)
    # 发送请求，得到响应
    content = urllib.request.urlopen(request).read().decode('utf8')
    # 解析内容
    soup = BeautifulSoup(content, 'lxml')
    # 得到所有的章节链接
    oa_list = soup.select('.book-mulu > ul > li > a')
    fp = open('三国演义.txt', 'w', encoding='utf8')
    # print(oa_list)
    # print(len(oa_list))
    # 遍历列表，通过对象依次获取内容和链接
    for oa in oa_list:
        # 得到链接
        href = 'http://www.shicimingju.com' + oa['href']
        # 得到章节标题
        title = oa.text
        print('正在下载%s......' % title)
        # 向href发送请求，通过bs得到该章节的内容
        text = get_text(href)
        string = title + '\n' + text + '\n'
        fp.write(string)
        print('结束下载%s' % title)
        time.sleep(2)
    fp.close()


def get_text(href):
    request = handle_request(href)
    content = urllib.request.urlopen(request).read().decode('utf8')
    soup = BeautifulSoup(content, 'lxml')
    odiv = soup.find('div', class_='chapter_content')
    return odiv.text


def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def main():
    parse_first()


if __name__ == '__main__':
    main()