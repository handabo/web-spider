# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random

class RandomUADownloaderMiddleware(object):
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        ]
    
    def process_request(self, request, spider):
        # 随机抽取一个ua
        ua = random.choice(self.user_agents)
        # print('*' * 100)
        # print('当前使用的ua为--%s' % ua)
        # print('*' * 100)
        # 添加到请求的头部
        request.headers.setdefault('User-Agent', ua)


class ProxyDownloaderMiddleware(object):
    def __init__(self):
        # 自己维护的代理ip池
        self.ippools = [
            '218.60.8.83:3129',
            '106.14.184.6:3128',
            '114.215.95.188:3128',
            '122.72.18.34:80',
        ]
    
    def process_request(self, request, spider):
        # 随机抽取一个代理
        self.ip = random.choice(self.ippools)
        print('*' * 100)
        print(self.ip)
        print('*' * 100)
        # 给这个请求添加代理
        request.meta['proxy'] = 'http://' + self.ip
        # 等待链接的时间
        request.meta['download_timeout'] = 5
    
    def process_exception(self, request, exception, spider):
        print('#' * 100)
        print(exception)
        print('#' * 100)
        # 抛出异常，将选择的不可用的代理从列表中移除
        self.ippools.remove(self.ip)
        # 返回request，让这个请求重新发送
        return request



class RandomproSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
