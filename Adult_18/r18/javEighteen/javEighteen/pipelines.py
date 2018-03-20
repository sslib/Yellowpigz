# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class javEighteenPipeline(object):
    def __init__(self):
        self.filename = open("actress.json","w")
    def process_item(self, item, spider):
        act = json.dumps(dict(item),ensure_ascii =False) + "\n"
        self.filename.write(act)
        return item
    def close_spider(self,spider):
        self.filename.close()