import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time


class ZhiLianSpider(object):
    def __init__(self, jl, kw, start_page, end_page):
        # 将这些都保存到成员属性中
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def run(self):
        # 打开文件
        self.fp = open('work.txt', 'w', encoding='utf8')
        # 要爬取多页，所以需要循环爬取
        for page in range(self.start_page, self.end_page + 1):
            print('正在爬取第%s页......' % page)
            request = self.handle_request(page)
            # 发送请求，获取响应
            content = urllib.request.urlopen(request).read().decode('utf8')
            # 解析内容
            self.parse_content(content)
            print('结束爬取第%s页' % page)
            time.sleep(2)
        self.fp.close()

    def parse_content(self, content):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')
        # 提取内容
        # 首先提取所有的table
        otable_list = soup.find_all('table', class_='newlist')
        # print(len(otable_list))
        # 过滤掉表头
        otable_list = otable_list[1:]
        # 遍历这个列表，依次提取每一个工作的详细信息
        for otable in otable_list:
            # 职位名称
            zwmc = otable.select('.zwmc > div > a')[0].text.rstrip('\xa0')
            # 公司名称
            gsmc = otable.select('.gsmc > a')[0].string
            # 职位月薪
            zwyx = otable.select('.zwyx')[0].string
            # 工作地点
            gzdd = otable.select('.gzdd')[0].string
            # print(zwmc)
            # exit()
            # 保存到字典中
            item = {
                '职位名称': zwmc,
                '公司名称': gsmc,
                '职位月薪': zwyx,
                '工作地点': gzdd,
            }
            self.fp.write(str(item) + '\n')

    def handle_request(self, page):
        # 拼接url
        # 将get参数写成一个字典
        data = {
            'jl': self.jl,
            'kw': self.kw,
            'p': page
        }
        # 处理data
        data = urllib.parse.urlencode(data)
        url = self.url + data
        # print(url)
        request = urllib.request.Request(url=url, headers=self.headers)
        return request


def main():
    # 工作地点
    jl = input('请输入工作地点:')
    # 工作关键字
    kw = input('请输入工作职位关键字:')
    # 起始页码和结束页码
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))

    # 面向对象封装
    zhilian = ZhiLianSpider(jl, kw, start_page, end_page)
    zhilian.run()


if __name__ == '__main__':
    main()