# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy import Selector

from bangumi import db
from bangumi.Item.bangumi.person import Person, PersonCharacter, PersonCharacterVoiceWork
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiCvSpider(scrapy.Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection = db['Id']
        id_list = [subject['bangumi_id'] for subject in self.collection.find({"bangumi_type": "person"})]
        spided_id = [person['bangumi_id'] for person in db['Person'].find()]
        for person_id in spided_id:
            id_list.remove(person_id)
        self.start_urls = ['http://bangumi.tv/person/%s' % subject_id for subject_id in
                           id_list]

    name = "bangumi_person"
    allowed_domains = ["bangumi.tv"]
    start_urls = []

    def parse(self, response):
        person = Person(works=[], character=[])
        root_selector = Selector(response)
        person['bangumi_id'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/a/@href').re('/person/(\d+)'))
        person['japan_name'] = get_field_value(root_selector.xpath('//*[@id="headerSubject"]/h1/a/text()').extract())
        person['chinese_name'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/small/text()').extract())
        person['job'] = get_field_value(
            root_selector.xpath('//*[@id="columnCrtB"]/div[1]/h2/text()').re(' {1}(\S{1,}?) {1}'))
        person['detail'] = ''.join(root_selector.xpath('//*[@id="columnCrtB"]/div[2]/text()').extract()) if len(
            root_selector.xpath('//*[@id="columnCrtB"]/div[2]/text()').extract()) != 0 else None

        person['cover_url'] = 'http://%s' % root_selector.xpath('//*[@id="columnCrtA"]/div[1]/div/a/@href').extract()[
            0] if len(root_selector.xpath('//*[@id="columnCrtA"]/div[1]/div/a/@href').extract()) != 0 else ''
        print(person['cover_url'])
        person['cover_prefix'] = 'person'
        person['info'] = dict()
        person['other_name'] = list()
        for info_item in root_selector.xpath('//*[@id="infobox"]/li'):

            name = info_item.xpath('.//text()').extract()[0][:-2]
            value = info_item.xpath('.//text()').extract()[1]

            if name == '性别':
                person['sex'] = value
                continue

            if name == '别名':
                person['other_name'].append(value)
                continue
            if name == '生日':
                try:
                    person['birthday'] = datetime.datetime.strptime(value, "%Y年%m月%d日")
                    continue
                except:
                    try:
                        person['birthday'] = datetime.datetime.strptime(value, "%Y-%m-%d")
                        continue
                    except:
                        pass
                    pass
            if name == '血型':
                person['blood'] = value
                continue
            if name == '出道时间':
                try:
                    person['debut'] = datetime.datetime.strptime(value, "%Y")
                    continue
                except:
                    pass
            if name == '身高':
                try:
                    person['height'] = float(value[:-2])
                    continue
                except:
                    pass

            if name in person['info']:
                person['info'][name].append(value)
            else:
                person['info'][name] = [value]

        if root_selector.xpath('//*[@id="headerSubject"]/div/ul/li[2]/a/text()').extract()[0] == "角色":
            request = scrapy.Request('http://bangumi.tv/person/%s/works/voice' % person['bangumi_id'],
                                     callback=self.parse_cv_character)
            request.meta['person'] = person
            return request
        else:
            request = scrapy.Request(
                'http://bangumi.tv/person/%s/works?sort=date&page=1' % person['bangumi_id'],
                callback=self.parse_cv_work)
            request.meta['person'] = person
            return request

    def parse_cv_character(self, response):
        person = response.meta['person']
        person['character'] = list()
        root_selector = Selector(response)
        for character_li in root_selector.xpath('//*[@id="columnCrtB"]/div[2]/ul/li'):
            character = PersonCharacter()
            character['japan_name'] = get_field_value(
                character_li.xpath('.//div[@class="ll innerLeftItem"]/a/@title').extract())
            character['bangumi_id'] = get_field_value(
                character_li.xpath('.//div[@class="ll innerLeftItem"]/a/@href').re('/character/(\d+)'))
            character['chinese_name'] = get_field_value(
                character_li.xpath('.//div[@class="ll innerLeftItem"]//p/text()').extract())
            character['work'] = list()
            for work in character_li.xpath('.//ul/li'):
                character_work = PersonCharacterVoiceWork()
                character_work['bangumi_id'] = get_field_value(work.xpath('.//div/h3/a/@href').re('/subject/(\d+)'))
                character_work['japan_name'] = get_field_value(work.xpath('.//div/h3/a/text()').extract())
                character_work['chinese_name'] = get_field_value(work.xpath('.//div//small/text()').extract())
                character['job'] = get_field_value(work.xpath('.//div/span/text()').extract())
                character['work'].append(character_work)
            person['character'].append(character)
        request = scrapy.Request('http://bangumi.tv/person/%s/works?sort=date&page=1' % person['bangumi_id'],
                                 callback=self.parse_cv_work)
        request.meta['person'] = person
        return request

    def parse_cv_work(self, response):
        person = response.meta['person']
        root_selector = Selector(response)
        for work_field in root_selector.xpath('//*[@id="browserItemList"]/li'):
            cv_work = PersonCharacterVoiceWork()
            if len(work_field.xpath('.//div/h3/small/text()')) == 0:
                cv_work['japan_name'] = get_field_value(work_field.xpath('.//div/h3/a/text()').extract())
            else:
                cv_work['japan_name'] = work_field.xpath('.//div/h3/small/text()').extract()[0] if len(
                    work_field.xpath('.//div/h3/small/text()').extract()[0]) != 0 else None
                cv_work['chinese_name'] = get_field_value(work_field.xpath('.//div/h3/a/text()').extract())
            cv_work['bangumi_id'] =get_field_value( work_field.xpath('.//div/h3/a/@href').re('subject/(\d+)'))
            cv_work['job'] = work_field.xpath('.//span[@class="badge_job"]/text()').extract()
            person['works'].append(cv_work)
        try:
            if root_selector.xpath('//*[@id="columnCrtB"]/div[3]/div/div/a/text()').extract()[-1] == "››":
                next_url = root_selector.xpath('//*[@id="columnCrtB"]/div[3]/div/div/a/@href').extract()[-1]
                request = scrapy.Request('http://bangumi.tv/person/%s/works%s' % (person['bangumi_id'], next_url),
                                         callback=self.parse_cv_work)
                request.meta['person'] = person
                return request
        except:
            return person
            pass

        return person
