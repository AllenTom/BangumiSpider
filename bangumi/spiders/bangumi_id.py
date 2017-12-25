# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from scrapy import Selector
from scrapy.http import Response

from bangumi.items import BangumiIdListItem, BangumiIdItem


class BangumiIdSpider(scrapy.Spider):
    name = "bangumi_id"
    allowed_domains = ["bangumi.tv"]
    start_urls = []
    # start_urls = ['http://bangumi.tv/anime/browser?page=1']
    max_page = -1
    id_type = "unknown"
    subject_type = "anime"

    def __init__(self, **kwargs):
        logging.log(logging.DEBUG, f'{self.subject_type} subject spider,id type is {self.id_type}')
        self.start_urls = [f'http://bangumi.tv/{self.subject_type}/browser?page=%s' % page for page in range(1, 20)]
        super().__init__(**kwargs)

    def parse(self, response: Response):
        id_sl = Selector(response=response).xpath('//*[@id="browserItemList"]/li')
        if self.max_page == -1:
            self.max_page = int(re.findall('\( \d+ / (\d+) \)',
                                           Selector(response=response).xpath(
                                               '//span[@class="p_edge"]/text()').extract()[0], re.S)[0])
            for page in range(1, self.max_page):
                self.start_urls.append(f'http://bangumi.tv/{self.subject_type}/browser?page=%s' % page)
        id_item_set = list()
        for subject in id_sl:
            id_item_set.append(BangumiIdItem(bangumi_id=subject.re('<a href="/subject/(.*?)" class="l">.*?</a>')[0],
                                             bangumi_type=self.id_type,
                                             bangumi_name=subject.re('<a href="/subject/.*?" class="l">(.*?)</a>')[0]))
        return BangumiIdListItem(bangumi_data=id_item_set)
