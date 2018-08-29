from threading import Thread, Lock
from queue import Queue
import requests
from bs4 import BeautifulSoup
import json, time

'''
采集线程退出条件：当页码队列为空时退出
解析线程退出条件：首先判断页码队列是否为空，如果页码队列为空，然后再去判断数据队列是否为空，如果数据队列也为空，那么解析线程退出
'''
# 标记解析线程何时退出标记位
g_flag = True

class CrawlThread(Thread):
    def __init__(self, name, page_queue, data_queue):
        super().__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/duanzi-{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        }

    def run(self):
        print('线程--%s--启动成功----' % self.name)
        '''
        1、从页码队列取出一个页码
        2、拼接生成待发送的url
        3、发送请求，得到响应
        4、将响应添加到数据队列中
        '''
        while 1:
            # 如果页码队列为空，那么该线程就应该退出
            if self.page_queue.empty():
                break
            page = self.page_queue.get()
            url = self.url.format(page)
            content = requests.get(url=url, headers=self.headers).text
            self.data_queue.put(content)
        print('线程-%s-运行结束--' % self.name)

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
            if g_flag == False:
                break
            try:
                content = self.data_queue.get(True, 3)
            except Exception as e:
                break
            self.parse_content(content)
            
        print('线程-%s-运行结束--' % self.name)
    
    def parse_content(self, content):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')
        resps = soup.select('.cont-item')
        for resp in resps:
            title = resp.select('a')[0]['title']
            text = resp.select('.cont-list-main p')[0].string
            item = {
                '用户名': title,
                '内容': text
            }
            # 开始解析
            string = json.dumps(item, ensure_ascii=False)
            self.lock.acquire()
            self.fp.write(string + '\n')
            self.lock.release()

def create_queue():
    page_queue = Queue()
    data_queue = Queue()
    for page in range(1, 8):
        page_queue.put(page)
    return page_queue, data_queue

def main():
    # 搞一个列表，用来存放所有的线程对象
    t_crawl_list = []
    t_parse_list = []
    # 打开文件
    fp = open('jian.txt', 'w', encoding='utf8')
    # 创建锁
    lock = Lock()
    # 在这创建队列
    page_queue, data_queue = create_queue()
    # 创建采集线程
    crawl_name_list = ['采集线程1', '采集线程2', '采集线程3']
    for crawl_name in crawl_name_list:
        t_crawl = CrawlThread(crawl_name, page_queue, data_queue)
        t_crawl.start()
        # 将线程保存到列表中
        t_crawl_list.append(t_crawl)
    # 创建解析线程
    parse_name_list = ['解析线程1', '解析线程2', '解析线程3']
    for parse_name in parse_name_list:
        t_parse = ParseThread(parse_name, data_queue, fp, lock)
        t_parse.start()
        t_parse_list.append(t_parse)
    
    for t_crawl in t_crawl_list:
        t_crawl.join()
    
    # 一直判断页码队列是否为空
    # while 1:
    #     if page_queue.empty():
    #         break
    time.sleep(3)
    while 1:
        if data_queue.empty():
            global g_flag
            g_flag = False
            break
    
    # 主线程要等待所有的子线程结束我才能结束
    for t_parse in t_parse_list:
        t_parse.join()
    
    # 关闭文件
    fp.close()
    print('主线程、子线程全部结束')

if __name__ == '__main__':
    main()

'''
1、文件解析，每一个段子解析为字典
2、采集线程和解析线程都是死循环，何时退出线程呢？
'''