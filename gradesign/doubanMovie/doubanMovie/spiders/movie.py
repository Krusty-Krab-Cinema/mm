# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import time

class MovieSpider(scrapy.Spider):
    name = 'movie'  # 爬虫名
    # allowed_domains = ['movie.douban.com']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }


    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        # yield scrapy.Request(url=url, headers=self.headers, meta={'proxy':'http:118.117.136.19:9000'})
        yield scrapy.Request(url=url, headers=self.headers)

    page = 1  # 翻页记录

    # 解析页面
    def parse(self, response):
        # item = DoubanmovieItem()
        movie_ol = response.xpath('//ol[@class="grid_view"]/li/div/div[2]')

        for div in movie_ol:
            # 电影名称和评分
            item = {}
            name = div.xpath('.//a/span[1]/text()').extract_first()
            mark = div.xpath('.//span[@class="rating_num"]/text()').extract_first()
            temp = response.xpath('//div[starts-with(@class,"bd")]/p/text()[2]').extract_first()
            # country =


            item = {
                'name':name,
                'mark':mark,
            }

            # 电影详情信息页面url
            detail_url = div.xpath('.//a/@href').extract_first()

            # 获取详细信息
            yield scrapy.Request(url=detail_url, callback=self.parse_info, meta={'item':item}, dont_filter=True)

        # 翻页
        if self.page <= 10:
            data = {
                'start':(self.page - 1) * 25,
            }
            data = parse.urlencode(data)

            # 下一页url
            next_url = 'https://movie.douban.com/top250?' + data
            self.page += 1

            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

    # 解析每一条电影链接对应的详情页信息
    def parse_info(self, response):
        item = response.meta['item']
        director = response.xpath('//div[@class="article"]//div[@id="info"]/span[1]/span[2]/a/text()').extract_first()
        release_time = response.xpath('//div[@class="article"]//div[@id="info"]/span[10]/text()').extract_first()
        length = response.xpath('//div[@class="article"]//div[@id="info"]/span[13]/text()').extract_first()
        imdb_link = response.xpath('//div[@class="article"]//div[@id="info"]/a[1]/@href').extract_first()
        cover_link = response.xpath('//div[@class="article"]//div[@id="mainpic"]//img/@src').extract_first()
        summary = response.xpath('//div[@class="article"]//div[@id="link-report"]/span[1]/text()').extract_first()



        item['director'] = director
        item['release_time'] = release_time
        item['length'] = length
        item['imdb_link'] = imdb_link
        item['cover_link'] = cover_link
        item['summary'] = summary

        time.sleep(2)
        yield item



