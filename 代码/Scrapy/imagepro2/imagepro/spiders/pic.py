# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from imagepro.items import ImageproItem
from scrapy_redis.spiders import RedisCrawlSpider

class PicSpider(RedisCrawlSpider):
    name = 'pic_redis'
    allowed_domains = ['699pic.com']
    redis_key = 'picspider:start_urls'
    # start_urls = ['http://699pic.com/people.html']

    # 自己配置自己的settings
    custom_settings = {
        'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        'SCHEDULER_PERSIST': True,
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 400,
        },
        'REDIS_HOST': '10.7.185.86',
        'REDIS_PORT': 6379,
        'DOWNLOAD_DELAY': 1,
    }

    # 详情页规则
    detail_link = LinkExtractor(restrict_css='.list')
    page_link = LinkExtractor(allow=r'/photo-0-6-\d+-0-0-0\.html')
    rules = (
        Rule(detail_link, callback='parse_item', follow=False),
        Rule(page_link, follow=False),
    )

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
