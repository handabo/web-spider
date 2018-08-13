import urllib.request
from lxml import etree
import time
import os


class TuPianSpider(object):
    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.url = 'http://sc.chinaz.com/tupian/meinvtupian_{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            print('正在下载第%s页......' % page)
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode('utf8')
            self.parse_content(content)
            print('结束下载第%s页' % page)
            time.sleep(2)
    
    def parse_content(self, content):
        # 解析内容
        tree = etree.HTML(content)
        # 提取这个页码所有图片的src属性
        image_srcs = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
        # 找到图片的标题
        image_titles = tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
        # print(image_srcs)
        # print(len(image_srcs))
        # 遍历列表下载图片
        for image_src in image_srcs:
            # 生成图片的名字
            filename = image_titles[image_srcs.index(image_src)] + '.' + image_src.split('.')[-1]
            print('正在下载--%s...' % filename)
            dirname = 'meinv'
            filepath = os.path.join(dirname, filename)
            urllib.request.urlretrieve(image_src, filepath)
            print('结束下载--%s' % filename)
            time.sleep(2)
    
    def handle_request(self, page):
        if page == 1:
            url = 'http://sc.chinaz.com/tupian/meinvtupian.html'
        else:
            url = self.url.format(page)
        # print(url)
        request = urllib.request.Request(url=url, headers=self.headers)
        return request


def main():
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    tupian = TuPianSpider(start_page, end_page)
    tupian.run()


if __name__ == '__main__':
    main()