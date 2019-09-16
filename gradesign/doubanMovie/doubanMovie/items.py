# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 电影名字
    release_time = scrapy.Field()  # 上映时间
    director = scrapy.Field()  # 导演名字
    length = scrapy.Field()  # 片长
    imdb_link = scrapy.Field()  # imdb下载链接
    mark = scrapy.Field()  # 评分
    cover_link = scrapy.Field()  # 封面图片
    summary = scrapy.Field()  # 概述


