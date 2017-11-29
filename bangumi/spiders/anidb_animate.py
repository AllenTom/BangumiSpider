# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy import Request

from bangumi.Item.anidb.animate import AnidbAnimate
from bangumi.spiders.bangumi_animate import get_field_value


class AnidbAnimateSpider(scrapy.Spider):
    name = 'anidb_animate'
    allowed_domains = ['http://anidb.net']
    start_urls = ['file:///C:/Users/TakayamaAren/Desktop/test/Eromanga-sensei%20-%20Anime%20-%20AniDB.html']

    def start_requests(self):
        headers = {
            "Accept - Encoding": "gzip, deflate, sdch",
            "User-Agent": 'Googlebot-Image/1.0'
        }
        for i, url in enumerate(self.start_urls):
            yield Request(url, cookies={'adbuin': '1496676366-hvsZ  '}, callback=self.parse, headers=headers)

    def parse(self, response):
        animate = AnidbAnimate()
        # print(response.body)
        # print(response.xpath('//*[@id="tab_1_pane"]/div/table/tbody/tr[3]/td/label/text()').extract())
        animate['ani_id'] = get_field_value(
            response.xpath('//*[@id="tab_1_pane"]/div/table/tbody/tr[1]/td/a/text()').re('^a(\d+)'))
        animate['official_title'] = list()
        for info_field in response.xpath('//*[@id="tab_1_pane"]/div/table/tbody/tr'):
            field_title = get_field_value(info_field.xpath('./th/text()').extract())
            if field_title == 'Official Title':
                animate['official_title'].append(info_field.xpath('./td/label/text()').extract()[0])
            elif field_title == 'Year':
                try:
                    animate['start'] = datetime.datetime.strptime(
                        get_field_value(info_field.xpath('./td/span[@itemprop="startDate"]/@content').extract()),
                        '%Y-%m-%d')
                except:
                    pass
                try:
                    animate['end'] = datetime.datetime.strptime(
                        get_field_value(info_field.xpath('./td/span[@itemprop="endDate"]/@content').extract()),
                        '%Y-%m-%d')
                except:
                    pass

        for staff_field in response.xpath('//*[@id="stafflist1"]/tbody/tr'):
            job


        return animate
