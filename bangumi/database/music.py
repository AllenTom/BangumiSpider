from mongoengine import *


class MusicArtist(EmbeddedDocument):
    bangumi_id = StringField()
    japan_name = StringField()
    chinese_name = StringField()
    job = StringField()


class MusicTrack(EmbeddedDocument):
    bangumi_id = StringField()
    name = StringField()
    number = StringField()
    artist = StringField()


class Music(Document):
    bangumi_id = StringField()
    name = StringField()
    cover_url = StringField()
    detail = StringField()
    info = MapField(ListField())
    track = MapField(ListField(EmbeddedDocumentField(MusicTrack)))
    artist = ListField(EmbeddedDocumentField(MusicArtist))
    created = DateTimeField()
    updated = DateTimeField()
