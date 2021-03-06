import scrapy


class BangumiIdItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    subject_type = scrapy.Field()
    name = scrapy.Field()
    create = scrapy.Field()
    update = scrapy.Field()


class BangumiIdListItem(scrapy.Item):
    bangumi_data = scrapy.Field()
