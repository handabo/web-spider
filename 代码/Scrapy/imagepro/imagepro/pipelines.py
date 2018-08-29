# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import urllib.request
import os

class ImageproPipeline(object):
    def open_spider(self, spider):
        self.fp = open('image.txt', 'w', encoding='utf8')
    
    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        string = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(string + '\n')

        self.download(item)
        return item
    
    def download(self, item):
        dirname = r'C:\Users\ZBLi\Desktop\1803\day09\imagepro\imagepro\spiders\pics'
        filename = item['name'] + '.' + item['src'].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['src'], filepath)
