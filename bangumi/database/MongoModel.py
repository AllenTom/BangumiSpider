from mongoengine import *


class BangumiID(Document):
    bangumi_id = StringField()
    name = StringField()
    type = StringField()
    created = DateTimeField()
    updated = DateTimeField()
