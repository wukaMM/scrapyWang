# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import chardet
import os


class ScrapywangPipeline(object):

    def process_item(self, item, spider):
        filename = item['title']
        line = item['desc'] + '\n'
        content_type = chardet.detect(line)

        if content_type['encoding'] != "UTF-8":
            line = line.decode(content_type['encoding'])
        line = line.encode("utf-8")
        if filename != "index.html":
            os.mkdir("code")
            filename = "code/"+filename
            
        open(filename,"wb").write(line)

        return item