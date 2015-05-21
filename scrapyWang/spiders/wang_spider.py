#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

from scrapy.spider import Spider
from scrapy.http import Request

from scrapyWang.items import ScrapywangItem
from soup import BeautifulSoup as bs 


class ScrapywangSpider(Spider):
    name = "wang"
    allowed_domain = []
    start_urls = ['https://pywinauto.googlecode.com/hg/pywinauto/docs/controls_overview.html']


    def parse(self, response):
        text_html = response.body
        soup = bs(text_html)
        xs = soup.findAll('a', {"class" : "reference external"})
        items = [x.get('href') for x in xs]
        items = filter(lambda x : x, items)

        for item in items:
            item = str(item)
            url = "https://pywinauto.googlecode.com/hg/pywinauto/docs/" + item
            try:
                r = Request(url, callback=self.parse, dont_filter=True)
                new_item = item.replace("#", ".")
                r.title = os.path.basename(new_item)
                r.foldname = os.path.dirname(new_item)
                text_html = text_html.replace(item, new_item)
                yield r
            except Exception, e:
                print "Exception : ",str(e)

        sw = ScrapywangItem()
        sw['desc'] = text_html
        try:
            sw['title'] = response.request.title
            sw['foldname'] = response.request.foldname
        except:
            sw['title'] = "index.html"
            sw['foldname'] = ""
        
        yield sw

        