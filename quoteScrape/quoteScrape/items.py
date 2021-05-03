# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#Tempory container for storing the items returned by spider then model it too.
import scrapy


class QuotescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field()
    author = scrapy.Field()
    # name = scrapy.Field()
    #pass
