# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 第一个页面要的内容为
    # 电影海报
    post = scrapy.Field()
    # 电影名字
    name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 类型
    _type = scrapy.Field()

    # 第二个页面要的内容为
    # 导演
    director = scrapy.Field()
    # 编剧
    editor = scrapy.Field()
    # 主演
    actor = scrapy.Field()
    # 地区
    area = scrapy.Field()
    # 语言
    lang = scrapy.Field()
    # 上映时间
    publish_time = scrapy.Field()
    # 片长
    pianchang = scrapy.Field()
    # 电影简介
    info = scrapy.Field()
