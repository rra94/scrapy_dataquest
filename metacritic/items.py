# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MetacriticItem(scrapy.Item):
    artist = scrapy.Field()
    album = scrapy.Field()
    metascore = scrapy.Field()
    userscore = scrapy.Field()
    releasedate = scrapy.Field()
    genre = scrapy.Field()
