# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BangumiItem(scrapy.Item):
    # define the fields for your model here like:
    # name = scrapy.Field()
    pass


class BangumiIdItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    bangumi_type = scrapy.Field()
    bangumi_name = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()


class BangumiIdListItem(scrapy.Item):
    bangumi_data = scrapy.Field()





class BangumiBookIDsItem(scrapy.Item):
    bangumi_id_set = scrapy.Field()


class CharacterItem(scrapy.Item):
    character_bangumi_id = scrapy.Field()
    character_job = scrapy.Field()
    name_japan = scrapy.Field()
    name_chinese = scrapy.Field()
    character_info = scrapy.Field()
    character_voices = scrapy.Field()





class AnimateCastDataItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    animate_cast_data = scrapy.Field()


# character spider model
class PersonCharacterVoiceInfo(scrapy.Item):
    title = scrapy.Field()
    value = scrapy.Field()


class PersonCharacterVoiceCharacterWork(scrapy.Item):
    bangumi_id = scrapy.Field()
    job = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()


class PersonCharacterVoiceCharacter(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    work = scrapy.Field()


class PersonCharacterVoiceWork(scrapy.Item):
    bangumi_id = scrapy.Field()
    job = scrapy.Field()
    name = scrapy.Field()


class PersonCharacterVoice(scrapy.Item):
    bangumi_id = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    info = scrapy.Field()
    character = scrapy.Field()
    works = scrapy.Field()


class AnimateCoverItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    url = scrapy.Field()


class CharacterVoiceImgItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    url = scrapy.Field()


class CharacterImgItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    url = scrapy.Field()



