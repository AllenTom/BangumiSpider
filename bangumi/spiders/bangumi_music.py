# -*- coding: utf-8 -*-
import datetime
import re
from collections import OrderedDict

import logging
import scrapy
from scrapy import Selector, Request

from bangumi import db
from bangumi.Item.bangumi.music import Music, MusicTrack, MusicArtist
from bangumi.spiders import SpiderDebug
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiMusicSpider(scrapy.Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not SpiderDebug:
            self.collection = db['Id']
            id_list = [subject['bangumi_id'] for subject in self.collection.find({"bangumi_type": "music"})]
            spided_id = [music['bangumi_id'] for music in db['Music'].find()]
            for music_id in spided_id:
                id_list.remove(music_id)
            self.start_urls = ['http://bangumi.tv/subject/%s' % subject_id for subject_id in
                               id_list]

    name = "bangumi_music"
    allowed_domains = ["bangumi.tv"]
    start_urls = ['http://bangumi.tv/subject/4224']

    def parse(self, response):
        logging.info("loading")
        music = Music()
        root_selector = Selector(response)
        music['bangumi_id'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/a/@href').re('/subject/(\d+)'))
        music['name'] = get_field_value(root_selector.xpath('//*[@id="headerSubject"]/h1/a/text()').extract())
        music['detail'] = root_selector.xpath('//*[@id="subject_summary"]/text()')
        if len(music['detail']) == 0:
            music['detail'] = None
        else:
            music['detail'] = "".join(music['detail'].extract())
        try:
            music['cover_url'] = 'http:%s' % root_selector.xpath('//*[@id="bangumiInfo"]/div/div/a/@href').extract()[0]
        except:
            music['cover_url'] = None
        music['cover_prefix'] = 'music'
        music_info_selector = Selector(response=response).xpath('//*[@id="infobox"]/li')
        music['info'] = dict()
        for item in music_info_selector:
            music_info_title = item.xpath('./span/text()').extract()[0][:-2]
            if music_info_title == '发售日期':
                try:
                    music['publish_date'] = datetime.datetime.strptime(
                        get_field_value(item.xpath('./text()').extract()),
                        "%Y-%m-%d")
                except:
                    pass

            music['info'][music_info_title] = list()
            li_content = (item.extract())
            # 处理获取信息
            if li_content.find('<a') == -1:
                # 去除多余信息
                li_content = re.sub('<span class="tip">(.*?)</span>', "", li_content)
                li_content = re.sub("<.*?>", "", li_content)
                if li_content.find("、") != -1:
                    value_text_set = li_content.split("、")
                    for i in value_text_set:
                        music['info'][music_info_title].append(i)
                else:
                    music['info'][music_info_title].append(li_content)
            else:
                for value in item.xpath('.//a/text()').extract():
                    music['info'][music_info_title].append(value)
        tag_field = response.xpath('//*[@class="subject_tag_section"]//span/text()')
        music['tag'] = [tag.extract() for tag in tag_field]

        request = Request('http://bangumi.tv/subject/%s/ep' % music['bangumi_id'], callback=self.parse_music_tract)
        request.meta['music'] = music
        return request

    def parse_music_tract(self, response):
        music = response.meta['music']
        root_selector = Selector(response)
        cat_cur = ""
        music['track'] = OrderedDict()
        for episode_field in root_selector.xpath('//*[@id="columnInSubjectA"]/div/ul/li'):
            episode_type = get_field_value(episode_field.xpath('./@class').extract())
            if episode_type == 'cat':
                cat_cur = get_field_value(episode_field.xpath('./text()').extract())
                music['track'][cat_cur] = list()
            else:
                track = MusicTrack()
                track['name'] = get_field_value(episode_field.xpath('./h6/a/text()').extract())
                track['bangumi_id'] = get_field_value(episode_field.xpath('./h6/a/@href').re('/ep/(\d+)'))
                track['number'] = get_field_value(episode_field.xpath('./h6/a/text()').re('^(\d+)'))
                track['artist'] = get_field_value(episode_field.xpath('./h6/a/text()').re('\((.*?)\)$'))
                track['name'] = track['name'].replace('%s.' % track['number'], '').replace('(%s)' % track['artist'], '')
                music['track'][cat_cur].append(track)
        request = Request('http://bangumi.tv/subject/%s/persons' % music['bangumi_id'],
                          callback=self.parse_music_artist)
        request.meta['music'] = music
        return request

    def parse_music_artist(self, response):
        music = response.meta['music']
        root_selector = Selector(response)
        music['artist'] = list()
        for artist_field in root_selector.xpath('//*[@id="columnInSubjectA"]/div'):
            artist = MusicArtist()
            artist['japan_name'] = artist_field.xpath('./div/h2/a/text()').extract()[0].replace('  / ', '')
            artist['bangumi_id'] = get_field_value(artist_field.xpath('./div/h2/a/@href').re('/person/(\d+)'))
            artist['chinese_name'] = get_field_value(artist_field.xpath('./div/h2/a/span/text()').extract())
            artist['job'] = get_field_value(artist_field.re('<span class="badge_job">(.*?)</span>'))
            music['artist'].append(artist)
        return music
