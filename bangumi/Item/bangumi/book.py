import scrapy


class BookItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    cover_url = scrapy.Field()
    cover_prefix = scrapy.Field()
    tag = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()
    press = scrapy.Field()
    page = scrapy.Field()
    ISBN = scrapy.Field()
    book_type = scrapy.Field()
    info = scrapy.Field()


