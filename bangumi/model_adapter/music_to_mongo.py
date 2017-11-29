from bangumi.database.music import *


def music_to_mongo(item):
    music = Music(
        bangumi_id=item['bangumi_id'],
        name=item['name'],
        info=item['info'],
        detail=item['detail']
    )
    track_dict = dict()
    for cat in item['track']:
        track_dict[cat] = list()
        for ep in item['track'][cat]:
            track = MusicTrack()
            track.name = ep['name']
            track.artist = ep['artist']
            track.bangumi_id = ep['bangumi_id']
            track.number = ep['number']
            track_dict[cat].append(track)
    music.track = track_dict
    artist_list = list()
    for artist in item['artist']:
        music_artist = MusicArtist()
        music_artist.bangumi_id = artist['bangumi_id']
        music_artist.job = artist['job']
        music_artist.chinese_name = artist['chinese_name']
        music_artist.japan_name = artist['japan_name']
        artist_list.append(music_artist)
    music.artist = artist_list
    return music
