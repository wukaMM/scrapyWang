# -*- coding: utf-8 -*-

# Scrapy settings for scrapyWang project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapyWang'

SPIDER_MODULES = ['scrapyWang.spiders']
NEWSPIDER_MODULE = 'scrapyWang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyWang (+http://www.yourdomain.com)'


ITEM_PIPELINES = {
    'scrapyWang.pipelines.ScrapywangPipeline':300
}
