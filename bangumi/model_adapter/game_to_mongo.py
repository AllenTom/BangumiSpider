from bangumi.database.game import *


def game_to_mongo(item):
    game = Game(
        name=item['name'],
        bangumi_id=item['bangumi_id'],
        detail=item['detail'],
        info=item['info']
    )

    game_cast_list = list()
    for cast in item['cast']:
        game_cast_list.append(GameCast(
            bangumi_person_id=cast['bangumi_id'],
            japan_name=cast['japan_name'],
            chinese_name=cast['chinese_name'],
            job=cast['job']
        ))
    game.cast = game_cast_list

    character_list = list()
    for character in item['character']:

        character_voice_list = [
            GameCharacterVoice(bangumi_id=cv['bangumi_id'],
                               japan_name=cv['japan_name'],
                               chinese_name=cv['chinese_name'])
            for cv in character['cv']
        ]
        character_list.append(GameCharacter(
            bangumi_id=character['bangumi_id'],
            japan_name=character['japan_name'],
            chinese_name=character['chinese_name'],
            job=character['job'],
            cv=character_voice_list,
        ))
    game.character = character_list
    return game
