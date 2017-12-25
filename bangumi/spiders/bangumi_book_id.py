# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector

from bangumi.database.MongoModel import BangumiID
from bangumi.items import BangumiIdListItem, BangumiIdItem
from bangumi.spiders.bangumi_id import BangumiIdSpider


class BangumiBookIdSpider(BangumiIdSpider):
    name = "bangumi_book_id"
    subject_type = "book"
    id_type = "book"
