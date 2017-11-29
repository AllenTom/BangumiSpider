import scrapy


class AnidbAnimate(scrapy.Item):
    ani_id = scrapy.Field()
    official_title = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
