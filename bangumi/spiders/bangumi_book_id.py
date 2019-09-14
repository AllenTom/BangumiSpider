# -*- coding: utf-8 -*-

from bangumi.spiders.bangumi_id import BangumiIdSpider


class BangumiBookIdSpider(BangumiIdSpider):
    name = "bangumi_book_id"
    subject_type = "book"
    id_type = "book"
