# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?ie=UTF-8&wd=ip']

    def parse(self, response):
        with open('ip.html', 'wb') as fp:
            fp.write(response.body)
