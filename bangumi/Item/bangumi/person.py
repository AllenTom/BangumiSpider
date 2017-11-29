import scrapy


class Person(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    info = scrapy.Field()
    character = scrapy.Field()
    works = scrapy.Field()
    cover_url = scrapy.Field()
    cover_prefix = scrapy.Field()
    detail = scrapy.Field()
    sex = scrapy.Field()
    birthday = scrapy.Field()
    blood = scrapy.Field()
    job = scrapy.Field()
    other_name = scrapy.Field()
    debut = scrapy.Field()
    height = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()


class PersonWork(scrapy.Item):
    bangumi_id = scrapy.Field()
    job = scrapy.Field()
    chinese_name = scrapy.Field()
    japan_name = scrapy.Field()


class PersonCharacter(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    job = scrapy.Field()
    work = scrapy.Field()


class PersonCharacterVoiceWork(scrapy.Item):
    bangumi_id = scrapy.Field()
    job = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
