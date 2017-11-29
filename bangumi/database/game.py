from mongoengine import *


class GameCast(EmbeddedDocument):
    bangumi_person_id = StringField()
    chinese_name = StringField()
    japan_name = StringField()
    job = ListField()


class GameCharacterVoice(EmbeddedDocument):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()


class GameCharacterInfo(EmbeddedDocument):
    name = StringField()
    value = StringField()


class GameCharacter(EmbeddedDocument):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()
    job = StringField()
    cv = ListField(EmbeddedDocumentField(GameCharacterVoice))


class Game(Document):
    name = StringField()
    bangumi_id = IntField()
    detail = StringField()
    info = MapField(ListField())
    cast = ListField(EmbeddedDocumentField(GameCast))
    character = ListField(EmbeddedDocumentField(GameCharacter))
    created = DateTimeField()
    updated = DateTimeField()
