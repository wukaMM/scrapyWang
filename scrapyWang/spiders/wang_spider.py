#!/usr/bin/python
# -*- coding:utf-8 -*-
import uuid

from scrapy.spider import Spider
from scrapy.http import Request

from scrapyWang.items import ScrapywangItem
from soup import BeautifulSoup as bs 


class ScrapywangSpider(Spider):
    name = "wang"
    allowed_domain = []
    start_urls = ['https://pywinauto.googlecode.com/hg/pywinauto/docs/controls_overview.html']


    def parse(self, response):
        sw = ScrapywangItem()
        sw['desc'] = response.body
        sw['title'] = uuid.uuid4().hex
        
        yield sw
        
        soup = bs(response.body)
        xs = soup.findAll('a', {'class': 'reference external'})
        items = [(x.text, x.get('href')) for x in xs]
        items = filter(lambda x : x[1], items)

        for item in items:
            url = "https://pywinauto.googlecode.com/hg/pywinauto/docs/" + item[1]
            try:
                yield Request(url, callback=self.parse, dont_filter=True, cookies=item[0])
            except Exception, e:
                print "Exception : ",str(e)

        