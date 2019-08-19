# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
# from scrapy.selector import Selector
from douban.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    # allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    url = 'https://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanItem()
        # selector = Selector(response)
        Movies = response.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@property="v:average"]/text()').extract()
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
            nextLink = response.xpath('//span[@class="next"]/link/@href').extract()
            # 第10页是最后一页，没有下一页链接
            if nextLink:
                nextLink = nextLink[0]
                print(nextLink)
                yield Request(self.url + nextLink, callback=self.parse)
        # print(response.url)






























