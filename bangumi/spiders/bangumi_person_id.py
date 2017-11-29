# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector

from bangumi.items import BangumiIdListItem, BangumiIdItem
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiPersonIdSpider(scrapy.Spider):
    name = "bangumi_person_id"
    allowed_domains = ["bangumi.tv"]
    start_urls = ['http://bangumi.tv/person?page=%s' % page for page in range(1, 20)]
    max_page = -1

    def parse(self, response):
        if self.max_page == -1:
            self.max_page = int(re.findall('\( \d+ / (\d+) \)',
                                           Selector(response=response).xpath(
                                               '//span[@class="p_edge"]/text()').extract()[0], re.S)[0])
            for page in range(1, self.max_page):
                self.start_urls.append('http://bangumi.tv/person?page=%s' % page)

            print(self.start_urls)
            print("get max page: %s" % self.max_page)

        person_id_list = list()
        for person_field in Selector(response=response).xpath('//div[@class="light_odd clearit"]//h2'):
            person_id_list.append(BangumiIdItem(
                bangumi_id=get_field_value(person_field.xpath('./a/@href').re('/person/(\d+)')),
                bangumi_type="person",
                bangumi_name=get_field_value(person_field.xpath('./a/text()').extract())
            ))
        return BangumiIdListItem(bangumi_data=person_id_list)
