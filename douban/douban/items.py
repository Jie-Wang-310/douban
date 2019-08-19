# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    movieInfo = scrapy.Field()
    star = scrapy.Field()
    quote = scrapy.Field()

# 第二种方法
# from scrapy import Item, Field
# class DoubanItem(Item)
#     title = Field()
#     movieInfo = Field()
#     star = Field()
#     quote = Field()


