# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 中国队大胜美国队  中国队大败美国队
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 头像
    face = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 好笑的个数
    haha_count = scrapy.Field()
