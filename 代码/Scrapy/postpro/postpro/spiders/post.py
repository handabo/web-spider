# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['cn.bing.com']
    # start_urls = ['https://cn.bing.com/translator/']

    # 官方是通过如下方式实现的
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 自己如果上来就想发送post，可以重写这个方法
    def start_requests(self):
        post_url = 'https://cn.bing.com/ttranslationlookup?&IG=51EEE86465BF400A822B74F3875D2636&IID=translator.5036.6'
        formdata = {
            'from': 'zh-CHS',
            'to': 'en',
            'text': '大地',
        }
        yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.lala)
    '''
    def parse(self, response):
        # 在这里接着发送post请求
        # 久旱逢甘霖，他乡遇故知，洞房花烛夜，金榜题名时
        post_url = 'https://cn.bing.com/ttranslationlookup?&IG=51EEE86465BF400A822B74F3875D2636&IID=translator.5036.6'
        formdata = {
            'from': 'zh-CHS',
            'to': 'en',
            'text': '大地',
        }
        yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.lala)
    '''
    
    def lala(self, response):
        print('*' * 100)
        print(response.text)
        print('*' * 100)

