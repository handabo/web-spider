# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import urllib.request
import os
import pymysql
from scrapy.utils.project import get_project_settings
import pymongo

class MongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        db = self.client.image
        self.collection = db.people
    
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        obj = dict(item)
        self.collection.insert(obj)
        return item

class MysqlPipeline(object):
    def open_spider(self, spider):
        settings = get_project_settings()
        # 依次获取数据库的配置信息
        host = settings['HOST']
        port = settings['PORT']
        user = settings['USER']
        pwd = settings['PWD']
        charset = settings['CHARSET']
        name = settings['NAME']

        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=name, charset=charset)
    
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # 插入数据
        sql = 'insert into people(name, publish_time, views, collect, download, zan, src) values("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item['name'], item['publish_time'], item['views'], item['collect'], item['download'], item['zan'], item['src'])
        self.cursor = self.conn.cursor()
        
        try:
            self.cursor.execute(sql)
            #提交
            self.conn.commit()
        except Exception as e:
            #错误回滚
            self.conn.rollback()
        return item

class ImageproPipeline(object):
    def open_spider(self, spider):
        self.fp = open('image.txt', 'w', encoding='utf8')
    
    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        string = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(string + '\n')

        # self.download(item)
        return item
    
    def download(self, item):
        dirname = r'C:\Users\ZBLi\Desktop\1803\day09\imagepro\imagepro\spiders\pics'
        filename = item['name'] + '.' + item['src'].split('.')[-1]
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['src'], filepath)
