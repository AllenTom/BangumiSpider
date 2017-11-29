# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy import Selector

from bangumi import db
from bangumi.Item.bangumi.character import Character, CharacterPlay
from bangumi.database.MongoModel import BangumiID
from bangumi.database.character import Character as CharacterDB
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiCharacterSpider(scrapy.Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection = db['BangumiID']
        id_list = [subject['bangumi_id'] for subject in self.collection.find({"bangumi_type": "character"})]
        spided_id = [character['bangumi_id'] for character in db['Character'].find()]
        for character_id in spided_id:
            id_list.remove(character_id)
        self.start_urls = ['http://bangumi.tv/character/%s' % subject_id for subject_id in
                           id_list]

    name = "bangumi_character"
    allowed_domains = ["bangumi.tv"]
    start_urls = []

    def parse(self, response):
        character = Character()
        root_selector = Selector(response)

        character['chinese_name'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/small/text()').extract())
        character['japan_name'] = get_field_value(root_selector.xpath('//*[@id="headerSubject"]/h1/a/text()').extract())
        character['bangumi_id'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/a/@href').re('/character/(\d+)'))

        character['cover_url'] = 'http:%s' % get_field_value(
            root_selector.xpath('//*[@id="columnCrtA"]/div[1]/div/a/@href').extract())
        character['cover_prefix'] = 'character'
        info_dict = dict()
        character['other_name'] = list()
        for info_item in root_selector.xpath('//*[@id="infobox"]/li'):

            name = info_item.xpath('.//text()').extract()[0][:-2]
            value = info_item.xpath('.//text()').extract()[1]
            if name == '别名':
                character['other_name'].append(value)
                continue
            if name == 'BWH':
                character['BWH'] = value
                continue
            if name == '生日':
                try:
                    character['birthday'] = datetime.datetime.strptime(value, "%m月%d日")
                    continue
                except:
                    try:
                        character['birthday'] = datetime.datetime.strptime(value, "%m-%d")
                        continue
                    except:
                        pass
                    pass
            if name == '性别':
                character['sex'] = value
                continue
            if name == '身高':
                try:
                    character['height'] = float(value[:-2])
                    continue
                except:
                    pass
            if name in info_dict:
                info_dict[name].append(value)
            else:
                info_dict[name] = [value]

        character['info'] = info_dict

        detail = root_selector.xpath('//*[@id="columnCrtB"]/div[2]/text()').extract()
        if len(detail) == 0:
            detail = ""
        else:
            detail = "".join(detail)

        character['detail'] = detail
        play_list = list()
        for play_field in root_selector.xpath('//*[@id="columnCrtB"]/ul/li'):
            character_play = CharacterPlay()
            character_play['bangumi_id'] = get_field_value(play_field.xpath('.//h3/a/@href').re('subject/(\d+)'))
            character_play['japan_name'] = get_field_value(play_field.xpath('.//h3/a/text()').extract())
            character_play['chinese_name'] = get_field_value(play_field.xpath('./div/div/small/text()').extract())
            character_play['job'] = get_field_value(play_field.xpath('./div/div/span/text()').extract())
            character_play['character_voice_bangumi_id'] = get_field_value(
                play_field.xpath('./ul/li/div/h3/a/@href').re('/person/(\d+)'))
            character_play['character_voice_name'] = get_field_value(
                play_field.xpath('./ul/li/div/h3/a/text()').extract())
            play_list.append(character_play)
        character['play'] = play_list
        return character
