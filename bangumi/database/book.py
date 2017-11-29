from mongoengine import *


class Book(Document):
    bangumi_id = StringField()
    name = StringField()
    info = MapField(ListField())
    detail = StringField()
    tag = ListField()
    author = StringField()
    publish_date = DateTimeField()
    press = StringField()
    page = IntField()
    ISBN = StringField()
    book_type = StringField()
    created = DateTimeField()
    updated = DateTimeField()

