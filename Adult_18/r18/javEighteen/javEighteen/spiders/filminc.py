# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from javEighteen.items import JavEighteenItem


class FilmincSpider(CrawlSpider):
    name = 'filminc'
    allowed_domains = ['r18.com']
    start_urls = ['http://www.r18.com/videos/vod/movies/studio/letter=a/sort=popular/page=1/']

    rules = (
        Rule(LinkExtractor(allow=r'studio/letter=a/sort=popular/page=\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = JavEighteenItem()
        for inc in response.xpath('//div[@class="cmn-list-info01 clearfix"]//li/div[@class="box02"]'):
            item['inc_name'] = inc.xpath('./p[@class="txt01"]//a/text()').extract()[0]
            item['inc_logo'] = inc.xpath('./p[@class="img01"]//img/@src').extract()[0]
            item['inc_id'] = re.findall('id=\d+',inc.xpath('./p[@class="txt01"]//a/@href').extract()[0])[0][3:]
            # item[''] = response.xpath('').extract()
            yield item
