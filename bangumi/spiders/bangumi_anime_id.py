from bangumi.spiders.bangumi_id import BangumiIdSpider


class BangumiAnimeIdSpider(BangumiIdSpider):
    subject_type = "anime"
    id_type = "animate"
    name = "bangumi_anime_id"
