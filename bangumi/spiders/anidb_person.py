# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class AnidbPersonSpider(scrapy.Spider):
    name = 'anidb_person'
    allowed_domains = ['anidb.net']
    start_urls = ['http://anidb.net/perl-bin/animedb.pl?show=creator&creatorid=1523']

    def start_requests(self):
        headers = {
            "Accept - Encoding": "gzip, deflate, sdch",
            "User-Agent": 'Googlebot-Image/1.0'
        }
        for i, url in enumerate(self.start_urls):
            yield Request(url, cookies={'adbuin': '1426674399-dzhZ  ',
                                        'anidbdefaulttabs': '"anime":{"tabbed_pane":{"locked":false},"tabbed_pane_main_1":{"locked":false},"tabbed_pane_main_2":{"locked":false},"tabbed_pane_main_3":{"locked":false},"tabbed_pane_main_4":{"name":"tab.staff","locked":false}},"creator":{"tabbed_pane":{"locked":false},"tabbed_pane_main_1":{"name":"tab.anime_production_major","locked":false},"tabbed_pane_main_2":{"name":"tab.anime_production_major","locked":false},"tabbed_pane_1":{"locked":false},"tabbed_pane_main_1_1":{"locked":false},"tabbed_pane_main_1_2":{"locked":false}}'},
                          callback=self.parse, headers=headers)

    def parse(self, response):
        print(response.body)
        for info_field in response.xpath('//*[@id="tab_1_pane"]/div/table/tbody/tr'):
            title = info_field.xpath('./th/text()').extract()[0]
            print(title)
