from bangumi.database.MongoModel import BangumiID


def id_to_mongo(item):
    return BangumiID(bangumi_id=item['bangumi_id'], name=item['bangumi_name'], type=item['bangumi_type'])
