# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from imagepro.items import ImageproItem

class TupianSpider(CrawlSpider):
    name = 'tupian'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/people.html']

    # 详情页规则
    detail_link = LinkExtractor(restrict_css='.list')
    page_link = LinkExtractor(allow=r'/photo-0-6-\d+-0-0-0\.html')
    rules = (
        Rule(detail_link, callback='parse_item', follow=False),
        Rule(page_link, follow=False),
    )
    '''
    True : 写成这个，代表爬取所有页
    '''

    '''
    第一页发送请求之后：响应来了
        提取100个详情页url
        提取出来  2 3 4 5 6 7 8 400
    详情页的响应来了：
        首先通过callback处理。
        不跟进
    页码的响应来了：
        没有callback，所以不处理
        不提取
    '''

    def parse_item(self, response):
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
