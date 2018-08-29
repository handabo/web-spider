# -*- coding: utf-8 -*-
import scrapy
from moviepro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie']

    # 查找得到页码的规律
    url = ''
    page = 1

    def parse(self, response):
        # 要得到每一个电影的详细信息，还要得到电影的详情页链接，还得向这个链接发送请求
        odiv_list = response.xpath('//div[@class="col-xs-1-5 col-sm-4 col-xs-6 movie-item"]')
        for odiv in odiv_list:
            # 新建一个对象
            item = MovieproItem()
            # 获取电影的详细信息
            item['post'] = odiv.xpath('xxx')
            item['name'] = odiv.xpath('xxx')
            item['_type'] = odiv.xpath('xxx')
            item['score'] = odiv.xpath('xxx')

            # 得到详情页的链接
            detail_url = odiv.xpath('xxx')
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})
    
    def parse_detail(self, response):
        # 首先获取到传递过来的参数
        item = response.meta['item']
        # 获取item的其他信息
        item['director'] = response.xpath('xxx')
        item['editor'] = response.xpath('xxx')
        item['actor'] = response.xpath('xxx')
        # ......
        yield item
