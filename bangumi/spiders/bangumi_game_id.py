# -*- coding: utf-8 -*-

from bangumi.spiders.bangumi_id import BangumiIdSpider


class BangumiGameIdSpider(BangumiIdSpider):
    name = "bangumi_game_id"
    id_type = "game"
    subject_type = "game"
