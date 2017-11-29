from mongoengine import *


class BangumiFailId(Document):
    bangumi_id = StringField()
    name = StringField()
    type = StringField()
    status = IntField()
    url = URLField()
    created = DateTimeField()
    updated = DateTimeField()


