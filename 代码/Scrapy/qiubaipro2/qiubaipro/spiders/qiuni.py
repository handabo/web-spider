# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiubaipro.items import QiubaiproItem

class QiuniSpider(CrawlSpider):
    name = 'qiuni'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    page_link = LinkExtractor(allow=r'/8hr/page/\d+/')
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )
    # 1  1 1 1 1  2 2 2  2 2   131 313    50个url
    # 第一页内容提取： 2 3 4 5 13
    # 2               1 3 4 5 13
    # 3               1 2 4 5 13
    # 4               1 2 3 5 13

    def parse_item(self, response):
        odiv_list = response.xpath('//div[@id="content-left"]/div')

        for odiv in odiv_list:
            # 创建对象
            item = QiubaiproItem()
            # 获取头像
            face = odiv.xpath('./div[@class="author clearfix"]//img/@src')[0].extract()
            # 获取用户名
            name = odiv.xpath('./div[@class="author clearfix"]//h2/text()')[0].extract().strip('\n')
            # 获取年龄
            try:
                age = odiv.xpath('./div[@class="author clearfix"]/div/text()')[0].extract()
            except Exception as e:
                age = '没有年龄'
            # 获取内容
            content_lt = odiv.xpath('.//div[@class="content"]/span[1]/text()').extract()
            content = ''.join(content_lt).strip('\n ')
            # 好笑个数
            haha_count = odiv.xpath('.//span[@class="stats-vote"]/i/text()')[0].extract()
            
            # 将抓取得到的内容依次保存到item里面
            # item['face'] = face
            # item['name'] = name
            # item['age'] = age
            # item['content'] = content
            # item['haha_count'] = haha_count
            lt = ['face', 'name', 'age', 'content', 'haha_count']
            for field in lt:
                item[field] = eval(field)
            
            yield item
