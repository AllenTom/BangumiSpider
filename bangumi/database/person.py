from mongoengine import *


class PersonCharacterWork(EmbeddedDocument):
    bangumi_id = StringField()
    job = StringField()
    japan_name = StringField()
    chinese_name = StringField()


class PersonCharacter(EmbeddedDocument):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()
    work = ListField(EmbeddedDocumentField(PersonCharacterWork))


class PersonWork(EmbeddedDocument):
    bangumi_id = StringField()
    job = ListField()
    chinese_name = StringField()
    japan_name = StringField()


class Person(Document):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()
    detail = StringField()
    sex = StringField()
    birthday = DateTimeField()
    blood = StringField()
    job = ListField()
    other_name = ListField()
    info = MapField(ListField())
    debut = DateTimeField()
    height = FloatField()
    character = ListField(EmbeddedDocumentField(PersonCharacter))
    person_works = ListField(EmbeddedDocumentField(PersonWork))
    created = DateTimeField()
    updated = DateTimeField()
