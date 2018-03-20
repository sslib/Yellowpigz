# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavEighteenItem(scrapy.Item):
    #actress
    act_name = scrapy.Field()
    act_img = scrapy.Field()
    act_home_id = scrapy.Field()
    #fileinc
    inc_name = scrapy.Field()
    inc_logo = scrapy.Field()
    inc_id = scrapy.Field()
    # pass
