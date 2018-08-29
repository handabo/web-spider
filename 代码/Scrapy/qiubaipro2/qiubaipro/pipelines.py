# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class QiubaiproPipeline(object):
    # 将文件的打开写到只调用一次的函数中
    # def __init__(self):
    #     self.fp = open('qiubai.txt', 'w', encoding='utf8')
    def open_spider(self, spider):
        self.fp = open('qiubai.txt', 'w', encoding='utf8')
    
    # 关闭爬虫的时候，调用一次，关闭文件
    def close_spider(self, spider):
        self.fp.close()

    # 处理item的函数，item：就是要处理的数据
    # 该函数会被一直反复的调用，只要有item就调用它
    def process_item(self, item, spider):
        # 将item写到文件中
        # 将item转化为字典
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item
