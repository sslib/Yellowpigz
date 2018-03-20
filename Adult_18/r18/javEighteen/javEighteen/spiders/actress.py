# -*- coding: utf-8 -*-
import scrapy
import re
from javEighteen.items import JavEighteenItem

class ActressSpider(scrapy.Spider):
    name = 'actress'
    allowed_domains = ['r18.com']
    offset = 1
    url = 'http://www.r18.com/videos/vod/movies/actress/letter=a/sort=popular/page='
    start_urls = [url + str(offset) + '/']

    def parse(self, response):
        item = JavEighteenItem()
        acts = response.xpath('//ul[@class="cmn-list-product03 nml07 clearfix"]/li/a')
        for act in acts:
            item['act_name'] = act.xpath('./div[@class="txt01"]/div[1]/text()').extract()[0]
            item['act_img'] = act.xpath('./p/img/@src').extract()[0]
            item['act_home_id'] = re.findall('id=\d+',act.xpath('./@href').extract()[0])[0][3:]
            yield item
        if self.offset < 318:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset) + '/',callback=self.parse)