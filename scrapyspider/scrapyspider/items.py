# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


# Importing the library
import scrapy

# Class Inheritance from scrapy.item class
class EmojiSpiderItem(scrapy.Item): 
    # Defining each field as separate line
    emoji_handle = scrapy.Field() 
    emoji_image = scrapy.Field()
    section = scrapy.Field()
