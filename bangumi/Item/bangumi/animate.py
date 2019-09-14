import scrapy


class AnimateItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    animate_type = scrapy.Field()
    name = scrapy.Field()
    summary = scrapy.Field()
    info = scrapy.Field()
    cover_url = scrapy.Field()
    cover_prefix = scrapy.Field()
    cast = scrapy.Field()
    character = scrapy.Field()
    episode = scrapy.Field()
    tag = scrapy.Field()
    start_play = scrapy.Field()
    chinese_name = scrapy.Field()
    episode_count = scrapy.Field()
    created = scrapy.Field()
    updated = scrapy.Field()
    rate = scrapy.Field()

class AnimateEpisodeItem(scrapy.Item):
    number = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    show_date = scrapy.Field()

class AnimateCastItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    job = scrapy.Field()


class AnimateCharacterItem(scrapy.Item):
    bangumi_id = scrapy.Field()
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    icon_url = scrapy.Field()
    job = scrapy.Field()
    info = scrapy.Field()
    cv = scrapy.Field()



class AnimateCharacterInfoItem(scrapy.Item):
    title = scrapy.Field()
    value = scrapy.Field()


class AnimateCharacterCVItem(scrapy.Item):
    japan_name = scrapy.Field()
    chinese_name = scrapy.Field()
    bangumi_id = scrapy.Field()
    icon_url = scrapy.Field()


class AnimateCategoryItem(scrapy.Item):
    name = scrapy.Field()
    episode_list = scrapy.Field()
