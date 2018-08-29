# -*- coding: utf-8 -*-
import scrapy
# 导入链接提取器
from scrapy.linkextractors import LinkExtractor
# CrawlSpider
# Rule ： 规则，指定要处理的函数，处理提取的链接的响应内容
from scrapy.spiders import CrawlSpider, Rule


class QiuqiuSpider(CrawlSpider):
    name = 'qiuqiu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # 定制规则
    le = LinkExtractor(allow=r'Items/')
    '''
    参数1：链接提取器
    参数2：用来处理响应的回调函数, 需要些函数名字符串
        普通spider：callback = self.parse_xxx
        crawlspider： callback = 'parse_xxx'
        【注】parse函数就是用来提取链接的，有专门的作用，不能重写，如果重写parse函数，那么CrawlSpider就不能用了
    参数3：follow  跟进，在提取的链接发送请求得到响应之后，在这些响应中要不要按照规则接着提取，要就是True，不要就是False
        follow也有默认值，如果前面有callback，follow不写默认为False，如果前面没有callback，follow不写，默认为True
    '''
    rules = (
        Rule(le, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
