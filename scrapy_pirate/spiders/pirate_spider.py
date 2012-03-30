#!/usr/bin/env python
#-*- coding:utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy_pirate.items import PirateTorrentItem

class PirateSpider(BaseSpider):
    name = 'pirate_spider'
    allowed_domains = 'thepiratebay.org'
    categories = {'201' : 'movies', '205' : 'tv_shows'}
    start_urls = ['http://thepiratebay.org/browse/%d/%d/3' % (c,i)
        for i in range(10)
        for c in (201, 205)]

    def parse(self, response):

        items = []
        category = self.categories[response.url.split('/')[-3]]
        hxs = HtmlXPathSelector(response)

        trs = hxs.select('//table[@id="searchResult"]/tr')[:-1] # last tr makes pagination

        for tr in trs:
            
            item = PirateTorrentItem()

            item['title'] = tr.select('./td[2]/div/a/text()').extract()[0]
            item['link'] = tr.select('./td[2]/div/a/@href').extract()[0]
            item['download_link'] = tr.select('./td[2]/a/@href').extract()[0]
            item['description'] = tr.select('./td[2]/font/text()').extract()[0][:-10]

            try:
                item['seeders'] = int(tr.select('./td[3]/text()').extract()[0])   # in XPath index starts at 0
            except ValueError:
                item['seeders'] = 0

            try:                
                item['leechers'] = int(tr.select('./td[4]/text()').extract()[0])
            except:
                item['leechers'] = 0

            items.append(item)  

        return items


# scrapy shell http://thepiratebay.org/browse/205/0/3

# class PirateTorrentItem(Item):
#     title = Field()
#     link = Field()
#     download_link = Field()
#     size = Field()
#     seeders = Field()
#     leechers = Field()
