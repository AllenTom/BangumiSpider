import scrapy
from mongoengine import *


class GameCast(scrapy.Item):
    bangumi_id = scrapy.Field()
    chinese_name = scrapy.Field()
    japan_name = scrapy.Field()
    job = scrapy.Field()


class GameCharacterVoice(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()


class GameCharacterInfo(scrapy.Item):
    name = scrapy.Field()
    value = scrapy.Field()


class GameCharacter(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    job = scrapy.Field()
    cv = scrapy.Field()


class Game(scrapy.Item):
    name = scrapy.Field()
    chinese_name = scrapy.Field()
    release_date = scrapy.Field()
    bangumi_id = scrapy.Field()
    detail = scrapy.Field()
    info = scrapy.Field()
    cast = scrapy.Field()
    cover_url = scrapy.Field()
    cover_prefix = scrapy.Field()
    character = scrapy.Field()
    platform = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
