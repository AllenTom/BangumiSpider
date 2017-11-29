import scrapy


class MusicArtist(scrapy.Field):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    job = scrapy.Field()


class MusicTrack(scrapy.Item):
    bangumi_id = scrapy.Field()
    name = scrapy.Field()
    artist = scrapy.Field()
    number = scrapy.Field()


class Music(scrapy.Item):
    bangumi_id = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    cover_url = scrapy.Field()
    cover_prefix = scrapy.Field()
    publish_date = scrapy.Field()
    tag = scrapy.Field()
    info = scrapy.Field()
    track = scrapy.Field()
    artist = scrapy.Field()
