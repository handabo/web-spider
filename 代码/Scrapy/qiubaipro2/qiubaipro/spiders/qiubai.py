# -*- coding: utf-8 -*-
# 导入需要的包
import scrapy
# 导入进来这个类，然后使用
from qiubaipro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com', 'www.baidu.com']
    start_urls = ['http://www.qiushibaike.com/']

    # 要拼接的url
    url = 'https://www.qiushibaike.com/8hr/page/{}/'
    page = 1

    def parse(self, response):
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
        
        # 你想要爬取多少页
        if self.page < 5:
            self.page += 1
            # 拼接url
            url = self.url.format(self.page)
            # callback: 就是响应过来之后通过哪一个回调处理响应
            yield scrapy.Request(url, callback=self.parse)