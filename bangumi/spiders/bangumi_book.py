# -*- coding: utf-8 -*-
import datetime
import re

import scrapy
from scrapy import Selector

from bangumi import db
from bangumi.Item.bangumi.book import BookItem
from bangumi.spiders import SpiderDebug
from bangumi.spiders.bangumi_animate import get_field_value


class BangumiBookSpider(scrapy.Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not SpiderDebug:
            self.collection = db['Id']
            id_list = [subject['bangumi_id'] for subject in self.collection.find({"bangumi_type": "book"})]
            spided_id = [book['bangumi_id'] for book in db['Book'].find()]
            for book_id in spided_id:
                id_list.remove(book_id)
            self.start_urls = ['http://bangumi.tv/subject/%s' % subject_id for subject_id in
                               id_list]

    name = "bangumi_book"
    allowed_domains = ["bangumi.tv"]
    start_urls = ['http://bangumi.tv/subject/37783']

    def parse(self, response):
        book = BookItem()
        root_selector = Selector(response)
        book['book_type'] = get_field_value(response.xpath('//*[@id="headerSubject"]/h1/small/text()').extract())
        book['bangumi_id'] = get_field_value(
            root_selector.xpath('//*[@id="headerSubject"]/h1/a/@href').re('/subject/(\d+)'))
        book['name'] = get_field_value(root_selector.xpath('//*[@id="headerSubject"]/h1/a/text()').extract())
        book['detail'] = ''.join(root_selector.xpath('//*[@id="subject_summary"]/text()').extract()) if len(
            root_selector.xpath('//*[@id="subject_summary"]/text()').extract()) != 0 else None
        book['cover_url'] = 'http:%s' % get_field_value(
            root_selector.xpath('//*[@id="bangumiInfo"]/div/div/a/@href').extract())
        book['cover_prefix'] = 'book'
        tag_field = response.xpath('//*[@class="subject_tag_section"]//span/text()')
        book['tag'] = [tag.extract() for tag in tag_field]
        book_info_selector = Selector(response=response).xpath('//*[@id="infobox"]/li')
        book['info'] = dict()
        for item in book_info_selector:
            book_info_title = item.xpath('./span/text()').extract()[0][:-2]
            if book_info_title == '作者':
                book['author'] = get_field_value(item.xpath('./text()').extract())
                continue
            elif book_info_title == '出版社':
                book['press'] = get_field_value(item.xpath('./text()').extract())
                continue
            elif book_info_title == '发售日':
                try:
                    book['publish_date'] = datetime.datetime.strptime(get_field_value(item.xpath('./text()').extract()),
                                                                      "%Y-%m-%d")
                except:
                    pass
                continue
            elif book_info_title == 'ISBN':
                book['ISBN'] = get_field_value(item.xpath('./text()').extract())
                continue
            elif book_info_title == '页数':
                book['page'] = int(get_field_value(item.xpath('./text()').extract()))
                continue

            book['info'][book_info_title] = list()
            li_content = (item.extract())
            # 处理获取信息
            if li_content.find('<a') == -1:
                # 去除多余信息
                li_content = re.sub('<span class="tip">(.*?)</span>', "", li_content)
                li_content = re.sub("<.*?>", "", li_content)
                if li_content.find("、") != -1:
                    value_text_set = li_content.split("、")
                    for i in value_text_set:
                        book['info'][book_info_title].append(i)
                else:
                    book['info'][book_info_title].append(li_content)
            else:
                for value in item.xpath('.//a/text()').extract():
                    book['info'][book_info_title].append(value)
        return book
