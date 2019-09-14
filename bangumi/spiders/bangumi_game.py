# -*- coding: utf-8 -*-
import datetime
import re

import scrapy
from scrapy import Selector, Request

from bangumi import db
from bangumi.Item.bangumi.game import Game, GameCharacterVoice, GameCharacter, GameCast
from bangumi.spiders import SpiderDebug
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiGameSpider(scrapy.Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not SpiderDebug:
            self.collection = db['Id']
            id_list = [subject['bangumi_id'] for subject in self.collection.find({"bangumi_type": "game"})]
            spided_id = [game['bangumi_id'] for game in db['Game'].find()]
            for game_id in spided_id:
                id_list.remove(game_id)
            self.start_urls = ['http://bangumi.tv/subject/%s' % subject_id for subject_id in
                               id_list]

    name = "bangumi_game"
    allowed_domains = ["bangumi.tv"]
    start_urls = ['http://bangumi.tv/subject/88868']

    def parse(self, response):
        game = Game()
        root_selector = Selector(response)
        game['bangumi_id'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/a/@href').re('/subject/(\d+)'))
        game['name'] = get_field_value(root_selector.xpath('//*[@id="headerSubject"]/h1/a/text()').extract())
        game['detail'] = ''.join(
            get_field_value(root_selector.xpath('//*[@id="subject_summary"]/text()').extract())) if len(
            root_selector.xpath('//*[@id="subject_summary"]/text()').extract()) != 0 else None
        try:
            game['cover_url'] = 'http:%s' % root_selector.xpath('//*[@id="bangumiInfo"]/div/div/a/@href').extract()[0]
        except:
            game['cover_url'] = None
        game['cover_prefix'] = 'game'
        game_info_selector = Selector(response=response).xpath('//*[@id="infobox"]/li')
        game['info'] = dict()
        game['platform'] = list()
        for item in game_info_selector:
            game_info_title = item.xpath('./span/text()').extract()[0][:-2]
            if game_info_title == '中文名':
                try:
                    game['chinese_name'] = get_field_value(item.xpath('./text()').extract())
                    continue
                except:
                    pass
            if game_info_title == '发行日期':
                try:
                    game['release_date'] = datetime.datetime.strptime(item.xpath('./text()').extract()[0], "%Y年%m月%d日")
                    continue
                except:
                    try:
                        game['release_date'] = datetime.datetime.strptime(item.xpath('./text()').extract()[0],
                                                                          "%Y-%m-%d")
                        continue
                    except:
                        pass
            if game_info_title == '平台':
                game['platform'].append(get_field_value(item.xpath('./text()').extract()))
                continue
            game['info'][game_info_title] = list()
            li_content = (item.extract())
            # 处理获取信息
            if li_content.find('<a') == -1:
                # 去除多余信息
                li_content = re.sub('<span class="tip">(.*?)</span>', "", li_content)
                li_content = re.sub("<.*?>", "", li_content)
                if li_content.find("、") != -1:
                    value_text_set = li_content.split("、")
                    for i in value_text_set:
                        game['info'][game_info_title].append(i)
                else:
                    game['info'][game_info_title].append(li_content)
            else:
                for value in item.xpath('.//a/text()').extract():
                    game['info'][game_info_title].append(value)
        request = Request(url='http://bangumi.tv/subject/%s/characters' % game['bangumi_id'],
                          callback=self.parse_game_character)
        request.meta['game'] = game
        print(game['chinese_name'])
        print(game['release_date'] if game['release_date'] is not None else "No date")
        print(game['platform'])
        return request

    def parse_game_character(self, response):
        game = response.meta['game']
        game['character'] = list()
        character_field = Selector(response).xpath('//*[@id="columnInSubjectA"]')
        for character in character_field.xpath('.//div[@class="clearit"]'):
            game_character = GameCharacter()
            game_character['cv'] = list()
            game_character['bangumi_id'] = get_field_value(character.re('<a href="/character/(\d+)" class="l">'))

            game_character['japan_name'] = get_field_value(character.xpath('./h2/a/text()').extract())
            game_character['chinese_name'] = get_field_value(character.xpath('./h2/span/text()').extract())[3:]
            game_character['job'] = get_field_value(character.re('<span class="badge_job">(.*?)</span>'))

            # cv information
            cv_list_field = character.xpath('.//div[@class = "actorBadge clearit"]/p')
            for cv_list in cv_list_field:
                cv = GameCharacterVoice()
                cv['bangumi_id'] = get_field_value(cv_list.re('<a href="/person/(\d+)" class="l">'))
                cv['japan_name'] = get_field_value(cv_list.xpath('./a/text()').extract())

                cv['chinese_name'] = get_field_value(cv_list.xpath('./small/text()').extract())
                game_character['cv'].append(cv)
            game['character'].append(game_character)
        request = Request(url='http://bangumi.tv/subject/%s/persons' % game['bangumi_id'],
                          callback=self.parse_game_cast)
        request.meta['game'] = game
        return request

    def parse_game_cast(self, response):
        game = response.meta['game']
        cast_set_field = Selector(response).xpath('//*[@id="columnInSubjectA"]/div[@class = "light_odd clearit"]')
        game['cast'] = list()
        for cast_item_field in cast_set_field:
            cast = GameCast()
            cast['bangumi_id'] = get_field_value(cast_item_field.xpath('.//h2/a').re('/person/(\d+)'))
            cast['japan_name'] = get_field_value(
                cast_item_field.xpath('.//h2/a/text()').extract()).replace(" / ", "") if get_field_value(
                cast_item_field.xpath('.//h2/a/text()').extract()) is not None else None
            cast['chinese_name'] = get_field_value(cast_item_field.xpath('.//h2/a/span/text()').extract())

            cast['job'] = list()
            for job in cast_item_field.xpath('.//div[@class = "prsn_info"]//span[@class = "badge_job"]/text()'):
                cast['job'].append(job.extract())
            game['cast'].append(cast)
        return game
