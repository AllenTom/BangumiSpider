# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector

from bangumi.items import BangumiIdListItem, BangumiIdItem
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiCharacterIdSpider(scrapy.Spider):
    name = "bangumi_character_id"
    allowed_domains = ["bangumi.tv"]
    start_urls = ['http://bangumi.tv/character?orderby=collects&page=%s' % page for page in range(1, 20)]
    # start_urls = ['http://bangumi.tv/character?orderby=collects&page=1']
    max_page = -1

    def parse(self, response):
        if self.max_page == -1:
            self.max_page = int(re.findall('\( \d+ / (\d+) \)',
                                           Selector(response=response).xpath(
                                               '//span[@class="p_edge"]/text()').extract()[0], re.S)[0])
            for page in range(1, self.max_page):
                self.start_urls.append('http://bangumi.tv/character?orderby=collects&page=%s' % page)

        character_id_list = list()
        for character_field in Selector(response).xpath('//div[@class="light_odd clearit"]//h2'):
            character_id_list.append(BangumiIdItem(
                bangumi_id=get_field_value(character_field.xpath('./a/@href').re('/character/(\d+)')),
                bangumi_type="character",
                bangumi_name=get_field_value(character_field.xpath('./a/text()').extract())
            ))
        return BangumiIdListItem(bangumi_data=character_id_list)
