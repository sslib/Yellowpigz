# -*- coding: utf-8 -*-
import scrapy
import re
from javEighteen.items import JavEighteenItem


class FilmincSSpider(scrapy.Spider):
    name = 'filminc_s'
    allowed_domains = ['r18.com']
    url = 'http://www.r18.com/videos/vod/movies/studio/letter=a/sort=popular/page='
    offset = 1
    start_urls = [url + str(offset) + '/']

    def parse(self, response):
        item = JavEighteenItem()
        incs = response.xpath('//div[@class="cmn-list-info01 clearfix"]//li/div[@class="box02"]')
        for inc in incs:
            item['inc_name'] = inc.xpath('./p[@class="txt01"]//a/text()').extract()[0]
            item['inc_logo'] = inc.xpath('./p[@class="img01"]//img/@src').extract()[0]
            item['inc_id'] = re.findall('id=\d+', inc.xpath('./p[@class="txt01"]//a/@href').extract()[0])[0][3:]
            # item[''] = response.xpath('').extract()
            if self.offset < 206:
                self.offset += 1
            yield scrapy.Request(self.url + str(self.offset) + '/', callback=self.parse)
            yield item
