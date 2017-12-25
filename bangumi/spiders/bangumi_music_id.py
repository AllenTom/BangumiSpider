# -*- coding: utf-8 -*-

from bangumi.spiders.bangumi_id import BangumiIdSpider


class BangumiMusicIdSpider(BangumiIdSpider):
    name = "bangumi_music_id"
    id_type = "music"
    subject_type = "music"
