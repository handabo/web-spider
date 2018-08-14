from threading import Thread, Lock
from queue import Queue
import requests
from bs4 import BeautifulSoup
import json


class CrawlThread(Thread):
    def __init__(self, name, page_queue, data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/duanzi-{}'
        self.headers = {
        	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def run(self):
        print('线程--%s--启动成功----' % self.name)
        '''
        1、从页码队列取出一个页码
        2、拼接生成待发送的url
        3、发送请求，得到响应
        4、将响应添加到数据队列中
        '''
        while True:
            page = self.page_queue.get()
            url = self.url.format(page)
            content = requests.get(url=url, headers=self.headers).text
            self.data_queue.put(content)
        print('线程--%s--运行结束--' % self.name)


class ParseThread(Thread):
    def __init__(self, name, data_queue, fp, lock):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        print('线程--%s--启动成功----' % self.name)
        '''
        1、从数据队列中取出一个数据
        2、解析和处理数据
        '''
        while 1:
            content = self.data_queue.get()
            self.parse_content(content)
        print('线程-%s-运行结束--' % self.name)
    
    def parse_content(self, content):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')
        # 开始解析
        item = {}
        string = json.dumps(item, ensure_ascii=False)
        self.lock.acquire()
        self.fp.write(string + '\n')
        self.lock.release()


def create_queue():
    page_queue = Queue()
    data_queue = Queue()
    for page in range(1, 6):
        page_queue.put(page)
    return page_queue, data_queue


def main():
    # 搞一个列表，用来存放所有的线程对象
    t_list = []
    # 打开文件
    fp = open('jian.txt', 'w', encoding='utf8')
    # 创建锁
    lock = Lock()
    # 创建队列
    page_queue, data_queue = create_queue()
    # 创建采集线程
    crawl_name_list = ['采集线程1', '采集线程2', '采集线程3']
    for crawl_name in crawl_name_list:
        t_crawl = CrawlThread(crawl_name, page_queue, data_queue)
        # 启动线程
        t_crawl.start()
        # 将线程保存到列表中
        t_list.append(t_crawl)

    # 创建解析线程
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_name_list:
        t_parse = ParseThread(parse_name, data_queue, fp, lock)
        t_parse.start()
        t_list.append(t_parse)
    
    # 主线程要等待所有的子线程结束我才能结束
    for t_tmp in t_list:
        t_tmp.join()
    
    # 关闭文件
    fp.close()
    print('主线程、子线程全部结束')


if __name__ == '__main__':
    main()

