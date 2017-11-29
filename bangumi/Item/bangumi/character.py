import scrapy


class Character(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    other_name = scrapy.Field()
    sex = scrapy.Field()
    birthday = scrapy.Field()
    height = scrapy.Field()
    BWH = scrapy.Field()
    info = scrapy.Field()
    detail = scrapy.Field()
    play = scrapy.Field()
    cover_url = scrapy.Field()
    cover_prefix = scrapy.Field()


class CharacterPlay(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    job = scrapy.Field()
    character_voice_name = scrapy.Field()
    character_voice_bangumi_id = scrapy.Field()
