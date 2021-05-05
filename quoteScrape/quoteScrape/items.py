# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#Temporary container for storing the items returned by spider then model them too.
import scrapy


class QuotescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    quote = scrapy.Field()
    tags = scrapy.Field()
    # name = scrapy.Field()
    #pass
