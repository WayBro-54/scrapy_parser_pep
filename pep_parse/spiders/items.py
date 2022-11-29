import scrapy


class PepParsingItem(scrapy.Item):
    text = scrapy.Field()
    status = scrapy.Field()
    number = scrapy.Field()
