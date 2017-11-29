import scrapy


class PicItem(scrapy.Item):
    url = scrapy.Field()
    bangumi_id = scrapy.Field()
    type = scrapy.Field()
