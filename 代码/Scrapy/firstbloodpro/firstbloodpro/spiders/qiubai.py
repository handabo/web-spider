# -*- coding: utf-8 -*-
# 导入需要的包
import scrapy

# Spider: scrapy里面最基础的爬虫类
class QiubaiSpider(scrapy.Spider):
    # 爬虫的名字，启动爬虫的时候需要用到
    name = 'qiubai'
    # 允许的域名，是一个列表, 妹子图，图片的地址和网页url的地址域名不是同一个
    allowed_domains = ['www.qiushibaike.com', 'www.baidu.com']
    # 起始的url列表，一般只写一个
    start_urls = ['http://www.qiushibaike.com/']

    # 该函数用来处理起始url的响应内容，该函数是一个重写的函数，
    # 该函数如果有返回值，需要返回一个可迭代对象
    # response就是响应的对象
    def parse(self, response):
        items = []
        # print('*' * 100)
        # print(response)
        
        # 先得到所有的div
        odiv_list = response.xpath('//div[@id="content-left"]/div')
        # print(len(odiv_list))
        for odiv in odiv_list:
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
            # print(haha_count)
            item = {
                '头像': face,
                '名称': name,
                '年龄': age,
                '内容': content,
                '个数': haha_count,
            }
            items.append(item)
        return items
        # print('*' * 100)