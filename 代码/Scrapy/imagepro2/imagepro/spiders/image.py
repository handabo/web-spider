# -*- coding: utf-8 -*-
import scrapy
from imagepro.items import ImageproItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/people.html']

    url = 'http://699pic.com/photo-0-6-{}-0-0-0.html'
    page = 1

    def parse(self, response):
        # 得到所有图片的链接
        href_list = response.xpath('//div[@class="list"]/a/@href').extract()
        for href in href_list:
            yield scrapy.Request(url=href, callback=self.parse_detail)
        
        '''
        调度器中：第一页的100个详情页链接，还有3个页码链接
        又是100详情页链接，又是一个页码链接
        '''
        if self.page < 2:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse_detail(self, response):
        # 创建一个对象
        item = ImageproItem()
        # 图片的名字
        item['name'] = response.xpath('//div[@class="photo-view"]/h1/text()').extract_first()
        # 发布时间
        item['publish_time'] = response.xpath('//div[@class="photo-view"]//span[@class="publicityt"]/text()').extract_first().rstrip(' 发布')
        # 浏览量
        item['views'] = response.xpath('//div[@class="photo-view"]//span[@class="look"]/read/text()').extract_first()
        # 收藏量
        item['collect'] = response.xpath('//div[@class="photo-view"]//span[@class="collect"]/text()').extract_first().rstrip(' 收藏')
        # 下载量
        item['download'] = response.xpath('//div[@class="photo-view"]//span[@class="download"]/text()').extract()[1].rstrip(' 下载\n\t')
        # 点赞个数
        item['zan'] = response.xpath('//span[@class="star-count"]/text()').extract_first()
        # 图片的链接
        item['src'] = response.xpath('//img[@id="photo"]/@src').extract_first()

        yield item

        # 下载防盗链图片
    #     yield scrapy.Request(url=item['src'], callback=self.download)
    
    # def download(self, response):
    #     with open('lala.jpg', 'wb') as fp:
    #         fp.write(response.body)

