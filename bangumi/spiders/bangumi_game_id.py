# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector

from bangumi.items import BangumiIdItem, BangumiIdListItem


class BangumiGameIdSpider(scrapy.Spider):
    name = "bangumi_game_id"
    allowed_domains = ["bangumi.tv"]
    start_urls = ['http://bangumi.tv/game/browser?page=%s' % page for page in range(1, 20)]
    max_page = -1
    def parse(self, response):
        id_sl = Selector(response=response).xpath('//*[@id="browserItemList"]/li')
        if self.max_page == -1:
            self.max_page = int(re.findall('\( \d+ / (\d+) \)',
                                           Selector(response=response).xpath(
                                               '//span[@class="p_edge"]/text()').extract()[0], re.S)[0])
            for page in range(1, self.max_page):
                self.start_urls.append('http://bangumi.tv/game/browser?page=%s' % page)

            print(self.start_urls)
            print("get max page: %s" % self.max_page)

        id_item_set = list()
        for subject in id_sl:
            id_item_set.append(BangumiIdItem(bangumi_id=subject.re('<a href="/subject/(.*?)" class="l">.*?</a>')[0],
                                             bangumi_type='game',
                                             bangumi_name=subject.re('<a href="/subject/.*?" class="l">(.*?)</a>')[0]))
        return BangumiIdListItem(bangumi_data=id_item_set)
