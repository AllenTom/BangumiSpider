from mongoengine import *


class CharacterPlay(EmbeddedDocument):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()
    job = StringField()
    character_voice_name = StringField()
    character_voice_bangumi_id = StringField()


class Character(Document):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()
    info = MapField(ListField())
    detail = StringField()
    other_name = ListField()
    sex = StringField()
    birthday = DateTimeField()
    height = FloatField()
    BWH = StringField()
    play = ListField(EmbeddedDocumentField(CharacterPlay))
    created = DateTimeField()
    updated = DateTimeField()
