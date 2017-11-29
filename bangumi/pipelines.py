# -*- coding: utf-8 -*-

# Define your model pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from bangumi import db
from bangumi.Item.anidb.animate import AnidbAnimate
from bangumi.Item.bangumi.animate import AnimateItem
from bangumi.Item.bangumi.book import BookItem
from bangumi.Item.bangumi.character import Character
from bangumi.Item.bangumi.game import Game
from bangumi.Item.bangumi.music import Music
from bangumi.Item.bangumi.person import Person
from bangumi.items import BangumiIdListItem


class BangumiPipeline(object):
    def process_item(self, item, spider):
        return item


class BangumiAnimatePipelines(object):
    def __init__(self):
        self.collection = db['Animate']

    def process_item(self, item, spider):
        if isinstance(item, AnimateItem):
            save_to_database(item, self.collection)
        return item


class BangumiGamePipelines(object):
    def __init__(self):
        self.collection = db['Game']

    def process_item(self, item, spider):
        if isinstance(item, Game):
            save_to_database(item, self.collection)
        return item


class BangumiIDPipelines(object):
    def __init__(self):
        self.collection = db['BangumiID']

    def process_item(self, item, spider):
        if isinstance(item, BangumiIdListItem):
            for subject in item['bangumi_data']:
                save_to_database(subject, self.collection)
        return item


class BangumiPersonPipelines(object):
    def __init__(self):
        self.collection = db['Person']

    def process_item(self, item, spider):
        if isinstance(item, Person):
            save_to_database(item, self.collection)

        return item
class AnidbAnimatePipelines(object):
    def __init__(self):
        self.collection = db['AniDB_Animate']
    def process_item(self, item, spider):
        if isinstance(item, AnidbAnimate):
            print('---------------------------')
            print(item)
            save_anidb_to_database(item, self.collection)
        return item

class BangumiCharacterPipelines(object):
    def __init__(self):
        self.collection = db['Character']

    def process_item(self, item, spider):
        if isinstance(item, Character):
            save_to_database(item, self.collection)
        return item


class ImageDownloadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if  'cover_url' in item and len(item['cover_url']) != 0:
            print("%s_%s" % (item['bangumi_id'], item['cover_prefix']))
            return Request(url=item['cover_url'],
                           meta={'image_name': "%s_%s" % (item['bangumi_id'], item['cover_prefix'])})
        return

    def file_path(self, request, response=None, info=None):
        image_name = request.meta['image_name']
        filename = image_name + '.jpg'
        return filename

    def item_completed(self, results, item, info):
        return item


class BangumiBookPipelines(object):
    def __init__(self):
        self.collection = db['Book']

    def process_item(self, item, spider):
        if isinstance(item, BookItem):
            save_to_database(item, self.collection)
        return item


class BangumiMusicPipelines(object):
    def __init__(self):
        self.collection = db['Music']

    def process_item(self, item, spider):
        if isinstance(item, Music):
            save_to_database(item, self.collection)
        return item


def save_to_database(item, collection):
    model = dict(item)
    if 'cover_prefix' in model:
        model.pop('cover_prefix')
    model['updated'] = datetime.datetime.now()
    exist_model = collection.find_one({'bangumi_id': model['bangumi_id']})
    if exist_model is not None:
        model['created'] = exist_model['created']
        collection.replace_one({'_id': exist_model['_id']}, model, upsert=True)
    else:
        model['created'] = datetime.datetime.now()
        try:
            collection.insert(model)
        except:
            pass

def save_anidb_to_database(item, collection):
    model = dict(item)
    if 'cover_prefix' in model:
        model.pop('cover_prefix')
    model['updated'] = datetime.datetime.now()
    exist_model = collection.find_one({'ani_id': model['ani_id']})
    if exist_model is not None:
        model['created'] = exist_model['created']
        collection.replace_one({'_id': exist_model['_id']}, model, upsert=True)
    else:
        model['created'] = datetime.datetime.now()

        collection.insert(model)
