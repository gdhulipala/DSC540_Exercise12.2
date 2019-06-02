#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:10:13 2019

@author: ganga
"""
# Importing the libraries to use the root project folder
import scrapy
from scrapyspider.items import EmojiSpiderItem 

# Defining class with inheritance
class EmoSpider(scrapy.Spider): 
    # Defining the name of the spider
    name = 'emo' 
    # Specifying domains to scrap
    allowed_domains = ['emoji-cheat-sheet.com'] 
    # Defining urls to iterate
    start_urls = [
        'http://www.emoji-cheat-sheet.com/', 
    ]
    # Method to parse the response
    def parse(self, response): 
        # Extracting the headers
        headers = response.xpath('//h2|//h3')
        lists = response.xpath('//ul')
        all_items = [] 
        # Iterating through headers
        for header, list_cont in zip(headers, lists):
            section = header.xpath('text()').extract()[0] 
            for li in list_cont.xpath('li'):
                item = EmojiSpiderItem() 
                item['section'] = section
                spans = li.xpath('div/span')
                if len(spans):
                    link = spans[0].xpath('@data-src').extract() 
                    # Iterating through emoji image item
                    if link:
                        item['emoji_image'] = response.url + link[0] 
                    # Finding the handle strings for emoji and sounds
                    handle_code = spans[1].xpath('text()').extract()
                else:
                    handle_code = li.xpath('div/text()').extract()
                if handle_code:
                    item['emoji_handle'] = handle_code[0] 
                # Adding items to the list
                all_items.append(item) 
        # This line returns the array of items        
        return all_items 